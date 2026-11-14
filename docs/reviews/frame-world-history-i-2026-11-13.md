# Frame read: world-history-i (World History I, about 500 to 1800, grade 9), 2026-11-13

Reader: the curriculum expert, cold (brief docs/pipeline/briefs/frame-read.md). I did not write this frame.

## What I read

- docs/agents/EXPERT.md, docs/agents/lenses/social-studies.md, docs/courses/social-studies/STANDARD.md (sections 1 to
  4), docs/sources/BASE-TEXTS.md (the ETSU partial base).
- The frame docs/courses/world-history-i/frame.md and its row in data/plans/frames.csv (`world-history-i,10,160`).
  No source map: the course has no base text (BASE-TEXTS.md: no social studies base text), only a partial base the
  frame does not map lesson by lesson, as allowed.
- All 37 wh1-* rows of data/progressions/social-studies.csv (standard, assumes, hands_on, models, words, notes).
- The anchor: every MA.WHI line of data/standards/ma-hss-2018.txt, lettered parts included.
- Frames before and after: docs/courses/world-geography-and-ancient-civilizations-ii/frame.md (grade 7, its
  "handed on" table), docs/courses/civics-government-and-civic-life/frame.md (grade 8, its "handed on" table),
  docs/courses/world-history-ii/frame.md (grade 10) and docs/courses/us-history-i/frame.md (grade 11), and the
  wh1-to-gov seam in docs/courses/us-government-and-politics/frame.md.
- The cross-subject rows named (e9-*, m3/m6/m7, s6/s7/s8, chem, phys): each exists in data/progressions. No ELA 9 or
  science 9 frame exists yet.
- Earlier reads: docs/reviews/progression-social-studies-2026-11-13.md, progression-social-studies-codex-2026-11-13.md,
  progression-social-studies-fixes-2026-11-13.md, and the other social studies frame reads of today (K, 1, 2, 5,
  grade 7, US Government, US History II).
- Gates: `python -X utf8 scripts/plan.py check` (frame world-history-i: 0 failures; 10 units, 160 days, 148 in units,
  12 checks and respond days). `python -X utf8 scripts/stale.py check`: 19 files, 0 failures.

## Verdict

The frame is sound and ready for the scope and sequence once the fixes below are made: every WHI code has a unit,
all 37 rows sit once, the units run in time order with honest reasons for the three overlaps, and the hard-history
weeks are named and guarded. The biggest risk is MA.WHI.T3.2: its twelve kingdom options run through units 3, 4 and 7,
every option is taught to everyone, and the standard's own task (map one kingdom and explain it in depth) has no home
a writer can build. The one change that matters most is to place that task in unit 3, where the parent code sits.

## Findings, most serious first

### 1. MA.WHI.T3.2's "one kingdom in depth" task has no home (moderate; firm)

**What is wrong.** wh1-african-kingdoms owns MA.WHI.T3.2 (map one kingdom or empire and explain its politics,
economy, culture and links). Its notes say the options "run across this row and" six others in units 3, 4 and 7, "and
each student maps one in depth". The frame's "One example in depth" rule says a short survey of all options, then one
in depth. But units 3, 4 and 7 teach all twelve options to everyone as full rows, not as a survey, and no unit says
when the student's own map-and-explain piece is made. A student who picks the Ottomans (unit 7, week 19 or later)
cannot do a task owned in unit 3 (weeks 7 to 10).
**Why it matters.** The writer of unit 3 cannot tell whether to plan the depth product, and the writer of unit 7 will
not plan it, since the code is not there. The standard's one task is the thing most likely to fall out.
**Fix (frame unit 3 and the wh1-african-kingdoms notes).** The depth task sits in unit 3, inside its 16 days (about
2 days): each student maps and explains one of the unit 3 options (Ghana, Mali and Songhai; Axum or the Swahili
city-states; the Mongol Empire), the options of units 4 and 7 are taught to all at their rows' depth, and the row note
says so in place of "each student maps one in depth" across all seven rows. Settled below. LAYER frame and
progression. REPEAT new.

