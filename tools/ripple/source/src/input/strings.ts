import {
  INSTRUMENT_ORDER, INSTRUMENTS, SCALE_ORDER, SCALES,
  clamp, dist, midiHz, spell,
} from '../core/music';
import {
  MAX_STRINGS, MenuItem, MenuState, PlayMode, StageString, Vec2, VoiceHandle,
  createString, nowS, orient, pushHistory, stageSize, state, strLen, zoneCount, zoneInfo,
} from '../core/state';
import { audio, bendVoice, initAudio, isSustaining, playEvent, releaseVoice } from '../audio/engine';
import { captureEvent } from '../audio/sequencer';
import { telemetry } from '../audio/telemetry';

let toastFn: (msg: string, ms?: number) => void = () => {};
let uiRefreshFn: () => void = () => {};

export function setInteractionCallbacks(
  toast: (msg: string, ms?: number) => void,
  refresh: () => void,
): void {
  toastFn = toast;
  uiRefreshFn = refresh;
}

export function burst(p: Vec2, color: string, n = 10, speed = 135): void {
  for (let i = 0; i < n; i++) {
    const ang = Math.random() * Math.PI * 2;
    const sp = speed * (0.35 + Math.random() * 0.85);
    state.particles.push({
      x: p.x,
      y: p.y,
      vx: Math.cos(ang) * sp,
      vy: Math.sin(ang) * sp,
      r: 1.8 + Math.random() * 2.4,
      color,
      life: 0,
      maxLife: 0.45 + Math.random() * 0.45,
    });
  }
  if (state.particles.length > 260) {
    state.particles.splice(0, state.particles.length - 260);
  }
}

export function notePop(p: Vec2, text: string, color: string, t: number): void {
  state.pops.push({ x: p.x, y: p.y, text, color, t0: t });
  if (state.pops.length > 36) state.pops.shift();
}

export function keepVoices(s: StageString, vs: VoiceHandle[]): void {
  s.voices.push(...vs);
  if (s.voices.length > 16) s.voices.splice(0, s.voices.length - 16);
}

export function addString(
  a: Vec2,
  b: Vec2,
  opts: Partial<{ inst: string; scale: string | null; root: number | null; oct: number; mode: PlayMode; gain: number }> = {},
  recordHistory = true,
  openPalette = true,
): StageString | null {
  if (state.strings.length >= MAX_STRINGS) {
    toastFn(`Maximum ${MAX_STRINGS} strings on stage.`);
    return null;
  }
  if (recordHistory) pushHistory();
  const s = createString(a, b, opts);
  state.strings.push(s);
  state.selectedId = s.id;
  if (openPalette) openMenu(s, 'inst');
  uiRefreshFn();
  return s;
}

export function removeString(s: StageString, recordHistory = true): void {
  const idx = state.strings.indexOf(s);
  if (idx < 0) return;
  if (recordHistory) pushHistory();
  for (const pid of Object.keys(s.holds)) endHold(s, pid);
  for (const v of s.voices) releaseVoice(v);
  state.strings.splice(idx, 1);
  if (state.selectedId === s.id) {
    state.selectedId = state.strings[0]?.id ?? null;
  }
  if (state.menu?.s === s) closeMenu();
  uiRefreshFn();
}

export function clearStrings(): void {
  if (!state.strings.length) return;
  pushHistory();
  for (const s of state.strings) {
    for (const pid of Object.keys(s.holds)) endHold(s, pid);
    for (const v of s.voices) releaseVoice(v);
  }
  state.strings = [];
  state.selectedId = null;
  closeMenu();
  uiRefreshFn();
}

export function undoEdit(): boolean {
  const prev = state.undoStack.pop();
  if (!prev) return false;
  state.redoStack.push(state.strings.map(s => ({
    a: [s.a.x, s.a.y], b: [s.b.x, s.b.y],
    inst: s.inst, scale: s.scale, root: s.root, oct: s.oct, mode: s.mode, gain: s.gain,
  })));
  restoreSerialized(prev);
  toastFn('Undid string change');
  return true;
}

