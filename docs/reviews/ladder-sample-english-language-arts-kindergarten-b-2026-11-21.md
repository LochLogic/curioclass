# Ladder sample review: english-language-arts-kindergarten, set B (2026-11-21)

Reader: fresh, read-only. Each day was read cold with the day before it, its section plan block, DEFAULTS.md, the days, items, wrongs, errors and sources rows, and every leans_on piece. Every exit key was reworked by hand. Gates (plan check, lesson check, filtered) showed only unrelated notes (section not in the units list, percent needing the text, rests on memory); none of the findings below were caught by them.

Method note on checking: numbers, key letters and sound facts were checked by hand against the texts and cards. Real-world facts were checked only against the sources.csv rows (status and kind of page); no page was re-fetched, so source findings are about row quality, not about the page itself.

## Days

- courses/english-language-arts-kindergarten/u01-6/d027.md (Day 27, exit E27, picture-and-beads informational page): teachable, but the exit hands the child the topic and the scribing part cannot fit its minutes.
- courses/english-language-arts-kindergarten/u02-6/d057.md (Day 57, exit E57, The Magic Bow retell): sound and runnable; only soft stem and hand-off wording issues.
- courses/english-language-arts-kindergarten/u03-3/d091.md (Day 91, exits X91a/b, tree and owl cards): two end items are unobservable or aimed at the wrong skill, and the repair block cannot run.
- courses/english-language-arts-kindergarten/u03-9/d117.md (Day 117, exit E117, fan palm card): the new fan palm card reuses the Day 89 palm and shade case, and the closing record load does not fit.
- courses/english-language-arts-kindergarten/u04-8/d153.md (Day 153, observation day): one key states a wrong sound fact and a new r-controlled sort is introduced on a day that says nothing new is taught.

## Findings (most serious first)

