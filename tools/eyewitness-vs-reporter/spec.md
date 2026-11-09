# Eyewitness vs Reporter

## One idea
The student holds two accounts of the Great Blizzard of 1888, a diary kept by a girl in Brooklyn who lived through it and a newspaper article written days later from interviews and records, and works a case file of question cards, filing each under diary, article, both or neither and highlighting the line that proves it, while a focus meter fills for each account (senses and feelings for the diary, numbers and causes for the article), so they learn what being there gives a writer and what it takes away.

## Not like
- fact-fusion (5, concept): three sources into one report. Here two accounts compared by focus.
- swap-the-teller (3, spec): narrators in fiction. Here firsthand and secondhand nonfiction.
- history-or-fiction (7, concept): history versus historical fiction. Here two kinds of true account.
- blizzard-scenes (concept): writing a blizzard scene from another view. Here reading real kinds of account.
- radio-hour-notes (3-5, spec): notes from listening. Here filing questions by source.

## Who and how
- Grade 4, ELA, module "Firsthand and Secondhand Accounts" (Reading Informational). Standard: RI.4.6.
- Driver: one student or a pair (tool.json `driver: "student"`). Both accounts are read on tap in their own voices.
- Case 1 (the 1888 blizzard, written for Curio Class from the historical record), then Case 2 in class mode (short public-domain excerpts from 1888 newspapers and a first-person account, lightly trimmed). tool.json `modes: ["Case 1", "Case 2"]`, `minutes: "20-30"`, `grades_label: "Grade 4"`.
- Nothing is saved; `Print` prints the case report.
- The diary's writer is made up and labeled so on the case file ("Lottie is made up. Her diary is built from real accounts of the storm.").

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| RI.4.6 (firsthand vs secondhand) | Read the case file: who wrote each account, when, and how they knew | two ID cards: "was there" and "wasn't there" | 2 |
| RI.4.6 (information) | File each question card under diary, article, both or neither and highlight the proving line | four drawers and highlighted lines | 3, 4 |
| RI.4.6 (focus) | Watch the focus meter fill: senses and feelings, numbers and causes | two meters with labeled segments | 5 |
| RI.4.6 (describe the differences) | Write the case report: one thing only the eyewitness knew, one only the reporter could know, one the reporter got from someone like the eyewitness | the report card with three slots | 6 |

## Screens and modes
Header (kit): title "Eyewitness vs Reporter"; `Cases`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A detective's desk lit by a green lamp, with a case folder and Inspector Hollis, a gray cat in a deerstalker cap. First hint: "Tap the case folder to open it." The first tap opens it with its line; the welcome is queued after it (`welcomeAfter: true`).

**Case file.** Two ID cards: "Lottie, age 11, Brooklyn. Wrote in her diary March 12 to 14, 1888. Was there." and "A reporter, writing for a city newspaper on March 17, 1888. Talked to people and read the Signal Service weather reports. Wasn't there for most of it." The diary on the left, the article on the right; tap any line to hear it.

**Question cards.** Ten cards come one at a time: What did the wind sound like? How deep was the snow in Central Park? How did the writer feel on the second night? What made the storm so strong? How many days did trains stop? Did the milk come? Who helped the family next door? What will the city do so it doesn't happen again? (neither: no account says), What color was the sky? and How did people get across the frozen East River? (both). The student files each card under Diary, Article, Both or Neither, then highlights the proving line. A wrong drawer: "Look again. Which writer would know that?"

**Focus meter.** Each account's meter fills from the lines the student highlights, sorted by a tag in the data (senses, feelings, numbers, causes, many places). After the cards, the meters show the shape: the diary's meter is mostly senses and feelings; the article's mostly numbers, causes and many places.

**Case report.** Three slots with sentence frames. The student picks a highlighted line for each slot and finishes the sentence. Inspector Hollis reads it back.

**Case 2 (class mode).** Two short excerpts from 1888 sources in the public domain (a newspaper report and a first-person account), read aloud with hard words glossed; the class files four question cards together.

At 1366x768 the two accounts fit side by side with the card above; at 680x425 the accounts are tabs.

## Content
Written for Curio Class, about 350 words each, from sourced facts:
- **Lottie's diary**: rain turned to snow on Sunday night, March 11; wind howled at the windows; snow drifted to the second-floor window; her father could not get to work; the milk did not come; a neighbor dug a path; she was scared at night when the stove fire got low; people walked across the frozen East River.
- **The article**: the storm struck March 11 to 14; Central Park measured about 21 inches, with drifts much deeper; some places in New York and New England got 40 to 50 inches or more; winds over 40 miles per hour; elevated trains stopped and telegraph lines fell; about 400 people died across the Northeast, many of them outdoors or at sea; the storm led the city to put many wires underground and helped lead to building a subway.
- Deaths are stated once, plainly, as a number in the article; no one in Lottie's diary dies.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Highlights are whole sentences; a card can be refiled.
- The report frames: "Only Lottie could tell us ___ because she ___." "Only the reporter could tell us ___ because ___." "The reporter learned ___ from people like Lottie."