export function redoEdit(): boolean {
  const next = state.redoStack.pop();
  if (!next) return false;
  state.undoStack.push(state.strings.map(s => ({
    a: [s.a.x, s.a.y], b: [s.b.x, s.b.y],
    inst: s.inst, scale: s.scale, root: s.root, oct: s.oct, mode: s.mode, gain: s.gain,
  })));
  restoreSerialized(next);
  toastFn('Redid string change');
  return true;
}

function restoreSerialized(list: Array<{
  a: [number, number]; b: [number, number]; inst: string;
  scale: string | null; root: number | null; oct: number; mode: PlayMode; gain?: number;
}>): void {
  for (const s of state.strings) {
    for (const pid of Object.keys(s.holds)) endHold(s, pid);
  }
  closeMenu();
  state.strings = list.map(d => createString({ x: d.a[0], y: d.a[1] }, { x: d.b[0], y: d.b[1] }, d));
  state.selectedId = state.strings[0]?.id ?? null;
  uiRefreshFn();
}

export function pluck(s: StageString, u: number, vel: number, down = false, quiet = false): void {
  initAudio();
  if (!audio.g) return;
  const n = zoneCount(s);
  const z = clamp(Math.floor(u * n), 0, n - 1);
  const info = zoneInfo(s, z);
  const t = nowS();
  const px = s.a.x + (s.b.x - s.a.x) * u;
  const py = s.a.y + (s.b.y - s.a.y) * u;
  const pan = clamp(((s.a.x + s.b.x) * 0.5 / stageSize.w) * 2 - 1, -0.75, 0.75);
  const effectiveVel = clamp(vel * s.gain, 0.08, 1.15);

  const ev = info.drum
    ? { drum: info.drum, vel: effectiveVel, pan }
    : { inst: s.inst, notes: info.notes, vel: effectiveVel, down, pan };

  const vs = playEvent(ev, audio.g.ctx.currentTime);
  keepVoices(s, vs);
  if (!quiet) captureEvent(ev);

  const col = INSTRUMENTS[s.inst].color;
  const freqHz = info.notes.length ? midiHz(info.notes[0]) : 160;
  s.vib = { amp: clamp(6 + vel * 15, 6, 22), pos: clamp(u, 0.08, 0.92), t0: t, freqHz };
  s.flash = { z, t };
  s.touched = t;

  if (!quiet) {
    burst({ x: px, y: py }, col, Math.round(7 + vel * 9), 95 + vel * 110);
    if (state.settings.labels) notePop({ x: px, y: py - 10 }, info.label, col, t);
  }

  // Emit physically-matched wavefield impulse directly from the string segment
  if (info.drum) {
    const drumFreq = info.drum === 'kick' || info.drum === 'dum' ? 68 : info.drum === 'hat' || info.drum === 'riq' ? 950 : 280;
    telemetry.pushPointImpulse(px, py, stageSize.w, stageSize.h, drumFreq, effectiveVel, col);
  } else {
    telemetry.pushStringImpulse(s.a.x, s.a.y, s.b.x, s.b.y, stageSize.w, stageSize.h, freqHz, effectiveVel, col);
  }
}

export function pluckZone(s: StageString, z: number, vel = 0.78): void {
  const n = zoneCount(s);
  if (z < 0 || z >= n) return;
  pluck(s, (z + 0.5) / n, vel, false, false);
}

export function pluckQuiet(s: StageString): void {
  pluck(s, 0.35, 0.58, false, true);
}

export function startHold(s: StageString, pid: string, u: number): void {
  initAudio();
  if (!audio.g) return;
  endHold(s, pid);
  const n = zoneCount(s);
  const z = clamp(Math.floor(u * n), 0, n - 1);
  const sustains = isSustaining(s.inst);
  const h = { z, u, voices: [] as VoiceHandle[], nextRoll: nowS(), sustains };
  s.holds[pid] = h;
  triggerHoldZone(s, pid, h);
}

