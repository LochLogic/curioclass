import { INSTRUMENTS, clamp, hexA } from '../core/music';
import {
  MenuState, StageString, stageSize, state, zoneCount, zoneInfo, stringLabel,
} from '../core/state';
import { THEMES } from './themes';

const QWERTY_LABELS = ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';', "'"];

export function drawInstIcon(
  g: CanvasRenderingContext2D,
  id: string,
  color: string,
  x: number,
  y: number,
  px: number,
): void {
  const r = px * 0.48;
  g.save();
  g.translate(x, y);
  g.strokeStyle = color;
  g.fillStyle = color;
  g.lineWidth = Math.max(1.3, px * 0.085);
  g.lineCap = 'round';
  g.lineJoin = 'round';

  switch (id) {
    case 'guitar':
    case 'egtr':
    case 'oud':
      g.beginPath();
      g.ellipse(-r * 0.25, r * 0.25, r * 0.45, r * 0.36, -0.7, 0, Math.PI * 2);
      g.moveTo(0, 0);
      g.lineTo(r * 0.75, -r * 0.75);
      g.stroke();
      if (id === 'egtr') {
        g.beginPath();
        g.moveTo(-r * 0.55, r * 0.1); g.lineTo(-r * 0.1, -r * 0.2);
        g.stroke();
      }
      break;
    case 'harp':
    case 'qanun':
    case 'koto':
      g.beginPath();
      g.moveTo(-r * 0.55, r * 0.65);
      g.lineTo(-r * 0.55, -r * 0.65);
      g.quadraticCurveTo(r * 0.65, -r * 0.65, r * 0.65, r * 0.65);
      g.closePath();
      g.stroke();
      for (let i = -1; i <= 1; i++) {
        g.beginPath();
        g.moveTo(i * r * 0.26, -r * 0.35 + i * r * 0.12);
        g.lineTo(i * r * 0.26, r * 0.6);
        g.stroke();
      }
      break;
    case 'sitar':
      g.beginPath();
      g.arc(-r * 0.3, r * 0.35, r * 0.36, 0, Math.PI * 2);
      g.moveTo(-r * 0.05, r * 0.08);
      g.lineTo(r * 0.7, -r * 0.7);
      g.moveTo(r * 0.45, -r * 0.7);
      g.lineTo(r * 0.72, -r * 0.45);
      g.stroke();
      break;
    case 'piano':
    case 'epiano':
    case 'lofi':
    case 'organ':
      g.strokeRect(-r * 0.78, -r * 0.52, r * 1.56, r * 1.04);
      for (let i = -1; i <= 1; i++) {
        g.beginPath();
        g.moveTo(i * r * 0.38, -r * 0.52);
        g.lineTo(i * r * 0.38, r * 0.52);
        g.stroke();
      }
      g.fillRect(-r * 0.52, -r * 0.52, r * 0.24, r * 0.56);
      g.fillRect(r * 0.08, -r * 0.52, r * 0.24, r * 0.56);
      break;
    case 'marimba':
    case 'kalimba':
    case 'celesta':
      for (let i = -2; i <= 2; i++) {
        const h = r * (0.95 - Math.abs(i) * 0.16);
        g.beginPath();
        g.moveTo(i * r * 0.34, -h * 0.55);
        g.lineTo(i * r * 0.34, h * 0.55);
        g.stroke();
      }
      break;
    case 'steelpan':
    case 'crystal':
      g.beginPath();
      g.arc(0, 0, r * 0.75, 0, Math.PI * 2);
      g.stroke();
      g.beginPath();
      g.arc(0, 0, r * 0.34, 0, Math.PI * 2);
      g.stroke();
      break;
    case 'violin':
    case 'cello':
    case 'strings':
      g.beginPath();
      g.ellipse(0, r * 0.22, r * 0.42, r * 0.46, 0, 0, Math.PI * 2);
      g.moveTo(-r * 0.7, -r * 0.55);
      g.lineTo(r * 0.7, r * 0.45);
      g.stroke();
      break;
    case 'flute':
      g.beginPath();
      g.moveTo(-r * 0.75, r * 0.45);
      g.lineTo(r * 0.75, -r * 0.45);
      g.stroke();
      for (const f of [-0.25, 0.05, 0.35]) {
        g.beginPath();
        g.arc(f * r, -f * r * 0.6, r * 0.1, 0, Math.PI * 2);
        g.fill();
      }
      break;
    case 'trumpet':
      g.beginPath();
      g.moveTo(-r * 0.75, 0);
      g.lineTo(r * 0.4, 0);
      g.lineTo(r * 0.78, -r * 0.42);
      g.lineTo(r * 0.78, r * 0.42);
      g.lineTo(r * 0.4, 0);
      g.stroke();
      break;
    case 'voices':
    case 'pad':
      g.beginPath();
      g.arc(0, 0, r * 0.22, 0, Math.PI * 2);
      g.stroke();
      g.beginPath();
      g.arc(0, 0, r * 0.56, -0.9, 0.9);
      g.stroke();
      g.beginPath();
      g.arc(0, 0, r * 0.56, Math.PI - 0.9, Math.PI + 0.9);
      g.stroke();
      break;
    case 'bells':
      g.beginPath();
      g.moveTo(-r * 0.58, r * 0.42);
      g.quadraticCurveTo(-r * 0.48, -r * 0.6, 0, -r * 0.65);
      g.quadraticCurveTo(r * 0.48, -r * 0.6, r * 0.58, r * 0.42);
      g.closePath();
      g.stroke();
      g.beginPath();
      g.arc(0, r * 0.62, r * 0.14, 0, Math.PI * 2);
      g.fill();
      break;
    case 'synth':
    case 'fmpluck':
      g.beginPath();
      g.moveTo(-r * 0.75, r * 0.35);
      g.lineTo(-r * 0.25, -r * 0.45);
      g.lineTo(r * 0.25, r * 0.45);
      g.lineTo(r * 0.75, -r * 0.35);
      g.stroke();
      break;
    case 'bass':
    case 'sub':
      g.beginPath();
      g.moveTo(-r * 0.75, 0);
      g.bezierCurveTo(-r * 0.35, -r * 0.9, r * 0.35, r * 0.9, r * 0.75, 0);
      g.stroke();
      break;
    case 'drums':
    case 'handdrums':
      g.beginPath();
      g.ellipse(0, -r * 0.2, r * 0.68, r * 0.32, 0, 0, Math.PI * 2);
      g.moveTo(-r * 0.68, -r * 0.2);
      g.lineTo(-r * 0.54, r * 0.5);
      g.quadraticCurveTo(0, r * 0.78, r * 0.54, r * 0.5);
      g.lineTo(r * 0.68, -r * 0.2);
      g.stroke();
      break;
    default:
      g.beginPath();
      g.arc(0, 0, r * 0.5, 0, Math.PI * 2);
      g.stroke();
  }
  g.restore();
}

