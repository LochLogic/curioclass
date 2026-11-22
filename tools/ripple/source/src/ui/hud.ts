import {
  BEATS, BEAT_ORDER, INSTRUMENTS, PARTS, SCALE_ORDER, SCALES,
  clamp, own, spell,
} from '../core/music';
import {
  STARTERS, StageSetup, StageShape, ThemeId, chordDegNow, chordLabel, createString,
  getStoredSetups, saveStoredSetups, snapshotSetup, stageSize, starterToSetup, state, transport,
} from '../core/state';
import { initAudio, setMasterVolume, setMixLevels, setReverbAmount } from '../audio/engine';
import {
  armLayer, makeLayer, removeLayer, setBeat, togglePlay, undoLayer,
} from '../audio/sequencer';
import { downloadBlob, recorder, RecordingTake } from '../export/recorder';
import { renderStemsZip } from '../export/wavZip';
import { THEME_ORDER, THEMES } from '../graphics/themes';
import { clearStrings, closeMenu, endHold, forgetPointer } from '../input/strings';
import { endFx } from '../input/pointer';

const $ = <T extends HTMLElement = HTMLElement>(sel: string) => document.querySelector<T>(sel)!;

let toastTimer: number | null = null;
export function toast(msg: string, ms = 2500): void {
  const el = $('#toast');
  el.textContent = msg;
  el.classList.add('show');
  if (toastTimer != null) clearTimeout(toastTimer);
  toastTimer = window.setTimeout(() => el.classList.remove('show'), ms);
}

export function fmtTime(sec: number): string {
  const s = Math.max(0, Math.floor(sec));
  return `${Math.floor(s / 60)}:${String(s % 60).padStart(2, '0')}`;
}

export interface HudCallbacks {
  onResizeStage: () => void;
  waveCanvas: HTMLCanvasElement;
  fgCanvas: HTMLCanvasElement;
}

let hudCb: HudCallbacks;
let filmTimer: number | null = null;

export function setShape(shape: StageShape): void {
  if (recorder.on) {
    toast('Stop recording before changing stage shape.');
    return;
  }
  const [w, h] = shape === 'vertical' ? [720, 1280] : [1280, 720];
  const sx = w / stageSize.w;
  const sy = h / stageSize.h;
  closeMenu();
  state.preview = null;
  endFx();
  for (const s of state.strings) {
    for (const pid of Object.keys(s.holds)) endHold(s, pid);
    s.a.x *= sx; s.a.y *= sy;
    s.b.x *= sx; s.b.y *= sy;
    s.pull = null;
  }
  state.particles = [];
  state.pops = [];
  stageSize.w = w;
  stageSize.h = h;
  state.shape = shape;
  hudCb.onResizeStage();
  refreshUI();
}

