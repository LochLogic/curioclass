science-grade-8 s04 fix, 2026-11-17

Findings merged: 22 (assessment 8, sequence 9, sources 5; no fault was named by two lenses). Fixed: 20. Rejected: 0. Lead: 3 lines (two findings fully, one in part).

Held up per lens: assessment 8 of 8, sequence 7 of 9 fixed in the plan (sequence 1 and 2 are days.csv work), sources 5 of 5.

Fixes in docs/courses/science-grade-8/s04.md:
- Assessment 1: scoring paragraph now says P1 and P2 need prior feedback and revision, M1 and M2 are unaided sittings scored once on day 97, and the day 98 response does not change their carried scores.
- Assessment 2: M1 no longer states "most full moons have no eclipse"; the include-list is now "what happens at full moon and new moon, and the seasons at both sites". Six key components kept.
- Assessment 3: day 95 retrieval now uses a window pane, a foam mat and a curtain.
- Assessment 4: M2 now gives three labeled panels (X, Y, Z) with records; the key names panel X; look-for line updated.
- Assessment 5: P2 feedback in day 100's three-minute opening, revision in day 101's three-minute opening; day 102 revision removed. Two points kept.
- Assessment 6: T2 limitations component no longer includes presentation; T2 is scored from the written argument or transcript, spoken participation is an unscored note.
- Assessment 7: T4 crater is 400 kilometres (0.2 centimetre); key and look-for updated.
- Assessment 8: M1 seasonal stem now an unfamiliar planet with a different tilt, sites at 45 degrees north and south.
- Sequence 3: day 98 opening set to feedback response 5 min and two retrievals 5 min inside the 50.
- Sequence 4: day 102 row gives the split (3, P1 block 20, galactic context 24, ticket 3 = 50); P2 revision sits in day 101.
- Sequence 5: day 99 retrieval is a held ball and a falling ball; orbit case waits for day 100.
- Sequence 6: added a focal line for argument from evidence, systems and system models, structure and function with days.
- Sequence 7 (part): rotation stated for days 88 and 90 (two 20-minute rotations of three groups). The plan table already lists paper, tape markers and safety glasses; the generated supplies line is a skel block and was not edited.
- Sequence 8: handoffs line says the paired plot is mass against attraction (day 100) and no orbital-period plot is used.
- Sequence 9: added a day 96 boundary ticket in U3 (feedback only) and pointed the day 96 U6 row at it.
- Sources 1 and 2: bending, red-moon cause, resolution limits, gravity-inferred core and galactic motion marked "written from memory, to be checked by the expert read" (no new pages cited, since none could be checked here).
- Sources 3, 4, 5: no-kit tables stated as model output; Manhattan museum page limited to what it states; base third-party media not adapted.

Gate: python -X utf8 scripts/unitplan.py check science-grade-8 gives PASS for s04.md. The file arrived with CRLF line endings; it is now LF.

REJECTED: none

LEAD:
- days.csv codes for days 77 to 91 should be MS-ESS1-1 only (MS-PS4-2 on day 79 for the light-ray retrieval), and day 78's code and skill should be the s5 readiness rows (sequence 1).
- Regenerate the header after days.csv sets the unit column to 4.1 for days 77 to 104, so it lists one section, not six (sequence 2).
- days.csv safety text for the lamp says "cool LED only with teacher-managed cord" but the plan table says battery-powered; align days.csv to battery lamps, and list white paper, tape markers and safety glasses in the supplies column (sequence 7).
