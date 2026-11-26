# Code Kitchen: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: code-kitchen

#### Built

Build only, 2026-11-02. No commits, branch operations or polish round.
Created the offline Tickets and Open kitchen tool from the kit starter frame.
Twelve levels cover typed values, variables, procedures, local parameters, nesting and menu-change edit counts.
Includes the safe expression parser, live Cook/Step/Stop, forty-step Undo, line editing, Pantry, saved kitchen,
progress dots and par rings, teacher notes, voice manifest, audit states, vector preview and illustrated station.
All intentional writes stayed in tools/code-kitchen/ and _scratch/code-kitchen/.

#### Numbers check

PASS. _scratch/code-kitchen/numbers.json records the independent Python computation.
"3" + "2" = "32"; 3 + 2 = 5; mixed number/text addition raises TypeError.
str(5) + " pancakes" has 10 characters; "Classic, thanks!" has 16, below the 24-character limit.
D10 has 15 starter lines. C8's largest changed stack is 5, within 1 to 8.
B4 edit comparisons are 1 versus 2; D10's second change is 1 versus 5; D12's egg change is 1 versus 3.
Runtime and real-input checks agreed with these counts. A line is configured before insertion, so D12's banana line costs one edit.
Computed contrast ratios match the spec: 6.25, 5.66, 14.78, 6.33, 16.02, 8.49, 7.28, 8.30, 6.36 and 6.08 to 1.
Corrected primary/header hover colors after visual review. Type is carried by shape and quotes as well as color.

#### Feel check

Played all twelve level paths through real held mouse input and typing, using the visible line drawer and controls.
Evidence: all-ui-1-6.json, all-ui-7-12.json and all-ui-frames/ in Scratch. All final menus matched.
Best moment: one changed topping slot dispatches five changed D10 orders and earns the one-edit result.
Flat moment 1: adding a customized call first took two edits. The drawer now configures the entire line before insertion.
Flat moment 2: food stayed in its cooking position when served. The pass now transfers the painted food and box/plate,
and prints the actual label, while the running card line and local jars make the program's effect visible.
Also kept Cook and the hint visible while the compact toolbox scrolls, and restored jar readouts on phones.
Bundled and opened both bar tools in Scratch. Compared the final tool beside Beat Lab in bar-comparison.png.
The painted copper equipment, shaped value chips, textured paper and live food have the intended finished working-place feel.

#### Done when

1. PASS: A1 stops at line 2 with the text/number error; changing stack to 4 serves T3. Runtime and real-input evidence.
2. PASS: A2 shows stack "32", then the mixed-addition label error, then serves with str(stack). Actual printed label is "5 pancakes".
3. PASS: A3 rejects text for to_go and serves both orders with False and True.
4. PASS: B4 reuse takes one edit; copied plates take two. Real editor run earned the ring; comparison runtime recorded two edits.
5. PASS: C8 size + 1 passes in one edit. Local size/topping jars appear during the call and locals are null after return.
6. PASS: D10 topping change takes one edit with a shared procedure and five with copied lines.
7. PASS: bluberries, stak, pour_pancakes(9) and a recursive recipe stop with their respective messages.
8. PASS: Open kitchen card and ticket survived a new-page reload; Clear saved plus Yes removed both and the storage entry.
9. PASS: all STANDARDS sizes checked, including 375x812 through port 8785. Cook, rail and active/selected card line stay in view.
   The full audit's default size checks were clean at 44 px. Targeted compact and phone repairs were then inspected.
10. PASS for behavior: welcome/how deduplication, Read, five fresh stopped events, mode scope and clean console checks.
    The final five-click test spoke all five errors. Narration uses browser fallback, with the prescribed voice prepared in lines.json.
    The bundled file has no external resource references or network code. Product branding uses Curio Class.
11. PASS: the recipe card is the largest stage region at 1366x768 and 1000x625. Running-line highlighting accompanies painted output.
12. PASS: real held slot clicks paused a running D10 immediately; later plate state stayed unchanged. Stop cleared every count.

