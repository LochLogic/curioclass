# Codex review: reserve-designer

## Played

Grade 9 solo: empty map, connected lean reserve by held clicks, futures, weak links, farm/crossing menus and Groups at 1/10/20 elk.
Played before builder notes or source. Compact projection and all three modes checked at every standard size and hosted 375 wide.
The painted valley and live species feedback are strong; the single-loss test earns its payoff.

## Findings fixed

- Should fix, general, Plan/Stress: stale stress totals survived a revision. Untested plans now reset their summary and Weakest cells pressed state.
- Should fix, general, Plan menus: clicking unbuyable land left another purchase menu open. Dismiss it first.
- Should fix, general, Show needs: potential elk corridors were dimmed until purchased. Highlight all potential route types and restate seasonal requirements.
- Should fix, general, Stress: empty Weakest cells and zero-new-loss narration implied cracks that did not exist. Give accurate empty guidance and a separate result line.
- Should fix, general, artwork: ovenbird eye mask was biologically misleading. Redrew it with Cornell's plain olive face, complete eye ring and crown stripe.
- Should fix, general, map art: road read as a narrow track. Redrew highway, bridge and wildlife crossing as a coherent, legible barrier and passage.
- Should fix, general, Craft: loss words overprinted crack symbols; slider focus crossed the label. Cleared those conflicts.
- Polish, general, flattest moment: selecting a future left generic directions. Its live hint now names the lost place, broken needs and Back to plan, with immediate sound.
- Should fix, general, 680x425 Stress: the new untested summary cut the hint off. Shortened it and the Run instruction; entry and revision now fit.
- Polish, general, Groups: the first prompt now asks for a 1-versus-20 comparison using displayed evidence.

Independent Python and browser checks match the three supplied plans: costs, six-species results, 0/14, 0/12 and 14/19 futures and the five exact weak cells.
Farm cap, overspending, bank/bridge gates, reload, live interruption controls, keyboard buying and all 96 arrow-key cells passed.
Notes retain the required opening sections; HS-LS2-7, HS-LS4-6 and HS-LS2-8 have corresponding student actions.

## Findings left

- Nit, general: small secondary bibliography, survey eyebrow and future-map captions remain. Primary instructions and controls stay readable.
- No blocker or should-fix left. The known spec conflict and browser narration limitation remain below.

## Flattest moment left

Groups remains a short supporting comparison after the richer reserve-design investigation. No extra feature or topic was added.

## Graphics

All 21 images checked in the contact sheet and their actual scene placements; no people or missing art tokens.
Four redraws made with built-in imagegen, then art.py --rekey: rd-ovenbird and the highway/bridge/crossing tiles.
Full prompts: art/prompts.json. Selected raw PNGs and finished WebPs are in art/raw and art.
Biological reference: [Cornell Ovenbird identification](https://www.allaboutbirds.org/guide/Ovenbird/id).
Art 568.9 KiB; bundle 850.4 KiB. The paintings and detailed survey scene were retained.

## Audit

Single final audit completed in about 32 minutes: 67 frames, 69 leads, no runtime errors; Chrome 9951, host 8755.
Dispositions: 2 clipping leads fixed; 25 secondary-text nits kept; 2 icon diagnostics, 37 welcome diagnostics, 2 menu-resize diagnostics and 1 Clear interruption accepted.
Every repeated-click row passed. Post-audit checks fixed clipping and the stale pressed state; menus reopened with no disabled actions.
Only affected frames were re-shot. The full audit was not rerun after those scoped repairs. One-cell results now say 1 future.
Evidence: [raw audit](../../_scratch/reserve-designer/review-audit/audit.md), [lead dispositions](../../_scratch/reserve-designer/review/audit-dispositions.md), and review Scratch frames/JSON.
Voice counts, held clicks (starts):

| Line | Kind | Expected | Spoken |
|---|---|---:|---:|
| farmChoice | how | 1/5 | 1/5 |
| crossing | how | 1/5 | 1/5 |
| allSix | event | 5/5 | 5/5 |
| alarm | event | 5/5 | 5/5 |
| stressDone | event | 5/5 | 5/5 |
| stressNoWeak | event | 5/5 | 5/5 |

Read with Sound off, immediate welcome after Read-to-mode change, and rapid stale-line cancellation passed.
Motion off: 2 of 10 watchers, zero running animations, instant stress result, dog shelter retains three seconds.
Grayscale protection remains clear through double outlines, flags, patterns and state words. Phone cells measured 28.4 px.

## Left open

- Spec conflict retained: the fixed budget can buy 21 cells; 200 ms each takes 4.2 seconds, above its stated four-second maximum.
- Supplied search counts and lower-budget bests lack seeds/witness plans. No optimality claim or solution is exposed to students.
- Narration uses the browser fallback; recordings were prohibited. Some short-lived lines are intentionally stopped when their state ends.
- The supplied NPS prairie-dog and OpenStax URLs did not load in the web reader; those source routes remain unverified.
- The temporary drive host's favicon 404 belonged to the wrapper, not the standalone tool. The tool itself embeds its favicon.
- Map-first taps skip the Plan welcome under the spec's stale-on-cell-click rule; the current instructions remain available through Read.
- No commits, shared-kit changes or writes to other tool folders. Owned Chrome/host processes closed; ports 9950, 9951 and 8755 checked free; host.html absent.
