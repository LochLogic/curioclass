# Overlap and Gap Audit

Cory's step 2 of the 2026-10-27 plan: after every catalog tool has at least an idea card, review the whole catalog
(live, specced and idea tools, 762 in all) for overlap between tools and for standards no tool teaches well. It reruns
the first overlap pass (docs/agents/overlap/method.md) on the new concept lines and adds the gap work the idea pass
raised. Output goes in docs/agents/audit/.

## Phase 1: tags and gaps (four agents at once)

**Tag agents (three).** The idea pass changed 379 concept lines and some formats, so the tags in
docs/agents/overlap/tags.csv are stale for those tools. Each tag agent takes some of the group files in
docs/agents/ideas/:

| Part | Groups |
|---|---|
| A | ela-1, ela-2, ela-3, lang |
| B | math-1, math-2, sci-1, sci-2 |
| C | ss-1, ss-2, ss-3, arts, cs-mix |

1. Read method.md (Tagging, the clash rule) and the existing tags.csv rows to match the house style: skill keys,
   the fixed list of 31 actions, and the coarse setting groups.
2. For every id in your groups, read tools/<id>/idea.md. Some ids were renamed after the group files were written:
   map an old id through docs/agents/overlap/renamed.json.
3. Write a fresh tag row in docs/agents/audit/tags-<part>.csv, with the same header as tags.csv. Copy band, subject,
   live, format and family from data/tools-concepts.csv. Reuse an existing skill key wherever a teacher would call the
   skill the same; a new key only for a new skill.
4. Never edit tags.csv itself.

**Gap agent (one).** Read docs/agents/IDEA-PASS-LOG.md and the MOVE lines in the idea cards (grep `MOVE`). Then run
`PYTHONIOENCODING=utf-8 python scripts/overlap/coverage.py` and `scripts/overlap/standards.py`. Write
docs/agents/audit/gaps.md with these sections:

- **Code moves:** one row per MOVE, as source tool and module, code, then target tool and module or "new tool". Check
  that the target really teaches the code (read its idea.md or spec.md). Check that the source keeps enough to teach,
  so a tool left with nothing gets flagged.
- **New tools:** one proposed catalog line per new tool the moves need, in the data/concepts/*.txt format
  (`module_id|title|format|family|concept`), plus a module line (id, subject, grade, title, standards) in the style of
  data/modules/*.txt. Merge duplicates. For example, two moves that each want a grades 6-8 spelling tool become one.
- **Uncovered codes:** the 41 CCSS-ELA codes with no tool, and any other code in the "all" column below full. For each,
  give the existing tool that should take it and how, or a new tool line.
- **Band holes:** codes that only a K-12 or wide-span tool covers, where that tool can't really teach the code at every
  grade (rule gf-04). Use the idea pass's K-12 span flags.
- **Catalog fixes:** module titles that no longer match their tool (skateboard-fund-chances / "Bike Fund Chances",
  behind-the-podcast / "Behind the Documentary"), one-tool families (silk-road), and definitions that must agree
  across tools (trapezoids: inclusive, in shape-family-tree and shape-courtroom).

The gap agent never edits data/. The orchestrator applies the changes.

## Phase 2: clashes (after phase 1)

The orchestrator merges the tag files into tags.csv and runs `python scripts/overlap/rule.py`. One or two judge agents
then group the hits into clusters and judge each by hand, the way clusters.md did. They also take the overlap risks the
idea cards named (in IDEA-PASS-LOG.md). Their output is docs/agents/audit/clashes.md, with these fixes:

- **Live tools never move.** A planned tool changes instead.
- **Reshape** (a new concept line in the same module) is the default fix.
- **Keep with a note** is used when the tools really differ in what the student does.

Every fix is re-checked with the rule.

## Rules

- Follow docs/agents/decisions/BASELINE.md. Rule 1 means a tool is never merged only to save work.
- Write "Curio Class", never "Curio" alone. No em dashes. Use they/them for Cory.
- Commit nothing. Never touch docs/BUILD-BOARD.md, closet/, game-remix or code-tracer.
- Report in under 25 lines. Questions go to Cory only when BASELINE can't settle them and they matter.
