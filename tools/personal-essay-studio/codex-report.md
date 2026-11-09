# Codex report: personal-essay-studio

## Built

Built all four modes as a private Grade 11 writing desk: ten neutral Spark cards, a native Draft editor, five-question Zoom lens, wide-shot finder, transparent signal meter, reflection frame, named versions, word diff, alternate openings, paragraph sequence board, read-aloud notes and plain-text copy.

Files are confined to tools/personal-essay-studio/ and _scratch/personal-essay-studio/. The generated image tool used its documented default output folder before the selected images were copied into the tool. No commits, shared-file changes, uploads or polish round.

The final offline bundle is 289237 bytes, about 282.5 KB. Its SHA-256 is 939c870f6560fc6aef418ae28eb5cf74a52609c8d573f83df8bb93a8cfd64e56. The draft metadata has stage=built.

## Numbers check

Before implementation, prepare.py recomputed the sample counts independently from spec.md. numbers.json preserves every counted signal and phrase.

| Sample | Words | Raw close-ups | Raw wide shots | Per 100: close / wide |
|---|---:|---:|---:|---:|
| Wide shot | 94 | 1 | 10 | 1 / 11 |
| Zoomed | 155 | 13 | 0 | 8 / 0 |

The browser agrees. Phrase precedence counts "a big success" once. The Zoomed sample has no finder matches. Bars appear at 50 words; the explicit visual cap is 25 signals per 100, while printed counts continue. A 287-word draft with limit 250 displays "over by 37".

Recomputed contrast on paper: brand 6.78:1, ink 14.52:1, muted 6.30:1, focus 5.61:1. These slightly differ from the spec but pass AA for their uses. Singular counts and multiline quoted spans received final calculation checks.

## Facts checked

