import {
  BEATS, BeatPart, INSTRUMENTS, PARTS, PROGS, SCALES,
  clamp, dist, own, scaleDegree, spell,
} from './music';

export type PlayMode = 'notes' | 'power' | 'chord' | 'lush';
export type ThemeId = 'obsidian' | 'cymatic' | 'warm';
export type StrumMode = 'hover' | 'click';
export type StageShape = 'landscape' | 'vertical';

export interface Vec2 {
  x: number;
  y: number;
}

export interface VoiceHandle {
  srcs: AudioScheduledSourceNode[];
  gate: GainNode | null;
  t: number;
}

export interface HoldState {
  z: number;
  u: number;
  voices: VoiceHandle[];
  nextRoll: number;
  sustains: boolean;
}

export interface StageString {
  id: number;
  a: Vec2;
  b: Vec2;
  inst: string;
  scale: string | null;
  root: number | null;
  oct: number;
  mode: PlayMode;
  gain: number;
  born: number;
  touched: number;
  near: boolean;
  vib: { amp: number; pos: number; t0: number; freqHz: number };
  flash: { z: number; t: number };
  pull: { u: number; d: number } | null;
  bend: number;
  voices: VoiceHandle[];
  holds: Record<string, HoldState>;
  track: Record<string, { side: number; x: number; y: number; t: number }>;
}

export interface LoopEvent {
  pos: number;
  inst?: string;
  drum?: string;
  notes?: number[];
  vel: number;
  down?: boolean;
  pan?: number;
  holdSec?: number;
}

export interface LoopLayer {
  id: number;
  len: number;
  offset: number;
  vol: number;
  muted: boolean;
  events: LoopEvent[];
  buckets: Record<number, LoopEvent[]>;
  gainNode?: GainNode;
}

export interface Particle {
  x: number;
  y: number;
  vx: number;
  vy: number;
  r: number;
  color: string;
  life: number;
  maxLife: number;
}

export interface NotePop {
  x: number;
  y: number;
  text: string;
  color: string;
  t0: number;
}

export interface MenuItem {
  id: string;
  label: string;
  sub?: string;
  color?: string;
  active?: boolean;
  kind: 'hub' | 'inst' | 'scale' | 'key' | 'oct' | 'mode' | 'action';
  value?: string | number;
  x: number;
  y: number;
  w: number;
  h: number;
  r?: number;
}

export interface MenuState {
  s: StageString;
  kind: 'hub' | 'inst' | 'scale' | 'key' | 'oct' | 'mode';
  cx: number;
  cy: number;
  items: MenuItem[];
  hover: string | null;
  openedAt: number;
}

export interface FxPadState {
  from: Vec2;
  to: Vec2;
  dark: number;
  thin: number;
  echo: number;
}

export interface SerializedString {
  a: [number, number];
  b: [number, number];
  inst: string;
  scale: string | null;
  root: number | null;
  oct: number;
  mode: PlayMode;
  gain?: number;
}

export interface StageSetup {
  v: number;
  name: string;
  saved?: number;
  w: number;
  h: number;
  shape?: StageShape;
  key: number;
  scale: string;
  beat: string;
  bpm: number;
  loopBars: number;
  follow: boolean;
  parts: Record<BeatPart, boolean>;
  strings: SerializedString[];
  layers: Array<{ len: number; offset: number; vol: number; muted: boolean; events: LoopEvent[] }>;
}

export const MAX_STRINGS = 12;
export const MAX_LAYERS = 8;
export const SETUP_STORE = 'resonance-setups-v1';

export const stageSize = { w: 1280, h: 720 };

export const state = {
  key: 9, // A
  scale: 'pentamin',
  strings: [] as StageString[],
  selectedId: null as number | null,
  nextStringId: 1,
  menu: null as MenuState | null,
  preview: null as { a: Vec2; b: Vec2; snapped?: boolean } | null,
  fx: null as FxPadState | null,
  shape: 'landscape' as StageShape,
  particles: [] as Particle[],
  pops: [] as NotePop[],
  mouse: {
    x: -1, y: -1, px: -1, py: -1,
    down: false, rightDown: false, inside: false,
    speed: 0, overHud: false,
    drag: null as null | {
      type: 'new' | 'end' | 'move' | 'grab' | 'fx' | 'bow' | 'dot' | 'strum';
      from?: Vec2;
      s?: StageString;
      end?: 'a' | 'b';
      u?: number;
      origA?: Vec2;
      origB?: Vec2;
    },
  },
  safeTop: 64,
  safeBottom: 610,
  fps: 60,
  mix: { live: 0.88, beat: 0.78 },
  settings: {
    strumMode: 'hover' as StrumMode,
    theme: 'obsidian' as ThemeId,
    waveIntensity: 0.75,
    reverb: 0.42,
    labels: true,
    quantize: true,
    volume: 0.9,
  },
  undoStack: [] as SerializedString[][],
  redoStack: [] as SerializedString[][],
  clean: false,
};