function drawLabel(
  g: CanvasRenderingContext2D,
  text: string,
  x: number,
  y: number,
  size: number,
  color: string,
  align: CanvasTextAlign = 'center',
  weight = 600,
): void {
  g.save();
  g.font = `${weight} ${size}px -apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, sans-serif`;
  g.textAlign = align;
  g.textBaseline = 'middle';
  g.lineWidth = 3.5;
  g.strokeStyle = 'rgba(5, 8, 14, 0.82)';
  g.strokeText(text, x, y);
  g.fillStyle = color;
  g.fillText(text, x, y);
  g.restore();
}

function roundRectPath(
  g: CanvasRenderingContext2D,
  x: number, y: number, w: number, h: number, r: number,
): void {
  g.beginPath();
  g.roundRect(x, y, w, h, r);
}

function drawString(g: CanvasRenderingContext2D, s: StageString, t: number): void {
  const inst = INSTRUMENTS[s.inst];
  const col = inst.color;
  const coreCol = THEMES[state.settings.theme].stringCore;
  const dx = s.b.x - s.a.x;
  const dy = s.b.y - s.a.y;
  const L = Math.hypot(dx, dy) || 1;
  const ux = dx / L, uy = dy / L;
  let nx = -uy, ny = ux;
  if (ny > 0) { nx = -nx; ny = -ny; }

  const age = t - s.vib.t0;
  const hasHold = Object.keys(s.holds).length > 0;
  const decayRate = inst.sustain ? 1.85 : 2.9;
  const baseAmp = s.vib.amp * Math.exp(-age * decayRate);
  const amp = hasHold ? Math.max(baseAmp, 7.5 + Math.sin(t * 9) * 1.5) : baseAmp;
  const live = amp > 0.25;
  const n = zoneCount(s);
  const selected = state.selectedId === s.id;

  const pl = s.pull;
  const px = pl ? s.a.x + dx * pl.u + (dy / L) * pl.d : 0;
  const py = pl ? s.a.y + dy * pl.u - (dx / L) * pl.d : 0;

  // 8-harmonic standing wave + initial traveling pluck packet
  const omega = clamp(24 + Math.log2(Math.max(55, s.vib.freqHz) / 55) * 9.5, 22, 62);
  const trace = (k: number, phaseShift = 0) => {
    g.beginPath();
    if (pl) {
      g.moveTo(s.a.x, s.a.y);
      g.lineTo(px, py);
      g.lineTo(s.b.x, s.b.y);
      return;
    }
    if (!live) {
      g.moveTo(s.a.x, s.a.y);
      g.lineTo(s.b.x, s.b.y);
      return;
    }
    const N = 56;
    const p = s.vib.pos;
    // Brief traveling triangle envelope on first 90ms
    const packetMix = Math.exp(-age * 16);
    for (let i = 0; i <= N; i++) {
      const u = i / N;
      let d = 0;
      for (let h = 1; h <= 7; h++) {
        d += (Math.sin(h * Math.PI * p) / (h * h)) * Math.sin(h * Math.PI * u) * Math.cos(h * age * omega + phaseShift);
      }
      if (packetMix > 0.02) {
        const tri = u < p ? u / Math.max(0.05, p) : (1 - u) / Math.max(0.05, 1 - p);
        d = d * (1 - packetMix * 0.4) + tri * Math.cos(age * omega) * packetMix * 0.55;
      }
      d *= amp * 1.32 * k;
      const x = s.a.x + dx * u + nx * d;
      const y = s.a.y + dy * u + ny * d;
      if (i) g.lineTo(x, y); else g.moveTo(x, y);
    }
  };

  g.save();
  g.lineCap = 'round';
  g.globalCompositeOperation = 'lighter';
  const glow = live ? clamp(amp / 15, 0.25, 1.0) : (s.near || selected ? 0.22 : 0.05);

  // Outer caustic halo
  trace(1);
  g.strokeStyle = hexA(col, 0.08 + 0.16 * glow);
  g.lineWidth = 10 + 11 * glow;
  g.stroke();

  // Mid luminous aura
  trace(1);
  g.strokeStyle = hexA(col, 0.22 + 0.36 * glow);
  g.lineWidth = 3.6 + 2.8 * glow;
  g.stroke();

  // Multi-phase chromatic harmonic ghosts while vibrating
  if (live) {
    g.strokeStyle = hexA(col, 0.24 * glow);
    g.lineWidth = 1.25;
    trace(-1, 0.18); g.stroke();
    trace(0.58, -0.25); g.stroke();
    trace(-0.58, 0.35); g.stroke();
  }
  g.restore();

  // Crisp luminous string core
  trace(1);
  g.strokeStyle = selected ? '#ffffff' : coreCol;
  g.lineWidth = inst.family === 'perc' ? 2.4 : (selected ? 2.2 : 1.75);
  g.stroke();

  // Active pulled point + semitone bend readout
  if (pl) {
    g.save();
    g.fillStyle = col;
    g.shadowColor = col;
    g.shadowBlur = 12;
    g.beginPath();
    g.arc(px, py, 5.5, 0, Math.PI * 2);
    g.fill();
    g.restore();
    if (Math.abs(s.bend) > 4) {
      drawLabel(
        g,
        (s.bend > 0 ? '+' : '−') + (Math.abs(s.bend) / 100).toFixed(1) + ' st',
        px + nx * 24, py + ny * 24, 12.5, col, 'center', 700,
      );
    }
  }

  // Active zone flash along the string
  const fa = t - s.flash.t;
  if (s.flash.z >= 0 && fa < 0.42) {
    const u0 = s.flash.z / n;
    const u1 = (s.flash.z + 1) / n;
    g.save();
    g.globalCompositeOperation = 'lighter';
    g.strokeStyle = hexA(col, 0.85 * (1 - fa / 0.42));
    g.lineWidth = 5.5;
    g.lineCap = 'round';
    g.beginPath();
    g.moveTo(s.a.x + dx * u0, s.a.y + dy * u0);
    g.lineTo(s.a.x + dx * u1, s.a.y + dy * u1);
    g.stroke();
    g.restore();
  }

  // Subtle fret ticks along the string
  g.strokeStyle = s.near || selected ? 'rgba(255,252,244,0.62)' : 'rgba(255,252,244,0.28)';
  g.lineWidth = 1.1;
  g.beginPath();
  for (let z = 1; z < n; z++) {
    const x = s.a.x + dx * (z / n);
    const y = s.a.y + dy * (z / n);
    g.moveTo(x - nx * 4.5, y - ny * 4.5);
    g.lineTo(x + nx * 4.5, y + ny * 4.5);
  }
  g.stroke();

  // Elegant anchor caps (low end has luminous dot)
  g.strokeStyle = hexA(coreCol, 0.88);
  g.lineWidth = 2.0;
  g.beginPath();
  for (const e of [s.a, s.b]) {
    g.moveTo(e.x - nx * 9, e.y - ny * 9);
    g.lineTo(e.x + nx * 9, e.y + ny * 9);
  }
  g.stroke();
  g.fillStyle = col;
  g.beginPath();
  g.arc(s.a.x, s.a.y, 4.0, 0, Math.PI * 2);
  g.fill();

  // Center instrument badge
  const mx = (s.a.x + s.b.x) * 0.5;
  const my = (s.a.y + s.b.y) * 0.5;
  const fresh = clamp(1 - (t - s.born) / 0.55, 0, 1);
  const dr = 15 + fresh * 8 + (s.near || selected ? 1.8 + Math.sin(t * 5) * 0.8 : 0);

  g.save();
  g.fillStyle = 'rgba(9, 12, 20, 0.88)';
  g.beginPath();
  g.arc(mx, my, dr, 0, Math.PI * 2);
  g.fill();
  g.strokeStyle = hexA(col, s.near || selected ? 1.0 : 0.72);
  g.lineWidth = selected ? 2.4 : 1.75;
  g.beginPath();
  g.arc(mx, my, dr, 0, Math.PI * 2);
  g.stroke();
  drawInstIcon(g, s.inst, col, mx, my, 19);
  g.restore();

  // Note names & string title (shown smoothly on hover, focus, or recent play)
  const showInfo = state.settings.labels && (s.near || selected || t - s.touched < 2.4) && !state.menu;
  if (showInfo) {
    drawLabel(g, stringLabel(s), mx + nx * 32, my + ny * 32, 12.5, col, 'center', 600);
    const size = n > 11 ? 9.5 : 10.5;
    for (let z = 0; z < n; z++) {
      const u = (z + 0.5) / n;
      const info = zoneInfo(s, z);
      const zx = s.a.x + dx * u - nx * 16;
      const zy = s.a.y + dy * u - ny * 16;
      drawLabel(g, info.label, zx, zy, size, 'rgba(248, 246, 238, 0.88)', 'center', 500);
      if (selected && z < QWERTY_LABELS.length) {
        drawLabel(g, QWERTY_LABELS[z], s.a.x + dx * u - nx * 30, s.a.y + dy * u - ny * 30, 8.5, hexA(col, 0.7), 'center', 600);
      }
    }
  }
}

