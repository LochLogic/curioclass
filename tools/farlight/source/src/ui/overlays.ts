import {
  getNearbyStars,
  SOL_STAR_REF,
  starDistanceLY,
  type PlanetData,
  type StarKind,
  type StarRef,
  type StarSystem,
} from '../sim/galaxy.ts';
import {
  checkJump,
  distanceToHomeLY,
  planetScanKey,
  type JourneyState,
} from '../sim/journey.ts';
import {
  evaluateEnding,
  SHIP_HULLS,
  STORY_TRANSMISSIONS,
  type ShipHullId,
} from '../sim/narrative.ts';
import type { ShipState } from '../sim/flight.ts';

export type OverlayMode = 'none' | 'galaxy' | 'system' | 'journal';

export interface OverlayCallbacks {
  onJumpTo(star: StarRef): void;
  onSelectTarget(star: StarRef): void;
  onPointAtPlanet(planet: PlanetData): void;
  onDescendToPlanet(planet: PlanetData): void;
  onSelectShip(hull: ShipHullId): void;
  onResetJourney(): void;
  onClose(): void;
}

const STAR_COLORS: Record<StarKind, string> = {
  'warm-sun': '#ffd97d',
  'amber-dwarf': '#ff9452',
  'sky-giant': '#7ec8ff',
  pulsar: '#63f5ff',
  'black-hole': '#e091ff',
};

const STAR_TITLES: Record<StarKind, string> = {
  'warm-sun': 'Golden Sun',
  'amber-dwarf': 'Sunset Star',
  'sky-giant': 'Blue Giant',
  pulsar: 'Pulsar',
  'black-hole': 'Black Hole',
};

export class Overlays {
  private container: HTMLElement;
  private mode: OverlayMode = 'none';
  private callbacks: OverlayCallbacks;

  private galaxyCanvas: HTMLCanvasElement | null = null;
  private mapRotY = 0.0;
  private mapTilt = 1.48; // Clean near-top-down default for effortless reading!
  private mapZoom = 1.0;
  private topDownMode = true;
  private draggingMap = false;
  private lastMouseX = 0;
  private lastMouseY = 0;
  private projectedStars: Array<{ star: StarRef; sx: number; sy: number; r: number }> = [];
  private selectedStar: StarRef | null = null;

  constructor(root: HTMLElement, callbacks: OverlayCallbacks) {
    this.callbacks = callbacks;
    this.container = document.createElement('div');
    this.container.className = 'overlay-backdrop hidden';
    root.appendChild(this.container);
  }

  getMode(): OverlayMode {
    return this.mode;
  }

  open(mode: OverlayMode, journey: JourneyState, system: StarSystem, ship: ShipState): void {
    this.mode = mode;
    if (mode === 'none') {
      this.container.classList.add('hidden');
      this.container.innerHTML = '';
      this.galaxyCanvas = null;
      return;
    }
    this.container.classList.remove('hidden');
    if (mode === 'galaxy') {
      this.selectedStar = journey.targetStar ?? journey.currentStar;
      this.renderGalaxyModal(journey, ship);
    } else if (mode === 'system') {
      this.renderSystemModal(journey, system);
    } else if (mode === 'journal') {
      this.renderJournalModal(journey);
    }
  }

