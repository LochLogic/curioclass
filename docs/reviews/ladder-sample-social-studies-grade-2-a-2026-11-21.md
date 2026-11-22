# Ladder sample, social studies grade 2, set A (2026-11-21)

Fresh reader, read-only. Days: 1, 25, 44, 58, 82. Gates run (filtered): plan.py check shows 0 sequence failures and 25 "section not in data/units.csv" failures (every section, not day faults); lesson.py check shows 0 failures on all five days (day 82 has one NOTE: the plan block names "35", never used).

## Days read

- courses/social-studies-grade-2/u01-1/d001.md (Understanding, readiness): teachable and timed; exit is easy and a stray template fragment is left in the text.
- courses/social-studies-grade-2/u02-3/d025.md (Application): sound and fits 40 minutes; repair is unclear, the plan's written task is dropped, UK spelling.
- courses/social-studies-grade-2/u03-4/d044.md (Check, end-of-unit): not runnable as written; one end item is never asked, three items have no answer row, and partner talk contradicts "answer alone".
- courses/social-studies-grade-2/u05-1/d058.md (Understanding): good sourcing and sensitivity; the six hear the exit's answer before they mark it.
- courses/social-studies-grade-2/u07-1/d082.md (Understanding): runs in time, but the exit cannot be failed and uses categories not yet taught.

## Findings

