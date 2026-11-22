import type { QualityTier } from '../render/gpu-context.ts';
import type { StarSystem } from '../sim/galaxy.ts';
import type { ShipState } from '../sim/flight.ts';
import type { PlanetFlightState } from '../sim/planet-flight.ts';
import type { OrbitalActivityState } from '../sim/slalom.ts';
import { distanceToHomeLY, type JourneyState } from '../sim/journey.ts';
import { v3Len, v3Sub } from '../sim/math.ts';
import type { OverlayMode } from './overlays.ts';

export interface HudCallbacks {
  onOpenOverlay(mode: OverlayMode): void;
  onScan(): void;
  onJump(): void;
  onLandOrOrbit(): void;
  onTouchdown(): void;
  onToggleOnFoot(): void;
  onToggleRover(): void;
  onBuildCamp(): void;
  onToggleMute(): void;
  onTogglePhotoMode(): void;
  onToggleTouch(): void;
  onLaunchGame(): void;
  onSelectQuality(tier: QualityTier): void;
}

const STAR_LABELS: Record<StarSystem['starKind'], string> = {
  'warm-sun': 'Golden Sun',
  'amber-dwarf': 'Sunset Star',
  'sky-giant': 'Blue Giant',
  pulsar: 'Pulsar',
  'black-hole': 'Black Hole',
};

export class Hud {
  private root: HTMLElement;
  private sysNameEl!: HTMLElement;
  private sysBadgeEl!: HTMLElement;
  private sysTagEl!: HTMLElement;
  private journeySummaryEl!: HTMLElement;
  private nearbyEl!: HTMLElement;
  private fpsEl!: HTMLElement;
  private speedTextEl!: HTMLElement;
  private speedFillEl!: HTMLElement;
  private solarTextEl!: HTMLElement;
  private solarFillEl!: HTMLElement;
  private toastEl!: HTMLElement;
  private landBtn!: HTMLButtonElement;
  private touchdownBtn!: HTMLButtonElement;
  private onFootBtn!: HTMLButtonElement;
  private roverBtn!: HTMLButtonElement;
  private campBtn!: HTMLButtonElement;
  private muteBtn!: HTMLButtonElement;
  private touchToggleBtn!: HTMLButtonElement;
  private titleScreenEl!: HTMLElement;
  private gravityEl!: HTMLElement;
  private solarLabelEl!: HTMLElement;
  private controlsEl!: HTMLElement;
  private qualButtons: HTMLButtonElement[] = [];
  private toastTimer = 0;