  private renderGalaxyModal(journey: JourneyState, ship: ShipState): void {
    const homeDist = Math.round(distanceToHomeLY(journey));
    const nearby = getNearbyStars(journey.galaxySeed, journey.currentStar, journey.jumpRangeLY * 1.65);
    if (distanceToHomeLY(journey) <= journey.jumpRangeLY * 2.2 && !nearby.some((s) => s.id === SOL_STAR_REF.id)) {
      nearby.push(SOL_STAR_REF);
    }

    const reachable = nearby
      .filter((s) => s.id !== journey.currentStar.id && starDistanceLY(journey.currentStar, s) <= journey.jumpRangeLY)
      .sort((a, b) => starDistanceLY(a, SOL_STAR_REF) - starDistanceLY(b, SOL_STAR_REF));

    const bestHomeStar = reachable[0] ?? null;

    this.container.innerHTML = `
      <div class="card modal-panel">
        <div class="modal-header">
          <div>
            <h2>🗺 Galaxy Star Chart</h2>
            <p class="modal-sub">Click any star inside the glowing ring (or pick from the list) to plot a jump! <strong>Sol (Home)</strong> is <strong>${homeDist} LY</strong> away.</p>
          </div>
          <div style="display:flex;gap:8px;">
            <button class="pill-btn" id="ov-view-toggle">${this.topDownMode ? 'Switch to 3D Tilt' : 'Switch to Top-Down'}</button>
            <button class="pill-btn" id="ov-close">Close (Esc)</button>
          </div>
        </div>
        <div class="galaxy-layout">
          <div>
            <canvas id="galaxy-canvas" width="640" height="400"></canvas>
            <div class="map-legend">
              <span><i style="background:#ffd97d"></i>Golden Sun</span>
              <span><i style="background:#ff9452"></i>Sunset Star</span>
              <span><i style="background:#7ec8ff"></i>Blue Giant</span>
              <span><i style="background:#63f5ff"></i>Pulsar</span>
              <span><i style="background:#e091ff"></i>Black Hole</span>
              <span><i style="background:#ffd166;box-shadow:0 0 8px #ffd166"></i>Home (Sol)</span>
            </div>
          </div>
          <div class="galaxy-sidebar" id="galaxy-sidebar"></div>
        </div>
      </div>
    `;

    this.container.querySelector('#ov-close')!.addEventListener('click', () => this.callbacks.onClose());
    const viewBtn = this.container.querySelector('#ov-view-toggle') as HTMLButtonElement;
    const canvas = this.container.querySelector('#galaxy-canvas') as HTMLCanvasElement;
    this.galaxyCanvas = canvas;

    const redraw = () => this.drawGalaxyCanvas(canvas, journey, nearby, bestHomeStar);
    const updateSidebar = () => this.renderGalaxySidebar(journey, ship, reachable, bestHomeStar, redraw);

    viewBtn.addEventListener('click', () => {
      this.topDownMode = !this.topDownMode;
      this.mapTilt = this.topDownMode ? 1.48 : 0.62;
      if (this.topDownMode) this.mapRotY = 0;
      viewBtn.textContent = this.topDownMode ? 'Switch to 3D Tilt' : 'Switch to Top-Down';
      redraw();
    });

    canvas.addEventListener('pointerdown', (e) => {
      this.draggingMap = true;
      this.lastMouseX = e.clientX;
      this.lastMouseY = e.clientY;
    });
    window.addEventListener('pointerup', () => {
      this.draggingMap = false;
    });
    canvas.addEventListener('pointermove', (e) => {
      if (!this.draggingMap) return;
      this.mapRotY += (e.clientX - this.lastMouseX) * 0.008;
      if (!this.topDownMode) {
        this.mapTilt = Math.max(0.25, Math.min(1.48, this.mapTilt + (e.clientY - this.lastMouseY) * 0.006));
      }
      this.lastMouseX = e.clientX;
      this.lastMouseY = e.clientY;
      redraw();
    });
    canvas.addEventListener('wheel', (e) => {
      e.preventDefault();
      this.mapZoom = Math.max(0.7, Math.min(2.2, this.mapZoom * (e.deltaY > 0 ? 0.92 : 1.09)));
      redraw();
    }, { passive: false });

    canvas.addEventListener('click', (e) => {
      const rect = canvas.getBoundingClientRect();
      const mx = (e.clientX - rect.left) * (canvas.width / rect.width);
      const my = (e.clientY - rect.top) * (canvas.height / rect.height);
      let best: StarRef | null = null;
      let bestD = 26;
      for (const item of this.projectedStars) {
        const d = Math.hypot(item.sx - mx, item.sy - my);
        if (d < bestD) {
          bestD = d;
          best = item.star;
        }
      }
      if (best) {
        this.selectedStar = best;
        this.callbacks.onSelectTarget(best);
        redraw();
        updateSidebar();
      }
    });

    redraw();
    updateSidebar();
  }

