r"""Record a tool's spoken lines on this PC with Qwen3-TTS (Apache 2.0), cloning the tool's own Gemini voice.

    S:\AI\tts\.venv\Scripts\python.exe scripts/localvoice.py <tool-id> [--n 40] [--forge]

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

--forge records on the Forge (lab119, RTX 2080) instead, so this PC's card stays free for art (Cory, 2026-10-28):
the lines and the reference go over, a job joins the Forge queue (E:/forge/queue, one GPU job at a time, shared with
challenge work), this script waits for it, brings the clips back and encodes them here. The Forge runs this same
file with --worker, so take picking and the length check are identical. A pilot on game-remix (42 lines) matched the
5080 takes (Whisper word errors 1.9 vs 1.1 percent, same pitch, movement and timbre) at about 5.4 s a line.
If the wait is cut off, `--forge-collect <job>` (the name it printed) picks the clips up later.
"""
import json, os, shutil, subprocess, sys, tempfile, time
from pathlib import Path

import numpy as np
import torch

ROOT = Path(__file__).resolve().parent.parent
PY = shutil.which('python') or 'python'  # the normal Python (lameenc, the Gemini SDK), not this venv
SR = 24000
MODEL = os.environ.get('CURIO_TTS_MODEL', 'Qwen/Qwen3-TTS-12Hz-1.7B-Base')  # the Forge points this at its local copy

FORGE = 'lab119'  # ssh alias (~/.ssh/config)
FDIR = 'E:/forge/curio-voice'  # bin/ (this script), jobs/<name>/ (job.json, ref.wav, out/)
FPY = r'E:\forge\venvs\tts312\Scripts\python.exe'  # mirrors S:\AI\tts (Python 3.12, qwen-tts 0.1.1)
FMODEL = 'E:/forge/hf-cache/hub/models--Qwen--Qwen3-TTS-12Hz-1.7B-Base/snapshots/fd4b254389122332181a7c3db7f27e918eec64e3'


def pcm_of(f):
    return np.frombuffer(f.read_bytes(), dtype=np.int16)


def plausible(text, wav):
    secs = len(wav) / SR
    return len(text) * .03 < secs < len(text) * .11 + 2.5


def pitch(w):
    """Median pitch (Hz) and pitch movement (semitone SD) of one take, or None when too little is voiced."""
    import librosa
    f0, voiced, _ = librosa.pyin(np.asarray(w, dtype=np.float32), fmin=60, fmax=400, sr=SR, frame_length=1024)
    f0 = f0[voiced & ~np.isnan(f0)]
    if len(f0) < 10:
        return None
    return np.median(f0), (12 * np.log2(f0 / np.median(f0))).std()


def liveliest(text, wavs, home):
    """A take with normal life in it, not the most excited one (Cory heard a flat batch, 2026-10-26, and asked that the
    fix stay gentle, 2026-10-27). The first take stays unless it is flat: movement under 3 semitones. Otherwise the
    take whose movement is nearest 4.5, the middle of what this bank's healthy takes measure, among takes that stay
    within 12 percent of the voice's home pitch, so a squeaky or shouted take never wins."""
    takes = [(w, pitch(w)) for w in wavs if plausible(text, np.asarray(w))]
    takes = [(w, p) for w, p in takes if p]
    if not takes:
        return wavs[0]
    if takes[0][0] is wavs[0] and takes[0][1][1] >= 3:
        return wavs[0]
    near = [(w, p) for w, p in takes if not home or abs(p[0] / home - 1) <= .12] or takes
    return min(near, key=lambda t: abs(t[1][1] - 4.5))[0]


def load_model():
    from qwen_tts import Qwen3TTSModel
    # bf16 only from Ampere on: the Forge's RTX 2080 (Turing) runs bf16 on slow kernels (32x once), so fp16 there
    dt = torch.bfloat16 if torch.cuda.get_device_capability(0)[0] >= 8 else torch.float16
    return Qwen3TTSModel.from_pretrained(MODEL, device_map='cuda:0', dtype=dt)


def make(m, prompt, todo, redo, takes, home, save):
    """Clone every line in batches of 8 (the fastest size on both cards); save(text, int16 bytes) after each take.
    Returns the lines whose length still looked off after one retry."""
    flagged = []
    for i in range(0, len(todo), 8):
        batch = todo[i:i + 8]
        wavs, sr = m.generate_voice_clone(text=batch, language=['English'] * len(batch), voice_clone_prompt=prompt)
        assert sr == SR, sr
        for text, w in zip(batch, wavs):
            if text in redo:
                w = liveliest(text, [w, *(m.generate_voice_clone(text=[text], language=['English'], voice_clone_prompt=prompt)[0][0]
                                          for _ in range(takes - 1))], home)
            if not plausible(text, w):  # one retry for a take that rambles or cuts off
                w = m.generate_voice_clone(text=[text], language=['English'], voice_clone_prompt=prompt)[0][0]
                if not plausible(text, w):
                    flagged.append(text)
            save(text, (np.clip(np.asarray(w), -1, 1) * 32767).astype(np.int16).tobytes())
        print(f'  made {min(i + 8, len(todo))} of {len(todo)}', flush=True)
    return flagged


