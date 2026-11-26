# Expert cold read: Visual Arts frames, grades 3 to 5, 6 to 8 and 9 to 12 (2026-11-25)

One combined read of three after-core arts frames written 2026-11-25 on the pattern of the fixed K to 2 pilot. Brief:
docs/pipeline/briefs/frame-read.md with the lead's after-core changes (subject arts; seams between bands and against
the other arts frames of the same band; check-week clashes listed apart and not counted).

## What I read

- AGENTS.md; docs/agents/EXPERT.md; docs/agents/lenses/arts.md; docs/courses/arts/STANDARD.md; the arts row of
  docs/ADOPTION-BAR-SUBJECTS.md (line 568, for the stale owed list only).
- docs/courses/visual-arts-grades-3-to-5/frame.md, -6-to-8/frame.md, -9-to-12/frame.md, in full.
- docs/courses/visual-arts-grades-k-to-2/frame.md (seams, models, handed-on table); the pilot's expert read and fix
  report (docs/reviews/frame-visual-arts-grades-k-to-2-2026-11-25.md, -fixes-2026-11-25.md), for pattern notes and
  REPEAT tags. I did not open the Codex read of the 3 to 5 frame, so this read is not anchored on it.
- data/progressions/arts.csv, all 76 va rows of grades 3 to 12 (ids, assumes, hands_on, models, cross_subject, notes).
- data/standards/ncas-performance-standards-words.txt, every visual arts line for grades 3 to 8 and the three levels.
- data/plans/frames.csv rows for the four visual arts courses.
- The Works cells of the music, theater, dance and media arts frames of all four bands, searched for every work and
  maker the three frames name.
- Gates run (all read-only): `frame.py check` on the three courses (0 failures each; 3 to 5 and 6 to 8: 60 unit days a
  year, 192 days; 9 to 12: 156 a level, 640 days), `progression.py check arts` (498 rows, 0 failures), `stale.py
  check` (121 files, 0 failures), `frame.py calendar` (for the clash section). I ran one read-only `git log` on
  arts.csv by mistake; nothing else touched git.
- No web pages were opened and nothing was downloaded. Every national standard's text below is from memory of the
  2014 visual arts performance standards; work facts are from memory and marked so.

## Verdict

- **Grades 3 to 5: sound, one serious fix shared with 6 to 8.** The 45 ids sit in their own years, every id's
  action matches the national standard, the seams to K to 2 and 6 to 8 match the rows at both ends, and the days add.
  The biggest risk is the works list: written beside the 6 to 8 frame, it shares nine works with it. The check-day
  plan also asks one teacher to read aloud, scribe and run handling items at once.
- **Grades 6 to 8: sound once the shared works are swapped and VA:Cr1.2.7a is retaught.** Days, checks, the
  once-a-week path and the cross-subject leans all hold. Unit 6 teaches written instructions (LeWitt-style) where the
  standard asks for criteria that guide a work to its goal, following a words line that drifted.
- **Grades 9 to 12: sound.** All 45 level ids match the national text, the level structure, bridge, review units and
  short path follow STANDARD.md 3.2, and the Level 4 rows contribute as written. It repeats several works from the
  bands below, and its seam section still says the 6 to 8 frame is not written.
- The one change that matters most: settle the works across the three bands in one pass (S1), so no student meets the
  same work as fresh study in two bands unless the plan names it a revisit with a new task.

## Findings

Counts: serious 2, moderate 5, minor 9, judgment calls 4.

### Serious

