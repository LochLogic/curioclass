import './styles.css';
import { STARTERS, nowS, stageSize, starterToSetup, state } from './core/state';
import { audio } from './audio/engine';
import { setSequencerUiCallback } from './audio/sequencer';
import { telemetry } from './audio/telemetry';
import { WavefieldRenderer } from './graphics/wavefield';
import { renderStage2D } from './graphics/stage2d';
import { setInteractionCallbacks, updateHolds } from './input/strings';
import { initPointer } from './input/pointer';
import { initKeyboard } from './input/keyboard';
import { recorder } from './export/recorder';
import { applySetup, initHud, refreshUI, startFilm, toast, toggleClean, toggleRec, updateLiveHud } from './ui/hud';

function boot(): void {
  const waveCanvas = document.getElementById('waveCanvas') as HTMLCanvasElement;
  const fgCanvas = document.getElementById('stageCanvas') as HTMLCanvasElement;
  const fgCtx = fgCanvas.getContext('2d')!;

  const wavefield = new WavefieldRenderer(waveCanvas);

  const layoutStage = () => {
    const vw = window.innerWidth;
    const vh = window.innerHeight;
    const aspect = stageSize.w / stageSize.h;
    let cssW = vw;
    let cssH = vw / aspect;
    if (cssH > vh) {
      cssH = vh;
      cssW = vh * aspect;
    }

    const dpr = Math.min(window.devicePixelRatio || 1, 2);
    for (const cv of [waveCanvas, fgCanvas]) {
      cv.style.width = `${Math.round(cssW)}px`;
      cv.style.height = `${Math.round(cssH)}px`;
    }

    wavefield.resize(Math.round(stageSize.w), Math.round(stageSize.h));
    fgCanvas.width = Math.round(stageSize.w * dpr);
    fgCanvas.height = Math.round(stageSize.h * dpr);
    fgCtx.setTransform(dpr, 0, 0, dpr, 0, 0);

    // Safe vertical bounds inside stage coordinates (away from top/bottom bars)
    state.safeTop = 64;
    state.safeBottom = stageSize.h - 110;
  };

  setSequencerUiCallback(refreshUI);
  setInteractionCallbacks(toast, refreshUI);

  initHud({
    onResizeStage: layoutStage,
    waveCanvas,
    fgCanvas,
  });

  initPointer(fgCanvas, toast);
  initKeyboard({
    toggleRec,
    toggleFilm: startFilm,
    toggleClean,
    refreshUI,
    toast,
  });

  // Load our signature "Resonance Harp" starter stage immediately behind the welcome card
  applySetup(starterToSetup(STARTERS[0]));
  layoutStage();
  window.addEventListener('resize', layoutStage);

  let prevT = nowS();
  const frame = () => {
    const t = nowS();
    const dt = Math.min(0.05, Math.max(0.001, t - prevT));
    prevT = t;

    telemetry.sampleAnalyser(audio.g?.analyser ?? null, dt);
    updateHolds(t);
    wavefield.render(t, dt);
    renderStage2D(fgCtx, t, dt);

    if (recorder.on) {
      recorder.compositeFrame(waveCanvas, fgCanvas);
    }
    updateLiveHud();
    requestAnimationFrame(frame);
  };
  requestAnimationFrame(frame);
}

boot();