  private drawGalaxyCanvas(
    canvas: HTMLCanvasElement,
    journey: JourneyState,
    stars: StarRef[],
    bestHomeStar: StarRef | null,
  ): void {
    const ctx = canvas.getContext('2d')!;
    const w = canvas.width;
    const h = canvas.height;
    ctx.clearRect(0, 0, w, h);

    const bg = ctx.createRadialGradient(w * 0.5, h * 0.5, 20, w * 0.5, h * 0.5, w * 0.62);
    bg.addColorStop(0, '#0f1c38');
    bg.addColorStop(1, '#060a16');
    ctx.fillStyle = bg;
    ctx.fillRect(0, 0, w, h);

    const scale = (145 / journey.jumpRangeLY) * this.mapZoom;
    const cosY = Math.cos(this.mapRotY);
    const sinY = Math.sin(this.mapRotY);
    const sinT = Math.sin(this.mapTilt);

    const project = (x: number, y: number, z: number) => {
      const dx = x - journey.currentStar.x;
      const dy = y - journey.currentStar.y;
      const dz = z - journey.currentStar.z;
      const rx = dx * cosY - dz * sinY;
      const rz = dx * sinY + dz * cosY;
      return {
        sx: w * 0.5 + rx * scale,
        sy: h * 0.5 + rz * scale * sinT - (this.topDownMode ? 0 : dy * scale * 0.7),
        depth: rz,
      };
    };

    // Subtle compass crosshairs
    ctx.strokeStyle = 'rgba(255, 255, 255, 0.06)';
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(0, h * 0.5);
    ctx.lineTo(w, h * 0.5);
    ctx.moveTo(w * 0.5, 0);
    ctx.lineTo(w * 0.5, h);
    ctx.stroke();

    // Inner (50%) and Outer (100% Max Jump) range rings with clear labels
    ctx.save();
    ctx.strokeStyle = 'rgba(110, 238, 255, 0.16)';
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.ellipse(w * 0.5, h * 0.5, journey.jumpRangeLY * 0.5 * scale, journey.jumpRangeLY * 0.5 * scale * sinT, 0, 0, Math.PI * 2);
    ctx.stroke();

    ctx.strokeStyle = 'rgba(110, 238, 255, 0.45)';
    ctx.lineWidth = 2;
    ctx.setLineDash([7, 5]);
    ctx.beginPath();
    ctx.ellipse(w * 0.5, h * 0.5, journey.jumpRangeLY * scale, journey.jumpRangeLY * scale * sinT, 0, 0, Math.PI * 2);
    ctx.stroke();
    ctx.restore();

    ctx.fillStyle = 'rgba(140, 238, 255, 0.75)';
    ctx.font = '600 11px Segoe UI, sans-serif';
    ctx.fillText(`Max Jump (${journey.jumpRangeLY} LY)`, w * 0.5 - 52, Math.max(18, h * 0.5 - journey.jumpRangeLY * scale * sinT - 6));

    // Golden direction arrow toward Home (Sol)
    const homeProj = project(SOL_STAR_REF.x, SOL_STAR_REF.y, SOL_STAR_REF.z);
    const hdx = homeProj.sx - w * 0.5;
    const hdy = homeProj.sy - h * 0.5;
    const hLen = Math.hypot(hdx, hdy);
    if (hLen > 14) {
      const arrowLen = Math.min(hLen, 168);
      const ax = w * 0.5 + (hdx / hLen) * arrowLen;
      const ay = h * 0.5 + (hdy / hLen) * arrowLen;
      ctx.strokeStyle = 'rgba(255, 214, 102, 0.78)';
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      ctx.moveTo(w * 0.5, h * 0.5);
      ctx.lineTo(ax, ay);
      ctx.stroke();

      // Pill badge for HOME direction
      const lbl = '★ HOME (SOL)';
      ctx.font = '700 11px Segoe UI, sans-serif';
      const tw = ctx.measureText(lbl).width + 12;
      const lx = Math.max(8, Math.min(w - tw - 8, ax - tw * 0.5));
      const ly = Math.max(18, Math.min(h - 10, ay - 10));
      ctx.fillStyle = 'rgba(20, 24, 42, 0.9)';
      ctx.fillRect(lx, ly - 12, tw, 17);
      ctx.strokeStyle = '#ffd166';
      ctx.lineWidth = 1;
      ctx.strokeRect(lx, ly - 12, tw, 17);
      ctx.fillStyle = '#ffd166';
      ctx.fillText(lbl, lx + 6, ly);
    }

    // Draw stars sorted back-to-front
    const list = stars.map((star) => ({ star, ...project(star.x, star.y, star.z) }));
    list.sort((a, b) => a.depth - b.depth);
    this.projectedStars = [];
    const placedLabels: Array<{ x: number; y: number; w: number; h: number }> = [];

    for (const item of list) {
      const { star, sx, sy } = item;
      if (sx < -20 || sx > w + 20 || sy < -20 || sy > h + 20) continue;

      const dist = starDistanceLY(journey.currentStar, star);
      const inRange = dist <= journey.jumpRangeLY && star.id !== journey.currentStar.id;
      const visited = journey.visitedStarIds.includes(star.id);
      const isCurrent = star.id === journey.currentStar.id;
      const isSelected = this.selectedStar?.id === star.id;
      const isBestHome = bestHomeStar?.id === star.id;

      if (inRange && (isSelected || isBestHome)) {
        ctx.strokeStyle = isSelected ? 'rgba(255, 160, 102, 0.85)' : 'rgba(255, 214, 102, 0.45)';
        ctx.lineWidth = isSelected ? 2.4 : 1.5;
        ctx.beginPath();
        ctx.moveTo(w * 0.5, h * 0.5);
        ctx.lineTo(sx, sy);
        ctx.stroke();
      }

      const r = isCurrent ? 8 : star.isHome ? 9 : inRange ? 6.5 : 3.5;
      this.projectedStars.push({ star, sx, sy, r });

      ctx.fillStyle = STAR_COLORS[star.starKind];
      ctx.globalAlpha = inRange || isCurrent || star.isHome ? 1.0 : 0.32;
      ctx.beginPath();
      ctx.arc(sx, sy, r, 0, Math.PI * 2);
      ctx.fill();
      ctx.globalAlpha = 1;

      if (visited || isCurrent) {
        ctx.strokeStyle = isCurrent ? '#ffffff' : '#ffd166';
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.arc(sx, sy, r + 3.5, 0, Math.PI * 2);
        ctx.stroke();
      }
      if (isSelected) {
        ctx.strokeStyle = '#ff8e62';
        ctx.lineWidth = 2.5;
        ctx.beginPath();
        ctx.arc(sx, sy, r + 7, 0, Math.PI * 2);
        ctx.stroke();
      }

      // Non-overlapping pill labels for crisp readability!
      const mustLabel = isCurrent || isSelected || star.isHome || isBestHome;
      if (mustLabel || inRange) {
        const text = isCurrent ? `YOU (${star.name})` : isBestHome ? `★ ${star.name}` : star.name;
        ctx.font = mustLabel ? '700 11px Segoe UI, sans-serif' : '600 11px Segoe UI, sans-serif';
        const tw = ctx.measureText(text).width + 10;
        const th = 16;
        const bx = sx + r + 5;
        const by = sy - 8;
        const overlaps =
          !mustLabel &&
          placedLabels.some((p) => bx < p.x + p.w + 4 && bx + tw + 4 > p.x && by < p.y + p.h + 2 && by + th + 2 > p.y);
        if (!overlaps && bx + tw < w - 6 && by > 6 && by + th < h - 6) {
          placedLabels.push({ x: bx, y: by, w: tw, h: th });
          ctx.fillStyle = isSelected ? 'rgba(255, 142, 98, 0.92)' : 'rgba(10, 16, 34, 0.84)';
          ctx.fillRect(bx, by, tw, th);
          ctx.fillStyle = isSelected ? '#161018' : isBestHome ? '#ffd166' : '#f2f7ff';
          ctx.fillText(text, bx + 5, by + 12);
        }
      }
    }
  }