export const transport = {
  playing: false,
  beat: 'lofi',
  bpm: 76,
  parts: { kick: false, snare: false, hats: false, bass: false, chords: false } as Record<BeatPart, boolean>,
  step: 0,
  stepTime: 0,
  lastStep: -1,
  lastStepTime: 0,
  timer: null as number | null,
  loopBars: 2,
  layers: [] as LoopLayer[],
  rec: null as null | { state: 'count' | 'rec'; start: number; len: number; offset: number; events: LoopEvent[] },
  nextLayerId: 1,
  follow: false,
  dirty: false,
};

export function nowS(): number {
  return performance.now() / 1000;
}

export function stepDur(): number {
  return 60 / transport.bpm / 4;
}

export function strLen(s: StageString): number {
  return dist(s.a, s.b);
}

export function orient(s: StageString): void {
  const dx = s.b.x - s.a.x, dy = s.b.y - s.a.y;
  const steep = Math.abs(dy) > Math.abs(dx) * 1.4;
  if (steep ? s.a.y < s.b.y : s.a.x > s.b.x) {
    const tmp = s.a;
    s.a = s.b;
    s.b = tmp;
  }
}

export function chordDegNow(): number | null {
  if (!transport.playing || !transport.follow || transport.lastStep < 0) return null;
  const parent = SCALES[state.scale].parent;
  const bar = Math.floor(transport.lastStep / 16);
  return PROGS[parent][bar % 4];
}

export function chordLabel(deg: number): string {
  const sc = SCALES[state.scale];
  const rootMidi = scaleDegree(sc.parent, state.key, 3, deg);
  const thirdMidi = scaleDegree(sc.parent, state.key, 3, deg + 2);
  const fifthMidi = scaleDegree(sc.parent, state.key, 3, deg + 4);
  const i3 = (thirdMidi - rootMidi + 12) % 12;
  const i5 = (fifthMidi - rootMidi + 12) % 12;
  const name = spell(rootMidi % 12, state.key, sc.parent);
  if (i3 === 3 && i5 === 6) return name + '°';
  if (i3 === 3) return name + 'm';
  return name;
}

export function zoneCount(s: StageString): number {
  const inst = INSTRUMENTS[s.inst];
  if (inst?.kit) return inst.kit.length;
  return clamp(Math.round(strLen(s) / 68), 5, 14);
}

export interface ZoneInfo {
  drum?: string;
  notes: number[];
  label: string;
}

export function zoneInfo(s: StageString, z: number): ZoneInfo {
  const inst = INSTRUMENTS[s.inst];
  if (inst?.kit) {
    const item = inst.kit[clamp(z, 0, inst.kit.length - 1)];
    return { drum: item.id, notes: [], label: item.label };
  }
  const scId = s.scale && own(SCALES, s.scale) ? s.scale : state.scale;
  const sc = SCALES[scId];
  const root = s.root != null ? s.root : state.key;
  const baseOct = clamp(inst.oct + s.oct, 1, 6);
  const followDeg = chordDegNow();

  if (followDeg != null && s.root == null) {
    const parent = SCALES[state.scale].parent;
    const chordSteps = [0, 2, 4, 6];
    const chordTone = chordSteps[z % chordSteps.length];
    const octShift = Math.floor(z / chordSteps.length);
    const midi = scaleDegree(parent, state.key, baseOct + octShift, followDeg + chordTone);
    const lbl = spell(midi % 12, state.key, parent);
    if (s.mode === 'power') {
      return { notes: [midi, midi + 7], label: lbl + '5' };
    }
    if (s.mode === 'chord' || s.mode === 'lush') {
      const m3 = scaleDegree(parent, state.key, baseOct + octShift, followDeg + chordTone + 2);
      const m5 = scaleDegree(parent, state.key, baseOct + octShift, followDeg + chordTone + 4);
      const arr = s.mode === 'lush'
        ? [midi, m3, m5, scaleDegree(parent, state.key, baseOct + octShift, followDeg + chordTone + 6)]
        : [midi, m3, m5];
      return { notes: arr, label: lbl + (s.mode === 'lush' ? '7' : '') };
    }
    return { notes: [midi], label: lbl };
  }

  const steps = sc.steps;
  const deg = z;
  const octOff = Math.floor(deg / steps.length);
  const stepIdx = ((deg % steps.length) + steps.length) % steps.length;
  const midi = 12 * (baseOct + octOff + 1) + root + steps[stepIdx];
  const lbl = spell(midi % 12, root, sc.parent);

  if (s.mode === 'power') {
    return { notes: [midi, midi + 7], label: lbl + '5' };
  }
  if (s.mode === 'chord' || s.mode === 'lush') {
    const at = (d: number) => {
      const o = Math.floor(d / steps.length);
      const idx = ((d % steps.length) + steps.length) % steps.length;
      return 12 * (baseOct + o + 1) + root + steps[idx];
    };
    const m3 = at(deg + 2);
    const m5 = at(deg + 4);
    const isMinor = ((m3 - midi) % 12) === 3;
    const notes = s.mode === 'lush' ? [midi, m3, m5, at(deg + 6)] : [midi, m3, m5];
    const suffix = s.mode === 'lush' ? (isMinor ? 'm7' : 'maj7') : (isMinor ? 'm' : '');
    return { notes, label: lbl + suffix };
  }
  return { notes: [midi], label: lbl };
}

