import { audio, ensurePcmTap, initAudio } from '../audio/engine';
import { stageSize } from '../core/state';
import { encodeWavFromInterleaved } from './wavZip';

export interface RecordingTake {
  videoBlob: Blob | null;
  videoUrl: string | null;
  videoExt: string;
  wavBlob: Blob;
  wavUrl: string;
  left: Float32Array;
  right: Float32Array;
  sampleRate: number;
  durationSec: number;
}

class StageRecorder {
  public on = false;
  public mode: 'video' | 'audio' = 'video';
  public startedAt = 0;
  public lastTake: RecordingTake | null = null;

  private mr: MediaRecorder | null = null;
  private videoChunks: Blob[] = [];
  private pcmL: Float32Array[] = [];
  private pcmR: Float32Array[] = [];
  private pcmSamples = 0;
  private compCanvas: HTMLCanvasElement | null = null;
  private compCtx: CanvasRenderingContext2D | null = null;
  private onDone: ((take: RecordingTake) => void) | null = null;

  private pickMime(): { mime: string; ext: string } {
    const candidates = [
      { mime: 'video/webm;codecs=vp9,opus', ext: 'webm' },
      { mime: 'video/webm;codecs=vp8,opus', ext: 'webm' },
      { mime: 'video/webm', ext: 'webm' },
      { mime: 'video/mp4', ext: 'mp4' },
    ];
    if (typeof MediaRecorder !== 'undefined') {
      for (const c of candidates) {
        if (MediaRecorder.isTypeSupported(c.mime)) return c;
      }
    }
    return { mime: '', ext: 'webm' };
  }

  public start(
    waveCanvas: HTMLCanvasElement,
    fgCanvas: HTMLCanvasElement,
    onDone: (take: RecordingTake) => void,
  ): boolean {
    if (this.on) return false;
    const g = initAudio();
    if (!g) return false;
    ensurePcmTap();

    this.on = true;
    this.startedAt = performance.now();
    this.pcmL = [];
    this.pcmR = [];
    this.pcmSamples = 0;
    this.videoChunks = [];
    this.onDone = onDone;

    audio.pcmCallback = (l, r) => {
      if (!this.on) return;
      this.pcmL.push(new Float32Array(l));
      this.pcmR.push(new Float32Array(r));
      this.pcmSamples += l.length;
    };

    if (this.mode === 'video' && typeof MediaRecorder !== 'undefined') {
      if (!this.compCanvas) {
        this.compCanvas = document.createElement('canvas');
        this.compCtx = this.compCanvas.getContext('2d');
      }
      this.compCanvas.width = stageSize.w;
      this.compCanvas.height = stageSize.h;
      this.compositeFrame(waveCanvas, fgCanvas);

      const tracks: MediaStreamTrack[] = [];
      const vStream = this.compCanvas.captureStream(30);
      tracks.push(...vStream.getVideoTracks());
      if (g.streamDest) tracks.push(...g.streamDest.stream.getAudioTracks());

      const mixed = new MediaStream(tracks);
      const { mime } = this.pickMime();
      try {
        this.mr = new MediaRecorder(mixed, mime ? { mimeType: mime, videoBitsPerSecond: 5_000_000 } : undefined);
        this.mr.ondataavailable = ev => {
          if (ev.data && ev.data.size > 0) this.videoChunks.push(ev.data);
        };
        this.mr.onstop = () => this.finalize();
        this.mr.start(250);
      } catch {
        this.mr = null;
      }
    }
    return true;
  }

  public compositeFrame(waveCanvas: HTMLCanvasElement, fgCanvas: HTMLCanvasElement): void {
    if (!this.on || !this.compCtx || !this.compCanvas) return;
    if (this.compCanvas.width !== stageSize.w || this.compCanvas.height !== stageSize.h) {
      this.compCanvas.width = stageSize.w;
      this.compCanvas.height = stageSize.h;
    }
    this.compCtx.drawImage(waveCanvas, 0, 0, this.compCanvas.width, this.compCanvas.height);
    this.compCtx.drawImage(fgCanvas, 0, 0, this.compCanvas.width, this.compCanvas.height);
  }

  public stop(): void {
    if (!this.on) return;
    this.on = false;
    audio.pcmCallback = null;
    if (this.mr && this.mr.state !== 'inactive') {
      this.mr.stop();
    } else {
      this.finalize();
    }
  }

  private finalize(): void {
    const sr = audio.g?.ctx.sampleRate ?? 44100;
    const left = new Float32Array(this.pcmSamples);
    const right = new Float32Array(this.pcmSamples);
    let off = 0;
    for (let i = 0; i < this.pcmL.length; i++) {
      left.set(this.pcmL[i], off);
      right.set(this.pcmR[i], off);
      off += this.pcmL[i].length;
    }

    if (this.lastTake) {
      if (this.lastTake.videoUrl) URL.revokeObjectURL(this.lastTake.videoUrl);
      URL.revokeObjectURL(this.lastTake.wavUrl);
    }

    const wavBytes = encodeWavFromInterleaved(left, right, sr);
    const wavBlob = new Blob([wavBytes as BlobPart], { type: 'audio/wav' });
    const wavUrl = URL.createObjectURL(wavBlob);

    let videoBlob: Blob | null = null;
    let videoUrl: string | null = null;
    const { mime, ext } = this.pickMime();
    if (this.videoChunks.length > 0) {
      videoBlob = new Blob(this.videoChunks, { type: mime || 'video/webm' });
      videoUrl = URL.createObjectURL(videoBlob);
    }

    const take: RecordingTake = {
      videoBlob,
      videoUrl,
      videoExt: ext,
      wavBlob,
      wavUrl,
      left,
      right,
      sampleRate: sr,
      durationSec: Math.max(0.1, (performance.now() - this.startedAt) / 1000),
    };
    this.lastTake = take;
    this.mr = null;
    this.onDone?.(take);
  }

}

export const recorder = new StageRecorder();

export function downloadBlob(blob: Blob, filename: string): void {
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = filename;
  document.body.appendChild(a);
  a.click();
  a.remove();
  setTimeout(() => URL.revokeObjectURL(url), 5000);
}