function drawPreview(g: CanvasRenderingContext2D, t: number): void {
  const pv = state.preview;
  if (!pv) return;
  const dx = pv.b.x - pv.a.x, dy = pv.b.y - pv.a.y;
  const L = Math.hypot(dx, dy);
  g.save();
  g.strokeStyle = pv.snapped ? 'rgba(130, 235, 255, 0.85)' : 'rgba(255, 245, 220, 0.72)';
  g.lineWidth = 2;
  g.setLineDash([7, 6]);
  g.lineDashOffset = -t * 36;
  g.beginPath();
  g.moveTo(pv.a.x, pv.a.y);
  g.lineTo(pv.b.x, pv.b.y);
  g.stroke();
  g.setLineDash([]);
  g.fillStyle = '#8ff0c0';
  g.beginPath(); g.arc(pv.a.x, pv.a.y, 4.5, 0, Math.PI * 2); g.fill();
  g.beginPath(); g.arc(pv.b.x, pv.b.y, 4.5, 0, Math.PI * 2); g.fill();
  const zones = clamp(Math.round(L / 68), 5, 14);
  if (L >= 60) {
    drawLabel(
      g,
      `${zones} notes${pv.snapped ? ' · snapped' : ''}`,
      (pv.a.x + pv.b.x) * 0.5, (pv.a.y + pv.b.y) * 0.5 - 18,
      12, '#cfe9ff', 'center', 600,
    );
  }
  g.restore();
}

