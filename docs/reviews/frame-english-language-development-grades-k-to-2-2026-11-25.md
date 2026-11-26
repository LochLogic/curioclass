# Frame read: English Language Development, grades K to 2, 2026-11-25

Reader: the curriculum expert, cold (brief docs/pipeline/briefs/frame-read.md, with the after-core changes the caller
set). I did not write this frame. It is the subject's pilot frame, so this read also judges the pattern the three
later ELD frames will copy.

## What I read

- AGENTS.md (via CLAUDE.md), docs/agents/EXPERT.md, docs/agents/lenses/eld.md, docs/ADOPTION-BAR-SUBJECTS.md part 10
  (items 1 to 14, Fails if) and its ELD row in "Before a scope and sequence in this subject", docs/courses/eld/STANDARD.md
  and docs/courses/eld/APPROACH.md in full.
- docs/agents/decisions/DESK-ANSWERS.md, every entry naming ELD: the eleven ELD tools (line 176), 2026-11-16
  (q-later-sel-eld), the 2026-11-21 stage 1 calls (13 grade frames, minutes, home languages), 2026-11-21 q-fix-eld-1,
  the 2026-11-21 course-shape entry ("ELD by WIDA cluster") and 2026-11-25 (after-core frames as band frames; item 9,
  English learner supports made in the lesson).
- docs/pipeline/briefs/frame-write.md in full, including "After-core courses (added 2026-11-25)".
- The frame docs/courses/english-language-development-grades-k-to-2/frame.md in full; its row in data/plans/frames.csv
  (20 units, 480 days, 30 minutes, 5 a week, 96 weeks, year). No source map (none is due: ELD places no base units).
- The course's rows: course-list.csv `rows` = `grade:K|1|2` over data/progressions/eld.csv, all 33 K to 2 rows read
  in full, and the 12 grade 3 rows (the seam).
- data/standards/wida-2020.txt (every K, 1, 2-3 and SI K-3 id).
- The core frames the course leans on, Units tables (and unit days from data/plans/calendar.csv): ELA K, 1, 2; math K,
  1, 2; science K, 1, 2; social studies K, 1, 2. Social studies grade 2 unit 5's section plan (s05.md) for the
  two-accounts pair; data/progressions/science.csv rows s1-like-parents and s1-parent-offspring.
- docs/courses/CALENDAR.md; data/plans/calendar.csv rows for this course and for the K to 2 core and after-core checks.
- Repository searches for every named pick (the two Aesop fables, candidate replacements); docs/sources/BASE-TEXTS.md
  on the EL Education edition.
- Gates: `python -X utf8 scripts/frame.py check english-language-development-grades-k-to-2`: 0 failures; notes "unit
  days by year: K 154, 1 154, 2 154" and "20 units, 480 days (462 in units, 18 for checks and respond days)".
  `python -X utf8 scripts/frame.py calendar`: ELD sits in K weeks 18 and 28, grade 1 weeks 18 and 28, grade 2 weeks
  17 and 27, no core clash; it reports after-core clashes (finding 7). `python -X utf8 scripts/stale.py check`: 70
  files, 0 failures.

Checked and found right: the 33 rows each sit in one unit; the 26 owned ids (K 12, grade 1 14) match the standards
file, and every id cited exists; the days add (K 30+31+24+25+22+22, grade 1 24+22+20+19+24+23+22, grade 2
19+19+20+22+22+27+25, each 154, plus 6 check and respond days a year); every calendar.csv row matches the weeks the
frame states (all 20 units and all six checks); the core check weeks the frame lists for K, 1 and 2 match CALENDAR.md's
target table, and no ELD check falls in one; host unit days and weeks match calendar.csv for every host cited; every
skill id cited in a host column sits in the host unit named; both ends of every seam are in the progression.

## Verdict

