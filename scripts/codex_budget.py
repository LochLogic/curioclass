"""Percent of the weekly Codex budget left, read from Codex's own session logs. No tokens.

    python -X utf8 scripts/codex_budget.py

Moved here from codex_runner.py (retired 2026-11-25, docs/CONSOLIDATION-PLAN.md step 3.2) so codex_scopes.py can keep
its budget stop.
"""
from pathlib import Path

SESSIONS = Path.home() / '.codex' / 'sessions'


def codex_remaining():
    """Percent of the weekly Codex budget left, from the newest "rate_limits" any Codex session logged (its last 4 MB;
    rollouts reach 140 MB). None when nothing recent says. Every session, the scripts' and the app's, shares one budget."""
    days = sorted((d for d in SESSIONS.glob('*/*/*') if d.is_dir()), reverse=True)[:3]
    files = sorted((f for d in days for f in d.glob('rollout-*.jsonl')), key=lambda f: f.stat().st_mtime, reverse=True)
    for f in files[:6]:
        try:
            with open(f, 'rb') as h:
                h.seek(max(0, f.stat().st_size - 4_000_000))
                tail = h.read().decode('utf-8', 'replace')
        except OSError:
            continue
        i = tail.rfind('"primary":{"used_percent":')
        if i >= 0:
            num = tail[i + 26:i + 40].split(',')[0].split('}')[0]
            try:
                return round(100 - float(num), 1)
            except ValueError:
                continue
    return None


if __name__ == '__main__':
    print(codex_remaining())