function drawFxPad(g: CanvasRenderingContext2D, t: number): void {
  const F = state.fx;
  if (!F) return;
  const { from: o, to: p } = F;
  const R = 190;
  g.save();
  g.strokeStyle = 'rgba(155, 205, 255, 0.25)';
  g.lineWidth = 1.4;
  for (const frac of [0.35, 0.68, 1.0]) {
    g.beginPath();
    g.arc(o.x, o.y, R * frac, 0, Math.PI * 2);
    g.stroke();
  }
  g.strokeStyle = 'rgba(155, 205, 255, 0.55)';
  g.lineWidth = 2;
  g.beginPath();
  g.moveTo(o.x, o.y);
  g.lineTo(p.x, p.y);
  g.stroke();
  g.fillStyle = '#9eeaff';
  g.beginPath();
  g.arc(p.x, p.y, 7 + Math.sin(t * 10) * 1.2, 0, Math.PI * 2);
  g.fill();

  drawLabel(g, 'AIR / THIN', o.x, o.y - R - 14, 10, 'rgba(200,225,255,0.75)');
  drawLabel(g, 'WARM / DARK', o.x, o.y + R + 14, 10, 'rgba(200,225,255,0.75)');
  drawLabel(g, 'ECHO', o.x + R + 24, o.y, 10, 'rgba(200,225,255,0.75)');
  const readouts: string[] = [];
  if (F.dark > 0.05) readouts.push(`Dark ${Math.round(F.dark * 100)}%`);
  if (F.thin > 0.05) readouts.push(`Air ${Math.round(F.thin * 100)}%`);
  if (F.echo > 0.05) readouts.push(`Echo ${Math.round(F.echo * 100)}%`);
  if (readouts.length) drawLabel(g, readouts.join(' · '), p.x, p.y - 20, 12, '#e8f5ff');
  g.restore();
}

