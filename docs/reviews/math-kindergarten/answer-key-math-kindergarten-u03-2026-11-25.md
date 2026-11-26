# Answer-key read: kindergarten math, unit 3

Job 029, kit 14. Requested report date: 2026-11-25. Actual read and fixes: 2026-11-26. Days 45 to 63.

## Verdict

**Fail for the cold-read protocol; content repaired.** Three ambiguous assessment prompts and one related repair-card/key mismatch were fixed, but an initial extraction exposed samples before my answer record, so this report cannot certify a fully independent cold solve.

## What I studied

- `docs/pipeline/briefs/sensitivity-read.md`, sections 1 to 3: solve first, compare, map evidence to the standard, disclose my errors.
- `docs/pipeline/briefs/section-write.md`, rules 7 to 10, and `docs/courses/math-kindergarten/DEFAULTS.md`: one spoken ask, counted turns, the single marking scale, and one actor per scene. The course default is 60 minutes; the older brief's general 20 to 30 minute note does not replace that course default.
- `data/plans/math-kindergarten/items.csv`, filtered to the named days and assessment kinds, with answer fields initially omitted: 159 rows. My initial extraction mistakenly retained `samples` and `steps`, discussed below.
- The named unit's original child cards and physical-piece masters: traced boundaries, compared endpoints, checked joins and area, and distinguished supplied apparatus conditions from observable results. Every assessment id was listed before opening the private answer-key files.
- `_scratch/l87/tmp/math-kindergarten-key-u3/cold-answers.json`: my answer and method for each of the 159 ids, recorded before the explicit answer-column/private-key comparison, but after the accidental sample exposure. Renewed solutions are in `re-solved.json`; the additional repair solution is in `repair-resolve.json` in the same folder.
- The source pages listed below were opened after the solution record, for content and apparatus checks rather than as outside study before solving.

## Items read

**159 assessment rows: 18 exits, 0 readiness, 141 end rows.** The end rows comprise 60 position observation rows, 40 shape-name observation rows, 15 single-attribute conference rows, 10 heft/capacity conference rows, 10 paper/build/draw/comparison/composition rows, and six teacher-only retained-record summaries. Repeated rows fund different roster collections; they are not 141 new tasks for one child. All 159 are teacher judged. Read and compared all 148 corresponding wrong-answer rows, including their letters and notes. Also checked the related repair item `s03-F58-D` after finding its picture mismatch.

The 159 corresponding private-key blocks agree with the data on stems, answers and samples before the fixes. Their look-fors also agree after removing only two harmless path-metadata sentences about paper responses. Repeated F1/F2 rows were compared individually against their appropriate prototype for stem, answer, samples, standard and judgment type; there were no differences.

## Faults and fixes

| Item or related piece | Kind | What was wrong | Fix made | Stage that made it |
|---|---|---|---|---|
| `s03-X48` | ambiguous | ?Show one way these shapes are different.? permits a true answer such as one is tilted, while the key requires a side-length contrast. | Spoken/print stem now says ?Tell one way the side lengths are different.? The key accepts a correct contrast within each figure or between their sides. Updated samples and wrong-answer notes keep an orientation-only response descriptive rather than assigning B without evidence. | section plan: field 3 supplied the broad stem and narrow key |
| `s03-X50` | ambiguous | ?Tell about this shape.? permits a correct feature-only description, while the key expects the name triangle and the day checks naming. | Spoken/print stem now says ?What is this shape called?? The key requires the name, treats boundary marks as supporting evidence, and requires no second spoken description. Updated the C note. | section plan: field 3 supplied the vague stem |
| `s03-X58` | ambiguous | ?Tell about the shape you found here.? does not identify the flag rather than the clearly pictured rectangular doorway; the key also bundled name, features and location. | Spoken/print stem now says ?What shape is the hanging flag?? The key accepts triangle, keeps feature/location descriptions optional, and distinguishes a doorway response from rejecting a narrow triangle. Updated the C note. | section plan: field 3 supplied the untargeted stem and bundled look-for |
| `s03-F58-D`, `u03-4/repair-58-D.md`, related to the day 57 handback | key | ?Join the opening in this five-edge drawing.? was illustrated by a three-edge open rectangular path; its data/private key said to close a four-sided frame. | Supplied a fresh irregular path with five drawn edges and one gap. The missing sixth edge closes the boundary. Updated the repair answer, look-fors, samples and matching private-key block. D remains the valid error for calling an open boundary closed. | data: mismatched print drawing and copied repair key |

