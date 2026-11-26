# Thesis Workshop: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: thesis-workshop

#### Built

One offline literary writing room with Build, Prove and Draft, complete Saki and Frost texts, passage lights, four meter readouts, five saved theses per text, evidence explanations, contradiction response, editable paragraph, local Copy and confirmed clear.

All authored files are in `tools/thesis-workshop/`; scripts, source snapshots, profiles, logs and frames are in `_scratch/thesis-workshop/`. No commits or polish round. Working commands use deadline wrappers; two initial read-only probes completed before the wrapper was installed. The direct user stop rule takes precedence over creating this report early.

#### Numbers check

`make_data.py` independently mapped the source ranges and recalculated every topic/move pair. All spec counts agree. `numbers.json` preserves all 30 Saki pairs and 24 Frost pairs.

- Saki topics: V 12, W 7, F 10, A 7. Moves: P 4, I 12, H 8, S 6, E 2.
- Vera + Story: W6, W7, W8, W10, W11, W22; Workable; N1 fits all six.
- Window + Planted: W7, W19; Thin. Window + Ending: zero; Nothing lit yet.
- Framton + Irony: eight; N2 fits five. Any + Any: 23; Too broad.
- Saki pair distribution: 14 Workable, 4 Thin, 8 Too narrow, 4 Too broad, as stated.
- Frost topics: R 12, C 10, T 5. Moves: Q 6, G 4, F 5, S 2, D 1.
- Roads + Equal: R6, R7, R9-R12; N1 fits six; N3 fits zero with four crossed lines. Any + Any: 20.

Browser checks passed 1,105 assertions with zero failures, including every chip pair with all four concrete meanings. `final-functional.json` is the result. Quote typography is normalized and the full text's words are checked in order against the downloaded originals.

#### Facts checked

