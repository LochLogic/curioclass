# Craft lens: research-quest (round 1)

Cold Craft lens on the built bundle `tools/research-quest/research-quest.html`. Frames and logs are in
`S:/CurioClass-codex-scratch/research-quest/craft/f1` and `f2` (drive.py, port 9881, held clicks, Sound on, Motion on
unless noted). Shared audit: `S:/CurioClass-codex-scratch/research-quest/audit-r1`.

## Contract

- One file, 1,587,349 bytes (1.59 MB): under the 2 MB goal.
- No network requests: the bundle has no http(s) URL at all, and `performance.getEntriesByType('resource')` was
  empty after a two-stop walk (f1 shot `net`).
- No console errors or exceptions in any shot (the two driver failures in f1 were my own script, re-run clean in f2).
- Kit used: `Curio.voice`, `Curio.tone`, `Curio.init`, kit css; nothing re-implemented.
- Frame times (rAF over 90 frames, headless Chrome with GPU off as the modest-laptop stand-in): marker walk at
  1366x768 and 1920x1080, idle (glint running) and Trail back open: median 16.7 ms, p95 16.8 ms, max 16.8 ms, none
  over 20 ms.
- Motion off: marker transition 0s, `.calm` set; audit "nothing runs forever" clean.

## Lines and voice check

`__tool.allLines()` and `voice/lines.json` hold the same 31 lines, word for word, in the same order.

| line | kind | expected | spoken |
|---|---|---|---|
| plan (one place toggled 5 times) | how | 1 | 1, then silent x4 |
| go (4 picked, then unpick/repick twice) | how | 1 | 1, then silent x2 |
| save (5 different ways tapped) | how | 1 | 1, then silent x4 |
| gather, gatherNext (4-note run) | how | 1 each | 1 each, then silent |
| toOrganize | how | 1 | 1 |
| placeNote, organize (4 notes placed) | how | 1 each | 1 each, then silent x3 |
| done (Done on, then a step changed) | how | 1 | 1, then silent |
| Mr. Adeyemi reply A (card A tapped 5 times, 4 s apart) | event | 5 | 5 |
| council questions 1 to 5 | event | 1 each as they come | 1 each |
| approved ending | event | 1 | 1 |
| trail | how | 1 | 1 |

- Stale: Next question tapped four times 0.2 s apart, then Start over and Yes: each council line was cut (`hush`) as
  the next arrived; nothing played after the reset (f1 `v-stale-fast`).
- Read: Read during a council line cut it and read; the next Next question started its line at once. With Sound off
  the council line went silent and Read still spoke (f1 `v-read-during`, `v-read-soundoff`).
- First tap (fresh state): a plain stage tap and Motion get the welcome; a question card gets only its own reply; Read
  speaks the hint only; Sound says nothing (f2 `t-stage`, `t-motion`, `t-question`; f1 `t-read`, `t-sound`).
- Order: lines follow the actions in every log.

## Findings

