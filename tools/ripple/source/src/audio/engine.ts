import { INSTRUMENTS, clamp, midiHz } from '../core/music';
import { LoopEvent, VoiceHandle, state } from '../core/state';

export interface AudioGraph {
  ctx: BaseAudioContext;
  master: GainNode;
  live: GainNode;
  beat: GainNode;
  fxLp: BiquadFilterNode;
  fxHp: BiquadFilterNode;
  delayL: DelayNode;
  delayR: DelayNode;
  delayWet: GainNode;
  reverbWet: GainNode;
  analyser: AnalyserNode | null;
  streamDest: MediaStreamAudioDestinationNode | null;
  noise: AudioBuffer;
  waves: {
    piano: PeriodicWave;
    keys: PeriodicWave;
    organ: PeriodicWave;
    lofi: PeriodicWave;
  };
  ks: Map<string, AudioBuffer>;
  buses: Map<string, GainNode>;
  tapNode: ScriptProcessorNode | null;
}

export const audio: {
  g: AudioGraph | null;
  pcmCallback: ((l: Float32Array, r: Float32Array) => void) | null;
} = {
  g: null,
  pcmCallback: null,
};

function makeNoiseBuffer(ctx: BaseAudioContext): AudioBuffer {
  const sr = ctx.sampleRate;
  const len = Math.floor(sr * 2.0);
  const buf = ctx.createBuffer(1, len, sr);
  const ch = buf.getChannelData(0);
  for (let i = 0; i < len; i++) ch[i] = Math.random() * 2 - 1;
  return buf;
}

// Procedural stereo velvet-noise impulse response for lush zero-sample studio reverb
function makeReverbIR(ctx: BaseAudioContext, seconds = 2.6, decay = 2.8): AudioBuffer {
  const sr = ctx.sampleRate;
  const len = Math.floor(sr * seconds);
  const buf = ctx.createBuffer(2, len, sr);
  for (let c = 0; c < 2; c++) {
    const data = buf.getChannelData(c);
    // Early reflections (first 65ms)
    const earlyCount = 14;
    for (let e = 0; e < earlyCount; e++) {
      const idx = Math.floor((0.008 + e * 0.0042 + Math.random() * 0.003) * sr);
      if (idx < len) data[idx] += (Math.random() > 0.5 ? 1 : -1) * (0.45 / (1 + e * 0.22));
    }
    // Smooth exponentially decaying stereo tail with gentle high-frequency damping
    let lp = 0;
    const damp = c === 0 ? 0.24 : 0.21;
    for (let i = 0; i < len; i++) {
      const t = i / len;
      const env = Math.pow(1 - t, decay);
      const raw = (Math.random() * 2 - 1) * env;
      lp += damp * (raw - lp);
      data[i] += lp * 0.55;
    }
  }
  return buf;
}

function makePeriodicWaves(ctx: BaseAudioContext) {
  const make = (amps: number[]) => {
    const real = new Float32Array(amps.length + 1);
    const imag = new Float32Array(amps.length + 1);
    for (let i = 0; i < amps.length; i++) imag[i + 1] = amps[i];
    return ctx.createPeriodicWave(real, imag, { disableNormalization: false });
  };
  return {
    piano: make([1.0, 0.56, 0.34, 0.22, 0.14, 0.09, 0.05, 0.03, 0.02]),
    keys:  make([1.0, 0.25, 0.18, 0.05, 0.09, 0.02, 0.03]),
    organ: make([0.9, 1.0, 0.72, 0.65, 0.0, 0.45, 0.0, 0.35, 0.0, 0.15]),
    lofi:  make([1.0, 0.32, 0.14, 0.06, 0.03]),
  };
}

export function buildGraph(ctx: BaseAudioContext, opts: { offline?: boolean } = {}): AudioGraph {
  const master = ctx.createGain();
  master.gain.value = opts.offline ? 0.9 : state.settings.volume;

  const live = ctx.createGain();
  live.gain.value = state.mix.live;

  const beat = ctx.createGain();
  beat.gain.value = state.mix.beat;

  const fxLp = ctx.createBiquadFilter();
  fxLp.type = 'lowpass';
  fxLp.frequency.value = 18000;
  fxLp.Q.value = 0.7;

  const fxHp = ctx.createBiquadFilter();
  fxHp.type = 'highpass';
  fxHp.frequency.value = 24;
  fxHp.Q.value = 0.7;

  // Stereo ping-pong echo (driven by Air Pad X-axis)
  const delayL = ctx.createDelay(1.2);
  const delayR = ctx.createDelay(1.2);
  delayL.delayTime.value = 0.28;
  delayR.delayTime.value = 0.37;
  const fbL = ctx.createGain(); fbL.gain.value = 0.38;
  const fbR = ctx.createGain(); fbR.gain.value = 0.38;
  const delayTone = ctx.createBiquadFilter();
  delayTone.type = 'lowpass'; delayTone.frequency.value = 3200;
  const delayWet = ctx.createGain();
  delayWet.gain.value = 0.0;

  const merger = ctx.createChannelMerger(2);
  delayL.connect(fbL); fbL.connect(delayR);
  delayR.connect(fbR); fbR.connect(delayTone); delayTone.connect(delayL);
  delayL.connect(merger, 0, 0);
  delayR.connect(merger, 0, 1);
  merger.connect(delayWet);

  // Procedural stereo convolution reverb
  const convolver = ctx.createConvolver();
  convolver.buffer = makeReverbIR(ctx);
  const reverbWet = ctx.createGain();
  reverbWet.gain.value = state.settings.reverb * 0.42;

  // Master compressor + soft safety limiter
  const comp = ctx.createDynamicsCompressor();
  comp.threshold.value = -10;
  comp.knee.value = 16;
  comp.ratio.value = 4.5;
  comp.attack.value = 0.004;
  comp.release.value = 0.16;

  live.connect(fxLp);
  beat.connect(fxLp);
  fxLp.connect(fxHp);

  fxHp.connect(comp);
  fxHp.connect(delayL);
  delayWet.connect(comp);
  fxHp.connect(convolver);
  convolver.connect(reverbWet);
  reverbWet.connect(comp);

  comp.connect(master);

  let analyser: AnalyserNode | null = null;
  let streamDest: MediaStreamAudioDestinationNode | null = null;

  if (!opts.offline && ctx instanceof AudioContext) {
    analyser = ctx.createAnalyser();
    analyser.fftSize = 1024;
    analyser.smoothingTimeConstant = 0.72;
    master.connect(analyser);
    analyser.connect(ctx.destination);

    try {
      streamDest = ctx.createMediaStreamDestination();
      master.connect(streamDest);
    } catch {
      streamDest = null;
    }
  } else {
    master.connect(ctx.destination);
  }

  return {
    ctx,
    master,
    live,
    beat,
    fxLp,
    fxHp,
    delayL,
    delayR,
    delayWet,
    reverbWet,
    analyser,
    streamDest,
    noise: makeNoiseBuffer(ctx),
    waves: makePeriodicWaves(ctx),
    ks: new Map(),
    buses: new Map(),
    tapNode: null,
  };
}

