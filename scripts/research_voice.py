r"""Recorded voice for the research cards' "Read to me" button (page 1), made on the Forge with Qwen3-TTS.

    S:\AI\tts\.venv\Scripts\python.exe scripts/research_voice.py record [--ids a,b] [--voice warm-teacher]
    S:\AI\tts\.venv\Scripts\python.exe scripts/research_voice.py collect <forge-job-name>
    S:\AI\tts\.venv\Scripts\python.exe scripts/research_voice.py assemble [--ids a,b] [--voice warm-teacher]

Cory asked for a better voice than the browser's and highlights that match (2026-11-04). Each card's page 1 is cut
into the same blocks the page lights up (title, each paragraph, "Quick facts", each fact, "Words to know", each word
row). Every block is cloned from a bank voice (voices/, scripts/voicebank.py) on the Forge, using the same worker as
scripts/localvoice.py, then brought back to build/research-voice/<voice>/ (gitignored).

assemble joins a card's blocks with short pauses into site/assets/research/voice/<id>.mp3 and times every word with
Whisper (large-v3, word timestamps, matched back to the card's own words, gaps filled by length, starts snapped to
where the voice resumes after a pause). The times go to
data/research-voice.json: {"voice": ..., "cards": {id: {"blocks": [[start ms, [word start ms, ...]], ...]}}}. The
page plays the MP3 and lights each word from those times; cards without a recording keep the browser voice.
"""
import difflib, hashlib, json, os, re, shutil, sys, tempfile, time
from pathlib import Path

import numpy as np

os.environ.setdefault('HF_HOME', r'S:\AI\models\huggingface')  # Whisper lives in the shared model store
os.environ.setdefault('HF_HUB_OFFLINE', '1')
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'scripts'))
import localvoice as lv  # noqa: E402  (Forge plumbing, SR, the worker itself)

SR = lv.SR
CARDS = json.loads((ROOT / 'data' / 'research-cards.json').read_text(encoding='utf-8'))['cards']
OUT = ROOT / 'site' / 'assets' / 'research' / 'voice'
TIMES = ROOT / 'data' / 'research-voice.json'
GAP = {'title': .55, 'para': .45, 'head': .35, 'item': .35}  # silence after each kind of block, seconds


def blocks(c):
    """Page 1's spoken blocks, in page order, as (kind, text). The text splits on spaces into exactly the words the
    page wraps (closet/research-card.html), so word i here is highlight i there."""
    b = [('title', c['title'])]
    b += [('para', p) for p in c['read']]
    b += [('head', 'Quick facts')] + [('item', f) for f in c['facts']]
    b += [('head', 'Words to know')] + [('item', f'{w}: {m}') for w, m in c['words']]
    return b


def spoken(text):
    """What the voice is given: a heading or title gets a full stop so it is said as a phrase, not run on."""
    return text if re.search(r'[.!?]$', text) else text + '.'


def stem(text, voice):
    return hashlib.sha1(f'{voice}|{spoken(text)}'.encode()).hexdigest()[:16]


def cache(voice):
    d = ROOT / 'build' / 'research-voice' / voice
    d.mkdir(parents=True, exist_ok=True)
    return d


def arg(name, default=None):
    return sys.argv[sys.argv.index(name) + 1] if name in sys.argv else default


def pick(ids):
    return [c for c in CARDS if not ids or c['id'] in ids.split(',')]


