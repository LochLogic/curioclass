"""Record a tool's spoken lines with Gemini text-to-speech, so Read and narration sound natural in every browser.

    python scripts/voice.py <tool-id> [--force] [--reencode]

Reads tools/<tool-id>/voice/lines.json:
    {"voice": "Puck", "style": "Say warmly, like ...", "lines": ["Sad. Rainy. When I feel sad ...", ...]}
Optional "tempo": 1.2 speeds every clip up (pitch kept) at encode time, so --reencode changes the pace for free.
Optional "groups": [["1", "2", ..., "10"], ...] records each group as one counted list and splits it at the pauses,
so a run of short lines (numbers) costs one request instead of ten; a group that doesn't split cleanly is recorded
line by line. Group lines are spoken lines too and don't need repeating in "lines".
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
            content = resp.candidates[0].content
            if content is None or not content.parts:  # the TTS preview sometimes returns no audio; ask again
                if attempt == 7:
                    raise RuntimeError(f'no audio returned for: {text[:60]}')
                print(f'no audio returned (finish reason {resp.candidates[0].finish_reason}), retrying')
                continue
            return content.parts[0].inline_data.data
        except Exception as e:
            if '429' in str(e) and 'per_day' in str(e) and len(MODELS) > 1:
                MODELS.pop(0)
                print(f'daily limit reached, switching to {MODELS[0]}')
                continue
            if 'tried to generate text' in str(e) and attempt < 7:  # another intermittent TTS preview refusal
                continue
            if '429' not in str(e) or attempt == 7:
                raise
            time.sleep(15)


def stretch(a, rate):
    """Speed speech up by `rate` without changing its pitch (WSOLA: overlap-add 40 ms windows, each nudged up to
    10 ms to line up with the last one, so there's no phasey echo)."""
    import numpy as np
    x = a.astype(np.float32)
    n, hop, tol = 960, 480, 240
    win = np.hanning(n).astype(np.float32)
    steps = int((len(x) - n - tol) / (hop * rate))
    if steps < 2:
        return a
    out = np.zeros(steps * hop + n, np.float32); norm = np.zeros_like(out)
    want = None  # what would naturally follow the last window placed
    for k in range(steps):
        c = int(k * hop * rate)
        lo, hi = max(0, c - tol), min(len(x) - n, c + tol)
        best = c if want is None else lo + int(np.argmax(np.correlate(x[lo:hi + n], want, 'valid')))
        out[k * hop:k * hop + n] += x[best:best + n] * win; norm[k * hop:k * hop + n] += win
        want = x[best + hop:best + hop + n] if best + hop + n <= len(x) else None
    out /= np.maximum(norm, 1e-3)
    return np.clip(out, -32768, 32767).astype(np.int16)


def encode(pcm, tempo=1.0):
    """Trim the silence at both ends and encode a small MP3 (24 kbps is plenty for one voice).
    tempo above 1 speeds the speech up without raising the pitch (lines.json "tempo")."""
    import numpy as np, lameenc
    a = np.frombuffer(pcm, dtype=np.int16)
    loud = np.flatnonzero(np.abs(a) > 400)
    if len(loud):
        a = a[max(0, loud[0] - 2400):loud[-1] + 3600]  # keep 0.1 s before and 0.15 s after
    if tempo != 1.0:
        a = stretch(a, tempo)
    enc = lameenc.Encoder()
    enc.set_bit_rate(24); enc.set_in_sample_rate(24000); enc.set_channels(1); enc.set_quality(2)
    return enc.encode(a.tobytes()) + enc.flush()


def split(pcm, n):
    """Cut a counted list into n clips at its n - 1 longest pauses, or None if the pauses aren't clear."""
    import numpy as np
    a = np.frombuffer(pcm, dtype=np.int16)
    loud = np.abs(a) > 500
    win = 240  # 10 ms
    frames = loud[:len(loud) // win * win].reshape(-1, win).any(axis=1)
    runs, start = [], None  # silent stretches between sounds, in frames
    first, last = np.flatnonzero(frames)[[0, -1]]
    for i in range(first, last + 1):
        if not frames[i] and start is None:
            start = i
        elif frames[i] and start is not None:
            runs.append((i - start, start, i)); start = None
    runs.sort(reverse=True)
    if len(runs) < n - 1 or runs[n - 2][0] < 18 or (len(runs) >= n and runs[n - 1][0] > runs[n - 2][0] * .6):
        return None  # fewer than n - 1 real pauses (180 ms or more), or no clear gap between pauses and the rest
    cuts = sorted((s + e) // 2 * win for _, s, e in runs[:n - 1])
    edges = [0, *cuts, len(a)]
    return [a[edges[k]:edges[k + 1]].tobytes() for k in range(n)]


def main():
    tool, force = sys.argv[1], '--force' in sys.argv
    folder = ROOT / 'tools' / tool / 'voice'
    spec = json.loads((folder / 'lines.json').read_text(encoding='utf-8'))
    raw = folder / 'raw'
    raw.mkdir(exist_ok=True)
    keep = set()
    for group in spec.get('groups', []):
        names = [raw / (Path(clip_name(t)).stem + '.pcm') for t in group]
        if all(r.exists() for r in names) and not force:
            continue
        try:
            pcm = record('. '.join(group) + '.', spec.get('voice', 'Puck'), spec.get('group_style', 'Count slowly and clearly, with a full pause after each number'))
        except RuntimeError:
            pcm = None  # no audio for the whole group; fall back to its lines one at a time
        parts = pcm and split(pcm, len(group))
        if parts:
            for r, part in zip(names, parts):
                r.write_bytes(part)
            print(f'recorded group {group[0]}..{group[-1]} in one request')
        else:
            print(f'group {group[0]}..{group[-1]} did not split cleanly; recording its lines one at a time')
    for text in [*spec['lines'], *(t for g in spec.get('groups', []) for t in g)]:
        f = folder / clip_name(text)
        r = raw / (f.stem + '.pcm')
        keep.add(f.name)
        if not r.exists() or force:
            r.write_bytes(record(text, spec.get('voice', 'Puck'), spec.get('style', 'Read this aloud clearly and warmly')))
        elif f.exists() and '--reencode' not in sys.argv:
            continue
        f.write_bytes(encode(r.read_bytes(), spec.get('tempo', 1.0)))
        print(f'recorded {f.name}: {f.stat().st_size // 1024} KB  {text[:60]}')
    for old in folder.glob('*.mp3'):
        if old.name not in keep:
            old.unlink()
            print(f'removed unused {old.name}')


if __name__ == '__main__':
    main()