function triggerHoldZone(s: StageString, pid: string, h: StageString['holds'][string]): void {
  if (!audio.g) return;
  for (const v of h.voices) releaseVoice(v);
  h.voices = [];
  const info = zoneInfo(s, h.z);
  const t = nowS();
  const px = s.a.x + (s.b.x - s.a.x) * h.u;
  const py = s.a.y + (s.b.y - s.a.y) * h.u;
  const pan = clamp(((s.a.x + s.b.x) * 0.5 / stageSize.w) * 2 - 1, -0.75, 0.75);
  const vel = clamp(0.76 * s.gain, 0.1, 1.1);
  const col = INSTRUMENTS[s.inst].color;

  if (h.sustains && !info.drum) {
    const ev = { inst: s.inst, notes: info.notes, vel, pan };
    h.voices = playEvent(ev, audio.g.ctx.currentTime, undefined, { held: true, pan });
    captureEvent({ ...ev, holdSec: 0.75 });
    const freqHz = info.notes.length ? midiHz(info.notes[0]) : 220;
    s.vib = { amp: 10, pos: h.u, t0: t, freqHz };
    s.flash = { z: h.z, t };
    s.touched = t;
    telemetry.setEmitter(`hold:${s.id}:${pid}`, s.a.x, s.a.y, s.b.x, s.b.y, stageSize.w, stageSize.h, freqHz, vel, col);
    if (state.settings.labels) notePop({ x: px, y: py - 10 }, info.label, col, t);
  } else {
    pluck(s, h.u, 0.74, false, false);
    h.nextRoll = t + 0.115;
  }
}

export function moveHold(s: StageString, pid: string, u: number): void {
  const h = s.holds[pid];
  if (!h) return;
  const n = zoneCount(s);
  const z = clamp(Math.floor(u * n), 0, n - 1);
  h.u = clamp(u, 0.02, 0.98);
  if (z !== h.z) {
    h.z = z;
    triggerHoldZone(s, pid, h);
  }
}

export function updateHolds(t: number): void {
  for (const s of state.strings) {
    for (const pid of Object.keys(s.holds)) {
      const h = s.holds[pid];
      if (!h.sustains && t >= h.nextRoll) {
        pluck(s, h.u, 0.68, false, false);
        h.nextRoll = t + 0.115;
      }
    }
  }
}

export function endHold(s: StageString, pid: string): void {
  const h = s.holds[pid];
  if (!h) return;
  for (const v of h.voices) releaseVoice(v);
  delete s.holds[pid];
  telemetry.removeEmitter(`hold:${s.id}:${pid}`);
}

export function projectOnString(p: Vec2, s: StageString): { u: number; side: number; dist: number } {
  const dx = s.b.x - s.a.x, dy = s.b.y - s.a.y;
  const L = Math.hypot(dx, dy) || 1;
  const u = ((p.x - s.a.x) * dx + (p.y - s.a.y) * dy) / (L * L);
  const side = ((p.x - s.a.x) * (-dy) + (p.y - s.a.y) * dx) / L;
  const cu = clamp(u, 0, 1);
  const d = Math.hypot(p.x - (s.a.x + dx * cu), p.y - (s.a.y + dy * cu));
  return { u, side, dist: d };
}

export function sweepPointer(pid: string, p: Vec2, t: number): void {
  for (const s of state.strings) {
    const pr = projectOnString(p, s);
    s.near = pr.dist < 32 && pr.u >= -0.05 && pr.u <= 1.05;
    const prev = s.track[pid];
    s.track[pid] = { side: pr.side, x: p.x, y: p.y, t };
    if (!prev) continue;
    if (pr.u < 0.01 || pr.u > 0.99) continue;
    // Detect crossing across the string line
    if ((prev.side > 0 && pr.side <= 0) || (prev.side < 0 && pr.side >= 0)) {
      if (Math.abs(prev.side) < 75 && Math.abs(pr.side) < 75) {
        const dt = Math.max(0.008, t - prev.t);
        const speed = Math.hypot(p.x - prev.x, p.y - prev.y) / dt;
        const vel = clamp(0.28 + speed / 1500, 0.25, 1.0);
        const down = p.y > prev.y;
        pluck(s, pr.u, vel, down, false);
        state.selectedId = s.id;
      }
    }
  }
}

export function forgetPointer(pid: string): void {
  for (const s of state.strings) {
    delete s.track[pid];
  }
}