- Complete story, characters, quoted words and passage openings: [Project Gutenberg #269](https://www.gutenberg.org/ebooks/269), plain-text source snapshot `pg269.txt`.
- Saki is H. H. Munro: [Project Gutenberg author record](https://www.gutenberg.org/ebooks/author/152), which names Hector Hugh Munro as his alias.
- Beasts and Super-Beasts, John Lane, 1914: #269 credits its transcription from that edition.
- Complete poem, twenty lines, order and double hyphen in line 18: [Project Gutenberg #29345](https://www.gutenberg.org/ebooks/29345), snapshot `pg29345.txt`. Its front matter retains 1916 and 1921 copyright dates; the tool identifies the collection's 1916 publication.
- August 1915 magazine appearance: [The Atlantic original issue](https://www.theatlantic.com/magazine/archive/1915/08/a-group-of-poems/306620/). This source has earlier textual variants; the tool uses the specified Gutenberg text.
- The poem opens Mountain Interval: the first poem in #29345's body.
- Every meaning, counter-reading, fit mark and contradiction mark is explicitly editorial analysis from the spec, not a universal fact or automated judgment of a student's prose.
- Scope thresholds and the Because checks are workshop heuristics, described in notes.md. Counts refer to tagged passages, not a proportion of words.
- Contrast recomputed with sRGB luminance: brand/white 5.56, brand/paper 5.07, ink/paper 15.21, muted/paper 6.35, against/paper 6.00, focus/paper 4.56. White on Topic 6.00, Move 6.80, Meaning 7.92. `facts.json` includes source hashes.

#### Break it

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

#### Voice walk

Real 120 ms held clicks at a two-second tap pace, default Sound setting, muted Chrome. No recorded audio was created. The smooth-narrator/Algieba inventory has 15 fixed lines and uses the kit's browser fallback.

Main path: topic Vera, Story move, N1, Show me, Save, Use this one, W6/W7/W8 with Because writing, Draft, Copy. Spoken keys: `w-build`, `meaning`, `w-prove`, `proveBecause`, `w-draft`. The early Build welcome is cut when the next instruction becomes relevant; its instructions remain in the hint/Read path.

Side path: broad and narrow changes twice each, Frost Roads + Equal + N3, contradiction link, Prove, a deliberately cheap Because, Swap. Spoken: `ready`, `broad`, `narrow`, `broad`, `narrow`, `w-build`, `meaning`, `against`, `popular`, `w-prove`. The scope events are events; the how lines do not nag. `play-results.json` keeps the full logs.

Read, Sound and Motion were exercised by the audit. Read and Motion repeated-click cases were clean; Sound cuts speech as intended. Re-tapping a selected mode no longer hushes its instruction: the repaired two-tap case records one w-prove and no cuts.

#### Feel check

Best moment: a familiar Frost claim crosses four consecutive lines and still leaves the choice to revise or defend it with the student. The lamps, cross marks and exact linked language make the consequence tangible.

Flattest moment 1: a valid early choice lit passages farther down the story, leaving the visible page quiet. Added a complete miniature passage-lamp strip and a deliberate Show me action; text never jumps on a chip tap.

Flattest moment 2: bench information slipped below the fold, and selected evidence could bury the remaining choices. Pinned the meter and primary action, then pinned a compact evidence picker above the actions. At 680, 1366 and 375 all remaining choices stay visible after a pick; the focused Because field is also in view.

The 30-45 minute depth is in comparing claims, giving reasons and revising the paragraph, not in repeating chip cycles. I would continue to revise a real paragraph here; cycling chips alone would become flat. No timer, points or confetti.

Both bar tools were opened. `sheets/feel-comparison.jpg` places the 1366 writing room beside Beat Lab. This tool is quieter, as the spec requires, but has a painted setting, paper depth, an active lamp surface and a concrete student-made paragraph.

#### Done when

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

#### Wave lessons

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

#### Audit leads

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

#### Frames looked at

Opened both bar frames, both finished WebP images, initial and compact check frames, all 12 full-run frames, all eight targeted final frames, and the three phone-host frames. Sizes: 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900, 375x812.

Also inspected all 28 audit PNGs through five named contact sheets, with direct views of compact Prove, clear and replacement dialogs; all eight repair frames and two repair phone frames. The final focused-field correction was re-shot and inspected at 680 only.

#### Art made

Two generated watercolor headers, no people. Prompts: `art/prompts.json`; built-in image tool, copied to `art/raw/`, processed only with free `art.py --rekey`. Both inspected at their finished size. Files: art/tw-open-window.webp and art/tw-yellow-wood.webp. No redraw needed.

Art 324.1 KB, recorded voice 0 KB. Final bundle 547.1 KB against the 2 MB goal. Original 260 KB art budget exceeded by 64.1 KB to keep the detailed paintings; the complete bundle remains well below 2 MB.

#### Art still to paint

None.

#### Engine changes wanted

No kit changes. Audit helper limitations are listed below.

#### Left open

- Authored voice bank recordings are intentionally absent; browser speech is used.
- Lexical word connections cannot prove reasoning. This is a spec limitation, not a mastery check.
- Audit helper phone context and automatic mode discovery remain coverage limitations, backed by independent tests above. At compact sizes the full thesis, quote cards and secondary writing controls need panel scrolling; all chip choices, the meter and primary actions remain reachable.
- The original spec is unchanged. Open questions were settled as recorded in handoff.md.

Final file hashes, closed-port checks and bundle sizes are in `_scratch/thesis-workshop/build-manifest.json`. All started Chrome instances and the 8785 server are closed; host.html is removed.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Handoff: thesis-workshop

#### Structure

`src.html` starts from the kit starter. The CSS is organized as room frame, manuscript, chips, promise meter, evidence cards, paragraph, and responsive layouts. The single script owns state, persistence, the chip predicates, text lighting, saved theses, evidence, paragraph assembly, and Curio.voice. `content.json` is loaded by a `json:content` bundle token and contains complete source text plus character ranges and tags. Generated HTML is the offline deliverable.

The promise meter and the primary action stay fixed beside a scrolling work page. Prove pins its evidence picker above the primary actions, so choosing one quotation cannot bury the other choices under the new card. At small landscape sizes the chip labels shorten, with their complete wording retained in accessible names and titles. At portrait widths of 760 and below the Text and Bench tabs share the workspace; Text shows the lit count. Draft expands the paragraph and reduces the manuscript to passage ids; its phone Text tab still opens the full text.

`window.__tool` exposes state, mode and text changes, chip selection, meter and Because predicates, paragraph assembly, the voice inventory and `vlog` for review. Browser checks, count calculations, source snapshots, full-size frames, contact sheets and process wrappers are in `_scratch/thesis-workshop/`.

#### Decisions and spec tensions

- Retained the complete mild ghost story for grade 10, as the spec leans. Teacher notes name its fictional drowning and graveyard material.
- Retained Frost's popular reading as N3. The four crossed passages make its evidence problem visible rather than hiding that reading.
- Preserved Frost's line 18 with `--`, as requested in Content. Saki's original long dashes also become `--` to obey the no-em-dash build rule. Words are unaltered; source whitespace and italic markers are normalized.
- Used the requested built-in image tool rather than the older local FLUX instruction. Both paintings have `people: false` and `drawn_by: codex` in prompts.json.
- Kept the spec's light writing room and its explicit palette. This is a mature writing instrument with no points or confetti.
- The brief asks for an early report, while the user's direct instruction says to stop when the report is written. Evidence was accumulated in Scratch; `codex-report.md` is written once as the final build action.
- Used the existing bundled bar tools for the required visual opening. Rebundling another tool would violate the user's write boundary.
- The exact prescribed Because predicates are word matches, so they cannot validate reasoning. They stay visible as non-graded nudges. Copied quotes and very short matching-word inputs receive a separate explanation prompt. Draft never awards an overall success score or badge. A crafted unrelated sentence can still match both words; a reader must judge it.
- “Workable or better” has no better category in the scope scale. Draft checks Workable; Too broad is not treated as better.
- Meaning's Any chip leaves the interpretation uncommitted. It says Pick a meaning and requires a concrete meaning before Use this one, rather than inventing fit tags for an unspecified interpretation.

#### Persistence and revision

Only `tw.v1` is used for writing. All storage operations are caught; the session continues with a notice if access fails. Five snapshots are allowed per text and a sixth opens a replacement dialog. Evidence ids are unique and must be lit. A chip change removes evidence outside the new scope and clears the old contradiction response. Paragraph edits survive evidence changes, with a reconciliation notice. Clear removes both texts after confirmation and does not immediately recreate the key.

#### Voice

Bank: smooth-narrator, Algieba. No recordings were generated, as instructed. Browser fallback supplies speech. Read speaks the current hint, never the literary text. The first completed topic-and-move pair starts the meaning instruction immediately so it is not lost behind the welcome at a two-second tap pace. Scope events use event narration; how lines use heard checks and state validity. Mode changes hush stale speech.

#### Sensitivity

The story is an early twentieth-century English fiction with a fabricated tale set near the Ganges, the historical phrase “pariah dogs,” and reference to a cemetery. Review whether preserving the original wording with the teacher-note context is appropriate. Do not present Vera's invented account as factual information about India. The tool touches fictional fear and death, not health guidance. Paintings are empty landscapes and an empty room, with no people.

#### Engine changes wanted

None. Shared kit files are unchanged.

#### Audit helper limitations

The single audit's `scripts/audit_tool.py` mode discovery looks only inside a `header`. This tool's top mode ribbon is a sibling of the title header, so automatic mode discovery misses it. The explicit evidence and paragraph states, the separate held-input writing walk, and the phone frames cover those modes. A future helper change could include `nav.seg[aria-label="Workshop mode"] button` in `MODES_JS` without changing the tool's layout.

The audit's phone context lookup failed on its own host. The independent 8785 host run successfully inspected the actual 375-pixel iframe and recorded zero console errors and no sideways overflow. The final report distinguishes those results from missing audit coverage. State-size labels in audit-states.json use the helper's exact `375x812` spelling.

#### Art still to paint

None. Two watercolor headers are generated, inspected and bundled. Raw images and prompts are retained. There are no people assets.

#### Build verification and next review

The independent content/browser run passed 1,105 assertions. The single mechanical audit completed with 30 pre-repair leads and no exceptions, infinite motion or resize lockups. Its tool findings were repaired and verified through focused held-click and frame checks. Repaired Prove choices and the focused Because field fit at 680, 1366 and 375; mode transitions retain focus; repeated selected-mode taps do not cut speech; rapid chip taps keep the final state synchronized.

The full source, generated bundle and evidence hashes are in the Scratch build manifest. Chrome ports 9980-9983 and server 8785 were checked closed, and tool host.html is removed. On this Windows session taskkill left three test-host processes alive; stop_host.py identified only command lines for this tool's exact host invocation and terminated them. The reusable Scratch host wrapper now terminates and waits on its own process directly.

The next step is the separate cold Build review requested by the owner, not another polish round in this session. Review the quality of actual student explanations, the compact scrolling tradeoff, authored voice recording when authorized, and the sensitivity notes. The lexical checks intentionally remain formative word nudges and cannot be a semantic assessment.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-09)
- 2026-11-25: handoff.md folded in (last changed 2026-11-09)