  constructor(root: HTMLElement, callbacks: HudCallbacks) {
    this.root = root;

    root.innerHTML = `
      <div class="title-screen" id="title-screen">
        <div class="card title-card">
          <div class="title-logo">FARLIGHT</div>
          <p class="title-sub">A cozy, wondrous galaxy to explore.<br>Chart your way home to Earth across glowing nebulae, ringed giants, and living worlds!</p>
          <div class="title-tips">
            <div>🚀 <strong>Fly:</strong> Drag screen to steer · <kbd>W</kbd><kbd>A</kbd><kbd>S</kbd><kbd>D</kbd> or Left Stick to move</div>
            <div>🗺 <strong>Explore:</strong> <kbd>M</kbd> Galaxy Map · <kbd>N</kbd> System Map · <kbd>F</kbd> Scan Worlds &amp; Critters</div>
            <div>🌍 <strong>Land &amp; Drive:</strong> <kbd>L</kbd> Descend · <kbd>G</kbd> Touchdown · <kbd>E</kbd> Walk · <kbd>K</kbd> 6-Wheel Rover · <kbd>B</kbd> Camp</div>
            <div>📱 <strong>Phones &amp; tablets:</strong> a thumbstick and buttons appear on touch screens (show or hide them with 🎮).</div>
          </div>
          <button class="pill-btn active launch-btn" id="btn-launch">✨ Launch Explorer</button>
        </div>
      </div>
      <div class="toast hidden" id="hud-toast"></div>
      <div class="top-bar">
        <div class="card">
          <div class="title-row">
            <span class="sys-name" id="hud-sys-name"></span>
            <span class="sys-badge" id="hud-sys-badge"></span>
          </div>
          <div class="sys-tagline" id="hud-sys-tag"></div>
          <div class="sys-pills">
            <button class="pill-btn" id="btn-galaxy">🗺 Galaxy Map (M)</button>
            <button class="pill-btn" id="btn-system">🪐 System (N)</button>
            <button class="pill-btn" id="btn-journal">📖 Journal (Q)</button>
            <button class="pill-btn" id="btn-scan">🔍 Scan (F)</button>
            <button class="pill-btn" id="btn-land">🌍 Descend (L)</button>
            <button class="pill-btn" id="btn-touchdown" style="display:none;">🛬 Touchdown (G)</button>
            <button class="pill-btn" id="btn-onfoot" style="display:none;">🚶 Step Out (E)</button>
            <button class="pill-btn" id="btn-rover" style="display:none;">🚙 Rover (K)</button>
            <button class="pill-btn" id="btn-camp" style="display:none;">⛺ Build Camp (B)</button>
            <button class="pill-btn active" id="btn-jump">🚀 Jump (J)</button>
          </div>
        </div>
        <div class="card stats-card">
          <div><strong>FARLIGHT</strong> · FPS: <strong id="hud-fps">60</strong></div>
          <div id="hud-journey" style="margin-top:3px;"></div>
          <div id="hud-gravity" style="margin-top:2px;color:#ffd166;"></div>
          <div id="hud-nearby" style="margin-top:4px;max-width:255px;"></div>
          <div class="sys-pills" style="justify-content:flex-end;margin-top:8px;" id="hud-qual-pills">
            <button class="pill-btn" id="btn-touch" title="Toggle Touch Controls">🎮</button>
            <button class="pill-btn" id="btn-photo" title="Photo Mode (H)">📸</button>
            <button class="pill-btn" id="btn-mute">🔊 Sound</button>
          </div>
        </div>
      </div>
      <div class="bottom-bar">
        <div class="card gauges">
          <div class="gauge">
            <div class="gauge-label"><span>Speed</span><span id="hud-speed-txt">0</span></div>
            <div class="bar-track"><div class="bar-fill fill-speed" id="hud-speed-bar" style="width:0%"></div></div>
          </div>
          <div class="gauge">
            <div class="gauge-label"><span id="hud-solar-lbl">Solar Charge</span><span id="hud-solar-txt">100%</span></div>
            <div class="bar-track"><div class="bar-fill fill-solar" id="hud-solar-bar" style="width:100%"></div></div>
          </div>
        </div>
        <div class="card controls-hint" id="hud-controls">
          <span><kbd>Drag</kbd> Steer</span>
          <span><kbd>W</kbd><kbd>A</kbd><kbd>S</kbd><kbd>D</kbd> Fly</span>
          <span><kbd>Shift</kbd> Boost</span>
          <span><kbd>C</kbd> Cruise</span>
          <span><kbd>F</kbd> Scan</span>
          <span><kbd>L</kbd> Land</span>
          <span><kbd>M</kbd> Map</span>
        </div>
      </div>
    `;

    this.sysNameEl = root.querySelector('#hud-sys-name')!;
    this.sysBadgeEl = root.querySelector('#hud-sys-badge')!;
    this.sysTagEl = root.querySelector('#hud-sys-tag')!;
    this.journeySummaryEl = root.querySelector('#hud-journey')!;
    this.nearbyEl = root.querySelector('#hud-nearby')!;
    this.fpsEl = root.querySelector('#hud-fps')!;
    this.speedTextEl = root.querySelector('#hud-speed-txt')!;
    this.speedFillEl = root.querySelector('#hud-speed-bar')!;
    this.solarTextEl = root.querySelector('#hud-solar-txt')!;
    this.solarFillEl = root.querySelector('#hud-solar-bar')!;
    this.toastEl = root.querySelector('#hud-toast')!;
    this.landBtn = root.querySelector('#btn-land')!;
    this.touchdownBtn = root.querySelector('#btn-touchdown')!;
    this.onFootBtn = root.querySelector('#btn-onfoot')!;
    this.roverBtn = root.querySelector('#btn-rover')!;
    this.campBtn = root.querySelector('#btn-camp')!;
    this.muteBtn = root.querySelector('#btn-mute')!;
    this.touchToggleBtn = root.querySelector('#btn-touch')!;
    this.titleScreenEl = root.querySelector('#title-screen')!;
    this.gravityEl = root.querySelector('#hud-gravity')!;
    this.solarLabelEl = root.querySelector('#hud-solar-lbl')!;

    root.querySelector('#btn-launch')!.addEventListener('click', () => {
      this.titleScreenEl.classList.add('hidden');
      callbacks.onLaunchGame();
    });
    this.touchToggleBtn.addEventListener('click', () => callbacks.onToggleTouch());
    root.querySelector('#btn-photo')!.addEventListener('click', () => callbacks.onTogglePhotoMode());
    this.controlsEl = root.querySelector('#hud-controls')!;

    root.querySelector('#btn-galaxy')!.addEventListener('click', () => callbacks.onOpenOverlay('galaxy'));
    root.querySelector('#btn-system')!.addEventListener('click', () => callbacks.onOpenOverlay('system'));
    root.querySelector('#btn-journal')!.addEventListener('click', () => callbacks.onOpenOverlay('journal'));
    root.querySelector('#btn-scan')!.addEventListener('click', () => callbacks.onScan());
    this.landBtn.addEventListener('click', () => callbacks.onLandOrOrbit());
    this.touchdownBtn.addEventListener('click', () => callbacks.onTouchdown());
    this.onFootBtn.addEventListener('click', () => callbacks.onToggleOnFoot());
    this.roverBtn.addEventListener('click', () => callbacks.onToggleRover());
    this.campBtn.addEventListener('click', () => callbacks.onBuildCamp());
    this.muteBtn.addEventListener('click', () => callbacks.onToggleMute());
    root.querySelector('#btn-jump')!.addEventListener('click', () => callbacks.onJump());

    const qualPills = root.querySelector('#hud-qual-pills')!;
    const tiers: QualityTier[] = ['performance', 'high', 'ultra'];
    tiers.forEach((tier) => {
      const btn = document.createElement('button');
      btn.className = 'pill-btn';
      btn.textContent = tier[0]!.toUpperCase() + tier.slice(1);
      btn.onclick = () => callbacks.onSelectQuality(tier);
      qualPills.appendChild(btn);
      this.qualButtons.push(btn);
    });
  }