| day | severity | kind | what is wrong | the exact fix | script gate would catch it |
|---|---|---|---|---|---|
| 153 | FIRM | key | The key says "car" and "star" sound the same in the middle. The /ar/ sound is word-final in the vowel-plus-r sense taught here, so "same in the middle" is wrong and a child who answers correctly is marked wrong. | Change the key to "car and star end the same" (or use a medial pair such as "cart" and "star"); update wrongs.csv to match. | no |
| 153 | FIRM | exit-goal | An r-controlled sorting task is new here, on a day that is an observation day with nothing new taught. It measures a skill no earlier day taught. | Replace the sort with the already-taught CVC or digraph sort from the unit's earlier days, or move the r-controlled sort to a taught day first. | no |
| 117 | FIRM | rule4 | The fan palm exit card reuses the palm and shade case from E89 (Day 89 exit card). Rule 4 forbids reusing an earlier day's case. Items, keys and wrongs do match the new fan palm card, so the card swap itself is consistent; the case is the problem. | Use a different living thing and different need on E117 (not palm, not shade); rewrite items s03-X117a/b, the key and the wrongs together. | no |
| 117 | FIRM | timing | The closing step asks for about 150 records (30 children, five records each) in 15 minutes. At roughly 6 seconds a record that is 15 minutes with no set-up. | Cut the closing to one record per child (30 records, about 5 minutes) and move the rest to the next day. | no |
| 27 | FIRM | exit-goal | The exit states the topic verbatim ("This page is about beads"), then asks the child for the topic. It measures listening, not the goal. | Remove the topic sentence from the read-aloud; ask for the topic of a page the child has not heard named. | no |
| 27 | FIRM | timing | The 9-minute scribing part (30 children at about 30 seconds each is 15 minutes, plus set-up) cannot fit. | Scribe 12 children a day over three days, or shorten to a one-line scribe per child with a 15-minute allotment. | no |
| 91 | FIRM | exit-goal | End items T2c and T2d are unobservable from the teacher's seat or aimed at the wrong skill (they do not check the goal in the plan). | Rewrite T2c and T2d as one aloud ask each that shows a mark on the observation sheet; update the key and wrongs. | no |
| 91 | SOFT | words | The words "gather", "support" and "shelter" are used in teaching and items but are not taught or reserved anywhere earlier. | Teach each once on Day 90 or swap for taught words (pick up, hold, home). | no |
| 91 | SOFT | timing | The repair block (re-teach for children who miss the end items) has no minutes left; the day sums to 120 with no slack. | Cut 5 minutes from the opener and give them to the repair block, or drop the repair block and move it to the hand-off day. | no |
| 91 | SOFT | source | The wiki-owl row is an Audubon magazine article, labelled as a wiki id; wiki-palm is an NPS page with the same wiki label. The id and the real source disagree, which could mislead a reader of the sources table. | Rename the ids (aud-owl, nps-fan-palm-oasis) and keep the status line. | no |
| 117 | SOFT | other | The plan block (u03-9.md line 109) still describes the Brazil nut and agouti E117 card. The day and data now use the fan palm card. | Rewrite that line for the fan palm card. | no |
| 117 | SOFT | source | The Who Depends on a Tree text (gk-u3-06) has no sources.csv row, so its tree facts have no recorded source. | Add a row with the park page, a checked status and the day. | yes (a source-row gate could) |
| 27 | SOFT | words | One exit stem carries two asks in one stem. | Split into two items or drop the second ask. | no |
| 57 | SOFT | words | A stem uses "then" where the retell cards use "next", so the stem word does not match the taught card word. | Change the stem to "next". | no |
| 57 | SOFT | handoff | handbacks.csv has only AJ for 56 to 57 and J for 57 to 58; the day before asks for a hand-back the next day does not pick up. | Add the missing hand-back rows or remove the ask on Day 56. | no |
| 153 | SOFT | words | A printed stem is longer than 10 words and is not marked as read aloud. | Shorten to 10 words or mark it teacher-read. | no |
| 153 | SOFT | handoff | The next day's opener does not pick up the Day 153 observation marks. | Add one line to Day 154's opener naming the marks to recheck. | no |
| 57 | SOFT | content | The retell key accepts any order of beginning, middle and end; The Magic Bow text (201 words) has a fixed order. | Tighten the key to the story order. | no |
| 27 | TEMPLATE | other | Application and Fluency days are labelled "nothing new is taught" in the template, but this day's exit introduces a new page type. The label does not fit. | Allow a one-line "introduced as a check" note on those days. | no |
| 117 | TEMPLATE | other | The "exits ask one thing, aloud" rule has no way to record a 150-mark closing; the template has no per-child mark cap. | Add a template line capping marks per child at one per day. | no |
| 153 | TEMPLATE | other | The observation-day template says "nothing new is taught" but the sheet design invites new item types. | Add a gate on observation days: items must come from earlier days' item ids. | yes (an item-id gate) |
| 91 | TEMPLATE | other | The 1,800-word teacher-prose cap is the only gate that fires, and it counts plan text the teacher never reads. It rewards cuts to timing notes rather than to prose. | Count only teacher-facing prose, not set-up notes. | yes |

## Ladder

Ledger terms were looked up with the filtered ledger command for the words the days teach. This grade is the floor of the ladder, so there is no lower grade to reuse; the check is instead against earlier units in the same grade. The days use the earlier units well: Day 57 retells with the cards from Day 54 to 56, Day 91 builds on the Day 89 tree cards, and Day 117 reuses the caption sheet from the earlier unit. The ladder fault is in Day 153 (r-controlled sort not taught earlier in the grade) and in Day 117 (the Day 89 palm case reused as an exit). Day 91 uses three words (gather, support, shelter) that no earlier unit taught. No day uses a different word for an old idea, apart from "then" and "next" on Day 57.

## Counts

| day | FIRM | SOFT | TEMPLATE |
|---|---|---|---|
| 27 | 2 | 1 | 1 |
| 57 | 0 | 3 | 0 |
| 91 | 1 | 3 | 1 |
| 117 | 2 | 2 | 1 |
| 153 | 2 | 2 | 1 |
| all | 7 | 11 | 4 |

Reader caveat: these counts come from the table above. During reading I noted further small wording faults (more two-ask stems, plan lines out of date) that are folded into the rows above rather than listed one by one.