export function applySetup(d: StageSetup): boolean {
  if (!d || !Array.isArray(d.strings)) {
    toast('Invalid setup file.');
    return false;
  }
  closeMenu();
  state.preview = null;
  endFx();
  for (const s of state.strings) {
    for (const pid of Object.keys(s.holds)) endHold(s, pid);
  }
  state.strings = [];
  transport.layers.slice().forEach(L => removeLayer(L.id));
  transport.rec = null;

  if ((d.shape === 'vertical' || d.shape === 'landscape') && d.shape !== state.shape) {
    setShape(d.shape);
  }

  const sx = stageSize.w / (d.w || 1280);
  const sy = stageSize.h / (d.h || 720);
  state.key = ((Math.round(d.key ?? 9) % 12) + 12) % 12;
  state.scale = own(SCALES, d.scale) ? d.scale : 'pentamin';
  transport.beat = own(BEATS, d.beat) ? d.beat : 'lofi';
  transport.bpm = clamp(Number(d.bpm) || BEATS[transport.beat].bpm, 50, 180);
  transport.loopBars = clamp(Number(d.loopBars) || 2, 1, 8);
  transport.follow = !!d.follow;
  for (const p of PARTS) {
    transport.parts[p] = !!(d.parts && d.parts[p]);
  }

  for (const st of d.strings.slice(0, 12)) {
    if (!Array.isArray(st.a) || !Array.isArray(st.b)) continue;
    const s = createString(
      { x: clamp(st.a[0] * sx, 24, stageSize.w - 24), y: clamp(st.a[1] * sy, 50, stageSize.h - 50) },
      { x: clamp(st.b[0] * sx, 24, stageSize.w - 24), y: clamp(st.b[1] * sy, 50, stageSize.h - 50) },
      {
        inst: own(INSTRUMENTS, st.inst) ? st.inst : 'harp',
        scale: st.scale && own(SCALES, st.scale) ? st.scale : null,
        root: st.root != null ? ((st.root % 12) + 12) % 12 : null,
        oct: clamp(st.oct ?? 0, -2, 2),
        mode: st.mode || 'notes',
        gain: st.gain ?? 1,
      },
    );
    state.strings.push(s);
  }
  state.selectedId = state.strings[0]?.id ?? null;

  if (Array.isArray(d.layers)) {
    for (const L of d.layers.slice(0, 8)) {
      if (!Array.isArray(L.events)) continue;
      transport.layers.push(makeLayer({
        len: clamp(L.len || 32, 16, 128),
        offset: L.offset || 0,
        vol: L.vol ?? 0.85,
        muted: !!L.muted,
        events: L.events,
      }));
    }
  }

  refreshUI();
  return true;
}

export function toggleClean(): void {
  state.clean = !state.clean;
  document.body.classList.toggle('clean', state.clean);
  if (!state.clean && filmTimer != null) {
    clearTimeout(filmTimer);
    filmTimer = null;
    $('#count').classList.remove('show');
  }
  refreshUI();
}

function showTakeModal(take: RecordingTake): void {
  const vid = $<HTMLVideoElement>('#takeVideo');
  const aud = $<HTMLAudioElement>('#takeAudio');
  const saveVid = $<HTMLButtonElement>('#saveVideo');
  const note = $('#takeNote');

  if (take.videoUrl) {
    vid.src = take.videoUrl;
    vid.classList.remove('hide');
    aud.classList.add('hide');
    saveVid.classList.remove('hide');
  } else {
    vid.classList.add('hide');
    aud.src = take.wavUrl;
    aud.classList.remove('hide');
    saveVid.classList.add('hide');
  }
  note.textContent = `Duration: ${fmtTime(take.durationSec)} · ${take.sampleRate} Hz stereo`;
  $('#saveModal').classList.add('open');
}

export function toggleRec(): void {
  if (recorder.on) {
    recorder.stop();
    if (state.clean) {
      state.clean = false;
      document.body.classList.remove('clean');
    }
    refreshUI();
    return;
  }
  const ok = recorder.start(hudCb.waveCanvas, hudCb.fgCanvas, take => {
    refreshUI();
    showTakeModal(take);
  });
  if (ok) {
    toast(recorder.mode === 'video' ? 'Recording video + sound...' : 'Recording sound...');
    refreshUI();
  }
}

export function startFilm(): void {
  if (recorder.on) {
    toggleRec();
    return;
  }
  initAudio();
  state.clean = true;
  document.body.classList.add('clean');
  const countEl = $('#count');
  let n = 3;
  const step = () => {
    if (!state.clean) {
      countEl.classList.remove('show');
      return;
    }
    if (n > 0) {
      countEl.textContent = String(n);
      countEl.classList.add('show');
      n--;
      filmTimer = window.setTimeout(step, 800);
    } else {
      countEl.classList.remove('show');
      filmTimer = null;
      recorder.mode = 'video';
      toggleRec();
    }
  };
  step();
}

