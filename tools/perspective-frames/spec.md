# Perspective Frames

## One idea
The student sits in on two town decisions, the 1950s plan that routed Interstate 94 through Rondo, the heart of Saint Paul's Black community, and a made-up town's vote today on turning a parking lot into a park, sorts quote cards by who said them (a highway planner, a Rondo shop owner, a Rondo family, a commuter) using clues in the words, then uses comparison frames (Whereas..., Both agree that..., Unlike...) to explain why each speaker sees the decision differently and takes a supported position, so they learn the language for comparing viewpoints with reasons.

## Not like
- is-the-historian-right (9-12, spec, in build): judging a historian's claim against sources. Here comparing speakers' viewpoints on one decision.
- summary-scaffold (6-8, spec later): summarizing one source. Here comparing several speakers.
- i-choose-because (K-2, spec): one choice with one reason. Here several viewpoints and a position.
- talk-moves-trainer (3-5, spec, this batch): joining a discussion in turns. Here comparing others' views in writing.
- mundo-hispano (6-12, spec, this batch): why a tradition matters to its community. Here why a decision looks different to each person it touches.

## Who and how
- Grades 6 to 8, English Language Development, module "Comparing Perspectives". Standards: WIDA ELD-SS (Standard 5, the language of social studies), Argue key language use (WIDA 2020).
- Driver: one student; class mode is "Add a speaker", where the class names a speaker the cards left out and writes their quote together on the projector (tool.json `driver: "student"`). Every card, frame and paragraph is read on tap.
- Two cases: "Rondo, 1956" (main) and "Lot 9 Park" (today). Help setting: Lots (clue words underlined, full frames), Some (frames with blanks), Little (frame starters, then typing). Teacher notes map them to WIDA 1-2, 3-4 and 5-6. tool.json `modes: ["Rondo, 1956", "Lot 9 Park", "Add a speaker"]`, `minutes: "25-35"`, `grades_label: "Grades 6-8"`.
- Nothing is saved; `Print` prints the perspective map and the paragraph.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| WIDA ELD-SS (stakeholders, decisions, consequences) | Sort quotes by speaker using clue words | the speaker columns with clue words lit | 2 |
| WIDA Argue (compare viewpoints with reasons) | Build comparison sentences that include each side's why | the comparison with "because" slots | 3 |
| WIDA ELD-SS (gains and losses) | Fill what each speaker gains and loses | the perspective map | 4 |
| WIDA Argue (take a supported position) | Write which view is most convincing and why, naming the other side | the closing paragraph | 5 |

## Screens and modes
Header (kit): title "Perspective Frames"; `Sort`, `Compare`, `Map`, `Position`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A town meeting room with folding chairs, a poster on an easel ("Public Hearing: Proposed Freeway Route, 1956") and a pile of quote cards. The moderator, Ms. Lorraine Hughes, a retired civics teacher, stands at the podium. First hint: "Tap the poster to hear what's being decided." The first tap reads the poster card; the welcome is queued after it (`welcomeAfter: true`).

**The Rondo case.** A short fact card first, read aloud: In 1956 Congress passed the Federal Aid Highway Act to build interstate freeways. Planners in Saint Paul had more than one possible route for Interstate 94; the one chosen ran along Rondo Avenue, through the center of the city's Black community. Between 1956 and 1968 the freeway was built, and at least 650 families were forced to move, along with many businesses, churches and clubs. The speakers on the quote cards are made up, and the card says so: "These speakers are made up. What happened is real."

**Sort.** Twelve quote cards, three per speaker. Clue words point to the speaker: "My customers walk here from three blocks around" (shop owner), "Our kids' school is two streets over" (family), "Twenty minutes faster to my job downtown" (commuter), "The route that costs the least and moves the most cars" (planner). The student drags each card into a speaker column; a wrong column asks "Which words told you who said it?"

**Compare.** For three pairs of speakers the student picks what each wants and why, then builds comparison sentences from frames: "Whereas the planner wants ___ because ___, the shop owner wants ___ because ___." "Both the commuter and the family agree that ___." "Unlike the planner, the family ___." A comparison without a reason ("The planner and the family disagree.") is nudged: "Why does each one see it that way?"

**Map.** A perspective map with each speaker's gains and losses, filled from the sorted quotes.

**Position.** The student writes a short paragraph comparing two viewpoints and says which is most convincing and why, naming the other side fairly. Then a closing card shows what happened later: in 2015 Saint Paul's mayor apologized for the routing, and people are still working on plans to reconnect the neighborhood, such as a land bridge over the freeway.

**Lot 9 Park.** The same moves for a made-up town today: a parking lot behind Main Street could become a park; speakers are a café owner, a parent, a nurse who parks there for night shifts, and a teen on the youth council.

**Add a speaker.** On the projector, the class adds a speaker the cards left out (for Rondo, a church pastor or a child; for Lot 9, a delivery driver) and writes their quote.

At 1366x768 the columns and cards fit; at 680x425 columns stack and cards are a drawer.

## Content
- Fact card and closing card for Rondo from the Sources table; every number is sourced. Quotes for both cases written for Curio Class, labeled as made up.
- The Rondo case is told plainly and with care: the harm to the Black community is named, the planners' stated reasons are shown fairly as their view, and the student is never asked to argue that the families' losses did not matter. The position frame asks which view is most convincing, and every view must be named fairly.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Cards can be moved and sentences rebuilt any time.
- With Motion off cards drop into columns without sliding and the map fills without growing.

