# Personal Essay Studio: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: personal-essay-studio

#### Built

Built all four modes as a private Grade 11 writing desk: ten neutral Spark cards, a native Draft editor, five-question Zoom lens, wide-shot finder, transparent signal meter, reflection frame, named versions, word diff, alternate openings, paragraph sequence board, read-aloud notes and plain-text copy.

Files are confined to tools/personal-essay-studio/ and _scratch/personal-essay-studio/. The generated image tool used its documented default output folder before the selected images were copied into the tool. No commits, shared-file changes, uploads or polish round.

The final offline bundle is 289237 bytes, about 282.5 KB. Its SHA-256 is 939c870f6560fc6aef418ae28eb5cf74a52609c8d573f83df8bb93a8cfd64e56. The draft metadata has stage=built.

#### Numbers check

Before implementation, prepare.py recomputed the sample counts independently from spec.md. numbers.json preserves every counted signal and phrase.

| Sample | Words | Raw close-ups | Raw wide shots | Per 100: close / wide |
|---|---:|---:|---:|---:|
| Wide shot | 94 | 1 | 10 | 1 / 11 |
| Zoomed | 155 | 13 | 0 | 8 / 0 |

The browser agrees. Phrase precedence counts "a big success" once. The Zoomed sample has no finder matches. Bars appear at 50 words; the explicit visual cap is 25 signals per 100, while printed counts continue. A 287-word draft with limit 250 displays "over by 37".

Recomputed contrast on paper: brand 6.78:1, ink 14.52:1, muted 6.30:1, focus 5.61:1. These slightly differ from the spec but pass AA for their uses. Singular counts and multiline quoted spans received final calculation checks.

#### Facts checked

