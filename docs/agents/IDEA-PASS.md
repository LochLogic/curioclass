# Idea pass

Cory's step 1 of the 2026-10-27 plan: firm up every catalog tool that is still only a catalog line (474 tools), short of
a full spec. The idea pass sits between the catalog line and SPEC.md. The catalog audit (overlap and gaps) reads its
cards next, and full specs come in later waves.

Groups are in `docs/agents/ideas/<group>.txt`, one tool id per line, ordered by grade: ss-1 to ss-3, ela-1 to ela-3,
math-1 and math-2, sci-1 and sci-2, arts, cs-mix (computer science, CTE, library, SEL, health and PE) and lang (world
languages and ELD). Run one agent per group, at most three at once.

## For each tool

1. Run `PYTHONIOENCODING=utf-8 python scripts/neighbors.py <tool-id>` to see the concept, its module and standards,
   and its neighbors. For any neighbor that already has a `tools/<id>/idea.md`, read its "One idea" line too.
2. Write `tools/<id>/idea.md` from the template below, and nothing else. Make it at most about 30 lines, plain and
   specific.
3. Settle choices with `docs/agents/decisions/BASELINE.md`. The main rules here:
   - Quality over saved work.
   - Every module code is taught well. If the tool can't teach a code well, say where it should go instead.
   - Better art by default.
   - Every tool works for one student alone, with no teacher present.
   - Plain facts, told with the human side.

## Template

```
# <Title> (idea card)

- Module: <module_id>, grade <g>. Codes: <codes from the module>
- Format / family: <format> / <family or none>. Fit: good | change to <format>, because ...
- One idea: <one sentence: what the student does, and what it shows them>
- How it plays (solo student by default):
  - First screen: ...
  - Core loop: ...
  - The aha or the end state: ...
  - Class mode or extras (optional): ...
- Standards, one line per code: <code>: <the activity that teaches it>. If it can't be taught well here, write
  "MOVE <code>: <where it should go, or 'new tool: idea'>".
- Not like: <the 1-3 closest neighbors and what makes this one different>
- Art: <generated scenes | people (illustrated) | public domain (Met or AIC object id, checked) | drawn in code>, and why
- Proposed title: keep | <new title> (when it clashes with a product, a neighbor or a known game name)
- Proposed concept line: keep | <new catalog line, at most 40 words, in the style of data/concepts/*.txt>
- Flags: <none | sensitive (what) | needs a data source (which) | overlap risk (with what) | too big | too thin>
```

Write a new concept line whenever the old one is vague, lists more than one idea, overlaps a neighbor, or would not
work for a student alone. The orchestrator applies the proposed titles and concept lines afterwards, through
`scripts/rename_tools.py` and the concept files. Idea agents never edit data/ themselves.

## Rules

- Write "Curio Class", never "Curio" alone. No em dashes anywhere.
- Use only honest clients for any lookup. Keep unconfirmed facts off the card, or flag them.
- Write only tools/<id>/idea.md for the tools in your group. Commit nothing. Never touch docs/BUILD-BOARD.md, closet/,
  game-remix or code-tracer.
- Report in under 30 lines:
  - how many cards you wrote;
  - the counts of "proposed concept line" and "proposed title" changes;
  - every MOVE line;
  - the flags that matter;
  - questions only when BASELINE can't settle them and they really matter, each with full context.