#### Wave lessons

- Hint and voice: PASS. Immediate action hints, kit queue, once-only how lines and fresh event keys. Final pace and Read logs inspected.
- Focus and layout: PASS. In-place slot updates and selection classes preserve focus; hint space is reserved; no focus on load.
- Sizes: PASS. All eight prescribed sizes reviewed. Compact Pantry, new ticket and line composer now fit their choices.
- No giveaways: PASS. Students write executable recipes; no solution/refactor button or length score is supplied.
- Honest numbers: PASS. Counter records slot/line edits and Undo restores it. Kitchen argument ranges are enforced per call.
- Standards: PASS. Students create typed variables, parameterized recipes and nested/decomposed recipes in the actual editor.
- Motion off: PASS. No infinite animation remained in the audit; 350 ms execution timing is retained.
- Short choices stay visible: PASS. Twelve levels fit the chooser; compact Pantry exposes all value tiles and Use value together.
- Resize mid-action: PASS. The audit reported no exceptions or controls left disabled.
- First-action welcome: PASS. Cook/Step/blank teaching can suppress the welcome as the standing rule requires; no late welcome is added.
- Unknown stays unknown: PASS, not a hidden-diagnosis activity. Unset jars are absent; tickets start unserved.
- One look, one meaning: PASS. Number/text/Boolean chips use separate shapes; error marks include words.
- Badge truth: PASS. Check marks require an exact plate match; par rings follow measured edits. Editing clears current done status.
- Hints change back: PASS. Mode, reset, error and editing transitions update the hint directly; Read uses that current hint.
- No word-copy answer: PASS. Correctness comes from execution, matching orders and adapting a program.

#### Audit leads

One full audit completed on ports 9981/8785, with 34 leads. Default sizes, calm mode and resize stress were clean.
Report: _scratch/code-kitchen/audit/audit.md. Every one of its 51 frames was reviewed in nine contact sheets.
The audit predates the final repairs below. Only targeted rechecks followed; no second full audit was run.

- Open kitchen/New ticket hidden by the compact panel: fixed by moving New ticket beside the primary actions.
- Hint/Cook lost after panel scrolling, including parameter run: fixed with sticky primary regions and measured hint height.
- Pantry tile/Use value overlap at 680: fixed by a two-column compact Pantry; all tiles and the action are visible together.
- Ticket label/Hang ticket overlap at 680: fixed by the four-column short-landscape form.
- Empty label input reported unnamed: added an explicit To-go label accessible name, in addition to its wrapping label.
- Four line-number focus-loss leads: fixed with class updates instead of rebuilding the card. Focused line remains the active element.
- Covered Cook/rail/card keeps in Pantry, ticket and level dialogs: expected native-modal coverage. Audit states now keep the foreground dialog.
- Dialog-background hint/choice leads: background controls are intentionally inert while a dialog is open. Sticky controls restore the working view.
- Missing welcome after first Cook/Step/C7-C9: expected suppression by the first action or blank how-to, as STANDARDS requires.
- Three lost stopped events at a two-second pace: fixed by retaining fresh event entries across unchanged retries.
  fresh-events.json records five spoken events of five, with no dropped entries.
- Welcome cut by quick Restart: fixed by preserving a relevant welcome already playing. restart-welcome.json has one uncut spoken welcome.
- The mode-switch movement count is expected re-layout. Remaining walk/keyboard, repeat and quick-tap rows were clean.

#### Frames looked at

All frames in first-frames/, test-frames/, extra-frames/, size-frames/, final-frames/, phone-frames/,
repair-frames/, repair-phone-frames/, all-ui-frames/, followup-frames/ and last-frames/ were viewed directly or in contact sheets.
Also viewed student-b4.png, keyboard-complete.png, bar-comparison.png, all 51 audit frames, the art contact sheet,
and full-size griddle, takeout box and existing backdrop. Scratch holds all frames and Chrome profiles.
Coverage includes every level, both modes, type failures, nesting, parameters, eight pancakes, forty lines,
twenty nested recursive calls, eight fully loaded tickets, a ninth-ticket rejection, and a 24-character label.
Motion off, grayscale, phone hosting, keyboard-only A1 completion, Enter/Pantry, Ctrl+Z and Alt+Down were checked.