**S1. The same works are studied as new in two or three bands.** LAYER frame. REPEAT new (the pilot's pattern note
asked for a range check across the band; this is across bands). Confidence firm (the frames' own text).

The 3 to 5 and 6 to 8 frames were written at the same time; each checked only against K to 2 (6 to 8 For the lead
item 4 says so). The result:

| Work | 3 to 5 | 6 to 8 | 9 to 12 | Keep in | Fix (the swap) |
|---|---|---|---|---|---|
| Jacob Lawrence, The Migration Series | unit 4 | unit 1 | units 2, 6 (review), 12 (revisit) | 3 to 5 and 9 to 12 | 6 to 8 unit 1: Pieter Bruegel the Elder, The Harvesters (Flanders, 1565, the Metropolitan Museum of Art, open access), how people lived and worked, with the kente |
| Romare Bearden, The Block | unit 1 | unit 2 | | 3 to 5 | 6 to 8 unit 2: promote the unit's candidate (a collage or assemblage maker from Latin America or Asia, from a museum's own page) to a pick |
| Gustave Caillebotte, Paris Street; Rainy Day | unit 3 | unit 6 | | 6 to 8 (its perspective lesson) | 3 to 5 unit 3: Camille Pissarro, Boulevard Montmartre on a Winter Morning (France, 1897, the Met, open access), a built place and a mood |
| Jaune Quick-to-See Smith, State Names | unit 9 | unit 7 | unit 13 (another work) | 6 to 8 (its map unit) | 3 to 5 unit 9: an Anishinaabe (Ojibwe) beaded bandolier bag from an open-access museum page, its floral designs read for their links to plants and place; the sensitivity agent reads an Anishinaabe source first. Keeps year 5's Native maker |
| Fan Kuan, Travelers among Mountains and Streams | unit 11 | unit 5 | | 6 to 8 (layered ink) | 3 to 5 unit 11: Qian Xuan, Wang Xizhi Watching Geese (China, about 1295, the Met, open access), judged by scholar-painters' standards of brush and spirit |
| Judy Baca, The Great Wall of Los Angeles | unit 6 | units 11 and 12 | | 6 to 8 | 3 to 5 unit 6: keep Chicano Park and promote the candidate (a group-made work from Asia or Africa) |
| Leonardo da Vinci's notebooks | unit 10 | unit 10 | | 6 to 8 (a record of early steps) | 3 to 5 unit 10: Maria Sibylla Merian, plates from Metamorphosis insectorum Surinamensium (Amsterdam, 1705, public domain), research by watching and drawing |
| Nation to Nation (treaties exhibition) | unit 12 | unit 12 | | 6 to 8 (an exhibition's sway on belief) | 3 to 5 unit 12: promote the candidate (an exhibit's own pages from outside the United States), and drop the treaties line from the leave-out and sensitivity bullets |
| Maya Lin, Vietnam Veterans Memorial | unit 12 | | units 4, 6, 9 | 9 to 12 (the jury unit) | 3 to 5 unit 12: Thomas Moran's Yellowstone paintings (1872, public domain; the unit plan picks the holding museum's page), pictures that helped make the first national park; the sensitivity agent reads a source on the Native nations of the Yellowstone lands first |
| Work Projects Administration posters (Library of Congress) | unit 5 | unit 1 | | both, with a split | 3 to 5 picks a parks poster only; 6 to 8 picks work-safety and travel posters and names the collection as a return (media arts K to 2 already uses its library and health posters) |
| Kehinde Wiley, Barack Obama | | unit 9 | unit 10 | 6 to 8 | 9 to 12 unit 10: Amy Sherald, Michelle LaVaughn Robinson Obama (2018, the National Portrait Gallery), described and linked |
| Warhol Foundation v. Goldsmith (2023) | | unit 9 | unit 12 | 9 to 12 (liberty and duty, Advanced) | 6 to 8 unit 9: Curio Class original case cards on own, borrowed, open-license and public domain images; no court case |
| Benin plaques and the 2022 return | | unit 5 | unit 15 | 6 to 8 (display changes value) | 9 to 12 unit 15: promote the candidate conservation case (Asia or the Americas, from the holding museum's own pages); update the leave-out bullet |
| Elizabeth Catlett, Sharecropper | unit 1 | | unit 1 (bridge) | 3 to 5 | 9 to 12 unit 1: Albrecht Dürer, Melencolia I (1514, the Met, open access), value built from line |

Why it matters: a student who takes the sequence studies Lawrence's series as new work in grades 3 and 6, and nine
works twice in three years; the bar's range criterion and the lens ("works from many times and places") are read
across a student's whole path, and unit plans would write the same work cards twice. The kept duplicates (Lawrence in
3 to 5 and Level 1) are fine: Level 1 assumes no earlier art, and its unit 12 revisit is the model for a named revisit.