| day | severity | kind | what is wrong | exact fix | script gate? |
|---|---|---|---|---|---|
| 44 | FIRM | key / exit-goal | s03-E16 (why the circled one can be made again) is in the packet, key and goal map, but the day's Item 5 line lists E12 E13 E14 E15 E17 E18 and skips it; the response page has no row. "Renewable" (MA.2.T5.2) is then measured only by a two-choice circle (E15, pond fish or coal), 50% by chance. | Add s03-E16 to the Item 5 line and a response row "Work Card: why the one you circled can or cannot be made again"; give Item 5 six minutes (take one from Collect). | yes (an item in items.csv never named in the day) |
| 44 | FIRM | exit-goal | The response page has no row for E1 (why people settled), E8 (city land use unlike the farm) or E16. Children are told to write or draw on the page for these, so no answer can be recorded. | Add three rows in order: "Inlet Map: why people settled by this bay", "Community B: how the city uses land, not as the farm does", and the E16 row. | no |
| 44 | FIRM | exit-goal | The day says "answer alone, no one helps", but Item 8 has children say E30 to a partner for a minute before writing, and both blank-response-page.md and the frame strip say "Say it to your partner first". A partner can supply the reason, so the written claim (E29 to E31) no longer shows the child's own thinking. | Cut the partner minute; the child says it to the scribe only if they ask. Delete "Say it to your partner first" from blank-response-page.md and from the strip's use on day 44. | no |
| 44 | FIRM | timing / handoff | "Thirds" and "a scribe takes one third at a time" are unexplained on the day. packet-assessment.md says each third gives a spoken reason on one of items 1, 3 and 5, but no part of the day holds minutes for hearing it. One scribe cannot write for ten children in lockstep reading. | State what each third does and give the hearing time (about 45 seconds a child, taken in Collect), or drop the thirds and say a scribe writes only for a child who asks. | no |
| 44 | SOFT | other | The packet's read-aloud asks ("Say why people settled", "Say how boat crews adapt their travel") differ from the items.csv stems ("write or draw ...", "a crew finds the water low at noon"). The day pulls the items.csv stems; the response page follows them. Two texts, one trap. | Delete "The items, read aloud" block from packet-assessment.md and let the day's ids supply the asks. | no |
| 44 | SOFT | exit-goal | Packet captions give answers almost word for word: "Boat crews change their travel times when the water rises and falls" (E2), "The yard crew shapes timber to make wooden boats" (E12, E17), "young fish are raised each year" (E16), "The farming community makes wool blankets" (E23). Listening to the caption is enough. | Reword the captions to describe the scene without the item's answer (for example "Boat crews watch the water line"). | no |
| 44 | SOFT | rule4 | E15 and E16 reuse day 38's case and reason: coal as non-renewable, "takes far longer to form than a person lives" (cards-resources-day-38.md Picture 5; d038.md). It checks recall of the taught case, not transfer. | Replace coal with a case not taught (natural gas), keep pond fish as the renewable. | no |
| 44 | SOFT | key | E26 says "circle one picture that shows equipment" but the key names objects (the wheel stand or the shaping tools); picture 1 also shows a flat board. | Ask "circle one thing that is equipment" or key "the second picture". | no |
| 44 | SOFT | other | E5 ("adapt, change the land, or both") and E29 are the same ask; E5 gives away "both" before the choice item. E14 ("one job near the forest that is not building boats") has no card anchor. | Drop E5 or E29; anchor E14 to a job on the Work Card. | no |
| 44 | SOFT | timing | Item 7 is four asks in 3 minutes; Item 8 is a circle, a minute of talk, a written two-line frame and the maker in 4 minutes; Item 3 is three asks in 3 minutes for children who "write or draw a few words". About 28 asks read once each in about 26 minutes. | Item 7 four minutes, Item 8 six minutes, by shortening Collect to 3 and the packet reading to 4; or split into two sittings. | no |
| 44 | SOFT | other | E9 to E11 are never asked at the sitting; they are scored from an explanation revised after written feedback on days 35 and 36, so they cannot show independent work. Their stems are teacher notes. | Record these three as "revised with feedback" on the sheet, apart from the sitting. | no |
| 44 | TEMPLATE | rule4 | The plan states "shared shape, by design": the Inlet Map, Community B, Learning B and the claim frame share the form of taught practice cards. The rule that no practice or model shares an end item's form cannot hold for an end-of-unit check whose items "sample only what earlier days taught". | Exempt end items from the form rule; keep the case, picture and number rule. | n/a |
| 44 | TEMPLATE | words | E29 to E31 have no path (spoken) in items.csv although the day reads them aloud; the student page prints E29 (19 words) and E30 (17 words), over the 10-word K to 2 limit. | Set path spoken for E29 to E31 and print only "Circle one" and the frame lines. | yes |
| 58 | FIRM | exit-goal | X58b ("The Weaver Card gives work and family as reasons. Say one reason ... this card does not give") is heard from the six in pairs work, before X58 is marked. It states the answer to X58 (work). Also the card gives two reasons (the loom town, the sister) while X58 keys one, and the distractor "a visit" can be read as the sister. | Hear X58b after the child marks X58; change the options to "work, a storm, a school" and key work. | no |
| 58 | SOFT | timing | The 4-minute hook returns day 57's ticket and 11 marked tasks, reads Anna, asks three questions, has two reviews and traces the route. In pairs work the teacher hears the six for 4.5 minutes while a small group "redoes continents" with no minutes and no teacher. | Hook 6 minutes (take 2 from Five reasons); move the continent redo to day 59's slot. | no |
| 58 | SOFT | rule4 | Sela (a far town needs weavers, so she moves) has the same shape as Teo and Nell; the exit's form is the pairs-sort form. | Give Sela a reason in a new shape, for example a school for her brother. | no |
| 58 | SOFT | words | Exit options "a storm, a visit" are not the five taught words (safe, family); P58-3's printed stem is 17 words. | Use the taught words on the card; shorten the stem. | partly (word count yes) |
| 25 | SOFT | other | "harbour" appears in the day, the cards and a wrong-answer row; US spelling is required. | Change to "harbor" now. | yes |
| 25 | SOFT | key / handoff | Return and repair has two 4-minute parts, then "the part more children needed is for the whole class; the other goes to a small group". Unclear whether both parts are taught to everyone. The plan's written task (a change, a stay and a date for each picture) is replaced by label-moving. | Say "teach the part more missed to everyone, the other to a group of at most 6"; add a 2-minute written line to the chart. | no |
| 25 | SOFT | ladder | The ledger lists day 25's skill as "name a physical and a cultural change on a street", yet every Harbor Street change is cultural (the card's key says so). "Cultural" reuses grade 1's "cultural feature" (u06-1) without naming it. | Add a physical change to the 2025 card (a dredged channel) or change the ledger skill; name the grade 1 link. | no |
| 25 | SOFT | exit-goal | The stall circled on X25 has no error letter ("not yet seen"), so the repair has nowhere to route. | Give the stall circle a letter. | no |
| 1 | SOFT | other | The exit line ends "read the board once 1" (a template fragment) and the day's check is 14 minutes with items 1 to 5 while the plan has 10 minutes and items 1 to 4. | Delete the fragment; align the plan. | partly |
| 1 | SOFT | timing | Six children are heard for three asks (X1 mark, X1b, X1c) in about a minute each (6 minutes). | Drop X1c on day 1 or give 8 minutes. | no |
| 1 | SOFT | exit-goal | X1 (trail map vs world map for a path) is nearly unfailable; X1c alone carries the supporting-question goal. | Use two close maps, or keep X1c for all six. | no |
| 1 | SOFT | other | The hook asks "Which looks more like the globe" (no right answer) while the plan asks "Which would help us compare how big lands are". | Align the hook with the plan. | no |
| 82 | FIRM | exit-goal | X82 accepts any of three pictures (only the corner flag is wrong) and X82b accepts any question on land, water, work or people. Those categories are taught on day 83 ("Tomorrow we ask smaller questions"), so the exit uses what the day has not taught and cannot show whether a child grasped the big question. | Ask one question with one right answer: "Which question helps our big question: Where do people get water? or What color is my pencil?" Move the three pictures to day 83. | no |
| 82 | FIRM | other | The X82 stem says "Your country card shows three small pictures and a flag", but cards-menu-day-82.md says the country card shows only outline and name, and the pictures are on the exit card. "First look" is then a 1-minute look at an outline and a name. | Say "Your exit card shows ..."; make First look 2 minutes of finding the country on the locator map. | no |
| 82 | SOFT | source | cards-japan-hook-day-82.md says the Japan page is "weak (Wikipedia only)" and cards-menu names row 10E as weak, but sources.csv now has 82J1 checked on the Statistics Bureau and 10E checked on National Geographic. 82A is a "search read" row. I could not re-read the Japan PDF (compressed). | Delete the stale notes; point to 82J1. | no |
| 82 | SOFT | words | "Australia and wider Oceania" is a new term never taught; menu pronunciation is "not yet checked"; cards-menu says the 16 packets are "planned only" though packet files exist. P82-1 is two asks (would it help, say how). | Say "Australia and nearby islands"; check names; update the note; ask only "How would it help?". | no |