  private renderGalaxySidebar(
    journey: JourneyState,
    ship: ShipState,
    reachable: StarRef[],
    bestHomeStar: StarRef | null,
    redraw: () => void,
  ): void {
    const sb = this.container.querySelector('#galaxy-sidebar');
    if (!sb) return;
    const st = this.selectedStar;
    const chk = checkJump(journey, ship, st);
    const visited = st ? journey.visitedStarIds.includes(st.id) : false;

    const quickList = reachable
      .slice(0, 6)
      .map((s) => {
        const d = Math.round(starDistanceLY(journey.currentStar, s));
        const active = st?.id === s.id;
        const isBest = bestHomeStar?.id === s.id;
        return `
          <button class="quick-star-btn ${active ? 'selected' : ''}" data-star-id="${s.id}">
            <span><i style="background:${STAR_COLORS[s.starKind]}"></i>${s.name}${isBest ? ' ★' : ''}</span>
            <small>${d} LY</small>
          </button>
        `;
      })
      .join('');

    sb.innerHTML = `
      <div class="sb-title">${st ? st.name : 'Select a Star'}</div>
      ${st ? `<div class="sys-badge" style="display:inline-block;margin:6px 0 8px;">${STAR_TITLES[st.starKind]}</div>` : ''}
      ${st ? `
        <div class="sb-stat"><span>Distance</span><strong>${Math.round(starDistanceLY(journey.currentStar, st))} LY</strong></div>
        <div class="sb-stat"><span>Solar Cost</span><strong>${chk.solarCost}%</strong></div>
        <div class="sb-stat"><span>Status</span><strong>${visited ? 'Visited ★' : 'Uncharted'}</strong></div>
        <p class="sb-msg">${chk.reason}</p>
        <button class="pill-btn active" id="ov-jump-btn" ${chk.ok ? '' : 'disabled'} style="width:100%;margin-top:8px;padding:9px;">
          🚀 Engage Jump Drive (J)
        </button>
      ` : ''}
      <div style="margin-top:12px;font-size:11px;font-weight:700;color:#8ceeff;text-transform:uppercase;letter-spacing:.6px;">
        Reachable Stars (★ = Toward Home)
      </div>
      <div class="quick-star-list">${quickList || '<p class="modal-sub">No stars in range.</p>'}</div>
    `;

    const btn = sb.querySelector('#ov-jump-btn') as HTMLButtonElement | null;
    if (btn && st && chk.ok) {
      btn.addEventListener('click', () => this.callbacks.onJumpTo(st));
    }
    sb.querySelectorAll<HTMLButtonElement>('[data-star-id]').forEach((itemBtn) => {
      itemBtn.addEventListener('click', () => {
        const found = reachable.find((s) => s.id === itemBtn.dataset['starId']);
        if (found) {
          this.selectedStar = found;
          this.callbacks.onSelectTarget(found);
          redraw();
          this.renderGalaxySidebar(journey, ship, reachable, bestHomeStar, redraw);
        }
      });
    });
  }

