# Research Quest: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: research-quest

#### Built

Built the five-stop research story, all six sources, five note methods, source retention, outline, plan choices, council rules, three endings and interactive Trail back. The research pack, confirmed Rewind and Start over, local save, keyboard alternative, Motion, Sound and Read work.

Required files are in tools/research-quest/. tool.draft.json has stage built. The offline bundle is 1,514,451 bytes, about 1479 KB, below 2 MB. No commits, branch changes, submissions or polish round.

#### Numbers check

Independent model: S:/CurioClass-codex/_scratch/research-quest/numbers.py and numbers.json. Seed 20261031, 200,000 random runs: 197,141 not yet, 2,858 homework, 1 approved. These are random choices, not estimates of student success. The ideal and source-credited quotation runs answer five questions. All three endings occur, questions range from five to seven, and at most seven are unanswered.

The shipped evaluator separately passed the ideal run, five isolated core failures, quotation, unmarked copying, changed meaning, seed mix, unused changed/close notes, empty outline, and two/three missing-answer boundaries. Evidence: model-checks.json. Supplied biological numbers and fictional dates were preserved.

All supplied contrast ratios reproduce: white/brand 5.47, brand/paper 4.85, brand/panel 5.26, ink/paper 13.61, muted/paper 5.68, muted/panel 6.16, focus/panel 7.58, focus/paper 6.99, white/brass 5.05, green/panel 4.82, red/panel 6.22.

#### Feel check

Played the complete quest through real held clicks at a two-second pace, then a complete run using only Tab, Shift+Tab and Enter. Both reached approval and Trail back. The keyboard run used credited quotations; the first used good paraphrases.

Best moment: the council places a meaning-changing note beside the original passage, and the resulting line takes you back to that exact note. The supported plan also earns the painted change from bare soil to milkweed and asters. Different choices change the optional questions and named homework.

Flattest moment 1: gathering risked feeling like a form. Painted source scenes, clipped paper, immediate saved-note wording/source and a paper response give each decision a visible result.

Flattest moment 2: early Trail back arcs did not land on their own cards. Endpoints now come from rendered card and stop positions and update on resize. Compact labels leave room for curves. The library desk was enlarged into a second opening panel on laptops so its painting can be enjoyed.

Compared snowy-mail-route and beat-lab at 1366x768. The finished council has a layered painted room, active brass nameplate and central paper answer, matching the bar in finish while keeping its parchment world.
![Research Quest beside Beat Lab](S:/CurioClass-codex/_scratch/research-quest/feel-comparison.jpg)

#### Done when

1. PASS. The ideal B/library/county/nature/notebook run, good notes with sources, proper headings, milkweed and fall flowers answers all five and is approved. Real click run plus model-checks.json.
2. PASS. Each core question fails alone after one earlier change. Trail targets return to Ask or Organize for question 1, Organize for 2/3/5, and Gather for source retention. Read-only cards show the actual choice, heading and relevant plan steps.
3. PASS. Questions 6/7 are conditional; unused notes do not trigger changed/close checks; the empty-outline answer uses the exact required sentence. Model checks and source-comparison frame.
4. PASS. Zero, one/two, and three-or-more missing answers produce the specified endings. Homework names the missing pieces and joins two with and. All three endings inspected.
5. PASS. A real fifth visit is refused; four saved notes gate Stop 4; every note must be placed; a fourth plan step is disabled with the reason shown. Real jittered drag and tap-then-tap both work.
6. PASS. No preserves the run. Rewind to Gather retains four notes and clears later work. Actual Page.reload preserves question B and Stop 2. Confirmed Start over removes rq-run and returns to empty Ask. Evidence: interaction frames and check_reload.py.
7. PASS. The chapter dominates the stage at 1280x720, 1366x768 and 1920x1080. Council speech is central. Full-size and audit frames inspected.
8. PASS. Rapid council clicks advance immediately and cut stale speech. Fast audit paths accept choices during marker movement. Resizing leaves no exception or disabled lock.
9. PASS. All 13 images load; no person is pictured. Six painted place tiles have code labels; page/ad/play marks are code. Final badge check reports zero broken visible images.
10. PASS. Chapter choices and main buttons fit all eight required sizes. All six source variants fit at 680x425. Phone checks use the real 375x812 host. Compact note excerpts are deliberate; full notes remain in the pack and Read.
11. PASS for implemented behavior. How lines speak once, council events occur and go stale correctly, Read works with Sound off, and final drive checks have no console errors. No external requests. Voice bank is smooth-narrator; recordings are deferred as required.

#### Wave lessons

- BR1 Hint/voice: PASS. Hints update synchronously, name enabled controls, use V.heard for the welcome/Ask distinction, and Read uses the current chapter/dialog. The two-second log contains each how line once and all five council questions.
- BR1 Focus/layout: PASS. No focus on load. Selections and note placement retain controls; intentional focus uses preventScroll. Audit settled focus and Enter paths are clean.
- BR1 Sizes: PASS. All required sizes and hosted 375 were inspected. The undersized Yes is fixed and measures 44 by 44.
- BR1 No giveaways: PASS. Neutral selection states, shuffled paraphrases, no score, truth meter or answer labels. Judgment waits for the council.
- BR1 Honest numbers: PASS. Visit, note and plan counts reflect actual state and fixed limits. Fictional documents are identified in notes/metadata.
- BR1 Standards: PASS. Question, source plan, note wording/source choice, outline and audience consequences are solo activities covering the listed process skills. Family engine: none.
- BR1 Motion off: PASS. Manual check reports zero infinite animations; audit clean. Marker becomes instant without locking input.
- Network short choices: PASS. Six places, five note methods, four note cards/headings and five plan options remain in the chapter. The pack is a collection with a full-pack dialog; it is not the only route to a research choice.
- Network resize: PASS. Audit flips to 760x900 and back after every state input and walk control: no exceptions or stuck controls.
- Network late welcome: PASS. A first question tap speaks its own reply and skips the welcome unmarked, as STANDARDS requires. Open dialogs now invalidate the background welcome.
- Network unknown: PASS. Bare garden until approval; no premature correctness marking.
- Network one look/meaning: PASS. Solid green/check paths answer; dashed red/cross paths do not. Teal means selected/current.
- Network truthful badges: PASS. Finished stops show the chosen question, four place pictures, note count and outline. Actual council results decide approval.
- Network hint returns: PASS. Visit changes, Redo, chapter changes and rewind update the current hint immediately.
- Network copying words: PASS. Quotation/paraphrase comparison is the lesson. No good/too-close/changed labels are exposed; consequences wait for the council.

#### Audit leads

One complete audit, about 27 minutes, exit 0. Full result: S:/CurioClass-codex/_scratch/research-quest/audit/audit.md. All 113 leads are covered below. The full audit was not repeated; fixes received targeted checks.

- 2 Ask overlap leads at 680: FIXED. The tight preview uses the picture caption for the brief, leaving all questions, replies and On to Plan clear. All four replies and the final opening at all eight sizes were re-shot without overlap.
- 3 pack-row overlap leads at 1280 in council/ending/trail: FIXED. Rows no longer shrink below their content. Targeted geometry shows no overlap. The collection can scroll; the chip opens every item in a dialog.
- 2 small Yes leads across compact/phone sizes: FIXED. Buttons have a 44-pixel minimum width. Compact Yes measures 44 by 44.
- 4 note-copy clipping leads: INTENTIONAL EXCERPTS. Compact cards show two lines; title, accessible text, pack and Read retain the full wording. All note controls/headings remain visible. Source meaning is unchanged.
- 1 mobile steps keep-region lead: INTENTIONAL EMPTY CELL. Five plan steps occupy five cells of a six-cell grid; Done uses the reserved sixth cell. No plan choice is covered.
- 97 Trail geometry/nested-label leads: INSPECTED, NO VISIBLE OVERPAINT. Path-only SVG groups contain curves and transparent 44-pixel hit paths, not rectangular text panels. Bounding boxes overlap by construction. HTML labels are readable in the inspected frames. A real curve click opened the correct Gather evidence card without changing the run.
- 4 welcome-not-heard leads on A/B/C/D: EXPECTED. Each first tap queues its own librarian reply, so STANDARDS says to skip the welcome without marking it said. Queuing it afterward would cause the late-welcome defect.
- Audit Motion off, resize, settled focus, five held repeats and two quick taps are clean. Browser errors absent. The helper log has a closed HTTP socket ConnectionResetError during teardown; the audit completed with exit 0.
- Additional guard fixed during review: background welcome cannot name inert question cards behind an open dialog. Dialogs name the next control. First-pack-dialog check confirms no welcome spoke over it.
- Final changes after the audit: that guard, visit badges, the fixes above and larger opening desk art. Only affected checks/frames were repeated.

#### Frames looked at

All manual PNGs were inspected through contact sheets and full-size checks of defects/key scenes. All 73 audit PNGs were reviewed in per-state sheets, with critical mobile/Gather/organizer scenes opened full size.

Scratch: S:/CurioClass-codex/_scratch/research-quest/. Frame folders: small-frames, compact-fix, functional-frames, size-frames, fixed-frames, final-fixed-frames, phone-fixed, phone-last, interaction-frames, ending-frames, edge-fixed-frames, source-extreme-frames, audit, audit-fix-frames and ask-art-frames. Bar frames: snowy-mail-route and beat-lab.

Final opening checked at 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900 and hosted 375x812. Also inspected: grayscale, Motion off, complete keyboard run, drag, all sources/endings, meaning comparison, rewind and dialogs.