export function initAudio(): AudioGraph | null {
  if (!audio.g) {
    const AC = window.AudioContext || (window as unknown as { webkitAudioContext: typeof AudioContext }).webkitAudioContext;
    if (!AC) return null;
    const ctx = new AC({ latencyHint: 'interactive' });
    audio.g = buildGraph(ctx);
  }
  const ctx = audio.g.ctx as AudioContext;
  if (ctx.state === 'suspended') {
    ctx.resume().catch(() => {});
  }
  return audio.g;
}

export function ensurePcmTap(): void {
  const g = initAudio();
  if (!g || g.tapNode || !(g.ctx instanceof AudioContext)) return;
  try {
    const sp = g.ctx.createScriptProcessor(2048, 2, 2);
    sp.onaudioprocess = ev => {
      if (audio.pcmCallback) {
        audio.pcmCallback(ev.inputBuffer.getChannelData(0), ev.inputBuffer.getChannelData(1));
      }
    };
    const silent = g.ctx.createGain();
    silent.gain.value = 0;
    g.master.connect(sp);
    sp.connect(silent);
    silent.connect(g.ctx.destination);
    g.tapNode = sp;
  } catch { /* ignore if unsupported */ }
}

export function setMasterVolume(v: number): void {
  if (!audio.g) return;
  const t = audio.g.ctx.currentTime;
  audio.g.master.gain.setTargetAtTime(clamp(v, 0, 1.2), t, 0.02);
}

export function setReverbAmount(v: number): void {
  if (!audio.g) return;
  const t = audio.g.ctx.currentTime;
  audio.g.reverbWet.gain.setTargetAtTime(clamp(v, 0, 1) * 0.48, t, 0.04);
}

export function setMixLevels(): void {
  if (!audio.g) return;
  const t = audio.g.ctx.currentTime;
  audio.g.live.gain.setTargetAtTime(state.mix.live, t, 0.025);
  audio.g.beat.gain.setTargetAtTime(state.mix.beat, t, 0.025);
}

export function setFx(dark: number, thin: number, echo: number): void {
  if (!audio.g) return;
  const t = audio.g.ctx.currentTime;
  const lpFreq = 18000 * Math.pow(320 / 18000, clamp(dark, 0, 1));
  const hpFreq = 24 * Math.pow(2400 / 24, clamp(thin, 0, 1));
  audio.g.fxLp.frequency.setTargetAtTime(lpFreq, t, 0.03);
  audio.g.fxHp.frequency.setTargetAtTime(hpFreq, t, 0.03);
  audio.g.delayWet.gain.setTargetAtTime(clamp(echo, 0, 1) * 0.58, t, 0.03);
}

function instBus(g: AudioGraph, id: string, dest: AudioNode): GainNode {
  const key = id + ':' + (dest === g.live ? 'L' : dest === g.beat ? 'B' : 'O');
  if (dest === g.live || dest === g.beat) {
    const hit = g.buses.get(key);
    if (hit) return hit;
  }
  const ctx = g.ctx;
  const inp = ctx.createGain();
  let node: AudioNode = inp;

  if (id === 'egtr') {
    const sh = ctx.createWaveShaper();
    const curve = new Float32Array(257);
    for (let i = 0; i < 257; i++) { const x = i / 128 - 1; curve[i] = Math.tanh(x * 3.8); }
    sh.curve = curve;
    const lp = ctx.createBiquadFilter(); lp.type = 'lowpass'; lp.frequency.value = 3400;
    const outG = ctx.createGain(); outG.gain.value = 0.52;
    node.connect(sh); sh.connect(lp); lp.connect(outG); node = outG;
  } else if (id === 'sitar') {
    const pk = ctx.createBiquadFilter(); pk.type = 'peaking'; pk.frequency.value = 1850; pk.Q.value = 3.2; pk.gain.value = 6.5;
    node.connect(pk); node = pk;
  } else if (id === 'koto') {
    const pk = ctx.createBiquadFilter(); pk.type = 'peaking'; pk.frequency.value = 2400; pk.Q.value = 2.0; pk.gain.value = 4.5;
    node.connect(pk); node = pk;
  } else if (id === 'oud') {
    const pk = ctx.createBiquadFilter(); pk.type = 'peaking'; pk.frequency.value = 680; pk.Q.value = 1.4; pk.gain.value = 4.0;
    node.connect(pk); node = pk;
  } else if (id === 'drums') {
    const sh = ctx.createWaveShaper();
    const curve = new Float32Array(257);
    for (let i = 0; i < 257; i++) { const x = i / 128 - 1; curve[i] = Math.tanh(x * 1.4); }
    sh.curve = curve;
    node.connect(sh); node = sh;
  }

  node.connect(dest);
  if (dest === g.live || dest === g.beat) g.buses.set(key, inp);
  return inp;
}

