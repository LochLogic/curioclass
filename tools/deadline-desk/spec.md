# Deadline Desk

## One idea
The student is a reporter at the class paper, and every issue needs two kinds of writing: quick pieces typed in one sitting (a weather note, a lunch review, a sports brief) and one long feature built over several sessions with notes, a draft and a revision, so the finished issue shows side by side what short and long time frames are for, while keyboarding warm-ups grow the typing stamina a whole page (grade 4) or two (grade 5) in one sitting needs.

## Not like
- class-pet-pitch (3, spec): two pieces about one pet judged by a principal's reactions. Here no judging of content; the job is routine, stamina and publishing.
- headline-writer (3, spec): reading a news story for its main idea. Here writing for the paper.
- draft-car-wash (3-5, spec): revising one draft station by station for a reader. Here the routine of writing often, short and long, and typing it.
- postcard-writer (2, spec): one short message. Here a whole issue over days.

## Who and how
- Grades 3-5, ELA, module "Typing, Publishing and Writing Routines" (Writing). Standards: W.3.6, W.4.6, W.5.6, W.3.10, W.4.10, W.5.10.
- Driver: one student (tool.json `driver: "student"`). Needs a keyboard; on a tablet without one, the warm-ups are skipped and a line says "Warm-ups need a keyboard. You can still write with the on-screen keys."
- Grade picker on first visit (3, 4, 5) sets the one-sitting goal: grade 3 half a page, grade 4 one page, grade 5 two pages (a page is the tool's page box, 250 words). tool.json `modes: []`, `minutes: "15-30 per session"`, `grades_label: "Grades 3-5"`.
- Saving: the issue is kept in this browser (localStorage, try/catch) so the feature can grow over days; the footer always says "Your writing stays on this device. Nothing is sent anywhere." `Clear my issue` removes it. Without storage the tool still works for one sitting and says the issue won't be kept.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| W.3.6, W.4.6, W.5.6 | Warm-ups: type home-row, top-row and word drills with the right fingers shown | a keyboard map lighting the next key and finger | 2 |
| W.4.6, W.5.6 | Quick piece: type a whole piece in one sitting until the page box meets the grade goal | the page filling with a word count | 3 |
| W.3.10, W.4.10, W.5.10 | Quick pieces: a single sitting each (weather note, lunch review, sports brief, ask-the-reporter answer) | the "one sitting" stamp | 3 |
| W.3.10, W.4.10, W.5.10 | Feature: notes session, draft session, revise session, on different days | the feature folder with three dated tabs | 4 |
| W.3.6, W.4.6, W.5.6 | Lay out and publish the issue (pick a template, place pieces, print or save as a file) | the front page and inside page | 5, 6 |

## Screens and modes
Header (kit): title "Deadline Desk"; `Issue`, `Warm-ups`, `Clear my issue`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** The class newsroom: desks, a wall clock, an assignment board, Captain Marsh the editor-in-chief (a walrus in a captain's cap). First hint: "Tap Warm-ups to get your fingers ready." The first tap plays the warm-up line; the welcome is queued after it (`welcomeAfter: true`).

**Warm-ups.** Focus: a keyboard map (760 x 260) with fingers color-and-letter coded, and a drill line above it (one line of 30 to 50 characters). Five drills, unlocking in order: home row (asdf jkl;), home row words (sad, lad, flask), top row added (we, tire, quote), bottom row added (box, can, move), and sentences. Each drill shows accuracy and characters per minute after it ends; the next drill unlocks at 90 percent accuracy, with no speed goal. A wrong key shows on the map; the line waits for the right key (no red flood). Each drill takes about a minute.

**Assignment board.** Four quick pieces and one feature per issue. Each card has a prompt, a reader, and its frame: quick pieces say "One sitting" and the feature says "Three sessions". Grade sets the quick piece length goal (grade 3: about 125 words, grade 4: 250, grade 5: 500 for the main quick piece and 125 for the others). The student picks any order.

**Quick piece.** Focus: a page box (single column, 680 wide) with the prompt above, a word counter, and a soft clock that counts up (no countdown, no buzzer). `File it` works at any length; when the main quick piece reaches its goal in one sitting, it gets the "One sitting, one page" stamp. Leaving and returning means the stamp says "Two sittings" instead, honestly, without blame.

**Feature.** Three tabs: Notes (a list of facts and quotes the student gathers, from a short interview card set: a classmate, a lunch worker, the school librarian, all fictional), Draft, and Revise (the draft beside a checklist: lead, order, quotes, ending). Each tab records the date it was worked on. The feature can be filed only after work on at least two different days; the tab says why: "Features take time to think. Come back another day."

**Publish.** Pick a template (two columns or three), drag filed pieces into slots, add the issue name and date. `Print` prints the front and inside pages; `Save as file` downloads one HTML page of the issue to the device.

At 1366x768 the keyboard map and drill fit without scrolling. At 680x425 the map shrinks to the key row in use.

## Content
- Drills: 5 sets of 6 lines (written for Curio Class; home-row words use only the home-row keys, checked).
- Quick piece prompts (12, three issues of four): Weather Watch ("Tell readers what the weather was this week and what to wear"), Lunch Review, Sports Brief (a recess game), Ask the Reporter ("A first grader asks: why do leaves fall?"), Pet of the Week, Hallway Fix (an opinion), Book Nook, How-To Corner, Library Find, Field Trip Recap, Club News, Thank-You Notes.
- Feature prompts (3): "The People Who Keep Our School Running" (interview cards: lunch worker Mr. Ruiz, custodian Ms. Park, librarian Mr. Adeyemi), "Our Recess Rules" (interview cards: three students), "What Grows in the School Garden" (interview cards: the garden club).
- Feature revise checklist: a lead that pulls readers in; facts in an order that makes sense; at least one quote; an ending that wraps up.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Typing: the page box is a plain textarea; the speech voice reads the student's text back on `Read mine`.
- Drill input listens for key events; Caps Lock on shows a note. Accuracy counts first-try keys.
- Session dates come from the device clock; "different day" means a different calendar date.
- No timer ever ends a piece; the clock is shown for the student's own pacing.

## Look
- Accent `--brand` #23395b ink-navy (header, mastheads, stamps); gold #f4c542 (the "filed" stamp, the next key on the map); paper #f6f7fa; ink #121a26; muted #4f5866. Scene: a busy cartoon newsroom with a big wall clock.
- Contrast (WCAG 2.1, computed): white on brand 11.62:1; brand on paper 10.84:1; ink on paper 16.32:1; muted on paper 6.71:1; ink on gold 10.75:1.
- Never color alone: finger zones have both color and a finger name on each key; stamps are words.
- Different from this batch (office green, car-wash blue, newsprint red, sticker magenta).

## Art
Local FLUX (`scripts/localart.py`); the editor is a walrus, so no people art. Interview card subjects are drawn as animals too (a raccoon custodian, a bear lunch worker, an owl librarian) to keep it to local art.
- newsroom (1): "A bright cartoon school newsroom with desks, a big wall clock and an assignment board, soft gouache, no text"; 16:9; cutout no.
- Captain Marsh (4, point, read, stamp, cheer): "A friendly walrus newspaper editor in a captain's cap <pose>, soft gouache, plain white background"; 1:1; cutout yes.
- interview subjects (9): "<a raccoon custodian with a mop / ...>, soft gouache, plain white background"; 1:1; cutout yes.
- prompt pictures (15): one per prompt; 4:3; cutout no.
About 29 images. Drawn in code: keyboard map, page box, tabs, templates, stamps.

## Voice
Bank voice `firm-captain` as Captain Marsh (unique in this batch). `Curio.voice` with `scope: () => state.screen + ':' + state.piece`, `welcomeAfter: true`.
- event `warm`: "Warm-ups! Fingers on the home row: the bumps go under your pointer fingers."
- how `welcome`: "Welcome to the newsroom, reporter. Quick pieces get written in one sitting. The feature takes a few days. Warm up first."
- event `drillDone`: "Ninety percent or better. Next drill unlocked." / "Close! Try that line again."
- how `boardHow`: "Pick an assignment. Quick ones today, the feature over several days."
- event `filed`: "Filed! One sitting." / "Filed over two sittings. That counts too."
- event `stamp`: "A whole page in one sitting. That's stamina."
- event `notYet`: "Features take time to think. Come back another day."
- how `publishHow`: "Drag your pieces into the paper, name the issue, then print or save it."
- event `published`: "Stop the presses! Issue {3} is out."
Read speaks the hint, which names the next action and control and never a disabled one. No line names a single letter alone.

## Family engine
none

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Drill unlock | Mash keys | The line waits for the right key and accuracy counts first tries; mashing drops it under 90 percent. |
| One-page stamp | Paste text | Paste is blocked in the quick piece box (a note says why); the stamp needs typed words. |
| One sitting | Type over two days | Then the stamp says "Two sittings"; there is nothing to lose, it's just honest. |
| Feature over time | Do it all at once | The feature can't be filed until it has work on two different days. |
| Word count | Type nonsense | Not caught; the tool can't judge content and says so in the teacher note. The paper is read by real people. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap Warm-ups: `warm`, `welcome` (queued, first time).
2. Each drill end: `drillDone`.
3. Board: `boardHow`; filing: `filed`, then `stamp` (waits) when earned.
4. Early feature filing: `notYet`.
5. Publish: `publishHow`; done: `published`.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| W.3.6 to W.5.6 and W.3.10 to W.5.10 wording (grade 4 one page, grade 5 two pages in a single sitting; routine writing over short and long time frames) | thecorestandards.org, Writing Grades 3 to 5 | CCSS ELA 2010 PDF | yes |
| Touch typing starts from the home row, with the raised bumps on F and J under the pointer fingers | BBC Bitesize, Dance Mat Typing | Typing.com, home row lessons | yes |
Backed twice: 2. Cut: 0.

Design choices (not claims): a page is 250 words in the tool's page box; 90 percent accuracy unlocks the next drill; no speed goals.

Checks run (Python, scratchpad b8, 2026-11-08): home-row drill words use only a s d f j k l and the semicolon; 12 quick prompts and 3 features; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 the keyboard map and drill fit; at 680x425 the map shows the active row.
2. Drills light the next key and finger, wait for the right key, and unlock at 90 percent accuracy. (W.3.6 to W.5.6)
3. A quick piece typed in one sitting to the grade goal gets the one-page stamp; returning later changes it to "Two sittings". (W.4.6, W.5.6, W.x.10)
4. The feature records session dates and can't be filed until two different days. (W.x.10)
5. Publish places filed pieces in a template and prints two pages. (W.x.6)
6. Save as file downloads the issue as one HTML page.
7. The issue survives a reload where storage works; `Clear my issue` removes it; the privacy line is always shown.
8. Without a keyboard, warm-ups say why they are skipped.
9. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
10. Motion off: stamps appear without slamming; no network requests.

## Open questions
- None for Cory.