| Student-facing content | Source and verification |
|---|---|
| Narrative situation, dialogue, detail, sequence and reflection | [CCSS W.11-12.3a-e](https://www.thecorestandards.org/ELA-Literacy/W/11-12/), checked at build. Practiced through the student's own Spark, lens notes, ending and sequence decisions. |
| Planning, rewriting and comparing approaches | W.11-12.5 on the same official page; actual versions, opening trials and order trials implement it. |
| Ten prompts, five lens questions, samples, ending frame and signal lists | Original Curio Class content in spec.md, copied into content.json. Sample statistics are computed, never stored as answer constants. |
| Five sparks, ten versions, 50-word threshold, chosen 250/500/650/none limits | Spec's interaction rules, verified with direct assertions. These are interface settings, not claims about essay quality. |
| Privacy and local saving | Bundle has no external request code; localStorage is guarded. A real reload, blocked-storage banner, two confirmations and DOM cleanup were checked. Read never receives student writing. |
| Generic college application word-range sentence | Omitted using the spec's permitted fallback. The [current prompts page](https://www.commonapp.org/apply/essay-prompts/) did not expose a current range; the available [official interface PDF](https://www.commonapp.org/files/Common-App-UI-updates.pdf) identifies the older 2025-2026 cycle. |
| Kitchen and tortilla images | Visually checked against the original fictional sample. No people, lettering, logos or cultural generalizations. Sensitivity is documented in handoff.md. |

#### Break it

34 browser functional assertions pass, followed by eight final gate/capacity assertions and four direct calculation checks. Evidence: functional-results.json, post-functional-results.json, last-results.json and calc-check.js.

- Repeated numbers, capitalized nonsense and quoted words inflate the raw close-up count. The interface explicitly identifies surface signals, capitalization guesses and the absence of an ideal balance. No grade, best score, reward or quality verdict can be set this way.
- Stock phrases in all capitals and both apostrophe styles are found. Every abstract word is found. Embedded word fragments do not match. A phrase's abstract word is not counted twice.
- At 49 words there are no bars; at 50 there are bars. Empty punctuation does not produce a meaningful score. Multiline double-quoted text counts as one quoted span.
- Ticking both spark checks can be dishonest. They are explicitly "Your checks," not verified assessment; the read-aloud ticks are private notes. No automated skill claim or reward follows either checklist.
- Paragraph jobs can be assigned without matching the prose. The strip reports those chosen jobs and asks pattern questions; it never certifies the essay's structure. Exact reordering and its protective snapshot pass.
- Blank lens answers do not insert a block. Real notes remain the student's words and survive rewriting the anchor. A blank reflection frame retains marked blanks, with no completion badge.
- Six Add spark attempts retain five sparks and point to the usable Use this spark control. The five-card capacity cannot be exceeded through the normal controls.
- Ten named versions block a new snapshot and block both destructive opening and order applications. An unnamed version can be evicted first; named versions remain protected.
- Clear's first confirmation preserves work. The second clears the draft, versions, sparks, pending field values, comparison display and outcome. Blocking storage produces the requested banner.

#### Voice walk

The held-click main path used 120 ms presses and about two seconds between actions, with default Sound. Actual start logs, not merely queued lines, show: w-spark, small, w-draft, lens, finder, w-then, w-revise, saved, opening.

The side path exercised finder off/on, Read priority, Sound off/on and Sequence board. w-draft, finder and order started; Read is logged separately. A stale Revise welcome with an already saved version was correctly dropped. All four modes' main how-to lines started.

The audit's five-click checks were clean. Its four rapid-mode welcome cuts were fixed by ignoring the already active mode; all four focused retests have cuts=[]. First-card welcome skips are permitted by BASELINE rule 16, and the next instruction remains visible and reachable through Read.

voice/lines.json contains 27 fixed lines and calm-professor, currently Schedar in the kept bank. Browser narration is fallback; no audio was recorded. Acoustic voice quality was not assessed from muted headless playback.

#### Feel check

Played the whole main writing path, then a side path and a keyboard-only path. The first card responds immediately, without an introduction blocking it. Later work changes the task from choosing a moment to detailing, reflecting, comparing openings and testing paragraph order.

Best moment: the student's own three reflection entries become a visible ending frame, while the wide kitchen and torn-tortilla photographs make the camera metaphor concrete.

Flattest moment 1: the original lens required scrolling before its fifth question and Drop action. Changed it to a compact desktop drawer, five columns in short landscape, and a pinned Drop action with internally scrolling phone fields.

Flattest moment 2: the ending initially appeared below the fold. Draft an ending now brings its result and Add action into view. The payoff stays the student's words and an editable result.

bar-comparison.png places the final example frame beside Beat Lab. Both bar tools were bundled and opened from Scratch. The writing studio intentionally has more quiet paper space, while its photographs, material cards, rose ink and typography have a finished visual character. Prompt cards stay text-only as specified.

#### Done when

1. PASS: both checks display the qualified ◎ line; Use this spark places its text above Draft.
2. PASS: a tapped sentence is outlined; the lens stays beside/under it; Drop inserts grey indented notes without composing sentences.
3. PASS: all listed phrases and words match case-insensitively; phrase precedence works; the Zoomed sample has no wide shots.
4. PASS: independent and browser sample values are 1/11 and 8/0 per 100 words.
5. PASS: the ending frame uses all three entries and visibly marks missing entries.
6. PASS: snapshots, word LCS underline/strike, preview-only opening trials and snapshot-before-apply work.
7. PASS: two preceding paragraphs produce the correct wait question; order preview is non-destructive; applying preserves the old draft and exact paragraph text.
8. FAIL literally with the 680x425 lens open: a required half-height sheet plus header/privacy/hint leaves a paper region smaller than the sheet. Default Draft is the largest work region; desktop paper remains largest, and the outlined sentence is uncovered at both sizes. This spec conflict is in handoff.md.
9. PASS: a real second prompt tap during the flip leaves only the second card open. Native typing across autosave retains the last keystrokes.
10. PASS: actual reload preserves the complete saved payload; both clear confirmations and storage failure pass.
11. PASS: the privacy line is outside the four mode views; prompts are the neutral spec text; both images load and show no person.
12. PASS: actual 375-pixel iframe checks show scrollWidth=375, half-screen sheets, visible selected text and usable Drop. Mode controls and Draft stay available at 1366. Long phone forms scroll vertically.

#### Wave lessons

1. PASS, hint and voice: immediate state hints, Curio.voice, valid conditions, real main/side logs, Read-only fixed text.
2. PASS, focus/layout: stable native editor and controls; job chips update in place; moved DOM cards retain focus; no focus on load.
3. PASS, sizes/targets: every STANDARDS size was captured. Target repairs reserve at least 44 pixels; final compact compare and sequence actions are in view.
4. PASS, no giveaways: no hidden-answer task or quality score. Surface signals and self-reports are identified honestly.
5. PASS, honest numbers: categories, threshold, bar cap, guesses and lack of an ideal balance are stated. Counts agree with computation.
6. PASS, standards: each listed writing standard is practiced by a solo student through actual writing or revision. No family engine applies.
7. PASS, Motion off: no infinite animation remains; flipping becomes instant; art stays present.
8. FAIL under the literal all-choices-at-once rule on portrait phones/760: the prescribed phone card wall and long writing forms require vertical scrolling. All ten Spark cards now fit the short landscape previews; the phone exception is retained explicitly.
9. PASS, resize mid-action: native rapid flip and window resize passed; the audit found no exception or stuck enabled state.
10. PASS, no late welcome: no welcomeAfter queue; first action has priority; rapid active-mode taps no longer hush narration.
11. PASS, unknown shown honestly: blank drafts/versions are blank; no inferred completion or hidden-state claim.
12. PASS, one look/one meaning: solid close-up bars, hatched wide-shot bars, dotted/dashed finder marks, explicit labels and grayscale frame.
13. PASS, badge truth: size marks say Your checks; no private check becomes a verified accomplishment.
14. PASS, hints change back: mode/finder/lens transitions restore the appropriate hint. A full spark list points to Use this spark.
15. PASS, no answer by copied words: this is authoring and self-revision, with no answer-matching quiz or sample-copy score.

#### Audit leads

The single full audit completed with 51 leads. audit-disposition.md answers every lead group and the welcome/rapid-tap rows. It preserves the original failures rather than claiming a clean rerun.

Fixed: target widths, accessible names, clipped landscape cards, utility dock, compact reflection/Compare/Sequence actions, lens focus and fields, visible lens hint, hover contrast and rapid-mode welcome cuts. Retained: vertical portrait card/form scrolling and the geometry conflict in Done when 8.

The first audit's phone host was served by two orphan test processes. Both exact command lines were verified and terminated; phone reruns pass. The initial sequence fixture had a JavaScript newline quoting error, silently ignored by the audit helper. The corrected fixture and direct three-paragraph checks pass. No second full audit ran.

#### Frames looked at

101 driver/audit PNGs were inspected directly or in contact sheets: bar-frames (2), early-frames (2), functional-frames (1), final-functional-frames (1), visual-frames (12), more-frames (12), live (5), audit (36), post-frames (12), retry-frames (8), final-target-frames (3), quick-frames (6), last-frames (1).

Failed host and fixture frames remain as evidence. The corrected phone states, complete compact controls, live drag, keyboard notes, grayscale and Motion off frames were inspected. bar-comparison.png is the finish comparison.

#### Art made

Two original images made with the built-in OpenAI image tool, no redraw required: art/pes-kitchen-wide.webp and art/pes-tortilla-close.webp. Full prompts and house style are in art/prompts.json; selected source PNGs are in art/raw/. Both are marked drawn_by=codex and people=false.

Total finished art is 138030 bytes, about 134.8 KB, against the preview budget of 260 KB. Recorded voice is 0 KB. Bundle is about 282.5 KB against the 2 MB goal. Both final 960x540 WebP files were viewed and used at large size in the example drawer.

#### Art still to paint

None. No people are required or depicted.

#### Engine changes wanted

No kit changes. Proposed audit-helper fix only: scripts/audit_tool.py, Audit.steps, should surface self.ev's audit_error for a JavaScript fixture instead of ignoring it. Exact change and reason are in handoff.md. Shared files were not edited.

#### Left open

- The strict 680 largest-paper condition conflicts with the half-height sheet; the sheet and uncovered sentence take priority. Portrait walls/forms retain necessary vertical scrolling.
- The meter and private ticks cannot establish writing quality or the truth of a memory. They explicitly avoid making that claim.
- No recorded voice, as instructed. Unlimited-length comparisons use a full LCS matrix and were not stress-tested at book scale.
- Three initial read-only commands lacked an explicit deadline. Subsequent commands used bounded runners/timers. The early-report instruction was resolved in favor of the user's stop-on-report instruction: evidence accumulated in Scratch, and this final report is written last.
- Two test host processes initially outlived their wrapper; both were verified and terminated. Final cleanup finds no owned Chrome/host processes, no tool host.html, and closed ports 8795, 9990 and 9991.

Build only is complete. No commit or polish round.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: personal-essay-studio


#### Played

Grade 11, a neutral skateboard-repair memory, all four modes, lens/finder, ending, openings, comparison, ordering and private read-aloud checks. Quiet but substantial, with a strong material desk and an earned personal ending.
Read CODEX-REVIEW first and verified S:\CurioClass-codex. Initial cold play preceded builder notes/source. The cold walk reached all modes and the opening preview; later comparison/sequence clicks hit hidden controls. Those frames are failed coverage, and comparison/sequence were correctly played after source reading. A complete held-click main-path rewalk then verified the repairs. This is a process limitation, not a claim of a second blind review.

#### Findings fixed

- blocker, general, Draft lens: selecting a second sentence reused the first sentence's answers and dropped them under the wrong anchor. Reload the selected sentence's own saved answers; switching back restores them.
- should fix, general, reflection: changing a source box left an obsolete ending on screen while Add inserted different words. The visible frame now updates with all three fields and picked details.
- should fix, general, revision: an opening preview survived edits to the underlying essay. Clear it on edits and check its source text before application. Sequence drag/re-entry also clears obsolete order previews.
- should fix, general, sequence jobs: inserting a paragraph shifted old job labels onto unrelated writing. Match unchanged paragraph text; rewritten paragraphs need a new choice.
- should fix, general, text analysis: ASCII word boundaries truncated accented words and names. Keep complete Unicode words; both specified sample counts remain unchanged.
- should fix, general, focus and hints: panel controls followed ten prompt cards in tab order; returning from the example restored a generic mode instruction over a different open tool. Move the panel earlier in DOM order without changing its visual position; restore the actual current instruction.
- should fix, general, audit next-action leads: a checked Spark's Use button and an opening's application action could stay below the viewport. Reveal new checks/Use and the bounded opening preview; compact the short-landscape half-height panel. Ending and opening payoffs receive visible focus.
- should fix, general, rapid prompt voice: the second identical how-to call cut the first and then stayed silent as already heard. Repeated how-to calls no longer interrupt themselves; obsolete finder/check instructions stop when their state ends.
- polish, general, flat note handoff: bring the inserted notes into view, return focus to Draft and speak the next editing action once. The post-card writing instruction is also heard once.
- polish, general, Compare: identical or lightly changed long drafts unnecessarily allocated a full word matrix. Skip identical text and trim matching prefixes/suffixes before the same exact LCS.
- polish, general, art: redraw the weaker wide kitchen as a clearly shared room with stronger foreground/middle/background distance, matching the retained tortilla photograph.

#### Findings left

- should fix, general, spec conflict: at 680x425 the prescribed half-height lens sheet is larger than the remaining paper region. The selected sentence stays uncovered and default Draft remains the largest work area. Changing this needs a spec decision.
- should fix, general, spec conflict: portrait prompt walls, the saved-Spark list and long forms require vertical scrolling; retaining the specified individual text/checks, ten cards and 44-pixel targets takes priority over showing every choice simultaneously. The five-Spark capacity frame confirms this on the laptop panel too. The immediate next action now scrolls into view, so this does not hide the action named by the hint.

#### Break it

- Meter: actually entered sixty numbers, capitalized nonsense and sixty quoted tokens. Counts rise, but no grade, best score, completion badge or ideal-ratio claim results. The category guesses, overlaps and cap are disclosed; this is the specified surface counter.
- Finder: every stock phrase and abstract word in uppercase, apostrophe variants, embedded fragments and phrase precedence. All lists match; embedded fragments do not; "a big success" counts once.
- Threshold/count: 49 versus 50 words, punctuation-only input, a 287-word draft at 250, None, accented words. Correct bars/gate, zero punctuation words, "over by 37" and no limit.
- Spark checks: falsely ticked a whole-life topic. Badge explicitly says "Your checks" and the panel calls it judgment, not a score. No verified skill claim. Five-spark capacity is prescribed; no reward for adding easy inputs.
- Reflection: blank fields retain three marked blanks and yield no success claim. Changed a field after generating the frame; visible and inserted wording now agree. No question assumes a student mistake.
- Lens: empty answers insert nothing. Switched anchors with notes already entered; nothing crosses to the unrelated sentence. Returned to the first anchor and restored/dropped its own notes.
- Versions/openings: ten named snapshots block the eleventh and destructive application; an unnamed snapshot can be evicted first. Preview never edits the draft; application saves first. A stale preview cannot be applied.
- Sequence: arbitrary job choices earn no correctness claim. Two preceding paragraphs produce the exact wait question; missing Looking back and reversed turn/reflection patterns ask the specified questions. Moving/reordering preserves paragraph text and snapshots first; stale drag preview clears.
- Read-aloud checklist: ticked all four without reading. They remain explicitly private notes, without scoring or certification.
- Clear: first confirmation retains writing; cancel retains it; second confirmed clear removes the data. Actual reload preserved the exact draft; a thrown storage SecurityError showed the banner/Not saved while retaining the new writing in memory.

#### Voice walk

Held 120 ms clicks about 2 seconds apart, default Sound/Motion: card, Add spark, size checks, Use this spark, Draft, lens, Drop, finder, Then and Now, Pick detail, ending, Revise, Save, Opening, Compare, Sequence.
Actual starts: sparkWrite, small, w-draft, lens, notes, finder, w-then, picked, turnWrite, ending, w-revise, saved, opening, useOpening, saved, order. Initial w-spark is superseded by the first card's own applicable instruction, permitted by BASELINE 16.
Student prose never enters narration. Automatic protective snapshots can have their saved line dropped on the immediate mode switch; manual Save events are heard. Browser fallback, no recorded clips; acoustic quality was not judged from muted playback.

| Line | Kind | Expected on five uses | Actual starts |
|---|---|---:|---:|
| finder | how | 1 | 1, then four silent/heard |
| saved | event | 5 | 5 |

The completed audit reports Read and the five-press checks clean. Its one rapid-card cut was repaired and retested: one start, no cut. Finder-off now leaves no obsolete instruction playing. The complete main path was rewalked after this repair, with the same start order above.

#### Facts checked

- Narrative situation/point of view, dialogue/description, purposeful sequence, precise language and reflection: [Common Core W.11-12.3a-e](https://www.thecorestandards.org/ELA-Literacy/W/11-12/), checked live. Spark/Opening, lens, sequence, student revision and Then and Now respectively practice them.
- Planning, rewriting and comparing approaches: W.11-12.5 on the same official page; actual snapshots, opening trials and ordering implement it. No family engine applies.
- Samples, prompts, questions, phrase/sense lists and ending frame: original Curio Class content in spec.md, checked against content.json. The sample is fictional, not a recipe or historical account.
- Independently recomputed samples: 94 words, 1 raw close-up/10 raw wide shots, rounded 1/11 per 100; 155 words, 13/0 raw, rounded 8/0. All browser values agree. Phrase overlap counts once; Zoomed has no finder matches.
- Five sparks, ten snapshots, 50-word meter threshold and 250/500/650/none choices: interface rules from the spec, not quality thresholds. The implemented 25-per-100 visual cap is disclosed, with printed counts continuing beyond it.
- Generic college word-range claim remains omitted. The [current Common App prompts page](https://www.commonapp.org/apply/essay-prompts/) does not expose bounds; its [official UI PDF](https://www.commonapp.org/files/Common-App-UI-updates.pdf) is explicitly 2025-2026. The spec authorizes omission without a current confirmation.
- Privacy: localStorage only, guarded saves, fixed instruction narration, clipboard only on Copy; one inline bundle has no automatic external requests. Notes begin with the three required sections.
- WCAG calculation: brand/paper 6.78, brand/panel 7.19, white/brand 7.30, ink/paper 14.52, muted/paper 6.30, focus/paper 5.61. All pass AA; spec approximations differ slightly.

#### Sensitivity

Flag the fictional Mr. Ortega/flour-tortilla kitchen example for the cultural reviewer: ordinary individual experience, no claim to represent a whole culture or universal cooking method. Both photographs contain no people and are marked people:false. Neutral prompts do not solicit health, trauma or family conflict; the sharing/privacy line stays present.

#### Flattest moment left

Compare is quiet when the student has made only a tiny edit. Its restrained before/after evidence fits Grade 11; adding a reward or judgment would change the intended studio. The formerly flatter notes handoff now reveals the student's own usable material and points to the next edit. Try this order also exposes its actual preview instead of quietly placing it beyond the paragraph cards.

#### Graphics

Both final 960x540 images inspected at asset and in-tool sizes. The retained Beat Lab finish-comparison image was inspected; the quiet writing desk keeps its own rich materials rather than adopting that tool's look. Redrawn art/raw/pes-kitchen-wide.png -> art/pes-kitchen-wide.webp through free art.py --rekey; prompt and credit retained. Strong tortilla close-up, rose ink, taped cards, serif paper, shadows and calm idle detail preserved. Finished art 150854 bytes; inline bundle about 305 KB (312044 bytes).
Main and responsive frames inspected directly and in Scratch contact sheets, including every STANDARDS width, 375 iframe, grayscale and Motion off. No infinite calm loop. Keyboard route reached Spark, Draft, Z-lens and editable dropped notes without pointer input.

#### Audit

One final audit completed within its 40-minute limit: Chrome 9951, host 8755, 41 frames inspected, 32 leads. No second audit. Full group disposition: _scratch/personal-essay-studio/audit-disposition.md.
Confirmed and repaired: hidden Spark/Opening next actions, ending focus, repeated-prompt how-to cut. Post-fix scoped checks cover 1366, 680 and a real 375 iframe; the complete voice path was replayed. The real pointer drag now changes paragraph order exactly; the original drag fixture started in a clipped row and is retained as failed coverage.
Dismissed: eleven native-modal background occlusions, three sticky-header/scroll-edge overlaps, ten first-card welcome omissions permitted by BASELINE 16, and the utility selector grouped as an answer set. Retained: prescribed portrait/form scrolling. Resize stress, console, targets, focus and calm rows otherwise clean.
Early phone audit rows failed because owned test-host processes survived taskkill and served a deleted host file. Exact command lines were verified, only those owned processes were terminated, and the correct host then returned 200. Independent phone frames replace no missing audit rows; that limit stays explicit. Scoped selector/scroll-timing fixture errors were corrected and are not counted as passes.

#### Left open

No kit, spec or unrelated folder changes; no commits. Work and evidence stay in the two authorized folders; imagegen's documented default output was copied into the tool.
Unlimited book-scale comparisons of unrelated texts still have quadratic LCS cost; identical and small-edit 10,000-word cases take about 2 ms in the tested browser. This is an essay studio, not a book comparison benchmark.
The initial read command and a quoting-failed read attempt lacked an explicit deadline; subsequent commands used explicit bounded jobs or subprocess runners. No command hit its time limit.
The generated iframe host's favicon 404 is a fixture warning, not a request by the inline tool (which has a data favicon). No tool exceptions or console warnings were observed. Early missing phone-audit rows remain a verification limit; the separate phone checks passed. Owned host/Chrome cleanup is verified before this report is installed.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Personal Essay Studio handoff

#### Source map

src.html starts from the kit starter and uses kit:curio plus kit:theme-912 with the spec's light rose palette. Its sections are responsive styles, stable HTML controls, word/sentence analysis, persistence, editor mirroring, version diff, sequence board and handlers. content.json is loaded by the bundle token and holds the spec prompts, samples, lists and fixed voice lines. No network requests occur in the bundled tool.

The writing surface is a native textarea with an identically laid-out, aria-hidden text mirror behind it. The mirror draws sentence outlines, finder underlines and grey note text without rebuilding the input or moving its caret. Sentence offsets select the original text; lens answers are stored by sentence text. Note blocks remain plain editable draft text when their anchor changes.

Cold review fixes: changing the selected sentence reloads its own lens answers; Drop notes reveals the inserted block and returns focus to Draft. Editing reflection fields updates the ending preview. Any draft edit invalidates the opening preview; a source-text guard also protects application. Dragging or rebuilding the sequence clears its old preview. Jobs follow unchanged paragraph text across insertion, rather than drifting by index. Unicode words retain their complete spelling. Compare trims common prefixes and suffixes before its exact word LCS, and identical versions skip the matrix. Very long unrelated texts still have quadratic LCS cost.

The side panel comes before the workspace in DOM order, with explicit grid positions retaining the same visual layout. Its controls precede the ten Spark cards for keyboard users. currentHint restores the actual open revision, lens, finder or ending instruction when leaving the example. The post-card writing instruction and note handoff are now spoken once.

Audit-confirmed follow-ups: Add spark reveals/focuses its new checks, and completing both checks reveals Use this spark. A compact three-column panel layout at short landscape keeps the required half-height sheet usable. Ending and opening generation focus their visible application actions; opening previews scroll internally when long. Try this order reveals its preview and keeps the sticky application action available. hint() only interrupts for a not-yet-heard how-to, so repeated prompt taps cannot cut the same instruction and silence its remainder. Finder-off and completed checks hush only their obsolete active how-to; Read remains under the kit's priority rules.

At narrow widths, the same hint moves into a strip above the workspace. It also moves there while the desktop lens hides the panel. The native input remains stable. The phone lens scrolls its five fields internally and keeps Drop notes visible. In short landscape frames, all five questions fit across the bottom sheet. Sequence reordering moves existing DOM cards; job chips update without rebuilding the focused controls.

#### Decisions and contradictions

- No open questions remain in the spec. Its settled ten neutral cards and prompt 7 wording are retained.
- The user's image-tool instruction overrides the spec's local FLUX method. Both requested photographs were made with the built-in OpenAI image tool. Both have people:false.
- The requested seven-line preview supersedes older memory notes about five lines.
- The user's instruction to stop when codex-report.md is written conflicts with CODEX-BUILD's early-report instruction. Evidence and report notes were accumulated in Scratch; the final report is written last and ends Build.
- The current Common App prompts page does not expose a current word-range statement in its readable text. The official available interface PDF is for 2025-2026. Following the spec's fallback, omit the generic college-limit claim and retain the 250/500/650/none picker.
- Recomputed sample counts match. Contrast ratios vary slightly: brand/paper 6.78, ink/paper 14.52, muted/paper 6.30, focus/paper 5.61. All meet AA for the uses here.
- Ten named versions are protected. When no unnamed version can be dropped, saving and destructive revision application stop with a clear instruction to unname a version. This resolves the unspecified all-named capacity case.
- Spark size ticks and read-aloud ticks are self-reports. A student can tick them without doing the thinking; they are labeled as the student's checks and have no score or verified skill claim. A private memory's time and place cannot be verified by this offline interface.
- At mobile widths the panel and lens use half-height bottom sheets. Long forms and the ten-card wall scroll, as the phone spec requires. The main mode controls remain visible.
- Done when 8 conflicts with the mobile sheet requirement at 680x425. A 212.5-pixel-high sheet plus header, privacy and hint leaves a paper region shorter than the sheet. The default Draft paper is the largest work region, and the selected sentence remains above the open sheet. The literal largest-region condition with that sheet open is not met.
- Revision tabs sit above the work so they stay directly reachable when the narrow panel becomes a bottom sheet. The open revision tool remains the sole main work area.

#### Sensitivity

The original example names Mr. Ortega and makes flour tortillas in a community kitchen. Check that the fictional experience and images remain ordinary and respectful, without implying a universal cultural cooking method. Student prompts are neutral and do not solicit health, trauma or family conflict. No generated people are shown.

#### Engine changes wanted

No kit engine changes. Shared kit and scripts were not edited. Existing Python lacks NumPy; the free art.py --rekey command was run with the existing S:/AI/tts/.venv/Lib/site-packages on sys.path, using the permitted Python executable.

scripts/audit_tool.py, Audit.steps, the `elif 'js' in s` branch: retain the return value of self.ev and surface an `audit_error` as a state-step failure. It currently ignores JavaScript syntax errors. The first sequence fixture contained literal newlines in a single-quoted JavaScript string, so that audit frame was empty. The fixture now uses JSON-escaped text; the working three-paragraph board is covered by direct tests.

#### Art

art/prompts.json contains the full house style and prompts. Cold review redrew pes-kitchen-wide with the built-in imagegen tool to show the shared room and camera distance more clearly, preserving the warm photographic style and the strong tortilla close-up. The selected raw images are in art/raw and the free converter produced the two WebP files. Voice uses browser fallback via Curio.voice; calm-professor and every fixed line are listed for later recording. No audio was recorded.

The current bank maps calm-professor to Schedar and marks it kept. The spec's delivery style is retained in voice/lines.json.

#### Evidence

Build evidence, bounded command runner, computations, screenshots, functional checks, voice walks and audit output are under _scratch/personal-essay-studio/. The bar tools were copied and bundled only inside Scratch to preserve the two-folder write restriction. No git commits or polish round.

The single audit reads its initial bundle snapshot. Later repairs are covered by targeted frames and functional assertions, not a second full audit. Two orphan test host processes caused the audit's original 375-pixel iframe failures. Their exact command lines were verified and both owned processes were terminated. Subsequent phone lens, panel and example frames pass. The host runner now terminates its own process handle and waits for exit.

#### Cold review verification

The one review audit completed within 40 minutes: 32 mechanical leads, 41 inspected frames. The audit's initial 375 host failed because owned test-host processes survived cleanup; those exact processes were verified and closed. Do not treat the missing phone-audit rows as passes. Independent real 375 iframe checks and the post-fix Spark action check pass, with no horizontal overflow.

Confirmed audit fixes were re-shot only in their affected states at 1366, 680 and 375. Rapid repeated prompt taps now produce one uninterrupted how-to start. The complete main writing path was rewalked after the narration change; all mode instructions are reached in order through the applicable post-card instruction, with no student prose spoken and no console errors. Real whole-pixel pointer dragging correctly reorders paragraphs. The final inline file is 312044 bytes.

The complete finding list, named factual sources, spec conflicts and verification limits are in codex-review.md. Scratch holds audit-disposition.md, review-validation.json and all retained failed fixtures, screenshots and logs. All owned Chrome and host ports are closed, and host.html is absent. No kit changes or git commits were made.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-08)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-08)
- 2026-11-25: handoff.md folded in (last changed 2026-11-08)