const KS_PARAMS: Record<string, { dur: number; bright: number; pick: number; t60: number; det?: number[]; buzz?: boolean }> = {
  guitar: { dur: 2.6, bright: 0.62, pick: 0.2,  t60: 3.4 },
  harp:   { dur: 3.4, bright: 0.36, pick: 0.48, t60: 5.2 },
  oud:    { dur: 1.8, bright: 0.85, pick: 0.11, t60: 2.0, det: [-6, 6] },
  bass:   { dur: 2.2, bright: 0.24, pick: 0.30, t60: 3.1 },
  egtr:   { dur: 3.0, bright: 0.72, pick: 0.14, t60: 5.0 },
  qanun:  { dur: 2.5, bright: 0.90, pick: 0.08, t60: 2.9, det: [-7, 0, 7] },
  sitar:  { dur: 3.3, bright: 0.95, pick: 0.06, t60: 4.6, buzz: true },
  koto:   { dur: 2.8, bright: 0.88, pick: 0.09, t60: 3.6, det: [-4, 4] },
};

function ksBuffer(g: AudioGraph, id: string, midi: number): AudioBuffer {
  const key = id + ':' + midi;
  const hit = g.ks.get(key);
  if (hit) return hit;
  const P = KS_PARAMS[id];
  const ctx = g.ctx, sr = ctx.sampleRate, n = Math.floor(sr * P.dur);
  const data = new Float32Array(n);

  const render = (freq: number, gain: number) => {
    const period = sr / freq;
    let N = Math.floor(period - 0.5), frac = period - 0.5 - N;
    if (frac < 0.1) { N -= 1; frac += 1; }
    if (N < 2) N = 2;
    const C = (1 - frac) / (1 + frac);
    const dl = new Float32Array(N);
    let lp = 0;
    for (let i = 0; i < N; i++) { lp += P.bright * ((Math.random() * 2 - 1) - lp); dl[i] = lp; }
    const off = Math.max(1, Math.round(P.pick * N));
    const ex = dl.slice();
    let peak = 1e-6;
    for (let i = 0; i < N; i++) { dl[i] = ex[i] - ex[(i - off + N) % N]; peak = Math.max(peak, Math.abs(dl[i])); }
    for (let i = 0; i < N; i++) dl[i] /= peak;
    const decay = Math.pow(0.001, 1 / (freq * P.t60));
    let idx = 0, prev = 0, apx = 0, apy = 0;
    for (let i = 0; i < n; i++) {
      const x = dl[idx];
      const avg = P.buzz && x < 0 ? 0.9 * x + 0.1 * prev : 0.5 * (x + prev);
      prev = x;
      const y = C * avg + apx - C * apy;
      apx = avg; apy = y;
      dl[idx] = y * decay;
      data[i] += x * gain;
      if (++idx >= N) idx = 0;
    }
  };

  const f = midiHz(midi);
  if (P.det) {
    for (const c of P.det) render(f * Math.pow(2, c / 1200), 1 / P.det.length + 0.1);
  } else {
    render(f, 1);
  }
  let peak = 1e-6;
  for (let i = 0; i < n; i++) peak = Math.max(peak, Math.abs(data[i]));
  const fade = Math.floor(sr * 0.05);
  for (let i = 0; i < n; i++) {
    let gn = 0.85 / peak;
    if (i > n - fade) gn *= (n - i) / fade;
    data[i] *= gn;
  }
  const buf = ctx.createBuffer(1, n, sr);
  buf.getChannelData(0).set(data);
  if (g.ks.size > 300) g.ks.delete(g.ks.keys().next().value!);
  g.ks.set(key, buf);
  return buf;
}

type EnvPt = [number, number, ('lin' | 'exp')?];

function env(param: AudioParam, t: number, pts: EnvPt[]): void {
  param.cancelScheduledValues(t);
  param.setValueAtTime(pts[0][1], t + pts[0][0]);
  for (let i = 1; i < pts.length; i++) {
    const [dt, v, kind] = pts[i];
    if (kind === 'exp') param.exponentialRampToValueAtTime(Math.max(v, 1e-4), t + dt);
    else param.linearRampToValueAtTime(v, t + dt);
  }
}

export interface PlayOpts {
  held?: boolean;
  holdSec?: number;
  pan?: number;
  graph?: AudioGraph;
}