export function refreshUI(): void {
  const sc = SCALES[state.scale];
  $('#keyVal').textContent = spell(state.key, state.key, sc.parent);
  $('#toneVal').textContent = sc.name;

  const strumBtn = $('#strumBtn');
  strumBtn.textContent = state.settings.strumMode === 'hover' ? 'Hover-Strum' : 'Click-Strum';
  strumBtn.classList.toggle('on', state.settings.strumMode === 'hover');

  $('#themeBtn').textContent = THEMES[state.settings.theme].name.split(' ')[0];
  $('#shapeBtn').textContent = state.shape === 'vertical' ? '9:16' : '16:9';
  $('#recMode').textContent = recorder.mode === 'video' ? 'Video + sound' : 'Sound only';

  const recBtn = $('#recBtn');
  recBtn.classList.toggle('on', recorder.on);
  $('#recLabel').textContent = recorder.on ? 'Stop' : 'Record';
  if (!recorder.on) $('#recTime').textContent = '';

  const playBtn = $('#playBtn');
  playBtn.classList.toggle('on', transport.playing);
  $('#playIcon').textContent = transport.playing ? '■' : '▶';
  $('#playLabel').textContent = transport.playing ? 'Stop' : 'Play';
  $('#bpmVal').textContent = String(transport.bpm);

  const followBtn = $('#followBtn');
  followBtn.classList.toggle('on', transport.follow);
  const deg = chordDegNow();
  $('#chordNow').textContent = deg != null ? chordLabel(deg) : '';

  // Beat style chips
  const beatBox = $('#beatChips');
  beatBox.querySelectorAll('button').forEach(btn => {
    btn.classList.toggle('on', btn.dataset.id === transport.beat);
  });

  // Beat part chips
  const B = BEATS[transport.beat];
  const partBox = $('#partChips');
  partBox.querySelectorAll('button').forEach((btn, i) => {
    const p = PARTS[i];
    btn.textContent = B.labels[i];
    btn.classList.toggle('on', transport.parts[p]);
  });

  // Loop layer controls
  const layerBtn = $('#layerBtn');
  layerBtn.classList.toggle('on', !!transport.rec);
  $('#layerLabel').textContent = transport.rec
    ? (transport.rec.state === 'count' ? 'Count-in...' : 'Recording...')
    : 'Record layer';
  $('#barsVal').textContent = `${transport.loopBars} bar${transport.loopBars > 1 ? 's' : ''}`;

  const layerChips = $('#layerChips');
  layerChips.innerHTML = '';
  transport.layers.forEach((L, idx) => {
    const chip = document.createElement('button');
    chip.className = 'chip' + (L.muted ? ' muted' : ' on');
    chip.textContent = `L${idx + 1}`;
    chip.title = 'Click to mute/unmute · Right-click to remove';
    chip.onclick = () => { L.muted = !L.muted; refreshUI(); };
    chip.oncontextmenu = e => { e.preventDefault(); removeLayer(L.id); };
    layerChips.appendChild(chip);
  });

  // Subtle bottom hint
  $('#hint').textContent = state.settings.strumMode === 'hover'
    ? 'Sweep across strings to play · Drag empty space to create · Right-click & slide to sustain · A to \' keys play focused string'
    : 'Hold Left-Click & sweep to strum · Alt+Drag to create a string · Right-click & slide to sustain · M for Hover-Strum';

  // Sync Settings inputs
  $<HTMLSelectElement>('#sTheme').value = state.settings.theme;
  $<HTMLSelectElement>('#sStrum').value = state.settings.strumMode;
  $<HTMLInputElement>('#sWave').value = String(state.settings.waveIntensity);
  $<HTMLInputElement>('#sReverb').value = String(state.settings.reverb);
  $<HTMLInputElement>('#sVol').value = String(state.settings.volume);
  $<HTMLInputElement>('#sQuant').checked = state.settings.quantize;
  $<HTMLInputElement>('#sLabels').checked = state.settings.labels;
}

export function updateLiveHud(): void {
  // Update step LEDs & chord label
  const leds = $('#leds').children;
  const activeBeat = transport.playing && transport.lastStep >= 0 ? Math.floor((transport.lastStep % 16) / 4) : -1;
  for (let i = 0; i < leds.length; i++) {
    leds[i].classList.toggle('on', i === activeBeat);
  }
  const deg = chordDegNow();
  const cEl = $('#chordNow');
  const nextTxt = deg != null ? chordLabel(deg) : '';
  if (cEl.textContent !== nextTxt) cEl.textContent = nextTxt;

  if (recorder.on) {
    const tStr = fmtTime((performance.now() - recorder.startedAt) / 1000);
    $('#recTime').textContent = tStr;
    $('#filmTime').textContent = tStr;
  }
}

