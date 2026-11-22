import { hexToRgb01 } from '../core/music';

export interface WaveImpulse {
  x0: number; // normalized 0..1
  y0: number; // normalized 0..1
  x1: number;
  y1: number;
  freqHz: number;
  amp: number;
  r: number;
  g: number;
  b: number;
  isPoint: boolean;
}

export interface ContinuousEmitter {
  id: string;
  x0: number;
  y0: number;
  x1: number;
  y1: number;
  freqHz: number;
  amp: number;
  r: number;
  g: number;
  b: number;
  phase: number;
}

export interface AudioBands {
  sub: number;
  mid: number;
  air: number;
  rms: number;
}

class TelemetryBus {
  private impulses: WaveImpulse[] = [];
  private emitters = new Map<string, ContinuousEmitter>();
  public bands: AudioBands = { sub: 0, mid: 0, air: 0, rms: 0 };
  private fftData: Uint8Array<ArrayBuffer> | null = null;
  private timeData: Uint8Array<ArrayBuffer> | null = null;

  pushStringImpulse(
    ax: number, ay: number, bx: number, by: number,
    stageW: number, stageH: number,
    freqHz: number, vel: number, colorHex: string,
  ): void {
    const [r, g, b] = hexToRgb01(colorHex);
    this.impulses.push({
      x0: ax / stageW, y0: ay / stageH,
      x1: bx / stageW, y1: by / stageH,
      freqHz,
      amp: Math.min(1.2, 0.35 + vel * 0.85),
      r, g, b,
      isPoint: false,
    });
    if (this.impulses.length > 24) this.impulses.shift();
  }

  pushPointImpulse(
    x: number, y: number,
    stageW: number, stageH: number,
    freqHz: number, vel: number, colorHex: string,
  ): void {
    const [r, g, b] = hexToRgb01(colorHex);
    this.impulses.push({
      x0: x / stageW, y0: y / stageH,
      x1: x / stageW, y1: y / stageH,
      freqHz,
      amp: Math.min(1.25, 0.3 + vel * 0.9),
      r, g, b,
      isPoint: true,
    });
    if (this.impulses.length > 24) this.impulses.shift();
  }

  setEmitter(
    id: string,
    ax: number, ay: number, bx: number, by: number,
    stageW: number, stageH: number,
    freqHz: number, vel: number, colorHex: string,
  ): void {
    const [r, g, b] = hexToRgb01(colorHex);
    const prev = this.emitters.get(id);
    this.emitters.set(id, {
      id,
      x0: ax / stageW, y0: ay / stageH,
      x1: bx / stageW, y1: by / stageH,
      freqHz,
      amp: Math.min(0.65, 0.22 + vel * 0.42),
      r, g, b,
      phase: prev ? prev.phase : 0,
    });
  }

  removeEmitter(id: string): void {
    this.emitters.delete(id);
  }

  clearEmitters(): void {
    this.emitters.clear();
  }

  drainImpulses(maxCount = 12): WaveImpulse[] {
    if (this.impulses.length === 0) return [];
    const out = this.impulses.splice(0, maxCount);
    return out;
  }

  getEmitters(): ContinuousEmitter[] {
    return Array.from(this.emitters.values());
  }

  sampleAnalyser(analyser: AnalyserNode | null, dt: number): void {
    if (!analyser) {
      const k = Math.exp(-dt * 6);
      this.bands.sub *= k;
      this.bands.mid *= k;
      this.bands.air *= k;
      this.bands.rms *= k;
      return;
    }
    const bins = analyser.frequencyBinCount;
    if (!this.fftData || this.fftData.length !== bins) {
      this.fftData = new Uint8Array(new ArrayBuffer(bins));
      this.timeData = new Uint8Array(new ArrayBuffer(bins));
    }
    analyser.getByteFrequencyData(this.fftData);
    analyser.getByteTimeDomainData(this.timeData!);

    let subSum = 0, midSum = 0, airSum = 0;
    const subEnd = Math.min(10, bins);
    const midEnd = Math.min(72, bins);
    const airEnd = Math.min(220, bins);
    for (let i = 1; i < subEnd; i++) subSum += this.fftData[i];
    for (let i = subEnd; i < midEnd; i++) midSum += this.fftData[i];
    for (let i = midEnd; i < airEnd; i++) airSum += this.fftData[i];

    let rmsAcc = 0;
    for (let i = 0; i < this.timeData!.length; i++) {
      const v = (this.timeData![i] - 128) / 128;
      rmsAcc += v * v;
    }
    const rmsRaw = Math.sqrt(rmsAcc / this.timeData!.length);

    const smooth = 1 - Math.exp(-dt * 14);
    this.bands.sub += (subSum / Math.max(1, (subEnd - 1) * 255) - this.bands.sub) * smooth;
    this.bands.mid += (midSum / Math.max(1, (midEnd - subEnd) * 255) - this.bands.mid) * smooth;
    this.bands.air += (airSum / Math.max(1, (airEnd - midEnd) * 255) - this.bands.air) * smooth;
    this.bands.rms += (Math.min(1, rmsRaw * 2.4) - this.bands.rms) * smooth;
  }
}

export const telemetry = new TelemetryBus();