## Look
- Accent `--brand` #46525e storm slate (header, folder, drawers); gold #f4c542 (highlights, the lamp); paper #f4f6f8; ink #141a20; muted #56606a. Scene: a lamplit detective desk, snow at the window.
- Contrast (WCAG 2.1, computed): white on brand 7.99:1; brand on paper 7.37:1; ink on paper 16.18:1; muted on paper 5.92:1; ink on gold 10.77:1.
- Never color alone: drawers have words and icons; meter segments carry labels.
- Different from this batch (lagoon teal, word violet, brick orange, kite magenta).

## Art
- People art goes to Gemini: Lottie at her window writing in a diary (an 11-year-old girl in 1888 Brooklyn, wool dress and shawl, illustrated), and the reporter at a desk with notes (illustrated, period dress); 2 images; 3:4; cutout yes.
- Local FLUX (`scripts/localart.py`): desk (1); Inspector Hollis (4 poses: read, point, think, nod); 1:1; cutout yes; storm scenes (4: snowdrifts on a city street with elevated train tracks, fallen telegraph wires, a frozen river, sunlight on dug-out paths; people small and far, no faces); 16:9; diary page texture and newspaper texture (2).
About 13 images. Drawn in code: case file, drawers, meters, report.

## Voice
Bank voice `knowing-guide` as Inspector Hollis (unique in this batch). Lottie's diary is read by `big-sister`; the article by `news-reader` (both unique in this batch). `Curio.voice` with `scope: () => state.case + ':' + state.card + ':' + state.step`, `welcomeAfter: true`.
- how `welcome`: "Two witnesses, one storm. One was there. One wasn't. Let's find out what each one can tell us."
- event, whole, `diaryLine` / `articleLine`: the tapped line in its voice.
- event `card`: the question card.
- how `fileHow`: "File this card under Diary, Article, Both or Neither. Then highlight the line that proves it."
- event `lookAgain`: "Look again. Which writer would know that?"
- event `neither`: "Neither one says. Sometimes no account can tell us."
- event `meters`: "Lottie's account is full of sounds and feelings. The reporter's is full of numbers and causes."
- how `reportHow`: "Now write the case report. Pick a line for each part."
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None. Tool-only code: case file, drawers, focus meter, report frames.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Drawers | Try every drawer | A wrong drawer says "Look again"; the card also needs a highlighted line from the right account. |
| Highlight | Highlight any line | The line must be one of the card's proving lines (data); wrong lines say "Does this line answer it?" |
| Meters | (no pass or fail) | The meters show the focus; they are a reading, not a score. |
| Report | Pick random lines | Each slot accepts only lines from the right account; Inspector Hollis reads it back, and a mismatch sounds wrong. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap the folder: `welcome` (queued, first time).
2. Lines: `diaryLine` / `articleLine` (whole).
3. Each card: `card`, `fileHow` (first time); `lookAgain` or `neither` as they fire.
4. After ten cards: `meters`. Report: `reportHow`.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| RI.4.6 wording | thecorestandards.org, Reading Informational Grade 4 | CCSS ELA 2010 PDF | yes |
| The blizzard struck March 11 to 14, 1888; rain turned to snow; Central Park about 21 inches; 40 to 50 inches or more in parts of New York and New England; strong winds and huge drifts | NOAA National Weather Service, the Blizzard of 1888 | Library of Congress, Blizzard of 1888 (Today in History, March 12) | yes |
| About 400 deaths across the Northeast | NOAA National Weather Service, the Blizzard of 1888 | Smithsonian Magazine, the Great Blizzard of 1888 | yes |
| Elevated trains stopped; telegraph lines fell; people crossed the frozen East River | Library of Congress, Chronicling America, March 1888 New York newspapers | New-York Historical Society, Blizzard of 1888 | yes |
| The storm helped lead New York to put wires underground and to plan a subway | Smithsonian Magazine, the Great Blizzard of 1888 | New York Transit Museum, history of the subway | yes |
Backed twice: 5. Cut: 1 (a temperature low for the city; sources gave different numbers, so the article doesn't give one).

Sensitivity note: storm deaths are told once, plainly, in the article; people art for Lottie and the reporter goes to the fresh-agent review.

Checks run (Python, scratchpad b12, 2026-11-09): the ten cards fill all four drawers (Diary 5, Article 3, Both 1, Neither 1); contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 both accounts fit; at 680x425 they are tabs.
2. The case file shows who was there and who wasn't. (RI.4.6)
3. Ten cards file into four drawers. (RI.4.6)
4. Each filed card needs a proving line. (RI.4.6)
5. The focus meters fill from highlights and show each account's shape. (RI.4.6)
6. The case report takes three lines and frames and prints. (RI.4.6)
7. Case 2 reads the public-domain excerpts with glosses.
8. Lottie is labeled made-up on the case file.
9. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
10. Motion off: snow at the window is still; no network requests.

## Open questions
- None for Cory.