1. **should fix** (general). `src.html:1265-1279`, the pointer drag fallback. `pointerDrag` is set on any pointerdown
   on a note card and cleared only on pointerup; there is no `pointercancel` handler. Chrome fires `pointercancel`
   when an HTML5 drag starts (the cards are `draggable="true"`), so after a real mouse drag the old card id stays
   armed. The next pointerup on any heading more than 8 px away, with no card tapped first, silently moves that old
   card there. Seen: f1 `drag-stale` (pointerdown then pointercancel on the library card, then one held click on "Our
   plan"): `headings` became `{library: 2}` while the hint said "Tap a note card first, then tap the heading where it
   belongs." The note moves while the hint says nothing moved, and it can change the council result. Clear
   `pointerDrag` on `pointercancel` and `dragstart`.
2. **should fix** (family:none). Stop 4 note cards clip each note to two lines at every height under 641 px
   (`src.html:318`; `411` at 600 px wide), with the full text only in a `title` tooltip that touch and keyboard users
   never see. At 1000x625 each card is about 160 px tall with most of it empty above the clipped text. The cut words
   are often what tells a good note from a too-close one, and the student is deciding where each note goes. Seen:
   audit `state-organize-1000x625.png`, `-680x425.png`, `-375x812.png` (audit lead "clipped text span.note-copy",
   confirmed). Let the text use the card's height, or show the full note when a card is selected.
3. **should fix** (family:none). Trail back sends some lines to the wrong stop. `evaluate()` (`src.html:677-679`)
   fixes Stop 4 for questions 2, 3 and 5, and for question 1 once B is chosen. When the place was never visited, the
   deciding choice was at Stop 2 (Plan), yet the line still goes to Stop 4 while its card says "Your visits did not
   bring back this evidence." (`traceEvidence`, `1039`). Done when 2 asks for each line to reach the stop whose
   choice decided it. Found by reading the code; Teaching may confirm on a run.
4. **polish** (general). Read speaks `#hint` plus the whole chapter's `innerText` (`src.html:642-643`), so it also
   reads the caps eyebrow ("STOP 1 / ASK"), the aria-hidden seal ("FRIDAY COUNCIL", "0 / 4 NOTES"), the footer line
   ("Bramble Hill Middle School · Garden Council") and, at Stop 4, "Tap me, then a heading" four times. Seen: audit
   held-click table, row #read. Better: build the Read text from the card's parts (title, choices, status), skipping
   `aria-hidden` and decoration.
5. **polish** (family:none). Trail back: lines from second-row cards run behind first-row cards, so part of "a line
   from each question" is hidden: question 5 at 1280x720 to 1920x1080, questions 3 to 5 at 375 wide. Seen: f2
   `kb-trail.png` (question 5's line vanishes behind the question 3 card), audit `state-trail-back-375x812.png`
   (lead "text hidden under another box", confirmed). Draw the lines above the cards with a light halo, or route them
   around.
6. **polish** (general). Empty stop badges show as small blank white pills under each stop not yet passed (`.stop
   small` keeps padding and background when empty, `src.html:41`). Seen: audit `size-1366x768.png`. Hide
   `.stop small:empty`.
7. **polish** (family:none). Under 641 px tall the marker sits over the current stop's label ("Or[pack]ize" at Stop
   4). Seen: audit `state-organize-1000x625.png`, `-680x425.png`. Lift it above the dot or set it beside.
8. **nit** (general). Two tab stops per council question on Trail back: each SVG `g.trace-path` (`tabindex="0"`) and
   its card button open the same dialog (f2 `kb-trail`: Shift+Tab from Rewind to a stop lands on an SVG path). Make
   the paths `tabindex="-1"` and keep the cards as the keyboard route.
9. **nit** (general). The ending says "Plan approved!" twice, as the heading and as the first words of the paragraph
   under it (audit `state-ending-1366x768.png`); "Not yet." does the same. Drop the repeat from the paragraph.
10. **nit** (general). The bundle's header comment says "Illustrations generated with OpenAI gpt-image"
    (`src.html:14`): a company name in a public file (rule 15), and it contradicts the spec's "All local FLUX";
    prompts.json records 11 of 13 images as gpt-image. If that route was approved, update the spec's Art line and drop
    the company name from the comment. rq-trail-map, rq-garden-bed and rq-garden-bloom have no `people` field (none
    shows people); add `"people": false`.
11. **nit** (general). `L.next` and `L.endingNext` are in `voice/lines.json` but never spoken (hint only; Read reads a
    longer string, so their clips would never play). Drop them from the lines or speak them.

Checked and clean: every control a button of 44 px or more (audit clean at every size); visible focus (f2
`kb-trail.png`); tap-then-tap by keyboard works (f1 `kb-organize`: Enter on a note, Tab to "What monarchs need",
Enter placed it); Trail back answered/missing uses icon and dashes as well as color; Motion and Sound set
`aria-pressed` and their labels. Words: no em dashes in src, notes, lines, prompts or spec; "Curio Class" only;
classroom-safe; privacy stated ("Your quest saves on this device. Nothing leaves it.", and "Only on this device" on
the pack chip at sizes that hide that line). Nothing cultural, Native or hard-history for a sensitivity review.

## Audit pilot

- Leads confirmed: Stop 4 clipped note text (finding 2); Trail back lines hidden under cards (finding 5).
- Leads wrong or harmless: the many Trail back "overlap" rows between route groups and stop labels are the lines'
  bounding boxes, by design (lines end at the stops); the pack list "1 of 6 controls out of view" at 1280x720 is a
  working scroll panel; "welcome not heard" after a question card, the pack chip or Start over is a first-tap cut
  (BASELINE rule 16) and the premise stays on screen and in Read.
- Missed by the audit: the stale pointer drag that moves a card (1), Trail back stop targets (3), what Read actually
  says (4), empty badge pills and the marker over the label (6, 7), doubled tab stops (8), doubled ending words (9).