#### Art made

Thirteen new cutouts made with the built-in image tool, one call per asset. No people and no redraws.
Preserved the existing diner-pass backdrop. Fourteen finished WebP files total 157,024 bytes, about 153 KiB.
Final bundle is 323,098 bytes (315.5 KiB), recorded by preflight.json and far below 2 MiB.
Each full generation prompt and provenance is in art/prompts.json. Raw originals are in art/raw/.
Only art.py --rekey processed the generated assets. preview.svg is drawn in code, as specified.
The open art question was resolved in favor of all thirteen painted pieces; handoff.md records that decision.

#### Art still to paint

None. All thirteen requested new assets are made and used, with the existing background.

#### Engine changes wanted

None. The kit and shared scripts were not edited.

#### Left open

- No recorded narration was made, as required for this build. Installed browser voices determine offline voice availability and timbre.
- A forty-line source card can execute more than forty lines through reused procedure calls. Such a run can exceed fourteen seconds.
  Kept 350 ms per executed line and live interruption controls; handoff.md explains the timing conflict with the source-card budget.
- Compact layouts use the Levels chooser in place of an always-visible twelve-dot panel strip; all levels and progress remain accessible.
- The full audit was not repeated after the targeted build repairs. A cold review remains the next separate task.
- Some cutouts have very thin key-edge pixels at native resolution; display-size art was inspected in the finished scene.

All Chrome and server processes started for this build are closed. tools/code-kitchen/host.html was removed.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: code-kitchen

#### Played

- Cold grade 7 route before reading the builder: A1 Pantry fix, type failure, B4/B6, C8, D10 change, Open kitchen.
- Then checked every base menu and change in all 12 levels through the runtime and editor. Rich setting; satisfying one-edit payoff.
- Also projected at 1366x768 and compared with existing Beat Lab and Snowy Mail Route bundles. No other tool was written.

#### Findings fixed

- Blocker, general, src.html: Undo crossed a menu boundary and restored a prepared answer for zero edits and a par ring. Each change now starts fresh history.
- Blocker, general, src.html: D12 awarded a ring for either phase. It now requires every rated phase, with per-phase counts and versioned saved rings.
- Should fix, general: Pantry offered other recipes' private names. It now offers globals and this recipe's local names/parameters.
- Should fix, general: redundant Indent/Outdent clicks cost edits. No-op operations now leave history and the counter alone.
- Should fix, general: incomplete runs and parameter levels could leave a listener without a named next control. Added contextual fixed voice lines.
- Should fix, general: new-ticket/composer dialogs retained hidden-control hints after closing. They restore context and drop stale dialog speech.
- Should fix, general: special valid names such as __proto__ were not safe dictionary keys. Runtime dictionaries now have no prototype.
- Should fix, general: the 1280x720 dot list clipped its last choices. Short landscape uses the complete Levels chooser.
- Should fix, general: six eggs extended onto the griddle controls. Both rows now fit its cooking surface.
- Should fix, general: compact parameter runs scrolled tools beneath sticky Cook controls. Run/level transitions now restore the panel top.
- Should fix, general: compact success pointed to hidden Levels; Open kitchen hid Add a line. Primary controls now expose the next action at 680 and 800.
- Should fix, general: a changed rail retained the previous menu's plate and success message. Both now clear when the new menu arrives.
- Should fix, general: Step, Levels and Clear saved could be silent or narrate hidden controls. Added contextual lines, named dialogs and stale-error hush.
- Polish: the pass names the actual plated food and reports the student's served orders and measured changes.
- Polish: redrew the syrup mound as a thin amber glaze; kept the copper kitchen, cutout food, ruled card and shaped chips.
- Polish: added jar-name ellipses/full titles, a takeout-box alt label, accurate Boolean-addition errors and singular wording.