export function playNote(
  id: string,
  midi: number,
  t: number,
  vel: number,
  dest?: AudioNode,
  len?: number,
  opts?: PlayOpts,
): VoiceHandle | null {
  const g = opts?.graph ?? audio.g;
  if (!g) return null;
  const ctx = g.ctx;
  t = Math.max(t, ctx.currentTime);
  vel = clamp(vel, 0.05, 1.2);
  const targetDest = dest ?? g.live;
  const synthId = id === 'epiano' ? 'keys' : id;
  const bus = instBus(g, synthId, targetDest);

  let out: AudioNode = bus;
  if (opts?.pan != null && typeof ctx.createStereoPanner === 'function') {
    const panner = ctx.createStereoPanner();
    panner.pan.value = clamp(opts.pan, -0.78, 0.78);
    panner.connect(out);
    out = panner;
  }

  const held = !!opts?.held;
  let gate: GainNode | null = null;
  if (held) {
    gate = ctx.createGain();
    gate.connect(out);
    out = gate;
  }
  const hs = held ? 45 : opts?.holdSec;
  const H = (base: number) => (hs != null ? Math.max(hs, 0.08) : base * (len || 1));

  const srcs: AudioScheduledSourceNode[] = [];
  const noiseSrc = (st: number, dur: number) => {
    const s = ctx.createBufferSource();
    s.buffer = g.noise;
    s.loop = true;
    s.start(st, Math.random() * 1.4);
    s.stop(st + dur + 0.05);
    srcs.push(s);
    return s;
  };
  const oscAt = (type: OscillatorType | PeriodicWave, freq: number, st: number, dur: number) => {
    const o = ctx.createOscillator();
    if (typeof type === 'string') o.type = type as OscillatorType;
    else o.setPeriodicWave(type);
    o.frequency.value = freq;
    o.start(st);
    o.stop(st + dur + 0.05);
    srcs.push(o);
    return o;
  };

  const f = midiHz(midi);

  // Karplus-Strong plucked instruments (incl. Koto)
  if (synthId in KS_PARAMS) {
    const s = ctx.createBufferSource();
    s.buffer = ksBuffer(g, synthId, midi);
    srcs.push(s);
    const lp = ctx.createBiquadFilter();
    lp.type = 'lowpass';
    lp.frequency.value = clamp(1800 + vel * 9500, 1200, 14000);
    const gn = ctx.createGain();
    gn.gain.value = 0.25 + 0.75 * vel;
    s.connect(lp); lp.connect(gn); gn.connect(out);
    s.start(t);

    if (synthId === 'koto') {
      // Characteristic subtle initial pitch scoop & woody body tap
      env(s.detune, t, [[0, 26], [0.055, 0, 'lin']]);
    }
    if (synthId === 'bass') {
      const o = oscAt('sine', f, t, 0.9), og = ctx.createGain();
      env(og.gain, t, [[0, 0], [0.01, 0.5 * vel], [0.9, 0.0001, 'exp']]);
      o.connect(og); og.connect(out);
    }
    return { srcs, gate, t };
  }

  if (synthId === 'piano' || synthId === 'keys' || synthId === 'lofi') {
    const isLofi = synthId === 'lofi';
    const dur = clamp(3.2 - (midi - 36) * 0.03, 1.2, 3.4) * (len || 1);
    const gn = ctx.createGain(), lp = ctx.createBiquadFilter();
    lp.type = 'lowpass'; lp.Q.value = isLofi ? 1.1 : 0.4;
    const maxF = isLofi ? Math.min(3400, f * 3.2 + 1200 * vel) : Math.min(11000, f * 5 + 2500 * vel + 600);
    env(lp.frequency, t, [[0, maxF], [dur * 0.6, Math.max(420, f * 1.5), 'exp']]);
    env(gn.gain, t, [[0, 0], [isLofi ? 0.014 : 0.005, 0.52 * vel], [0.14, 0.29 * vel, 'exp'], [dur, 0.0001, 'exp']]);
    const wave = synthId === 'keys' ? g.waves.keys : isLofi ? g.waves.lofi : g.waves.piano;
    const o1 = oscAt(wave, f, t, dur);
    const o2 = oscAt(wave, f * (isLofi ? 1.0032 : 1.0018), t, dur);
    const g2 = ctx.createGain(); g2.gain.value = 0.6;
    if (isLofi) {
      // Gentle tape pitch wow/flutter
      const lfo = oscAt('sine', 2.4 + Math.random() * 0.8, t, dur), lg = ctx.createGain();
      lg.gain.value = 7.5;
      lfo.connect(lg); lg.connect(o1.detune); lg.connect(o2.detune);
    }
    o1.connect(lp); o2.connect(g2); g2.connect(lp); lp.connect(gn); gn.connect(out);
    if (synthId === 'piano') {
      const n = noiseSrc(t, 0.04), bp = ctx.createBiquadFilter(), ng = ctx.createGain();
      bp.type = 'bandpass'; bp.frequency.value = 2600; bp.Q.value = 0.8;
      env(ng.gain, t, [[0, 0.18 * vel], [0.035, 0.0001, 'exp']]);
      n.connect(bp); bp.connect(ng); ng.connect(out);
    }
    return { srcs, gate, t };
  }

  if (synthId === 'celesta') {
    const dur = 2.4;
    const gn = ctx.createGain();
    env(gn.gain, t, [[0, 0], [0.003, 0.45 * vel], [0.22, 0.22 * vel, 'exp'], [dur, 0.0001, 'exp']]);
    const o1 = oscAt('sine', f, t, dur);
    const o2 = oscAt('sine', f * 2, t, dur * 0.65), g2 = ctx.createGain(); g2.gain.value = 0.28;
    const o3 = oscAt('sine', f * 4.01, t, 0.35), g3 = ctx.createGain();
    env(g3.gain, t, [[0, 0.14 * vel], [0.32, 0.0001, 'exp']]);
    o1.connect(gn); o2.connect(g2); g2.connect(gn); o3.connect(g3); g3.connect(gn);
    gn.connect(out);
    return { srcs, gate, t };
  }

  if (synthId === 'crystal') {
    // Glass harmonica / Tibetan crystal singing bowl
    const hold = H(1.4), dur = hold + 1.8;
    const gn = ctx.createGain();
    env(gn.gain, t, [[0, 0], [0.16, 0.44 * vel], [hold, 0.36 * vel], [dur, 0.0001, 'exp']]);
    const o1 = oscAt('sine', f, t, dur);
    const o2 = oscAt('sine', f * 1.0015, t, dur), g2 = ctx.createGain(); g2.gain.value = 0.42;
    const o3 = oscAt('sine', f * 2.756, t, dur * 0.7), g3 = ctx.createGain();
    env(g3.gain, t, [[0, 0], [0.12, 0.12 * vel], [dur * 0.68, 0.0001, 'exp']]);
    const lfo = oscAt('sine', 3.2, t, dur), lg = ctx.createGain(); lg.gain.value = 0.09;
    const trem = ctx.createGain(); trem.gain.value = 0.91;
    lfo.connect(lg); lg.connect(trem.gain);
    o1.connect(trem); o2.connect(g2); g2.connect(trem); o3.connect(g3); g3.connect(trem);
    trem.connect(gn); gn.connect(out);
    return { srcs, gate, t };
  }

  if (synthId === 'pad') {
    // Lush evolving stereo ambient pad
    const hold = H(1.5), dur = hold + 1.4;
    const gn = ctx.createGain(), lp = ctx.createBiquadFilter();
    lp.type = 'lowpass'; lp.Q.value = 1.4;
    env(lp.frequency, t, [[0, Math.max(380, f * 1.4)], [0.65, Math.min(5200, f * (3.2 + 2.5 * vel))], [dur, Math.max(360, f * 1.2), 'exp']]);
    env(gn.gain, t, [[0, 0], [0.28, 0.28 * vel], [hold, 0.24 * vel], [dur, 0.0001, 'exp']]);
    for (const [d, mult] of [[-12, 1], [-4, 1], [5, 1], [13, 1], [0, 2]] as Array<[number, number]>) {
      const o = oscAt(mult === 2 ? 'triangle' : 'sawtooth', f * mult, t, dur);
      o.detune.value = d;
      const og = ctx.createGain(); og.gain.value = mult === 2 ? 0.22 : 0.26;
      o.connect(og); og.connect(lp);
    }
    lp.connect(gn); gn.connect(out);
    return { srcs, gate, t };
  }

  if (synthId === 'fmpluck') {
    const dur = 1.15 * (len || 1);
    const gn = ctx.createGain();
    env(gn.gain, t, [[0, 0], [0.004, 0.52 * vel], [0.16, 0.22 * vel, 'exp'], [dur, 0.0001, 'exp']]);
    const car = oscAt('sine', f, t, dur);
    const mod = oscAt('sine', f * 2, t, dur), mg = ctx.createGain();
    env(mg.gain, t, [[0, f * (2.6 + 3.0 * vel)], [0.18, f * 0.2, 'exp'], [dur, 1, 'exp']]);
    mod.connect(mg); mg.connect(car.frequency);
    const lp = ctx.createBiquadFilter(); lp.type = 'lowpass'; lp.Q.value = 2.4;
    env(lp.frequency, t, [[0, Math.min(11000, f * 7)], [0.24, Math.max(600, f * 1.8), 'exp']]);
    car.connect(lp); lp.connect(gn); gn.connect(out);
    return { srcs, gate, t };
  }

  if (synthId === 'strings') {
    const hold = H(0.95), dur = hold + 0.8;
    const gn = ctx.createGain(), lp = ctx.createBiquadFilter();
    lp.type = 'lowpass'; lp.frequency.value = 1100 + 2400 * vel; lp.Q.value = 0.6;
    env(gn.gain, t, [[0, 0], [0.09, 0.3 * vel], [hold, 0.24 * vel], [dur, 0.0001, 'exp']]);
    const lfo = oscAt('sine', 5.3, t, dur), lg = ctx.createGain();
    env(lg.gain, t, [[0, 0], [0.25, 0], [0.6, 7]]);
    lfo.connect(lg);
    for (const d of [-9, 0, 8]) {
      const o = oscAt('sawtooth', f, t, dur);
      o.detune.value = d; lg.connect(o.detune); o.connect(lp);
    }
    lp.connect(gn); gn.connect(out);
    return { srcs, gate, t };
  }

  if (synthId === 'flute') {
    const hold = H(0.5), dur = hold + 0.3;
    const gn = ctx.createGain();
    env(gn.gain, t, [[0, 0], [0.05, 0.5 * vel], [hold, 0.42 * vel], [dur, 0.0001, 'exp']]);
    const lfo = oscAt('sine', 5, t, dur), lg = ctx.createGain();
    env(lg.gain, t, [[0, 0], [0.18, 0], [0.45, 9]]);
    lfo.connect(lg);
    const o1 = oscAt('sine', f, t, dur), o2 = oscAt('triangle', f * 2, t, dur), g2 = ctx.createGain();
    g2.gain.value = 0.13;
    lg.connect(o1.detune); lg.connect(o2.detune);
    o1.connect(gn); o2.connect(g2); g2.connect(gn);
    const n = noiseSrc(t, dur), bp = ctx.createBiquadFilter(), ng = ctx.createGain();
    bp.type = 'bandpass'; bp.frequency.value = Math.min(9000, f * 2.2); bp.Q.value = 1.6;
    env(ng.gain, t, [[0, 0.45], [0.07, 0.09, 'exp'], [dur, 0.04]]);
    n.connect(bp); bp.connect(ng); ng.connect(gn);
    gn.connect(out);
    return { srcs, gate, t };
  }

  if (synthId === 'bells') {
    const dur = 2.8;
    const gn = ctx.createGain();
    env(gn.gain, t, [[0, 0], [0.003, 0.5 * vel], [dur, 0.0001, 'exp']]);
    const car = oscAt('sine', f, t, dur), mod = oscAt('sine', f * 3.51, t, dur), mg = ctx.createGain();
    env(mg.gain, t, [[0, f * (1.2 + 2 * vel)], [1.1, f * 0.15, 'exp']]);
    mod.connect(mg); mg.connect(car.frequency);
    const p2 = oscAt('sine', f * 2.76, t, 0.9), pg = ctx.createGain();
    env(pg.gain, t, [[0, 0.16 * vel], [0.8, 0.0001, 'exp']]);
    car.connect(gn); p2.connect(pg); pg.connect(gn); gn.connect(out);
    return { srcs, gate, t };
  }

  if (synthId === 'organ') {
    const hold = H(0.55), dur = hold + 0.14;
    const gn = ctx.createGain(), trem = ctx.createGain();
    env(gn.gain, t, [[0, 0], [0.012, 0.5 * vel], [hold, 0.5 * vel], [dur, 0.0001, 'exp']]);
    const o = oscAt(g.waves.organ, f / 2, t, dur);
    const lfo = oscAt('sine', 6.2, t, dur), lg = ctx.createGain(); lg.gain.value = 0.12; trem.gain.value = 0.88;
    lfo.connect(lg); lg.connect(trem.gain);
    o.connect(trem); trem.connect(gn); gn.connect(out);
    return { srcs, gate, t };
  }

  if (synthId === 'marimba' || synthId === 'kalimba') {
    const M = synthId === 'marimba';
    const gn = ctx.createGain(); gn.gain.value = 1; gn.connect(out);
    const part = (mult: number, level: number, decay: number) => {
      const o = oscAt('sine', f * mult, t, decay), pg = ctx.createGain();
      env(pg.gain, t, [[0, 0], [0.002, level * vel], [decay, 0.0001, 'exp']]);
      o.connect(pg); pg.connect(gn);
    };
    if (M) { part(1, 0.6, 0.9); part(4, 0.22, 0.14); part(10, 0.07, 0.04); }
    else { part(1, 0.6, 1.7); part(2, 0.08, 0.5); part(5.4, 0.16, 0.09); part(8.9, 0.05, 0.04); }
    return { srcs, gate, t };
  }

  if (synthId === 'steelpan') {
    const dur = 1.5;
    const gn = ctx.createGain();
    env(gn.gain, t, [[0, 0], [0.004, 0.5 * vel], [0.2, 0.26 * vel, 'exp'], [dur, 0.0001, 'exp']]);
    const car = oscAt('sine', f, t, dur), mod = oscAt('sine', f * 2, t, dur), mg = ctx.createGain();
    env(car.frequency, t, [[0, f * 1.012], [0.05, f, 'exp']]);
    env(mg.gain, t, [[0, f * (1.4 + 1.6 * vel)], [0.3, f * 0.18, 'exp']]);
    mod.connect(mg); mg.connect(car.frequency);
    const p2 = oscAt('sine', f * 2.005, t, 0.7), pg = ctx.createGain();
    env(pg.gain, t, [[0, 0.2 * vel], [0.7, 0.0001, 'exp']]);
    car.connect(gn); p2.connect(pg); pg.connect(gn); gn.connect(out);
    return { srcs, gate, t };
  }

  if (synthId === 'violin' || synthId === 'cello') {
    const V = synthId === 'violin';
    const hold = H(0.55), dur = hold + 0.24;
    const gn = ctx.createGain();
    env(gn.gain, t, [[0, 0], [0.07, 0.36 * vel], [hold, 0.3 * vel], [dur, 0.0001, 'exp']]);
    const lfo = oscAt('sine', V ? 5.8 : 5.1, t, dur), lg = ctx.createGain();
    env(lg.gain, t, [[0, 0], [0.16, 0], [0.4, V ? 14 : 9]]);
    lfo.connect(lg);
    let node: AudioNode = ctx.createGain();
    for (const d of [0, 5]) { const o = oscAt('sawtooth', f, t, dur); o.detune.value = d; lg.connect(o.detune); o.connect(node); }
    for (const [fr, gain] of (V ? [[520, 6], [1150, 4], [2900, 6]] : [[230, 6], [600, 5], [1500, 4]])) {
      const b = ctx.createBiquadFilter(); b.type = 'peaking'; b.frequency.value = fr; b.Q.value = 2.2; b.gain.value = gain;
      node.connect(b); node = b;
    }
    const lp = ctx.createBiquadFilter(); lp.type = 'lowpass'; lp.frequency.value = (V ? 4800 : 2600) + 1500 * vel;
    node.connect(lp); lp.connect(gn);
    const n = noiseSrc(t, dur), bp = ctx.createBiquadFilter(), ng = ctx.createGain();
    bp.type = 'bandpass'; bp.frequency.value = V ? 3200 : 1800; bp.Q.value = 0.7;
    env(ng.gain, t, [[0, 0.05], [0.1, 0.012, 'exp'], [dur, 0.008]]);
    n.connect(bp); bp.connect(ng); ng.connect(gn);
    gn.connect(out);
    return { srcs, gate, t };
  }

  if (synthId === 'trumpet') {
    const hold = H(0.4), dur = hold + 0.13;
    const gn = ctx.createGain(), lp = ctx.createBiquadFilter();
    lp.type = 'lowpass'; lp.Q.value = 1.4;
    env(lp.frequency, t, [[0, f * 1.2], [0.05, Math.min(9000, f * (4 + 4 * vel))], [hold, Math.min(8000, f * 4)], [dur, f * 1.5]]);
    env(gn.gain, t, [[0, 0], [0.03, 0.4 * vel], [hold, 0.34 * vel], [dur, 0.0001, 'exp']]);
    const lfo = oscAt('sine', 5.4, t, dur), lg = ctx.createGain();
    env(lg.gain, t, [[0, 0], [0.22, 0], [0.42, 8]]);
    lfo.connect(lg);
    const o1 = oscAt('sawtooth', f, t, dur), o2 = oscAt('square', f, t, dur), g2 = ctx.createGain();
    g2.gain.value = 0.25; lg.connect(o1.detune); lg.connect(o2.detune);
    env(o1.detune, t, [[0, -35], [0.045, 0]]);
    o1.connect(lp); o2.connect(g2); g2.connect(lp); lp.connect(gn); gn.connect(out);
    return { srcs, gate, t };
  }

  if (synthId === 'voices') {
    const hold = H(0.9), dur = hold + 0.75;
    const gn = ctx.createGain();
    env(gn.gain, t, [[0, 0], [0.14, 0.3 * vel], [hold, 0.26 * vel], [dur, 0.0001, 'exp']]);
    const src = ctx.createGain();
    const lfo = oscAt('sine', 4.8, t, dur), lg = ctx.createGain();
    env(lg.gain, t, [[0, 0], [0.3, 0], [0.7, 8]]);
    lfo.connect(lg);
    for (const d of [-9, 0, 9]) { const o = oscAt('sawtooth', f, t, dur); o.detune.value = d; lg.connect(o.detune); o.connect(src); }
    const n = noiseSrc(t, dur), ng = ctx.createGain(); ng.gain.value = 0.05; n.connect(ng); ng.connect(src);
    for (const [fr, q, level] of [[780, 7, 1], [1180, 8, 0.6], [2850, 9, 0.28]]) {
      const b = ctx.createBiquadFilter(), bg = ctx.createGain();
      b.type = 'bandpass'; b.frequency.value = fr; b.Q.value = q; bg.gain.value = level;
      src.connect(b); b.connect(bg); bg.connect(gn);
    }
    gn.connect(out);
    return { srcs, gate, t };
  }

  if (synthId === 'synth') {
    const hold = H(0.32), dur = hold + 0.16;
    const gn = ctx.createGain(), lp = ctx.createBiquadFilter();
    lp.type = 'lowpass'; lp.Q.value = 6.5;
    env(lp.frequency, t, [[0, Math.min(12000, f * (5 + 7 * vel))], [0.22, Math.min(9000, f * 2.2), 'exp']]);
    env(gn.gain, t, [[0, 0], [0.005, 0.42 * vel], [0.14, 0.28 * vel, 'exp'], [hold, 0.25 * vel], [dur, 0.0001, 'exp']]);
    const o1 = oscAt('sawtooth', f, t, dur), o2 = oscAt('square', f, t, dur), g2 = ctx.createGain();
    o2.detune.value = 9; g2.gain.value = 0.5;
    o1.connect(lp); o2.connect(g2); g2.connect(lp); lp.connect(gn); gn.connect(out);
    return { srcs, gate, t };
  }

  if (synthId === 'sub') {
    const dur = 0.92 * (len || 1);
    const gn = ctx.createGain();
    env(gn.gain, t, [[0, 0], [0.008, 0.88 * vel], [dur, 0.0001, 'exp']]);
    const o = oscAt('sine', f, t, dur);
    env(o.frequency, t, [[0, f * 2.2], [0.05, f, 'exp']]);
    const sh = ctx.createWaveShaper(), c = new Float32Array(257);
    for (let i = 0; i < 257; i++) { const x = i / 128 - 1; c[i] = Math.tanh(x * 2.2); }
    sh.curve = c;
    o.connect(sh); sh.connect(gn); gn.connect(out);
    return { srcs, gate, t };
  }

  return { srcs, gate, t };
}