The frame is a sound pilot in shape: language through the grade's own content, one live host per unit cited by course
days with "If later" lines, two checks a year placed off the core weeks, three entry points that change help and never
the task, and careful sensitive ground. It is not ready to be copied as it stands: eight of its twenty units plan no
social and instructional language although bar item 1 asks for SI in every unit, grade 1's science inform unit is
paired with the wrong science unit, and both end-of-unit fables are already used by ELA grade 3 (one as an unseen
assessment text) and social studies kindergarten. Fix findings 1 to 3 before the 3 to 5, 6 to 8 and 9 to 12 frames
copy the pattern; the rest are small.

## Findings, most serious first

### 1. Eight units plan no SI, against bar item 1 (serious; firm)

LAYER frame. REPEAT new.

What is wrong. Bar part 10 item 1: "social and instructional language (SI) planned in every unit beside one of LA, MA,
SC or SS"; STANDARD section 3 says the same ("SI every unit"). The frame places each year's four SI rows in four
units and says nothing about SI in the others: units 3, 6, 11, 12, 13, 16, 17 and 18 name no SI id and no SI use in
What students learn. The daily talk routine is SI in practice, but the frame never says so, and a unit writer reading
unit 3 or unit 17 will plan no SI language goal.

Why it matters. It is a named PRIME match criterion (Match.ELD.1) behind an [I] bar item, and the pattern multiplies
in the later bands: grades 3 to 5 have 8 or 9 content rows a year against 4 SI rows, so more than half their units
would plan no SI.

Fix. In each of the eight units, add one sentence to What students learn, as review (not in the Skills column):
"SI (review, carried; owned in grade 3): WIDA.ELD-SI.K-3.<use>, <the talk move on this content>." Picks in Settled by
the expert. Add one line to The course in brief, Every unit, the same moves: "SI in every unit: the unit's own SI row,
or one SI use named as review on the host content (bar item 1)." Carry it into For the lead item 2 as a "copy" rule.

### 2. Unit 12 is paired with the wrong science unit (serious; firm)

LAYER progression and frame. REPEAT new.

What is wrong. Unit 12 (and row g1-sc-inform) teaches "how young animals and plants are like their parents", with
"Both ___ have", alike and different, and an end-of-unit task to "match the young to the parent; tell the teacher how
they are alike". That is 1-LS3-1, science grade 1 row s1-like-parents, taught in science grade 1 unit 3 "Like their
parents" (days 22 to 27, weeks 9 to 12). The host the frame and the row's cross_subject name is s1-parent-offspring,
science grade 1 unit 7 "Parents and young" (days 56 to 61, weeks 24 to 26), which is 1-LS1-2: how the young signal
(crying, cheeping) and parents respond (feeding, protecting). So in weeks 23 to 27 the ELD class talks about likeness
while science teaches signals and responses, and the likeness content is three months stale.

Why it matters. "Language through content, the core unit the class studies that month" is the subject's first
principle (STANDARD section 3; lens). A scope writer would build 23 days on a host that does not hold the content.

Fix. Keep unit 12 in weeks 23 to 27 on its live host and retarget its inform use to that host: a short report on a
pattern of behavior ("When the baby ___, the parent ___"; signal, cry, feed, protect, pattern), with likeness
retrieved on day 2 from science unit 3 and the sky patterns from science unit 1. The fixer edits g1-sc-inform's
cross_subject to name both `science:s1-parent-offspring (host investigation)` and `science:s1-like-parents (host
investigation, earlier)`, and rewrites its task, forms and words to the behavior pattern with likeness as retrieval.
Unit 12's Host, What students learn and end-of-unit lines change to match; the "never 'How are you like your
parents?'" note stays.

### 3. Both end-of-unit fables are already used by other courses (serious; firm)

LAYER frame. REPEAT yes (lesson 11, picks chosen so they do not repeat another grade's picks).

What is wrong. Units 8 and 20 claim "The Lion and the Mouse" and "The Crow and the Pitcher" are "not used by any other
Curio Class course". Both are: ELA grade 3 uses The Crow and the Pitcher as its unit 1 mid-unit assessment text (u01-3,
day 13; data/plans/english-language-arts-grade-3/items.csv s01-A6 to A8) and The Lion and the Mouse on day 12 and
again in unit 2 (s01.md, u01-3.md, u02-1.md); social studies kindergarten reads The Lion and the Mouse on day 16
(s02.md).