### 2. Writing grows in one jump, from a paragraph to a multi-page argument (moderate; likely)

**What is wrong.** Units 1 to 9 write claim paragraphs "at the grade 6 to 8 level of D4.1"; the counterclaim and the
multi-page argument come only in unit 10 (weeks 28 to 31). The mid-year check asks for "a short sourced argument"
that no unit has taught at that length. The row (wh1-historical-argument) itself says writing "grows from short
paragraphs in the first unit to a multi-page argument", but the frame sets no step between.
**Why it matters.** The lens names "writing from sources appears once a year or never builds from short to long" as
a scope-and-sequence error, and adoption reviewers look for growth across the year. A grade 9 student who writes
single paragraphs for 27 weeks meets the counterclaim and length together in the last month, beside the ELA 9
process argument.
**Fix (frame, Course in brief "Inquiry arc" and unit 6).** Add a middle step in unit 6, inside its 15 days: a
one-to-two page claim from the Crusade accounts (Crusader, Byzantine, Muslim and Jewish) with one counterclaim named
and answered, as a rehearsal; D4.1.9-12 stays owned in unit 10, and the mid-year check's short argument then tests
something taught. No progression edit is needed, since the row's notes already describe the growth. Settled below.
The frame's "For the lead" item 2 suggests a progression split if readers want the counterclaim earlier; this
smaller change does the job without it. LAYER frame. REPEAT new.

### 3. wh1-sources-of-the-past and wh1-graphic-displays hand on to no row (minor; firm)

**What is wrong.** wh1-sources-of-the-past teaches the five source checks (origin, authority, structure, context,
corroborative value) and has an empty hands_on, yet us1-research-inquiry's notes say "Students use all five checks
from grade 9" and assume only wh2 rows; us1-news-reading says the grade 8 news habit is "kept in use between by
wh1-sources-of-the-past". wh1-graphic-displays (maps, parallel timelines, charts, a geospatial tool) also hands on
nothing, while wh2-imperialism-causes maps empires "at more than one scale" (D2.Geo.3) with no assumes on it.
**Why it matters.** US History I's readiness check will not test the five checks it names, and the gate cannot see
either thread. The frame's "Handed on" table is complete for the data but misses both.
**Fix (data/progressions/social-studies.csv, then the frames).** wh1-sources-of-the-past hands_on gains
us1-research-inquiry (us1-research-inquiry assumes gains it; kind: maintained skill, kept in use in grade 10 by the
source-sourcing model); wh1-graphic-displays hands_on gains wh2-imperialism-causes (and its assumes gains it). Then
add both rows to this frame's "Handed on" table and to the "Picked up" tables of the World History II and US History I
frames. LAYER progression. REPEAT yes (the social studies progression read, finding 3: skills handed on to no one
though a later row builds on them).

### 4. MA.WHI.T3.2h to T3.2j are taught in part (minor; firm)

**What is wrong.** The three American options name Maya "pyramid building and long-distance trade", the Aztec
empire's "conquests of neighbors and monumental sculpture", and the Inca empire's "conquests". wh1-american-empires
and unit 4's "What students learn" name the cities, Tenochtitlan, the road network and quipu, but not trade, conquest,
tribute-taking or the monuments.
**Why it matters.** These are the parts that make the three into empires and link them to the rest of unit 4's
power question; a unit writer working from the row will plan city life and records only.
**Fix (row notes and frame unit 4).** Add: "Classic Maya pyramid-temples and long-distance trade (obsidian, jade,
cacao); the Mexica and Inca states' conquests of neighbouring peoples and the tribute and labour they took; Mexica
monumental sculpture such as the Sun Stone." No day change. LAYER progression and frame. REPEAT yes (the grade 1
frame read, finding 2, and the Codex progression read: lettered parts of a bundled code left out).

### 5. Unit 6's dates do not hold MA.WHI.T3.6's era (minor; firm)