  private renderSystemModal(journey: JourneyState, system: StarSystem): void {
    const rows = system.planets
      .map((p) => {
        const scanned = journey.scannedPlanets.some((r) => r.key === planetScanKey(system.ref.id, p.id));
        const rgb = `rgb(${Math.round(p.colorA[0] * 255)},${Math.round(p.colorA[1] * 255)},${Math.round(p.colorA[2] * 255)})`;
        return `
          <div class="planet-row">
            <div class="planet-dot" style="background:${rgb};box-shadow:0 0 12px ${rgb};"></div>
            <div class="planet-info">
              <div class="planet-name">${p.name} ${scanned ? '<span class="scanned-tag">★ Scanned</span>' : ''} ${p.hasRings ? '<span class="ring-tag">Ringed</span>' : ''}</div>
              <div class="planet-fact">${p.funFact}</div>
            </div>
            <button class="pill-btn" data-planet-id="${p.id}">Face Planet</button>
            ${p.landable ? `<button class="pill-btn active" data-descend-id="${p.id}">🌍 Descend</button>` : `<span class="ring-tag">Gas Giant</span>`}
          </div>
        `;
      })
      .join('');

    this.container.innerHTML = `
      <div class="card modal-panel">
        <div class="modal-header">
          <div>
            <h2>${system.name}: System Map</h2>
            <p class="modal-sub">${system.tagline} Fly close to a world and press <kbd>F</kbd> to scan it!</p>
          </div>
          <button class="pill-btn" id="ov-close">Close (Esc)</button>
        </div>
        <div class="planet-list">${rows}</div>
      </div>
    `;

    this.container.querySelector('#ov-close')!.addEventListener('click', () => this.callbacks.onClose());
    this.container.querySelectorAll<HTMLButtonElement>('[data-planet-id]').forEach((btn) => {
      btn.addEventListener('click', () => {
        const pid = Number(btn.dataset['planetId']);
        const planet = system.planets.find((p) => p.id === pid);
        if (planet) {
          this.callbacks.onPointAtPlanet(planet);
          this.callbacks.onClose();
        }
      });
    });
    this.container.querySelectorAll<HTMLButtonElement>('[data-descend-id]').forEach((btn) => {
      btn.addEventListener('click', () => {
        const pid = Number(btn.dataset['descendId']);
        const planet = system.planets.find((p) => p.id === pid);
        if (planet) {
          this.callbacks.onDescendToPlanet(planet);
          this.callbacks.onClose();
        }
      });
    });
  }