#### Art made

13 finished images: 954,126 bytes, about 932 KB. Ten made with the built-in image tool during this build: marker, library desk, six place scenes, council room and replacement blooming garden. Three retained paintings: map, empty bed and caterpillar.

Blooming garden redrawn once because the inherited picture lacked recognizable milkweed. The replacement shows broad milkweed leaves, pink clusters, purple asters and a monarch. No people, faces or body parts generated.

Assets: S:/CurioClass-codex/research-quest/tools/research-quest/art/. Prompt catalog: art/prompts.json. Originals: art/raw/. Finished files processed only with art.py --rekey. Credits identify OpenAI gpt-image and the three local FLUX paintings. preview.svg is code drawn.

#### Art still to paint

None. No deferred people assets or labeled placeholders.

#### Engine changes wanted

None in the kit. handoff.md records a possible audit-helper improvement: scripts/audit_tool.py, PAGE_JS should distinguish accessible names on path-only SVG groups from painted text and test path geometry rather than rectangular group bounds. No shared engine or script was edited.

#### Left open

Narration recordings were intentionally not created. Browser speech supplies behavior until the separate recording pipeline uses the supplied 31 lines and Algieba configuration.

The 20-30 minute classroom duration is the spec's intended pace, not a measured classroom study. Compact organizer excerpts and council slide headings are deliberate; complete wording remains in the pack and Read.

host.html removed. Every Chrome and host started here is closed; no listener remains on 9980, 9981, 9982 or 8785. Final git status contains changes only in tools/research-quest/. Build only, ready for the separate cold review.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: research-quest
#### Played
Cold complete Grade 7 held-click run before builder notes/source, Ask through approval and Trail back; then a complete keyboard-only run and teacher/projector checks. The painted world is inviting, and saved research choices earn specific consequences.
#### Findings fixed
- should fix, general, Organize/how: selecting a note after Done became live still instructed Press Done. Selected-note hint now wins; queued hints validate the actual selection/readiness.
- should fix, general, pack dialogs/openDialog: nested content removed the focused item and replaced the focus-return anchor. Nested cards now focus their first live control and preserve the original anchor; Enter closes back to the pack chip at all eight sizes.
- should fix, general, Read: textContent joined adjacent headings and answer letters into words. Read now uses rendered text boundaries.
- should fix, general, compact ending: audit frame state-ending-680x425 showed the garden image under the recap status. Constrained the image's grid row; all three endings, including the too-close aside, rechecked at 680, 800 and 1000 widths.
- should fix, general, compact Organize: audit frame state-selected-ready-outline-680x425 showed heading/note rows growing into the plan-step count. Constrained the grids and added titled source-name ellipses. Three/four notes in one heading rechecked at 680, 800 and 1000 widths.
- polish, general, Trail back: crossing curves made the earned causal recap flat. Hover and keyboard focus now isolate the matching curve and its stop; wide cards and read-only evidence cards name the actual earlier choice.
- should fix, general, art/rq-caterpillar: inherited cartoon anatomy/style weakened a biological source card. Repainted in botanical ink/watercolor, keeping the monarch and milkweed readable in the final crop.
#### Findings left
- should fix, general, spec Content/question 4: the mandated reply calls every unmarked quotation the book's words, including interviews/pages. Exact spec wording retained; correcting it needs a spec decision.
- Scope limitation, module/AASL.Collaborate: responses are automatic by specification. Students assemble the supporting evidence, but do not compose replies to the audience. Deeper response practice would change the specified interaction; catalog writes are outside scope.
#### Flattest moment left
Four predefined note selections repeat the same mechanic. The source comparisons and exact saved notes give them purpose; adding a writing mechanic would exceed the spec.
#### Graphics
All 13 assets checked in rendered scenes and art contact sheet; none shows a person. One caterpillar repainted using the built-in image tool; raw art and final prompt description are in art/raw/rq-caterpillar.png and art/prompts.json. Mobile contains its whole body. Two inherited local FLUX paintings remain; the source credit was corrected. Art: 1,005,892 bytes (982.3 KB). Bundle: 1,587,349 bytes (1550.1 KB), below 2 MB.

All eight STANDARDS sizes inspected, including hosted 375x812; additional compact/phone Plan, Gather, Organize, council and seven-question Trail back extremes. Motion off and grayscale inspected. Compared the existing Beat Lab and Snowy Mail Route bundles without writing their folders. The warm painted desk, source scenes, council room and garden payoff remain intact.
#### Audit
One final audit, exit 0, 1,797 seconds (29 minutes 57 seconds), 124 leads; _scratch/research-quest/review-audit/audit.md. All 89 frames inspected. Disposition of every lead:

- 2 compact organizer overlaps and 1 nested-dialog focus loss: fixed and specifically rechecked. Also fixed the ending-image/status collision seen in the audit frames, which the mechanical rows missed.
- 8 compact note-copy rows: designed excerpts with full titles, full pack cards and Read; no answer choice or heading is hidden.
- 4 pack-scroll rows: collection, not the answer set; the pack chip opens every item. All immediate research choices remain in view.
- 1 mobile steps keep-region sample: Done intentionally occupies the sixth cell beside five plan steps; all five choices are visible.
- 102 Trail geometry/nested-label rows: inspected, no painted text obscured. Path groups have accessible names and broad transparent hit paths, not rectangular painted panels. Actual curve/card keyboard use opens the right read-only evidence.
- 6 welcome skips: four first question taps speak their own reply; two modal-opening taps suppress instructions for inert background controls. Welcomes stay unmarked. This follows the standing voice rules.

Motion off, repeated/quick held clicks, settled focus and resize checks were clean; no tool console errors. The helper logged a closed local HTTP socket during teardown and still exited 0. Final fixes received only targeted rechecks; the full audit was not repeated.

Independent evaluator checks: ideal, each question 1-5 failing alone, credited quotation, unmarked copy, changed meaning, seed blend, empty outline, and ending boundaries passed. Keyboard checks passed four-visit/three-step limits, complete quotation run, approval, trace, real reload, Rewind No/Yes retaining Gather notes and clearing later work, and Start over removing rq-run. No tool exceptions or external requests; manual host favicon 404 is in the generated test wrapper only.

Voice registry matched allLines exactly. Held input counts:

| Line | Kind | Expected | Spoken |
| --- | --- | --- | --- |
| Topic-choice reply, five repeats | event | 5 | 5 |
| Tap a heading, five placements | how | 1 | 1 |
| Press Done, five placements | how | 1 | 1 |
| Three rapidly advanced council questions | event | 3, old speech cut | 3, old speech cut |
| Read with Sound off | read | 1 | 1 |

Read boundary fix was verified from the actual log. Contrast recomputed independently: minimum 4.82:1 across all 11 specified pairs. Wave checks covered live hints, preserved focus, targets, no premature answer marking, honest counts, solo defaults, calm animation, source meaning, state-matched labels and resize.
#### Left open
The two spec limitations above remain. Browser narration continues until separate recordings exist; no recording was made. No kit/catalog/shared files were changed and no git commits were made. All Chrome and host processes started here are closed; host.html is absent.

<!-- end part -->

## Refine

<!-- part: refine.md -->

OPEN (round 1, Claude Refine 2026-11-05; Codex fixes next)
Counts: blockers 2 (general 2, family 0), should fix 8 (general 8, family 0), polish accepted 15

### Refine: research-quest

Lenses: teaching.md, play.md, craft.md (no sensitivity.md; all three lenses found nothing cultural, Native or
hard-history). Not a Curiosity. Integrator spot-checks: read src.html 664-700 (`evaluate`, `answerText`), 790-797
(save buttons), 838-848 (`endingView`), 1035-1042 (`traceEvidence`), 1262-1279 (pointer drag fallback); each claim
below that cites those lines was confirmed in the code.

#### Blocker
1. **Trail back points to the wrong stop when the cause was not at Stop 4.** src.html:677-678 (`references` in
   `evaluate()`), with `traceEvidence` at 1039. The stop is fixed per question (`['library',4]`, `['county',4]`,
   `['nature',4]`, notebook 4 once B is chosen), so leaving a useful place out at Plan sends the red line to
   "4 Organize" while its own card says "Your visits did not bring back this evidence." The student rewinds to
   Organize and finds nothing to fix. Same flaw the other way: question 4 with an empty outline (every note in Not
   needed) points to Stop 3, but the cause is Stop 4. This is the tool's one idea and fails Done when 2. Seen:
   teaching/frames skiplib-trail.png, skiplib-trace-q2.png, allnotneeded-trail.png, teaching/logic-out.json
   (q1/q2/q3/q5 not-visited runs all `X@4`); play/out/fail-trail-1366.png, trail-click-q1.png; craft finding 3
   (code read). Fixed: compute the stop from the actual cause for each result: place never visited = Stop 2 (card:
   "You did not plan a visit to [place]."); note saved without source, copied without quote marks, or meaning
   changed = Stop 3; note in Not needed, wrong heading, or missing plan step, or an empty outline for question 4 =
   Stop 4; question not B = Stop 1. Add a failing run (one skipped useful place, one all-Not-needed run) to
   `audit-states.json` so the audit sees a red trail. (general)

#### Should fix
2. **"Save note with its source" is styled as the right answer.** src.html:796: `save-note` gets the plain class
   `''`, `save-source` gets the default primary (teal) style. Spec: choices "never show right or wrong when made".
   Seen: audit-r1/state-gather-1366x768.png. Fixed: both save buttons the same style (both plain, or both primary).
   (general)