def record(cards, voice):
    import soundfile as sf
    bdir = ROOT / 'voices' / voice
    ref_wav, sr = sf.read(bdir / 'ref.wav', dtype='float32')
    assert sr == SR, sr
    have = cache(voice)
    todo = list(dict.fromkeys(spoken(t) for c in cards for _, t in blocks(c) if not (have / f'{stem(t, voice)}.pcm').exists()))
    print(f'{len(cards)} cards, {len(todo)} blocks to record in {voice}', flush=True)
    if not todo:
        return
    name = time.strftime('%Y%m%d-%H%M%S') + f'-voice-research-{voice}'
    tmp = Path(tempfile.mkdtemp())
    job = tmp / name
    job.mkdir()
    lines = [[t, hashlib.sha1(f'{voice}|{t}'.encode()).hexdigest()[:16]] for t in todo]
    (job / 'job.json').write_text(json.dumps({'tool': 'research-cards', 'voice': voice, 'lines': lines, 'redo': [], 'takes': 1,
                                              'home': None, 'ref_text': (bdir / 'ref.txt').read_text(encoding='utf-8')},
                                             ensure_ascii=False), encoding='utf-8')
    sf.write(job / 'ref.wav', ref_wav, SR)
    (tmp / 'job.cmd').write_text(f'@echo off\r\nset CURIO_TTS_MODEL={lv.FMODEL}\r\nset HF_HUB_OFFLINE=1\r\n'
                                 f'"{lv.FPY}" {lv.FDIR}/bin/localvoice.py --worker {lv.FDIR}/jobs/{name}\r\n', encoding='ascii')
    shutil.copyfile(lv.__file__, tmp / 'localvoice.py')
    lv.rsh(f'New-Item -ItemType Directory -Force {lv.FDIR}/bin, {lv.FDIR}/jobs | Out-Null')
    lv.scp('localvoice.py', f'{lv.FORGE}:{lv.FDIR}/bin/localvoice.py', tmp)
    lv.scp(name, f'{lv.FORGE}:{lv.FDIR}/jobs/', tmp)
    lv.scp('job.cmd', f'{lv.FORGE}:E:/forge/queue/pending/{name}.cmd', tmp)
    lv.rsh('Start-ScheduledTask -TaskName Forge-Queue')
    shutil.rmtree(tmp, ignore_errors=True)
    print(f'queued on the Forge as {name}', flush=True)
    lv.forge_wait(name, len(todo))
    collect(name)


def collect(name):
    tmp = Path(tempfile.mkdtemp())
    lv.scp(f'{lv.FORGE}:{lv.FDIR}/jobs/{name}', '.', tmp)
    job = tmp / name
    spec = json.loads((job / 'job.json').read_text(encoding='utf-8'))
    have = cache(spec['voice'])
    got = 0
    for _, s in spec['lines']:
        f = job / 'out' / f'{s}.pcm'
        if f.exists():
            shutil.copyfile(f, have / f'{s}.pcm')
            got += 1
    flagged = json.loads((job / 'flagged.json').read_text(encoding='utf-8')) if (job / 'flagged.json').exists() else []
    shutil.rmtree(tmp, ignore_errors=True)
    print(f'{got} of {len(spec["lines"])} blocks back from the Forge', flush=True)
    for t in flagged:
        print(f'  CHECK by ear (length looked off): {t}')


def trim(a):
    """Cut the silence at both ends, keeping 0.08 s before and 0.12 s after (as scripts/voice.py does)."""
    loud = np.flatnonzero(np.abs(a) > 400)
    return a[max(0, loud[0] - int(.08 * SR)):loud[-1] + int(.12 * SR)] if len(loud) else a


def norm(w):
    return re.sub(r"[^a-z0-9]", '', w.lower())


_asr = None


def word_starts(a, words):
    """Start time (s) of each of the block's words in clip a: Whisper's words matched to ours, the rest spread by length."""
    global _asr
    if _asr is None:
        import torch
        from transformers import pipeline
        _asr = pipeline('automatic-speech-recognition', model='openai/whisper-large-v3',
                        device=0 if torch.cuda.is_available() else -1)
    import librosa
    x = librosa.resample(a.astype(np.float32) / 32768, orig_sr=SR, target_sr=16000)
    got = _asr(x, return_timestamps='word', generate_kwargs={'language': 'en', 'task': 'transcribe'})['chunks']
    heard = [norm(g['text']) for g in got]
    ours = [norm(w) for w in words]
    starts = [None] * len(words)
    for blk in difflib.SequenceMatcher(None, ours, heard, autojunk=False).get_matching_blocks():
        for k in range(blk.size):
            starts[blk.a + k] = got[blk.b + k]['timestamp'][0]
    matched = sum(s is not None for s in starts)
    end = len(a) / SR
    known = [(i, s) for i, s in enumerate(starts) if s is not None]
    if not known or known[0][0] != 0:
        known.insert(0, (0, starts[0] if starts[0] is not None else .05))
        starts[0] = known[0][1]
    known.append((len(words), end))
    for (i, s), (j, e) in zip(known, known[1:]):  # fill each gap in proportion to word length
        if j - i > 1:
            w = [len(words[k]) + 2 for k in range(i, j)]
            t = s
            for k in range(i, j):
                starts[k] = t
                t += (e - s) * w[k - i] / sum(w)
    # Whisper's word times can be off by a few tenths at a pause; the sound itself is exact. A word Whisper puts in (or
    # just before) a pause starts where the voice comes back, and the word nearest a pause's end is pulled onto it.
    for s, e in pauses(a):
        after = [k for k in range(len(starts)) if starts[k] >= e]  # Whisper late: the first word after the pause
        if after and starts[after[0]] - e <= .35 and not any(s - .1 <= x < e for x in starts):
            starts[after[0]] = e
        inside = [k for k in range(len(starts)) if s - .1 <= starts[k] < e]
        if inside:  # only the last of them comes after the pause; any before it ended there, so keep them clear of it
            starts[inside[-1]] = e
            for n, k in enumerate(reversed(inside[:-1]), 1):
                starts[k] = min(starts[k], s - .25 * n)
    for k in range(1, len(starts)):  # never go backwards
        starts[k] = max(starts[k], starts[k - 1])
    k = 0
    while k < len(starts):  # words given one shared start: share out the time up to the next word by length
        j = k
        while j + 1 < len(starts) and starts[j + 1] == starts[k]:
            j += 1
        if j > k:
            nxt = starts[j + 1] if j + 1 < len(starts) else len(a) / SR
            w = [len(words[i]) + 2 for i in range(k, j + 2 if j + 1 < len(starts) else j + 1)]
            span, t = nxt - starts[k], starts[k]
            for i in range(k, j + 1):
                starts[i] = t
                t += span * w[i - k] / sum(w)
        k = j + 1
    return starts, matched


