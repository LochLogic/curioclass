# Science data gaps: expectation dimensions and unit anchors (2026-11-14)

Two gaps the science unit plan skeleton reported as missing data are closed: the three dimensions of every
performance expectation (new file data/standards/ngss-pe-dimensions.csv) and an "Anchor: ..." tail on every
science unit cell. Rights data was out of scope and is untouched.

## 1. Terms of use

- The PDF prints "(c) 2013 Achieve, Inc. All rights reserved" on every page, and says its core idea text is
  reproduced from the NRC Framework with the National Academy of Sciences' permission.
- The site's trademarks and copyright page
  (https://www.nextgenscience.org/ngss-trademarks-and-copyright/ngss-trademarks-and-copyright, read 2026-11-14)
  says the National Academies Press holds the copyright. Its public licence lets states, districts, schools,
  teachers and non-profit education entities copy, adapt and rearrange the standards without asking. The name is a
  WestEd trademark with strict use rules and a required disclaimer.
- Curio Class is not plainly one of those licensed users, so verbatim reuse is **not clearly allowed**. Following
  the repository's convention (data/standards/ma-hss-2018.txt: "ids and Curio Class's own words only"), the new
  file holds codes, the framework's category names, and our own lines only. Every line was checked by script
  against its source line: no run of 6 or more words is shared. The trademark is never named in student, teacher
  or family copy (the skeleton already says so).

## 2. Source used

The official DCI arrangements PDF, https://www.nextgenscience.org/sites/default/files/AllDCI.pdf, dated September
2017. This is the same document that data/standards/ngss-pes.txt names. It had been read into the session
scratchpad on 2026-11-13 and was parsed again from there. Nothing was downloaded into the repository or
S:\CurioClass-sources. The foundation boxes were read column by column, using the position of each line on the
page, so the practice, core idea and crosscutting concept columns do not run into each other. Each element was
tied to its expectations through the "(code)" tags printed after it.

The topic arrangement pages were not needed. The Massachusetts 2016 STE framework
(https://www.doe.mass.edu/frameworks/scitech/2016-04.pdf, saved to the scratchpad only) was read only for the
code comparison.

## 3. The CSV

data/standards/ngss-pe-dimensions.csv has a header comment block in the style of the other standards files,
then these columns:

| Column | Holds |
|---|---|
| pe | expectation code, exactly as in ngss-pes.txt (the join key) |
| dimension | `statement`, `clarification`, `boundary`, `sep`, `dci`, `ccc`, `eta`, `nos` |
| code | `SEP1` to `SEP8` (in the framework's order), the core idea code (`PS1.A`), or `CCC1` to `CCC7`; blank for statement, clarification, boundary, eta and nos |
| name | the practice, core idea or crosscutting concept name; for eta and nos, the connection heading |
| element | our own line |
| role | `secondary` where the core idea is marked secondary to that expectation, else blank |

Rows: 1,312 in all.

| dimension | Rows | Notes |
|---|---|---|
| statement | 208 | one per expectation |
| clarification | 98 | only where it narrows or sets the emphasis of what is taught; left out where it only lists examples |
| boundary | 124 | every assessment boundary, with the limits kept exact |
| sep | 210 | |
| dci | 354 | 51 of them secondary |
| ccc | 192 | |
| eta | 47 | Connections to Engineering, Technology and Applications of Science |
| nos | 79 | Connections to Nature of Science |

The eta and nos rows are printed in the boxes and kept so a unit plan can use them. They are not one of the three
dimensions.

**All 208 expectations are present**, and the file has no other codes. Every expectation has at least one sep row
and one dci row.

**Could not be completed as three dimensions:** 16 expectations have no ccc row, because their box lists no
crosscutting concept, or lists only an engineering or nature of science connection (an eta or nos row stands in):

- 1-PS4-4, 2-LS4-1, 3-PS2-4
- HS-ESS3-2
- the engineering expectations K-2-ETS1-1, K-2-ETS1-3, 3-5-ETS1-1 to 3-5-ETS1-3, MS-ETS1-1 to MS-ETS1-4 and
  HS-ETS1-1 to HS-ETS1-3

This is how the source prints them, not a parsing loss. Nothing else is missing.

**Massachusetts codes** (in the file header): of the codes the science frames cite, the Massachusetts 2016 STE
framework:

- **leaves out 23:** K-PS2-2, K-ESS3-1, 1-PS4-2, 2-ESS1-1, 2-LS2-2, 3-LS2-1, 3-PS2-2, 4-LS1-2, MS-PS1-3,
  MS-LS1-6, MS-LS1-8, MS-ETS1-3, MS-LS4-3, MS-LS4-6, MS-ESS1-3, HS-LS2-8, HS-LS4-6, HS-ESS2-7, HS-ESS3-4,
  HS-ESS3-6, HS-ESS1-6, HS-PS4-2 and HS-PS4-4;
- **folds 6 into other codes:** 2-LS2-1, MS-ESS3-3, HS-LS2-3, HS-LS4-3, HS-ESS1-3 and HS-ESS2-1;
- **splits 2:** MS-ESS1-1 into 1a and 1b, and HS-PS3-4 into 4a and 4b.

It also places middle school codes by grade, drops crosscutting concepts from its standards, and rewords many
shared codes. Whether that matters is the lead's call. It does not change this file, which follows the NGSS
wording.

## 4. Anchors added

The frames were checked with the skeleton's own rule (`\s+Anchor:\s*(.+)$` on the unit cell); `unit_skeleton.py
--list science` cannot help yet because no science course has a days.csv. Seven units had no "Anchor:" tail. Six
named a design problem or question under another label, and grade 4 unit 6 used "Anchor A:" and "Anchor B:",
which the parser does not read. Each got a tail at the end of its unit cell, and an "Anchor source:" sentence at
the end of the row's last column (Sensitive topics and teacher notes, where the high school frames already record
sources). Nothing else changed.

The OpenSciEd unit pages were read at openscied.org on 2026-11-14. The frames treat those units as reference
only, so only ideas were taken, never wording.

| Course, unit | Anchor (short) | Source | Why |
|---|---|---|---|
| Kindergarten 3, Ramps and targets | the ball rolls down the book ramp and stops short of the block tower or rolls past it; the class changes the ramp, push or a bumper until it knocks the tower down | our own, from the frame's design problem; idea of OpenSciEd K.3 Forces and Motion (ball to a target past an obstacle) | children can see it; it sets up defining the problem (K-2-ETS1-1) and testing whether a fix changes speed or direction (K-PS2-2) |
| Grade 1 6, Sending a message | one bell or whistle calls the whole playground in with no one shouting; design a light or sound signal across the playground or hallway | our own; idea of OpenSciEd 1.2 Waves: Sound (a clock tower bell as a signal) | everyday and puzzling (one sound reaches everyone); drives 1-PS4-4 straight after the sound and light units |
| Grade 2 3, Materials and their best uses | a paper doll in a paper hat comes back soggy from a drizzle; test rubber, wool, foil, cloth and plastic for the best hat | our own, from the frame's design question; OpenSciEd 2.2 (designing a toy) read and not used, since it leans on 2-PS1-3 | classify materials by properties (2-PS1-1) and pick the best one from test data (2-PS1-2) |
| Grade 4 6, Senses and structures | the cat at night (shining eyes, sure feet, a bolt at an unheard sound) and the white flower in colored water | the frame's own anchors A and B, named on one line so the skeleton reads them; OpenSciEd 4.4 (flying squirrels) read and not used, since the unit's question is built on the cat and the plant | light into the eye (4-PS4-2), senses to brain to response (4-LS1-2), structures for survival (4-LS1-1) |
| Biology 9, Designing for a river | after the Elwha River dams came down (2011 to 2014), salmon returned above the old dam sites within a few years and freed sediment built new beach and delta | our own, the case the design problem already names; federal river science and park records (public domain); OpenSciEd B.1 read and not used | measured change after an engineering choice; drives criteria and trade-offs (HS-ETS1-1, HS-ETS1-3) and judging solutions to human impact (HS-LS2-7, HS-ESS3-4) |
| Chemistry 7, Design an energy device | a foil-lined box with a clear lid in the sun melts cheese while a dish of water beside it stays barely warm | our own, the frame's solar oven problem; OpenSciEd P.1 (a winter grid failure) carries HS-PS3-3 but was not used, since it is an electricity supply problem and not a heating device | puzzling (same sunlight, very different warming); drives designing a device that converts energy (HS-PS3-3) by breaking it into smaller problems (HS-ETS1-2) |
| Physics 2, Softer landings | a crash-test car front crumples while the dummy is almost unhurt; road deaths per mile fell for decades as crumple zones and airbags came in | idea of OpenSciEd P.3 Collisions and Momentum (crash data patterns); federal road safety records (public domain) | a crushed part protecting a person is puzzling; drives designing a device that lowers collision force by stretching collision time (HS-PS2-3); the notes column already lists crash-test numbers as the no-kit path |

`python -X utf8 scripts/frame.py check` passes for all 12 science frames (0 failures), and every science unit cell
now ends in a readable "Anchor:" tail.

**For the lead:** the high school frames put "Anchor: ..." before the compelling question. The skeleton's greedy
regex therefore reads the question into the anchor and leaves the question empty, in all 28 high school units
that already had anchors. The three high school tails added here sit at the end of the cell, so they read cleanly.
A fix would be in the skeleton (stop the anchor at the first sentence before a question) or in the frames; that is
not in this job.

## 5. What the skeleton's science adapter must change

Today, std_text() gives science only ngss-pes.txt (codes only), so field 1 asks the writer for each expectation's
line, and field 2 prints a three-dimension table of MARK cells. To read the new file:

1. **Load it** as data/standards/ngss-pe-dimensions.csv: skip the lines that start with `#`, then
   `csv.DictReader` (the same pattern as `focus_weights()` uses for ccss-math-focus.csv). **Join key: `pe`**, which
   equals the codes in `days.csv` `codes` and in the frame's Owned standards column.
2. **Field 1 (statement):** for a science code, use the row with `dimension == 'statement'` (`element`) as the
   expectation's line, and drop the "no statement on file" MARK. Append the `boundary` row's `element` (and the
   `clarification` row's `element` where one exists) as "Limit:" and "Emphasis:" lines, in place of the request to
   write the assessment boundary.
3. **Field 2 (three-dimensions table):** for each expectation, fill the columns from the rows where `dimension` is:
   - `sep`: `name` and `element`
   - `dci`: `code`, `name` and `element`, with "(secondary)" when `role == 'secondary'`
   - `ccc`: `name` and `element`

   Join several rows of one dimension with "; ". Where an expectation has no `ccc` row, print the `eta` or `nos`
   row's `name` with "(connection, no crosscutting concept)", not a MARK. The `eta` and `nos` rows can go on a
   "Connections" line under the table.
4. **Keep** the unit-level "Practices: ... Crosscutting: ..." list from the frame's C3 column beside the table.
   It is the unit's own focal list, and it may differ from the box elements.
5. **SUBJECT_STD['science']** can stay as it is (ngss-pes.txt remains the code list). The new file is a second
   loader, not a replacement.

## Files

- New: data/standards/ngss-pe-dimensions.csv
- Edited (one unit row each: the unit cell tail and the last column's source sentence):
  - docs/courses/science-kindergarten/frame.md (unit 3)
  - docs/courses/science-grade-1/frame.md (unit 6)
  - docs/courses/science-grade-2/frame.md (unit 3)
  - docs/courses/science-grade-4/frame.md (unit 6)
  - docs/courses/biology/frame.md (unit 9)
  - docs/courses/chemistry/frame.md (unit 7)
  - docs/courses/physics/frame.md (unit 2)
- Unchanged: data/standards/ngss-pes.txt, every script and brief.