def worker(job):
    """On the Forge (from its queue): record job.json's lines into job/out/. A requeued job keeps what it made."""
    import soundfile as sf
    spec = json.loads((job / 'job.json').read_text(encoding='utf-8'))
    stem = dict(spec['lines'])
    out = job / 'out'
    out.mkdir(exist_ok=True)
    todo = [t for t in stem if not (out / f'{stem[t]}.pcm').exists()]
    ref, sr = sf.read(job / 'ref.wav', dtype='float32')
    m = load_model()
    prompt = m.create_voice_clone_prompt(ref_audio=(ref, sr), ref_text=spec['ref_text'])
    flagged = make(m, prompt, todo, set(spec['redo']), spec['takes'], spec['home'],
                   lambda t, b: (out / f'{stem[t]}.pcm').write_bytes(b))
    (job / 'flagged.json').write_text(json.dumps(flagged, ensure_ascii=False), encoding='utf-8')


def rsh(cmd):
    r = subprocess.run(['ssh', '-o', 'BatchMode=yes', '-o', 'ConnectTimeout=15', FORGE, cmd], capture_output=True, text=True)
    return r.stdout.strip()


def scp(src, dst, cwd):
    # local paths stay relative to cwd: scp reads "C:" as a host name
    subprocess.run(['scp', '-q', '-r', src, dst], cwd=cwd, check=True, stderr=subprocess.DEVNULL)


def forge_submit(tool, todo, redo, takes, home, ref_wav, ref_text, rawf):
    import soundfile as sf
    name = time.strftime('%Y%m%d-%H%M%S') + f'-voice-{tool}'  # the queue runs the oldest name first
    tmp = Path(tempfile.mkdtemp())
    job = tmp / name
    job.mkdir()
    (job / 'job.json').write_text(json.dumps({'tool': tool, 'lines': [[t, rawf(t).stem] for t in todo], 'redo': redo,
                                              'takes': takes, 'home': home, 'ref_text': ref_text}, ensure_ascii=False), encoding='utf-8')
    sf.write(job / 'ref.wav', ref_wav, SR)
    (tmp / 'job.cmd').write_text(f'@echo off\r\nset CURIO_TTS_MODEL={FMODEL}\r\nset HF_HUB_OFFLINE=1\r\n'
                                 f'"{FPY}" {FDIR}/bin/localvoice.py --worker {FDIR}/jobs/{name}\r\n', encoding='ascii')
    shutil.copyfile(__file__, tmp / 'localvoice.py')
    rsh(f'New-Item -ItemType Directory -Force {FDIR}/bin, {FDIR}/jobs | Out-Null')
    scp('localvoice.py', f'{FORGE}:{FDIR}/bin/localvoice.py', tmp)
    scp(name, f'{FORGE}:{FDIR}/jobs/', tmp)
    scp('job.cmd', f'{FORGE}:E:/forge/queue/pending/{name}.cmd', tmp)
    rsh('Start-ScheduledTask -TaskName Forge-Queue')
    shutil.rmtree(tmp, ignore_errors=True)
    print(f'queued on the Forge as {name} ({len(todo)} lines, about {len(todo) * 5.4 / 60:.0f} min once it starts)', flush=True)
    return name


def forge_wait(name, total):
    seen = None
    while True:
        r = rsh(f"(Select-String -Path E:/forge/logs/{name}.log -Pattern '^=== .* EXIT ' -ErrorAction SilentlyContinue | Select-Object -Last 1).Line;"
                f"'made ' + @(Get-ChildItem {FDIR}/jobs/{name}/out -ErrorAction SilentlyContinue).Count;"
                f"'ahead ' + @(Get-ChildItem E:/forge/queue/running, E:/forge/queue/pending -Filter *.cmd | Where-Object Name -lt '{name}.cmd').Count")
        lines = r.splitlines()
        done = next((x for x in lines if ' EXIT ' in x), None)
        if done:
            code = done.split(' EXIT ')[1].split()[0]
            if code != '0':
                sys.exit(f'Forge job {name} failed (exit {code}); its log is E:/forge/logs/{name}.log')
            return
        made = next((x.split()[1] for x in lines if x.startswith('made ')), '0')
        ahead = next((x.split()[1] for x in lines if x.startswith('ahead ')), '0')
        now = f'made {made} of {total}' if made != '0' else f'waiting in the queue ({ahead} jobs ahead)'
        if now != seen:
            print(f'  Forge: {now}', flush=True)
            seen = now
        time.sleep(60)


