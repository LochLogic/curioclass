# Codex report: thesis-workshop

## Built

One offline literary writing room with Build, Prove and Draft, complete Saki and Frost texts, passage lights, four meter readouts, five saved theses per text, evidence explanations, contradiction response, editable paragraph, local Copy and confirmed clear.

All authored files are in `tools/thesis-workshop/`; scripts, source snapshots, profiles, logs and frames are in `_scratch/thesis-workshop/`. No commits or polish round. Working commands use deadline wrappers; two initial read-only probes completed before the wrapper was installed. The direct user stop rule takes precedence over creating this report early.

## Numbers check

`make_data.py` independently mapped the source ranges and recalculated every topic/move pair. All spec counts agree. `numbers.json` preserves all 30 Saki pairs and 24 Frost pairs.

- Saki topics: V 12, W 7, F 10, A 7. Moves: P 4, I 12, H 8, S 6, E 2.
- Vera + Story: W6, W7, W8, W10, W11, W22; Workable; N1 fits all six.
- Window + Planted: W7, W19; Thin. Window + Ending: zero; Nothing lit yet.
- Framton + Irony: eight; N2 fits five. Any + Any: 23; Too broad.
- Saki pair distribution: 14 Workable, 4 Thin, 8 Too narrow, 4 Too broad, as stated.
- Frost topics: R 12, C 10, T 5. Moves: Q 6, G 4, F 5, S 2, D 1.
- Roads + Equal: R6, R7, R9-R12; N1 fits six; N3 fits zero with four crossed lines. Any + Any: 20.

Browser checks passed 1,105 assertions with zero failures, including every chip pair with all four concrete meanings. `final-functional.json` is the result. Quote typography is normalized and the full text's words are checked in order against the downloaded originals.

## Facts checked