#### Findings left

- No known unresolved blocker or should-fix after scoped rechecks.
- Polish: building the first large multi-procedure card remains the slowest stretch. Keeping the specified editor and content.

#### Break it

- Every served dot: blank cards, repeated Step, rapid Cook/Stop, missing orders and extra serve calls do not complete a level.
- Types: quoted number, joined "32", mixed label addition, text yes/no, unknown name, misspelled topping and range 9 all stop on the relevant line.
- A2 succeeds after numeric inputs and str(stack); A3 needs actual False/True. No answer cards, slider sweep or reflection gate exists.
- Boundary Undo: before, earned par with zero edits. After, both changed-menu plates remain wrong; a real one-edit correction succeeds.
- Copied B4: two edits, no new ring. Shared recipe: one edit, ring. Existing legitimately earned rings remain best achievements.
- D10 copied: five edits for each change, no ring; reused: one for the rated second change, ring.
- D12 copied eggs then shared topping: counts 3 and 1, no ring. Reuse for both changes: 1 and 1, ring.
- All B4-C9 and D11 rated changes pass in one edit with their reused solution. No score uses card length.
- No-op indentation stays at zero, a real indentation costs one, and Undo restores zero. Recursive calls stop at depth 20.
- Stop clears food/results; a held slot click stops Cook immediately and its plate stays unchanged afterward.
- Forty lines remain editable at 680x425. Eight full tickets are accepted; a ninth is refused. Saved card/tickets reload, then clear after Yes.
- Evidence: review-all-twelve.json, undo-blocked.json, copied-counters.json, copied-b4-clean.json, types-and-errors.json, no-op-edits.json in Scratch.

#### Voice walk

- Sound on, default state, held 120 ms presses and two-second gaps: rail welcome, slot, Pantry, 4, Use value, Cook, Read, Open kitchen, New ticket, Close, Tickets, C7, Cook.
- Final route heard in order: w-tickets, slot, served, Read current result, w-open, ticket, levels, blank plus Press Cook, incomplete plus Edit/Cook.
- Side path: B4 Cook, manager change, edit shared count, Cook; change then par events heard. Rapid mode/Read/Sound transitions dropped stale lines.
- Counts below are per named fresh-page route. Read and navigation intentionally interrupt speech whose state has ended.

| Line | Kind | Expected | Spoken |
|---|---|---|---|
| slot | how | 1 | 1, then silent |
| stopped | event | 5 | 5 |
| w-tickets / w-open | welcome | 1 each | 1 each |
| Step / Levels / confirmation | how | 1 each | 1 each |

- Keyboard-only A1 serves with visible focus on Cook. Voice manifest and allLines contain the same 17 lines. Browser fallback; no audio recorded.
- Final logs: voice-main-final.json, step-first.json, levels-first.json, confirm-context.json, stop-hush.json; repeat/side logs retained too.

#### Facts checked