Sources opened: 58A (nps.gov Anna page: matches the card, Yugoslavia, 1920, age 18, mother and aunt, hugging and crying, 12 September 1991, interviewer Paul E. Sigrist Jr.); 38B (EIA coal: "nonrenewable because it takes millions of years to form", matches); 82J1 (stat.go.jp PDF: could not read it, judged only); 56A (gov.bw, a "search read" row, not on my days: certificate expired, unchecked). Row 1A (1904 Boulder map) I judged from its status only (margin read off the full image). All other places on these five days are invented and marked so. No made-up Native nation, no enslaved-people language, and no company names found in the five days.

## Ladder

- Day 1 leans on kindergarten (two maps beside a globe, u03-2) and grade 1 (supporting question, question board): reviews are named and match the ledger; nothing assumed that is missing.
- Day 25 uses grade 1's then-and-now chart (u02-2) and the grade 2 pair from day 24. The grade 1 "cultural feature" (u06-1) is a different use of "cultural" and is not named.
- Day 44 reuses day 38's coal case and its "takes far longer to form" wording as an end item.
- Day 58 reviews unit 1's who/when/where, unit 2's continents and unit 4's arrow; "reason" gets a new meaning (why a person moved, not "why you think") and the day says so.
- Day 82 reviews the unit 2 locator card and grade 1's supporting question, but asks for "work, people" categories before day 83 teaches them.
- Overall the grade used the lower grades well: reviews are named in the ledger's words. The gap shows in reused vocabulary ("cultural") and end items that repeat taught cases.

## Counts

| day | FIRM | SOFT | TEMPLATE |
|---|---|---|---|
| 1 | 0 | 4 | 0 |
| 25 | 0 | 4 | 0 |
| 44 | 4 | 7 | 2 |
| 58 | 1 | 3 | 0 |
| 82 | 2 | 2 | 0 |
| all | 7 | 20 | 2 |
