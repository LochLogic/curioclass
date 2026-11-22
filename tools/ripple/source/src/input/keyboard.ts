import { clamp } from '../core/music';
import { state, transport } from '../core/state';
import { armLayer, togglePlay, undoLayer } from '../audio/sequencer';
import {
  closeMenu, pluckZone, redoEdit, removeString, undoEdit,
} from './strings';

const QWERTY_KEYS = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', "'"];

export interface KeyboardActions {
  toggleRec: () => void;
  toggleFilm: () => void;
  toggleClean: () => void;
  refreshUI: () => void;
  toast: (msg: string) => void;
}

export function initKeyboard(actions: KeyboardActions): void {
  window.addEventListener('keydown', e => {
    const tag = (e.target as HTMLElement | null)?.tagName;
    if (tag === 'INPUT' || tag === 'TEXTAREA' || tag === 'SELECT') return;

    const k = e.key.toLowerCase();

    // Undo / Redo string edits
    if ((e.ctrlKey || e.metaKey) && k === 'z') {
      e.preventDefault();
      if (e.shiftKey) redoEdit();
      else undoEdit();
      return;
    }
    if ((e.ctrlKey || e.metaKey) && k === 'y') {
      e.preventDefault();
      redoEdit();
      return;
    }

    if (e.ctrlKey || e.metaKey || e.altKey) return;

    if (e.key === 'Escape') {
      if (state.menu) { closeMenu(); return; }
      const openModal = document.querySelector('.modal.open');
      if (openModal) { openModal.classList.remove('open'); return; }
      if (state.clean) { actions.toggleClean(); return; }
      return;
    }

    if (document.querySelector('.modal.open')) return;

    // QWERTY melodic playing on the focused/selected string
    const qIdx = QWERTY_KEYS.indexOf(k);
    if (qIdx >= 0 && !e.repeat) {
      const s = state.strings.find(x => x.id === state.selectedId) || state.strings[0];
      if (s) {
        state.selectedId = s.id;
        pluckZone(s, qIdx, 0.8);
      }
      return;
    }

    // 1..9 selects string by index
    if (k >= '1' && k <= '9') {
      const idx = parseInt(k, 10) - 1;
      if (state.strings[idx]) {
        state.selectedId = state.strings[idx].id;
        actions.toast(`Focused string ${idx + 1}`);
      }
      return;
    }

    if (e.key === 'Tab' && state.strings.length > 0) {
      e.preventDefault();
      const idx = state.strings.findIndex(x => x.id === state.selectedId);
      const next = state.strings[(idx + 1) % state.strings.length];
      state.selectedId = next.id;
      return;
    }

    if (e.key === 'Delete' || e.key === 'Backspace') {
      const s = state.strings.find(x => x.id === state.selectedId);
      if (s) {
        e.preventDefault();
        removeString(s);
        actions.toast('Removed string (Ctrl+Z to undo)');
      }
      return;
    }

    if (e.code === 'Space') {
      e.preventDefault();
      togglePlay();
      return;
    }

    if (k === 'm') {
      state.settings.strumMode = state.settings.strumMode === 'hover' ? 'click' : 'hover';
      actions.refreshUI();
      actions.toast(state.settings.strumMode === 'hover' ? 'Hover-Strum active' : 'Click-Strum active');
      return;
    }

    if (k === 'l') {
      const err = armLayer();
      if (err) actions.toast(err);
      return;
    }

    if (k === 'z') {
      if (undoLayer()) actions.toast('Removed last loop layer');
      return;
    }

    if (k === 'r') { actions.toggleRec(); return; }
    if (k === 'f') { actions.toggleFilm(); return; }
    if (k === 'h') { actions.toggleClean(); return; }

    if (e.key === '[') {
      state.key = (state.key + 11) % 12;
      actions.refreshUI();
      return;
    }
    if (e.key === ']') {
      state.key = (state.key + 1) % 12;
      actions.refreshUI();
      return;
    }
    if (e.key === '-' || e.key === '_') {
      transport.bpm = clamp(transport.bpm - 2, 50, 180);
      actions.refreshUI();
      return;
    }
    if (e.key === '=' || e.key === '+') {
      transport.bpm = clamp(transport.bpm + 2, 50, 180);
      actions.refreshUI();
      return;
    }
  });
}