## Look
- Accent `--brand` #3f4f5f town-hall slate (header, podium, columns); gold #f4c542 (clue words, gains on the map); paper #f3f5f7; ink #121a22; muted #555f69. Scene: a town meeting room with folding chairs.
- Contrast (WCAG 2.1, computed): white on brand 8.42:1; brand on paper 7.70:1; ink on paper 16.06:1; muted on paper 5.95:1; ink on gold 10.79:1.
- Never color alone: clue words are underlined; gains and losses are labeled with words and plus and minus signs.
- Different from this batch (detective teal, earth red, book-group purple, highlighter olive).

## Art
- People art goes to Gemini: Ms. Lorraine Hughes (a Black woman in her seventies with glasses), 3 poses; 1950s speakers (a white highway planner with rolled maps, a Black shop owner in an apron, a Black mother with two children, a white commuter in a hat), 2 poses each; Lot 9 speakers (a Vietnamese American café owner, a Latina parent with a stroller, a Black nurse in scrubs, a white teen with a clipboard), 2 poses each; "illustrated 1950s <speaker> at a town hearing <pose>, soft gouache, plain white background"; 1:1; cutout yes. The Rondo art goes to the fresh-agent review.
- Local FLUX (`scripts/localart.py`): the meeting room (1); a 1950s neighborhood street with houses and shops, no faces (1); a parking lot behind a main street today (1).
About 22 images. Drawn in code: columns, frames, perspective map.

## Voice
Bank voice `calm-professor` as Ms. Hughes and the hint voice (unique in this batch); the planner and the commuter are read by `friendly-dad`, the family and the parent by `gentle-storyteller`, and the shop owner and the café owner by `knowing-guide` (each unique in this batch). `Curio.voice` with `scope: () => state.case + ':' + state.view`, `welcomeAfter: true`.
- how `welcome`: "Sort what people said by who said it. Then explain why they see it differently."
- event, whole, `facts`: the fact card.
- event `quote`: the quote card.
- event `clue`: "Which words told you who said it?"
- event `why`: "Why does each one see it that way?"
- event, whole, `paragraph`: the student's paragraph.
- event, whole, `later`: the closing card.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None. Tool-only code: quote sorting with clue words, comparison frames with reason slots, the perspective map, the position paragraph, two cases.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Sort | Drag cards at random | Each card is keyed; a wrong column asks for the clue words. |
| Compare | "They disagree." for every pair | Each frame needs both reasons in its because slots. |
| Compare | Use the same reason for both sides | The two reason slots must come from different speakers' quotes. |
| Position | Name only one side | The position frame needs the other view named with its reason. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap the poster: the poster card, `welcome` (queued, first time); `facts` (whole) before Sort.
2. Sort: `quote` on tap; `clue` on a wrong column.
3. Compare: `why` as it fires. Position: `paragraph` (whole), then `later` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| WIDA 2020: Standard 5 is the language of social studies; Argue covers comparing viewpoints and taking a supported position | WIDA ELD Standards Framework, 2020 Edition | WIDA, Key Language Uses: A Closer Look (2020) | yes |
| The Federal Aid Highway Act of 1956 funded the interstate freeways; more than one route for I-94 in Saint Paul was considered | Wikipedia, Rondo neighborhood (checked 2026-11-09) | Minnesota Historical Society, Rondo Neighborhood and I-94 research guide | yes |
| Rondo's center was demolished between 1956 and 1968 for I-94, and at least 650 families were displaced along with many businesses | Wikipedia, Rondo neighborhood (checked 2026-11-09) | MNopedia (Minnesota Historical Society), Rondo neighborhood | yes |
| In 2015 Saint Paul's mayor apologized for the routing; a land bridge over I-94 has been under discussion | Wikipedia, Rondo neighborhood (checked 2026-11-09), citing MinnPost, October 14, 2016 | Star Tribune, March 25, 2021, on Rondo land bridge advocates | yes |
Backed twice: 4. Cut: 0.

Sensitivity note: the Rondo case names the displacement of a Black community plainly; speakers are made up and labeled; the tool goes to the fresh-agent review.

Checks run (Python, scratchpad b27, 2026-11-09): the saved Rondo page has "between 1956 and 1968", "At least 650 families", "Federal Aid Highway Act of 1956", the 2015 mayor's apology and the land bridge; every quote card's clue word appears in no other speaker's cards; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 columns and cards fit; at 680x425 columns stack and cards are a drawer.
2. Quotes sort by speaker; wrong columns ask for clue words. (WIDA ELD-SS)
3. Comparison frames need both reasons. (WIDA Argue)
4. The perspective map shows gains and losses. (WIDA ELD-SS)
5. The position paragraph names both sides; the closing card plays. (WIDA Argue)
6. The made-up label shows on every quote; Lot 9 Park plays the same way.
7. Help levels, Add a speaker and Print work.
8. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
9. Motion off: cards and map appear without motion; no network requests.

## Open questions
- Home-language support: home-language glossaries for ELD frames (Cory's open question in RUNBOOK.md)? (default used: English only, with pictures and read-aloud)