Fault counts: **ambiguous 3; key 1; off-goal 0; rule4 0; needs-info 0; two-asks 0; key-on-child-page 0.** The key fault is the additional repair, not an incorrect numerical answer among the 159 assessment rows. No ids, collection days, goals or standard codes changed. Four items.csv rows and three wrongs.csv notes changed through `rows.py`, each after its dry run. Three exit print cards, three existing private-key files, and the related repair picture changed. No new item or handback row was needed: the existing 48 to 49, 50 to 51, 57 to 58 and 58 to 59 Return routes already carry these ids.

## Renewed solutions for changed work

| Item | My answer after the change, before the revised key comparison | Method |
|---|---|---|
| `s03-X48` | All square sides are equal. The rectangle has two longer and two shorter sides. Its long side is longer than a square side; its short side is shorter. | Inspect the existing 105-by-105 square and 235-by-85 rectangle. 235>105>85. Turn does not alter any side length. |
| `s03-X50` | Triangle. | The reserved outline consists of three joined straight segments and three corners; rotate mentally without changing those features. |
| `s03-X58` | Triangle. | Select the hanging flag explicitly identified by the new stem, not the doorway. Its three outer straight edges meet in three corners. |
| `s03-F58-D` | Join the two free endpoints with a sixth edge; the boundary is then closed. | The replacement path has five segments and six marked corners. The endpoint segment closes it without reusing exit 57's boundary. |

All renewed solutions agree with the revised keys. The 105-by-105 square and 235-by-85 rectangle in exit 48 permit both the within-figure equal/unequal comparison and the between-figure longer/shorter comparison. These are drawing coordinates used by this reader, not numerical measurements children must know.

## Goal, access, one-ask and marking checks

The retained assessment covers K.G.A.1 positions and environmental shapes, K.G.A.2 names across size and turn, K.G.B.5 construction/drawing, K.G.B.6 composition, and K.MD.A.1/A.2 measurable attributes and direct comparisons. Informal feature probes such as days 46 and 48 support the geometry sequence; they do not, by themselves, establish the entire shape-naming standard. The separate F2 observations carry all five names across their two variants.

The altered day 48 prompt keeps its comparison goal and taught side-length language, explicitly modeled in day 48. Days 50 and 58 now elicit the intended shape name with one spoken ask. Existing boundary marks are evidence/access, not an additional oral question. No child is required to read a label or independently read the stem. Blank `path` fields are intentional for the named drawing/marking responses, as their administration notes explain. The longest actual child assessment stem is nine words, and all named shared child sheets fit the course's 60-word reading cap in the gate output. The six day 63 summary stems are teacher records, not read to children.

F3 construction and drawing, F4 filling and seam tracing, and F5's three attribute proposals already have separate ids and separate spoken turns. Exit 61 is one integrated request for two ways to compose the same whole, directly checking its day's goal, rather than two unrelated questions. Its two products are not supplemented by another exit interview. No new split is required.

Turn arithmetic checked: F1 is 30 children times six 45-second responses, 135 heard minutes, distributed as eighteen cells plus 1.5 setup minutes on each of ten days. F2 is 30 times five 45-second responses, 112.5 heard minutes, plus the named resets over eight days. A measurement conference is three 45-second attribute asks, 45 seconds heft, 75 seconds capacity and 15 seconds reset, 4.5 minutes per child; six children take 27 minutes. The ordinary six exit responses use 4.5 minutes inside the eight-minute block. Marking remains shown, shown with help, not yet seen; unheard words are not inferred from marks. A square is also a rectangle; broad correct classification is not evidence of error B, which requires an observed rejection due to turning.

