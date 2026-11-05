# Codex report: code-kitchen

## Built

Build only, 2026-11-02. No commits, branch operations or polish round.
Created the offline Tickets and Open kitchen tool from the kit starter frame.
Twelve levels cover typed values, variables, procedures, local parameters, nesting and menu-change edit counts.
Includes the safe expression parser, live Cook/Step/Stop, forty-step Undo, line editing, Pantry, saved kitchen,
progress dots and par rings, teacher notes, voice manifest, audit states, vector preview and illustrated station.
All intentional writes stayed in tools/code-kitchen/ and _scratch/code-kitchen/.

## Numbers check

PASS. _scratch/code-kitchen/numbers.json records the independent Python computation.
"3" + "2" = "32"; 3 + 2 = 5; mixed number/text addition raises TypeError.
str(5) + " pancakes" has 10 characters; "Classic, thanks!" has 16, below the 24-character limit.
D10 has 15 starter lines. C8's largest changed stack is 5, within 1 to 8.
B4 edit comparisons are 1 versus 2; D10's second change is 1 versus 5; D12's egg change is 1 versus 3.
Runtime and real-input checks agreed with these counts. A line is configured before insertion, so D12's banana line costs one edit.
Computed contrast ratios match the spec: 6.25, 5.66, 14.78, 6.33, 16.02, 8.49, 7.28, 8.30, 6.36 and 6.08 to 1.
Corrected primary/header hover colors after visual review. Type is carried by shape and quotes as well as color.

## Feel check

Played all twelve level paths through real held mouse input and typing, using the visible line drawer and controls.
Evidence: all-ui-1-6.json, all-ui-7-12.json and all-ui-frames/ in Scratch. All final menus matched.
Best moment: one changed topping slot dispatches five changed D10 orders and earns the one-edit result.
Flat moment 1: adding a customized call first took two edits. The drawer now configures the entire line before insertion.
Flat moment 2: food stayed in its cooking position when served. The pass now transfers the painted food and box/plate,
and prints the actual label, while the running card line and local jars make the program's effect visible.
Also kept Cook and the hint visible while the compact toolbox scrolls, and restored jar readouts on phones.
Bundled and opened both bar tools in Scratch. Compared the final tool beside Beat Lab in bar-comparison.png.
The painted copper equipment, shaped value chips, textured paper and live food have the intended finished working-place feel.

## Done when

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

## Wave lessons

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

## Audit leads

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

## Frames looked at

All frames in first-frames/, test-frames/, extra-frames/, size-frames/, final-frames/, phone-frames/,
repair-frames/, repair-phone-frames/, all-ui-frames/, followup-frames/ and last-frames/ were viewed directly or in contact sheets.
Also viewed student-b4.png, keyboard-complete.png, bar-comparison.png, all 51 audit frames, the art contact sheet,
and full-size griddle, takeout box and existing backdrop. Scratch holds all frames and Chrome profiles.
Coverage includes every level, both modes, type failures, nesting, parameters, eight pancakes, forty lines,
twenty nested recursive calls, eight fully loaded tickets, a ninth-ticket rejection, and a 24-character label.
Motion off, grayscale, phone hosting, keyboard-only A1 completion, Enter/Pantry, Ctrl+Z and Alt+Down were checked.

## Art made

Thirteen new cutouts made with the built-in image tool, one call per asset. No people and no redraws.
Preserved the existing diner-pass backdrop. Fourteen finished WebP files total 157,024 bytes, about 153 KiB.
Final bundle is 323,098 bytes (315.5 KiB), recorded by preflight.json and far below 2 MiB.
Each full generation prompt and provenance is in art/prompts.json. Raw originals are in art/raw/.
Only art.py --rekey processed the generated assets. preview.svg is drawn in code, as specified.
The open art question was resolved in favor of all thirteen painted pieces; handoff.md records that decision.

## Art still to paint

None. All thirteen requested new assets are made and used, with the existing background.

## Engine changes wanted

None. The kit and shared scripts were not edited.

## Left open

- No recorded narration was made, as required for this build. Installed browser voices determine offline voice availability and timbre.
- A forty-line source card can execute more than forty lines through reused procedure calls. Such a run can exceed fourteen seconds.
  Kept 350 ms per executed line and live interruption controls; handoff.md explains the timing conflict with the source-card budget.
- Compact layouts use the Levels chooser in place of an always-visible twelve-dot panel strip; all levels and progress remain accessible.
- The full audit was not repeated after the targeted build repairs. A cold review remains the next separate task.
- Some cutouts have very thin key-edge pixels at native resolution; display-size art was inspected in the finished scene.

All Chrome and server processes started for this build are closed. tools/code-kitchen/host.html was removed.
