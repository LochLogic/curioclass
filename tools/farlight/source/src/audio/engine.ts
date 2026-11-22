import type { StarKind } from '../sim/galaxy.ts';
import { createRng } from '../sim/prng.ts';

export type AudioScene = 'space' | 'planet-fly' | 'on-foot' | 'jump';

// MIDI note -> Hz
function midiToHz(midi: number): number {
  return 440 * Math.pow(2, (midi - 69) / 12);
}

// Cozy, wondrous musical scales (semitone offsets from root)
const SCALES: Record<StarKind, { root: number; notes: number[]; tempoSec: number }> = {
  'warm-sun':    { root: 60, notes: [0, 2, 4, 7, 9, 12, 14, 16, 19], tempoSec: 1.55 }, // C Major Pentatonic
  'amber-dwarf': { root: 57, notes: [0, 2, 5, 7, 9, 12, 14, 17, 19], tempoSec: 1.75 }, // A Dorian / Cozy Sunset
  'sky-giant':   { root: 62, notes: [0, 2, 4, 6, 7, 9, 11, 14, 18], tempoSec: 1.45 },  // D Lydian Shimmer
  pulsar:        { root: 64, notes: [0, 2, 7, 9, 11, 12, 14, 19], tempoSec: 1.15 },    // E Sparkling Pulse
  'black-hole':  { root: 55, notes: [0, 2, 3, 7, 10, 12, 14, 15], tempoSec: 2.05 },    // G Mysterious Wonder
};

export class ProceduralAudioEngine {
  private ctx: AudioContext | null = null;
  private masterGain: GainNode | null = null;
  private reverbNode: ConvolverNode | null = null;
  private musicBus: GainNode | null = null;
  private sfxBus: GainNode | null = null;

  // Continuous engine / wind bed
  private noiseFilter: BiquadFilterNode | null = null;
  private noiseGain: GainNode | null = null;
  private engineOsc: OscillatorNode | null = null;
  private engineOscGain: GainNode | null = null;

  private muted = false;
  private unlocked = false;
  private starKind: StarKind = 'warm-sun';
  private rng = createRng(202604);
  private nextNoteTimer = 0.6;
  private chordStep = 0;

  isMuted(): boolean {
    return this.muted;
  }

  unlock(): void {
    if (this.unlocked) {
      if (this.ctx?.state === 'suspended') {
        void this.ctx.resume();
      }
      return;
    }
    const AudioCtx = window.AudioContext || (window as unknown as { webkitAudioContext: typeof AudioContext }).webkitAudioContext;
    if (!AudioCtx) return;

    const ctx = new AudioCtx();
    this.ctx = ctx;

    const master = ctx.createGain();
    master.gain.value = this.muted ? 0 : 0.72;
    master.connect(ctx.destination);
    this.masterGain = master;

    // Synthetic 2.5s stereo shimmer reverb (0 bytes of audio files!)
    const sampleRate = ctx.sampleRate;
    const irLen = Math.floor(sampleRate * 2.5);
    const irBuf = ctx.createBuffer(2, irLen, sampleRate);
    for (let ch = 0; ch < 2; ch++) {
      const data = irBuf.getChannelData(ch);
      let lp = 0;
      for (let i = 0; i < irLen; i++) {
        const decay = Math.pow(1 - i / irLen, 2.7);
        const white = (Math.random() * 2 - 1) * decay;
        lp = lp * 0.72 + white * 0.28;
        data[i] = lp * 0.55;
      }
    }
    const reverb = ctx.createConvolver();
    reverb.buffer = irBuf;
    const reverbGain = ctx.createGain();
    reverbGain.gain.value = 0.42;
    reverb.connect(reverbGain);
    reverbGain.connect(master);
    this.reverbNode = reverb;

    const musicBus = ctx.createGain();
    musicBus.gain.value = 0.48;
    musicBus.connect(master);
    musicBus.connect(reverb);
    this.musicBus = musicBus;

    const sfxBus = ctx.createGain();
    sfxBus.gain.value = 0.58;
    sfxBus.connect(master);
    sfxBus.connect(reverb);
    this.sfxBus = sfxBus;

    // Continuous soft noise bed (ship thrusters in space / gentle breeze on planets)
    const noiseBuf = ctx.createBuffer(1, sampleRate * 2, sampleRate);
    const nData = noiseBuf.getChannelData(0);
    let last = 0;
    for (let i = 0; i < nData.length; i++) {
      const w = Math.random() * 2 - 1;
      last = (last + 0.04 * w) / 1.04;
      nData[i] = last * 2.6;
    }
    const noiseSrc = ctx.createBufferSource();
    noiseSrc.buffer = noiseBuf;
    noiseSrc.loop = true;

    const noiseFilter = ctx.createBiquadFilter();
    noiseFilter.type = 'lowpass';
    noiseFilter.frequency.value = 260;

    const noiseGain = ctx.createGain();
    noiseGain.gain.value = 0.02;

    noiseSrc.connect(noiseFilter);
    noiseFilter.connect(noiseGain);
    noiseGain.connect(master);
    noiseSrc.start();

    this.noiseFilter = noiseFilter;
    this.noiseGain = noiseGain;

    // Warm ship hum oscillator
    const osc = ctx.createOscillator();
    osc.type = 'triangle';
    osc.frequency.value = 68;
    const oscGain = ctx.createGain();
    oscGain.gain.value = 0.015;
    osc.connect(oscGain);
    oscGain.connect(master);
    osc.start();
    this.engineOsc = osc;
    this.engineOscGain = oscGain;

    this.unlocked = true;
  }