3. **A stale pointer drag can silently move a note.** src.html:1265-1279. `pointerDrag` is set on pointerdown and
   cleared only on pointerup; there is no `pointercancel` or `dragstart` handler, and Chrome fires `pointercancel`
   when the HTML5 drag starts on the `draggable` card. The next pointerup on any heading 8 px or more away moves the
   old card while the hint says "Tap a note card first...". Seen: craft/f1 `drag-stale` (`headings` became
   `{library: 2}`). Fixed: clear `pointerDrag` on `pointercancel` and on `dragstart`. (general)
4. **Organize note cards clip the note to two lines, with empty space above it.** src.html:318 (and 411 at 600 px
   wide), `.note-card .note-copy`, at every height under 641 px and at 375 wide. The cut words are what tell a good
   note from a too-close one, and the source line ("× no source") is cut too; the full text is only a hover
   `title` that touch and keyboard users never get. All three lenses and the audit lead agree. Seen:
   audit-r1/state-organize-1000x625.png, state-organize-680x425.png, state-organize-800x500.png,
   state-organize-375x812.png. Fixed: text starts at the top of the card and uses its height; the source line is
   never clipped; a selected card (tap-then-tap) shows the full note. (general)
5. **"Those are the book's exact words... name the book" on notes not from the book.** src.html:694. Question 4's
   note can be the county page or the club notebook, and the source line can be shown right above "name the book".
   Seen: teaching out-county-copy-q4.json, out-notebook-copy-q4.json; frames county-copy-q4.png,
   notebook-copy-q4.png. Fixed: "Those are the exact words from [source title]. Put them in quote marks." and, when
   the note has no source, "...Put them in quote marks and name where they came from." Update the matching line in
   spec.md Content (question 4) to the same wording; it is a factual correction, not a rule change. (general)

#### Polish accepted
6. **Ending repeats its heading.** `endingView()` (src.html:842-848): "Plan approved!" heading then "Plan
   approved! ..." in the paragraph; "Not yet." the same. Drop the repeat from the paragraph (spoken line unchanged).
   Seen: audit-r1/state-ending-1366x768.png, play/out/fail-ending-1366.png. (general)
7. **Homework list blurs when piece 1 is missing.** src.html:843-844. "a clear question and what our garden has now
   and when the flowers should bloom." Join pieces with ", and " (or "; and ") so piece 1's own "and" reads clearly.
   Seen: teaching two-missing-ending.png. (general)
8. **Meaning-changed paraphrase is always the shortest.** spec Content, src.html:525-576 (good/close/changed
   lengths, e.g. nature 120/123/42, county 143/131/66). "Skip the short one" solves it without reading. Rewrite the
   six changed versions to be about as long and fluent as the good one (within about 15 percent), same wrong
   meaning; e.g. nature "Grown monarchs feed on nectar from many flowers, mostly in spring before they head north."
   Update the same strings in spec.md Content. Seen: teaching lens length table. (general)
9. **Question 4 does not show which note it asks about.** src.html:688-695. Show the note's text above the source
   line in the speech card. Seen: teaching nbcopy-q4.png. (general)
10. **Trail back lines hidden under cards.** Lines from second-row cards (Q5, Q7; Q3-Q5 at 375 wide) run behind
    first-row cards. Draw the lines above the cards with a light halo, or route them around. Seen:
    play/out/fail-trail-1366.png, trail-focus-q5-1366.png; craft/f2 kb-trail.png;
    audit-r1/state-trail-back-375x812.png. (general)
11. **Trace card has no way to act.** `trace()` dialog says "Follow it to Stop N" but offers only "Back to quest".
    Add "Rewind to Stop N" that goes through the existing Yes / No check. Seen: play/out/trail-click-q1.png.
    (general)
12. **After a saved note the hint points to the pack while the place buttons are right below.** `how()` stop 3,
    `gatherNext`. On layouts where `.visit-tab` shows in the card, say "Tap the next place below."; keep the pack
    wording where the tabs are hidden (this is a hint change only; keep the spoken line if its clip exists, or
    update lines.json to match). Seen: audit-r1/state-saved-note-1366x768.png. (general)
13. **Read reads decoration.** src.html:642-643 reads the chapter `innerText`: caps eyebrow, aria-hidden seal
    ("FRIDAY COUNCIL", "0 / 4 NOTES"), footer, "Tap me, then a heading" x4. Build the Read text from the card's
    title, choices and status, skipping `aria-hidden` and decoration. Seen: audit held-click table row #read.
    (general)
14. **Empty stop badges show as blank white pills.** src.html:41 `.stop small`. Hide `.stop small:empty`. Seen:
    audit-r1/size-1366x768.png. (general)
15. **Marker covers the current stop's label under 641 px tall.** ("Orga ze", "Ga er"). Lift the marker above the
    dot or set it beside the label. Seen: audit-r1/state-organize-680x425.png, state-gather-680x425.png,
    state-organize-1000x625.png. (general)
16. **Nit: two tab stops per council question on Trail back.** SVG `g.trace-path` has `tabindex="0"` and its card
    opens the same dialog. Set the paths to `tabindex="-1"`; cards stay the keyboard route (paths stay clickable).
    Seen: craft/f2 kb-trail. (general)
17. **Nit: company name in the bundle header and missing people flags.** src.html:14 "Illustrations generated with
    OpenAI gpt-image" (rule 15): drop the company name (e.g. "Illustrations generated for Curio Class"). Add
    `"people": false` to rq-trail-map, rq-garden-bed and rq-garden-bloom in prompts.json. (general)
18. **Nit: unused lines.** `L.next` and `L.endingNext` are in voice/lines.json but never spoken. Remove them from
    the spoken lines (keep them as hint text). (general)

#### Settled calls
- **Blocker count.** Teaching had two blockers, Play one, Craft rated the Trail back stop a should fix (from code
  only). Teaching and Play confirmed it on runs, so it stays a blocker. Teaching's blocker 2 (unsourced copies
  approved) is also a blocker: see item 19 (integrator call, 2026-11-06).
- **Severity of clipped Organize cards.** Teaching polish, Play and Craft should fix: should fix, since the cut
  text is the information the student sorts by.
- **Audit "overlap" rows on Trail back.** All three lenses agree they are the 44 px transparent hit strokes and
  the lines' bounding boxes, not visible clutter. Only the visible lines-under-cards case (item 10) is taken.
- **"Welcome not heard" after a first tap on a question card, the pack chip or Start over** is allowed (BASELINE
  rule 16). Do not change.
- **Pack list at 1280x720 / 1366x768** is a working scroll panel (Craft); not a fix.
- Keep the ending bands and the seven questions. The council rules change only as items 19 to 22 say.
- Keep "Copy it, with quote marks" a valid, approvable choice for some notes.

#### Integrator calls (2026-11-06, BASELINE: a check must reward the right practice; rule 2 for codes)

The merge routed these to the spec's open questions. They are settled here from Cory's standing rules, not sent to
Cory: the tool claims Engage VI.B.1 (quote and paraphrase with credit), so a council that approves uncredited copies
fails the spec's own "Scores and checks reward the right thing" lesson. Update spec.md's Content and Done when to
match each change.

19. **Blocker: unsourced or unquoted copies are approved.** Save the library note well with a source and the other
    three as "Copy it, no quote marks" with no source: "Plan approved!" with five ticks (teaching onlylib-ending.png,
    onlylib-trail.png). Fix: question 4 checks every outlined note, not one. Any outlined note copied without quote
    marks or saved without a source brings back question 4's challenge for that note (name the note), and Trail back
    points to Stop 3. Re-run the brute force on the council: the all-good plan approves, every uncredited copy fails.
20. **Should fix: quoting everything wins.** Four quotes with sources, obvious headings: approved with no aside
    (play/out/quote-all-ending.png). Fix: when every outlined note is a quote, one council member asks "Can you say
    that in your own words?" as an uncounted aside (the plan still approves; the paraphrase cards now have a reason).
21. **Should fix: meaning-changed notes still answer questions 2, 3 and 5.** All-changed run counts Lily's question as
    held (teaching allchanged-q2.png, allchanged-ending.png). Fix: a question whose answering note is the changed
    version is not answered, and Trail back points to Stop 3.
22. **Should fix: "Not yet" ending names nothing to do (Play 5).** Give it the same named missing pieces as the
    homework ending.
23. **Should fix: AASL Collaborate is represented, not taught (Teaching 5).** Answers are filled in automatically.
    Drop the Collaborate code from the tool's standards (tool.draft.json, spec Map and Standards map, notes.md),
    BASELINE rule 2; note the move in notes.md so the catalog can give it to a tool that teaches it.
24. **Polish: Mr. Adeyemi's reply to B reads as "correct" (Play 10).** Give it a question back, e.g. "Good. What will
    you need to find out first?", so the four replies stay even.
25. **Polish: spec Art line says "All local FLUX"** but prompts.json records 11 of 13 images as gpt-image (Craft 10).
    Correct the spec's Art line to what prompts.json records; flag any people image for Cory's contact sheet.

#### Not taken
- Stop labels moved onto the painted clearings (Play 4, second half): needs art-coordinate rework; revisit at Final
  look with the real map.
- Question 3 accepting the county note under any heading (Teaching 12): matches spec, harmless.
- Pack list cut at 1280x720 (Play 9): working scroll panel, not clipped content.

<!-- end part -->

<!-- part: refine/craft.md -->

### Craft lens: research-quest (round 1)

