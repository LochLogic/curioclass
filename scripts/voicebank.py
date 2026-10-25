r"""Record the voice bank's reference clips with Gemini (once per voice), for Qwen3-TTS to clone from.

    python scripts/voicebank.py [voice-id ...]       record the missing references (3 lines each, about 72 requests for 24)

voices/bank.json lists each voice (Gemini voice + style). Each gets the bank's three shared lines, trimmed and joined
with short pauses into voices/<id>/ref.wav (15 to 20 s) and voices/<id>/ref.txt (the words, for cloning).
The bank is frozen once recorded: nothing here needs Gemini again. A tool uses a voice with "bank": "<id>" in its
voice/lines.json; scripts/localvoice.py then clones that reference.
"""
import json, sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'scripts'))
from voice import record  # noqa: E402


def trim(a):
    loud = np.flatnonzero(np.abs(a) > 400)
    return a[max(0, loud[0] - 1200):loud[-1] + 2400] if len(loud) else a


def main():
    import soundfile as sf
    bank = json.loads((ROOT / 'voices' / 'bank.json').read_text(encoding='utf-8'))
    wanted = set(sys.argv[1:])
    for v in bank['voices']:
        out = ROOT / 'voices' / v['id']
        if (wanted and v['id'] not in wanted) or (out / 'ref.wav').exists():
            continue
        out.mkdir(parents=True, exist_ok=True)
        parts = []
        for i, line in enumerate(bank['lines']):
            f = out / f'take{i}.pcm'  # kept, so a failed run picks up where it stopped
            if not f.exists():
                f.write_bytes(record(line, v['voice'], v['style']))
            parts.append(trim(np.frombuffer(f.read_bytes(), dtype=np.int16)))
        gap = np.zeros(int(24000 * .45), np.int16)
        ref = np.concatenate([p for a in parts for p in (a, gap)][:-1])
        sf.write(out / 'ref.wav', ref, 24000)
        (out / 'ref.txt').write_text(' '.join(bank['lines']), encoding='utf-8')
        print(f"{v['id']} ({v['voice']}): {len(ref) / 24000:.1f} s", flush=True)


if __name__ == '__main__':
    main()
