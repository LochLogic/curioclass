# Living Explainer

## One idea
The student publishes a short web explainer answering "How many moons does Saturn have?" as it stood in 2019, then the newsroom calendar jumps forward and real findings arrive (62 moons announced in May 2023, 128 more in March 2025) along with reader comments, and each time the student updates the piece, changes how the evidence is shown (a sentence, a table, a timeline chart, a link), logs the change in a public change log, and writes a timed response in one sitting, so they learn that published writing can be kept accurate and clear as facts change, and that regular short writing builds the skill.

## Not like
- explainer-studio (7, spec): building one explainer page. Here keeping a published piece accurate over time, grades 9 to 12.
- tough-text-club (9-12, spec, this batch): reading complex texts. Here publishing and revising one's own.
- question-sharpener (12, spec): sharpening a research question. Here answering one whose answer keeps moving.
- verb-switchboard (8, spec, this batch): sentence-level grammar. Here a whole published piece and its log.
- bike-lane-briefing (8, spec, this batch): weighing others' articles. Here owning one's own.

## Who and how
- Grades 9 to 12, ELA, module "Publishing and Updating Writing" (Writing). Standards: W.9-10.6, W.11-12.6, W.9-10.10, W.11-12.10.
- Driver: one student; class mode is "Reader desk", where classmates post comments on a projected draft (tool.json `driver: "student"`). Every finding, comment and draft is read on tap.
- Two stories: "Saturn's Moons" (real findings, 2019 to 2025) and "Mill Pond Swimming" (a made-up town beach question with practice water tests). tool.json `modes: ["Saturn's Moons", "Mill Pond", "Quick writes", "Reader desk"]`, `minutes: "30-45 per sitting"`, `grades_label: "Grades 9-12"`.
- Drafts, the change log and quick writes are saved on this device only (localStorage), and the screen says so: "Your drafts stay on this device. Nothing is uploaded." `Clear my work` erases them. `Print` prints the final piece with its change log.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| W.9-10.6, W.11-12.6 (produce and publish) | Write and publish the first explainer in the web page builder | the published page with a date | 2 |
| W.9-10.6, W.11-12.6 (update in response to new information and feedback) | Revise the piece when a finding or comment arrives; log what changed and why | the page, the diff view and the change log | 3 |
| W.9-10.6, W.11-12.6 (display information flexibly; links) | Choose how to show the evidence: sentence, table, timeline chart or link; the reader check says which reads fastest | the display chooser and the reader check | 4 |
| W.9-10.10, W.11-12.10 (short time frames, single sitting) | Write a timed quick write at each update (10 or 20 minutes) | the timer and the saved quick writes | 5 |
| W.9-10.10, W.11-12.10 (extended time frames) | Keep one piece going across sittings to a final version | the version history | 6 |

## Screens and modes
Header (kit): title "Living Explainer"; `Page`, `Findings`, `Change log`, `Quick writes`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A science desk at a small online magazine: a browser window showing a blank explainer page, a wall calendar set to October 2019, a findings tray and a comments panel; the editor, Grace Odum, waves from the next desk. First hint: "Tap the first finding to hear it." The first tap reads it; the welcome is queued after it (`welcomeAfter: true`).

**Page.** A web page builder: headline, dek, body blocks (paragraph, table, timeline chart, pull quote, link card). The student writes the first version from the 2019 finding card: in October 2019 Carnegie Science announced 20 new moons of Saturn, giving it more known moons than Jupiter. `Publish` stamps a date.

**Findings.** The calendar steps forward. Each step drops a finding card and two or three reader comments:
1. May 2023: 62 new moons announced, bringing Saturn's confirmed total to 145, then 146 later that month. Comments: "Your page still says 2019!", "Why do the numbers keep changing?"
2. March 2025: 128 more moons announced at once, bringing the total to 274; NASA lists 274 confirmed moons. Comments: "Are these even real moons? They're tiny.", "A table would help."
At each step the student revises; a diff view shows what changed. The piece must answer the comments it accepts (why counts change: new telescopes and follow-up observations confirm small, faint moons) or log why a comment was declined.

**Change log.** Each update adds a line: date, what changed, why, source. A log line needs a date, a change and a source; "fixed stuff" fails. The log publishes at the bottom of the page, as real outlets do.

**Display chooser.** For the moon counts the student tries a sentence, a table (year and total) and a timeline chart; a reader check asks three timed questions ("What was the count in 2023?") and shows which version readers answered fastest, and the student picks one and says why. Link cards point to the finding cards (inside the tool; no live links).

**Quick writes.** At each update a single-sitting prompt with a 10- or 20-minute timer: "In 150 words, explain to a sixth grader why the number changed." The timer can be paused once for a break; the writing is saved as it is when time runs out.

**Mill Pond.** A made-up town beach: practice water test results arrive weekly through a summer, and the student keeps a "Can we swim today?" explainer current, with closures and reopenings in the log.

**Reader desk.** The projector shows a student's draft; classmates post comments from their own screens while the page is open.