export function releaseVoice(v: VoiceHandle | null): void {
  if (!v || !audio.g) return;
  const t = audio.g.ctx.currentTime;
  if (v.gate) v.gate.gain.setTargetAtTime(0, t, 0.075);
  for (const s of v.srcs) {
    try { s.stop(t + 0.65); } catch { /* already stopped */ }
  }
}

export function bendVoice(v: VoiceHandle | null, cents: number, glide = 0.025): void {
  if (!v || !audio.g) return;
  const t = audio.g.ctx.currentTime;
  for (const s of v.srcs) {
    const det = (s as OscillatorNode | AudioBufferSourceNode).detune;
    if (!det) continue;
    const tagged = s as unknown as { _d0?: number };
    if (tagged._d0 == null) tagged._d0 = det.value;
    det.cancelScheduledValues(t);
    det.setTargetAtTime(tagged._d0 + cents, t, glide);
  }
}

export function playDrum(
  name: string,
  t: number,
  vel: number,
  dest?: AudioNode,
  opts?: { pan?: number; graph?: AudioGraph },
): void {
  const g = opts?.graph ?? audio.g;
  if (!g) return;
  const ctx = g.ctx;
  t = Math.max(t, ctx.currentTime);
  vel = clamp(vel, 0.05, 1.2);
  let out: AudioNode = instBus(g, 'drums', dest ?? g.live);
  if (opts?.pan != null && typeof ctx.createStereoPanner === 'function') {
    const panner = ctx.createStereoPanner();
    panner.pan.value = clamp(opts.pan, -0.75, 0.75);
    panner.connect(out);
    out = panner;
  }
  const gn = ctx.createGain();
  gn.connect(out);

  const tone = (type: OscillatorType, f0: number, f1: number, sweep: number, dur: number, level: number) => {
    const o = ctx.createOscillator(), og = ctx.createGain();
    o.type = type; o.frequency.value = f0;
    env(o.frequency, t, [[0, f0], [sweep, f1, 'exp']]);
    env(og.gain, t, [[0, level * vel], [dur, 0.0001, 'exp']]);
    o.connect(og); og.connect(gn);
    o.start(t); o.stop(t + dur + 0.05);
  };
  const noise = (type: BiquadFilterType, freq: number, q: number, dur: number, level: number, at = 0) => {
    const n = ctx.createBufferSource(), f = ctx.createBiquadFilter(), ng = ctx.createGain();
    n.buffer = g.noise; n.loop = true;
    f.type = type; f.frequency.value = freq; f.Q.value = q;
    env(ng.gain, t + at, [[0, level * vel], [dur, 0.0001, 'exp']]);
    n.connect(f); f.connect(ng); ng.connect(gn);
    n.start(t + at, Math.random() * 1.4); n.stop(t + at + dur + 0.05);
  };

  switch (name) {
    case 'kick': tone('sine', 155, 44, 0.11, 0.42, 1.0); noise('lowpass', 2500, 0.5, 0.012, 0.35); break;
    case 'snare': noise('highpass', 1300, 0.6, 0.19, 0.6); tone('triangle', 200, 165, 0.05, 0.11, 0.45); break;
    case 'hat': noise('highpass', 7800, 0.8, 0.045, 0.3); break;
    case 'ohat': noise('highpass', 7200, 0.8, 0.3, 0.26); break;
    case 'clap':
      noise('bandpass', 1500, 1.1, 0.02, 0.5);
      noise('bandpass', 1500, 1.1, 0.02, 0.5, 0.012);
      noise('bandpass', 1500, 1.1, 0.16, 0.55, 0.026);
      break;
    case 'tomL': tone('sine', 135, 82, 0.2, 0.34, 0.85); break;
    case 'tomH': tone('sine', 215, 140, 0.16, 0.28, 0.8); break;
    case 'rim': tone('triangle', 1750, 1700, 0.01, 0.03, 0.4); noise('bandpass', 2400, 3, 0.02, 0.3); break;
    case 'dum': tone('sine', 98, 58, 0.09, 0.3, 1.0); noise('lowpass', 900, 0.5, 0.02, 0.4); break;
    case 'tak': noise('bandpass', 3300, 1.6, 0.04, 0.7); tone('sine', 790, 760, 0.02, 0.06, 0.22); break;
    case 'riq': noise('highpass', 6200, 1.2, 0.06, 0.2); break;
    case 'ka': noise('bandpass', 2300, 1.4, 0.035, 0.45); break;
    case 'slap': noise('bandpass', 1700, 0.9, 0.07, 0.75); tone('sine', 420, 300, 0.03, 0.06, 0.3); break;
    case 'shaker': noise('highpass', 5200, 0.9, 0.11, 0.2); break;
    case 'cowbell': {
      const bp = ctx.createBiquadFilter(), cg = ctx.createGain();
      bp.type = 'bandpass'; bp.frequency.value = 800; bp.Q.value = 2.5;
      env(cg.gain, t, [[0, 0.5 * vel], [0.28, 0.0001, 'exp']]);
      const o1 = ctx.createOscillator(), o2 = ctx.createOscillator();
      o1.type = 'square'; o1.frequency.value = 540;
      o2.type = 'square'; o2.frequency.value = 808;
      o1.connect(bp); o2.connect(bp); bp.connect(cg); cg.connect(gn);
      o1.start(t); o1.stop(t + 0.32); o2.start(t); o2.stop(t + 0.32);
      break;
    }
    case 'tick': tone('triangle', 1500, 1480, 0.01, 0.04, 0.5); break;
  }
}

export function playEvent(
  ev: Omit<LoopEvent, 'pos'> & { pos?: number },
  t: number,
  dest?: AudioNode,
  opts?: PlayOpts,
): VoiceHandle[] {
  const g = opts?.graph ?? audio.g;
  if (!g) return [];
  if (ev.drum) {
    playDrum(ev.drum, t, ev.vel, dest, { pan: ev.pan, graph: g });
    return [];
  }
  const notes = ev.notes ? (ev.down ? ev.notes.slice().reverse() : ev.notes) : [];
  const voices: VoiceHandle[] = [];
  const spread = notes.length > 1 ? 0.022 : 0;
  notes.forEach((m, i) => {
    const v = playNote(ev.inst || 'harp', m, t + i * spread, ev.vel, dest, 1, {
      ...opts,
      pan: ev.pan,
      holdSec: ev.holdSec ?? opts?.holdSec,
      graph: g,
    });
    if (v) voices.push(v);
  });
  return voices;
}

export function isSustaining(instId: string): boolean {
  return !!INSTRUMENTS[instId]?.sustain;
}
