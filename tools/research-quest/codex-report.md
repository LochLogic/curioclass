# Codex report: research-quest

## Built

Built the five-stop research story, all six sources, five note methods, source retention, outline, plan choices, council rules, three endings and interactive Trail back. The research pack, confirmed Rewind and Start over, local save, keyboard alternative, Motion, Sound and Read work.

Required files are in tools/research-quest/. tool.draft.json has stage built. The offline bundle is 1,514,451 bytes, about 1479 KB, below 2 MB. No commits, branch changes, submissions or polish round.

## Numbers check

Independent model: S:/CurioClass-codex/_scratch/research-quest/numbers.py and numbers.json. Seed 20261031, 200,000 random runs: 197,141 not yet, 2,858 homework, 1 approved. These are random choices, not estimates of student success. The ideal and source-credited quotation runs answer five questions. All three endings occur, questions range from five to seven, and at most seven are unanswered.

The shipped evaluator separately passed the ideal run, five isolated core failures, quotation, unmarked copying, changed meaning, seed mix, unused changed/close notes, empty outline, and two/three missing-answer boundaries. Evidence: model-checks.json. Supplied biological numbers and fictional dates were preserved.

All supplied contrast ratios reproduce: white/brand 5.47, brand/paper 4.85, brand/panel 5.26, ink/paper 13.61, muted/paper 5.68, muted/panel 6.16, focus/panel 7.58, focus/paper 6.99, white/brass 5.05, green/panel 4.82, red/panel 6.22.

## Feel check

Played the complete quest through real held clicks at a two-second pace, then a complete run using only Tab, Shift+Tab and Enter. Both reached approval and Trail back. The keyboard run used credited quotations; the first used good paraphrases.

Best moment: the council places a meaning-changing note beside the original passage, and the resulting line takes you back to that exact note. The supported plan also earns the painted change from bare soil to milkweed and asters. Different choices change the optional questions and named homework.

Flattest moment 1: gathering risked feeling like a form. Painted source scenes, clipped paper, immediate saved-note wording/source and a paper response give each decision a visible result.

Flattest moment 2: early Trail back arcs did not land on their own cards. Endpoints now come from rendered card and stop positions and update on resize. Compact labels leave room for curves. The library desk was enlarged into a second opening panel on laptops so its painting can be enjoyed.

Compared snowy-mail-route and beat-lab at 1366x768. The finished council has a layered painted room, active brass nameplate and central paper answer, matching the bar in finish while keeping its parchment world.
![Research Quest beside Beat Lab](S:/CurioClass-codex/_scratch/research-quest/feel-comparison.jpg)

## Done when

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

## Wave lessons

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

## Audit leads

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

## Frames looked at

All manual PNGs were inspected through contact sheets and full-size checks of defects/key scenes. All 73 audit PNGs were reviewed in per-state sheets, with critical mobile/Gather/organizer scenes opened full size.

Scratch: S:/CurioClass-codex/_scratch/research-quest/. Frame folders: small-frames, compact-fix, functional-frames, size-frames, fixed-frames, final-fixed-frames, phone-fixed, phone-last, interaction-frames, ending-frames, edge-fixed-frames, source-extreme-frames, audit, audit-fix-frames and ask-art-frames. Bar frames: snowy-mail-route and beat-lab.

Final opening checked at 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900 and hosted 375x812. Also inspected: grayscale, Motion off, complete keyboard run, drag, all sources/endings, meaning comparison, rewind and dialogs.

## Art made

13 finished images: 954,126 bytes, about 932 KB. Ten made with the built-in image tool during this build: marker, library desk, six place scenes, council room and replacement blooming garden. Three retained paintings: map, empty bed and caterpillar.

Blooming garden redrawn once because the inherited picture lacked recognizable milkweed. The replacement shows broad milkweed leaves, pink clusters, purple asters and a monarch. No people, faces or body parts generated.

Assets: S:/CurioClass-codex/research-quest/tools/research-quest/art/. Prompt catalog: art/prompts.json. Originals: art/raw/. Finished files processed only with art.py --rekey. Credits identify OpenAI gpt-image and the three local FLUX paintings. preview.svg is code drawn.

## Art still to paint

None. No deferred people assets or labeled placeholders.

## Engine changes wanted

None in the kit. handoff.md records a possible audit-helper improvement: scripts/audit_tool.py, PAGE_JS should distinguish accessible names on path-only SVG groups from painted text and test path geometry rather than rectangular group bounds. No shared engine or script was edited.

## Left open

Narration recordings were intentionally not created. Browser speech supplies behavior until the separate recording pipeline uses the supplied 31 lines and Algieba configuration.

The 20-30 minute classroom duration is the spec's intended pace, not a measured classroom study. Compact organizer excerpts and council slide headings are deliberate; complete wording remains in the pack and Read.

host.html removed. Every Chrome and host started here is closed; no listener remains on 9980, 9981, 9982 or 8785. Final git status contains changes only in tools/research-quest/. Build only, ready for the separate cold review.

