"""Before and after gates for each consolidation step (docs/CONSOLIDATION-PLAN.md, ground rule 3).

Since 4.G this is `scripts/gate.py --all --site` with a saved run; the gate list and the compare live in gate.py.

    python -X utf8 scripts/consolidation_gates.py run <step> [<glob> ...]   gate.py --all --site --save <step>
    python -X utf8 scripts/consolidation_gates.py compare <before> <after>  gate.py compare <before> <after>
    python -X utf8 scripts/consolidation_gates.py list                      gate.py list --all

Raw output goes to build/gates/<step>/<gate>.txt (ignored); summary.csv and, for compare, compare-<before>.txt go to
docs/reviews/consolidation/<step>/ and are the only files committed. Older steps kept their raw files in
docs/reviews/consolidation/<step>/, and compare reads them there when build/gates has none. board.py and
course_status.py rewrite docs/BUILD-BOARD.md and docs/COURSES-STATUS.md; commit or restore those before the step's
own commit.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import gate  # noqa: E402


def main(a):
    if len(a) >= 2 and a[0] == 'run':
        args = ['--all', '--site', '--save', a[1]] + (['--only', ','.join(a[2:])] if a[2:] else [])
        gate.main(args)
        return 0
    if len(a) == 3 and a[0] == 'compare':
        return gate.main(a)
    if a == ['list']:
        return gate.main(['list', '--all', '--site'])
    raise SystemExit(__doc__)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
