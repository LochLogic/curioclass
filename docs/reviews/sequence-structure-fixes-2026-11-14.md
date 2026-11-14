# Structure pass after the social studies scope and sequence fixes, 2026-11-14

PRODUCTION-PATH step 3. This pass applied every "For the structure pass" item in the five fix reports
(sequence-k-2-, sequence-3-5-, sequence-6-8-, sequence-9-11- and sequence-12-fixes-2026-11-14.md) and the lead's four
items. No unit, day count or check week moved. The five "Settled" tables are in docs/reviews/DIGEST.md, with a short
table for the choices made here.

## Where reports conflicted, and what was decided

1. **Rule 2's readiness wording** (3-5 item 7, 6-8 item 15, the lead's item 3). The lead's words were used in
   sequence-write.md and frame-write.md lesson 16. They cover both reports' points: "last used two or more grades
   back", and "or earlier the same year".
2. **STANDARD.md's literacy line** (6-8 item 21, 9-11 item 21, 12 item 31). The 9-11 version was used, with RST
   added: it says where the codes are and how they are used (listed as also met, placed per course). The 12 version
   only deleted the line.
3. **MA.6.T2.3's date** (6-8 item 1 proposed 2.5 million). The framework PDF (printed page 86) says c. 2.6 million,
   so 2.6 was used. Day 6 of grade 6 and the ss6-timeline-deep-time row said 2.5 and now say 2.6.
4. **MA.WHI.T3.7** (9-11 item 2 proposed "within the Church and with kings"). The framework (page 144) names only the
   struggles within the church, so the own-word line says that. The progression row (9-11 item 6) keeps "and with
   kings", because it describes the investiture struggle the unit teaches.
5. **CALENDAR.md grade 8 science** (6-8 item 20 left the choice to the lead). The target is now week 15, as the data
   has it. Week 15 breaks no stagger rule, and moving the science check would reopen a finished frame.

## Items applied

**data/progressions/social-studies.csv** (notes column unless said; 85 rows changed; progression gate 0 failures)
- K-2 items 2 to 7: ssk-work, ss1-leaders (Dolores Huerta in, Cesar Chavez out), ss1-community-problems,
  ss1-voting, ss2-people-environment, ss2-resources-industries.
- 3-5 items 1 to 4: ss5-slavery-colonies, ss5-independence-war, ss5-constitution and ss5-informed-action now open
  with a readiness check.
- 6-8 items 4 to 14: ss6-phoenician-trade, ss7-roman-republic, ss7-buddhism-empires, ss7-athenian-democracy,
  ss8-haudenosaunee-influence, ss8-declaration, ss8-amendments-civil-war, ss8-civil-rights-laws,
  ss8-constitution-text, ss8-court-research and ss8-civic-action, as written.
- 9-11 items 5 to 17: wh1-graphic-displays, wh1-european-kingdoms, wh1-iberia-1492, wh1-historical-argument; six
  wh1 rows' grade 6 and 7 handoffs became readiness checks (wh1-silk-roads-mongols' "The retrieval may use" became
  "The readiness check may use"); the us1 rows' grade 5 and 8 handoff clauses became readiness checks (World History
  I clauses, us1-native-west and us1-civil-rights-1900s stay retrieval); us1-revolution-war, us1-news-reading,
  us1-early-republic, us1-slavery-economy, us1-reform-movements and us1-progressivism, as written.
- 9-11 item 10: wh2-social-movements assumes ss5-civil-rights-movements and ss8-civil-rights-laws. Two edits were
  added so the gate passes: both rows now hand on to it (hands_on), and its notes name the handoff (a readiness check
  on World History II day 108).
- 12 items 1 to 28: every Economics, Government and US History II row, as written.
- ss6-timeline-deep-time: 2.5 changed to 2.6 million years (conflict 3).
- data/progressions/parts/ss-k2.csv (the earlier draft part): ss1-leaders changed to match, so the old part cannot
  bring Chavez back.

**data/standards/ma-hss-2018.txt**
- MA.2.T2.4 (K-2 item 8). MA.6.T2.3 (2.6 million), MA.6.T4b.1 and MA.8.T2.1 (6-8 items 1 to 3), each checked
  against the framework PDF. MA.USI.T3.3, MA.USI.T4.2e, MA.WHI.T3.7 and MA.WHI.T5.1 (9-11 items 1 to 4), also
  checked against the PDF. A dated header note lists the widened codes and the PDF pages.
- The header's literacy note now says RH and WHST are loaded in ccss-literacy-6-12.txt.

**Other files**
- data/plans/later.csv L8 (K-2 item 9, 9-11 item 20, 12 item 32): marks the topics as named in all six courses and
  the fifteen topic pages as added. L8 stays open for the pages' worksheets, and its title says so.
- data/modules.csv (9-11 item 19, 12 item 32): fifteen topic rows added. World History I has ten (How Societies Meet
  to Reason, Rights and Rulers). World History II has two (Genocide and Terror Since 1945, Global Problems Research).
  US History II has three (The Economic Toolkit, Presidents and the War in Vietnam, Rights Movements Since the 1960s).
  Each row has C3 codes that exist in c3-indicators.txt and source `added.txt`.
- docs/courses/social-studies/STANDARD.md (6-8 item 21, 9-11 item 21, 12 item 31): literacy status (conflict 2).
- docs/ADOPTION-BAR-SUBJECTS.md:
  - Literacy status (6-8 item 22, 9-11 item 22).
  - C4 evidence and fail cells (3-5 item 6): "readiness check or opening retrieval task".
  - C8 (K-2 item 10): where a unit assumes only rows from the year before, or from earlier the same year, the
    opening retrieval task's teacher notes are the before-teaching evidence.
