r"""A listening page for the voice bank: each voice's Gemini reference, then Qwen3-TTS cloning it on two new lines.

    S:\AI\tts\.venv\Scripts\python.exe scripts/voicebank_sample.py      -> shots/voice-bank.html
"""
import base64, json
from pathlib import Path

import numpy as np, soundfile as sf, torch, lameenc
from qwen_tts import Qwen3TTSModel

ROOT = Path(__file__).resolve().parent.parent
TEST = ["Can you find the shape with three sides? Point to it and say its name out loud!",
        "Notice how the curve flattens out as the numbers grow. What would happen if we doubled the rate?"]


def mp3(a, sr=24000):
    a = (np.clip(np.asarray(a, dtype=np.float32), -1, 1) * 32767).astype(np.int16)
    e = lameenc.Encoder(); e.set_bit_rate(40); e.set_in_sample_rate(sr); e.set_channels(1); e.set_quality(2)
    return base64.b64encode(e.encode(a.tobytes()) + e.flush()).decode()


bank = json.loads((ROOT / 'voices' / 'bank.json').read_text(encoding='utf-8'))
m = Qwen3TTSModel.from_pretrained('Qwen/Qwen3-TTS-12Hz-1.7B-Base', device_map='cuda:0', dtype=torch.bfloat16)
h = ['<!doctype html><meta charset=utf-8><title>Voice bank</title><style>body{font:16px system-ui;max-width:1000px;margin:24px auto;padding:0 16px}'
     '.v{border-top:1px solid #ddd;padding:12px 0}.v h2{font-size:17px;margin:0 0 2px}.v p{margin:0 0 8px;color:#666;font-size:14px}'
     '.g{display:grid;grid-template-columns:repeat(3,1fr);gap:8px}.c{background:#f3f1ea;border-radius:10px;padding:8px}.c b{display:block;font-size:12px;margin-bottom:4px}audio{width:100%}</style>'
     '<h1>Voice bank candidates</h1><p>Each voice: the Gemini reference it is cloned from, then two lines made on this PC by copying it. '
     'Pick the ones to keep (any number). Line 1 is for little kids, line 2 for older students.</p>']
for v in bank['voices']:
    d = ROOT / 'voices' / v['id']
    if not (d / 'ref.wav').exists():
        continue
    ref, _ = sf.read(d / 'ref.wav', dtype='float32')
    prompt = m.create_voice_clone_prompt(ref_audio=(ref, 24000), ref_text=(d / 'ref.txt').read_text(encoding='utf-8'))
    wavs, sr = m.generate_voice_clone(text=TEST, language=['English'] * 2, voice_clone_prompt=prompt, max_new_tokens=600)
    cells = [('Gemini reference', mp3(ref))] + [(f'Clone, line {i + 1}', mp3(w, sr)) for i, w in enumerate(wavs)]
    h.append(f'<div class="v"><h2>{v["id"]} <small>({v["voice"]})</small></h2><p>{v["style"]}. For: {v["for"]}</p><div class="g">'
             + ''.join(f'<div class="c"><b>{k}</b><audio controls preload="none" src="data:audio/mpeg;base64,{b}"></audio></div>' for k, b in cells) + '</div></div>')
    print('sampled', v['id'], flush=True)
(ROOT / 'shots' / 'voice-bank.html').write_text(''.join(h), encoding='utf-8')
print('wrote shots/voice-bank.html')
