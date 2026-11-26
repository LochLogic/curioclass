# Frame fixes: English Language Development, grades K to 2, 2026-11-25

The one fix pass of COURSE-RUN stage 3 for the ELD after-core band pilot. Reads fixed:
docs/reviews/frame-english-language-development-grades-k-to-2-2026-11-25.md (expert, E1 to E13) and
docs/reviews/frame-english-language-development-grades-k-to-2-codex-2026-11-25.md (second model, C1 to C7).
Files changed: the frame, data/progressions/eld.csv (11 rows, CRLF kept), docs/courses/eld/STANDARD.md,
docs/courses/eld/APPROACH.md; frames.csv, calendar.csv and CALENDAR.md through `frame.py sync`.

## Gates

| Gate | Result |
|---|---|
| `python -X utf8 scripts/frame.py sync` | frames.csv 66 courses; calendar.csv 962 rows |
| `python -X utf8 scripts/frame.py check english-language-development-grades-k-to-2` | 0 failures (K 154, 1 154, 2 154 unit days; 480 days) |
| `python -X utf8 scripts/progression.py check eld` | 162 rows, 0 failures |
| `python -X utf8 scripts/stale.py check` | 70 files, 0 failures |

No unit, day count or check week moved.

## Findings

20 findings: 20 applied (E4 by its second option), 0 rejected. Where the reads disagreed, see the notes.