Why it matters. An end-of-unit assessment here must be unseen, and the grade 2 ELD task would spoil ELA grade 3's
unseen assessment for the same English learners a year later. The kindergarten social studies use means many grade 1
ELD students have heard The Lion and the Mouse.

Fix (settled below). Unit 8: "The Bear and the Two Travelers" (Townsend's translation; a lesson stated at the close,
fits "how does the story end, and what does it teach?"). Unit 20: "The Fox and the Goat" (Townsend; a clear problem,
the fox in the well, and a solution). Neither appears anywhere in docs or data. Replace "not used by any other
Curio Class course" with "checked unused in docs/ and data/ on 2026-11-25". For the lead item 2's "picks checked
unused" rule holds; add "search docs/ and data/ for the title, including section plans and items.csv, not frames only".

### 4. Days do not follow the load rule the frame states (moderate; likely)

LAYER frame. REPEAT yes (days by load, lesson 9).

What is wrong. The Days bullet says an LA row weighs most, a content row next, an SI row least. The counts run the
other way in places: grade 1's two-row units are the shortest (unit 10, SC Explain plus SI Explain, 19 days; unit 9,
SS Argue plus SI Argue, 20) while its one-row units are longer (unit 11, 24; unit 12, 23; unit 13, 22). In grade 2,
unit 17 holds two content rows (SC Explain and SC Argue, four carried ids) in 22 days, the same as unit 18's one row,
and unit 14 (LA plus SI, plus the year's new talk routine) has 19, fewer than unit 16's single SS row (20). After the
three assessment and respond days, unit 10 has 16 teaching days for two rows and unit 11 has 21 for one.

Why it matters. The real driver is host timing, which is a fair reason, but the frame states a different one; a scope
writer will meet the squeeze in units 10, 14 and 17 without being told why.

Fix. Either rebalance inside each year (for example unit 10 to 22 and unit 11 to 21; unit 17 to 24 and unit 18 to 20,
both inside their hosts' windows), or rewrite the bullet: "Days follow the host windows first; within them, a unit
holding two rows gets ..." and name units 10, 14 and 17 as tight with what each leaves to the respond day.

### 5. Each year's last unit lies outside every course-level check (moderate; likely)

LAYER frame. REPEAT new.

What is wrong. Every year-end check falls before the year's last unit (6, 13, 20), so those units are sampled by no
course-level check. Units 6 and 13 are the only math units of kindergarten and grade 1, which own those ids
(WIDA.ELD-MA.K.Inform and WIDA.ELD-MA.1.Inform, both modes): four owned ids that no course-level check ever samples.
The frame explains the week choice but not this cost.

Why it matters. Bar item 7 asks growth watched across the year in more than one way; the owned math language of two
years rests on one end-of-unit sitting each.

Fix. In K and grade 1 the year-end check samples the year's math language on new content through the retrieval route
(a heard description of a new group or shape; a chart told), drawing on units 6 and 13's forms as taught earlier in
units 1 and 7 where the forms overlap, or the frame says plainly: "MA K and MA 1 are checked by their end-of-unit
assessment only; the record goes to the next teacher." For the copying frames: place each owner year's MA, SC and SS
rows before the year-end check where host order allows, and say so where it does not.

### 6. Unit 19 runs mostly after its host, and its fallback pair does not exist (moderate; firm)

LAYER frame. REPEAT new.

What is wrong. Social studies grade 2 unit 5 runs weeks 18 to 23; unit 19 runs weeks 22 to 27, so four of its six weeks
follow the host, yet For the lead item 7 does not list it among the units behind their host. (The host's two-accounts
day falls on school day 107, week 22, per s05.md, so the start is well timed; the rest is not.) Social studies unit 6,
alongside in weeks 23 to 26, interviews a family member about where the family came from, which unit 19's sensitive
note does not mention. The family note "offers the host's other pair (two reports of a town flood)": the progression
row names that pair as an example, but the host's written section plan (s05.md) uses arrival accounts (Antin, Anna,
Catherine) and an invented classroom move, and no flood pair; the flood pair appears only in social studies grade 2's
year-end check (unseen accounts).

Why it matters. A family asking for "the other text" would be offered something that does not exist, and the host's
check pair would be spent if ELD wrote it.

Fix. Add unit 19 to For the lead item 7. In unit 19's note: "The alternative pair is Curio Class's own (two class
reports of one school event, not a move), written with the unit; the host's year-end flood pair is not used." Add: "Social
studies unit 6 runs alongside and asks for family interviews; ELD prompts stay on the supplied sources."

### 7. After-core check weeks pile up, and the tool and the brief disagree (moderate; firm)

LAYER process. REPEAT new.

What is wrong. `frame.py calendar` reports clashes in all six ELD check weeks: K weeks 18 and 28, grade 1 weeks 18 and
28, grade 2 weeks 17 and 27, with physical education (the same six weeks exactly), visual arts (weeks 17 and 18) and
library or health (weeks 27 and 28). The brief bars only core weeks; the stagger rule CALENDAR.md states (one teacher,
no week holds two subjects' checks) is what the tool applies. The frame's own rule, "the latest free week before the
core checks", is why ELD and PE land together: two pilots used the same rule.

Why it matters. In many K to 2 schools the classroom teacher teaches designated ELD, so ELD's one-to-one talk task
competes with the same adult's time. Every later after-core frame using "latest free week" will pile on the same weeks.

Fix. For the lead: a rule for after-core frames among themselves (either "after-core checks may share a week with one
another; the tool lists them as notes, not clashes" or a set of after-core weeks per subject). Until then this frame
keeps its weeks; For the lead item 2 should not tell the later ELD frames to copy "latest free week" without the rule.

### 8. g2-ma-argue is taught only in half (minor; firm)

LAYER progression. REPEAT new.

What is wrong. The row's task, frames and words are odd and even as well as comparing three-digit numbers; unit 18
drops odd and even because math grade 2 unit 8 (days 132 to 143) comes later. The frame says so, but the row is
unchanged. The ids are carried (grade 3 owns them), so no owned standard is short.

Fix. For the lead: the fixer adds to g2-ma-argue's notes "A frame may argue from comparisons only when the host's odd and
even unit comes later; odd and even then returns in grade 3."

### 9. Kindergarten's mid-year talk check follows math's one-to-one days with no gap (minor; judgment call)

LAYER frame. REPEAT new.

What is wrong. Math kindergarten's mid-year check is days 84 and 85 (week 17); ELD's is days 86 and 87. CALENDAR.md rule 2
keeps ELA and math one-to-one checks five school days apart because one adult hears every child alone. ELD's talk task
is also heard one at a time. Grades 1 and 2 are fine (seven and five days from the nearest core one-to-one).

Fix. Add to the Weeks paragraph: "Kindergarten's mid-year talk tasks follow math's one-to-one days 84 and 85 directly;
where one adult gives both, the heard parts and drawing go on day 86 and every talk task on day 87, so the one-to-one
load starts two school days after math's." Grades 1 and 2 need no change; no unit or day count moves.

### 10. Stale notes (minor; firm)

LAYER process. REPEAT yes.

- For the lead item 9 says frame.py reads the grade as "k-2", "does not see ELD checks" and spreads band days over 96
  weeks. It is out of date: frame.py (calendar_rows, the band branch) places each year on its own grade's calendar,
  and `frame.py calendar` lists ELD's weeks by grade and checks them. Replace item 9 with the after-core clash question
  of finding 7.
- docs/ADOPTION-BAR-SUBJECTS.md, ELD row: "Owed: the progression check entry in scripts/progression.py; four calls
  (Desk q-fix-eld-1). Build after C11 is proven". The check entry is done (STANDARD.md owed table, 2026-11-21) and the
  four calls were answered (DESK-ANSWERS 2026-11-21). Replacement: "Owed: nothing before the frames (written, Cory,
  2026-11-25). The scope and sequence, unit plans and days wait until C11 is proven in the core courses (STANDARD
  section 6)."
- For the lead item 1 rewrites STANDARD.md and the lens but misses docs/courses/eld/APPROACH.md's opening line
  ("Building waits until C11 is proven in the core courses"); it takes the same addition.

### 11. The mid-unit count names unit 20 (minor; firm)

LAYER frame. REPEAT new.

The Days bullet says "units 1, 2, 19 and 20 are over 25 days and each hold one mid-unit assessment day". Unit 20 has 25
days, is not over 25, and its row names no mid-unit assessment. Fix: "units 1, 2 and 19".

### 12. Cognate notes call true cognates non-cognates (minor; firm)

LAYER frame (and progression, same kind). REPEAT new.

Unit 14: "escuela and school (not a cognate, so the card carries it)": both come from Latin schola (Wiktionary,
etymonline). Unit 10: "regla and rule are not": both from Latin regula. They are cognates that are hard to see, which is
the useful teaching point. Unit 14 also names "insecto and insect", which has nothing to do with a schools unit. The
grade 3 rows carry the same slip (fuerza and force, gobierno and government). Fix: "escuela and school share a root but
look different, so the card carries it"; the same wording for regla and rule; drop insecto in unit 14 (use "comunidad
and community"). The spanish read will see these; the progression fixer applies the same wording to the grade 3 rows.

### 13. Sources named loosely (minor; likely)

LAYER frame. REPEAT yes.

- Base text: "EL Education K to 5, CC BY 4.0" holds only for the 2017 edition (BASE-TEXTS.md line 25); the 2025 edition
  is CC BY-NC 4.0 (Open Up Resources, edition page). Write "EL Education K-5 Language Arts, 2017 edition, CC BY 4.0".
- Unit 19: "a national child traumatic stress network's free guidance" names no guide. NCTSN holds a refugee trauma
  collection, including the "Children of War" guide for educators and a fact sheet on traumatic separation and refugee
  and immigrant trauma; name the network and the guide by title with its address.
- Unit 11: "a national park service or geological survey image": US Geological Survey images are generally public
  domain; National Park Service pages carry many copyrighted images. Write "a US Geological Survey or National Park
  Service image marked public domain, credited".

## Spot checks at source (facts named from memory)

| Fact in the frame | Held? | Source |
|---|---|---|
| Townsend translated Aesop, 1867 | Holds | Project Gutenberg #21 (translator George Fyler Townsend); Internet Archive scan "Three hundred Aesop's fables", Routledge [1867] |
| The Lion and the Mouse and The Crow and the Pitcher are in Townsend | Hold (so do The Bear and the Two Travelers and The Fox and the Goat) | Gutenberg #21 text, mirror ftp2.gwdg.de |
| Neither fable is used by another Curio Class course | Fails | finding 3 |
| EL Education K to 5 is CC BY 4.0 | Holds for 2017 only | finding 13 |
| Federal English learner toolkit, OELA, free online | Holds | ncela.ed.gov English Learner Tool Kit |
| NCTSN free guidance for teachers of refugee and immigrant children | Holds in part (resources exist; none named) | nctsn.org refugee trauma resources; Children of War guide for educators |
| escuela/school and regla/rule are not cognates | Fails | finding 12 |
| Host texts: ELA grade 2 unit 4 tales; science grade 1 rice on a drum, peephole box | Hold | the host frames' Units tables |
| The host's town flood pair (unit 19) | Fails | finding 6 |

## The lens checklist (course frame layer)

| Line | Met? |
|---|---|
| Units built on word lists or drills with no content | Met: every unit has a content host |
| One level for all, or levels that change the content | Met: three entry points, same task |
| A WIDA id the file does not hold | Met: every id checked |
| No entry and exit points, or a course that stands in for ELA | Met: Entry points bullet, bar item 8 line |
| ELA pairing missing for an LA unit, host missing for MA, SC or SS | Met in form; unit 12's host is the wrong unit (finding 2) |

## The pattern: what the other ELD frames should and should not copy

Copy: one unit per content row with each live host cited by course days, "If later" lines, and later hosts never used;
the Host unit and key language uses column (For the lead 3); a Year column with each year whole (its own units, two
checks with a respond day each, its own talk routine); end-of-unit assessments of two days on Curio Class's own new
content plus a respond day; the entry-point withdrawal days; the sensitive-ground notes per unit; retrieval on day 2
for last year's rows; the paper path and printing-only costs.

Copy with the fixes: SI in every unit, the unit's own row or one SI use named as review (finding 1); picks checked
unused across docs/ and data/, not frames only (finding 3); host content checked against the host row's standard, not
its title (finding 2); days stated as host-window first, with tight units named (finding 4).

Do not copy: "the latest free week before the core checks" until the lead settles after-core weeks among themselves
(finding 7); a year-end check that leaves an owner year's only math or science row unsampled without saying so
(finding 5); "not a cognate" for a hidden cognate (finding 12).

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Unit 8's end-of-unit tale: "The Bear and the Two Travelers" (Townsend, retold in Curio Class words) | Unused anywhere in docs/ and data/; ends with its lesson | frame.md unit 8 |
| Unit 20's end-of-unit fable: "The Fox and the Goat" (Townsend, retold) | Unused; plain problem and solution | frame.md unit 20 |
| SI review per unit: 3 Inform (the weather report to a partner), 6 Inform (telling a partner how the set was sorted), 11 Inform (a place described so a partner can draw it), 12 Inform (the report to a partner), 13 Inform (a hidden shape described), 16 Explain (why a plan used the resource), 17 Argue (agreeing and disagreeing on the best material), 18 Argue (answering a partner's claim) | Each is the talk the unit already plans, named as SI | frame.md units 3, 6, 11 to 13, 16 to 18 |
| Mid-unit wording: "units 1, 2 and 19" | Unit 20 has 25 days | frame.md Days bullet |
| Cognate wording as in finding 12; unit 14's example "comunidad and community" | Accurate and on the unit's content | frame.md units 10, 14 |
| "EL Education K-5 Language Arts, 2017 edition, CC BY 4.0" | Licence differs by edition | frame.md Base text |

## For Cory

- Newcomer strand time (For the lead item 8): a people-and-time call already raised by the frame; I agree with its pick
  (added time where the school gives it, else a side table inside the period, the school deciding).

## Sources

- Project Gutenberg #21, Three Hundred Aesop's Fables, tr. George Fyler Townsend: https://www.gutenberg.org/ebooks/21
  (text read from the mirror https://ftp2.gwdg.de/pub/misc/gutenberg/2/21/21.txt, titles checked).
- Internet Archive scan, Routledge [1867]: https://archive.org/details/threehundredaeso00aesouoft (date only).
- Open Up Resources, EL Education K-5 Language Arts 2025 edition (licence CC BY-NC 4.0):
  https://www.openupresources.org/ela-curricula/el-education-k-5-language-arts-2025-edition/
- NCELA, English Learner Tool Kit: https://www.ncela.ed.gov/educator-support/toolkits/english-learner-toolkit
- NCTSN, Children of War guide for educators:
  https://www.nctsn.org/sites/default/files/resources//children_of_war_guide_for_educators.pdf
- Wiktionary, escuela: https://en.wiktionary.org/wiki/escuela ; etymonline, school: https://www.etymonline.com/word/school

## For the source list

- The Gutenberg #21 main site returned 503; the gwdg.de mirror of the plain text works.
- NCTSN's Children of War guide for educators (address above) as the named guide for unit 19's sensitivity read.

## Confidence

Findings 1, 2, 3, 6, 7, 8, 10, 11 and 12 firm (the files and sources agree); 4, 5 and 13 likely; 9 a judgment call.