## Rule 4

Compared the assessment cards, reserved physical masters, practice and repair pieces, all other unit 3 item cases, and the relevant teaching/model blocks. No reserved SVG is identical to a teaching/practice/repair SVG. That exact-match check supplements, rather than replaces, the case comparison: the badge/folder scene, concealed open strip path, tilted-square choices, reserved side comparison, narrow sort target, thin triangle, long rectangle, strip-built triangle, toy wagon, ribbon pair, ring/star heft envelopes, bowl/pot transfer, built six-edge frame, hallway flag, unequal-rectangle join, irregular-hexagon choices, two-way square fill and turned partner composition stay distinct from taught examples. F1/F2 displays are covered assessment masters, not practice. Later retention/summary of their original evidence does not introduce a second scored case.

Filtered ledger commands were run for `shape`, `tub` and `length` with `--before math-kindergarten`. The script includes the named course itself; kindergarten has no lower math grade in this ladder. Its returned current-course cases were not treated as lower-grade reuse. No whole ledger was requested. Generic shape names and methods are reused as taught concepts; original cases and pictures remain reserved.

## Facts, sources and safety

There is no item fact about a real person, place, event or species. `sources.csv` row `s03-original` explicitly identifies these contexts and quantities as invented and identifies actual weight/capacity relations as preconditions to test before class. Counts of sides, equality of edges, closure, joins and triangle tiling were checked directly from the original vector geometry. For example, four 92.5-square pieces have the area of the 185-square outline, and two triangles with legs 360 and 180 fill the 360-by-180 rectangle along a diagonal. Children need none of those coordinate numbers.

Opened public preparation pages already recorded in these sources.csv rows on 2026-11-26:

