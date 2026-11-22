import { BEATS, BeatPart, INSTRUMENTS, PARTS, PROGS, SCALES, clamp, midiHz, scaleDegree } from '../core/music';
import { LoopEvent, LoopLayer, MAX_LAYERS, stageSize, state, stepDur, transport } from '../core/state';
import { AudioGraph, audio, initAudio, playDrum, playEvent, playNote } from './engine';
import { telemetry } from './telemetry';

let onUiDirty: (() => void) | null = null;
export function setSequencerUiCallback(cb: () => void): void {
  onUiDirty = cb;
}

export function layerOut(L: LoopLayer, graph?: AudioGraph): AudioNode {
  const g = graph ?? audio.g!;
  if (!graph && L.gainNode) return L.gainNode;
  const gn = g.ctx.createGain();
  gn.gain.value = L.vol;
  gn.connect(g.live);
  if (!graph) L.gainNode = gn;
  return gn;
}

export function makeLayer(d: {
  len: number;
  offset: number;
  events: LoopEvent[];
  vol?: number;
  muted?: boolean;
  id?: number;
}): LoopLayer {
  const buckets: Record<number, LoopEvent[]> = {};
  for (const ev of d.events) {
    const p = ((Math.floor(ev.pos) % d.len) + d.len) % d.len;
    (buckets[p] ||= []).push(ev);
  }
  const L: LoopLayer = {
    id: d.id ?? transport.nextLayerId++,
    len: d.len,
    offset: d.offset,
    vol: clamp(d.vol ?? 0.85, 0, 1.4),
    muted: !!d.muted,
    events: d.events,
    buckets,
  };
  return L;
}

export function removeLayer(id: number): void {
  const idx = transport.layers.findIndex(L => L.id === id);
  if (idx < 0) return;
  const [L] = transport.layers.splice(idx, 1);
  if (L.gainNode) {
    try { L.gainNode.disconnect(); } catch { /* ignore */ }
  }
  onUiDirty?.();
}

export function undoLayer(): boolean {
  if (!transport.layers.length) return false;
  const last = transport.layers[transport.layers.length - 1];
  removeLayer(last.id);
  return true;
}

export interface OfflineScheduleOpts {
  parts: Record<BeatPart, boolean>;
  layers: LoopLayer[];
  dest: (L: LoopLayer) => AudioNode;
  beatDest: AudioNode;
  graph: AudioGraph;
}

export function scheduleStep(step: number, t: number, o?: OfflineScheduleOpts): void {
  const live = !o;
  const g = o ? o.graph : audio.g;
  if (!g) return;
  const B = BEATS[transport.beat];
  const P = o ? o.parts : transport.parts;
  const bar = Math.floor(step / 16);
  const s = step % 16;
  const pick = (arr: string[]) => arr[bar % arr.length][s];
  const beatDest = o ? o.beatDest : g.beat;
  const swingShift = s % 2 === 1 ? B.swing * stepDur() : 0;
  const tPlay = t + swingShift;

  if (P.kick) {
    const c = pick(B.kick);
    if (c !== '-') {
      const vel = c === 'X' ? 0.95 : 0.7;
      playDrum(B.kickAs || 'kick', tPlay, vel, beatDest, { graph: g });
      if (live) {
        telemetry.pushPointImpulse(stageSize.w * 0.5, stageSize.h * 0.82, stageSize.w, stageSize.h, 62, vel * 0.55, '#6aa6ff');
      }
    }
  }
  if (P.snare) {
    const c = pick(B.snare);
    if (c !== '-') {
      const vel = c === 'X' ? 0.9 : 0.65;
      playDrum(B.snareAs || 'snare', tPlay, vel, beatDest, { graph: g });
      if (live) {
        telemetry.pushPointImpulse(stageSize.w * 0.5, stageSize.h * 0.26, stageSize.w, stageSize.h, 480, vel * 0.35, '#ffd166');
      }
    }
  }
  if (P.hats) {
    const c = pick(B.hats);
    if (c !== '-') {
      playDrum(c === 'o' ? 'ohat' : (B.hatAs || 'hat'), tPlay, s % 4 === 0 ? 0.72 : 0.45, beatDest, { graph: g });
    }
  }

  const parent = SCALES[state.scale].parent;
  const deg = PROGS[parent][bar % 4];
  if (P.bass) {
    const c = pick(B.bass);
    if (c !== '-') {
      const addMap: Record<string, number> = { '0': 0, '3': 2, '5': 4, '8': 7 };
      const add = addMap[c] ?? 0;
      let m = scaleDegree(parent, state.key, 1, deg + add);
      while (m > 52) m -= 12;
      playNote(B.bassInst, m, tPlay, 0.82, beatDest, 1, { graph: g });
      if (live) {
        telemetry.pushPointImpulse(stageSize.w * 0.28, stageSize.h * 0.75, stageSize.w, stageSize.h, midiHz(m), 0.42, '#7aa8ff');
      }
    }
  }

  if (P.chords) {
    const c = pick(B.chords);
    if (c !== '-') {
      const tones = B.seventh ? [0, 2, 4, 6] : [0, 2, 4];
      tones.forEach((k, i) => {
        let m = scaleDegree(parent, state.key, 3, deg + k);
        while (m > 76) m -= 12;
        playNote(B.chordInst, m, tPlay + i * 0.012, 0.38, beatDest, B.chordLen, { graph: g });
      });
      if (live) {
        const col = INSTRUMENTS[B.chordInst]?.color || '#a78bfa';
        telemetry.pushStringImpulse(
          stageSize.w * 0.25, stageSize.h * 0.5,
          stageSize.w * 0.75, stageSize.h * 0.5,
          stageSize.w, stageSize.h, 280, 0.28, col,
        );
      }
    }
  }

  // Play recorded loop layers
  const layerList = o ? o.layers : transport.layers;
  for (const L of layerList) {
    if (live && L.muted) continue;
    const p = (((step - L.offset) % L.len) + L.len) % L.len;
    const evs = L.buckets[p];
    if (evs) {
      for (const ev of evs) {
        playEvent(ev, tPlay + (ev.pos - p) * stepDur(), o ? o.dest(L) : layerOut(L), { graph: g });
        if (live && ev.notes?.length) {
          const xNorm = clamp(0.5 + (ev.pan ?? 0) * 0.5, 0.15, 0.85);
          const col = INSTRUMENTS[ev.inst || 'harp']?.color || '#8ff0c0';
          telemetry.pushPointImpulse(
            stageSize.w * xNorm, stageSize.h * 0.48,
            stageSize.w, stageSize.h, midiHz(ev.notes[0]), ev.vel * 0.45, col,
          );
        }
      }
    }
  }

  if (!live) return;

  // Handle active loop layer recording
  const R = transport.rec;
  if (R) {
    if (step >= R.start - 16 && step < R.start && s % 4 === 0) {
      playDrum('tick', tPlay, s === 0 ? 0.85 : 0.5, g.beat, { graph: g });
    }
    if (step === R.start) {
      R.state = 'rec';
      onUiDirty?.();
    }
    if (step === R.start + R.len) {
      finishLayer();
    }
  }
  transport.lastStep = step;
  transport.lastStepTime = t;
}

