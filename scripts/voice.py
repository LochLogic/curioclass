"""Record a tool's spoken lines with Gemini text-to-speech, so Read and narration sound natural in every browser.

    python scripts/voice.py <tool-id> [--force] [--reencode]

Reads tools/<tool-id>/voice/lines.json:
    {"voice": "Puck", "style": "Say warmly, like ...", "lines": ["Sad. Rainy. When I feel sad ...", ...]}
Each line becomes voice/<hash>.mp3 (committed); the raw speech stays in voice/raw/ (not committed), so
--reencode can redo the MP3s for free. scripts/bundle_tool.py turns the token "voice:*" in src.html
into a {line text: data URI} object, and the tool plays a recording when the exact text has one, falling back to
the browser's own voice. Needs GEMINI_API_KEY like scripts/art.py, and `pip install lameenc`.
"""
import hashlib, json, sys, time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MODELS = ['gemini-2.5-flash-preview-tts', 'gemini-2.5-pro-preview-tts']  # the second takes over when the first hits its daily limit


def clip_name(text):
    return hashlib.sha1(text.encode('utf-8')).hexdigest()[:12] + '.mp3'


def record(text, voice, style):
    """Raw 16-bit mono 24 kHz speech from Gemini, retrying through the per-minute quota."""
    sys.path.insert(0, str(ROOT / 'scripts'))
    from art import api_key
    from google import genai
    from google.genai import types
    client = genai.Client(api_key=api_key())
    for attempt in range(8):
        try:
            resp = client.models.generate_content(
                model=MODELS[0], contents=f'{style}: {text}',
                config=types.GenerateContentConfig(response_modalities=['AUDIO'], speech_config=types.SpeechConfig(
                    voice_config=types.VoiceConfig(prebuilt_voice_config=types.PrebuiltVoiceConfig(voice_name=voice)))))
            return resp.candidates[0].content.parts[0].inline_data.data
        except Exception as e:
            if '429' in str(e) and 'per_day' in str(e) and len(MODELS) > 1:
                MODELS.pop(0)
                print(f'daily limit reached, switching to {MODELS[0]}')
                continue
            if '429' not in str(e) or attempt == 7:
                raise
            time.sleep(15)


def encode(pcm):
    """Trim the silence at both ends and encode a small MP3 (24 kbps is plenty for one voice)."""
    import numpy as np, lameenc
    a = np.frombuffer(pcm, dtype=np.int16)
    loud = np.flatnonzero(np.abs(a) > 400)
    if len(loud):
        a = a[max(0, loud[0] - 2400):loud[-1] + 3600]  # keep 0.1 s before and 0.15 s after
    enc = lameenc.Encoder()
    enc.set_bit_rate(24); enc.set_in_sample_rate(24000); enc.set_channels(1); enc.set_quality(2)
    return enc.encode(a.tobytes()) + enc.flush()


def main():
    tool, force = sys.argv[1], '--force' in sys.argv
    folder = ROOT / 'tools' / tool / 'voice'
    spec = json.loads((folder / 'lines.json').read_text(encoding='utf-8'))
    raw = folder / 'raw'
    raw.mkdir(exist_ok=True)
    keep = set()
    for text in spec['lines']:
        f = folder / clip_name(text)
        r = raw / (f.stem + '.pcm')
        keep.add(f.name)
        if not r.exists() or force:
            r.write_bytes(record(text, spec.get('voice', 'Puck'), spec.get('style', 'Read this aloud clearly and warmly')))
        elif f.exists() and '--reencode' not in sys.argv:
            continue
        f.write_bytes(encode(r.read_bytes()))
        print(f'recorded {f.name}: {f.stat().st_size // 1024} KB  {text[:60]}')
    for old in folder.glob('*.mp3'):
        if old.name not in keep:
            old.unlink()
            print(f'removed unused {old.name}')


if __name__ == '__main__':
    main()