export function pullString(s: StageString, u: number, p: Vec2): void {
  const dx = s.b.x - s.a.x, dy = s.b.y - s.a.y;
  const L = Math.hypot(dx, dy) || 1;
  const d = clamp(((p.x - s.a.x) * (dy / L) - (p.y - s.a.y) * (dx / L)), -85, 85);
  s.pull = { u: clamp(u, 0.08, 0.92), d };
  const cents = clamp((Math.abs(d) / 85) * 200 * (d >= 0 ? 1 : -1), -200, 200);
  s.bend = cents;
  for (const v of s.voices) bendVoice(v, cents);
  s.touched = nowS();
}

export function releasePull(s: StageString): void {
  if (!s.pull) return;
  const { u, d } = s.pull;
  s.pull = null;
  s.bend = 0;
  for (const v of s.voices) bendVoice(v, 0, 0.03);
  if (Math.abs(d) > 8) {
    pluck(s, u, clamp(0.35 + Math.abs(d) / 95, 0.35, 1.0), d > 0, false);
  }
}

export function nearestEndpoint(p: Vec2, r = 16): { s: StageString; end: 'a' | 'b' } | null {
  let best: { s: StageString; end: 'a' | 'b'; d: number } | null = null;
  for (const s of state.strings) {
    for (const end of ['a', 'b'] as const) {
      const d = dist(p, s[end]);
      if (d <= r && (!best || d < best.d)) best = { s, end, d };
    }
  }
  return best ? { s: best.s, end: best.end } : null;
}

export function nearestBadge(p: Vec2, r = 18): StageString | null {
  let best: { s: StageString; d: number } | null = null;
  for (const s of state.strings) {
    const mid = { x: (s.a.x + s.b.x) * 0.5, y: (s.a.y + s.b.y) * 0.5 };
    const d = dist(p, mid);
    if (d <= r && (!best || d < best.d)) best = { s, d };
  }
  return best ? best.s : null;
}

export function nearestBody(p: Vec2, r = 11): { s: StageString; u: number } | null {
  let best: { s: StageString; u: number; d: number } | null = null;
  for (const s of state.strings) {
    const pr = projectOnString(p, s);
    if (pr.dist <= r && pr.u > 0.06 && pr.u < 0.94) {
      const mid = { x: (s.a.x + s.b.x) * 0.5, y: (s.a.y + s.b.y) * 0.5 };
      if (dist(p, mid) < 20) continue;
      if (!best || pr.dist < best.d) best = { s, u: pr.u, d: pr.dist };
    }
  }
  return best ? { s: best.s, u: best.u } : null;
}