Fix: apply the swaps above (each is a pick the unit plan confirms on the item's own page, as the frames' Base text
bullets say); add one line to each frame's Base text bullet: "No work studied in another visual arts band is studied
again as new work; a revisit is named as one, with its new task." Re-check after the swaps that 3 to 5 still has, in
every year, Africa, Asia, Europe, the Americas, a Native maker or community and a living maker (year 5's Native maker
is the bandolier bag; year 3's living maker is Shaun Tan, see m9). Facts in the table are from memory.

**S2. Grade 7's VA:Cr1.2.7a is taught as writing instructions, not criteria.** LAYER standard and frame. REPEAT yes
(the pilot's C1: a words line drifted and the unit followed it). Confidence likely.

The national standard asks the student to develop criteria that guide making a work toward an identified goal. The
words line (line 1027) says "Write guidelines to steer making ... toward a stated aim", and 6 to 8 unit 6 takes
"guidelines" as Sol LeWitt's how-to instructions: the kept card is instructions a partner follows, judged on where
they were unclear. That checks clear instructions, not whether criteria steer a work to its aim. A day writer would
build an instruction-writing lesson. The row va-g7-ideas carries the same words.

Fix: unit 6's VA:Cr1.2.7a line becomes: the student writes three or four criteria the perspective work must meet for
its stated aim (for example "the street reads as deep from the vanishing point", "the eye goes first to the doorway"),
checks the half-made work against them at a marked point and makes one change they steered; LeWitt stays as a study of
how written rules shape a work. Evidence: a kept card with the aim, the criteria, the midpoint check and the change.
Year 7's year-end check item ("written guidelines for a new small task with its aim") becomes "criteria for a given
aim, and one decision they would steer". Words line 1027: "Set criteria a work must meet for its aim, and let them
steer making." (14 words). Row va-g7-ideas: "write guidelines to steer" becomes "set criteria that steer".

### Moderate

**M1. The 3 to 5 check day asks one teacher to do three things at once.** LAYER frame. REPEAT yes (pilot E3, check-day
load). Confidence likely.

The brief's 39 minutes run a 15-minute sitting with prompts read aloud on request and answers scribed for a child who
writes with difficulty, then a 12-minute table of six groups of five, each child showing safe handling of a tool in
about 24 seconds (units 1, 5 and 9), while the others "finish the sitting". In a class of 30 the reading aloud, the
scribing and the table compete, and 24 seconds is not enough to watch a child carry, use, pass and store pointed
scissors (VA:Cr2.2.4a). Unit 9's table item (clean and store a brush and palette) needs paint on a day the brief says
has none.

Fix: move the three handling items off the check day. VA:Cr2.2.3a and VA:Cr2.2.5a are observed on the last two making
days from a rotating list on the record sheet (as 9 to 12 unit 2 does); VA:Cr2.2.4a is the tool-check record from the
gate before pointed scissors are first used, plus one observation on a making day. The check-day table then holds only
scribed answers. Add to the brief: the teacher reads every sitting prompt aloud once to the whole class before the
table opens.

**M2. Three words-file lines and two rows are narrower than the national standards (the lead's open items).** LAYER
standard and progression. REPEAT yes (pilot C1). Confidence likely (standard text from memory).

- VA:Pr5.1.4a (line 1096): "in different places, times, and formats" loses indoor or outdoor and physical or digital,
  and "times" reads as eras, which is VA:Pr4.1.4a's ground. The 3 to 5 frame's replacement is 15 words, over the
  14-word limit. Line: "Analyze showing and protecting art indoors or out, temporary or permanent, physical or
  digital." (14). Row va-g4-show: replace "Compare a museum's old and new ways of keeping and showing art from pictures
  and a short video, and plan" with "Compare old and new ways of keeping and showing art, weigh indoor or outdoor,
  short or long term and paper or screen, and plan" (it also drops the video, which the paper path does not need).
- VA:Re8.1.5a (line 1145): leaves out visual elements. Line: "Find an artwork's ideas and mood from form, structure,
  context, subject, visual elements, media." (14). Row va-g5-judge: add "visual elements" after "subject".
- VA:Cn10.1.7a (line 1171): "document" loses "visual" and "to make and experience art". The 6 to 8 frame's
  replacement is 15 words. Line: "Alone or together, visually record where and when people locally make or see art."
  (14).

The frames already teach each in full, so only the line, the two rows and the frames' For the lead items change.

**M3. Stale notes in all three frames.** LAYER process. REPEAT yes (pilot E5). Confidence firm.

| Where | Note | Now | Rewrite |
|---|---|---|---|
| 9 to 12, Seams, first paragraph | "Visual Arts, grades 6 to 8 has no frame written, so this table is taken from the progression's grade 8 rows" | The 6 to 8 frame exists; its handed-on table matches this one row for row | "The rows below match Visual Arts, grades 6 to 8's handed-on table and the Level 1 rows' `assumes` cells." |
| 3 to 5, For the lead 1 | "four after-core clashes, all with physical-education ... Year 4 (weeks 17 and 25) shows no clash today" | `frame.py calendar` now keys arts by course: grade 4 week 17 clashes with dance, media arts and theater, week 25 with media arts; grades 3 and 5 week 26 have five or six courses | Replace with the clash list in the section below |
| 3 to 5, For the lead 3; 9 to 12, For the lead 8 | va-g5-design "labelled"; va-g8-craft "open licence" | Both rows now read "labeled" and "open license" (row changes landed) | Drop both items |
| 3 to 5, For the lead 3 | "(Row changes below)" | No Row changes section | Drop with the item |
| 6 to 8, Standard bullet | "two rows' descriptions leave out part of an id and are listed under For the lead" | No For the lead item names them | Name them (va-g7-ideas, see S2, and any other) or drop the clause |
| 6 to 8, For the lead 4; 3 to 5, For the lead 2 | works across bands unchecked; words-line pick | Settled by S1 and M2 | Replace with the settled lines |

**M4. The 9 to 12 show units run into the finals week, not to week 31.** LAYER frame. REPEAT new. Confidence firm
(arithmetic).

The brief and the Grade 12 calendar bullet say the curating unit's show is in weeks 25 to 31. Level 1 unit 5 is days
121 to 158 (weeks 25 to 32); Levels 2 and 3 units 10 and 15 are days 119 to 158 (weeks 24 to 32). Their last two or
three days, the second check day included, share week 32 with the year-end check. The senior fold rule ("runs to week
31") is then wrong as written.

Fix: the Course-level checks bullet says "in weeks 24 or 25 to 32 (days 119 or 121 to 158), its show by day 155 and
its respond days in week 32 beside the year-end check"; the Grade 12 bullet folds up to five days so the show and its
respond day land by week 31 for a school whose seniors leave early.

**M5. Same-band repeats with the other arts frames.** LAYER frame. REPEAT new. Confidence firm.

- A Lakota winter count from the Smithsonian's winter count pages: visual arts 3 to 5 unit 4 (grade 3) and media arts
  3 to 5 (grade 5, MA:Cn10.1.5b). Fix: visual arts keeps it (VA:Pr6.1.3a is about how cultures record history); the
  lead asks media arts for another record of an event, or names it in both as a planned cross-link.
- Shaun Tan: visual arts 3 to 5 unit 2 (his invented worlds) and media arts 3 to 5 (The Lost Thing). Different works;
  fix: one line in each unit naming the other as a link, or visual arts promotes its candidate (a living maker from
  Africa or Latin America) and keeps Tan as the candidate.
- Lewis Hine's child-labor photographs: visual arts grade 5 (unit 12) and media arts grade 6. Adjacent years, other
  band; fix: visual arts keeps Hine (Moran replaces Lin, S1) only if media arts 6 to 8 swaps, else visual arts uses
  Moran alone with its candidate exhibit. The lead decides in the calendar pass.
- Different works by one maker, no change asked: Sol LeWitt (dance 6 to 8, in Lucinda Childs's Dance; visual arts 6 to
  8 unit 6), Wangechi Mutu (media arts 9 to 12; visual arts 9 to 12 unit 3), Wendy Red Star (media arts K to 2;
  visual arts 9 to 12 unit 9). Each is a cross-link the unit plans can name.

### Minor

- **m1.** 6 to 8 states the check-day minutes two ways (brief: set-up 3, self-check 5, sitting 27, collecting 3, 2
  spare; Course-level checks: set-up 3, sitting 32, collecting 3, clean-up 2). Fix: the course-level check paragraph
  says "as the brief's check day, with the self-check's 5 minutes added to the sitting". LAYER frame.
- **m2.** 9 to 12 Base text: "four Native American makers or Native-led shows: units 5, 9, 13, 18 and 19" lists five
  units and six makers or shows (unit 9 has Luger and Red Star). Fix: "six Native makers or Native-led shows, in units
  5, 9, 13, 18 and 19". LAYER frame.
- **m3.** 9 to 12 Day kinds: "a paired unit of 32 to 40 days runs roughly: 9 understanding, 6 fluency, 14 to 20
  application ... 1 respond" adds to at least 34, more than unit 2's 32. Fix: "8 or 9 understanding, 5 or 6 fluency,
  12 to 20 application". LAYER frame.
- **m4.** Free paths that buy: 6 to 8 unit 9 ("clean foam trays bought new") breaks "nothing must be bought". Fix: the
  free path is a card collagraph (cereal-box card layers glued, inked with thickened tempera, rubbed with a spoon).
  9 to 12 unit 7 ("plates from clean food trays") lacks the meat-tray rule 3 to 5 and 6 to 8 state. Fix: add "never
  from raw meat or poultry". LAYER frame.
- **m5.** The Great Wall of Los Angeles is "begun 1976" in 3 to 5 and "begun 1974" in 6 to 8. S1 removes it from 3 to
  5; the 6 to 8 unit plan confirms the year on the mural's own pages (from memory: conceived 1974, painted from 1976).
  LAYER frame.
- **m6.** Jaune Quick-to-See Smith died in 2025 (from memory; 9 to 12 says "1940 to 2025"); 6 to 8 unit 7 still says
  "born 1940; the unit plan records her dates". Fix: "1940 to 2025" in 6 to 8, so no count of living makers leans on
  her. LAYER frame.
- **m7.** Row va-g1-craft (a K to 2 row) still says "practise each tool's safe grip" (UK verb). Fix: "practice".
  LAYER progression.
- **m8.** 9 to 12 Readiness bullet, the Level 4 sentence ("its ten minutes on the last day of unit 15's respond work
  for a student continuing") is hard to follow. Fix: "Level 4 has no review unit: a returning student's readiness
  check is ten minutes on unit 16's day 2, on the Level 3 guide." LAYER frame.
- **m9.** 9 to 12 unit 2 calls the VA:Re7.1.Ia task a "short proposal" (from the words line "Propose ways"); the
  standard asks the student to hypothesize. A writer may read "proposal" as an exhibit proposal. Fix: "a short written
  hypothesis, with evidence from three panels". LAYER frame.

### Judgment calls

- **J1.** 3 to 5 meets VA:Pr4.1.3a's online spaces with a paper mock-up of a class web page and VA:Cr1.2.3a's
  technology with paper tools. Reasonable for a no-device course; keep, and let the unit plan offer the shared device
  in turns where the school has one, as unit 2 already does.
- **J2.** 9 to 12 For the lead 3, no blades so no linocut. Keep until the safety agent's read; linocut in Levels 2 and
  3 is usual in high school and would be Cory's call through APPROACH.
- **J3.** 9 to 12 For the lead 4, two levels in one room. The frame's pick (each level keeps its units and ids, shared
  openers and critique days marked) is sound; it is a scope question for Cory.
- **J4.** Lawrence's series in grade 3 and again in Level 1 (S1 keeps both). Reasonable reviewers may want one; the
  Level 1 entry rule and the designed revisit in unit 12 make the pair defensible.

## The lead's open items, confirmed

| Line | Verdict | What it should be |
|---|---|---|
| VA:Pr5.1.4a (1096) | Wrong enough to fix: "times" misleads and indoor or outdoor and physical or digital are lost | "Analyze showing and protecting art indoors or out, temporary or permanent, physical or digital." |
| VA:Re8.1.5a (1145) | Incomplete: visual elements missing | "Find an artwork's ideas and mood from form, structure, context, subject, visual elements, media." |
| VA:Cn10.1.7a (1171) | Incomplete: "visual" and "make or experience" lost | "Alone or together, visually record where and when people locally make or see art." |
| VA:Cr1.2.7a (1027), new | Drifted: criteria became guidelines (S2) | "Set criteria a work must meet for its aim, and let them steer making." |

Each replacement is 14 words or fewer; the two proposed in the frames were 15. Also still open from the pilot and
confirmed: docs/ADOPTION-BAR-SUBJECTS.md line 568 still lists "Owed: the standards gate (later.csv L83); load the 63
strand ids" (both done 2026-11-21); STANDARD.md 3.4's Pending row for visual arts 6 to 8 and media arts.

## Row changes: landed

Checked in data/progressions/arts.csv: va-g5-design reads "labeled"; va-g8-craft reads "open license"; va-g4-museum
carries VA:Cn10.1.4a and its tradition piece; va-g3-show names the class web page; va-g6-design names the collection of
ideas with the public or invented option; va-g7-design names the visual record with no faces; the four 6 to 8 and one
9 to 12 cross_subject cells match the frames' Cross-subject sections, and 3 to 5's two (ela:SL.3.1, math:4.G.A.3).
Every hands_on and model_out cell matches the frames' seam and model tables (12 models into grade 6, 13 into Level 1,
13 ending in Level 4). Not yet landed: the two row edits in M2 and the one in S2 (new here).

## Data checks (the brief's list)

| Check | 3 to 5 | 6 to 8 | 9 to 12 |
|---|---|---|---|
| Owned skills, each in one unit | Met (24 rows) | Met (24) | Met (24 plus 4 Level 4 rows) |
| Standards in full | Met (45; three taught past a narrow line, M2) | 44 in full; VA:Cr1.2.7a in part (S2) | Met (45; Level 4 assesses `.IIIa` again) |
| Units and reasons, order | Met | Met (cave art after social studies grade 6 unit 2; scale after math grade 7 unit 1) | Met |
| Days fit the year | 64 a year, 60 in units; shares follow the ids | Same | 160 a level, 156 in units; bridge 12 (7.5 percent) |
| Seams | K to 2 handed-on table matches row for row; hands on to 6 to 8 match | Both ends match | Matches 6 to 8 (but the note is stale, M3) |
| Cross-subject | ELA grade 3 unit 1 before unit 2; math grade 4 unit 9 a year back | All four leans taught first | ELA grade 11 and 12 argument units come first |
| Stale notes | M3 | M3 | M3 |

## Lens checklist (course frame layer)

| Lens line | Verdict |
|---|---|
| Four processes every year, most units three | Met in all three |
| A grade's ids in its own year; a level not tied to a grade | Met |
| Works from many traditions and centuries, with setting | Met within each year; missed across bands (S1) |
| Technique harder across units and years | Met; the group mural returns in 6 to 8 unit 11 with the same artist (fixed by S1; unit 11 names what is harder: a joined wall composition on a shared grid) |
| No daily period in K to 8 | Met (two 40-minute sessions; once-a-week path) |
| A showing in every unit | Met |
| Technique taught before making; discipline words taught | Met |
| Critique protocol and revision after feedback | Met |
| End-of-unit assessment is making, showing or response, not a vocabulary quiz | Met |
| Our own questions; no coalition essential questions or cornerstone tasks | Met |
| Room, set-up and clean-up minutes, cheap stand-ins | Met, except m4 and M1 |
| Safety (blades, heat, dust, fumes) | Met; J2 open |
| No student performs alone without another way | Not applicable at this layer (group and wall showings) |
| "Respond" used only for respond days | Met (Level 4 critique as respond day follows APPROACH) |
| Five disciplines not planned as one | Met; same-band repeats listed (M5) |

## After-core check-week clashes (for the lead's calendar pass; not counted)

From `frame.py calendar`, which now keys the arts by course. Visual arts checks stay off every core check week.

- Grade 3: week 18 (visual arts, physical education); week 26 (visual arts, computer science, dance, media arts,
  physical education, SEL).
- Grade 4: week 17 (visual arts, dance, media arts, theater); week 25 (visual arts, media arts).
- Grade 5: week 18 (visual arts, computer science, dance, ELD, media arts, physical education, theater); week 26
  (visual arts, dance, physical education, SEL).
- Grades 6, 7 and 8: day 83, week 17 (visual arts, dance, media arts, physical education, theater; health on day 84);
  week 32 is the finals week by rule.
- 9 to 12: weeks 16 and 32 in every level, shared with health and physical education; no stagger rule beyond finals.

## What is right and should not be touched

- The four-unit year with two threads a unit in the same slot each year, and 9 to 12's five-unit level with its
  bridge, review units and four Level 4 units, one per row.
- The id-by-id "End-of-unit evidence" lines, the course-level checks naming only the ids they test, and the carried,
  unscored product records ("no artifact is scored twice").
- The once-a-week arithmetic (32 sessions every year, check and respond weeks off the core weeks) and the 80-day
  short path (76 unit days plus 4 in every level).
- 6 to 8's show unit before the finals-week check, and 3 to 5's show unit after the year-end check: both follow the
  calendar rules for their grades.
- The sensitivity notes: looking only for sacred and ceremonial works, public or invented options marked the same, no
  task on a student's own body, culture or immigration status, the values rule on political works.

## What I could not judge, and what it would need

- The national time figures for 6 to 8 and 9 to 12: the visual arts educators' association's middle and high school
  opportunity-to-learn checklists (arteducators.org, 2025 postings) are downloads this job may not make. The lead
  reads them at source.
- Work facts and rights lines (dates, holdings, open-access status, whether a maker is living): from memory, for the
  swaps in S1 too. Each unit plan opens the item's own page, as the Base text bullets say.
- Whether each school's local museum or community source is open and free: the unit plans' candidates.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| The fourteen work swaps and the one-band rule in S1 | Range across a student's path; keeps each band's anchor work where its id uses it best | the three frames |
| Words lines for VA:Pr5.1.4a, VA:Re8.1.5a, VA:Cn10.1.7a, VA:Cr1.2.7a as in the table | Full action of the national standard in 14 words or fewer | data/standards/ncas-performance-standards-words.txt |
| Row edits va-g4-show, va-g5-judge, va-g7-ideas (M2, S2) | Rows match the standards and the frames | data/progressions/arts.csv |
| 6 to 8 unit 6 teaches criteria for an aim, LeWitt kept as a study | VA:Cr1.2.7a in full | 6 to 8 frame |
| 3 to 5 handling items observed on making days; check-day table for scribing only | One adult, one job; no paint on a check day | 3 to 5 frame |
| 9 to 12 show-unit weeks restated (24 or 25 to 32) | The days already say so | 9 to 12 frame |
| Minor wording and count fixes m1 to m9 | Consistency | the three frames; arts.csv (m7) |

## For Cory

- Money: the supplies ceilings. The frames' picks: $75 a class a year for 3 to 5 (as K to 2), $100 for 6 to 8 (its
  print year runs $100), $150 a class a level for 9 to 12. All optional beside a free path.
- Scope: two levels taught in one high school period (J3), and whether Levels 2 and 3 may use linocut with an adult
  rule, which would change APPROACH "Safe use" (J2).

## Sources

No source was opened for this read. The national visual arts performance standards (2014) and every work fact are
from memory, and are marked so above; the repository files listed under "What I read" are the evidence for every
other finding.
