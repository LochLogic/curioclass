/**
 * Multi-touch virtual thumbstick & context-aware action buttons for phones, iPads, and touch Chromebooks.
 * Tracks individual pointerIds so players can move with their left thumb while steering with their right thumb.
 */

export interface TouchInputState {
  forward: number;   // -1..1
  strafe: number;    // -1..1
  vertical: number;  // -1..1
  boost: boolean;
  brake: boolean;    // Brake in flight / Jetpack & Jump on foot or rover
  cruiseToggleCount: number;
}

export function computeStickAxes(
  dx: number,
  dy: number,
  maxRadius: number,
  deadzone = 0.12,
): { strafe: number; forward: number; knobX: number; knobY: number } {
  const dist = Math.hypot(dx, dy);
  if (dist < 1e-5 || maxRadius <= 0) {
    return { strafe: 0, forward: 0, knobX: 0, knobY: 0 };
  }
  const clamped = Math.min(dist, maxRadius);
  const nx = (dx / dist) * (clamped / maxRadius);
  const ny = (dy / dist) * (clamped / maxRadius);
  const mag = Math.hypot(nx, ny);
  if (mag < deadzone) {
    return { strafe: 0, forward: 0, knobX: nx * maxRadius, knobY: ny * maxRadius };
  }
  const scaled = (mag - deadzone) / (1 - deadzone);
  return {
    strafe: (nx / mag) * scaled,
    forward: -(ny / mag) * scaled, // Up on screen = +forward
    knobX: nx * maxRadius,
    knobY: ny * maxRadius,
  };
}

export class TouchControls {
  private root: HTMLElement;
  private layer: HTMLElement;
  private stickBase!: HTMLElement;
  private stickKnob!: HTMLElement;
  private brakeBtn!: HTMLButtonElement;
  private cruiseBtn!: HTMLButtonElement;
  private upBtn!: HTMLButtonElement;
  private downBtn!: HTMLButtonElement;

  private activeStickPointer: number | null = null;
  private stickCenterX = 0;
  private stickCenterY = 0;
  private readonly maxRadius = 46;
  private visible = false;

  readonly state: TouchInputState = {
    forward: 0,
    strafe: 0,
    vertical: 0,
    boost: false,
    brake: false,
    cruiseToggleCount: 0,
  };

  constructor(uiRoot: HTMLElement, onCruiseToggle: () => void) {
    this.root = uiRoot;
    this.layer = document.createElement('div');
    this.layer.className = 'touch-layer hidden';
    this.layer.innerHTML = `
      <div class="touch-stick" id="tc-stick">
        <div class="touch-knob" id="tc-knob"></div>
      </div>
      <div class="touch-actions">
        <div class="touch-col">
          <button class="touch-btn small" id="tc-up">▲</button>
          <button class="touch-btn small" id="tc-down">▼</button>
        </div>
        <div class="touch-col">
          <button class="touch-btn" id="tc-cruise">Cruise</button>
          <button class="touch-btn accent" id="tc-boost">Boost</button>
          <button class="touch-btn" id="tc-brake">Brake</button>
        </div>
      </div>
    `;
    uiRoot.appendChild(this.layer);

    this.stickBase = this.layer.querySelector('#tc-stick')!;
    this.stickKnob = this.layer.querySelector('#tc-knob')!;
    this.brakeBtn = this.layer.querySelector('#tc-brake')!;
    this.cruiseBtn = this.layer.querySelector('#tc-cruise')!;
    this.upBtn = this.layer.querySelector('#tc-up')!;
    this.downBtn = this.layer.querySelector('#tc-down')!;

    // Left virtual thumbstick pointer handling
    this.stickBase.addEventListener('pointerdown', (e) => {
      e.stopPropagation();
      e.preventDefault();
      if (this.activeStickPointer !== null) return;
      this.activeStickPointer = e.pointerId;
      this.stickBase.setPointerCapture(e.pointerId);
      const rect = this.stickBase.getBoundingClientRect();
      this.stickCenterX = rect.left + rect.width * 0.5;
      this.stickCenterY = rect.top + rect.height * 0.5;
      this.updateStick(e.clientX, e.clientY);
    });

    this.stickBase.addEventListener('pointermove', (e) => {
      if (e.pointerId !== this.activeStickPointer) return;
      e.stopPropagation();
      e.preventDefault();
      this.updateStick(e.clientX, e.clientY);
    });

    const resetStick = (e: PointerEvent) => {
      if (e.pointerId !== this.activeStickPointer) return;
      this.activeStickPointer = null;
      this.state.forward = 0;
      this.state.strafe = 0;
      this.stickKnob.style.transform = 'translate(0px, 0px)';
    };
    this.stickBase.addEventListener('pointerup', resetStick);
    this.stickBase.addEventListener('pointercancel', resetStick);

    const bindHold = (btn: HTMLButtonElement, onChange: (down: boolean) => void) => {
      btn.addEventListener('pointerdown', (e) => {
        e.stopPropagation();
        e.preventDefault();
        btn.setPointerCapture(e.pointerId);
        btn.classList.add('pressed');
        onChange(true);
      });
      const release = (e: PointerEvent) => {
        e.stopPropagation();
        btn.classList.remove('pressed');
        onChange(false);
      };
      btn.addEventListener('pointerup', release);
      btn.addEventListener('pointercancel', release);
    };

    bindHold(this.layer.querySelector('#tc-boost')!, (down) => {
      this.state.boost = down;
    });
    bindHold(this.brakeBtn, (down) => {
      this.state.brake = down;
    });
    bindHold(this.upBtn, (down) => {
      this.state.vertical = down ? 1 : 0;
    });
    bindHold(this.downBtn, (down) => {
      this.state.vertical = down ? -1 : 0;
    });

    this.cruiseBtn.addEventListener('pointerdown', (e) => {
      e.stopPropagation();
      e.preventDefault();
      this.state.cruiseToggleCount++;
      onCruiseToggle();
    });
  }

  private updateStick(clientX: number, clientY: number): void {
    const res = computeStickAxes(
      clientX - this.stickCenterX,
      clientY - this.stickCenterY,
      this.maxRadius,
    );
    this.state.strafe = res.strafe;
    this.state.forward = res.forward;
    this.stickKnob.style.transform = `translate(${res.knobX.toFixed(1)}px, ${res.knobY.toFixed(1)}px)`;
  }

  setVisible(show: boolean): void {
    this.visible = show;
    this.layer.classList.toggle('hidden', !show);
    this.root.classList.toggle('touch-active', show);
  }

  isVisible(): boolean {
    return this.visible;
  }

  updateContext(mode: 'space' | 'planet-fly' | 'on-foot' | 'rover', cruiseActive: boolean): void {
    const groundMode = mode === 'on-foot' || mode === 'rover';
    this.upBtn.style.display = groundMode ? 'none' : 'grid';
    this.downBtn.style.display = groundMode ? 'none' : 'grid';
    this.cruiseBtn.style.display = groundMode ? 'none' : 'grid';
    this.cruiseBtn.classList.toggle('pressed', cruiseActive);
    this.brakeBtn.textContent = mode === 'on-foot' ? 'Jetpack' : mode === 'rover' ? 'Jump' : 'Brake';
  }
}
