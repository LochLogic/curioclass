export interface ScaleDef {
  id: string;
  name: string;
  short: string;
  steps: number[];
  parent: 'major' | 'minor' | 'dorian' | 'hijaz';
}

export interface DrumZone {
  id: string;
  label: string;
}

export type InstFamily = 'plucked' | 'keys' | 'orchestral' | 'synth' | 'perc';

export interface InstrumentDef {
  id: string;
  name: string;
  color: string;
  oct: number;
  family: InstFamily;
  sustain?: boolean;
  kit?: DrumZone[];
}

export interface BeatDef {
  id: string;
  name: string;
  bpm: number;
  swing: number;
  labels: [string, string, string, string, string];
  kick: string[];
  snare: string[];
  hats: string[];
  bass: string[];
  chords: string[];
  chordInst: string;
  bassInst: string;
  chordLen: number;
  seventh?: boolean;
  kickAs?: string;
  snareAs?: string;
  hatAs?: string;
}

export const SHARP_NAMES = ['C', 'C♯', 'D', 'D♯', 'E', 'F', 'F♯', 'G', 'G♯', 'A', 'A♯', 'B'];
export const FLAT_NAMES  = ['C', 'D♭', 'D', 'E♭', 'E', 'F', 'G♭', 'G', 'A♭', 'A', 'B♭', 'B'];
const FLAT_ROOTS_MAJ = new Set([5, 10, 3, 8, 1]);
const FLAT_ROOTS_MIN = new Set([2, 7, 0, 5, 10]);

export function spell(pc: number, root: number, parent: string): string {
  const useFlat = parent === 'major' ? FLAT_ROOTS_MAJ.has(root) : FLAT_ROOTS_MIN.has(root);
  return (useFlat ? FLAT_NAMES : SHARP_NAMES)[((pc % 12) + 12) % 12];
}

export function midiHz(midi: number): number {
  return 440 * Math.pow(2, (midi - 69) / 12);
}

export function clamp(v: number, a: number, b: number): number {
  return v < a ? a : v > b ? b : v;
}

export function dist(a: { x: number; y: number }, b: { x: number; y: number }): number {
  return Math.hypot(a.x - b.x, a.y - b.y);
}

export function hexA(hex: string, a: number): string {
  const n = parseInt(hex.slice(1), 16);
  return `rgba(${(n >> 16) & 255},${(n >> 8) & 255},${n & 255},${a})`;
}

export function hexToRgb01(hex: string): [number, number, number] {
  const n = parseInt(hex.slice(1), 16);
  return [((n >> 16) & 255) / 255, ((n >> 8) & 255) / 255, (n & 255) / 255];
}

export function hexToHue(hex: string): number {
  const [r, g, b] = hexToRgb01(hex);
  const max = Math.max(r, g, b), min = Math.min(r, g, b);
  const d = max - min;
  if (d < 1e-5) return 0;
  let h = 0;
  if (max === r) h = ((g - b) / d) % 6;
  else if (max === g) h = (b - r) / d + 2;
  else h = (r - g) / d + 4;
  h /= 6;
  return h < 0 ? h + 1 : h;
}

