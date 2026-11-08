# Codex review: code-kitchen

## Played

- Cold grade 7 route before reading the builder: A1 Pantry fix, type failure, B4/B6, C8, D10 change, Open kitchen.
- Then checked every base menu and change in all 12 levels through the runtime and editor. Rich setting; satisfying one-edit payoff.
- Also projected at 1366x768 and compared with existing Beat Lab and Snowy Mail Route bundles. No other tool was written.

## Findings fixed

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

## Findings left

- No known unresolved blocker or should-fix after scoped rechecks.
- Polish: building the first large multi-procedure card remains the slowest stretch. Keeping the specified editor and content.

## Break it

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

## Voice walk

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

## Facts checked

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

## Sensitivity

- None requiring a cultural lens: a fictional first-person cooking workstation, no people images, bodies, health advice, named cultures or historical claims.
- The student is the cook. Adding a decorative person is not needed to explain this station; all 14 assets correctly say people:false.

## Flattest moment left

- Entering the first large card still involves many small editor actions. The sharp result is seeing that work pay off at the next menu change.

## Graphics

- Checked all 14 assets in a contact sheet and at use size across the required sizes, maximum food, grayscale and Motion off.
- Replaced syrup only, via built-in imagegen and art.py --rekey. Final asset: art/syrup.webp; prompt/provenance: art/prompts.json; old art preserved in Scratch.
- No placeholders or missing painted assets. No restyling or stripped graphics. Final bundle 326,644 bytes (319.0 KiB); 14 images total 155,534 bytes.
- Evidence includes review-sizes/, review-audit-fixes/, review-voice-final/, review-art-contact.png and review-bar-comparison.png.

## Audit

- Completed once, exit 0, within 40 minutes. Port 9941, host 8745, chrome-prof-review. Assessed all 89 leads and viewed all 75 frames.
- All eight default sizes, Motion off, control/Enter walks, repeated/quick taps and resize stress were clean apart from the listed state leads.
- Fixed compact parameter-run overlap, hidden success Levels and related Open kitchen control access; same-size rechecks pass at 680 and 800.
- Manager overlaps are the specified note over the rail/card; now a named nonmodal dialog. Old-menu plate/status cleared and re-shot at all eight sizes.
- Native Levels-dialog background occlusion is intentional: its foreground has all twelve 44-pixel choices visible. Inspected every size.
- Six missing-welcome leads are expected first-action suppression under BASELINE rule 16; Step now has its own explicit instruction too.
- Post-audit targeted batches: 12 state/size shots and 8 voice/control shots, zero console errors. No second full audit or review round.
- Report: _scratch/code-kitchen/review-audit/audit.md. Final guards and source/bundle hashes: review-verification.json in Scratch.

## Left open

- As in the spec/build handoff: 40 source lines can expand into more than 40 executed lines through procedure calls, exceeding 14 seconds at 350 ms per line.
- Kept the stated execution pacing and live interruption; capping valid expanded programs would change the language/spec.
- No recorded narration: the brief forbids recording in this workflow. Intended easy-coach timbre depends on later voice production.
- An earlier temporary iframe host requested a missing favicon. Its Scratch helper now supplies a data icon; both final batches are console-clean.
- Process note: two quick setup checks lacked explicit watchdogs; all bundle, drive and audit runs were bounded.
- All project edits stayed in the two allowed folders. No commits, branch operations or kit changes. All owned Chrome/server ports are closed; host.html removed.