**What is wrong.** Unit 6 is "1000 to 1400" and its row pairs al-Andalus with Norman Sicily. MA.WHI.T3.6 is
coexistence, tolerance and trade between Arab and Christian kingdoms "from the 8th to the early 10th century", the age
of Umayyad Cordoba, before Norman Sicily (from 1061) existed.
**Why it matters.** A writer following the unit's dates will teach the 1100s and miss the century the standard names.
**Fix (frame unit 6 title and the wh1-mediterranean-encounters notes).** Title "about 750 to 1400"; the T3.6 core
case is Umayyad al-Andalus to the caliphate of Cordoba (756 to about 1000), with Norman Sicily kept as the later
example beside the Crusades. Settled below. LAYER frame. REPEAT new.

### 6. One "Check set adds" item is owned content (minor; firm)

**What is wrong.** Unit 4 lists "Kievan Rus and Mongol rule over Russia" as a candidate addition. MA.WHI.T3.2k names
Russia among the European kingdoms, and wh1-european-kingdoms teaches it.
**Why it matters.** Candidates are "confirmed or dropped" at each unit plan; owned content placed there can be
dropped by a busy writer.
**Fix (frame unit 4).** Reword: "Russia is owned (T3.2k); candidate: Kievan Rus before 1240 and the Mongol yoke, at
more depth (New York 9.9; California grade 7)." LAYER frame. REPEAT yes (the grade 5 frame read, finding 1: owned
content held as a candidate).

### 7. Stale notes: the frame is written, but two records say it is not (minor; firm)

**What is wrong.** data/plans/flow-status.csv still reads `frame:world-history-i,active,...,"Writing: ..."`, and
docs/reviews/frame-world-geography-and-ancient-civilizations-ii-2026-11-13.md says "No World History I frame exists
yet" (lines 12 and 179). The frame is written and the gate passes on it.
**Fix.** flow-status note: "Written; expert read 2026-11-13 (docs/reviews/frame-world-history-i-2026-11-13.md)". In
the grade 7 report, add after line 179: "Since written (2026-11-13): the World History I frame's 'Picked up' table
matches every grade 7 hand-on row for row (checked in frame-world-history-i-2026-11-13.md)." LAYER process.
REPEAT yes (stale notes in the progression and grade 2 and 5 frame reads).

## Checked and found right (do not undo)

- **Owned skills.** All 37 wh1-* rows sit in one unit each; review uses (D3.1 checks, the parallel timeline, D2.His.1
  context) are named as review, never in the Skills column. No unit teaches another grade's skill without saying so.
- **Standards in full.** Every MA.WHI code and lettered part sits in a unit (T1.5a to c, T2.5a to c, T3.2a to l,
  T4.1a and b, T6.2a to d, T6.3a and b), apart from the parts in findings 4 and 5. MA.WHI.T5.3 is now named on both
  wh1-colonial-americas and wh1-atlantic-slave-trade, as the progression read asked.
- **Order.** Belief systems before every unit that needs them (Crusades, millet, Reformations); the forms-of-power
  terms before the feudal comparison; unit 5's carried learning before the Renaissance and the Scientific
  Revolution; the world slavery comparison (unit 6) before the Atlantic system (unit 8); the English case before the
  Enlightenment. The three overlaps in time each carry a reason that holds.
- **Days.** 15, 15, 16, 14, 11, 15, 16, 16, 12, 18 for 5, 4, 4, 3, 3, 3, 4, 3, 3, 5 rows: no unit far from its share.
  Unit 10 is the fullest (four content rows, the capstone argument and the action in 18 days); it holds because
  wh1-constitutional-democracy is "kept short" and grade 8 taught the structure. The week ranges add up (day 160 ends
  week 32).