  setSystem(system: StarSystem): void {
    this.sysNameEl.textContent = system.name;
    this.sysBadgeEl.textContent = STAR_LABELS[system.starKind];
    this.sysTagEl.textContent = system.tagline;
  }

  setQuality(tier: QualityTier): void {
    const order: QualityTier[] = ['performance', 'high', 'ultra'];
    this.qualButtons.forEach((b, i) => b.classList.toggle('active', order[i] === tier));
  }

  setMuted(muted: boolean): void {
    this.muteBtn.textContent = muted ? '🔇 Muted' : '🔊 Sound';
    this.muteBtn.classList.toggle('active', muted);
  }

  setPhotoMode(enabled: boolean): void {
    this.root.classList.toggle('photo-mode', enabled);
  }

  setTouchActive(enabled: boolean): void {
    this.touchToggleBtn.classList.toggle('active', enabled);
  }

  isTitleVisible(): boolean {
    return !this.titleScreenEl.classList.contains('hidden');
  }

  showToast(message: string, durationSec = 4.2): void {
    this.toastEl.textContent = message;
    this.toastEl.classList.remove('hidden');
    this.toastTimer = durationSec;
  }

  update(
    ship: ShipState,
    system: StarSystem,
    journey: JourneyState,
    fps: number,
    dt: number,
    planetFlight: PlanetFlightState | null,
    orbital: OrbitalActivityState | null = null,
  ): void {
    if (this.toastTimer > 0) {
      this.toastTimer -= dt;
      if (this.toastTimer <= 0) {
        this.toastEl.classList.add('hidden');
      }
    }

    this.fpsEl.textContent = `${Math.round(fps)}`;
    const activeSpeed = planetFlight ? planetFlight.speed : ship.speed;
    this.speedTextEl.textContent = `${Math.round(activeSpeed)} m/s`;
    const speedPct = Math.min(100, (activeSpeed / (ship.maxSpeed * 3.2)) * 100);
    this.speedFillEl.style.width = `${speedPct.toFixed(1)}%`;

    this.solarTextEl.textContent = `${Math.round(ship.solarCharge)}%`;
    this.solarFillEl.style.width = `${ship.solarCharge.toFixed(1)}%`;

    const homeDist = Math.round(distanceToHomeLY(journey));
    const targetTxt = journey.targetStar ? ` · Next: <strong>${journey.targetStar.name}</strong>` : '';
    this.journeySummaryEl.innerHTML = `★ <strong>${journey.discoveryStars}</strong> Stars · Home: <strong>${homeDist} LY</strong>${targetTxt}`;

    if (planetFlight) {
      const gravTxt = planetFlight.surfaceGravityG < 0.45 ? 'Low-G Moon!' : planetFlight.surfaceGravityG > 1.15 ? 'Heavy World' : 'Earth-like';
      this.gravityEl.textContent = `Gravity: ${planetFlight.surfaceGravityG.toFixed(2)} G (${gravTxt})`;
      if (planetFlight.onFoot || planetFlight.inRover) {
        this.solarLabelEl.textContent = planetFlight.inRover ? 'Jump Boost' : 'Jetpack';
        this.solarTextEl.textContent = `${Math.round(planetFlight.jetpackFuel)}%`;
        this.solarFillEl.style.width = `${planetFlight.jetpackFuel.toFixed(1)}%`;
        this.landBtn.style.display = 'none';
        this.touchdownBtn.style.display = 'none';
        this.onFootBtn.style.display = 'inline-block';
        this.onFootBtn.textContent = '🛸 Board Ship (E)';
        this.roverBtn.style.display = 'inline-block';
        this.roverBtn.textContent = planetFlight.inRover ? '🚶 Exit Rover (K)' : '🚙 Rover (K)';
        this.campBtn.style.display = 'inline-block';
        const modeTxt = planetFlight.inRover ? 'Driving 6-Wheel Rover' : 'On Foot';
        this.nearbyEl.innerHTML = `Exploring: <strong>${planetFlight.planet.name}</strong> (${modeTxt})<br><span style="opacity:.8">Space: Boost Jump · F: Scan · B: Build Camp!</span>`;
        this.controlsEl.innerHTML = `
          <span><kbd>Drag</kbd> Look</span>
          <span><kbd>W</kbd><kbd>A</kbd><kbd>S</kbd><kbd>D</kbd> ${planetFlight.inRover ? 'Drive' : 'Walk'}</span>
          <span><kbd>Space</kbd> ${planetFlight.inRover ? 'Jump Boost' : 'Jetpack'}</span>
          <span><kbd>K</kbd> Rover</span>
          <span><kbd>F</kbd> Scan</span>
          <span><kbd>B</kbd> Camp</span>
          <span><kbd>E</kbd> Ship</span>
        `;
        return;
      }

      this.campBtn.style.display = 'none';
      this.roverBtn.style.display = planetFlight.landed ? 'inline-block' : 'none';
      this.roverBtn.textContent = '🚙 Rover (K)';

      this.solarLabelEl.textContent = 'Solar Charge';
      this.landBtn.style.display = 'inline-block';
      this.landBtn.textContent = '🚀 Return to Orbit (L)';
      this.touchdownBtn.style.display = 'inline-block';
      this.touchdownBtn.textContent = planetFlight.landed ? '🛫 Lift Off (G)' : '🛬 Touchdown (G)';
      this.onFootBtn.style.display = planetFlight.landed ? 'inline-block' : 'none';
      this.onFootBtn.textContent = '🚶 Step Out (E)';
      const status = planetFlight.landed ? 'Landed' : `Alt: ${Math.round(planetFlight.altitudeAGL)}m`;
      this.nearbyEl.innerHTML = `Surface: <strong>${planetFlight.planet.name}</strong> (${status})<br><span style="opacity:.8">${planetFlight.landed ? 'Press E to step outside and explore on foot!' : 'Press [ / ] to shift sunrise & sunset!'}</span>`;
      this.controlsEl.innerHTML = `
        <span><kbd>Drag</kbd> Look</span>
        <span><kbd>W</kbd><kbd>A</kbd><kbd>S</kbd><kbd>D</kbd> Fly</span>
        <span><kbd>R</kbd>/<kbd>V</kbd> Up/Down</span>
        <span><kbd>G</kbd> Land/Liftoff</span>
        <span><kbd>E</kbd> Step Out</span>
        <span><kbd>[</kbd><kbd>]</kbd> Sun Time</span>
      `;
      return;
    }

    this.solarLabelEl.textContent = 'Solar Charge';
    this.landBtn.style.display = 'inline-block';
    this.landBtn.textContent = '🌍 Descend (L)';
    this.touchdownBtn.style.display = 'none';
    this.onFootBtn.style.display = 'none';
    this.roverBtn.style.display = 'none';
    this.campBtn.style.display = 'none';
    const slalomTxt = orbital && !orbital.completed ? ` · Rings: ${orbital.passedCount}/${orbital.rings.length}` : orbital?.completed ? ' · Slalom ★' : '';
    this.gravityEl.textContent =
      (ship.localGravityG >= 0.05
        ? `Orbital Gravity: ${ship.localGravityG.toFixed(2)} G`
        : 'Deep Space · 0.00 G') + slalomTxt;
    this.controlsEl.innerHTML = `
      <span><kbd>Drag</kbd> Steer</span>
      <span><kbd>W</kbd><kbd>A</kbd><kbd>S</kbd><kbd>D</kbd> Fly</span>
      <span><kbd>Shift</kbd> Boost</span>
      <span><kbd>C</kbd> Cruise</span>
      <span><kbd>F</kbd> Scan</span>
      <span><kbd>L</kbd> Land</span>
      <span><kbd>M</kbd> Map</span>
    `;

    let nearest = system.planets[0];
    let bestDist = Infinity;
    for (const p of system.planets) {
      const d = v3Len(v3Sub(p.position, ship.position)) - p.radius;
      if (d < bestDist) {
        bestDist = d;
        nearest = p;
      }
    }
    if (nearest) {
      this.nearbyEl.innerHTML = `Nearest: <strong>${nearest.name}</strong> (${Math.max(0, Math.round(bestDist))} km)<br><span style="opacity:.8">${nearest.funFact}</span>`;
    }
  }

  showError(message: string): void {
    const isMissingGpu = message.toLowerCase().includes('webgpu');
    this.root.innerHTML = `
      <div class="error-overlay">
        <div class="card error-box">
          <h1>${isMissingGpu ? 'WebGPU Required for Farlight' : 'Farlight Graphics Error'}</h1>
          <p>${message}</p>
        </div>
      </div>
    `;
  }
}