  toggleMute(): boolean {
    this.muted = !this.muted;
    if (this.masterGain && this.ctx) {
      this.masterGain.gain.setTargetAtTime(this.muted ? 0 : 0.72, this.ctx.currentTime, 0.05);
    }
    return this.muted;
  }

  setSystemMood(starKind: StarKind, seed: number): void {
    this.starKind = starKind;
    this.rng = createRng(seed ^ 0x51a7c0de);
    this.chordStep = 0;
  }

  /** Called every frame to smoothly adapt engine/wind ambience & advance the generative score */
  update(dt: number, scene: AudioScene, speedRatio: number, boostAmount: number, jetpacking: boolean): void {
    if (!this.unlocked || !this.ctx || this.ctx.state !== 'running') return;
    const now = this.ctx.currentTime;

    // Continuous thruster / wind / jetpack ambience
    if (this.noiseFilter && this.noiseGain && this.engineOsc && this.engineOscGain) {
      if (scene === 'jump') {
        this.noiseFilter.frequency.setTargetAtTime(1400, now, 0.15);
        this.noiseGain.gain.setTargetAtTime(0.18, now, 0.15);
        this.engineOsc.frequency.setTargetAtTime(145, now, 0.2);
        this.engineOscGain.gain.setTargetAtTime(0.06, now, 0.15);
      } else if (scene === 'on-foot') {
        const targetFreq = jetpacking ? 920 : 320;
        const targetVol = jetpacking ? 0.12 : 0.035;
        this.noiseFilter.frequency.setTargetAtTime(targetFreq, now, 0.08);
        this.noiseGain.gain.setTargetAtTime(targetVol, now, 0.08);
        this.engineOscGain.gain.setTargetAtTime(jetpacking ? 0.035 : 0.0, now, 0.08);
        this.engineOsc.frequency.setTargetAtTime(jetpacking ? 130 : 60, now, 0.08);
      } else {
        const clampedSpd = Math.max(0, Math.min(1, speedRatio));
        const freq = 200 + clampedSpd * 480 + boostAmount * 620;
        const vol = 0.018 + clampedSpd * 0.045 + boostAmount * 0.065;
        this.noiseFilter.frequency.setTargetAtTime(freq, now, 0.1);
        this.noiseGain.gain.setTargetAtTime(vol, now, 0.1);
        this.engineOsc.frequency.setTargetAtTime(62 + clampedSpd * 46 + boostAmount * 35, now, 0.1);
        this.engineOscGain.gain.setTargetAtTime(0.012 + clampedSpd * 0.025 + boostAmount * 0.02, now, 0.1);
      }
    }

    // Generative ambient melody & warm chords
    if (scene === 'jump') return;
    this.nextNoteTimer -= dt;
    if (this.nextNoteTimer <= 0) {
      const cfg = SCALES[this.starKind];
      this.nextNoteTimer = cfg.tempoSec * (0.7 + this.rng.next() * 0.75);

      // Every 4th beat, swell a warm soft pad chord
      if (this.chordStep % 4 === 0) {
        const rootOffset = this.rng.pick([0, 0, 2, 4, 5]);
        const baseMidi = cfg.root - 12 + (cfg.notes[rootOffset] ?? 0);
        this.playWarmPad(midiToHz(baseMidi), cfg.tempoSec * 4.2, 0.085);
        this.playWarmPad(midiToHz(baseMidi + 7), cfg.tempoSec * 4.2, 0.06);
      }
      this.chordStep++;

      // Play a gentle FM bell / electric piano note (higher & airier on planets!)
      if (this.rng.chance(0.82)) {
        const semitone = this.rng.pick(cfg.notes);
        const octaveShift = scene === 'on-foot' ? 12 : this.rng.chance(0.35) ? 12 : 0;
        const hz = midiToHz(cfg.root + semitone + octaveShift);
        this.playBellNote(hz, 1.8 + this.rng.next() * 1.4, 0.095);
      }
    }
  }