  private renderJournalModal(journey: JourneyState): void {
    const homeDist = Math.round(distanceToHomeLY(journey));

    const endingHtml = journey.reachedHome
      ? (() => {
          const end = evaluateEnding({
            scannedCount: journey.scannedPlanets.length,
            campCount: journey.camps.length,
            visitedExotic: journey.visitedExotic,
            discoveryStars: journey.discoveryStars,
          });
          return `
            <div class="planet-row" style="border:1px solid #ffd166;background:rgba(255,209,102,0.14);margin-bottom:12px;">
              <div class="planet-info">
                <div class="planet-name">${end.badge}: ${end.title}</div>
                <div class="planet-fact">${end.description}</div>
              </div>
            </div>
          `;
        })()
      : '';

    const transmissionsHtml = STORY_TRANSMISSIONS.filter(
      (tx) => journey.totalJumps >= tx.minJumps || (tx.id === 'tx-home' && journey.reachedHome),
    )
      .reverse()
      .map(
        (tx) => `
          <div class="planet-row">
            <div class="planet-info">
              <div class="planet-name">📡 ${tx.title} <span class="ring-tag">${tx.sender}</span></div>
              <div class="planet-fact">${tx.body}</div>
            </div>
          </div>
        `,
      )
      .join('');

    const shipsHtml = SHIP_HULLS.map((hull) => {
      const unlocked = journey.unlockedShips.includes(hull.id);
      const active = journey.activeShip === hull.id;
      const canBuy = !unlocked && journey.discoveryStars >= hull.costStars;
      const label = active ? 'Active Ship ✓' : unlocked ? 'Board Ship' : `Unlock (★ ${hull.costStars})`;
      return `
        <div class="planet-row">
          <div class="planet-info">
            <div class="planet-name">🚀 ${hull.name} <span class="ring-tag">+${hull.bonusRangeLY} LY · ${Math.round(hull.speedMult * 100)}% Speed</span></div>
            <div class="planet-fact">${hull.description}</div>
          </div>
          <button class="pill-btn ${active || canBuy ? 'active' : ''}" data-ship-id="${hull.id}" ${!unlocked && !canBuy ? 'disabled' : ''}>${label}</button>
        </div>
      `;
    }).join('');

    const campsHtml =
      journey.camps.length === 0
        ? `<p class="modal-sub">No Cozy Research Camps built yet! Land on a planet (L → G), step out (E), and press <kbd>B</kbd> to build a camp.</p>`
        : journey.camps
            .map(
              (c) => `
              <div class="planet-row">
                <div class="planet-info">
                  <div class="planet-name">⛺ ${c.planetName} Camp <span class="ring-tag">${c.systemName}</span></div>
                  <div class="planet-fact">Beaming +1 Discovery Star back to Earth Observatory on every jump!</div>
                </div>
              </div>
            `,
            )
            .join('');

    const scannedHtml =
      journey.scannedPlanets.length === 0
        ? `<p class="modal-sub">No discoveries logged yet! Fly near planets or walk on surfaces and press <kbd>F</kbd> to scan.</p>`
        : journey.scannedPlanets
            .slice()
            .reverse()
            .map(
              (rec) => `
              <div class="planet-row">
                <div class="planet-info">
                  <div class="planet-name">★ ${rec.planetName} <span class="ring-tag">${rec.systemName}</span></div>
                  <div class="planet-fact">${rec.funFact}</div>
                </div>
              </div>
            `,
            )
            .join('');

    this.container.innerHTML = `
      <div class="card modal-panel">
        <div class="modal-header">
          <div>
            <h2>Explorer's Journal &amp; Hangar</h2>
            <p class="modal-sub">${journey.reachedHome ? '🎉 You made it home to Sol! Keep exploring the galaxy anytime.' : `Chart your way back to Sol (${homeDist} LY away) while discovering worlds &amp; unlocking ships!`}</p>
          </div>
          <button class="pill-btn" id="ov-close">Close (Esc)</button>
        </div>
        ${endingHtml}
        <div class="journal-grid">
          <div class="j-stat"><span>Discovery Stars</span><strong>★ ${journey.discoveryStars}</strong></div>
          <div class="j-stat"><span>Systems Visited</span><strong>${journey.visitedStarIds.length}</strong></div>
          <div class="j-stat"><span>Research Camps</span><strong>⛺ ${journey.camps.length}</strong></div>
          <div class="j-stat"><span>Jump Range</span><strong>${journey.jumpRangeLY} LY</strong></div>
          <div class="j-stat"><span>Years Elapsed</span><strong>${journey.yearsPassed} yrs</strong></div>
          <div class="j-stat"><span>Distance to Sol</span><strong>${homeDist} LY</strong></div>
        </div>
        <h3 style="margin:14px 0 8px;font-size:14px;color:#ffd166;">🚀 Ship Hangar</h3>
        <div class="planet-list" style="max-height:175px;">${shipsHtml}</div>
        <h3 style="margin:14px 0 8px;font-size:14px;color:#8ceeff;">📡 Messages from Earth Observatory</h3>
        <div class="planet-list" style="max-height:175px;">${transmissionsHtml}</div>
        <h3 style="margin:14px 0 8px;font-size:14px;color:#ffd166;">⛺ Cozy Research Camps (${journey.camps.length}) &amp; Discoveries (${journey.scannedPlanets.length})</h3>
        <div class="planet-list" style="max-height:175px;">${campsHtml}${scannedHtml}</div>
        <div style="display:flex;justify-content:flex-end;margin-top:14px;">
          <button class="pill-btn" id="ov-reset">Start New Journey</button>
        </div>
      </div>
    `;

    this.container.querySelector('#ov-close')!.addEventListener('click', () => this.callbacks.onClose());
    this.container.querySelector('#ov-reset')!.addEventListener('click', () => this.callbacks.onResetJourney());
    this.container.querySelectorAll<HTMLButtonElement>('[data-ship-id]').forEach((btn) => {
      btn.addEventListener('click', () => {
        const hull = btn.dataset['shipId'] as ShipHullId;
        this.callbacks.onSelectShip(hull);
        this.renderJournalModal(journey);
      });
    });
  }
}