export const SCALES: Record<string, ScaleDef> = {
  major:      { id: 'major',      name: 'Major',            short: 'major',     steps: [0, 2, 4, 5, 7, 9, 11], parent: 'major' },
  minor:      { id: 'minor',      name: 'Minor',            short: 'minor',     steps: [0, 2, 3, 5, 7, 8, 10], parent: 'minor' },
  pentamaj:   { id: 'pentamaj',   name: 'Major pentatonic', short: 'maj penta', steps: [0, 2, 4, 7, 9],        parent: 'major' },
  pentamin:   { id: 'pentamin',   name: 'Minor pentatonic', short: 'min penta', steps: [0, 3, 5, 7, 10],       parent: 'minor' },
  blues:      { id: 'blues',      name: 'Blues',            short: 'blues',     steps: [0, 3, 5, 6, 7, 10],    parent: 'minor' },
  dorian:     { id: 'dorian',     name: 'Dorian',           short: 'dorian',    steps: [0, 2, 3, 5, 7, 9, 10], parent: 'dorian' },
  lydian:     { id: 'lydian',     name: 'Lydian',           short: 'lydian',    steps: [0, 2, 4, 6, 7, 9, 11], parent: 'major' },
  mixolydian: { id: 'mixolydian', name: 'Mixolydian',       short: 'mixolyd',   steps: [0, 2, 4, 5, 7, 9, 10], parent: 'major' },
  phrygian:   { id: 'phrygian',   name: 'Phrygian',         short: 'phrygian',  steps: [0, 1, 3, 5, 7, 8, 10], parent: 'minor' },
  hijaz:      { id: 'hijaz',      name: 'Hijaz',            short: 'hijaz',     steps: [0, 1, 4, 5, 7, 8, 10], parent: 'hijaz' },
  hirajoshi:  { id: 'hirajoshi',  name: 'Hirajoshi',        short: 'hirajoshi', steps: [0, 2, 3, 7, 8],        parent: 'minor' },
  harmmin:    { id: 'harmmin',    name: 'Harmonic minor',   short: 'harm min',  steps: [0, 2, 3, 5, 7, 8, 11], parent: 'minor' },
};

export const SCALE_ORDER = Object.keys(SCALES);

export const PROGS: Record<ScaleDef['parent'], number[]> = {
  major:  [0, 4, 5, 3],
  minor:  [0, 5, 2, 6],
  dorian: [0, 3, 0, 6],
  hijaz:  [0, 1, 0, 6],
};

export function scaleDegree(parent: ScaleDef['parent'], root: number, oct: number, d: number): number {
  const steps = SCALES[parent].steps;
  return 12 * (oct + 1) + root + 12 * Math.floor(d / steps.length) + steps[((d % steps.length) + steps.length) % steps.length];
}

export const DRUM_ZONES: DrumZone[] = [
  { id: 'kick', label: 'Kick' },   { id: 'snare', label: 'Snare' },
  { id: 'hat', label: 'Hat' },     { id: 'clap', label: 'Clap' },
  { id: 'tomL', label: 'Low tom' },{ id: 'tomH', label: 'High tom' },
  { id: 'ohat', label: 'Open hat'},{ id: 'rim', label: 'Rim' },
];

export const HAND_ZONES: DrumZone[] = [
  { id: 'dum', label: 'Dum' },     { id: 'tak', label: 'Tak' },
  { id: 'ka', label: 'Ka' },       { id: 'slap', label: 'Slap' },
  { id: 'riq', label: 'Riq' },     { id: 'clap', label: 'Clap' },
  { id: 'cowbell', label: 'Cowbell'}, { id: 'shaker', label: 'Shaker' },
];