function renderSetupsModal(): void {
  const starterBox = $('#starterList');
  starterBox.innerHTML = '';
  for (const S of STARTERS) {
    const btn = document.createElement('button');
    btn.className = 'tile';
    btn.innerHTML = `<b>${S.name}</b><span>${S.note}</span>`;
    btn.onclick = () => {
      applySetup(starterToSetup(S));
      $('#setupsModal').classList.remove('open');
      toast(`Loaded "${S.name}"`);
    };
    starterBox.appendChild(btn);
  }

  const listBox = $('#setupList');
  const stored = getStoredSetups();
  listBox.innerHTML = '';
  if (!stored.length) {
    listBox.innerHTML = '<p class="small muted">No saved setups yet.</p>';
  } else {
    stored.forEach((d, idx) => {
      const row = document.createElement('div');
      row.className = 'setupRow';
      const span = document.createElement('span');
      span.textContent = `${d.name} (${d.strings.length} strings)`;
      const loadBtn = document.createElement('button');
      loadBtn.textContent = 'Load';
      loadBtn.onclick = () => {
        applySetup(d);
        $('#setupsModal').classList.remove('open');
        toast(`Loaded "${d.name}"`);
      };
      const delBtn = document.createElement('button');
      delBtn.textContent = '×';
      delBtn.onclick = () => {
        stored.splice(idx, 1);
        saveStoredSetups(stored);
        renderSetupsModal();
      };
      row.append(span, loadBtn, delBtn);
      listBox.appendChild(row);
    });
  }
}

function renderMixerModal(): void {
  const box = $('#mixRows');
  box.innerHTML = '';
  const addRow = (label: string, val: number, onChange: (v: number) => void) => {
    const row = document.createElement('div');
    row.className = 'mixRow';
    const sp = document.createElement('span');
    sp.textContent = label;
    const inp = document.createElement('input');
    inp.type = 'range'; inp.min = '0'; inp.max = '1.3'; inp.step = '0.02';
    inp.value = String(val);
    const num = document.createElement('code');
    num.textContent = `${Math.round(val * 100)}%`;
    inp.oninput = () => {
      const v = parseFloat(inp.value);
      num.textContent = `${Math.round(v * 100)}%`;
      onChange(v);
    };
    row.append(sp, inp, num);
    box.appendChild(row);
  };

  addRow('Live strings', state.mix.live, v => { state.mix.live = v; setMixLevels(); });
  addRow('Backing beat', state.mix.beat, v => { state.mix.beat = v; setMixLevels(); });
  transport.layers.forEach((L, idx) => {
    addRow(`Loop layer ${idx + 1}`, L.vol, v => {
      L.vol = v;
      if (L.gainNode) L.gainNode.gain.value = v;
    });
  });
}

