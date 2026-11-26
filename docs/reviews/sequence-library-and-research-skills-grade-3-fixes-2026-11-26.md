# Fixes: scope and sequence of library-and-research-skills-grade-3, 2026-11-26

Fix pass per build/scope-writes/AFTERCORE-FIX.md on the expert read
docs/reviews/sequence-library-and-research-skills-grade-3-2026-11-26.md. The Codex read waits for Codex's usage reset
(after 2026-11-30). The other library reads (kindergarten, grade 1, grade 4, grade 5) have no "Across" section; their
findings that touch grade 3 were applied as band items.

Counts: applied 14 (expert 7 findings with every "Settled by the expert" row, band 3, lead calls 3, own 1); not
applied 0. 11 defect rows logged as fixed.

## Applied

- **Expert 1** (scope-and-sequence.md, Shorter path): 30-minute session splits for days 16, 17, 26 (5, 4, 12, 5)
  and 30 (10, 11, 5); days 11 and 29 hand out the catalog page before the session. 10 days short = about 2 lost
  sessions: fold-in 1 rebuilt (day 2 into day 3 at 28 minutes, day 1 unchanged), fold-in 2 is day 12 into day 14,
  and the day 9 fold-in holds only for a third lost session (turn routine practiced live on day 10, day 8's exit
  ticket one scenario card).
- **Expert 2** (days.csv days 11, 19, 28, 29; .md units 2, 3, 4 and check 2; frame unit evidence cells and check 2
  cell): day 11 two places on "where to look", a map item, the four cards' parts named (about 26 minutes); day 19
  choose two sources and say why, one "why this box" line (about 27); day 28 the copied-sentence item (about 22);
  day 29 second try in another kind, a second-source item, a "why this box" line (about 27, one label drops if long).
- **Expert 3** (days.csv days 15 to 17; .md unit 3 arc and retrieval; frame unit 3 Days list, retrieval line and
  seam row): checkable statement and second-source think-aloud moved to day 16; day 17 budgeted at 27 minutes with
  the notes as exit evidence; g2-two-books-differ retrieved on day 16. Day 16 now also carries
  g3-source-kinds-and-makers and ~AASL.IV.B.3.
- **Expert 4** (days.csv day 23; .md unit 4; frame unit 4 retrieval line): waiting teams get a two-part card,
  retrieval then finishing day 22's notes and starring the fact to report.
- **Expert 5** (days.csv days 1, 3, 6, 9, 10, 11, 15, 17, 19, 22; .md units 1 to 4; frame units 1 to 4): password
  pair by length (four unrelated words versus a name or short word, no symbol swap); spider pictures webs and silk
  only; dependence as shelter, plants and clean water; far side gets sunlight; weather service indoor rule (browser
  check); one-answer labels on clear-cut kinds only, the diagram and captioned photo discussed, not marked.
- **Expert 6** (days.csv day 21; .md unit 4; frame unit 4 Days list): the team meeting opens with SEL's four talk
  turn steps in SEL's words.
- **Expert 7** (days.csv days 14, 19): unit 2's groups by name from day 11's record sheet; day 19's pond set shares no
  source with unit 4's.
- **Band, grade 4 read 8a and 8b** (.md Sources not loaded; days.csv day 6): the band file is on disk and was read by
  the frame, its store entry waits on L149; no day leans on the digital-citizenship presentation (sensitivity-read
  source only, browser check).
- **Band, kindergarten read 3** (already met by expert 6; same turn card rule).
- **Band, grade 4 read 9 / grade 5** (unit 4 codes off the checks): kept as written, see lead call 10.
- **Lead call 1** (frame Placement paragraph and For the lead item 3): reworded as settled by CALENDAR.md rule 1;
  scope For the lead item 1 dropped.
- **Lead calls 4 and 7** (frame unit 1, 2 and 4 Days lists): the look-it-up sort, the library map, the turn routine
  and the password pair now sit on the show-me days the scope models them on; unit 4's one self-check is on the
  gallery day and the revision day ends with the look-back line. Scope For the lead items 2 and 4 dropped.
- **Lead call 10** (.md Owned codes paragraph): unit 4's codes stay off the checks with the reason named; scope For
  the lead item 3 dropped. The .md For the lead section now reads "None" with the reasons.
- **Own** (.md Shorter path): the new 27-minute sittings on days 19 and 29 overran the 30-minute session's 26
  working minutes; each drops one source label there (about 25).

## Not applied

None. Lead call 2 (no source-map.csv) and lead call 14 (band readiness) have nothing to act on here; lead call 8:
no begun day has empty codes (day 30, a respond day, keeps its empty codes cell, as it reteaches and claims nothing).

## Settled (for DIGEST)

| Judgment | Reason |
|---|---|
| An invented password pair is judged by length: four unrelated words versus a name or short word, never a symbol swap | Current federal guidance puts length first |
| One-answer primary or secondary items use clear-cut kinds only; a diagram or captioned photo is discussed, not marked | Either answer is defensible |
| An observed team day gives waiting teams real work (finish notes, star the fact to report) beyond the retrieval | One adult must be able to observe |
| A sitting that grows past 26 minutes names what drops in the 30-minute session | Shorter path must hold in minutes |
| A ~VI.B.2 item asks "respect their rights" as well as naming the maker | Full code asked |

## For the structure pass

- docs/agents/lenses/library.md: "catalogues" to "catalogs", "licences" to "licenses", "judgement" to "judgment"
  (US spelling; lead call 13), if not already applied from the grade 1 pass.
- data/plans/calendar.csv: no change (no week moved; checks stay in weeks 13 and 29).

## For Cory

None.

## Gates

- `python -X utf8 scripts/sequence.py check library-and-research-skills-grade-3`: 0 failures; notes "standard None
  is on no day" for unit 3 (lead call 12, left).
- `python -X utf8 scripts/frame.py check library-and-research-skills-grade-3`: 0 failures (4 units, 30 days).
- No unit, day count, owned row or week changed, so the stagger is as before (library is a special, outside rule 1).
