# Answer-key read: social-studies-grade-1, unit 1, days 1 to 10 (2026-11-19)

Kind: answer-key. Items read: 20 (3 readiness R1 to R3, 9 exit X1 to X8 and X10, 8 end E1 to E8), with their 28 wrongs rows and the unit's shared pieces. Every item is teacher-judged (spoken, pointed or circled). Each item was solved cold from the stem and card text before the key, samples and look-fors were opened.

## Verdict

Pass with fixes. The cold answers matched the keys on 14 items; the faults were two marks whose stem gave the answer, a key that contradicted the park case, keys that rested on a photograph nobody had opened, a too-narrow key, and four rule 4 reuses.

## Faults

| Item | Kind | What was wrong | Fix |
|---|---|---|---|
| s01-X4 | ambiguous (given away) | Mark read "circle the picture of the club that keeps its pieces on a mat": the stem named the answer, so the mark tested only matching. | Mark now asks for the picture that shows a rule that helps the club finish its puzzle; card file matches. |
| s01-X7 | ambiguous (given away) | Mark described the right picture word for word. | Mark now asks for the picture where everyone has a part in getting visitors to the rooms, with both pictures described as before; card file matches. |
| s01-X10 | rule4 | The reading-club case (Pass books gently / Who gets a book next?) is printed in the unit 3 opener as the teaching cases for errors G and I, and the ledger lists a reading club as a unit 4 exit case. | New case: a bird-watching club (Keep voices low so the birds stay near / Keep voices low); key questions "Where do we sit to watch?", "Who keeps the list of birds?"; wrongs row "Pass books." became "Keep voices low."; exit card and key lines updated. The opener's book examples stay as teaching cases. |
| s01-E7, s01-E6 | key | Key said the volunteers "bag the plants" and "collect those plants in bags". The case says Ivy pulls the weeds and Sam and Noor bag them, and the plants are what the weeds crowd out. The stem says the worker "assigns the areas", but the case said "tells each volunteer where to start". | Keys now say pull and bag the weeds, clear the weeds from the patch. Case text now says the worker "gives each volunteer an area to start in". |
| s01-E4, s01-E5, s01-E8 | needs-info | Keys named a worker holding up a plant, "listen while a plant is shown", "learn from the worker" and "caring for this place". The photograph file was never opened by the writer, and the caption says only that group volunteers take a close look at non-native species on the Coastal Trail. | Keys rest on the caption (look closely together, learn together, stay together on the trail so everyone can hear and learn). E5 key says the teacher looks at the print before day 9 and writes the two actions on the key; the same line is added to the day 9 card file. |
| s01-E8 | key | Sample named a child ("Jo"). | Changed to "another". |
| s01-E2 | ambiguous | Key allowed one word per question (role for the setter's job); duty is equally right. | Key accepts any fitting unit word (belong, rule, duty, role, goal). |
| s01-X8 | needs-info | Key allowed only "right change"; a first grader is not given that link from counting coins. | Key also accepts "the table knows how much money it has" and any tie from counting to the table's work; card key line updated. |
| s01-R1 | rule4 | Second-try aid was a school gate with a bell, the same picture as day 10 fresh-try card F (school bell). | Aid is now a gate with a big painted sun; key reads "Why is there a sun?". |
| strips-class-rules (piece) | rule4 | Example strip 3 "Put the scissors in the tray" is the R2 case. | Example is now "Push in your chair." R2 stays: it is the planned retrieval of kindergarten's case, and the ledger lists it as a deliberate review. |
| unit 1 opener (piece) | rule4 | The error A teaching cards were the X1 pair ("Where do we walk?" / "Walks are fun"). | Opener now uses "Where does the snail live?" / "Snails are slow". X1 unchanged. |

No fault found: R2, R3, X1, X2, X3, X5, X6, E1, E3. X3 and X6 name the foil's flaw in the choice text, which is the contrast being taught; the spoken part carries the test.

## Section plan field 3 lines that no longer match items.csv

These docs are not mine to edit; the lead should refresh them:
- docs/courses/social-studies-grade-1/u01-2.md section 3, day 4 table row and X4 line: the mark wording now asks for the picture that shows a rule that helps the club finish.
- docs/courses/social-studies-grade-1/u01-3.md section 3: X7 mark wording; X8 answer (broader); X10 whole line (bird-watching club, new rule card text, new sample questions, wrong "Keep voices low"). Field 4 rows G and I quote "Who gets a book next?" and "Pass books" as error examples; they still work as teaching examples but no longer match the exit.
- docs/courses/social-studies-grade-1/u01-1.md section 4 row A and the u01-1 section 1 line still quote "Walks are fun" as the error A example; the opener now uses the snail pair. X1 itself is unchanged and matches.
- Plan notes say the E4 to E8 wording is "the sent wording": the stems are unchanged; only keys and the case text changed.

## Left

- The Group Volunteering print has never been opened by any writer. E4, E5 and E8 are safe on the caption alone, but the teacher must look at the print and note the two actions before day 9.
- plan.py check: no new FAIL. The three existing FAILs (sections 1.1 to 1.3 not in data/units.csv) are not from this unit's items.

## My own errors

- I ran `git --version` once (output discarded) before I noticed the no-git rule. It touched nothing.
- My first helper script failed to write because of a shell heredoc problem; I rewrote it with the file tool. No data was changed by the failed attempt.
