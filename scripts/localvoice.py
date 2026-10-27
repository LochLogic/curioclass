r"""Record a tool's spoken lines on this PC with Qwen3-TTS (Apache 2.0), cloning the tool's own Gemini voice.

    S:\AI\tts\.venv\Scripts\python.exe scripts/localvoice.py <tool-id> [--n 40]

With "bank": "<voice-id>" in voice/lines.json the tool clones a frozen voice from voices/ (scripts/voicebank.py) and
Gemini is never called. Without it, the tool's own Gemini voice is copied as below.

Each tool's voice comes from voice/lines.json (Gemini voice + style). Qwen copies it from one reference clip, so local
lines sound like the Gemini ones and the two can mix in one tool:
  1. The reference is a Gemini recording already in voice/raw/ (3 to 9 seconds, the longest), or "ref" in lines.json
     names the line to use. With none recorded yet, it records one line with Gemini first (one request).
  2. Every line still missing is cloned in batches and saved to voice/raw/ like a Gemini take.
  3. scripts/voice.py (in the normal Python) then encodes the MP3s, with the tool's tempo.
--n caps how many lines one run makes. Lines made here are listed in voice/local.json (credit: Qwen3-TTS, Apache 2.0).
No daily limit; about 1 to 2 seconds of GPU per line on the RTX 5080. The designed-voice mode is not used: Cory
found it sounded wrong for children's tools (2026-10-25). Listen before shipping; a take that runs far too long or
short for its text is redone once and then flagged.
"""
import json, shutil, subprocess, sys
from pathlib import Path

import numpy as np
import torch

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'scripts'))
from voice import clip_name  # noqa: E402

PY = shutil.which('python') or 'python'  # the normal Python (lameenc, the Gemini SDK), not this venv
SR = 24000


def pcm_of(f):
    return np.frombuffer(f.read_bytes(), dtype=np.int16)


def plausible(text, wav):
    secs = len(wav) / SR
    return len(text) * .03 < secs < len(text) * .11 + 2.5


def liveliest(text, wavs):
    """The take that sounds least bored: higher median pitch plus more rise and fall (Cory heard a flat batch, 2026-10-26)."""
    import librosa
    def score(w):
        w = np.asarray(w, dtype=np.float32)
        if not plausible(text, w):
            return -1e9
        f0, voiced, _ = librosa.pyin(w, fmin=60, fmax=400, sr=SR, frame_length=1024)
        f0 = f0[voiced & ~np.isnan(f0)]
        if len(f0) < 10:
            return -1e9
        return np.median(f0) / 10 + (12 * np.log2(f0 / np.median(f0))).std()
    return max(wavs, key=score)


def main():
    tool = sys.argv[1]
    cap = int(sys.argv[sys.argv.index('--n') + 1]) if '--n' in sys.argv else 10 ** 6
    folder = ROOT / 'tools' / tool / 'voice'
    spec = json.loads((folder / 'lines.json').read_text(encoding='utf-8'))
    raw = folder / 'raw'; raw.mkdir(exist_ok=True)
    lines = list(dict.fromkeys([*spec['lines'], *(t for g in spec.get('groups', []) for t in g)]))
    rawf = lambda t: raw / (Path(clip_name(t)).stem + '.pcm')
    local = json.loads((folder / 'local.json').read_text(encoding='utf-8')) if (folder / 'local.json').exists() else {}

    def ref_pick():
        if spec.get('ref') and rawf(spec['ref']).exists():
            return spec['ref']
        gem = [t for t in lines if rawf(t).exists() and t not in local and 3 <= len(pcm_of(rawf(t))) / SR <= 9]
        return max(gem, key=lambda t: len(pcm_of(rawf(t))), default=None)

    bank = spec.get('bank')  # a voice from the frozen bank (voices/bank.json): no Gemini at all
    if bank:
        bdir = ROOT / 'voices' / bank
        if not (bdir / 'ref.wav').exists():
            sys.exit(f'voice bank has no {bank} yet (python scripts/voicebank.py {bank})')
        import soundfile as sf
        ref_audio, ref = (sf.read(bdir / 'ref.wav', dtype='float32')[0], SR), (bdir / 'ref.txt').read_text(encoding='utf-8')
    else:
        ref = ref_pick(); ref_audio = None
    if not ref:  # no Gemini take yet: record one so there is a voice to copy
        first = max((t for t in lines if 40 <= len(t) <= 120), key=len, default=lines[0])
        print(f'no reference yet: recording one line with Gemini: {first[:60]}')
        subprocess.run([PY, str(ROOT / 'scripts' / 'voice.py'), tool, '--only', first], check=True)
        ref = ref_pick() or (first if rawf(first).exists() else None)
        if not ref:
            sys.exit('could not get a reference clip (Gemini quota?); add one with scripts/voice.py first')
    # --redo 1,4,9 --takes 5: re-record those lines (lines.json order), keeping the liveliest of N takes
    redo = [lines[int(i)] for i in sys.argv[sys.argv.index('--redo') + 1].split(',')] if '--redo' in sys.argv else []
    takes = int(sys.argv[sys.argv.index('--takes') + 1]) if '--takes' in sys.argv else 5
    for t in redo:
        rawf(t).unlink(missing_ok=True)
        (folder / clip_name(t)).unlink(missing_ok=True)
    todo = [t for t in lines if not rawf(t).exists()][:cap]
    print(f'{tool}: {len(todo)} lines to make, copying the voice of: {ref[:60]}', flush=True)
    if not todo:
        return
    from qwen_tts import Qwen3TTSModel
    m = Qwen3TTSModel.from_pretrained('Qwen/Qwen3-TTS-12Hz-1.7B-Base', device_map='cuda:0', dtype=torch.bfloat16)
    prompt = m.create_voice_clone_prompt(ref_audio=ref_audio or (pcm_of(rawf(ref)).astype(np.float32) / 32768, SR), ref_text=ref)
    flagged = []
    for i in range(0, len(todo), 8):
        batch = todo[i:i + 8]
        wavs, sr = m.generate_voice_clone(text=batch, language=['English'] * len(batch), voice_clone_prompt=prompt)
        assert sr == SR, sr
        for text, w in zip(batch, wavs):
            if text in redo:
                w = liveliest(text, [w, *(m.generate_voice_clone(text=[text], language=['English'], voice_clone_prompt=prompt)[0][0]
                                          for _ in range(takes - 1))])
            if not plausible(text, w):  # one retry for a take that rambles or cuts off
                w = m.generate_voice_clone(text=[text], language=['English'], voice_clone_prompt=prompt)[0][0]
                if not plausible(text, w):
                    flagged.append(text)
            rawf(text).write_bytes((np.clip(np.asarray(w), -1, 1) * 32767).astype(np.int16).tobytes())
            local[text] = 'qwen3-tts-1.7b-base clone'
        print(f'  made {min(i + 8, len(todo))} of {len(todo)}', flush=True)
        (folder / 'local.json').write_text(json.dumps(local, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    subprocess.run([PY, str(ROOT / 'scripts' / 'voice.py'), tool, '--no-record'], check=True)  # encode the new MP3s only
    for t in flagged:
        print(f'  CHECK by ear (length looked off): {t}')


if __name__ == '__main__':
    main()