- docs/agents/lenses/social-studies.md lines 46 and 91 (9-11 item 23): "a qualified person" became the sensitivity
  agent's read, per FOUNDATION section 7 item 3 as changed 2026-11-14. The science lens line 86 has the same old
  wording. It is outside this pass and was left alone.
- docs/courses/english-language-arts-grade-12/frame.md (12 items 29 and 30, with the optional clause): changed the
  unit 8 cut order and the e12-research lean row.
- docs/courses/CALENDAR.md line 57 (6-8 item 20): grade 8 science target week 15 (conflict 5).
- docs/courses/social-studies/grade-3-outline.md line 95 (3-5 item 5): Penobscot, with the reason and its source.
- docs/APPROACH-SOURCES.md (12 item 33, and the 3-5 report's "For the source list"): a new section, "Social studies
  scope and sequence reads, 2026-11-14".
- docs/reviews/DIGEST.md (6-8 item 23, 12 item 34): the five Settled tables, plus this pass's own table.
- `frame.py sync` (K-2 item 1, 6-8 item 19, 9-11 item 18) regenerated calendar.csv and the CALENDAR.md table.
  frames.csv was unchanged. The sync also picked up frame changes the fix passes had made but not synced: the grade 2
  unit 1 question, World History I units 6 and 7, and the US History II check 2 label.
- 12 item 35 and 3-5 item 8 (ELA 4's SL.4.4 line) needed no change. 9-11 item 24 (ELA 9 to 11 frames) also needed
  no change.

## The lead's items

1. **scripts/sequence.py.** New `md_fails` check. It fails a scope-and-sequence.md that is empty, has no
   "# Scope and sequence" title, has no "## Unit N" sections, or is missing a section for any unit. It was tested on
   an empty file, a file with no units and a file missing a unit. A missing "Shorter path" section is reported as a
   note, not a failure.
2. **scripts/frame.py.** New `days_calendar`. When data/plans/<course>/days.csv exists, that course's calendar.csv
   rows come from it:
   - each day sits on its school_day where that column is filled, and on the even spread otherwise;
   - days run in school-day order, and a unit or check run is cut wherever another day falls between.
   Held days now show: kindergarten unit 5's on-the-day lessons (days 41, 42 and 43 in weeks 7, 12 and 19), grade 6
   day 55 (unit 3's look-back, week 11) and grade 7 day 120 (unit 8's look-back, week 24). If a course's check days
   do not match its frame's checks table, it falls back to the frame. `citations` now takes a unit's whole span
   across its runs. CALENDAR.md says the code matches.
3. **Briefs.**
   - sequence-write.md rule 2 and frame-write.md lesson 16 have the lead's readiness words, word for word.
   - sequence-write.md has three new rules: each part of each code asked (rule 2); a check right after an
     end-of-unit assessment draws from earlier units (rule 3); and rule 10, "A shorter path". The files list and
     the gate paragraph changed with them, and the old rule 10 is now 11.
   - sequence-read.md has the matching checks.
   - frame-write.md lesson 5 now says "readiness check or retrieval task".
   - plan.md and plan-read.md now state the readiness rule.
   - docs/courses/UNIT-PLAN.md field 4 and its template line contradicted the rule ("given before the unit opens,
     in the last ten minutes of the previous unit"). They now follow rule 2, so a unit that needs only retrieval
     fills the field with its retrieval tasks. Grade 4 math keeps Cory's 2026-11-11 pre-unit timing until its
     scope and sequence is rewritten, and the opening note and rule 11 say so.
   - GLOSSARY's "readiness check" row said "given before a unit opens" and now matches rule 2.
4. **Dolores Huerta.** The grade 1 days.csv, frame and scope and sequence already named Huerta. The progression row
   (and its draft part) was the one place left that named Chavez as the grade 1 good-leader case. Chavez still
   appears in MA.USII.T4.8e (the standard's own words), the grade 1 scope and sequence's note on why he was replaced,
   the tools-for-change spec (the grape boycott, alongside Huerta) and an old SEL worksheet list. None of those uses
   him as the grade 1 case, so they were left.

## For the lead (not Cory's)

- **Shorter path.** Grades K to 5 have no "## Shorter path" section, and `sequence.py` notes it.
  - K and 2 have a shorter-period route.
  - 3 to 5 have compressible days.
  - Grade 1 has neither.
  A short section in each (K to 2: the period route, plus fold-in days if a shorter year applies to a part-week
  course) would clear the notes.
- **The readiness timing in UNIT-PLAN.md was Cory's 2026-11-11 choice** (Desk card q-unit-plans). It was made for
  grade 4 math, and that course still keeps it. The lead may want to tell Cory that every other course now places
  the check on the unit's first day.
- **The grade 12 fix report's For Cory item** (the US Government paper route for NML.T5.1 and T5.3) is that report's,
  not this pass's. It is noted at the top of the DIGEST entry.

## Gates

| Command | Result |
|---|---|
| `plan.py check` | exit 0 |
| `sequence.py check <course>`, all 15 | 0 failures each (grades K to 5: the Shorter path note) |
| `frame.py check <course>`, all 15; `frame.py check` (all 52) | 0 failures; exit 0 |
| `progression.py check social-studies` | 384 rows, 0 failures |
| `stale.py check` | 56 files, 0 failures |
| `frame.py calendar` | no stagger break; social studies check weeks unchanged (K 15, 30; 1 14, 31; 2 14, 31; 3 14, 25, 28; 4 8, 21, 27; 5 16, 29; 6 15, 23, 32; 7 13, 24, 32; 8 10, 20, 29 to 30) |

## For Cory

None.