// 30 studio instruments (5 rows x 6 columns in the radial palette)
export const INSTRUMENTS: Record<string, InstrumentDef> = {
  // Row 1: Plucked strings
  guitar:    { id: 'guitar',    name: 'Guitar',          color: '#ffd166', oct: 3, family: 'plucked' },
  egtr:      { id: 'egtr',      name: 'Electric guitar', color: '#ff5d73', oct: 3, family: 'plucked' },
  harp:      { id: 'harp',      name: 'Harp',            color: '#8ff0c0', oct: 4, family: 'plucked' },
  oud:       { id: 'oud',       name: 'Oud',             color: '#ff9e6b', oct: 3, family: 'plucked' },
  qanun:     { id: 'qanun',     name: 'Qanun',           color: '#c9e265', oct: 4, family: 'plucked' },
  koto:      { id: 'koto',      name: 'Koto',            color: '#f7a8b8', oct: 4, family: 'plucked' },

  // Row 2: Keys & Mallets
  piano:     { id: 'piano',     name: 'Piano',           color: '#dfeaff', oct: 3, family: 'keys' },
  epiano:    { id: 'epiano',    name: 'Electric piano',  color: '#9fb8ff', oct: 3, family: 'keys' },
  lofi:      { id: 'lofi',      name: 'Lo-Fi tape',      color: '#d8b4fe', oct: 3, family: 'keys' },
  organ:     { id: 'organ',     name: 'Organ',           color: '#d9a877', oct: 3, family: 'keys', sustain: true },
  marimba:   { id: 'marimba',   name: 'Marimba',         color: '#f2b880', oct: 4, family: 'keys' },
  kalimba:   { id: 'kalimba',   name: 'Kalimba',         color: '#7fe0d0', oct: 4, family: 'keys' },

  // Row 3: Orchestral & Resonance
  violin:    { id: 'violin',    name: 'Violin',          color: '#ffa8c5', oct: 4, family: 'orchestral', sustain: true },
  cello:     { id: 'cello',     name: 'Cello',           color: '#d98cb3', oct: 2, family: 'orchestral', sustain: true },
  strings:   { id: 'strings',   name: 'Strings',         color: '#ff8fd0', oct: 3, family: 'orchestral', sustain: true },
  flute:     { id: 'flute',     name: 'Flute',           color: '#9eeaff', oct: 4, family: 'orchestral', sustain: true },
  trumpet:   { id: 'trumpet',   name: 'Trumpet',         color: '#f5b83d', oct: 4, family: 'orchestral', sustain: true },
  voices:    { id: 'voices',    name: 'Voices',          color: '#d4c5ff', oct: 3, family: 'orchestral', sustain: true },

  // Row 4: Bells, Glass & World
  sitar:     { id: 'sitar',     name: 'Sitar',           color: '#e6a0ff', oct: 3, family: 'plucked' },
  steelpan:  { id: 'steelpan',  name: 'Steel pan',       color: '#5fd4f4', oct: 4, family: 'keys' },
  bells:     { id: 'bells',     name: 'Bells',           color: '#fff59a', oct: 5, family: 'synth' },
  celesta:   { id: 'celesta',   name: 'Celesta',         color: '#c7f9ff', oct: 5, family: 'keys' },
  crystal:   { id: 'crystal',   name: 'Crystal bowl',    color: '#7ef9ff', oct: 4, family: 'orchestral', sustain: true },
  pad:       { id: 'pad',       name: 'Ambient pad',     color: '#a78bfa', oct: 3, family: 'synth', sustain: true },

  // Row 5: Synth, Bass & Percussion
  synth:     { id: 'synth',     name: 'Synth',           color: '#6dff9c', oct: 4, family: 'synth', sustain: true },
  fmpluck:   { id: 'fmpluck',   name: 'FM pluck',        color: '#38bdf8', oct: 4, family: 'synth' },
  bass:      { id: 'bass',      name: 'Bass',            color: '#7aa8ff', oct: 1, family: 'synth' },
  sub:       { id: 'sub',       name: 'Boom bass',        color: '#5b8cff', oct: 1, family: 'synth' },
  drums:     { id: 'drums',     name: 'Drums',           color: '#ff6b6b', oct: 0, family: 'perc', kit: DRUM_ZONES },
  handdrums: { id: 'handdrums', name: 'Hand drums',      color: '#ff8552', oct: 0, family: 'perc', kit: HAND_ZONES },
};

export const INSTRUMENT_ORDER = Object.keys(INSTRUMENTS);