- Numbers versus quoted text; "3" + "2" = "32", 3 + 2 = 5: Python Software Foundation, [Tutorial section 3](https://docs.python.org/3/tutorial/introduction.html).
- str(5) + " pancakes" = "5 pancakes": Python Software Foundation, [str](https://docs.python.org/3/library/functions.html#func-str).
- Mixed number/text addition raises TypeError: Python Software Foundation, [TypeError](https://docs.python.org/3/library/exceptions.html#TypeError).
- True and False are Boolean values: Python Software Foundation, [Boolean type](https://docs.python.org/3/library/stdtypes.html#boolean-type-bool). The stricter kitchen action type rules are original to this tool.
- def, argument binding, call-local names and nesting: Python Software Foundation, [Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions).
- Reuse centralizes changes: Abelson/Sussman, [SICP 1.1.8](https://mitp-content-server.mit.edu/books/content/sectbyfn/books_pres_0/6515/sicp.zip/full-text/book/book-Z-H-10.html); actual edit comparisons independently executed above.
- Standards: [CSTA](https://csteachers.org/k12standards/) and data/standards/csta-2026-ids.txt. Typed variables, parameterized calls and nested decomposition are student actions.
- Original Curio Class rules: kitchen ranges, exact ticket matching, labels, pars, 40 lines, 8 tickets and 20-call guard checked against spec and runtime.
- Independent recomputation: 24-character limit contains the 10-character pancake label and 16-character Classic label; D10 is 15 starter lines; C8 peaks at 5 pancakes.
- Palette contrast recomputed: white/brand 6.25, brand/paper 5.66, ink/paper 14.78, muted/paper 6.33, number 8.49, text 7.28, Boolean 8.30 to one.

#### Sensitivity

- None requiring a cultural lens: a fictional first-person cooking workstation, no people images, bodies, health advice, named cultures or historical claims.
- The student is the cook. Adding a decorative person is not needed to explain this station; all 14 assets correctly say people:false.

#### Flattest moment left

- Entering the first large card still involves many small editor actions. The sharp result is seeing that work pay off at the next menu change.

#### Graphics

- Checked all 14 assets in a contact sheet and at use size across the required sizes, maximum food, grayscale and Motion off.
- Replaced syrup only, via built-in imagegen and art.py --rekey. Final asset: art/syrup.webp; prompt/provenance: art/prompts.json; old art preserved in Scratch.
- No placeholders or missing painted assets. No restyling or stripped graphics. Final bundle 326,644 bytes (319.0 KiB); 14 images total 155,534 bytes.
- Evidence includes review-sizes/, review-audit-fixes/, review-voice-final/, review-art-contact.png and review-bar-comparison.png.

#### Audit

- Completed once, exit 0, within 40 minutes. Port 9941, host 8745, chrome-prof-review. Assessed all 89 leads and viewed all 75 frames.
- All eight default sizes, Motion off, control/Enter walks, repeated/quick taps and resize stress were clean apart from the listed state leads.
- Fixed compact parameter-run overlap, hidden success Levels and related Open kitchen control access; same-size rechecks pass at 680 and 800.
- Manager overlaps are the specified note over the rail/card; now a named nonmodal dialog. Old-menu plate/status cleared and re-shot at all eight sizes.
- Native Levels-dialog background occlusion is intentional: its foreground has all twelve 44-pixel choices visible. Inspected every size.
- Six missing-welcome leads are expected first-action suppression under BASELINE rule 16; Step now has its own explicit instruction too.
- Post-audit targeted batches: 12 state/size shots and 8 voice/control shots, zero console errors. No second full audit or review round.
- Report: _scratch/code-kitchen/review-audit/audit.md. Final guards and source/bundle hashes: review-verification.json in Scratch.

#### Left open

- As in the spec/build handoff: 40 source lines can expand into more than 40 executed lines through procedure calls, exceeding 14 seconds at 350 ms per line.
- Kept the stated execution pacing and live interruption; capping valid expanded programs would change the language/spec.
- No recorded narration: the brief forbids recording in this workflow. Intended easy-coach timbre depends on later voice production.
- An earlier temporary iframe host requested a missing favicon. Its Scratch helper now supplies a data icon; both final batches are console-clean.
- Process note: two quick setup checks lacked explicit watchdogs; all bundle, drive and audit runs were bounded.
- All project edits stayed in the two allowed folders. No commits, branch operations or kit changes. All owned Chrome/server ports are closed; host.html removed.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Code Kitchen handoff

Built by an earlier agent; cold review completed 2026-11-08, without commits. See codex-review.md for current findings.
For another cold review, follow CODEX-REVIEW.md's play-before-maker-reports order.

#### Structure

src.html starts from the kit starter. CSS uses real viewport layout, an editable lined card and a painted station.
The panel precedes the card in DOM order for keyboard use. On phones the station folds into a shallow strip.
The line model is {kind, name, args, depth}: assign, def or call. __tool.line exposes constructors for tests.
The safe expression parser accepts whole numbers, quoted text, True/False, names, str() and +. It never evaluates JavaScript.
The runtime uses explicit call frames and local dictionaries, stopping at 20 nested calls. Each kitchen action waits 350 ms.
Menu mutations update tickets and start a fresh edit counter. Undo restores card and counter together.
Open kitchen and level progress use separate localStorage keys with try/catch.

The Add a line drawer first chooses a kind, then configures the whole line before insertion. This makes an inserted
add_topping("banana") one edit for D12. Indent is inherited from the selected line; use Outdent for a call after a body.
The editor preserves the actual input node when a slot changes, and line/level selection updates classes in place.
The rail is horizontally scrollable on phones, and the latest jars stay visible in the station strip.
Compact screens use the Levels dialog instead of showing the entire twelve-dot strip in the panel.

Kitchen argument ranges apply to each call. Two valid pour_pancakes(8) calls produce sixteen pancakes and a wrong plate,
not a false type or range error. Stacks beyond eight compress their spacing so all cutouts still fit.

#### Timing edge case

Forty straight executed lines take about fourteen seconds at 350 ms each. A forty-line source card that reuses procedures
can execute many more than forty lines. Such a run can exceed fourteen seconds. Kept the specified per-line timing;
Cook, Step, Stop, editing, level selection and mode selection remain live. No false infinite-recursion error is used
to cap an otherwise finite program. A genuinely recursive chain still stops at twenty nested calls.

#### Open question decision

Accepted the spec's leaning: made all thirteen additional painted kitchen cutouts, with no people,
and preserved the existing diner-pass painting. Full prompts and provenance are in art/prompts.json.
Built-in imagegen generated each asset separately. Originals are copied to art/raw and only art.py --rekey processed them.

#### Engine changes wanted

None. No kit, script, documentation or other tool source was changed.

#### Follow-up

Read codex-review.md for the cold review's measured checks and remaining limitations. No narration was recorded.
The browser's installed voice is used, so the intended Umbriel timbre cannot be guaranteed by lines.json alone.

The one full mechanical audit finished with 34 leads. Default sizes, calm mode and resize stress were clean.
Build repairs addressed compact forms, sticky primary controls, in-place line focus, five fresh error events,
and a welcome interrupted by Restart. Focused follow-up checks passed; the full audit was not repeated.
Native dialogs intentionally cover the background card and rail. audit-states.json now keeps their foreground
dialog instead of requiring the covered background to remain unobscured.
The audit's missing-welcome flags for first Cook, Step and C7-C9 are expected first-action suppression.

#### Cold review changes

Menu transitions clear Undo history. Keeping old snapshots allowed a pre-written changed-menu answer to be restored
with zero counted edits. changeEdits records each phase; D12's ring requires both rated changes to meet par.
Saved par flags need parVersion 2. Older served dots remain, while older rings are re-earned under verified rules.
Pantry excludes assignments local to other recipes. New fixed voice lines cover incomplete runs, saved kitchen,
ticket forms and line composition. Dialog close restores its prior hint and drops instructions for hidden controls.
The pass now names the actual served food and summarizes the student's orders and measured changes.
The syrup was redrawn with built-in imagegen as a thin amber glaze; original art is preserved in Scratch.
Compact Cook starts and level selection restore the panel to its top, so the sticky controls cannot cover the edit counter.
Completed short-landscape runs expose Levels beside the primary controls. Open kitchen shares Cook's row with New ticket
at those sizes, keeping Add a line and Pantry visible. The Manager's note is a named nonmodal dialog; closing it returns
focus to Cook without scrolling. A changed menu clears the old plate and its success message.
Step, Ticket sets and Clear saved have their own once-only instructions. Stop and an actual error edit hush stale error speech.
The single cold-review audit completed within its 40-minute limit, with 89 leads assessed and 75 frames inspected.
Compact layout, current-menu feedback and contextual voice fixes received scoped rechecks in Scratch's review-audit-fixes/
and review-voice-final/. The final verification manifest is _scratch/code-kitchen/review-verification.json.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-08)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-08)
- 2026-11-25: handoff.md folded in (last changed 2026-11-08)
