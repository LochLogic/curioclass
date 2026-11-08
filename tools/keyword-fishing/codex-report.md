# Codex report: keyword-fishing

## Built

Offline Grades 3-5 lake puzzle with the exact 30 fictional pages, six levels, Free fishing, eight line slots, every supplied swap, typed words, live matching, clickable fish tags, pail reel-in and saved level stickers. Seven generated paintings. Kit frame, voice, Motion, Sound and Read. Build only; no commits or polish round.

## Numbers check

PASS: prepare.py independently reproduced all 25 stated catches, all 22 little words and 30 pages before building. core-results-fixed.json compares exact IDs against the bundled __tool.catch API. The browser also checks five plural pairs and every listed swap.
Source-note discrepancy: later exhaustive enumeration found 31 one-to-three-word Level 1 solutions with the listed swaps, versus its stated four. Four is the original-tiles-only count. Level 4 has the stated 11 with swaps; the other levels have 82, 59, 51 and 38, all above the stated 27 minimum. solution-counts.json records both counts. No spec or content was changed. This broader enumeration happened during verification, not before the first build.
Contrast checks: white/brand 4.99, brand/paper 4.54, ink/paper 13.57, muted/white 6.76, focus/white 5.18, ink/fish-tag 13.86, Cast text/gold 7.37. Header focus is white.

## Feel check

Best moment: Level 4's zero catch opens back up when big is swapped for size, then a successful cast gives the answer page a gold fin and a saved fish sticker.
Flat moment 1: the first cast only lifted fish inside the lake. Changed it to send painted fish across the scene into the pail, with a small pail landing response. Word controls stay live throughout.
Flat moment 2: broad schools made compact title tags pile up. Changed narrow crowded schools and away fish to reveal tags on focus/hover; tapped cards retain the full title, site and snippet. The empty lake now leaves the bobber and count clear.
Played all six levels through held clicks, then Free fishing, unknown words and keyboard use. Compared feel-comparison.png with Snowy Mail Route and inspected Beat Lab. The painted lake, fish, glints and reel-in meet the visual bar. Depth comes from six distinct search problems; Free fishing remains a small fixed pond.

## Done when

1. PASS: all 25 supplied catches and exact IDs match __tool.catch; each tested cast bucket matches its snapshot. numbers.json and core-results-fixed.json.
2. PASS: count and CSS targets update synchronously; 550 ms transitions re-aim from current positions. Calm snaps immediately. storage-resize-results.json includes before/after positions.
3. PASS: six real held-click solutions earned all six stickers. Earned numbers survived reload; No retained them and Yes cleared them. student-run.json and storage-resize-results.json.
4. PASS: all little words together catch 30; every little word preserves the two-fish sea/eat catch; adding one shows Same fish. core-results-fixed.json.
5. PASS: Level 3 starts with eight words and zero fish. lay selection enables removal and swap. Every listed replacement was exercised; words without swaps disable Swap. core-results-fixed.json.
6. PASS: typed moonstone remains on the line, empties the lake and shows the required message. Typed volcanoes catches four. unknown.json and core-results-fixed.json.
7. FAIL strictly for unobstructed pointer coverage: all 30 card contents were checked, and real Enter on T1 opens its card. Tags are at least 12 px. Crowded fish and banked nonmatches overlap, so some pointer hit areas are covered in tight views. All remain keyboard buttons. Narrow/away tags reveal on focus/hover beyond the spec's 680-only exception.
8. PASS: lake occupies 60 percent of the main width at 1280, 1366 and 1920; bobber center is 50/50. Size JSONs and inspected frames.
9. PASS: adding a word 80 ms into a cast immediately cancels it, changes the catch and prevents stale completion. Real drags on/off work. core-results-fixed.json, cancelled-cast-label.json, drag-on.json and drag-off.json.
10. PASS for primary controls: one full size sweep covered every specified size in both modes, including the real 375x812 iframe. Targeted checks cover the compact full line, Free fishing, swaps, wrong small catch and phone unknown-word state. Questions, line, tiles and Cast remain visible without page scrolling. final-summary.json and phone state JSONs.
11. PASS for targeted queue checks: voice-final-two-second.json shows one how line, two solved-event starts and Read priority with held taps at 2 s. Sound-off checks use no heard lines. All 19 runtime lines match lines.json. Final prompts ask for selection before naming enabled Remove/Swap controls, following STANDARDS over literal spec wording. No browser console errors in drive batches; no external requests or exceptions in storage/resize checks. The full audit did not complete.

## Wave lessons