export const BEATS: Record<string, BeatDef> = {
  boombap: {
    id: 'boombap', name: 'Boom bap', bpm: 88, swing: 0.16,
    labels: ['Kick', 'Snare', 'Hats', 'Bass', 'Chords'],
    kick: ['X-----x---x-----', 'X-----x--x-x----'],
    snare: ['----X-------X---'],
    hats: ['x-x-x-x-x-x-x-x-'],
    bass: ['0-----0---0-----', '0-----0--0-5----'],
    chords: ['x--x------x-----'],
    chordInst: 'piano', bassInst: 'bass', chordLen: 0.6,
  },
  lofi: {
    id: 'lofi', name: 'Lo-fi', bpm: 76, swing: 0.22,
    labels: ['Kick', 'Snare', 'Hats', 'Bass', 'Chords'],
    kick: ['X-----x-x-------', 'X-----x---x--x--'],
    snare: ['----x-------x---'],
    hats: ['x-x-x-x-x-x-x-x-'],
    bass: ['0-------0--5----', '0-------0-----3-'],
    chords: ['x-------x-------'],
    chordInst: 'lofi', bassInst: 'bass', chordLen: 1.4, seventh: true,
  },
  house: {
    id: 'house', name: 'House', bpm: 122, swing: 0,
    labels: ['Kick', 'Clap', 'Hats', 'Bass', 'Chords'],
    kick: ['X---X---X---X---'],
    snare: ['----X-------X---'],
    hats: ['--o---o---o---o-', '--o---o---o--xo-'],
    bass: ['--0--0-0--0--0-8'],
    chords: ['x--x--x---x--x--'],
    chordInst: 'epiano', bassInst: 'bass', chordLen: 0.35, snareAs: 'clap',
  },
  ambient: {
    id: 'ambient', name: 'Ambient', bpm: 68, swing: 0.05,
    labels: ['Pulse', 'Rim', 'Shaker', 'Sub', 'Pad'],
    kick: ['X---------x-----', 'X---------------'],
    snare: ['------------x---', '------x---------'],
    hats: ['x---x---x---x---'],
    bass: ['0---------------', '0-------5-------'],
    chords: ['x---------------'],
    chordInst: 'pad', bassInst: 'sub', chordLen: 2.2, seventh: true,
    snareAs: 'rim', hatAs: 'shaker',
  },
  synthwave: {
    id: 'synthwave', name: 'Synthwave', bpm: 112, swing: 0,
    labels: ['Kick', 'Snare', 'Hats', 'Bass', 'Chords'],
    kick: ['X---X---X---X---'],
    snare: ['----X-------X---'],
    hats: ['x-x-x-x-x-x-x-o-'],
    bass: ['0-0-0-0-0-0-0-8-', '0-0-0-0-5-5-3-0-'],
    chords: ['x-------x---x---'],
    chordInst: 'synth', bassInst: 'bass', chordLen: 0.7,
  },
  trap: {
    id: 'trap', name: 'Trap', bpm: 140, swing: 0,
    labels: ['Kick', 'Snare', 'Hats', 'Boom', 'Chords'],
    kick: ['X------x--x-----', 'X-----x---x--x--'],
    snare: ['--------X-------'],
    hats: ['x-x-x-x-xxx-x-xx', 'x-x-xxx-x-x-xxxx'],
    bass: ['0------0--0-----', '0-----0---0--5--'],
    chords: ['x---------------'],
    chordInst: 'bells', bassInst: 'sub', chordLen: 1,
  },
  dembow: {
    id: 'dembow', name: 'Dembow', bpm: 96, swing: 0,
    labels: ['Kick', 'Snare', 'Hats', 'Bass', 'Chords'],
    kick: ['X---X---X---X---'],
    snare: ['---x--x----x--x-'],
    hats: ['x-x-x-x-x-x-x-x-'],
    bass: ['0-----0-0-----5-'],
    chords: ['x-----x---x-----'],
    chordInst: 'guitar', bassInst: 'bass', chordLen: 1,
  },
  maqsum: {
    id: 'maqsum', name: 'Maqsum', bpm: 100, swing: 0,
    labels: ['Dum', 'Tak', 'Riq', 'Bass', 'Oud'],
    kick: ['X-------X-------'],
    snare: ['--X---X-----X---', '--X---X-----X-x-'],
    hats: ['x-xxx-xxx-xxx-xx'],
    bass: ['0-------0-----5-'],
    chords: ['x-------------x-'],
    chordInst: 'oud', bassInst: 'bass', chordLen: 1,
    kickAs: 'dum', snareAs: 'tak', hatAs: 'riq',
  },
};

export const BEAT_ORDER = Object.keys(BEATS);
export const PARTS = ['kick', 'snare', 'hats', 'bass', 'chords'] as const;
export type BeatPart = typeof PARTS[number];

export function own<T extends object>(table: T, key: unknown): key is keyof T {
  return typeof key === 'string' && Object.prototype.hasOwnProperty.call(table, key);
}
