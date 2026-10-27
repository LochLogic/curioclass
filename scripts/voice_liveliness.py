r"""How lively each recorded line sounds: median pitch, pitch movement and speaking rate per take.

    S:\AI\tts\.venv\Scripts\python.exe scripts/voice_liveliness.py <tool-id> [--flat 3.0]

Run it after `localvoice.py` (it needs librosa, which is in the TTS venv). Cory heard a "very bored" batch in Score
Keeper (2026-10-26); those takes had a pitch movement (semitone SD) under about 3. Lines below --flat are listed at the
end with their lines.json index, ready for `localvoice.py <id> --redo i,j --takes 5`, which keeps the liveliest take.
Judge praise lines ("You fixed it!") by ear even when they pass: they should sound the brightest.
"""
import json, sys
from pathlib import Path

import librosa
import numpy as np

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'scripts'))
from voice import clip_name  # noqa: E402


def main():
    tool = sys.argv[1]
    flat = float(sys.argv[sys.argv.index('--flat') + 1]) if '--flat' in sys.argv else 3.0
    folder = ROOT / 'tools' / tool / 'voice'
    lines = json.loads((folder / 'lines.json').read_text(encoding='utf-8'))['lines']
    low = []
    for i, t in enumerate(lines):
        f = folder / 'raw' / (Path(clip_name(t)).stem + '.pcm')
        if not f.exists():
            print(f'{i:2d} MISSING  {t[:55]}')
            continue
        w = np.frombuffer(f.read_bytes(), dtype=np.int16).astype(np.float32) / 32768
        f0, voiced, _ = librosa.pyin(w, fmin=60, fmax=400, sr=24000, frame_length=1024)
        f0 = f0[voiced & ~np.isnan(f0)]
        if len(f0) < 10:
            print(f'{i:2d} TOO SHORT TO MEASURE  {t[:55]}')
            continue
        st = 12 * np.log2(f0 / np.median(f0))
        sd = st.std()
        print(f'{i:2d} f0med {np.median(f0):5.0f}  semis-sd {sd:4.2f}  range {np.percentile(st, 95) - np.percentile(st, 5):4.1f}'
              f'  rate {len(t) / (len(w) / 24000):4.1f}c/s  {t[:55]}')
        if sd < flat:
            low.append(i)
    print(f'flat (semis-sd under {flat}): ' + (','.join(map(str, low)) if low else 'none'))


if __name__ == '__main__':
    main()