At 1366x768 the page and side panel fit; at 680x425 the side panel is a tab.

## Content
- Saturn findings from the Sources table, written as short cards for Curio Class with their dates.
- Reader comments, the Mill Pond story and its practice water tests written for Curio Class; Mill Pond is labeled made up.
- Quick write prompts: six per story.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- The student can revise between findings at any time; each `Publish` saves a version.
- With Motion off the calendar changes without flipping pages and charts draw at once.

## Look
- Accent `--brand` #8a3b12 magazine rust (header, page frame, publish button); gold #f4c542 (new changes in the diff, the timer's last minute); paper #fbf4ef; ink #2a1206; muted #6a5548. Scene: a small magazine office with a window at dusk.
- Contrast (WCAG 2.1, computed): white on brand 7.73:1; brand on paper 7.10:1; ink on paper 16.24:1; muted on paper 6.42:1; ink on gold 10.87:1.
- Never color alone: the diff marks added text with underline and removed text with strike-through and labels.
- Different from this batch (newsroom navy, lane green, club purple, calendar teal).

## Art
- People art goes to Gemini: Grace Odum (a Nigerian American woman in her thirties with a headset), 3 poses; "illustrated science editor <pose>, soft gouache, plain white background"; 1:1; cutout yes.
- Local FLUX (`scripts/localart.py`): Saturn with faint dots of small moons (1); a telescope dome at night (1); a small-town pond with a swim sign (1); the magazine office (1).
About 7 images. Drawn in code: page builder, diff, log, timeline chart, timer.

## Voice
Bank voice `wise-mentor` as Grace and the hint voice (unique in this batch); reader comments are read by `casual-peer` (unique in this batch). `Curio.voice` with `scope: () => state.story + ':' + state.step + ':' + state.view`, `welcomeAfter: true`.
- how `welcome`: "You'll publish this page today, and it won't stay right for long. Keep it accurate as the findings come in, and log every change."
- event, whole, `finding`: the finding card.
- event `comment`: the reader comment.
- event `stale`: "Your page still says {2019}. What's changed?"
- event `logAsk`: "What changed, why, and where did it come from?"
- event `time`: "One minute left. Finish your thought."
- event `privacy`: "Your drafts stay on this device. Nothing is uploaded."
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None. Tool-only code: page builder with versions and diff, findings calendar, comment queue, change log checks, display chooser with a timed reader check, quick write timer, localStorage save wrapped in try and catch.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Updates | Add a sentence at the end | The stale check finds the old number anywhere on the page. |
| Change log | Write "updated" | A log line needs a date, what changed and a source from the finding cards. |
| Comments | Ignore them | Each comment must be answered in the piece or declined in the log. |
| Quick writes | Leave them blank | A quick write needs at least 60 words to count, and the print shows its time. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap the first finding: `finding`, `welcome` (queued, first time).
2. First save: `privacy`.
3. Each step: `finding` (whole), then each `comment`; `stale` if the page still holds an old number.
4. Log: `logAsk` as it fires. Quick write: `time` at one minute left.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| W.9-10.6, W.11-12.6, W.9-10.10 and W.11-12.10 wording | thecorestandards.org, Writing 9-10 and 11-12 | CCSS ELA 2010 PDF | yes |
| October 2019: 20 new moons of Saturn announced, putting Saturn ahead of Jupiter | Carnegie Science, announcement October 2019 | Wikipedia, Moons of Saturn (checked 2026-11-09) | yes |
| May 2023: 62 new moons announced, total 145, then 146 | University of British Columbia, May 2023 | Wikipedia, Moons of Saturn, citing Minor Planet Center electronic circulars | yes |
| March 11, 2025: 128 new moons announced, total 274 | NASA Science, Saturn Moons, "274 confirmed moons" (checked 2026-11-09) | University of British Columbia, "2025 Discovery of more Saturnian Moons" | yes |
Backed twice: 4. Cut: 0.

Design choices (not claims): Mill Pond, its water tests, the reader comments and the magazine are made up and labeled.

Checks run (Python, scratchpad b24, 2026-11-09): the saved NASA page says "274 confirmed moons"; the saved Wikipedia text has "62 moons being announced", "up to 145", "to 146" and "128 moons of Saturn were simultaneously announced"; 146 plus 128 is 274; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 page and panel fit; at 680x425 the panel is a tab.
2. The first piece publishes with a date. (W.9-10.6, W.11-12.6)
3. Findings and comments arrive; the stale check fires; updates show in the diff. (W.9-10.6, W.11-12.6)
4. The display chooser runs the timed reader check. (W.9-10.6, W.11-12.6)
5. Quick writes time, save and print. (W.9-10.10, W.11-12.10)
6. Versions persist across sittings on this device; the privacy line shows; Clear my work erases. (W.9-10.10, W.11-12.10)
7. Mill Pond and Reader desk work.
8. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
9. Motion off: calendar and charts change at once; no network requests.
10. Storage blocked: the tool still works for the session and says drafts won't be kept.

## Open questions
- None for Cory.