- **Seams.** Every grade 7 hand-on (the grade 7 frame's table, rows 81 to 88) and every grade 8 hand-on to a wh1 row
  (the civics frame's table, rows 85 to 89) is in this frame's "Picked up" table. Every wh1 hands_on is picked up in
  the World History II, US History I and US Government frames in the unit named. Chronology: grade 7 ends about 500,
  unit 1 opens with exchanges up to about 500.
- **Base text.** None; ETSU World History Since 1500 as a partial base for 1450 to 1800, with its image-by-image check
  named. No NC or reference source is mapped.
- **Values and hard history.** Faiths in the present tense as followers describe them; no "primitive" or "animist";
  Mexica sacrifice plain without standing for the society; the Rhineland massacres, the 1204 sack, plague massacres,
  the devshirme, Luther on the Jews, the Banda conquest and the Atlantic trade (about 12.5 million taken, about 10.7
  million landed) named plainly; no role play in units 6 and 8; qualified-reader flags on units 2, 4 and 8.

## Cross-subject

Same-year leans are all on ELA 9 (W.9-10.7, RI.9-10.6, RI.9-10.7, RI.9-10.8, RI.9-10.9, W.9-10.1, W.9-10.2), each
with a pick that lets history go first or teaches its own version, and earlier-year leans on math 3, 6, 7 and science
6 to 8 that need only retrieval. Every row named exists. No ELA 9 frame exists, so "taught first" cannot be checked;
the frame's hard-content and writing-load notes give that frame what it needs. Finding 2's unit 6 rehearsal should be
added to the ELA 9 writing-load note (no shared due week with an ELA 9 essay).

## The lens checklist (course frame layer)

| Line | Result |
|---|---|
| An anchor standard in the course's Massachusetts topic range has no unit | Met (WHI.T1 to T6 all placed; findings 1, 4 and 5 are about depth, not placement) |
| The replaced grade 3 year, or "your state" in grade 8, keeps Massachusetts-only content | Not applicable |
| No unit lists what the check set adds, or an addition has no recorded source | Met: every unit lists additions, each with its member (finding 6 is one owned item among them) |

## What I could not judge

- The ELA 9 and science 9 frames (not written).
- Accuracy of the African religions, Native and Atlantic slave trade content (flagged for the sensitivity read and a
  qualified reader).
- Whether Tennessee 2024 confirms the candidates (the frame says it was not read; nor did I read it).

## Settled by the expert

| Choice | Reason | File it touches |
|---|---|---|
| The MA.WHI.T3.2 map-and-explain depth task sits in unit 3 (about 2 of its 16 days), on one of Ghana-Mali-Songhai, Axum or the Swahili city-states, or the Mongol Empire | The parent code is owned there; a later option cannot be chosen for a task due in week 10 | docs/courses/world-history-i/frame.md (unit 3); wh1-african-kingdoms notes |
| A one-to-two page claim with one counterclaim, from the Crusade accounts, in unit 6 | A middle step so writing builds; uses unit 6's multi-account sources | docs/courses/world-history-i/frame.md (unit 6, Inquiry arc) |
| Unit 6 dated "about 750 to 1400", with Umayyad Cordoba as the T3.6 core case | The standard names the 8th to early 10th century | docs/courses/world-history-i/frame.md (unit 6); wh1-mediterranean-encounters notes |

## For Cory

- **People.** As the frame says, units 2, 4 and 8 need a qualified person's read before any unit ships (FOUNDATION
  7.3); none is in place.
- **Days.** 160 (a full year) is right for what the rows hold; I would not take the 150 alternative.

Not logged in the defect ledger (`plan.py defect`): the brief allows edits to this report only. The caller may log
findings 1 to 7 with found_by `expert`.

## Sources

No outside source was fetched for this read; it rests on the repository files above and memory.
- Massachusetts 2018 as coded in data/standards/ma-hss-2018.txt (WHI.T1 to T6, lettered parts).
- C3 Framework, NCSS, revised 2017 (D4.1.9-12 wording; the inquiry arc): from memory and the repo's earlier reads.
- Umayyad al-Andalus and the caliphate of Cordoba (756 to 1031), Norman conquest of Sicily from 1061; Mexica Sun Stone;
  Maya trade goods: from memory (likely; check at the unit plan).

## For the source list

Nothing new.