export function stringLabel(s: StageString): string {
  const inst = INSTRUMENTS[s.inst];
  if (inst?.kit) return inst.name;
  const bits = [inst.name];
  if (s.scale) bits.push(SCALES[s.scale].short);
  if (s.root != null) bits.push(spell(s.root, s.root, SCALES[s.scale || state.scale].parent));
  if (s.oct > 0) bits.push(`+${s.oct} oct`);
  if (s.oct < 0) bits.push(`${s.oct} oct`);
  if (s.mode !== 'notes') bits.push(s.mode);
  return bits.join(' · ');
}

export function serializeStrings(): SerializedString[] {
  const r = (v: number) => Math.round(v * 10) / 10;
  return state.strings.map(s => ({
    a: [r(s.a.x), r(s.a.y)],
    b: [r(s.b.x), r(s.b.y)],
    inst: s.inst,
    scale: s.scale,
    root: s.root,
    oct: s.oct,
    mode: s.mode,
    gain: Math.round(s.gain * 100) / 100,
  }));
}

export function pushHistory(): void {
  state.undoStack.push(serializeStrings());
  if (state.undoStack.length > 30) state.undoStack.shift();
  state.redoStack.length = 0;
}

export function createString(
  a: Vec2,
  b: Vec2,
  opts: Partial<{ inst: string; scale: string | null; root: number | null; oct: number; mode: PlayMode; gain: number }> = {},
): StageString {
  const t = nowS();
  const s: StageString = {
    id: state.nextStringId++,
    a: { x: a.x, y: a.y },
    b: { x: b.x, y: b.y },
    inst: opts.inst && own(INSTRUMENTS, opts.inst) ? opts.inst : 'harp',
    scale: opts.scale && own(SCALES, opts.scale) ? opts.scale : null,
    root: opts.root != null ? ((opts.root % 12) + 12) % 12 : null,
    oct: clamp(opts.oct ?? 0, -2, 2),
    mode: opts.mode ?? 'notes',
    gain: clamp(opts.gain ?? 1, 0.2, 1.5),
    born: t,
    touched: t,
    near: false,
    vib: { amp: 0, pos: 0.5, t0: -10, freqHz: 220 },
    flash: { z: -1, t: -10 },
    pull: null,
    bend: 0,
    voices: [],
    holds: {},
    track: {},
  };
  orient(s);
  return s;
}

export interface StarterPreset {
  id: string;
  name: string;
  note: string;
  key: number;
  scale: string;
  beat: string;
  bpm: number;
  parts: BeatPart[];
  strings: Array<[number, number, number, number, string, string | null, number, PlayMode?]>;
}