def pauses(a, quiet=700, least=.1):
    """Silent stretches inside the clip (20 ms frames under the quiet level, at least `least` seconds), as (start, end)."""
    f = np.abs(a[:len(a) // 480 * 480].reshape(-1, 480)).max(1) > quiet
    out, st = [], None
    for i, loud in enumerate(f):
        if not loud and st is None:
            st = i
        if loud and st is not None:
            if st and (i - st) * .02 >= least:
                out.append((st * .02, i * .02))
            st = None
    return out


def assemble(cards, voice):
    import lameenc
    have = cache(voice)
    OUT.mkdir(parents=True, exist_ok=True)
    data = json.loads(TIMES.read_text(encoding='utf-8')) if TIMES.exists() else {'voice': voice, 'cards': {}}
    if data.get('voice') != voice and len(cards) == len(CARDS):
        data = {'voice': voice, 'cards': {}}
    for c in cards:
        bl = blocks(c)
        files = [have / f'{stem(t, voice)}.pcm' for _, t in bl]
        if not all(f.exists() for f in files):
            print(f'{c["id"]}: not recorded yet ({sum(f.exists() for f in files)} of {len(files)} blocks)')
            continue
        parts, times, t0, matched, total = [], [], .25, 0, 0
        parts.append(np.zeros(int(.25 * SR), np.int16))
        for (kind, text), f in zip(bl, files):
            a = trim(lv.pcm_of(f))
            words = text.split()
            ws, m = word_starts(a, words)
            matched += m
            total += len(words)
            times.append([round(t0 * 1000), [round((t0 + s) * 1000) for s in ws]])
            parts += [a, np.zeros(int(GAP[kind] * SR), np.int16)]
            t0 += len(a) / SR + GAP[kind]
        pcm = np.concatenate(parts)
        speech = np.abs(pcm[np.abs(pcm) > 400]).astype(float)
        if len(speech):
            rms = np.sqrt((speech ** 2).mean())
            pcm = (pcm * min(4500 / rms, 28000 / speech.max())).astype(np.int16)
        enc = lameenc.Encoder()
        enc.set_bit_rate(40); enc.set_in_sample_rate(SR); enc.set_channels(1); enc.set_quality(2)
        (OUT / f'{c["id"]}.mp3').write_bytes(enc.encode(pcm.tobytes()) + enc.flush())
        data['voice'] = voice
        data['cards'][c['id']] = {'blocks': times}
        print(f'{c["id"]}: {t0:.0f} s, {matched} of {total} words timed by Whisper', flush=True)
    data['cards'] = dict(sorted(data['cards'].items()))
    TIMES.write_text(json.dumps(data, separators=(',', ':')) + '\n', encoding='utf-8')


def main():
    cmd = sys.argv[1]
    voice = arg('--voice', 'warm-teacher')
    if cmd == 'record':
        record(pick(arg('--ids')), voice)
    elif cmd == 'collect':
        collect(sys.argv[2])
    elif cmd == 'assemble':
        assemble(pick(arg('--ids')), voice)
    else:
        sys.exit(__doc__)


if __name__ == '__main__':
    main()