Cold Craft lens on the built bundle `tools/research-quest/research-quest.html`. Frames and logs are in
`S:/CurioClass-codex-scratch/research-quest/craft/f1` and `f2` (drive.py, port 9881, held clicks, Sound on, Motion on
unless noted). Shared audit: `S:/CurioClass-codex-scratch/research-quest/audit-r1`.

#### Contract

- One file, 1,587,349 bytes (1.59 MB): under the 2 MB goal.
- No network requests: the bundle has no http(s) URL at all, and `performance.getEntriesByType('resource')` was
  empty after a two-stop walk (f1 shot `net`).
- No console errors or exceptions in any shot (the two driver failures in f1 were my own script, re-run clean in f2).
- Kit used: `Curio.voice`, `Curio.tone`, `Curio.init`, kit css; nothing re-implemented.
- Frame times (rAF over 90 frames, headless Chrome with GPU off as the modest-laptop stand-in): marker walk at
  1366x768 and 1920x1080, idle (glint running) and Trail back open: median 16.7 ms, p95 16.8 ms, max 16.8 ms, none
  over 20 ms.
- Motion off: marker transition 0s, `.calm` set; audit "nothing runs forever" clean.

#### Lines and voice check

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

#### Findings

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

#### Audit pilot

- Leads confirmed: Stop 4 clipped note text (finding 2); Trail back lines hidden under cards (finding 5).
- Leads wrong or harmless: the many Trail back "overlap" rows between route groups and stop labels are the lines'
  bounding boxes, by design (lines end at the stops); the pack list "1 of 6 controls out of view" at 1280x720 is a
  working scroll panel; "welcome not heard" after a question card, the pack chip or Start over is a first-tap cut
  (BASELINE rule 16) and the premise stays on screen and in Read.
- Missed by the audit: the stale pointer drag that moves a card (1), Trail back stop targets (3), what Read actually
  says (4), empty badge pills and the marker over the label (6, 7), doubled tab stops (8), doubled ending words (9).

<!-- end part -->

<!-- part: refine/play.md -->

### Play lens: research-quest (round 1)

Played twice: once as a grade 6-8 student alone (ideal run, a careless run that skipped two useful places and
quoted the Butterfly Blend ad, and a "quote everything" cheap run), once as a teacher projecting at 1366x768.
My frames: `S:/CurioClass-codex-scratch/research-quest/play/out/`. Shared audit frames:
`S:/CurioClass-codex-scratch/research-quest/audit-r1/`.

The story holds up well for a solo student: every stop's first screen names the action, the pack and stop badges
make progress clear, the council speech card is center stage, and the persistence across reloads worked (my later
shots reopened straight into the saved trail state). The problems are in the payoff and in how cheaply it can be won.

#### Findings

1. **Trail back sends "didn't visit it" failures to Stop 4, not Stop 2.** blocker, general
   - Where: `src.html` `evaluate()`, the `references` table (`['notebook', run.question !== 1 ? 1 : 4], ['library',4],
     ['county',4], ... ['nature',4]`): the stop is fixed per question, whatever choice actually caused the miss.
   - What: skip the garden club notebook and the nature center at Plan, and the trail draws Q1 and Q5 as
     "Still missing · Stop 4" into **4 Organize**, while the evidence line under the same card says "Your visits did
     not bring back this evidence." Opening the line gives "Trail back · Organize ... Follow it to Stop 4 ... No
     matching note in the outline." A student who rewinds to Organize finds nothing to fix there; the real cause was
     the Plan choice. The same happens for Q2 and Q3 if the library or county office is skipped. The Trail back is the
     tool's one idea ("each council question traces a line straight back to the choice that answers it") and spec
     Done when 2 asks that each failed rule's line goes to the stop whose choice decided it. A readout that points to
     the wrong cause is a blocker.
   - Better: compute the stop from the actual cause: not visited = Stop 2, not saved or meaning changed or no source =
     Stop 3, in Not needed / wrong heading / missing plan step = Stop 4, wrong question = Stop 1. Also Q4 with an empty
     outline currently points to Stop 3; the cause there is Stop 4.
   - Seen: `play/out/fail-trail-1366.png`, `play/out/trail-click-q1.png`, `play/out/trail-1000.png`.

2. **Quoting every source word for word earns a full approval; paraphrasing is never needed.** should fix, general
   - Where: `evaluate()`: Q2, Q3, Q5 ignore the note's way; Q4 accepts `quote` with a source; the too-close aside only
     fires for version 1.
   - What: the cheap sweep (tap "Copy it, with quote marks" and "Save note with its source" four times, then the
     obvious headings) gets "Plan approved!" with no aside at all. The three "In my own words" cards, the most
     interesting choice in the tool, are skippable at zero cost, and "always quote, always cite" is exactly the habit
     a grade 6-8 research lesson wants to move past (an outline of four block quotes is a pile, not a case; the chapter
     title says "Make a case, not a pile"). A teacher projecting it will see the class find this in one run.
   - Better: real material, not a penalty game: e.g. when every outlined note is a quote, Principal Okoro (or Lily)
     asks one more question, "Can you say that in your own words?", that only a good paraphrase answers; or the slides
     at Stop 5 show the quotes and a council member reacts. Keep "quote marks are acceptable" for one or two notes.
   - Seen: `play/out/quote-all-ending.png`.

