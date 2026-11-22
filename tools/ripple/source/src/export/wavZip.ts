import { BEATS, BeatPart, PARTS } from '../core/music';
import { state, stepDur, transport } from '../core/state';
import { buildGraph } from '../audio/engine';
import { scheduleStep } from '../audio/sequencer';

export function encodeWavFromInterleaved(left: Float32Array, right: Float32Array, sampleRate: number): Uint8Array {
  const n = left.length;
  const buf = new ArrayBuffer(44 + n * 4);
  const v = new DataView(buf);
  const str = (off: number, s: string) => {
    for (let i = 0; i < s.length; i++) v.setUint8(off + i, s.charCodeAt(i));
  };
  str(0, 'RIFF');
  v.setUint32(4, 36 + n * 4, true);
  str(8, 'WAVE');
  str(12, 'fmt ');
  v.setUint32(16, 16, true);
  v.setUint16(20, 1, true); // PCM
  v.setUint16(22, 2, true); // Stereo
  v.setUint32(24, sampleRate, true);
  v.setUint32(28, sampleRate * 4, true);
  v.setUint16(32, 4, true);
  v.setUint16(34, 16, true);
  str(36, 'data');
  v.setUint32(40, n * 4, true);

  let off = 44;
  for (let i = 0; i < n; i++) {
    const l = Math.max(-1, Math.min(1, left[i]));
    const r = Math.max(-1, Math.min(1, right[i]));
    v.setInt16(off, l < 0 ? l * 0x8000 : l * 0x7fff, true);
    v.setInt16(off + 2, r < 0 ? r * 0x8000 : r * 0x7fff, true);
    off += 4;
  }
  return new Uint8Array(buf);
}

export function wavBytesFromAudioBuffer(ab: AudioBuffer): Uint8Array {
  const l = ab.getChannelData(0);
  const r = ab.numberOfChannels > 1 ? ab.getChannelData(1) : l;
  return encodeWavFromInterleaved(l, r, ab.sampleRate);
}

const CRC_TABLE = (() => {
  const t = new Uint32Array(256);
  for (let n = 0; n < 256; n++) {
    let c = n;
    for (let k = 0; k < 8; k++) c = (c & 1) ? (0xedb88320 ^ (c >>> 1)) : (c >>> 1);
    t[n] = c >>> 0;
  }
  return t;
})();

function crc32(u8: Uint8Array): number {
  let c = 0xffffffff;
  for (let i = 0; i < u8.length; i++) c = CRC_TABLE[(c ^ u8[i]) & 0xff] ^ (c >>> 8);
  return (c ^ 0xffffffff) >>> 0;
}

export function zipBlob(files: Array<{ name: string; bytes: Uint8Array }>): Blob {
  const enc = new TextEncoder();
  const parts: BlobPart[] = [];
  const central: Uint8Array[] = [];
  let offset = 0;

  for (const f of files) {
    const nameBytes = enc.encode(f.name);
    const crc = crc32(f.bytes);
    const size = f.bytes.length;

    const lh = new ArrayBuffer(30 + nameBytes.length);
    const lv = new DataView(lh);
    lv.setUint32(0, 0x04034b50, true);
    lv.setUint16(4, 20, true);
    lv.setUint16(8, 0, true);
    lv.setUint32(14, crc, true);
    lv.setUint32(18, size, true);
    lv.setUint32(22, size, true);
    lv.setUint16(26, nameBytes.length, true);
    new Uint8Array(lh, 30).set(nameBytes);
    const lhU8 = new Uint8Array(lh);
    parts.push(lhU8, f.bytes as BlobPart);

    const ch = new ArrayBuffer(46 + nameBytes.length);
    const cv = new DataView(ch);
    cv.setUint32(0, 0x02014b50, true);
    cv.setUint16(4, 20, true);
    cv.setUint16(6, 20, true);
    cv.setUint32(16, crc, true);
    cv.setUint32(20, size, true);
    cv.setUint32(24, size, true);
    cv.setUint16(28, nameBytes.length, true);
    cv.setUint32(42, offset, true);
    new Uint8Array(ch, 46).set(nameBytes);
    central.push(new Uint8Array(ch));

    offset += lhU8.length + size;
  }

  let cdSize = 0;
  for (const c of central) { parts.push(c as BlobPart); cdSize += c.length; }

  const eocd = new ArrayBuffer(22);
  const ev = new DataView(eocd);
  ev.setUint32(0, 0x06054b50, true);
  ev.setUint16(8, files.length, true);
  ev.setUint16(10, files.length, true);
  ev.setUint32(12, cdSize, true);
  ev.setUint32(16, offset, true);
  parts.push(new Uint8Array(eocd));

  return new Blob(parts, { type: 'application/zip' });
}

export async function renderStemsZip(onStatus: (msg: string) => void): Promise<Blob | null> {
  const activeParts = PARTS.filter(p => transport.parts[p]);
  const activeLayers = transport.layers.filter(L => !L.muted && L.events.length > 0);
  if (activeParts.length === 0 && activeLayers.length === 0) {
    onStatus('Enable at least one beat part or record a loop layer first.');
    return null;
  }

  // Render 4 bars (or longest loop layer) + 2s reverb tail
  const maxSteps = Math.max(64, ...activeLayers.map(L => L.len));
  const durSec = maxSteps * stepDur() + 2.2;
  const sr = 44100;
  const files: Array<{ name: string; bytes: Uint8Array }> = [];

  const renderOne = async (
    label: string,
    partsSel: Record<BeatPart, boolean>,
    layersSel: typeof activeLayers,
  ) => {
    onStatus(`Rendering ${label}...`);
    const offCtx = new OfflineAudioContext(2, Math.ceil(durSec * sr), sr);
    const graph = buildGraph(offCtx, { offline: true });
    const layerNodes = new Map<number, GainNode>();
    for (const L of layersSel) {
      const gn = offCtx.createGain();
      gn.gain.value = L.vol;
      gn.connect(graph.live);
      layerNodes.set(L.id, gn);
    }
    const sd = stepDur();
    for (let step = 0; step < maxSteps; step++) {
      scheduleStep(step, 0.05 + step * sd, {
        parts: partsSel,
        layers: layersSel,
        dest: L => layerNodes.get(L.id) || graph.live,
        beatDest: graph.beat,
        graph,
      });
    }
    const rendered = await offCtx.startRendering();
    files.push({ name: `${label}.wav`, bytes: wavBytesFromAudioBuffer(rendered) });
  };

  const emptyParts = Object.fromEntries(PARTS.map(p => [p, false])) as Record<BeatPart, boolean>;
  const beatLabels = BEATS[transport.beat].labels;

  for (const p of activeParts) {
    const idx = PARTS.indexOf(p);
    const nm = `beat-${beatLabels[idx].toLowerCase().replace(/\s+/g, '_')}`;
    await renderOne(nm, { ...emptyParts, [p]: true }, []);
  }
  for (let i = 0; i < activeLayers.length; i++) {
    await renderOne(`layer-${i + 1}`, emptyParts, [activeLayers[i]]);
  }
  await renderOne('full-mix', { ...transport.parts }, activeLayers);

  onStatus(`Packing ${files.length} WAV stems...`);
  return zipBlob(files);
}