export function initHud(cb: HudCallbacks): void {
  hudCb = cb;

  // Prevent hover-strum while pointer is over HUD bars
  for (const id of ['#top', '#dock']) {
    const el = $(id);
    el.addEventListener('pointerenter', () => { state.mouse.overHud = true; forgetPointer('mouse'); });
    el.addEventListener('pointerleave', () => { state.mouse.overHud = false; });
  }

  // Build Beat chips & Part chips & 4 LEDs
  const beatBox = $('#beatChips');
  for (const id of BEAT_ORDER) {
    const btn = document.createElement('button');
    btn.className = 'chip';
    btn.dataset.id = id;
    btn.textContent = BEATS[id].name;
    btn.onclick = () => {
      initAudio();
      setBeat(id);
      if (!transport.playing) togglePlay();
      refreshUI();
    };
    beatBox.appendChild(btn);
  }

  const partBox = $('#partChips');
  for (const p of PARTS) {
    const btn = document.createElement('button');
    btn.className = 'chip';
    btn.onclick = () => {
      initAudio();
      transport.parts[p] = !transport.parts[p];
      if (!transport.playing && transport.parts[p]) togglePlay();
      refreshUI();
    };
    partBox.appendChild(btn);
  }

  const leds = $('#leds');
  for (let i = 0; i < 4; i++) {
    const sp = document.createElement('span');
    if (i === 0) sp.className = 'down';
    leds.appendChild(sp);
  }

  // Top bar buttons
  $('#keyDown').onclick = () => { state.key = (state.key + 11) % 12; refreshUI(); };
  $('#keyUp').onclick = () => { state.key = (state.key + 1) % 12; refreshUI(); };
  $('#toneDown').onclick = () => {
    const i = SCALE_ORDER.indexOf(state.scale);
    state.scale = SCALE_ORDER[(i + SCALE_ORDER.length - 1) % SCALE_ORDER.length];
    refreshUI();
  };
  $('#toneUp').onclick = () => {
    const i = SCALE_ORDER.indexOf(state.scale);
    state.scale = SCALE_ORDER[(i + 1) % SCALE_ORDER.length];
    refreshUI();
  };
  $('#strumBtn').onclick = () => {
    state.settings.strumMode = state.settings.strumMode === 'hover' ? 'click' : 'hover';
    refreshUI();
    toast(state.settings.strumMode === 'hover' ? 'Hover-Strum active' : 'Click-Strum active');
  };
  $('#themeBtn').onclick = () => {
    const i = THEME_ORDER.indexOf(state.settings.theme);
    state.settings.theme = THEME_ORDER[(i + 1) % THEME_ORDER.length];
    refreshUI();
    toast(`Theme: ${THEMES[state.settings.theme].name}`);
  };
  $('#shapeBtn').onclick = () => setShape(state.shape === 'landscape' ? 'vertical' : 'landscape');
  $('#recMode').onclick = () => {
    if (recorder.on) return;
    recorder.mode = recorder.mode === 'video' ? 'audio' : 'video';
    refreshUI();
  };
  $('#recBtn').onclick = () => toggleRec();
  $('#filmBtn').onclick = () => startFilm();
  $('#filmStop').onclick = () => { if (recorder.on) toggleRec(); };
  $('#cleanExit').onclick = () => toggleClean();
  $('#clearBtn').onclick = () => { clearStrings(); toast('Cleared stage (Ctrl+Z to undo)'); };
  $('#helpBtn').onclick = () => $('#helpModal').classList.add('open');
  $('#setBtn').onclick = () => { refreshUI(); $('#setModal').classList.add('open'); };
  $('#setupsBtn').onclick = () => { renderSetupsModal(); $('#setupsModal').classList.add('open'); };

  // Dock buttons
  $('#playBtn').onclick = () => togglePlay();
  $('#bpmDown').onclick = () => { transport.bpm = clamp(transport.bpm - 2, 50, 180); refreshUI(); };
  $('#bpmUp').onclick = () => { transport.bpm = clamp(transport.bpm + 2, 50, 180); refreshUI(); };
  $('#followBtn').onclick = () => { transport.follow = !transport.follow; refreshUI(); };
  $('#layerBtn').onclick = () => {
    const err = armLayer();
    if (err) toast(err);
    else if (transport.rec) toast('Count-in (1 bar)... start playing on the next downbeat!');
  };
  $('#barsDown').onclick = () => { transport.loopBars = clamp(transport.loopBars / 2, 1, 8); refreshUI(); };
  $('#barsUp').onclick = () => { transport.loopBars = clamp(transport.loopBars * 2, 1, 8); refreshUI(); };
  $('#undoLayer').onclick = () => { if (undoLayer()) toast('Removed last loop layer'); };
  $('#mixBtn').onclick = () => { renderMixerModal(); $('#mixModal').classList.add('open'); };

  // Welcome modal
  $('#startPlay').onclick = () => {
    initAudio();
    $('#startModal').classList.remove('open');
  };
  $('#startEmpty').onclick = () => {
    initAudio();
    clearStrings();
    $('#startModal').classList.remove('open');
  };

  // Close modal buttons & backdrop click
  document.querySelectorAll<HTMLButtonElement>('[data-close]').forEach(btn => {
    btn.onclick = () => $(`#${btn.dataset.close}`).classList.remove('open');
  });
  document.querySelectorAll<HTMLElement>('.modal').forEach(mod => {
    mod.addEventListener('click', e => {
      if (e.target === mod && mod.id !== 'startModal') mod.classList.remove('open');
    });
  });

  // Settings bindings
  $<HTMLSelectElement>('#sTheme').onchange = e => {
    state.settings.theme = (e.target as HTMLSelectElement).value as ThemeId;
    refreshUI();
  };
  $<HTMLSelectElement>('#sStrum').onchange = e => {
    state.settings.strumMode = (e.target as HTMLSelectElement).value as 'hover' | 'click';
    refreshUI();
  };
  $<HTMLInputElement>('#sWave').oninput = e => {
    state.settings.waveIntensity = parseFloat((e.target as HTMLInputElement).value);
  };
  $<HTMLInputElement>('#sReverb').oninput = e => {
    state.settings.reverb = parseFloat((e.target as HTMLInputElement).value);
    setReverbAmount(state.settings.reverb);
  };
  $<HTMLInputElement>('#sVol').oninput = e => {
    state.settings.volume = parseFloat((e.target as HTMLInputElement).value);
    setMasterVolume(state.settings.volume);
  };
  $<HTMLInputElement>('#sQuant').onchange = e => {
    state.settings.quantize = (e.target as HTMLInputElement).checked;
  };
  $<HTMLInputElement>('#sLabels').onchange = e => {
    state.settings.labels = (e.target as HTMLInputElement).checked;
  };

  // Setups save & JSON import/export
  $('#setupSave').onclick = () => {
    const inp = $<HTMLInputElement>('#setupName');
    const name = inp.value.trim() || `Setup ${new Date().toLocaleTimeString()}`;
    const list = getStoredSetups();
    list.unshift(snapshotSetup(name));
    saveStoredSetups(list.slice(0, 20));
    inp.value = '';
    renderSetupsModal();
    toast(`Saved "${name}"`);
  };
  $('#setupFileOut').onclick = () => {
    const data = snapshotSetup('Ripple setup');
    downloadBlob(new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' }), 'ripple-setup.json');
  };
  $('#setupFileIn').onclick = () => $<HTMLInputElement>('#setupFile').click();
  $<HTMLInputElement>('#setupFile').onchange = async e => {
    const file = (e.target as HTMLInputElement).files?.[0];
    if (!file) return;
    try {
      const parsed = JSON.parse(await file.text()) as StageSetup;
      if (applySetup(parsed)) {
        $('#setupsModal').classList.remove('open');
        toast(`Loaded "${parsed.name || file.name}"`);
      }
    } catch {
      toast('Could not read setup JSON.');
    }
    (e.target as HTMLInputElement).value = '';
  };

  // Mixer Stems export
  $('#stemsBtn').onclick = async () => {
    const note = $('#stemsNote');
    const btn = $<HTMLButtonElement>('#stemsBtn');
    btn.disabled = true;
    try {
      const zip = await renderStemsZip(msg => { note.textContent = msg; });
      if (zip) {
        downloadBlob(zip, `ripple-parts-${transport.bpm}bpm.zip`);
        note.textContent = 'Stems ZIP downloaded!';
      }
    } catch (err) {
      note.textContent = 'Stem export failed: ' + String(err);
    } finally {
      btn.disabled = false;
    }
  };

  // Save Recording modal downloads
  $('#saveVideo').onclick = () => {
    const take = recorder.lastTake;
    if (take?.videoBlob) downloadBlob(take.videoBlob, `ripple-take.${take.videoExt}`);
  };
  $('#saveWav').onclick = () => {
    const take = recorder.lastTake;
    if (take) downloadBlob(take.wavBlob, 'ripple-take.wav');
  };

  refreshUI();
}