| Student-facing content | Source and verification |
|---|---|
| Narrative situation, dialogue, detail, sequence and reflection | [CCSS W.11-12.3a-e](https://www.thecorestandards.org/ELA-Literacy/W/11-12/), checked at build. Practiced through the student's own Spark, lens notes, ending and sequence decisions. |
| Planning, rewriting and comparing approaches | W.11-12.5 on the same official page; actual versions, opening trials and order trials implement it. |
| Ten prompts, five lens questions, samples, ending frame and signal lists | Original Curio Class content in spec.md, copied into content.json. Sample statistics are computed, never stored as answer constants. |
| Five sparks, ten versions, 50-word threshold, chosen 250/500/650/none limits | Spec's interaction rules, verified with direct assertions. These are interface settings, not claims about essay quality. |
| Privacy and local saving | Bundle has no external request code; localStorage is guarded. A real reload, blocked-storage banner, two confirmations and DOM cleanup were checked. Read never receives student writing. |
| Generic college application word-range sentence | Omitted using the spec's permitted fallback. The [current prompts page](https://www.commonapp.org/apply/essay-prompts/) did not expose a current range; the available [official interface PDF](https://www.commonapp.org/files/Common-App-UI-updates.pdf) identifies the older 2025-2026 cycle. |
| Kitchen and tortilla images | Visually checked against the original fictional sample. No people, lettering, logos or cultural generalizations. Sensitivity is documented in handoff.md. |

## Break it

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

## Voice walk

The held-click main path used 120 ms presses and about two seconds between actions, with default Sound. Actual start logs, not merely queued lines, show: w-spark, small, w-draft, lens, finder, w-then, w-revise, saved, opening.

The side path exercised finder off/on, Read priority, Sound off/on and Sequence board. w-draft, finder and order started; Read is logged separately. A stale Revise welcome with an already saved version was correctly dropped. All four modes' main how-to lines started.

The audit's five-click checks were clean. Its four rapid-mode welcome cuts were fixed by ignoring the already active mode; all four focused retests have cuts=[]. First-card welcome skips are permitted by BASELINE rule 16, and the next instruction remains visible and reachable through Read.

voice/lines.json contains 27 fixed lines and calm-professor, currently Schedar in the kept bank. Browser narration is fallback; no audio was recorded. Acoustic voice quality was not assessed from muted headless playback.

## Feel check

Played the whole main writing path, then a side path and a keyboard-only path. The first card responds immediately, without an introduction blocking it. Later work changes the task from choosing a moment to detailing, reflecting, comparing openings and testing paragraph order.

Best moment: the student's own three reflection entries become a visible ending frame, while the wide kitchen and torn-tortilla photographs make the camera metaphor concrete.

Flattest moment 1: the original lens required scrolling before its fifth question and Drop action. Changed it to a compact desktop drawer, five columns in short landscape, and a pinned Drop action with internally scrolling phone fields.

Flattest moment 2: the ending initially appeared below the fold. Draft an ending now brings its result and Add action into view. The payoff stays the student's words and an editable result.

bar-comparison.png places the final example frame beside Beat Lab. Both bar tools were bundled and opened from Scratch. The writing studio intentionally has more quiet paper space, while its photographs, material cards, rose ink and typography have a finished visual character. Prompt cards stay text-only as specified.

## Done when

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

## Wave lessons

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

## Audit leads

The single full audit completed with 51 leads. audit-disposition.md answers every lead group and the welcome/rapid-tap rows. It preserves the original failures rather than claiming a clean rerun.

Fixed: target widths, accessible names, clipped landscape cards, utility dock, compact reflection/Compare/Sequence actions, lens focus and fields, visible lens hint, hover contrast and rapid-mode welcome cuts. Retained: vertical portrait card/form scrolling and the geometry conflict in Done when 8.

The first audit's phone host was served by two orphan test processes. Both exact command lines were verified and terminated; phone reruns pass. The initial sequence fixture had a JavaScript newline quoting error, silently ignored by the audit helper. The corrected fixture and direct three-paragraph checks pass. No second full audit ran.

## Frames looked at

101 driver/audit PNGs were inspected directly or in contact sheets: bar-frames (2), early-frames (2), functional-frames (1), final-functional-frames (1), visual-frames (12), more-frames (12), live (5), audit (36), post-frames (12), retry-frames (8), final-target-frames (3), quick-frames (6), last-frames (1).

Failed host and fixture frames remain as evidence. The corrected phone states, complete compact controls, live drag, keyboard notes, grayscale and Motion off frames were inspected. bar-comparison.png is the finish comparison.

## Art made

Two original images made with the built-in OpenAI image tool, no redraw required: art/pes-kitchen-wide.webp and art/pes-tortilla-close.webp. Full prompts and house style are in art/prompts.json; selected source PNGs are in art/raw/. Both are marked drawn_by=codex and people=false.

Total finished art is 138030 bytes, about 134.8 KB, against the preview budget of 260 KB. Recorded voice is 0 KB. Bundle is about 282.5 KB against the 2 MB goal. Both final 960x540 WebP files were viewed and used at large size in the example drawer.

## Art still to paint

None. No people are required or depicted.

## Engine changes wanted

No kit changes. Proposed audit-helper fix only: scripts/audit_tool.py, Audit.steps, should surface self.ev's audit_error for a JavaScript fixture instead of ignoring it. Exact change and reason are in handoff.md. Shared files were not edited.

## Left open

- The strict 680 largest-paper condition conflicts with the half-height sheet; the sheet and uncovered sentence take priority. Portrait walls/forms retain necessary vertical scrolling.
- The meter and private ticks cannot establish writing quality or the truth of a memory. They explicitly avoid making that claim.
- No recorded voice, as instructed. Unlimited-length comparisons use a full LCS matrix and were not stress-tested at book scale.
- Three initial read-only commands lacked an explicit deadline. Subsequent commands used bounded runners/timers. The early-report instruction was resolved in favor of the user's stop-on-report instruction: evidence accumulated in Scratch, and this final report is written last.
- Two test host processes initially outlived their wrapper; both were verified and terminated. Final cleanup finds no owned Chrome/host processes, no tool host.html, and closed ports 8795, 9990 and 9991.

Build only is complete. No commit or polish round.