function drawParticles(g: CanvasRenderingContext2D, dt: number): void {
  const list = state.particles;
  if (!list.length) return;
  g.save();
  g.globalCompositeOperation = 'lighter';
  for (let i = list.length - 1; i >= 0; i--) {
    const p = list[i];
    p.life += dt;
    if (p.life >= p.maxLife) {
      list.splice(i, 1);
      continue;
    }
    const k = 1 - p.life / p.maxLife;
    p.x += p.vx * dt;
    p.y += p.vy * dt;
    p.vx *= 0.965;
    p.vy *= 0.965;
    g.fillStyle = hexA(p.color, k * 0.72);
    g.beginPath();
    g.arc(p.x, p.y, p.r * (0.45 + 0.55 * k), 0, Math.PI * 2);
    g.fill();
  }
  g.restore();
}

function drawPops(g: CanvasRenderingContext2D, t: number): void {
  const list = state.pops;
  for (let i = list.length - 1; i >= 0; i--) {
    const p = list[i];
    const age = t - p.t0;
    if (age > 0.85) {
      list.splice(i, 1);
      continue;
    }
    const k = 1 - age / 0.85;
    g.save();
    g.globalAlpha = k;
    drawLabel(g, p.text, p.x, p.y - age * 34, 13.5, p.color, 'center', 700);
    g.restore();
  }
}