function tick(): void {
  if (!transport.playing || !audio.g) return;
  const ctx = audio.g.ctx;
  const ahead = 0.12;
  while (transport.stepTime < ctx.currentTime + ahead) {
    scheduleStep(transport.step, transport.stepTime);
    transport.step++;
    transport.stepTime += stepDur();
  }
}

export function ensureDefaultParts(): void {
  const anyPart = PARTS.some(p => transport.parts[p]);
  const anyLayer = transport.layers.some(L => !L.muted && L.events.length > 0);
  if (!anyPart && !anyLayer) {
    transport.parts.kick = true;
    transport.parts.snare = true;
    transport.parts.hats = true;
    transport.parts.bass = true;
  }
}

export function startTransport(autoEnableParts = true): void {
  const g = initAudio();
  if (!g || transport.playing) return;
  if (autoEnableParts) ensureDefaultParts();
  transport.playing = true;
  transport.step = 0;
  transport.lastStep = -1;
  transport.stepTime = g.ctx.currentTime + 0.08;
  transport.timer = window.setInterval(tick, 24);
  tick();
  onUiDirty?.();
}

export function stopTransport(): void {
  transport.playing = false;
  if (transport.timer != null) {
    clearInterval(transport.timer);
    transport.timer = null;
  }
  if (transport.rec) {
    transport.rec = null;
  }
  onUiDirty?.();
}

export function togglePlay(): void {
  if (transport.playing) stopTransport();
  else startTransport();
}

export function setBeat(id: string): void {
  if (!BEATS[id]) return;
  transport.beat = id;
  transport.bpm = BEATS[id].bpm;
  onUiDirty?.();
}

export function stepAt(time: number): number {
  return transport.lastStep + (time - transport.lastStepTime) / stepDur();
}

export function armLayer(): string | null {
  if (transport.rec) {
    transport.rec = null;
    onUiDirty?.();
    return 'Layer recording cancelled.';
  }
  if (transport.layers.length >= MAX_LAYERS) {
    return `Maximum ${MAX_LAYERS} loop layers reached.`;
  }
  initAudio();
  if (!transport.playing) startTransport(false);
  const nextBar = Math.ceil((transport.step + 4) / 16) * 16;
  const start = nextBar + 16; // 1 bar count-in
  const len = transport.loopBars * 16;
  transport.rec = { state: 'count', start, len, offset: start, events: [] };
  onUiDirty?.();
  return null;
}

export function captureEvent(ev: Omit<LoopEvent, 'pos'>): void {
  const R = transport.rec;
  if (!R || R.state !== 'rec' || !audio.g) return;
  let pos = stepAt(audio.g.ctx.currentTime) - R.start;
  if (state.settings.quantize) pos = Math.round(pos * 2) / 2;
  pos = ((pos % R.len) + R.len) % R.len;
  R.events.push({ ...ev, pos });
}

export function finishLayer(): void {
  const R = transport.rec;
  transport.rec = null;
  if (!R) return;
  if (R.events.length > 0) {
    const L = makeLayer({ len: R.len, offset: R.offset, events: R.events, vol: 0.85, muted: false });
    transport.layers.push(L);
  }
  onUiDirty?.();
}