- Complete story, characters, quoted words and passage openings: [Project Gutenberg #269](https://www.gutenberg.org/ebooks/269), plain-text source snapshot `pg269.txt`.
- Saki is H. H. Munro: [Project Gutenberg author record](https://www.gutenberg.org/ebooks/author/152), which names Hector Hugh Munro as his alias.
- Beasts and Super-Beasts, John Lane, 1914: #269 credits its transcription from that edition.
- Complete poem, twenty lines, order and double hyphen in line 18: [Project Gutenberg #29345](https://www.gutenberg.org/ebooks/29345), snapshot `pg29345.txt`. Its front matter retains 1916 and 1921 copyright dates; the tool identifies the collection's 1916 publication.
- August 1915 magazine appearance: [The Atlantic original issue](https://www.theatlantic.com/magazine/archive/1915/08/a-group-of-poems/306620/). This source has earlier textual variants; the tool uses the specified Gutenberg text.
- The poem opens Mountain Interval: the first poem in #29345's body.
- Every meaning, counter-reading, fit mark and contradiction mark is explicitly editorial analysis from the spec, not a universal fact or automated judgment of a student's prose.
- Scope thresholds and the Because checks are workshop heuristics, described in notes.md. Counts refer to tagged passages, not a proportion of words.
- Contrast recomputed with sRGB luminance: brand/white 5.56, brand/paper 5.07, ink/paper 15.21, muted/paper 6.35, against/paper 6.00, focus/paper 4.56. White on Topic 6.00, Move 6.80, Meaning 7.92. `facts.json` includes source hashes.

## Break it

- Scope and fit: swept every finite chip pair and meaning. Meter matches current tags; no saved best score or completion award exists.
- Stopword-only Because: `that this with from` gets two open circles.
- Cheap `fair better`: finds both prescribed word connections, but explicitly asks for an explanation. Draft also flags this explanation work.
- Copying W23 verbatim: triggers both connections, but the copied-quotation detector asks for reasoning. Rechecked in the browser.
- A developed explanation passes the two word nudges without the short/copy warning. These checks cannot establish quality; a crafted unrelated sentence can still match both words. The spec requires these lexical checks, so they are never presented as a grade or an overall success result.
- Duplicate evidence, unlit evidence and a fourth card are rejected. Changing scope prunes stale evidence and clears the old contradiction response.
- Sixth save opens a replace dialog; no silent eviction or sixth slot. Replacement stays at five.
- Typed HTML remains inert; own-words drift gets a visible warning. Free prose never changes the chip-based light.
- Hand-edited draft survives changed evidence and gets a reconciliation note. Reload preserves saved theses, evidence and paragraph. Cancel clear preserves them; confirm clear removes tw.v1 and both texts.
- Blocked localStorage: usable six-passage state with a session-only notice. No uncaught error.
- Two real taps 60 ms apart while the 150 ms fade is active: latest topic Framton, no lit passages, Too narrow and Nothing lit yet all agree. No stale outcome.

## Voice walk

Real 120 ms held clicks at a two-second tap pace, default Sound setting, muted Chrome. No recorded audio was created. The smooth-narrator/Algieba inventory has 15 fixed lines and uses the kit's browser fallback.

Main path: topic Vera, Story move, N1, Show me, Save, Use this one, W6/W7/W8 with Because writing, Draft, Copy. Spoken keys: `w-build`, `meaning`, `w-prove`, `proveBecause`, `w-draft`. The early Build welcome is cut when the next instruction becomes relevant; its instructions remain in the hint/Read path.

Side path: broad and narrow changes twice each, Frost Roads + Equal + N3, contradiction link, Prove, a deliberately cheap Because, Swap. Spoken: `ready`, `broad`, `narrow`, `broad`, `narrow`, `w-build`, `meaning`, `against`, `popular`, `w-prove`. The scope events are events; the how lines do not nag. `play-results.json` keeps the full logs.

Read, Sound and Motion were exercised by the audit. Read and Motion repeated-click cases were clean; Sound cuts speech as intended. Re-tapping a selected mode no longer hushes its instruction: the repaired two-tap case records one w-prove and no cuts.

## Feel check

Best moment: a familiar Frost claim crosses four consecutive lines and still leaves the choice to revise or defend it with the student. The lamps, cross marks and exact linked language make the consequence tangible.

Flattest moment 1: a valid early choice lit passages farther down the story, leaving the visible page quiet. Added a complete miniature passage-lamp strip and a deliberate Show me action; text never jumps on a chip tap.

Flattest moment 2: bench information slipped below the fold, and selected evidence could bury the remaining choices. Pinned the meter and primary action, then pinned a compact evidence picker above the actions. At 680, 1366 and 375 all remaining choices stay visible after a pick; the focused Because field is also in view.

The 30-45 minute depth is in comparing claims, giving reasons and revising the paragraph, not in repeating chip cycles. I would continue to revise a real paragraph here; cycling chips alone would become flat. No timer, points or confetti.

Both bar tools were opened. `sheets/feel-comparison.jpg` places the 1366 writing room beside Beat Lab. This tool is quieter, as the spec requires, but has a painted setting, paper depth, an active lamp surface and a concrete student-made paragraph.

## Done when

1. PASS: six exact Vera + Story passages and Workable, independently calculated and checked in the DOM.
2. PASS: Any + Any 23/Too broad, Window + Planted Thin, Window + Ending zero/Nothing lit yet.
3. PASS: Frost four contradictions and links to R9-R12, including a phone Text frame.
4. PASS: N0 sets Summary in both texts across all tested pairs.
5. PASS: no quote word/keyword gives open circles; one of each gives both word checks, with an extra nudge for cheap matching.
6. PASS: assembled quotation/id/Because/answer content, editable paragraph and successful Copy; zero HTTP(S) requests in the writing walk.
7. PASS: reload, save replacement, evidence/draft retention, cancel clear and confirmed clear tested.
8. PASS: manuscript larger than bench at 1366 and 680; paragraph largest in Draft. Frames inspected.
9. PASS: real 60 ms tap spacing during the fade leaves the final chip, text lights and meter synchronized; repair-rapid.json.
10. PASS with compact tradeoff: no sideways scroll; all chips and meter fit at 680. At 375 the Text/Bench tabs provide access and the meter stays pinned; the claim and secondary writing controls can need bench scrolling.
11. PASS for browser narration and image loading: main how path, repeated events, both painted headers, no people. Authored bank recordings remain intentionally unrecorded.

## Wave lessons

- Hint and voice: PASS. mode/state updates are immediate, Read uses the hint, how lines use heard checks, and no action waits for audio. The compact hint now names the visible Use this one action; selected-mode repeat taps preserve speech.
- Focus and layout: PASS. no load focus, visible keyboard ring, stable chip controls and a reserved hint. Repaired Use this one, saved-thesis use and Make my draft preserve focus on the new mode button; real held-click results recorded.
- Sizes and targets: PASS. seven STANDARDS sizes and a 375 host inspected, with 44 px targets. No horizontal scroll in the functional frames.
- No giveaways: PASS. this is a transparent drafting instrument, not a hidden-answer quiz. Word matches are labeled as limited nudges; no success score exists.
- Honest numbers: PASS. editorial tags and passage-count assumptions are stated. Low-fit claims remain visibly low fit in Draft.
- Standards: PASS. students shape a claim (W.9-10.2), choose and explain evidence (W.9-10.9), and answer a competing reading (RL.9-10.1).
- Motion off: PASS. Audit found nothing running forever; authored CSS stops loops and transitions, preserving interaction timing.
- Short choices: PASS. Chips stay visible; the repaired picker keeps every remaining workable-set choice visible, including at 680 and 375. Long text and saved writing scroll.
- Resize mid-animation: PASS. synchronous state/class updates; no moving-node model to lose. Audit completed with no exceptions or controls left disabled after resizing.
- Welcome: PASS. no welcomeAfter delay; a relevant action can cut the early welcome.
- Unknown as unknown: PASS. unchosen fields show bracket prompts and Choose; Nothing lit yet is explicit.
- One look, one meaning: PASS. lamp means included, check means tagged fit, cross means tagged challenge. Grayscale inspected.
- Badge truth: PASS. no mastery badge. Checklist reports the stored writing state and its limits.
- Hint changes back: PASS. mode changes and chip changes recompute the current action; fixed the desktop Show me hint that named a phone-only tab.
- No copying-word answer: FAIL as a semantic test. Short and copied inputs are flagged, but the prescribed lexical nudges cannot judge whether a complete explanation is sound. No grade or mastery claim is made; a human reader remains necessary.

## Audit leads

Single audit completed on the frozen pre-repair bundle: 30 leads. No runtime exceptions, endless animations or resize lockups. Ten five-click voice cases were clean. All leads are accounted for below; the full audit was not repeated after repairs.

- Eight name leads (seven own-words sizes and the Because state): fixed with explicit textarea accessible names. Associated visible labels remain.
- Four closed-disclosure overlap leads: fixed by explicitly hiding closed details content. Real open/close check reports zero closed textarea rectangles.
- Two iframe/no-hint leads: helper coverage gap. Independent 375-host Build, Text, Draft and repaired Prove/Text-switch runs completed without console errors or sideways overflow. This is not described as an audit phone pass.
- Two compact Save-hint/scroll leads: fixed by naming the visible Use this one action. Secondary writing and saved-thesis controls still scroll.
- Three mode-action focus leads: fixed. Use this one and saved use land on m-prove; Make my draft lands on m-draft.
- Two hidden evidence-choice leads: fixed with the pinned picker. Every remaining choice is on screen after W6 is selected at 680, 1366 and 375, with targets at least 44 pixels. The focused Because field also fits.
- Three modal-background leads: intended. Native dialogs cover and disable the bench behind them; the replacement choices and clear/cancel controls remain usable. Removed the inappropriate background-hint keep requirement for future audits.
- Three missing-welcome leads on empty Prove, empty Draft and premature Use this one: intentional valid alternatives. They speak the enabled next action rather than claiming unavailable evidence exists. The full writing path hears all mode how lines.
- Three quick repeated-mode speech cuts: fixed by avoiding a hush when the selected mode is tapped again. Targeted native taps 0.7 seconds apart record no cuts.

The helper only discovers modes inside header; this tool uses a sibling top ribbon. Explicit evidence/draft states and the separate real writing walk cover those modes. Corrected future state-size labels from 375 to 375x812 and expanded mode states; the completed audit used the original state plan. One retry of two focused shots corrected a selector-quoting error in the test harness; both then ran without errors.

## Frames looked at

Opened both bar frames, both finished WebP images, initial and compact check frames, all 12 full-run frames, all eight targeted final frames, and the three phone-host frames. Sizes: 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900, 375x812.

Also inspected all 28 audit PNGs through five named contact sheets, with direct views of compact Prove, clear and replacement dialogs; all eight repair frames and two repair phone frames. The final focused-field correction was re-shot and inspected at 680 only.

## Art made

Two generated watercolor headers, no people. Prompts: `art/prompts.json`; built-in image tool, copied to `art/raw/`, processed only with free `art.py --rekey`. Both inspected at their finished size. Files: art/tw-open-window.webp and art/tw-yellow-wood.webp. No redraw needed.

Art 324.1 KB, recorded voice 0 KB. Final bundle 547.1 KB against the 2 MB goal. Original 260 KB art budget exceeded by 64.1 KB to keep the detailed paintings; the complete bundle remains well below 2 MB.

## Art still to paint

None.

## Engine changes wanted

No kit changes. Audit helper limitations are listed below.

## Left open

- Authored voice bank recordings are intentionally absent; browser speech is used.
- Lexical word connections cannot prove reasoning. This is a spec limitation, not a mastery check.
- Audit helper phone context and automatic mode discovery remain coverage limitations, backed by independent tests above. At compact sizes the full thesis, quote cards and secondary writing controls need panel scrolling; all chip choices, the meter and primary actions remain reachable.
- The original spec is unchanged. Open questions were settled as recorded in handoff.md.

Final file hashes, closed-port checks and bundle sizes are in `_scratch/thesis-workshop/build-manifest.json`. All started Chrome instances and the 8785 server are closed; host.html is removed.