// ───────────────────────── Radial & Grid String Menu ─────────────────────────
export function openMenu(s: StageString, kind: MenuState['kind']): void {
  const mx = (s.a.x + s.b.x) * 0.5;
  const my = (s.a.y + s.b.y) * 0.5;
  const items: MenuItem[] = [];
  const col = INSTRUMENTS[s.inst].color;
  const isPerc = !!INSTRUMENTS[s.inst].kit;

  let cx = clamp(mx, 140, stageSize.w - 140);
  let cy = clamp(my, state.safeTop + 115, state.safeBottom - 115);

  if (kind === 'hub') {
    const entries: Array<{ id: string; label: string; sub?: string; color?: string; kind: MenuItem['kind']; value?: string }> = [
      { id: 'inst', label: 'Instrument', sub: INSTRUMENTS[s.inst].name, color: col, kind: 'hub', value: 'inst' },
      ...(isPerc ? [] : [
        { id: 'scale', label: 'Scale', sub: s.scale ? SCALES[s.scale].short : 'Stage', color: '#9eeaff', kind: 'hub' as const, value: 'scale' },
        { id: 'key',   label: 'Key',   sub: s.root != null ? spell(s.root, s.root, 'minor') : 'Stage', color: '#ffd166', kind: 'hub' as const, value: 'key' },
        { id: 'oct',   label: 'Octave', sub: s.oct === 0 ? '0' : (s.oct > 0 ? `+${s.oct}` : `${s.oct}`), color: '#8ff0c0', kind: 'hub' as const, value: 'oct' },
        { id: 'mode',  label: 'Voicing', sub: s.mode, color: '#d4c5ff', kind: 'hub' as const, value: 'mode' },
      ]),
      { id: 'del', label: 'Delete', color: '#ff6b7a', kind: 'action', value: 'delete' },
    ];
    const R = 76;
    entries.forEach((e, i) => {
      const ang = -Math.PI * 0.5 + (i / entries.length) * Math.PI * 2;
      items.push({
        ...e,
        x: cx + Math.cos(ang) * R,
        y: cy + Math.sin(ang) * R,
        w: 62, h: 62, r: 31,
      });
    });
  } else if (kind === 'inst') {
    const cols = 6, cw = 96, ch = 54, gap = 7;
    const rows = Math.ceil(INSTRUMENT_ORDER.length / cols);
    const totalW = cols * cw + (cols - 1) * gap;
    const totalH = rows * ch + (rows - 1) * gap;
    cx = clamp(mx, totalW * 0.5 + 26, stageSize.w - totalW * 0.5 - 26);
    cy = clamp(my, state.safeTop + totalH * 0.5 + 48, state.safeBottom - totalH * 0.5 - 26);
    INSTRUMENT_ORDER.forEach((id, i) => {
      const c = i % cols, r = Math.floor(i / cols);
      const inst = INSTRUMENTS[id];
      items.push({
        id: 'inst:' + id,
        label: inst.name,
        color: inst.color,
        active: s.inst === id,
        kind: 'inst',
        value: id,
        x: cx - totalW * 0.5 + c * (cw + gap) + cw * 0.5,
        y: cy - totalH * 0.5 + r * (ch + gap) + ch * 0.5,
        w: cw, h: ch,
      });
    });
  } else if (kind === 'scale') {
    const list: Array<{ id: string | null; label: string }> = [
      { id: null, label: 'Follow Stage' },
      ...SCALE_ORDER.map(id => ({ id, label: SCALES[id].name })),
    ];
    const cols = 3, cw = 132, ch = 40, gap = 7;
    const rows = Math.ceil(list.length / cols);
    const totalW = cols * cw + (cols - 1) * gap;
    const totalH = rows * ch + (rows - 1) * gap;
    cx = clamp(mx, totalW * 0.5 + 26, stageSize.w - totalW * 0.5 - 26);
    cy = clamp(my, state.safeTop + totalH * 0.5 + 48, state.safeBottom - totalH * 0.5 - 26);
    list.forEach((entry, i) => {
      const c = i % cols, r = Math.floor(i / cols);
      items.push({
        id: 'sc:' + (entry.id ?? 'stage'),
        label: entry.label,
        color: '#9eeaff',
        active: s.scale === entry.id,
        kind: 'scale',
        value: entry.id ?? '',
        x: cx - totalW * 0.5 + c * (cw + gap) + cw * 0.5,
        y: cy - totalH * 0.5 + r * (ch + gap) + ch * 0.5,
        w: cw, h: ch,
      });
    });
  } else if (kind === 'key') {
    const list: Array<{ v: number; label: string }> = [
      { v: -1, label: 'Stage' },
      ...Array.from({ length: 12 }, (_, k) => ({ v: k, label: spell(k, k, 'minor') })),
    ];
    const cols = 4, cw = 76, ch = 40, gap = 7;
    const rows = Math.ceil(list.length / cols);
    const totalW = cols * cw + (cols - 1) * gap;
    const totalH = rows * ch + (rows - 1) * gap;
    cx = clamp(mx, totalW * 0.5 + 26, stageSize.w - totalW * 0.5 - 26);
    cy = clamp(my, state.safeTop + totalH * 0.5 + 48, state.safeBottom - totalH * 0.5 - 26);
    list.forEach((entry, i) => {
      const c = i % cols, r = Math.floor(i / cols);
      items.push({
        id: 'key:' + entry.v,
        label: entry.label,
        color: '#ffd166',
        active: (entry.v === -1 && s.root == null) || s.root === entry.v,
        kind: 'key',
        value: entry.v,
        x: cx - totalW * 0.5 + c * (cw + gap) + cw * 0.5,
        y: cy - totalH * 0.5 + r * (ch + gap) + ch * 0.5,
        w: cw, h: ch,
      });
    });
  } else if (kind === 'oct') {
    const vals = [-2, -1, 0, 1, 2];
    const cw = 68, ch = 46, gap = 8;
    const totalW = vals.length * cw + (vals.length - 1) * gap;
    cx = clamp(mx, totalW * 0.5 + 26, stageSize.w - totalW * 0.5 - 26);
    cy = clamp(my, state.safeTop + 70, state.safeBottom - 50);
    vals.forEach((v, i) => {
      items.push({
        id: 'oct:' + v,
        label: v === 0 ? '0' : (v > 0 ? `+${v}` : `${v}`),
        sub: 'oct',
        color: '#8ff0c0',
        active: s.oct === v,
        kind: 'oct',
        value: v,
        x: cx - totalW * 0.5 + i * (cw + gap) + cw * 0.5,
        y: cy,
        w: cw, h: ch,
      });
    });
  } else if (kind === 'mode') {
    const modes: Array<{ v: PlayMode; label: string; sub: string }> = [
      { v: 'notes', label: 'Single', sub: '1 note' },
      { v: 'power', label: 'Power',  sub: 'Root + 5th' },
      { v: 'chord', label: 'Triad',  sub: '3-note chord' },
      { v: 'lush',  label: 'Lush 7th', sub: '4-note chord' },
    ];
    const cw = 104, ch = 50, gap = 8;
    const totalW = modes.length * cw + (modes.length - 1) * gap;
    cx = clamp(mx, totalW * 0.5 + 26, stageSize.w - totalW * 0.5 - 26);
    cy = clamp(my, state.safeTop + 70, state.safeBottom - 50);
    modes.forEach((m, i) => {
      items.push({
        id: 'mode:' + m.v,
        label: m.label,
        sub: m.sub,
        color: '#d4c5ff',
        active: s.mode === m.v,
        kind: 'mode',
        value: m.v,
        x: cx - totalW * 0.5 + i * (cw + gap) + cw * 0.5,
        y: cy,
        w: cw, h: ch,
      });
    });
  }

  state.menu = { s, kind, cx, cy, items, hover: null, openedAt: nowS() };
}