| Read | # | Applied or rejected | What changed, or why not |
|---|---|---|---|
| Expert | E1 | Applied | SI in every unit: course-brief line; units 3, 6, 11, 12, 13, 16, 17, 18 each name one SI use as review (id, owner, talk move, look-for). Picks settled with C3 (see note 1). |
| Expert | E2 | Applied | Unit 12 retargeted to science grade 1 unit 7's content (signals and responses, 1-LS1-2); likeness retrieved from unit 3 (s1-like-parents, days 22 to 27). g1-sc-inform: cross_subject adds `science:s1-like-parents (host investigation, earlier)`; task, frames, forms, words rewritten. Cross-subject table gains the s1-like-parents row; seam and model lines updated. |
| Expert | E3 | Applied | Unit 8 "The Bear and the Two Travelers", unit 20 "The Fox and the Goat" (Townsend 1867, retold); "checked unused in docs/ and data/, including section plans and items.csv, on 2026-11-25" (re-searched: only the expert read and the library's raw Gutenberg texts hold them). |
| Expert | E4 | Applied (option 2) | Days bullet now says host windows first, then load, and names units 10, 14 and 17 as tight with what they leave to the respond day. Rebalancing (option 1) would move check days, which the brief keeps fixed this pass. |
| Expert | E5 | Applied | Weeks paragraph states that MA K (unit 6) and MA 1 (unit 13) are checked by end-of-unit assessment only, the record going on; grade 2 narrate goes to grade 3. Pattern note added. |
| Expert | E6 | Applied | Unit 19 note: alternative pair is Curio Class's own (two class reports of one school event); host flood pair not used; social studies unit 6 family interviews named. Unit 19 added to the "just after the host" list (now in Language through content). g2-ss-argue's teacher note fixed the same way. Cross-subject ss2-two-accounts row says alongside then just after. |
| Expert | E7 | Applied | Weeks kept (task rule); clash listed in For the lead item 5 and below; "latest free week" is no longer offered as a copy rule. |
| Expert | E8 | Applied | g2-ma-argue notes: comparisons only when the odd and even unit comes later; odd and even return in grade 3. |
| Expert | E9 | Applied | Weeks paragraph: kindergarten mid-year heard parts and drawing day 86, every talk task day 87. |
| Expert | E10 | Applied | Old item 9 (frame.py) removed; APPROACH opening and STANDARD (opening, owed table, Grain, section 3 heading, section 6) fixed in place; ADOPTION-BAR row and lens line go to the lead with replacement text (not files this pass may edit). |
| Expert | E11 | Applied | "units 1, 2 and 19". |
| Expert | E12 | Applied | Unit 10 regla/rule and unit 14 escuela/school now "share a root but look different"; unit 14 example "comunidad and community" (insecto dropped). Rows g1-si-explain (regla) and g3-ss-explain (gobierno) fixed. No "fuerza" exists in eld.csv; fuente/source and fiable/reliable are true non-cognates and stay. |
| Expert | E13 | Applied | Base text "EL Education K-5 Language Arts, 2017 edition, CC BY 4.0" (2025 edition CC BY-NC, not used); NCTSN guide for educators named with its address; federal toolkit address added; unit 11 "a US Geological Survey or National Park Service image marked public domain, credited". |
| Codex | C1 | Applied | Checked at source (WIDA 2020 framework, printed pages 52, 72, 74): units 4, 9, 10 now teach every part of their owned ids in our words (the question tested or problem, comparing two solutions, picking supporting observations; topic, a pictured source, fact or opinion, evidence linked to the claim); end-of-unit tasks match. Rows k-sc-explain, g1-sc-explain, g1-ss-argue notes extended. |
| Codex | C2 | Applied | Same as E1 (note 1). |
| Codex | C3 | Applied | Recurrence map in "Key language uses as the spine": every use returns in a later unit of its year, through its row or SI review, with what gets harder; grade 2 narrate named as the one single-unit use, carried weekly by the routine's retell step and checked in grade 3. |
| Codex | C4 | Applied | Unit 2: ELA weather stories start day 49, so days 31 to 48 use class events and ELA unit 1's toy story; mid-unit about day 46. Unit 12: as E2. Unit 16: SS grade 2 unit 3 opens on school day 45, so ELD days 39 to 44 bridge (unit row and cross-subject row). |
| Codex | C5 | Applied | Unit 9 end-of-unit wording: picture supports and word bank kept, cloze and sentence frames removed per the withdrawal rule, accommodations kept. |
| Codex | C6 | Applied | As E10; old item 1's "four band frames are written" claim gone (For the lead item 1 is now current). |
| Codex | C7 | Applied | Same as E11. |

Notes where the reads disagreed:
1. SI picks (E1 against C2). Settled by bar item 13 and C3: each review use is chosen so that a key language use
   returns within the year. Unit 3 Narrate (not the expert's Inform, which the unit already owns), unit 6 Argue
   (both), unit 11 Narrate (codex's recurrence pick over its own Inform pick), unit 12 Explain, unit 13 Argue, unit 16
   Inform (codex), units 17 and 18 Argue (expert; unit 17 already explains twice). Kindergarten explain begins with
   one framed "because" in unit 3, so unit 4 is its return.
2. E4's two options: the second, because the first moves check days.

## Pattern notes for the other ELD frames

- SI in every unit: the unit's own SI row, or one SI use as review, chosen so each key language use returns inside
  the year; write the recurrence map in the spine bullet.
- Check every owned row against the framework's own lists for its id (printed pages, not the code); grades 3 to 5,
  6 to 8 and 9 to 12 should do this before the frame read.
- Check each host against the host row's standard and the host frame's day ranges inside the unit (where its parts
  start), and convert host course days to school days with calendar.csv: social studies and science K to 5 do not
  meet daily.
- Picks for unseen texts: search docs/ and data/ (section plans and items.csv too), not frames only.
- Days: host windows first, tight units named. Say which owned rows no course-level check samples.
- Cognates: "share a root but look different" for hidden cognates; check etymology before "not a cognate".
- Check weeks: off core weeks; do not copy "latest free week" until the lead's after-core calendar pass.

## Left for the lead

1. After-core check clashes (kept, CALENDAR.md rule 1 pass): K week 18 arts and PE; K week 28 library and PE;
   grade 1 week 18 arts and PE; grade 1 week 28 PE; grade 2 week 17 arts and PE; grade 2 week 27 health and PE.
2. docs/agents/lenses/eld.md and docs/ADOPTION-BAR-SUBJECTS.md ELD row: replacement text in the frame's For the
   lead items 2 and 3.
3. frame-write.md item 5: "For ELD, head the C3 column Host unit and key language uses" (frame item 4).

## For Cory

- Newcomer strand delivery (people and time): added period where the school gives one, else a side table inside
  the period; who teaches it and how a newcomer meets the missed unit language need your call before the strand is
  written (frame For the lead item 6).