| Source row | Opened page | What I checked |
|---|---|---|
| `s03-base-3-13` | [Position and shape descriptions](https://im.kendallhunt.com/k5/teachers/kindergarten/unit-3/lesson-13/preparation.html) | Spoken positional descriptions and partner shape work. |
| `s03-base-3-1` | [Informal shape descriptions](https://im.kendallhunt.com/k5/teachers/kindergarten/unit-3/lesson-1/preparation.html) | Early feature language without a formal definition requirement. |
| `s03-base-3-2` | [Matching shapes](https://im.kendallhunt.com/k5/teachers/kindergarten/unit-3/lesson-2/preparation.html) | Shape class is retained across size and orientation. |
| `s03-base-3-5` | [Circles and triangles](https://im.kendallhunt.com/k5/teachers/kindergarten/unit-3/lesson-5/preparation.html) | Naming, informal attributes, examples and nonexamples. |
| `s03-base-3-6` | [Rectangles and squares](https://im.kendallhunt.com/k5/teachers/kindergarten/unit-3/lesson-6/preparation.html) | Squares are special rectangles; side lengths may be equal, longer or shorter. No recited definition required. |
| `s03-base-3-7` | [Building from components](https://im.kendallhunt.com/k5/teachers/kindergarten/unit-3/lesson-7/preparation.html) | Build shapes and compare lengths by lining up endpoints. |
| `s03-base-3-8` | [Drawing shapes](https://im.kendallhunt.com/k5/teachers/kindergarten/unit-3/lesson-8/preparation.html) | Approximate drawings can preserve shape attributes. |
| `s03-base-3-9` | [Environmental shapes](https://im.kendallhunt.com/k5/teachers/kindergarten/unit-3/lesson-9/preparation.html) | Name shapes found in the school environment. |
| `s03-base-3-10` | [Composing shapes](https://im.kendallhunt.com/k5/teachers/kindergarten/unit-3/lesson-10/preparation.html) | Whole-side joins form larger shapes. |
| `s03-base-3-11` | [Same shapes](https://im.kendallhunt.com/k5/teachers/kindergarten/unit-3/lesson-11/preparation.html) | Turn and size do not change shape class. |
| `s03-base-3-12` | [Multiple compositions](https://im.kendallhunt.com/k5/teachers/kindergarten/unit-3/lesson-12/preparation.html) | Different pieces can make the same larger shape. |
| `s03-base-3-14` | [Shapes in art](https://im.kendallhunt.com/k5/teachers/kindergarten/unit-3/lesson-14/preparation.html) | Describing components and composing pictures. |
| `s03-base-7-8` | [Weight comparison](https://im.kendallhunt.com/k5/teachers/kindergarten/unit-7/lesson-8/preparation.html) | Holding actual objects is the comparison evidence; size alone cannot establish weight. |
| `s03-base-7-9` | [Capacity comparison](https://im.kendallhunt.com/k5/teachers/kindergarten/unit-7/lesson-9/preparation.html) | Capacity is distinct from height; containers, water and a tray support direct comparison. |

These rows already say `checked: 2026-11-26`, the actual date, rather than the requested generation-date stamp `checked: 2026-11-25`. I did not backdate them or edit sources.csv, which is outside this job's write scope. The two remaining unit 3 base preparation rows are sequence/planning references, not additional factual premises used in these item solutions.

**Judged, not physically verified:** actual heft differences, about-same felt weight, capacity outcomes, tactile accessibility, print handling and classroom timings. Retain all pretests. A picture cannot establish the star's weight or the bowl's capacity. The teacher must secure light fillings, keep pieces large and out of mouths, adult-cut the paper, use unbreakable vessels and small room-temperature water amounts over a tray, stop at the rim, and dry spills immediately. Where actual vessels or a valid pretest are absent, keep the component not yet seen. About-same heft is not a claim of exact measured equality. No body comparison or personal family disclosure is required. Invented partner Rin is the single actor in the composition scene.

No assessment key was found on a child-held answer sheet. Reserved preparation masters that state apparatus conditions are adult setup materials. Existing private `teacher-key.md` pieces are already named in Before class and explicitly kept private. No new teacher-key piece or day-page edit was required.

**Browser check:** none. Every page attempted opened; no refused page was retried.

## Section plan field 3 lines needing the data writer's sync

Do not edit these plans in this job. The changed data is the assessment source of truth.

1. `docs/courses/math-kindergarten/u03-1.md`, E48: replace ?Show one way these shapes are different.? with ?Tell one way the side lengths are different.? Update its accepted sample to include correct within-figure or between-side length contrasts; an orientation-only comment is not the requested evidence.
2. `docs/courses/math-kindergarten/u03-2.md`, E50: replace ?Tell about this shape.? with ?What is this shape called?? Its independent spoken evidence is the name triangle; extra spoken features are optional.
3. `docs/courses/math-kindergarten/u03-4.md`, E58: replace ?Tell about the shape you found here.? with ?What shape is the hanging flag?? Require the indicated shape name, rather than a mandatory bundle of name, features and position.
4. Pre-existing mismatch, same file, E60: its not-yet-seen sample says an open trace is D, while current items.csv samples and wrongs.csv give the five-sided selection as unclassified x. Sync that line to the data and do not force D on an unrelated match error.
5. Pre-existing mismatch, `docs/courses/math-kindergarten/u03-5.md`, E61: ?six explain unchanged outside? conflicts with the data's explicit no-extra-exit-oral-question instruction. Keep the later funded practice descriptions on their separate case, as the field's budget already says.

## My own errors and limits

1. The first supposedly key-free extraction omitted `answer` but accidentally retained `samples` and `steps`. It requested those fields for all 159 rows; the returned display was truncated, but samples for early exits were visibly exposed. Some subsequent physical-packet preparation prose also supplied pretest outcomes before my solution record. I cannot undo that exposure or claim these are fully cold answers. The saved solutions predate the explicit answer-column/private-key comparison, not all possible key exposure. A fresh reader is required for the independent cold-read requirement.
2. My provisional F1 answer for the beside cell identified the hexagon beside the triangle. The administration indicates the left triangle beside the hexagon. The relation was right, but I had reversed the indicated target and reference before reading the administration. This affects `s03-F1-talk-60` and the nine `s03-F1-48-3` through `s03-F1-56-3` collection rows; it is my target-mapping error, not a key fault.
3. My initial F1-paper interpretation allowed any shapes marked for later discussion. The administration requires finishing the retained marks for the six already observed relationships. That was my incomplete reading of its collection role, not a wrong geometry key.
4. I first tried DEFAULTS.md at the repository root; it is the course file under docs/courses/math-kindergarten/. I corrected the path before making content judgments.

No arithmetic correction to my solutions was needed. Broadly correct provisional responses and physical-outcome conditions were not counted as key faults. No additional worker was used.

## Could not settle and left

- Full cold independence remains unmet for the reason above. The content fixes are usable, but this report is not an unqualified cold-read completion.
- Actual apparatus, access and class timing need the teacher's named pretests; no physical classroom trial was performed.
- The five section-plan field 3 synchronizations are listed for the data writer, outside this job's edit scope.
- Source rows retain their actual checked date of 2026-11-26. No source row was changed.
- Existing course-wide gate debt is not reclassified as a template exception. The six teacher-only day 63 summaries explain why the gate's student-page requirements need lead review, but this job does not change their type or add a fake child task.
- Helper and dependency files remain only in `_scratch/l87/tmp/math-kindergarten-key-u3/`. No stray empty folder was observed or removed.

## Initial answer and method record

This table preserves my recorded answers, including the provisional F1 errors just disclosed. Identical answer/method records are grouped only for space; every assessment id is listed. It does not replace the independence limitation.

| Item ids | My recorded answer | My method |
|---|---|---|
| `s03-X45` | Behind the folder from the arrow side. | The opaque folder occludes the lower badge. |
| `s03-X46` | Three straight sections with corners and an open join; not a closed triangle. | Trace the tactile path and detect the gap. |
| `s03-X47` | The larger upright square. | Count four equal sides and right corners regardless of turn. |
| `s03-X48` | Square has all sides equal; nonsquare rectangle has long and short sides. Also different orientation or size is literally valid. | Compare visible features; broad wording permits several differences. |
| `s03-X49` | Under the triangle picture. | Target is closed with three straight sides despite being narrow and sideways. |
| `s03-X50` | Triangle; three joined straight sides. | Count boundary segments, ignore turn and proportions. |
| `s03-X51` | Rectangle. | Four right corners, unequal adjacent side lengths. |
| `s03-X52` | A closed triangle with the three supplied strips. | 190+120>190; arrange three endpoints into a closed boundary. |
| `s03-X53` | Length, height, weight or capacity, one attribute. | End-to-end/upward gesture, lifting or marking inside identifies a measurable attribute. |
| `s03-X54` | Align one pair of ends; wavy-edged ribbon is longer. | Straighten without stretching and compare far ends, 270 versus 220 drawing units. |
| `s03-X55` | Cannot infer weight from picture; conditional on heft, star heavier and ring lighter. | Swap hands and compare actual sealed objects; preparation states the empirical result. |
| `s03-X56` | Cannot infer capacity from silhouettes; conditional on observed transfer, low wide bowl holds more. | Fill bowl and transfer to empty pot; stop at rim with water remaining in bowl. |
| `s03-X57` | Closed six-sided outline with two long and four short slanted sides. | Copy frame boundary, retain closure and side structure. |
| `s03-X58` | Door is rectangular; hanging face is triangular. | The prompt does not identify one target; either visible shape supports description. |
| `s03-X59` | One long rectangle from two unequal rectangles joined on the matching short full edges. | Join 70-unit edges: 180+240 long by 70 wide. |
| `s03-X60` | First choice to the right of target, the turned larger hexagon. | Six sides retained by rotation and scaling; alternatives have five and four. |
| `s03-X61` | Four small squares in a 2-by-2 array, or two triangles meeting along a diagonal. | 4*(92.5 squared)=185 squared; each triangle is half a 185 square. |
| `s03-X62` | A nonsquare rectangle, a square and a triangle. | Trace internal seams of supplied composite; printed image is not necessarily a partner product. |
| `s03-F1-paper` | Any marked display shapes supported by later descriptions; no unique selection. | Identify indicated target and reference from the reserved display; above/below from vertical order, front/behind from occlusion and viewing arrow. Beside and next to are interchangeable. |
| `s03-F5-paper` | Any three distinct measurable attributes among length, height, weight and capacity. | Point end to end, bottom to top, lift, or indicate interior; repeated prompts require a different attribute, any valid order. |
| `s03-F1-talk-58`, `s03-F1-48-1`, `s03-F1-49-1`, `s03-F1-50-1`, `s03-F1-51-1`, `s03-F1-52-1`, `s03-F1-53-1`, `s03-F1-54-1`, `s03-F1-55-1`, `s03-F1-56-1` | Above shelf: clock circle. | Identify indicated target and reference from the reserved display; above/below from vertical order, front/behind from occlusion and viewing arrow. Beside and next to are interchangeable. |
| `s03-F2-talk-58`, `s03-F2-51-1`, `s03-F2-52-1`, `s03-F2-53-1`, `s03-F2-54-1`, `s03-F2-55-1`, `s03-F2-56-1`, `s03-F2-57-1` | Circle: curved closed boundary, no corners. | Track boundary sides/corners across different sizes and rotations in reserved pair panels. |
| `s03-F5-talk-58`, `s03-F5-talk-59`, `s03-F5-talk-60`, `s03-F5-talk-61`, `s03-F5-talk-62` | One measurable attribute: length. | Point end to end, bottom to top, lift, or indicate interior; repeated prompts require a different attribute, any valid order. |
| `s03-F6-weight-58`, `s03-F6-weight-59`, `s03-F6-weight-60`, `s03-F6-weight-61`, `s03-F6-weight-62` | About the same, conditional on actual heft. | Heft both, swap hands; size alone gives no weight evidence. |
| `s03-F6-capacity-58`, `s03-F6-capacity-59`, `s03-F6-capacity-60`, `s03-F6-capacity-61`, `s03-F6-capacity-62` | Valid transfer either direction; short wide vessel holds more if the pretest outcome occurs. | Full smaller source leaves room in larger destination, or larger source retains water at smaller rim. Adult pours safely. |
| `s03-F1-talk-59`, `s03-F1-48-2`, `s03-F1-49-2`, `s03-F1-50-2`, `s03-F1-51-2`, `s03-F1-52-2`, `s03-F1-53-2`, `s03-F1-54-2`, `s03-F1-55-2`, `s03-F1-56-2` | Below shelf: square. | Identify indicated target and reference from the reserved display; above/below from vertical order, front/behind from occlusion and viewing arrow. Beside and next to are interchangeable. |
| `s03-F2-talk-59`, `s03-F2-51-2`, `s03-F2-52-2`, `s03-F2-53-2`, `s03-F2-54-2`, `s03-F2-55-2`, `s03-F2-56-2`, `s03-F2-57-2` | Triangle: three straight sides. | Track boundary sides/corners across different sizes and rotations in reserved pair panels. |
| `s03-F1-talk-60`, `s03-F1-48-3`, `s03-F1-49-3`, `s03-F1-50-3`, `s03-F1-51-3`, `s03-F1-52-3`, `s03-F1-53-3`, `s03-F1-54-3`, `s03-F1-55-3`, `s03-F1-56-3` | Beside triangle: six-sided shape. | Identify indicated target and reference from the reserved display; above/below from vertical order, front/behind from occlusion and viewing arrow. Beside and next to are interchangeable. |
| `s03-F2-talk-60`, `s03-F2-51-3`, `s03-F2-52-3`, `s03-F2-53-3`, `s03-F2-54-3`, `s03-F2-55-3`, `s03-F2-56-3`, `s03-F2-57-3` | Square: four equal sides and right corners. | Track boundary sides/corners across different sizes and rotations in reserved pair panels. |
| `s03-F1-talk-61`, `s03-F1-48-4`, `s03-F1-49-4`, `s03-F1-50-4`, `s03-F1-51-4`, `s03-F1-52-4`, `s03-F1-53-4`, `s03-F1-54-4`, `s03-F1-55-4`, `s03-F1-56-4` | Next to circle: triangle. | Identify indicated target and reference from the reserved display; above/below from vertical order, front/behind from occlusion and viewing arrow. Beside and next to are interchangeable. |
| `s03-F2-talk-61`, `s03-F2-51-4`, `s03-F2-52-4`, `s03-F2-53-4`, `s03-F2-54-4`, `s03-F2-55-4`, `s03-F2-56-4`, `s03-F2-57-4` | Rectangle: four right corners with long and short sides. | Track boundary sides/corners across different sizes and rotations in reserved pair panels. |
| `s03-F1-talk-62`, `s03-F1-48-5`, `s03-F1-49-5`, `s03-F1-50-5`, `s03-F1-51-5`, `s03-F1-52-5`, `s03-F1-53-5`, `s03-F1-54-5`, `s03-F1-55-5`, `s03-F1-56-5` | In front of book: square. | Identify indicated target and reference from the reserved display; above/below from vertical order, front/behind from occlusion and viewing arrow. Beside and next to are interchangeable. |
| `s03-F2-talk-62`, `s03-F2-51-5`, `s03-F2-52-5`, `s03-F2-53-5`, `s03-F2-54-5`, `s03-F2-55-5`, `s03-F2-56-5`, `s03-F2-57-5` | Hexagon: six straight sides. | Track boundary sides/corners across different sizes and rotations in reserved pair panels. |
| `s03-F2-paper` | Pair the two circles, triangles, squares, nonsquare rectangles and six-sided polygons. | Track boundary sides/corners across different sizes and rotations in reserved pair panels. |
| `s03-F3-build` | Closed square using four equal strips. | Coaster has four equal 105-unit sides and right corners; preserve boundary. |
| `s03-F3-draw` | Closed triangle matching tent face. | Trace the three outer sides; inner tent line is not another outer edge. |
| `s03-F6-length` | Wave strip longer than dotted strip. | Align near ends: 280 versus 210 drawing units. |
| `s03-F6-height` | Ring tower taller than striped tower. | Common bottoms: 145 versus 115 drawing units. |
| `s03-F6-equal` | Same length. | Align ends of two 190-unit strips, with orientation removed. |
| `s03-F4-fill` | Two triangles cover the nonsquare rectangle without gaps or overlap. | Each right triangle has legs 360 and 180; join hypotenuses. |
| `s03-F4-seam` | One corner-to-opposite-corner diagonal. | Trace shared hypotenuse after filling, either diagonal orientation is valid. |
| `s03-A63-F1`, `s03-A63-F2`, `s03-A63-F3`, `s03-A63-F4`, `s03-A63-F5`, `s03-A63-F6` | No new student response: retain the separate earlier observation judgments. | Administrative summary, not a fresh assessment item. |
| `s03-F1-behind`, `s03-F1-48-6`, `s03-F1-49-6`, `s03-F1-50-6`, `s03-F1-51-6`, `s03-F1-52-6`, `s03-F1-53-6`, `s03-F1-54-6`, `s03-F1-55-6`, `s03-F1-56-6` | Behind box: circle. | Identify indicated target and reference from the reserved display; above/below from vertical order, front/behind from occlusion and viewing arrow. Beside and next to are interchangeable. |
| `s03-F5-talk-58-2`, `s03-F5-talk-59-2`, `s03-F5-talk-60-2`, `s03-F5-talk-61-2`, `s03-F5-talk-62-2` | Another distinct attribute: height. | Point end to end, bottom to top, lift, or indicate interior; repeated prompts require a different attribute, any valid order. |
| `s03-F5-talk-58-3`, `s03-F5-talk-59-3`, `s03-F5-talk-60-3`, `s03-F5-talk-61-3`, `s03-F5-talk-62-3` | A third distinct attribute: capacity. | Point end to end, bottom to top, lift, or indicate interior; repeated prompts require a different attribute, any valid order. |

## Gate evidence

Final completed gate: exit 0, **zero new failing findings**, nine new note lines. The baseline contained 304 failing lines; the final course run contained 302. Existing course debt remains, and no failure was relabeled as a template exception.

The direct launcher initially failed because this installation reports a directory as `sys.executable`. Running the unchanged gate through its actual executable then exposed missing `markdown` and `pypdf` dependencies. Both dependencies were installed only under this job's approved scratch folder. The successful baseline and final runs used that dependency folder through `PYTHONPATH` and corrected the executable path in memory before invoking the unchanged gate. No shared script or global installation changed, and no baseline was forced.

Print verification limit: the final gate reported that the three changed exit cards and the related repair card did not receive a new page count because the browser wrote nothing. Their word counts stayed low, but this is not a completed final print-layout check. This limitation remains for the lead.

Independent geometry, 159-id inventory and turn-arithmetic assertions also passed.

Actual final gate output, including every new line:

```text
12 gates run into build/gates/now-math-kindergarten; 2 exited non-zero: index-reports, plan-math-kindergarten
302 failing line(s) for math-kindergarten now, by gate and rule (--verbose lists them):
      70  lesson-math-kindergarten: belongs to day
      59  lesson-math-kindergarten: and more have the same
      59  plan-math-kindergarten: and more have the same
      30  lesson-math-kindergarten: end item is not on the student page,
      19  index-reports: orphans
      10  lesson-math-kindergarten: At home parts add to minutes; an assessment
      10  lesson-math-kindergarten: the exit ticket runs past its half page
       9  lint-math-kindergarten: style UK spelling
       7  lesson-math-kindergarten: and have the same stem
       7  plan-math-kindergarten: and have the same stem
       6  lesson-math-kindergarten: the parts after the warm-up do not add
       4  lesson-math-kindergarten: on an assessment day the At home path
       3  lesson-math-kindergarten: copied-exit
       1  lesson-math-kindergarten: day shows names which is neither an exit
       1  lesson-math-kindergarten: day shows phrase is not in the goal
       1  lesson-math-kindergarten: day the goal piece names no item in
       1  lesson-math-kindergarten: teacher words, student words , min, side more
       1  lesson-math-kindergarten: the student page prints to more than two
       1  plan-math-kindergarten: day shows names which is neither an exit
       1  plan-math-kindergarten: day shows phrase is not in the goal
       1  plan-math-kindergarten: day the goal piece names no item in
       1  plan-math-kindergarten: unit days and no mid-unit assessment
== lesson-math-kindergarten (8 new line(s), 0 failing); failing lines fell 205 -> 204
  note courses/math-kindergarten/u03-1/exit-48.md: blank, 12 words, student page page count not checked (Chrome wrote nothing), 0 failure(s)
  note courses/math-kindergarten/u03-1/teacher-key.md: story, 5219 words, 0 failure(s)
  note courses/math-kindergarten/u03-2/exit-50.md: blank, 9 words, student page page count not checked (Chrome wrote nothing), 0 failure(s)
  note courses/math-kindergarten/u03-2/teacher-key.md: story, 5461 words, 0 failure(s)
  note courses/math-kindergarten/u03-4/exit-58.md: blank, 10 words, student page page count not checked (Chrome wrote nothing), 0 failure(s)
  note courses/math-kindergarten/u03-4/repair-58-D.md: blank, 13 words, student page page count not checked (Chrome wrote nothing), 0 failure(s)
  note courses/math-kindergarten/u03-4/teacher-key.md: story, 5034 words, 0 failure(s)
  note lesson_course: 203 failure(s) in 160 day(s), 134 in day files
== plan-math-kindergarten (1 new line(s), 0 failing); failing lines fell 71 -> 70
  note math-kindergarten: 1891 items and 1972 wrong answers checked, 69 failure(s)
gate math-kindergarten against its baseline: 0 failing finding(s), 9 new note line(s)
```