3. **Organize note cards clip the note to two lines while the card is mostly empty.** should fix, general
   - Where: Stop 4 `.note-card .note-copy` at 680x425, 800x500, 1000x625 and 375.
   - What: at 1000x625 each card is about 160 px tall with the text pushed to the bottom and cut ("...so no milkweed
     means no..."), with a large blank area above it. The student has to place notes by meaning, and a too-close or
     changed version can only be told apart by reading it; the full text lives only in a hover `title`. Confirms the
     audit's clipped-text lead.
   - Better: let the copy fill the card from the top (no clamp when there is room), clamp only when truly short of
     space, and give the open card in the pack the full text.
   - Seen: `audit-r1/state-organize-1000x625.png`, `audit-r1/state-organize-680x425.png`.

4. **Trail back lines run under the cards and the painted map does not match the stops.** polish, general
   - Where: Trail back, all sizes (audit overlap leads, confirmed).
   - What: lines from the second row of cards (Q5, Q7) start under the first-row cards and are hidden for part of
     their run; with five or more lines converging on "4 Organize" the picture becomes a fan of identical curves. The
     painted trail and its clearings sit in different places from the code stop labels in a row along the top, so the
     lines end on labels, not on places on the map. Better: one row of cards, or lines routed around cards, and stop
     labels placed on the painted clearings so the line lands on the place where the choice was made.
   - Seen: `play/out/fail-trail-1366.png`, `play/out/trail-focus-q5-1366.png`, `audit-r1/state-trail-back-1366x768.png`.

5. **The ending lands flat and repeats itself.** polish, general
   - Where: `endingView()`.
   - What: the heading "Plan approved!" is followed by body text starting "Plan approved! ..."; "Not yet." is followed
     by "Not yet. The council asks...". After five stops of work the approved moment is one sentence and a picture; the
     "Not yet" ending names nothing the student could do (only the homework band lists pieces). Better: drop the
     repeated words, and let the council react in story terms (Lily's line about the bed, Mr. Hale's about planting
     day), and give "Not yet" the same named missing pieces the homework ending has.
   - Seen: `audit-r1/state-ending-1366x768.png`, `play/out/fail-ending-1366.png`.

6. **The trace card has no way to act on what it shows.** polish, general
   - Where: `trace()` dialog.
   - What: the read-only card says "Follow it to Stop 4" but offers only "Back to quest"; the student then has to find
     Rewind, open its menu, pick the stop and confirm. Better: a "Rewind to Stop N" button in the card (still with the
     Yes / No check), which turns the Trail back into the second run the spec plans for.
   - Seen: `play/out/trail-click-q1.png`.

7. **After saving a note the hint says "Tap a place in your pack" while the place buttons are right below the note.**
   polish, general
   - Where: `how()` stop 3, `gatherNext`; wide layouts show the `.visit-tab` row in the card.
   - What: the hint points the student to the side panel when the nearer control is the row of place buttons just
     under the note (the `needs` already targets `.visit-tab`). Better: "Tap the next place below." on wide layouts,
     keeping the pack wording where the tabs are hidden.
   - Seen: `audit-r1/state-saved-note-1366x768.png`.

8. **Marker covers the current stop's label in the short layouts.** nit, general
   - Where: stop strip at 680x425 and 1000x625 ("Orga ze", "Pres", "Ga er" under the backpack).
   - Seen: `audit-r1/state-organize-680x425.png`, `audit-r1/state-gather-680x425.png`, `play/out/trail-1000.png`.

9. **Pack list cuts "Your outline" at the panel bottom.** nit, general
   - Where: side panel at 1280x720 and 1366x768 from Stop 4 on; the last pack item is half hidden above Rewind.
   - Seen: `audit-r1/state-ending-1366x768.png`.

10. **Mr. Adeyemi's reply to B reads as "correct".** nit, general
    - "That's a question you can answer, and it's about our garden." is the only reply with no question back, so the
      cheap sweep (tap each card, listen) finds the answer at Stop 1. Spec says choosing shows no right or wrong; a
      reply that still nudges (for example "Good. What will you need to find out first?") keeps the pattern even.

No cultural, Native or hard-history content; nothing for a sensitivity review.

#### Counts
blocker 1, should fix 2, polish 4, nit 3.

#### Audit pilot
- Leads confirmed: Organize note text clipped (680, 800, 1000, 375); Trail back lines overlapping and hidden under
  cards; pack list cut short by its scroll panel at 1280x720 (also visible at 1366x768).
- Leads wrong or harmless: "welcome not heard" after a first tap on a question card is allowed (BASELINE rule 16); the
  premise is on the Stop 1 card and in the story text. The many trail-back "overlap" rows between `g` groups are the
  invisible 44 px hit paths overlapping each other, not visible clutter; only the visible-line cases above matter.
- Missed: the Trail back pointing to the wrong stop (needs a failing run, the audit states only cover the ideal
  run); the quote-everything cheap pass; the empty space above the clipped note text; the duplicated ending words;
  the marker covering stop labels. A failing-run state in `audit-states.json` would have caught finding 1.

<!-- end part -->

<!-- part: refine/teaching.md -->

### Teaching lens: research-quest (round 1)

Cold lens, 2026-11-06. Read spec.md, src.html, notes.md, tool.draft.json, audit-states.json and audit-r1/audit.md.
I drove the bundle in my own Chrome (port 9861). Council logic was checked by running `__tool.evaluate` on seeded runs.
Frames: `S:/CurioClass-codex-scratch/research-quest/teaching/frames/`, outputs `.../teaching/out-*.json`,
logic table `.../teaching/logic-out.json`.

Counts: blockers 2, should fix 4, polish 4, nit 2.

#### Blockers

1. **Trail back sends a skipped visit to Stop 4, not Stop 2** (src.html:677-678, `references`; traceEvidence 1039).
   Leave out the library, county office, nature center or notebook at Plan and its council question fails, but the
   Trail back line and card say "Stop 4" (Organize). The dialog title says "Trail back · Organize" and the text says
   "Your visits did not bring back this evidence", so the label and the reason disagree. The real shortcut was the
   Stop 2 plan. Trail back is the tool's one idea ("traces a line straight back to the choice"), so pointing at the
   wrong stop teaches the wrong lesson. It also fails Done when 2: changing one earlier choice (the visit plan) does
   not send the line to that stop. The same applies when every note goes in Not needed: question 4 points to Stop 3
   and says "Your visits did not bring back this evidence", but the cause is Organize (allnotneeded-trail).
   How seen: logic-out.json (q2_libraryNotVisited, q3_countyNotVisited, q5_natureNotVisited, q1_notebookNotVisited
   are all `X@4`); frames skiplib-trail.png, skiplib-trace-q2.png, allnotneeded-trail.png. Better: when the note's
   place was never visited, use Stop 2 and say "You did not plan a visit to the library". When the note is in Not
   needed, use Stop 4. Tag: general.

2. **A plan built on unattributed copied words gets "Plan approved!"** (src.html:674, question 4 checks one note only).
   Save the library note well with its source. Save the other three as "Copy it, no quote marks" with **Save note**
   (no source). The council approves with zero missing pieces and no aside. Trail back shows five green ticks,
   including "Where did that fact come from? You kept the source with this note." Three of four notes are someone
   else's exact words with no quote marks and no source, and the tool's only verdict praises it. That undoes
   AASL Engage VI.B.1 (the code this tool claims for quoting and paraphrasing) and the spec's own premise that
   "every shortcut you take comes back". How seen: logic-out.json `onlyLibrarySourced: approved`; frames
   onlylib-ending.png, onlylib-trail.png. Better (stays inside the story): any outlined note copied without quote
   marks, or saved with no source, brings back question 4's challenge for that note (the principal points at it),
   or adds an uncounted aside like the too-close one. This changes a council rule, so the integrator may route the
   exact rule to the spec's open questions. The flaw itself must be fixed before Cory. Tag: general.

#### Should fix

3. **Meaning-changed notes count as "Answer held"** (src.html:671-676, 697-699). If every note uses the
   changed-meaning version, questions 2, 3 and 5 are still answered with a tick. Lily asks "When should our flowers
   bloom?" and the answer on screen is "Monarchs only visit flowers in the spring. Our plan: Plant flowers that bloom
   in late summer and fall." That contradicts itself and still counts as held. Q2 is answered by "they can use other
   plants too". Q3 is answered by "Any milkweed from any store works, and a little pesticide is fine." The ending is
   "Approved, with homework" (one missing piece) while every note says the opposite of its source. How seen:
   logic-out.json `allChanged`; frames allchanged-q2.png, allchanged-q5.png, allchanged-ending.png,
   allchanged-trail.png. Better: a question whose answering note is a changed version is not answered, and its trail
   card says the note changed the source's meaning (Stop 3). Tag: general.

4. **"Those are the book's exact words... name the book" on notes that are not from the book** (src.html:694).
   Question 4 targets the first note under "What monarchs need", or else the first outlined note. When that note is
   the county page or the club notebook copied without quote marks, the principal still says "the book's exact
   words" and "name the book". In the county case the source line is shown right above it, so "name the book" is
   also wrong. How seen: out-county-copy-q4.json, out-notebook-copy-q4.json; frames county-copy-q4.png,
   notebook-copy-q4.png. Better: "Those are the exact words from [title]. Put them in quote marks." (Spec Content
   wording carries the same flaw: fix both.) Tag: general.

5. **AASL Collaborate is only represented, not taught** (spec Standards; notes.md "Standards in the activity").
   Every council answer is "filled in automatically from your pack". The student presses Next question and reads.
   They never choose, say or defend an answer, so "presenting findings to a group and answering its questions" is
   watched, not done. notes.md itself says Collaborate is "represented". Per BASELINE rule 2, either add a real step
   (for example, at each question the student taps the pack note or slide they would answer with, then the council
   reacts to that choice), or move the code to a tool that teaches it. Tag: general.

6. **"Save note with its source" is styled as the main button** (src.html:796, `btn('save-source',..., primary)`
   against a plain "Save note"). The spec says choices "never show right or wrong when made". The teal primary
   styling tells the student which save is right before the council does. How seen: audit-r1
   state-gather-1366x768.png. Better: give both save buttons the same style. Tag: general.

#### Polish

7. **Meaning-changed paraphrase is always the shortest** (spec Content, src.html:525-576). Lengths (good/close/
   changed): library 103/106/74, county 143/131/66, nature 120/123/42, notebook 73/69/40, video 78/56/44,
   seed 61/61/53. On a second run, or in a teacher-led class vote, "skip the short one" works without reading for
   meaning. The shuffled order does not hide this. Better: make the changed versions as long and as fluent as the
   others (for example, nature: "Grown monarchs feed on nectar from many flowers, mostly in spring before they head
   north."). Tag: general.

8. **The homework list reads badly when piece 1 is missing** (src.html:843-844). Output: "come back with a clear
   question and what our garden has now and when the flowers should bloom." Piece 1 already contains "and", so the
   list blurs. Frame two-missing-ending.png. Better: join with a semicolon or "; and", or reword piece 1 ("a clear
   question about our garden's needs"). Tag: general.

9. **Question 4 never says which fact it is asking about** (src.html:688-695). The speech card shows "Where did
   that fact come from?" and then a citation, but not the note it is about. The student can't connect the answer to
   a note without opening the pack. Better: show the note text above the source line (frame nbcopy-q4.png).
   Tag: general.

10. **Organize note cards clip the fact that decides the heading** (audit lead, confirmed on
    audit-r1/state-organize-800x500.png). At 680x425, 800x500, 1000x625 and 375 wide, the note text is cut to two
    lines ("It's the only plant they eat, so no...") and the source line is cut too. "× no source" is the
    information a student should notice here. Better: keep the source line whole and let the card grow, or open the
    full note on the first tap. Tag: general.

#### Nit

11. **The approved ending says "Plan approved!" twice**, once as the heading and again at the start of the line
    (audit-r1/state-ending-1366x768.png). Tag: general.
12. **Question 3 accepts the county note under any heading**, including "What our garden has now". It is harmless,
    but a teacher discussing "Did your outline make the note useful?" may notice. Tag: general.

#### Checked and fine

- **Done when 1:** the ideal run is approved with five ticks (logic-out `ideal`; audit state-ending and
  state-trail-back frames).
- **Done when 2:** each of questions 1 to 5 fails on its own when one choice changes (question A, notebook heading,
  library in Not needed, no milkweed step, no source, copy without quotes, no fall step). The stop is wrong when the
  changed choice is the visit plan (blocker 1).
- **Done when 3:** question 6 appears only with a changed note, question 7 only with the seed step, and the
  too-close aside only with a too-close note. With no notes in the outline, question 4 says "There's nothing in the
  outline to point to." (allnotneeded-q4).
- **Done when 4:** endings follow the count (0 approved; 1 or 2 homework, with pieces named; 5 not yet).
- **Done when 5:** Go is enabled only at exactly four places. On to Stop 4 is enabled only at four notes. A fourth
  plan step is disabled with a title. Tap-then-tap reaches the end (audit states organize to trail-back).
- **Done when 6:** the run survives a fresh tab (rewind-reload: stop 4 restored). Rewind to Plan keeps the question
  and places and clears notes and headings (rewind-check). Start over, No then Yes, clears both state and `rq-run`
  (restart-check).
- **Facts:** "caterpillars eat only milkweed", "adults feed on nectar of many flowers during breeding and
  migration" and "up to 3,000 miles" match the FWS monarch page (fetched 2026-11-06). That page's overview also
  says "more than 2,000 miles (3,000 km)", but the video passage uses the Behavior figure, so it is fine. Native
  common milkweed and butterfly weed, fall nectar and no pesticides match the Xerces and USDA lines in the spec.
  All story places and people are labeled fictional in notes.md.
- **Grade fit:** language is plain for 6-8. The notes' What it teaches, Key skills, Support at home and Talk about
  it are true of this tool, and the home ideas are doable tonight. No sensitive topic, so no rule 8 note is needed.
  No cultural, Native or hard-history content, so there is no sensitivity referral.
- **Codes taught by doing:** I.A.1 (Ask), I.B.2 and C3 D1.5 (Plan), D3.1 and W.6-8.7 (four sources into an
  outline). Engage VI.B.1 is practiced at Gather but undercut at judging (blocker 2). Collaborate is not taught
  (should fix 5).

#### Audit pilot

- **Leads confirmed:** the organize note-copy clipping at small sizes (polish 10, which also matters for teaching).
- **Leads wrong or not mine:** the many trail-back "overlap" and "hidden under path" rows come from the SVG route
  hit areas (44 px transparent strokes) overlapping cards and each other. On my 1366x768 frames the visible lines
  and cards read clearly, so I'm leaving those for Play and Craft. The "pack item cut by a scroll panel" row at
  1280x720 is not a teaching issue.
- **Missed (out of its reach):** wrong Trail back stop for skipped visits (blocker 1), approval of unsourced
  copies (blocker 2), changed-meaning answers held (should fix 3), the "book's exact words" mismatch (should fix 4),
  the styled-right save button (should fix 6) and the shortest-option tell (polish 7). None of these show in a
  layout or voice check.

<!-- end part -->

## Fix

<!-- part: polish.md -->

### Polish: research-quest (Codex fix, round 1)

The explicit Curiosity instruction takes precedence over Refine's older lesson classification and its keep-endings call. The tool is now an open research desk: Question, Sources, Notes, Outline and Evidence can be used in any order. No welcome screen, kit header, numbered ladder, score, level, quiz or finish screen remains. Evidence gaps are document readouts, not an approval grade. All evidence paths below are relative to `_scratch/research-quest/`.

#### Blocker

- **1 FIXED.** Routes use the actual cause: unsuitable question = Question; unvisited source = Sources; unsaved, uncredited, unquoted or changed note = Notes; excluded note, wrong heading, missing plan step or empty outline = Outline. Original skipped-library route was 4; now 2. Original empty-outline citation route was 3; now 4. `fix-before/skip-library.png`, `fix-after/skip-library.png`, `fix-before/all-not-needed.png`, `fix-after/all-not-needed.png`; `logic-verified.json` tests all four useful sources. Both failing runs are in `audit-states.json` as real-input states.
- **19 FIXED.** The citation check examines every outlined note, lists every issue and names its note and source. The named exploit now lists county, nature and notebook, routes to Notes and exposes the missing credits and quote marks. The original 32-case probe accepted 15 uncredited variants; the corrected 10,000-combination test has zero false citation passes and 28,020 assertions. `fix-before/unsourced-copies.png`, `fix-after/unsourced-copies.png`, `logic-before.json`, `logic-verified.json`. Approval itself is removed under Curiosity precedence.

#### Should fix

- **2 FIXED.** Both save controls use the same plain style. `save-style-before.json` and `save-style-after.json` record their computed backgrounds; `fix-before/save-style.png` and `fix-after/save-style.png` show the same 1366x768 state.
- **3 FIXED.** Pointer state clears on cancel, native drag start, drag end, blur and a new pointer down. Native drag start no longer silently selects a note. Cancel, native-start/cancel and blur probes followed by a heading click all leave heading 0 and selection null: `cancellation-final.json`, `last-proofs/final-cancellation.png`, against `stale-pointer-before.json` and `fix-before/stale-pointer.png`. Real keyboard placement moves the note to heading 2. The native drag fixture emitted no drop; native-drop success is not claimed.
- **4 FIXED.** Card text begins at the top and uses available space; source lines have reserved space. Selecting a note opens its full wording over the note tray, leaving headings available. Back to notes returns to the cards. Before frames: `fix-before/organize-680.png`, `organize-800.png`, `organize-1000.png`, `phone-before/phone-organize.png`. Final evidence: `fixture-recheck/organize-680x425.png` and `fixture-recheck/selected-note-680x425.png`, `selected-note-800x500.png`, `selected-note-1000x625.png`, `selected-note-375x812.png`, with matching JSON. At 680 the selected text measures 56/56 px client/scroll height and the full credit 32/32; every card credit is within its card. Text and credit client/scroll heights also match at 800, 1000 and 375. Main controls remain available; long unselected note bodies can scroll rather than losing words to a two-line clamp or hover-only title.
- **5 FIXED.** Copy explanations name the actual document and add the missing-credit instruction only when needed. The note's wording is shown before its credit. `fix-after/county-copy.png`, `fix-after/notebook-copy.png`, `county-copy-after.json`, `notebook-copy-after.json` at 1366x768; paired wording corrected in spec Content. These are original fictional document titles, not claims that a county page or notebook is a book.
- **20 FIXED.** An all-quote outline retains its evidence links and displays the uncounted aside, "Can you say that in your own words?" `fix-before/all-quote.png`, `fix-after/all-quote.png`, `all-quote-after.json`, `logic-verified.json`. There is no win or approval state.
- **21 FIXED.** Changed meanings cannot support questions 1, 2, 3 or 5. Each routes to Notes, including when a second organizational problem exists. Before: all four were supported. After: all four expose gaps. `fix-before/all-changed.png`, `fix-after/all-changed.png`, `logic-verified.json`; covered across all 10,000 note combinations.
- **22 FIXED BY REMOVAL.** The Not yet ending is removed with all ending bands. Each evidence gap instead names its missing material and its cause, available immediately rather than after a forced finish. `last-layout/evidence.png`; zero ending renderers in `contract-final.json`. No replacement finish was added.
- **23 FIXED.** AASL Collaborate is removed from the claimed standards in source metadata, spec and notes. `notes.md` explicitly records that automatic responses do not teach it and asks the integrator to give the code to a tool with real collaboration. No catalog outside the allowed folders was edited.

#### Polish accepted

- **6 FIXED BY REMOVAL.** No ending heading or paragraph remains to repeat. `last-layout/evidence.png`, `contract-final.json` (zero ending renderers). The live empty-outline detail also avoids repeating its status as a second answer card.
- **7 FIXED BY REMOVAL.** No homework list or joined ending sentence remains. Missing material is shown in separate evidence cards and note details; no ambiguous conjunction chain. `last-layout/evidence.png`.
- **8 FIXED.** All six changed variants are fluent and within 15% of the matching good variant: ratios 1.010, 0.930, 1.008, 0.945, 1.141, 1.082. Same strings in spec Content. `logic-verified.json`; original ratios in `logic-before.json`. The shortest-choice shortcut no longer identifies the changed version reliably.
- **9 FIXED.** Credit details show the actual note text before the source, including every problematic note. `fix-after/county-copy.png`, `fix-after/notebook-copy.png`, `fix-after/unsourced-copies.png` at 1366x768.
- **10 FIXED.** Visible routes have a paper halo and sit above the map cards; lower-row routes use the side margins to avoid upper-row text. Card buttons remain the main input route. Final 1366 and 375 evidence: `fixture-recheck/evidence-seven-1366x768.png` and `fixture-recheck/evidence-seven-375x812.png`, both inspected with all seven routes. The accepted transparent-hit-stroke geometry leads are not treated as painted overlap.
- **11 FIXED.** Every evidence detail offers Rewind to the named file through the existing Yes / No confirmation. The real-input sequence opened the skipped-library detail, chose Sources and chose No; work remained intact. `input-final/rewind.png`, `final-rewind.json`; direct inspection of `trace()` and `confirmReset()` confirms the shared path.
- **12 FIXED.** Wide saved-note hint: "Tap the next place below." Compact layouts name the visible Pack control. `extra-final/saved-hint.png`, `hint-final.json` at 1366x768. The final Pack button is on the power rail at every size, including `phone-final/phone-organize.png`.
- **13 FIXED.** Read is assembled from semantic working content, not chapter innerText. It includes note text and credits, choices and evidence, and skips seals, hidden/decorative copies, placement instructions and footer. It also works inside dialogs via their own Read button. `final-read.json`, `voice-walk-final.json`, `input-final/read.png`, `extra-final/initial-voice.png`. The final semantic filter also excludes dialog help and includes the dialog title; the live `read` field in `fixture-recheck/all-not-needed-680x425.json` confirms the title, question and single status without the footer.
- **14 FIXED BY REMOVAL.** Empty stop badges and the numbered stop strip are removed. The defensive `small:empty` rule also exists. `last-layout/default.png`; independent file tabs have no empty pills.
- **15 FIXED BY REMOVAL.** No marker overlaps a compact label because the sequential marker and stop strip are removed. `last-layout/organizer-680.png`, `organizer-800.png`, `organizer-1000.png` and `phone-final/phone-organize.png`.
- **16 FIXED.** SVG route groups have tabindex -1; their cards remain keyboard buttons. No duplicate tab route is added. Source `trailView()`; `input-final/keyboard.png` also verifies keyboard note placement.
- **17 FIXED.** The bundle header credits illustrations to Curio Class without the company name. All 13 prompt entries explicitly declare people false, including the three named entries. `contract-final.json`; no new painting or people image was made.
- **18 FIXED.** L.next and L.endingNext and all forced-route narration are removed from the spoken bank. `allLines()` and `voice/lines.json` both contain one quiet initial hint. `voice-walk-final.json`, `contract-final.json`.
- **24 FIXED.** B asks, "What would you need to find out about the garden first?" Same wording in spec and source; no automatic praise or correctness marker. The four options remain freely revisable. `reply-final/question-b-final.png` and `question-b-final.json` at 1366x768, after held clicks on Question and B.
- **25 FIXED.** Spec Art now matches the prompt records: eleven generated gpt-image paintings, two retained local FLUX paintings. All people flags are false, so no people contact sheet is required. No images were replaced or removed from the asset set.

#### Settled calls

The blocker severity, source-credit requirement, meaning checks, standards removal, and permission to quote with a source are applied. Source relevance still allows the county note under any useful outline heading. The pack is a scrollable collection. Transparent route hit geometry is not painted clutter. Existing art remains.

The old keep-ending-bands instruction and sequential seven-question presentation conflict with the explicit Curiosity request. Ending bands and the forced presentation were removed. The seven question texts remain available as evidence prompts, with the original conditional meaning-change and seed-ad prompts. No welcome, score, goal ladder or forced finish was introduced.

Unattended decisions: use an open desk with freely accessible files; retain the supplied six-document scope; keep browser narration; leave the catalog number unassigned because neither spec nor concept catalog assigns Research Quest a number. Do not fabricate a numbered plate or a new observational dataset.

#### Cheats tried

The old library-good / three-uncredited-copies pattern now lists all three citation failures. Single missing source, unquoted copy and combinations of those conditions were tested across all four notes in 10,000 combinations. Zero incorrect citation passes.

All changed notes, one changed note at a time, changed notes with organizational problems, skipped useful sources, all Not needed, wrong headings and missing plan steps route to their actual cause. All-source quotations stay valid and invite paraphrasing. Length-only selection is neutralized within 15%. No score, grade or finish can be earned by a tap pattern.

Three independent canceled-pointer patterns followed by a heading click do not move a note. Keyboard placement does. The native drag fixture reached dragstart/pointercancel/dragend without drop, so native drop remains unverified rather than reported as working.

#### Voice walk

Held clicks used a 0.12-second press and two-second spacing: choose quotation, save with source, open Outline, open Evidence, inspect the credit card, Read inside it. The optional initial hint became stale on the first action and was correctly dropped. One Read entry was logged at about 12 seconds. There is no automatic council or ending narration. A separate working-board Read entry includes full note wording and sources without repeated placement instructions. Browser narration is used; no recorded clips were generated or listened to audibly in this muted run. Bank equality: 1 = 1.

#### Engine changes wanted

None. All changes are tool-local. No shared kit, scripts or catalog file was changed.

#### The real material

Fetched/checked 2026-11-06. Raw verification downloads, rights notes and reproducible gathering script are in `data/source-manifest.json` and `gather_sources.py`. Every request had an 18-second timeout; gathering remained within 45 minutes. No observational dataset was sampled, and no outside passages or media were packed into the tool. All six original fictional documents are bundled in full.

| Material | Named source and rights | Independent check |
|---|---|---|
| Caterpillar milkweed dependency; adult nectar; eastern migration up to 3,000 miles | [U.S. Fish and Wildlife Service, Monarch](https://www.fws.gov/species/monarch-danaus-plexippus). Federal-authored facts public domain, 17 USC 105; [FWS rights notice](https://www.fws.gov/disclaimer) acknowledges third-party exceptions. No third-party media copied. | [NPS, Protecting Western Monarchs](https://www.nps.gov/articles/000/protecting-western-monarchs.htm), [NPS migration event](https://www.nps.gov/planyourvisit/event-details.htm?id=0AFA7A72-FFED-E75A-C80160AEB245F91C). |
| Native milkweed, fall nectar and pesticide avoidance | [Xerces, Monarch Butterfly Conservation](https://xerces.org/monarchs), fact checking only; no copyrighted text or images reused. Student text is original Curio Class writing, CC BY 4.0. | [NPS, Monarchs on the Move](https://www.nps.gov/articles/000/monarchs-in-cuyahoga-valley.htm), Protecting Western Monarchs. [NPS rights](https://www.nps.gov/aboutus/disclaimer.htm): federal-authored text generally public domain; outside images excluded. |
| Common milkweed and butterfly weed identities | [USDA PLANTS](https://plants.usda.gov/), federal plant facts public domain. Regional suitability belongs only to the fictional setting. | [University of Connecticut, Milkweed](https://homegarden.cahnr.uconn.edu/factsheets/milkweed/), reference only; copyright UConn, no text or media packed. |
| Six example documents, authors, notebook count of two, ad, dates, candidate notes and evidence rules | Original fictional Curio Class material, CC BY 4.0. Candidate versions can deliberately distort a source; they are not biological assertions endorsed by the instrument. | Verified against each original passage and exact evaluator tests. |
| Standards references | [AASL Framework](https://standards.aasl.org/framework/), copyright AASL. Codes and citation only; no framework text reproduced. Collaborate removed. | Claimed practice checked against the implemented note and evidence interactions. |
| Illustrations and code | Existing generated Curio Class illustrations; two retained FLUX.1-schnell paintings, model Apache 2.0. Original content CC BY 4.0; code MIT. | Existing provenance retained in art/prompts.json; all 13 people flags false. |

#### Curiosity short test and lesson creep

These are agent judgments from the solo research and counterfactual comparison paths, not claims from a human user study. The revised desk supports open comparison and revision with no terminal state. A kid may be drawn to the painted sources and evidence routes; unassigned replay appeal is not established. Adult replay and a month of depth remain limited by the six-document corpus. The real working material is the document wording, citations and their links, with real biological facts inside explicitly fictional documents. This is a bounded document instrument, not a general research or gardening system. No claim that it reaches Beat Lab's or Elements Inspector's depth is made.

The four questions, explicitly:

- Would a kid open it unassigned? The painted sources and changing routes offer a low floor; sustained unassigned return is not established.
- Would an adult play for fun? Brief source/note comparison is interesting, but replay is limited by the fixed corpus.
- Is the real thing the interface? Yes for document wording, citations and links; biological facts are real, while the example documents are explicitly fictional.
- Does it work without a score or finish? Yes. Files and evidence stay open to revision without an approval band or terminal state.

All four model frames were opened and inspected in `model-frames/`. Compare `last-layout/default.png` and `model-frames/beat-lab.png`: the desk uses its own material and permanent working controls, but has substantially less depth. No model file was modified.

Lesson-creep scan: no header or ending renderer, and no score/level/goal/quiz/finish flow. `complete` occurs only in the source's biological phrase "life cycle"; `score` appears only in the Manual's honesty statement that there is none. Legacy unused ending CSS is inert, not a reachable screen. Internal result booleans describe evidence support and never accumulate into a grade.

#### Audit

The single full audit completed in **1115.9 seconds (18.6 minutes)**, below its 40-minute limit. `fix-audit/audit.md`, `fix-audit-result.json` and all 81 frames were inspected (also collected in `fix-audit-contacts/`). The audit found 233 mechanical leads, not 233 confirmed instrument defects. Every lead has an individual disposition in `audit-dispositions.json`:

- 18 hidden legacy-hint checks: accepted under Curiosity precedence. The old lesson panel is hidden; working controls, Read and Manual carry the instrument.
- 28 state-step, focus and keep-region checks from invalid compact fixtures: corrected. Hidden visit tabs were replaced by the visible Pack path. Later rows in the working scroll collection are reached with Tab and Enter, not a click below its scroll edge. Fixtures begin with the visible confirmed reset. Twelve scoped real-input cases then passed with zero console errors, including all four saved notes, four selected-note sizes, all Not needed, skipped library and seven routes at 1366 and 375. See `fixture-recheck/summary.json` and all twelve corresponding frames.
- 95 SVG/nested-label geometry checks: accepted after inspecting the actual frames. Transparent 44 px hit strokes and group bounding boxes are not painted rectangles; side-routed, haloed visible strokes do not disappear under cards.
- 81 modal occlusion checks: accepted. The active native dialog intentionally covers inactive map/rail content and has its own Read and return controls.
- 11 lesson-welcome checks: accepted under Curiosity precedence and BASELINE 16. The initial cue can be skipped or cut by an action; no lesson welcome is required.

The audit's 20 initial controls reported no errors or lost focus, including Enter twice after each click. Five-repeat checks were clean. The rapid-tap cue cut is included among the 11 voice leads. Resize checks reported no exceptions or stuck disabled controls; Motion off had no endless animations. Invalid compact fixture paths were not claimed as complete state coverage before the scoped recheck.

Inspection of the held-click table found one additional moment mismatch: the optional cue could speak after opening Manual or Pack. A tool-local validity guard now drops it while a dialog is open. `fixture-recheck/manual-first-1366x768.json` and `pack-first-1366x768.json` log a stale drop and no spoken cue. This was the only application change after the full audit; no second full audit was run.

Final bundle: **1,573,716 bytes**, one offline file, zero unresolved art tokens, zero remote resource attributes or fetch functions, no kit stylesheet, header element or ending renderer. Runtime reopening also recorded zero network resources. `contract-final.json` and `final-validation.json` preserve the checks and hashes. All assigned Chrome ports and host 8725 were closed; no host.html was left in the tool folder.

#### Left open

The supplied spec/catalog does not assign a Curiosity plate number to Research Quest, so plate is null and no number was invented. The six-document corpus has limited adult replay and month-long depth; the report does not certify the full Curiosity short-test bar. No new dataset or topic was invented to hide that limit.

Native HTML drop remains unverified: the driver fixture emitted native dragstart/pointercancel/dragend without a drop. The silent-move fault is closed across three cancellation patterns, and the keyboard placement path passes. Browser narration remains the fallback; no recorded voice take was generated or audibly reviewed in this muted run.

The complete audit precedes the single dialog-hint guard and the corrected fixture descriptions. Those changes received scoped rechecks rather than a second full audit, as required by the one-audit rule.

No commits. Writes were restricted to tools/research-quest and _scratch/research-quest. refine.md and refine/ were not edited. The resumed session's failed concurrent browser attempts and earlier intermediate clipping frames are preserved; they are not presented as final passing evidence.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Research Quest build handoff

#### Structure

src.html starts from the kit starter. CSS lays out the illustrated parchment map, chapter card and research pack at actual viewport size. The JavaScript contains exact story data, voice lines, serializable run state, a pure council evaluator, chapter renderers and delegated input handlers. Artwork is referenced through one art table and art tokens. Curio.voice owns the narration queue; the tool owns the hint immediately on each state change.

#### Tricky parts

- Council questions use the spec's exact presence, heading, source and plan-step tests. Question 4 selects the first note in visit order under What monarchs need, then the first outlined note elsewhere. Question 6 checks only outlined notes. Not needed never counts as outline evidence.
- A correct source quotation is allowed. Copying without quote marks fails question 4, including when it has a source.
- Rewind retains the reopened stop's choices and clears later choices. Revisiting Gather offers Redo note. No network calls or personal data.
- Choice order for paraphrases is shuffled once per run and persisted. The words, not answer labels, appear on screen.
- The chapter dominates the map; a short landscape view uses a dot strip and pack chip. Phones use a full-width card.
- Trail back buttons correspond to code-drawn paths and open read-only choice cards. Question 1 returns to Ask if the question is unsuitable, or Organize if the garden heading is the missing condition.

#### Open questions and build decisions

The spec contains no explicit open-question section. Its leaning toward one continuous quest, no score, delayed story consequences and the five-stop map was followed. No topics or game modes were added. Three existing paintings were retained, nine missing paintings generated, and the blooming garden repainted to show recognizable milkweed. The source request for local FLUX was superseded by the owner's explicit image-tool instruction and CODEX-BUILD.md.

The source's migration distance is reproduced as a fictional video statement and qualified by the supplied good paraphrase. The planted garden is the story payoff, not a new planting simulator. Extra instructional how lines name enabled controls. Metadata credits both retained art and new art.

Compact organizer cards use deliberate excerpts with the full words in their title, the research pack, and Read. Short council layouts show slide headings; the full outline remains in the pack. At 760 wide the pack collapses below the stage; on phones the hint and pack stay in a fixed bottom bar, with Rewind and Start over available inside the pack. Trail lines recalculate their endpoints after layout and resize rather than relying on illustration coordinates.

The opening uses two large painted panels on laptops: the empty bed and the library desk. At the tightest landscape preview the brief is carried by the picture caption, question cards and reply so the next button stays clear. Phones retain the garden panel and the small desk beside the brief. Only the opening was re-shot at every required size after this art adjustment.

#### Verification artifacts

Scratch: S:/CurioClass-codex/_scratch/research-quest. numbers.py and numbers.json contain the independent 200,000-run model and contrast checks. model-checks.json checks the shipped evaluator. student-run.json records a complete held-click run and narration. keyboard.json records a complete keyboard-only run. check_reload.py verifies reload, clear and zero external requests. Frame folders preserve initial size coverage and targeted fixes. The audit folder contains the final mechanical audit. No temporary scripts or screenshots are kept in the tool folder.

#### Engine changes wanted

None in the kit. A possible audit-helper improvement, left outside this tool's write scope: in scripts/audit_tool.py, PAGE_JS, distinguish a path-only SVG group's accessible name from painted text, and use painted-path hit geometry instead of its rectangular group bounds for overlap leads. Preserve the HTML button and label checks. The Trail back's visible curves intersect by design; the wide, transparent hit paths are not rectangles drawn over labels.

#### Audit dispositions

The one complete audit finished in about 27 minutes with 113 leads. Seven leads represented three concrete layout defects: two Ask overlaps at 680, the same shrinking pack question row in three 1280 states, and two undersized Yes targets. All were fixed and re-shot at the affected sizes. The full audit was not repeated.

The other 106 leads are explained in codex-report.md: four intentional note excerpts, one empty sixth-cell sample in the mobile plan-step grid reserved for Done, 97 SVG-path or nested-label geometry reports, and four expected welcome skips when the first question tap speaks its own reply. The full audit's repeated taps, focus and resize checks were clean. The final welcome guard for open dialogs and the four painted visit badges were verified separately. The pack list can scroll as a collection; the count chip opens the whole pack, and Gather also has four visit buttons on wide screens.

#### Next work

The separate cold review is documented in codex-review.md. Narration recordings were intentionally not created. No commits or additional polish round.

#### Cold review changes, 2026-10-31

The cold review used ports 9960/9961 and host 8765. Its evidence is under _scratch/research-quest/review-*. The council evaluator and all specified outcomes remain intact. Organize now prioritizes the selected-note instruction over Done, with state-specific queued-line validity. Nested pack cards preserve the original focus anchor. Read uses rendered text boundaries so adjacent headings and answer letters are not joined into words.

Trail back keeps its map and every route. Focusing or hovering a question isolates that route and its stop; wide cards and read-only cards show the actual evidence choice. Compact cards keep the short question labels. traceEvidence supplies these descriptions, and highlightTrace controls only presentation.

The inherited caterpillar was replaced using the built-in image generation tool, then processed with art.py --rekey. The prompt is in art/prompts.json and the raw painting in art/raw/rq-caterpillar.png. Two local FLUX paintings remain. See codex-review.md for the final audit disposition and any limitations.

The review audit completed in 1,797 seconds with 124 leads. Its frames exposed a compact ending image extending under the footer status and populated organizer grids growing into the plan-step label; explicit shrinking grid rows now keep both within their reserved space. Compact heading source names have titled ellipses. The audit also caught focus falling to the page during a nested-card transition; openDialog now focuses the first live control after replacing content. All three endings and three/four-note organizer headings were rechecked at 680, 800 and 1000 widths; nested-card focus and Enter-to-return passed all eight standard sizes. No full audit rerun.


#### Curiosity fix, 2026-11-06 (supersedes historical descriptions above)

The explicit user instruction overrides Refine's lesson classification and its keep-endings call.
The current file is an open desk, with five independent file tabs, its own power rail, maker plate and lower-left Manual.
There is no header from the kit, numbered route, welcome, score, quiz, approval band or finish screen.
The evaluator returns evidence results only. It checks every outlined citation and rejects changed meanings as support.
Evidence causes determine the route. Selected cards expose full wording; cancelled native drags cannot carry stale pointer state.
Voice speaks one quiet hint and otherwise only Read. voice/lines.json matches allLines().
The supplied spec has no Curiosity number and CURIOSITIES.md has no Research Quest entry. plate is null, visibly unnumbered.
The underlying material remains six fictional source documents with verified biological facts. This authenticity ceiling is explicit.
AASL Collaborate was removed; catalog reassignment belongs to the integrator, outside this write scope.
No kit change, paid generation, installation, registration, upload, git operation or external message was performed.

#### Engine changes wanted (current fix)

None. Historical audit-helper suggestions above are informational only.


#### Fix verification closeout

The single full audit completed in 1115.9 seconds (18.6 minutes), with 81 inspected frames and 233 mechanical leads.
Dispositions are in _scratch/research-quest/audit-dispositions.json. They comprise 18 legacy hidden-hint checks,
28 invalid fixture actions/focus/keep checks, 95 SVG or nested-label geometry checks, 81 expected modal occlusions,
and 11 lesson-welcome checks overridden by the Curiosity brief. No exceptions or stuck controls were found in the resize checks.

The compact fixtures originally used hidden visit tabs. A first correction still tried to click a Pack row below its scroll edge.
The final audit-states.json uses visible Pack input, Tab and Enter to bring each source into view, with a confirmed reset for isolation.
Twelve scoped real-input cases then passed, including all four saved notes, selected full notes at 680/800/1000/375,
all Not needed, a skipped useful source, seven evidence routes at 1366/375 and first-tap Manual/Pack.
Every scoped case had zero console errors. Source lines fit the note cards. The selected county note at 680 had
text client/scroll heights 56/56 and source heights 32/32. Other selected-note sizes also had equal client/scroll heights.

One small voice correction followed the full audit: an initial cue is stale while a dialog is open. First-tap Manual and Pack
were rechecked: neither spoke that cue. No second full audit was run. Native HTML drag in the test fixture emitted no drop;
native drop is therefore unverified. Three canceled-drag patterns cannot move or silently select a note, and keyboard placement works.

Current evidence: fixture-recheck/, last-proofs/, input-final/, last-layout/, fix-before/, fix-after/, fix-audit/,
logic-verified.json (10000 combinations, 28020 assertions), contract-final.json and the data/source-manifest.json licence record.
The report does not claim the six-document corpus has the depth of Beat Lab or Elements Inspector. The catalog number remains unassigned.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-04)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-04)
- 2026-11-25: refine.md folded in (last changed 2026-11-08)
- 2026-11-25: refine/craft.md folded in (last changed 2026-11-08)
- 2026-11-25: refine/play.md folded in (last changed 2026-11-08)
- 2026-11-25: refine/teaching.md folded in (last changed 2026-11-08)
- 2026-11-25: polish.md folded in (last changed 2026-11-08)
- 2026-11-25: handoff.md folded in (last changed 2026-11-08)