export function closeMenu(): void {
  state.menu = null;
}

export function hitMenuItem(p: Vec2): MenuItem | null {
  const M = state.menu;
  if (!M) return null;
  for (const it of M.items) {
    if (it.r) {
      if (dist(p, { x: it.x, y: it.y }) <= it.r + 4) return it;
    } else {
      if (Math.abs(p.x - it.x) <= it.w * 0.5 + 2 && Math.abs(p.y - it.y) <= it.h * 0.5 + 2) return it;
    }
  }
  return null;
}

export function chooseMenuItem(it: MenuItem): void {
  const M = state.menu;
  if (!M) return;
  const s = M.s;
  if (it.kind === 'hub' && typeof it.value === 'string') {
    openMenu(s, it.value as MenuState['kind']);
    return;
  }
  if (it.kind === 'action' && it.value === 'delete') {
    removeString(s);
    return;
  }
  pushHistory();
  if (it.kind === 'inst' && typeof it.value === 'string') {
    s.inst = it.value;
    s.touched = nowS();
    closeMenu();
    pluckQuiet(s);
    return;
  }
  if (it.kind === 'scale') {
    s.scale = it.value ? String(it.value) : null;
    s.touched = nowS();
    closeMenu();
    pluckQuiet(s);
    return;
  }
  if (it.kind === 'key') {
    const v = Number(it.value);
    s.root = v < 0 ? null : v;
    s.touched = nowS();
    closeMenu();
    pluckQuiet(s);
    return;
  }
  if (it.kind === 'oct') {
    s.oct = clamp(Number(it.value), -2, 2);
    s.touched = nowS();
    closeMenu();
    pluckQuiet(s);
    return;
  }
  if (it.kind === 'mode') {
    s.mode = it.value as PlayMode;
    s.touched = nowS();
    closeMenu();
    pluckQuiet(s);
    return;
  }
}

export function updateStringOrient(s: StageString): void {
  orient(s);
  if (strLen(s) < 40) removeString(s);
}
