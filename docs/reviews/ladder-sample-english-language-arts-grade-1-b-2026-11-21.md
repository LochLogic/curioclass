# Ladder sample review: english-language-arts-grade-1, set b (2026-11-21)

Reader: fresh, read-only. Gates run in the permitted filtered form. lesson.py check shows no failure on any of the five days. Teacher word counts: d026 1414, d049 1164, d092 1409, d124 1672, d153 1284 (limit 1800). plan.py check shows 38 grade-wide failures about units and similar, none specific to these days; its NOTE "plan block names X which the day never uses" fires on all five.

Checked against a source: bird facts on d092 and d153 (sources.csv rows g1-u3-f1 to f30 and g1-u4-f1 to f12, solid). Only judged: all keys on non-factual items, timing (30 children times seconds a turn plus set-up), teacher fit.

## One line per day

- courses/english-language-arts-grade-1/u01-6/d026.md (Practice): runs in the time, but the exit tests the skill of day 25 and the key misses one accepted change.
- courses/english-language-arts-grade-1/u02-4/d049.md (Practice, tales): both tale texts say the required sensitivity read has not been done, and one source row rests on Wikipedia.
- courses/english-language-arts-grade-1/u03-4/d092.md (Practice, informational): sound teaching, but one repair claim is wrong against the day's own pages and two stems carry more than one ask.
- courses/english-language-arts-grade-1/u04-1/d124.md (Practice, overloaded): the exit reuses a taught case, the sort picture gives away its own answer, and one count on a page is wrong.
- courses/english-language-arts-grade-1/u04-8/d153.md (Application, observe): reviews the lower days well, but the exit repeats two end items and one end item is unclear.

## Findings (most serious first)