  private playWarmPad(freq: number, duration: number, volume: number): void {
    if (!this.ctx || !this.musicBus) return;
    const now = this.ctx.currentTime;
    const osc = this.ctx.createOscillator();
    const osc2 = this.ctx.createOscillator();
    const filter = this.ctx.createBiquadFilter();
    const gain = this.ctx.createGain();

    osc.type = 'sawtooth';
    osc2.type = 'triangle';
    osc.frequency.value = freq;
    osc2.frequency.value = freq * 1.004; // subtle warm chorus detune

    filter.type = 'lowpass';
    filter.frequency.setValueAtTime(360, now);
    filter.frequency.linearRampToValueAtTime(740, now + duration * 0.45);
    filter.frequency.linearRampToValueAtTime(280, now + duration);

    gain.gain.setValueAtTime(0.0001, now);
    gain.gain.linearRampToValueAtTime(volume, now + duration * 0.35);
    gain.gain.exponentialRampToValueAtTime(0.0001, now + duration);

    osc.connect(filter);
    osc2.connect(filter);
    filter.connect(gain);
    gain.connect(this.musicBus);

    osc.start(now);
    osc2.start(now);
    osc.stop(now + duration + 0.05);
    osc2.stop(now + duration + 0.05);
  }

  private playBellNote(freq: number, duration: number, volume: number): void {
    if (!this.ctx || !this.musicBus) return;
    const now = this.ctx.currentTime;
    // Gentle 2-operator FM bell (soft Rhodes / celesta timbre)
    const carrier = this.ctx.createOscillator();
    const mod = this.ctx.createOscillator();
    const modGain = this.ctx.createGain();
    const gain = this.ctx.createGain();

    carrier.type = 'sine';
    carrier.frequency.value = freq;
    mod.type = 'sine';
    mod.frequency.value = freq * 2.0;

    modGain.gain.setValueAtTime(freq * 0.65, now);
    modGain.gain.exponentialRampToValueAtTime(1.0, now + duration * 0.45);

    gain.gain.setValueAtTime(0.0001, now);
    gain.gain.linearRampToValueAtTime(volume, now + 0.025);
    gain.gain.exponentialRampToValueAtTime(0.0001, now + duration);

    mod.connect(modGain);
    modGain.connect(carrier.frequency);
    carrier.connect(gain);
    gain.connect(this.musicBus);

    carrier.start(now);
    mod.start(now);
    carrier.stop(now + duration + 0.05);
    mod.stop(now + duration + 0.05);
  }

  playScanDiscovery(): void {
    if (!this.ctx || !this.sfxBus) return;
    const notes = [72, 76, 79, 84]; // C5-E5-G5-C6 joyful discovery sparkle!
    notes.forEach((m, i) => {
      setTimeout(() => this.playBellNote(midiToHz(m), 1.1, 0.14), i * 95);
    });
  }

  playRingChime(ringIndex: number): void {
    if (!this.ctx || !this.sfxBus) return;
    const scale = [67, 71, 74, 76, 79, 84]; // Ascending triumphant slalom chimes!
    const midi = scale[ringIndex % scale.length] ?? 79;
    this.playBellNote(midiToHz(midi), 0.95, 0.18);
  }

  playJumpWarp(): void {
    if (!this.ctx || !this.sfxBus) return;
    const now = this.ctx.currentTime;
    const osc = this.ctx.createOscillator();
    const gain = this.ctx.createGain();
    osc.type = 'sine';
    osc.frequency.setValueAtTime(140, now);
    osc.frequency.exponentialRampToValueAtTime(760, now + 1.8);
    gain.gain.setValueAtTime(0.001, now);
    gain.gain.linearRampToValueAtTime(0.16, now + 0.45);
    gain.gain.exponentialRampToValueAtTime(0.0001, now + 2.1);
    osc.connect(gain);
    gain.connect(this.sfxBus);
    osc.start(now);
    osc.stop(now + 2.15);
  }

  playTouchdown(landed: boolean): void {
    if (!this.ctx || !this.sfxBus) return;
    const now = this.ctx.currentTime;
    const osc = this.ctx.createOscillator();
    const gain = this.ctx.createGain();
    osc.type = 'triangle';
    osc.frequency.setValueAtTime(landed ? 220 : 120, now);
    osc.frequency.exponentialRampToValueAtTime(landed ? 75 : 340, now + 0.35);
    gain.gain.setValueAtTime(0.14, now);
    gain.gain.exponentialRampToValueAtTime(0.0001, now + 0.38);
    osc.connect(gain);
    gain.connect(this.sfxBus);
    osc.start(now);
    osc.stop(now + 0.4);
  }

  playUiTap(): void {
    if (!this.ctx || !this.sfxBus) return;
    const now = this.ctx.currentTime;
    const osc = this.ctx.createOscillator();
    const gain = this.ctx.createGain();
    osc.type = 'sine';
    osc.frequency.setValueAtTime(660, now);
    osc.frequency.exponentialRampToValueAtTime(880, now + 0.06);
    gain.gain.setValueAtTime(0.06, now);
    gain.gain.exponentialRampToValueAtTime(0.0001, now + 0.07);
    osc.connect(gain);
    gain.connect(this.sfxBus);
    osc.start(now);
    osc.stop(now + 0.08);
  }
}
