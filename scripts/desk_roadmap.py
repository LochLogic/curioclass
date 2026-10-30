r"""Roadmap tab for the Review Desk: docs/ROADMAP.md as HTML.

    python scripts/desk_roadmap.py <out.json>     write the document (then ArtifactData set stats/roadmap)

Run it whenever docs/ROADMAP.md changes, so the tab matches the file.
"""
import json, sys
from datetime import datetime, timezone
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent.parent
text = (ROOT / 'docs/ROADMAP.md').read_text(encoding='utf-8')
doc = {'html': markdown.markdown(text, extensions=['tables', 'sane_lists']), 'at': datetime.now(timezone.utc).isoformat(timespec='seconds')}
Path(sys.argv[1]).write_text(json.dumps(doc, ensure_ascii=False), encoding='utf-8')
print(len(doc['html']), 'characters')