def forge_collect(name):
    """Bring a finished Forge job's clips into voice/raw/, list them in local.json, and encode."""
    from voice import clip_name
    tmp = Path(tempfile.mkdtemp())
    scp(f'{FORGE}:{FDIR}/jobs/{name}', '.', tmp)
    job = tmp / name
    spec = json.loads((job / 'job.json').read_text(encoding='utf-8'))
    tool = spec['tool']
    folder = ROOT / 'tools' / tool / 'voice'
    lf = folder / 'local.json'
    local = json.loads(lf.read_text(encoding='utf-8')) if lf.exists() else {}
    got = 0
    for text, stem in spec['lines']:
        f = job / 'out' / f'{stem}.pcm'
        if f.exists():
            shutil.copyfile(f, folder / 'raw' / f'{stem}.pcm')
            (folder / clip_name(text)).unlink(missing_ok=True)  # a redone line encodes again
            local[text] = 'qwen3-tts-1.7b-base clone'
            got += 1
    lf.write_text(json.dumps(local, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    flagged = json.loads((job / 'flagged.json').read_text(encoding='utf-8')) if (job / 'flagged.json').exists() else []
    shutil.rmtree(tmp, ignore_errors=True)
    print(f'{tool}: {got} of {len(spec["lines"])} clips back from the Forge', flush=True)
    subprocess.run([PY, str(ROOT / 'scripts' / 'voice.py'), tool, '--no-record'], check=True)  # encode the new MP3s only
    for t in flagged:
        print(f'  CHECK by ear (length looked off): {t}')


def main():
    if '--worker' in sys.argv:
        return worker(Path(sys.argv[sys.argv.index('--worker') + 1]))
    sys.path.insert(0, str(ROOT / 'scripts'))
    if '--forge-collect' in sys.argv:
        return forge_collect(sys.argv[sys.argv.index('--forge-collect') + 1])
    from voice import clip_name
    tool = sys.argv[1]
    cap = int(sys.argv[sys.argv.index('--n') + 1]) if '--n' in sys.argv else 10 ** 6
    folder = ROOT / 'tools' / tool / 'voice'
    spec = json.loads((folder / 'lines.json').read_text(encoding='utf-8'))
    raw = folder / 'raw'
    raw.mkdir(exist_ok=True)
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
    # --redo 1,4,9 --takes 5: re-record those lines (lines.json order); a flat first take is swapped for a normal one (liveliest)
    redo = [lines[int(i)] for i in sys.argv[sys.argv.index('--redo') + 1].split(',')] if '--redo' in sys.argv else []
    takes = int(sys.argv[sys.argv.index('--takes') + 1]) if '--takes' in sys.argv else 5
    forge = '--forge' in sys.argv
    if not forge:  # with --forge the old clips stay until the new ones come back
        for t in redo:
            rawf(t).unlink(missing_ok=True)
            (folder / clip_name(t)).unlink(missing_ok=True)
    todo = [t for t in lines if t in redo or not rawf(t).exists()][:cap]
    print(f'{tool}: {len(todo)} lines to make, copying the voice of: {ref[:60]}', flush=True)
    if not todo:
        return
    ref_wav = ref_audio[0] if ref_audio else pcm_of(rawf(ref)).astype(np.float32) / 32768
    # the voice's home pitch, from its reference clip: re-takes may not drift far from it
    home = (pitch(ref_wav) or (None,))[0] if redo else None
    if forge:
        name = forge_submit(tool, todo, redo, takes, home and float(home), ref_wav, ref, rawf)
        forge_wait(name, len(todo))
        return forge_collect(name)
    m = load_model()
    prompt = m.create_voice_clone_prompt(ref_audio=(ref_wav, SR), ref_text=ref)

    def save(text, b):
        rawf(text).write_bytes(b)
        local[text] = 'qwen3-tts-1.7b-base clone'
        (folder / 'local.json').write_text(json.dumps(local, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    flagged = make(m, prompt, todo, redo, takes, home, save)
    subprocess.run([PY, str(ROOT / 'scripts' / 'voice.py'), tool, '--no-record'], check=True)  # encode the new MP3s only
    for t in flagged:
        print(f'  CHECK by ear (length looked off): {t}')


if __name__ == '__main__':
    main()