function drawMenu(g: CanvasRenderingContext2D, M: MenuState, t: number): void {
  const openAnim = clamp((t - M.openedAt) / 0.14, 0, 1);
  g.save();
  g.globalAlpha = openAnim;

  // Backdrop panel for grid menus
  if (M.kind !== 'hub') {
    let minX = Infinity, minY = Infinity, maxX = -Infinity, maxY = -Infinity;
    for (const it of M.items) {
      minX = Math.min(minX, it.x - it.w * 0.5);
      minY = Math.min(minY, it.y - it.h * 0.5);
      maxX = Math.max(maxX, it.x + it.w * 0.5);
      maxY = Math.max(maxY, it.y + it.h * 0.5);
    }
    const pad = 16;
    const headerH = 28;
    roundRectPath(g, minX - pad, minY - pad - headerH, maxX - minX + pad * 2, maxY - minY + pad * 2 + headerH, 16);
    g.fillStyle = 'rgba(10, 14, 22, 0.92)';
    g.fill();
    g.strokeStyle = 'rgba(255, 255, 255, 0.14)';
    g.lineWidth = 1.2;
    g.stroke();

    const titles: Record<string, string> = {
      inst: 'Choose Instrument (30)',
      scale: 'String Scale',
      key: 'String Key',
      oct: 'Octave Offset',
      mode: 'Chord / Voicing Mode',
    };
    drawLabel(g, titles[M.kind] || '', (minX + maxX) * 0.5, minY - pad - headerH * 0.45, 13, '#e8eef8', 'center', 600);
  } else {
    // Subtle connecting ring for hub
    g.strokeStyle = 'rgba(255, 255, 255, 0.12)';
    g.lineWidth = 1.2;
    g.beginPath();
    g.arc(M.cx, M.cy, 74, 0, Math.PI * 2);
    g.stroke();
  }

  for (const it of M.items) {
    const hovered = M.hover === it.id;
    const col = it.color || '#a5d8ff';
    if (it.r) {
      g.beginPath();
      g.arc(it.x, it.y, it.r + (hovered ? 2.5 : 0), 0, Math.PI * 2);
      g.fillStyle = hovered ? 'rgba(30, 42, 66, 0.96)' : 'rgba(11, 15, 24, 0.92)';
      g.fill();
      g.strokeStyle = hovered ? col : (it.active ? hexA(col, 0.85) : 'rgba(255,255,255,0.2)');
      g.lineWidth = hovered || it.active ? 2 : 1.2;
      g.stroke();
      drawLabel(g, it.label, it.x, it.y - (it.sub ? 5 : 0), 11.5, hovered ? '#ffffff' : col, 'center', 600);
      if (it.sub) drawLabel(g, it.sub, it.x, it.y + 10, 9.5, 'rgba(210,220,235,0.75)', 'center', 500);
    } else {
      roundRectPath(g, it.x - it.w * 0.5, it.y - it.h * 0.5, it.w, it.h, 10);
      g.fillStyle = hovered
        ? hexA(col, 0.24)
        : it.active
          ? hexA(col, 0.16)
          : 'rgba(255, 255, 255, 0.045)';
      g.fill();
      g.strokeStyle = hovered || it.active ? hexA(col, 0.9) : 'rgba(255, 255, 255, 0.1)';
      g.lineWidth = hovered || it.active ? 1.6 : 1;
      g.stroke();

      if (it.kind === 'inst' && typeof it.value === 'string') {
        drawInstIcon(g, it.value, col, it.x, it.y - 8, 20);
        drawLabel(g, it.label, it.x, it.y + 16, 10, hovered ? '#ffffff' : 'rgba(235,240,248,0.88)', 'center', 500);
      } else {
        drawLabel(g, it.label, it.x, it.y - (it.sub ? 6 : 0), 11.5, hovered ? '#ffffff' : col, 'center', 600);
        if (it.sub) drawLabel(g, it.sub, it.x, it.y + 10, 9.5, 'rgba(210,220,235,0.72)', 'center', 500);
      }
    }
  }
  g.restore();
}

function drawCursorHalo(g: CanvasRenderingContext2D): void {
  const m = state.mouse;
  if (!m.inside || m.overHud || state.menu || state.fx) return;
  const activeStrum = state.settings.strumMode === 'hover' || m.down;
  g.save();
  const r = activeStrum ? 7 + Math.min(7, m.speed * 0.008) : 5;
  g.strokeStyle = m.rightDown
    ? 'rgba(180, 145, 255, 0.75)'
    : activeStrum
      ? 'rgba(155, 225, 255, 0.52)'
      : 'rgba(255, 255, 255, 0.22)';
  g.lineWidth = 1.4;
  g.beginPath();
  g.arc(m.x, m.y, r, 0, Math.PI * 2);
  g.stroke();
  g.restore();
}

export function renderStage2D(g: CanvasRenderingContext2D, t: number, dt: number): void {
  g.clearRect(0, 0, stageSize.w, stageSize.h);

  // Subtle empty-stage prompt when user clears all strings
  if (state.strings.length === 0 && !state.preview) {
    drawLabel(
      g,
      'Drag anywhere to stretch a string · or open Setups for a ready-made stage',
      stageSize.w * 0.5,
      stageSize.h * 0.5,
      15,
      'rgba(210, 225, 245, 0.55)',
      'center',
      500,
    );
  }

  for (const s of state.strings) {
    drawString(g, s, t);
  }
  drawPreview(g, t);
  drawFxPad(g, t);
  drawParticles(g, dt);
  drawPops(g, t);
  if (state.menu) drawMenu(g, state.menu, t);
  drawCursorHalo(g);
}