- Hint and voice: PASS, hint updates synchronously; V.heard chooses how lines; result speech takes priority over an unfinished how line; Read retains priority. Literal spec feedback that named disabled controls was replaced by selection-first prompts, with enabled-control instructions after selection. Solved feedback names the next level control.
- Focus and layout: PASS in keyboard solve, swapping and removal; restored focus uses preventScroll. Selection does not rebuild a word under the pointer. Hint has reserved minimum height. Swap choices moved onto the lake to leave the hint uncovered.
- Sizes: FAIL strictly for exposed fish hit areas in crowded scenes; PASS for primary 44 px controls, reserved hints and every required viewport. Final targeted measurements have no small targets or hidden primary controls. Long drawer lists scroll independently; compact buckets collapse to counts.
- No giveaways: PASS within this live-preview design. Answer fins and stickers appear only after a cast. A small wrong catch still fails the question. Fish titles/snippets are intentionally inspectable in the spec.
- Honest numbers: PASS, on-screen fish are explicitly 30 made-up pages; notes explain every-word matching, the plural approximation and the fictional three-fish goal.
- Standards: PASS within the spec's given-question scope. Students select searchable words and identify possible pages. Notes distinguish this from full source reading/evaluation. No family engine is named.
- Motion off: PASS, zero infinite animations; instant re-aiming and immediate cast result. All generated art is present.
- Short choice sets: PASS for level numbers, level tiles and swap words; drawer word lists contain the complete vocabulary and intentionally scroll. All five drawer tabs stay visible.
- Resize mid-animation: PASS, a cast completed after flipping to 760x900; no exceptions or stuck casting flag.
- Delayed welcome: PASS in held-tap logs; first tile's own how line supersedes the now-stale welcome. Mode welcomes use Curio.voice, not welcomeAfter.
- Unknown as unknown: PASS, unknown typed words say no fish know them and stay tied on with a zero catch.
- One look, one meaning: PASS, four painted topic kinds retain their identity; dim edge fish are nonmatches, gold fins explicitly say Answers it.
- Badge truth: PASS, Nibble count is the live exact catch; bucket is the last completed cast. Cancelled casts no longer leave Reeling in.
- Reversible hint: PASS, modes, drawers, line edits, swaps, casts and clearing set the current next-action hint immediately.
- No answer by copying words: PASS with the intended keyword lesson. Tiles are deliberately taken from the given question; dead words, alternate words and wrong small catches prevent blindly copying the whole question from solving it.

## Audit leads

Audit not finished. It was run once on port 9991, host 8795, and stopped at its 40-minute limit. It saved 58 frames but no audit.md, so there is no completed lead list or certification of its full walk/repeat/resize checks. The process tree was stopped and both ports closed.
Confirmed during frame inspection and targeted PAGE_JS checks: short targets fixed; selected compact word/caption overlap fixed; popup fitting fixed; fixed popup moved out of its scroll-panel ancestor; inactive-control prompts fixed; mid-cast Motion off removes moving copies. Final five measured states have no non-fish UI leads in final-summary.json.
Remaining fish/fish overlaps and covered banked fish are real clustering, not silently dismissed as clean geometry. The popup intentionally covers background fish. Those items remain for cold review; strict all-fish pointer coverage is marked FAIL above. The full audit was not repeated.

## Frames looked at

58 build/reference PNGs: bar-frames 2, early-frames 4, functional-frames 7, late-frames 8, size-frames 19, targeted-frames 7, post-frames 7 and final-frames 4. Also art-contact.png and feel-comparison.png. All 58 audit PNGs were inspected through audit-contact-008 through audit-contact-058, eight sheets. Older frames preserve repaired defects; final-frames and the targeted JSONs show the final repairs.

## Art made

Seven new gpt-image paintings: misty lake/dock, orange fish, violet fish, coral fish, blue fish, red/white bobber and tin pail. Each was processed only with art.py --rekey and inspected in contact view and in play. No redraw was needed. Art 232.3 KB; final bundle 398,648 bytes (389.3 KB). Code preview.svg was also made and inspected.

## Art still to paint

None. No people. Recorded narration was explicitly outside this build.

## Engine changes wanted

None required.

## Left open

The full mechanical audit timed out and produced no audit.md. Dense fish/bank overlap leaves some pointer targets covered; keyboard access remains. Fish gather at fixed target positions with gentle swim loops rather than continuous orbital paths. Narrow crowded and away fish expose title tags on focus/hover; full cards remain available. Browser speech is used, not recorded Achird clips. Compact bucket contents are hidden beyond their count as specified. The general equal-time motion guideline conflicts with the spec's explicit instant calm cast; the latter was followed for this brief preview action. No live classroom or listening review.
The report was kept in Scratch until all checks completed because the user required stopping immediately when the report is written. The two reference tools were bundled only in Scratch copies, honoring the write boundary.
The index is the supplied Words column, not displayed snippets. B1's snippet contains find while its index does not, so find correctly catches zero under the spec. Teacher notes explicitly identify this model limitation. Snippet and index data were retained.

Cleanup: owned Chrome/server processes closed; 9990, 9991 and 8795 checked closed. host.html removed. No commits, branch changes, shared-source edits or polish round.