export const STARTERS: StarterPreset[] = [
  {
    id: 'resonance',
    name: 'Ripple Harp',
    note: 'Harp melody, crystal singing bowl, lush chords and warm bass',
    key: 9, scale: 'pentamin', beat: 'lofi', bpm: 76, parts: [],
    strings: [
      [210, 185, 1070, 165, 'harp', null, 0, 'notes'],
      [240, 295, 1040, 285, 'crystal', null, 0, 'notes'],
      [220, 405, 760, 415, 'pad', 'minor', 0, 'lush'],
      [810, 415, 1080, 395, 'celesta', null, 0, 'notes'],
      [300, 520, 980, 520, 'bass', null, 0, 'notes'],
    ],
  },
  {
    id: 'zen',
    name: 'Zen Koto & Water',
    note: 'Japanese Hirajoshi scale with Koto, Flute, Crystal bowl and Hand drums',
    key: 2, scale: 'hirajoshi', beat: 'lofi', bpm: 74, parts: [],
    strings: [
      [220, 185, 1060, 170, 'koto', null, 0, 'notes'],
      [260, 305, 1020, 300, 'flute', null, 0, 'notes'],
      [220, 430, 680, 450, 'crystal', null, -1, 'chord'],
      [740, 450, 1060, 420, 'handdrums', null, 0, 'notes'],
    ],
  },
  {
    id: 'band',
    name: 'Midnight Studio',
    note: 'Lo-Fi tape chords, electric guitar lead, bass and boom-bap drums',
    key: 9, scale: 'minor', beat: 'boombap', bpm: 88, parts: ['kick', 'snare', 'hats'],
    strings: [
      [280, 170, 1000, 155, 'egtr', 'pentamin', 0, 'notes'],
      [240, 295, 1040, 290, 'lofi', 'minor', 0, 'lush'],
      [230, 445, 650, 470, 'bass', 'minor', 0, 'notes'],
      [710, 470, 1060, 430, 'drums', null, 0, 'notes'],
    ],
  },
  {
    id: 'synthwave',
    name: 'Neon Pulse',
    note: 'FM pluck leads, analog synth chords, a deep boom bass and driving drums',
    key: 5, scale: 'dorian', beat: 'synthwave', bpm: 112, parts: ['kick', 'snare', 'hats'],
    strings: [
      [240, 175, 1040, 165, 'fmpluck', null, 0, 'notes'],
      [240, 305, 1040, 305, 'synth', null, 0, 'chord'],
      [240, 445, 660, 465, 'sub', null, 0, 'notes'],
      [720, 465, 1060, 435, 'drums', null, 0, 'notes'],
    ],
  },
  {
    id: 'oud',
    name: 'Oud & Hijaz Night',
    note: 'Oud, qanun, orchestral strings and Maqsum hand drums in Hijaz',
    key: 2, scale: 'hijaz', beat: 'maqsum', bpm: 100, parts: ['kick', 'snare'],
    strings: [
      [260, 180, 1020, 165, 'oud', null, 0, 'notes'],
      [280, 300, 1000, 305, 'qanun', null, 0, 'notes'],
      [240, 425, 700, 455, 'strings', null, 0, 'chord'],
      [760, 455, 1060, 415, 'handdrums', null, 0, 'notes'],
    ],
  },
  {
    id: 'chamber',
    name: 'Chamber Ensemble',
    note: 'Right-click & slide on Violin, Cello, Voices and Flute for lush sustain',
    key: 7, scale: 'lydian', beat: 'ambient', bpm: 72, parts: [],
    strings: [
      [280, 175, 1000, 160, 'violin', null, 0, 'notes'],
      [260, 300, 1020, 295, 'cello', null, 0, 'notes'],
      [260, 430, 690, 460, 'voices', null, 0, 'lush'],
      [740, 455, 1040, 420, 'flute', null, 0, 'notes'],
    ],
  },
];

export function starterToSetup(S: StarterPreset): StageSetup {
  return {
    v: 2,
    name: S.name,
    w: 1280,
    h: 720,
    shape: 'landscape',
    key: S.key,
    scale: S.scale,
    beat: S.beat,
    bpm: S.bpm,
    loopBars: 2,
    follow: false,
    parts: Object.fromEntries(PARTS.map(p => [p, S.parts.includes(p)])) as Record<BeatPart, boolean>,
    layers: [],
    strings: S.strings.map(([ax, ay, bx, by, inst, scale, oct, mode]) => ({
      a: [ax, ay], b: [bx, by], inst, scale, root: null, oct, mode: mode ?? 'notes', gain: 1,
    })),
  };
}

export function snapshotSetup(name: string): StageSetup {
  return {
    v: 2,
    name,
    saved: Date.now(),
    w: stageSize.w,
    h: stageSize.h,
    shape: state.shape,
    key: state.key,
    scale: state.scale,
    beat: transport.beat,
    bpm: transport.bpm,
    parts: { ...transport.parts },
    loopBars: transport.loopBars,
    follow: transport.follow,
    strings: serializeStrings(),
    layers: transport.layers.map(L => ({
      len: L.len, offset: L.offset, vol: L.vol, muted: L.muted, events: L.events,
    })),
  };
}

export function getStoredSetups(): StageSetup[] {
  try {
    const raw = localStorage.getItem(SETUP_STORE);
    if (!raw) return [];
    const parsed = JSON.parse(raw);
    return Array.isArray(parsed) ? parsed : [];
  } catch {
    return [];
  }
}

export function saveStoredSetups(list: StageSetup[]): void {
  try {
    localStorage.setItem(SETUP_STORE, JSON.stringify(list));
  } catch { /* ignore storage quota errors */ }
}