| day | severity | kind | what is wrong | exact fix | script gate would catch |
|---|---|---|---|---|---|
| 49 | FIRM | safety | Texts g1-u2-03 (Efik and Ibibio tale) and g1-u2-04 (Weaver Girl and Cowherd) state that the required sensitivity read has not been done. No record of a read was found. | Run the fresh-agent sensitivity read on both texts, log it, and only then remove the "not done" line; hold the day until then. | no |
| 124 | FIRM | rule4 | X124d reuses the Ben-waits case taught in the day, so it tests recall, not transfer. | Replace X124d with a new two-meaning-word case that appears nowhere in d123, d124 or the shared pieces; update items.csv key. | no |
| 124 | FIRM | key | The key and teaching say "fly" occurs twice on page 8; it occurs four times. | Change the count to four in the key and the model line. | no |
| 124 | FIRM | exit-goal | The Both and But picture arrives with its sort answer already shown, so the sort measures reading the picture, not the goal. | Print the picture without the Both/But labels; children assign them. | no |
| 26 | FIRM | exit-goal | The exit asks the child to turn a fact into a change (day 25's skill) instead of answering a partner's question, which is day 26's goal. | Rewrite the exit stem so a partner's question is given and the child revises the sentence in answer to it. | no |
| 26 | FIRM | key | The key omits "lower the sides", which the taught sign model accepts as a correct change. | Add "lower the sides" to the accepted answers in items.csv and the teacher key. | no |
| 49 | FIRM | source | sources.csv row for g1-u2-04 cites Wikipedia through a search summary, with no URL and no checked status. | Replace with a solid source (museum or university folk-tale collection), set status to checked with URL; if none, remove the claim. | yes (a status column check) |
| 92 | FIRM | content | The repair says only page D tells that down keeps the duck warm. If pairs hold F page 2, that page says it too, so the claim is wrong. | State which page each pair holds, or change the repair to "find the page that says it"; recheck against g1-u3-01. | no |
| 153 | FIRM | rule4 | The exit repeats end items A64 and A65 in form and case. | Replace the exit case with an unused two-page pairing; keep A64 and A65 as they are. | no |
| 153 | FIRM | key | End item A66 repeats A65 and its referent ("it") is unclear, so two answers fit. | Replace "it" with the named bird and change the stem so it asks one thing not asked by A65. | no |
| 26 | SOFT | other | Error letters A and C in the day do not match errors.csv for unit 1. | Align the letters in the day and wrongs.csv to errors.csv. | yes |
| 26 | SOFT | handoff | handbacks.csv covers only AA though three errors are named. | Add rows for the other two named errors. | yes |
| 26 | SOFT | rule4 | The crown repair card has the same form as the exit. | Change the repair to a different frame (oral, no sentence change). | no |
| 26 | SOFT | ladder | K taught "revise after a partner question" but the day presents it as new. | Open with "Remember in kindergarten we changed a sentence after a question" and name it review. | no |
| 26 | SOFT | timing | The 90-second retry is tight for 30 children. | Cut the retry to partners only, or allow 150 seconds. | no |
| 26 | SOFT | other | Text metadata omits day 26. | Add day 26 to the text rows used. | yes |
| 49 | SOFT | exit-goal | The exit tests order only, not the day's retell goal. | Add a one-ask item on cause or character, or narrow the goal wording. | no |
| 49 | SOFT | content | The error D repair stem has two asks. | Split into two stems or keep one. | no |
| 49 | SOFT | key | The home exit card differs from items.csv and prints no expected answer. | Match the card to items.csv and give the answer on the teacher side only. | no |
| 49 | SOFT | timing | Several parts are tight. | Trim one model or cut a turn from each. | no |
| 49 | SOFT | handoff | No handback row for 48 to 49 error D. | Add the row. | yes |
| 92 | SOFT | words | X92a distractor "fast blur" is defensible and the stem has no question. | Make the distractor clearly false and end the stem with a question. | no |
| 92 | SOFT | other | X92b has several asks in one stem. | One ask per stem. | no |
| 92 | SOFT | rule4 | The "fresh" repair page is a taught text. | Use an untaught page. | no |
| 92 | SOFT | content | The "article says" box is a sketch but the day says copy. | Make the box a sentence frame or change "copy" to "draw". | no |
| 92 | SOFT | other | The plan says 240 words but the day says 150. | Fix the plan or the day to agree. | no |
| 92 | SOFT | ladder | "gather" and "compare" are used without review wording. | Name them as words from kindergarten. | no |
| 124 | SOFT | content | Fly-card strips, "his" and "her" are not in the pieces the day names. | Add the strips and cards to the print list. | partly |
| 124 | SOFT | other | The day is overloaded (several new ideas in 120 minutes). | Move the pronoun work to day 125. | no |
| 124 | SOFT | ladder | The day does not name K two-meaning words or K Both/But as review. | Add the review wording. | no |
| 124 | SOFT | timing | Printing feedback is tight. | Give feedback to a sample, not every child. | no |
| 153 | SOFT | other | The sheet record and the spoken path conflict. | Pick one and edit the other. | no |
| 153 | SOFT | content | Two identical "waits" cards leave the Both card ambiguous. | Change one card's sentence. | no |
| 153 | SOFT | key | X153a key has a picture ambiguity. | Name the picture in the stem. | no |
| 153 | SOFT | timing | No slack in the hearing part. | Cut one syllable card. | no |
| 153 | SOFT | words | A vowel-team syllable is taught as new on an Application day. | Move to a Practice day or swap the word. | no |
| 153 | SOFT | source | The g1-u4-03 row has no URL and no day 153. | Add URL and day. | yes |
| 26 | TEMPLATE | other | "No practice shares the exit form" fights a deliberate repair card that mirrors the exit. | Let a repair slot share the form if it is outside the exit set, or change the rule. | n/a |
| 49 | TEMPLATE | other | "Heard six" exits make the exit speak for six children a day, not 30. | Allow whole-class marking for oral exits, or state it as a sample. | n/a |
| 153 | TEMPLATE | timing | The 90-second hearing budget cannot hold three pieces in this grade. | Set the budget by piece count. | n/a |

## Ladder

What the grade gap caused: kindergarten ideas (revise after a partner question, retell, gather and compare, two-meaning words, Both and But) came back in days 26, 49, 92 and 124 as if new or with no review wording. That cost minutes and, on day 124, crowded the day. Day 153 reviews well and uses the lower days in the same words. Overall, grade 1 used kindergarten's cases well in not repeating them as exits (checked "paint jar" and "puppet hat" in the ledger, no clash) but did not name the review.

## Counts

| day | FIRM | SOFT | TEMPLATE |
|---|---|---|---|
| d026 | 2 | 6 | 1 |
| d049 | 2 | 5 | 1 |
| d092 | 1 | 6 | 0 |
| d124 | 3 | 4 | 0 |
| d153 | 2 | 6 | 1 |
| all | 10 | 27 | 3 |

Note: several findings were drafted from detailed reading and a compacted summary of it; exact day sentences were not re-quoted. A fixer should reopen each cited line before editing.
