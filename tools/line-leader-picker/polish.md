# Polish: line-leader-picker (Codex fix, round 1)

The user's Curiosity brief takes precedence over the legacy lesson spec and Refine. The workbench has no kit header, grade tags, forced quiz, answer gate, score, level or finish screen. The existing evidence questions are optional observations in any order; both fairness opinions are independent and ungraded. After the first quiet hint, speech is requested with Read. The exact automatic-narration requests below are left explicitly NOT FIXED instead of claiming a lesson-style pass.

Evidence paths below are relative to `_scratch/line-leader-picker/`. Named JSON files in that Scratch root record the numbers or Read log for the corresponding frames. Original source is preserved as `src-before.html`; Refine was not edited.

## Blocker
None in Refine.

## Should fix
1. **NOT FIXED as prescribed: automatic three-answer narration chain.** Reproduced dropped feedback and evidence at both 3.5 s and 6 s in `before-voice-3.5.json` / `before-voice-6.json`. The Curiosity replacement removes automatic questions and answer grading. Repeated held-click chains at both paces have zero automatic speech entries, with observations `[false,true,true]` and matching facts. See `after-chain-3.5.json`, `after-chain-6.json` and their frames in `after-break-frames/`. Read speaks the current evidence. No automatic chain is claimed.
2. **FIXED: premature Our chart facts.** Before: C had `[true,true,true]` with all observations null. After: summaries is `{}` before any inspection, and the first inspection records `[true,null,null]`. See `before-summary.json`, `after-summary.json` and `after-functional-frames/after-summary.png`. A freely chosen fairness call may create a row with unknown facts, since Curiosity calls do not require the observations.
3. **FIXED: visible evidence and chosen verdict.** Q1 highlights both step pictures on the selected rule; Q2 rings empty columns; Q3 also marks the tallest counts. Each inspected chip has a 24 × 24 px yes/no fact mark. Both verdicts have a blue outline and white inset when pressed. See `after-functional-frames/after-rule-read.png`, `after-sizes-frames/after-fair-680.png`, and final re-shots `after-compact-frames/final-fair-680.png` / `final-fair-375.png`. The marks show facts, never correctness grades.
4. **FIXED: two meanings for thumbs.** Evidence controls now use check/cross pictures with Yes/No accessible names; thumbs remain only on fairness opinions. fChecks and q0/q1/q2 name the new controls, with the bank matching runtime. Compare `before-frames/before-mismatch.png` with `after-compact-frames/final-fair-680.png`; see `validation.json`.
5. **FIXED: Q1 points to the rule.** A mismatch readout says “Think about the rule, not this month's stickers.” followed by the rule line. `before-rule-mismatch.json` captured the old chart instruction. `after-rule-read.json` records the new exact Read sequence; the rule's step pictures are highlighted in its frame at 1366 × 768.
6. **FIXED: Q2 names the actual count.** Seed 7 has six empty columns. Read requests “Six friends never got a turn.”, then “Being left out feels sad.”, then the separate same-chance explanation for C. `after-count-read.json` and `after-functional-frames/after-count-read.png` prove it. The singular classmate line remains only in classmate readouts.
7. **FIXED: the old tile identifies the changed slot.** Before: tapping old Stays at the front left `which:true`, glow 0. After: glow 2 marks the new Goes to the back tile, the twenty counts remain 1, and the optional inspection ends. See `before-old-tile.json`, `after-old-tile.json` and their 1366 × 768 frames. Any first inspection can leave the comparison prompt; there is no correct-answer gate.
8. **FIXED: selected tile re-taps preserve the month.** Before: both modes lost all days and counts. After: Change retains Ant 20 and no new Before; Make retains all twenty days. Five further step-1 re-taps also retain twenty days. See `before-retap.json`, `after-retap.json`, `final-state-patterns.json` and their frames. Tile names remain available through Read; an unchanged Change tile adds the specified same-step explanation.
9. **FIXED: Bee's absence has a counterfactual test.** The same uniform day-2 draw is compared with the all-present jar. Bee's absence sentence is included only when Bee has zero turns and would otherwise have led. A omits it, B includes it, and C follows the paired draw. `after-bee.json` records A/B/C/D. `after-model.json` checks 1,000 paired C months: zero mismatches, 15 affected zeros and 382 unaffected zeros. Counts and the persistent bed mark are visible in `after-functional-frames/after-bee.png`.
10. **FIXED: saved calls survive new months.** A saved false verdict remains false after New month and the next inspection. Additional card re-taps, attendance switches and mode round trips preserve healthy false and sick true independently. See `before-verdict.json`, `after-verdict.json`, `final-state-patterns.json` and the summary frames.
11. **FIXED: summary wording and Close label.** An empty board uses “Check a rule card first. Its row fills in here.”; the invitation appears only after two rows have a verdict. The return instruction names X, and Close is visible at 1366 and above. See `after-summary-empty.json`, `final-summary-two.json`, `after-functional-frames/after-summary-empty.png` and `after-values-frames/final-summary-two.png`.
12. **FIXED: compact stickers are readable.** Before: 680 stars were 8 × 4.39 px, 800 stars 8 × 6.25 px, phone stars 7 × 4.39 px. After: both gold and all twenty dashed Before stickers are 12 × 12 px at 680 × 425, 800 × 500 and 375 × 812. Dense short cells reserve space for the count instead of drawing stars through it. See `before-stars-680.json`, `before-stars-800.json`, `before-phone-fixed.json`, `after-fair-375.json`, `final-before-680.json`, `final-before-800.json`, `final-before-375.json`, and the matching final frames in `after-values-frames/`.

## Polish accepted
1. **NOT FIXED as automatic speech; Read order FIXED.** The tile name precedes Tap Run in `after-tile-read.json`: “The leader goes to the back of the line. Tap Run to play our month.” No automatic how-to queue is retained, following the Curiosity voice rule.
2. **FIXED: Q3 wording.** The chip uses the full spoken question. Our chart uses the same picture with “Led more, one none?”. See `after-compact-frames/final-fair-375.png` and `after-values-frames/final-summary-two.png`.
3. **FIXED: name slip placement.** The slip is positioned inside the jar scene. At 1366 × 768 its rectangle has zero intersections with all twenty calendar squares. See `after-jar-slip.json` and its frame in `after-break-frames/`.
4. **FIXED: projector type.** At 1920 × 1080, rule names are 18 px, questions 20 px, evidence 17 px, verdicts 19 px. See `after-projector.json` and `after-functional-frames/after-projector.png`.
5. **FIXED: Fair hint names visible material.** Fair uses fChecks while its month runs, rather than naming the hidden machine. See `after-break-frames/after-model.png` and `after-model.json`.
6. **FIXED: Bee's bed remains visible.** The bed mark is tied to the switch, rather than exactly two completed days. All four finished-rule tests have `bed:true` in `after-bee.json`.
7. **NOT FIXED: re-offer the Who quiz.** The forced Who overlay was removed under the Curiosity brief. Its explanation is in the Manual and the authored rule card stamps without an answer. `after-retap.json` and `after-make-calm.json` show no Who overlay after finished months. Reintroducing an unanswered quiz would violate the user's instruction.
8. **FIXED: Rule B's explanation.** `final-B-read.json` records “Every friend comes to the front in turn, so everyone has the same chance.” at the B rule inspection.
9. **FIXED: accepted nits.** tie11 through tie20, most1 and zero20 were removed. All four compact utilities have title labels. Run's darker gradient top gives 5.218:1 white-text contrast, formerly 4.40:1. See `validation.json`; final compact geometry records every utility visible and tappable.

## Settled calls
- Designed count/classmate overlap and icon-only font-size-zero controls remain intentional; the animal cast and all 47 existing paintings were kept.
- The older welcome-cut cases are superseded by one quiet first hint and explicit Read. No welcome screen or new welcome requirement was added.
- Classmate narration is now its current readout plus Read; there is no queued tail to race a later tap.
- Q2 uses the actual zero-count sequence, as settled in should fix 6.
- Thumbs remain on verdicts; observation controls and fact markers use yes/no pictures.
- Our chart displays data facts, never right/wrong marks for observations or verdicts. Unknown cells stay unknown until inspected in that recorded month. The previous recorded month stays until replaced.
- Keyboard focus, Motion off, sixty-pixel controls and the offline bundle were rechecked. The header-only audit discovery limitation is documented below rather than restoring a kit header.

## Cheats tried
- All No on C still shows the actual Yes/Yes/Yes facts, empty columns and tallest counts; it earns no score or pass.
- Fair before inspecting any question is allowed and ungraded. Q3 can be inspected first. `after-free-explore.json` records all three evidence controls enabled independently.
- A's deliberately inaccurate first Yes records the data's No without awarding anything. `final-summary-two.json` keeps the student's Fair opinion distinct from that fact.
- Repeating selected step 1 five times preserves the twenty-day result. Card re-taps, switching Bee twice, and mode round trips preserve the separate saved calls. `final-state-patterns.json`.
- Interpreter stress: 6,000 A/B/D months with/without absence and 1,000 C counterfactual pairs, zero mismatches. `after-model.json`. Independent Python sampling and occupancy arithmetic agree in `validation.json`.

## Voice walk
- Read log requests, each once at its relevant inspection: Q1 rule correction plus C rule line; six-friend count plus feelings plus same-chance line; chosen tile name then Run; B's equal-chance line; two-row summary invitation and X return instruction. Evidence: `after-rule-read.json`, `after-count-read.json`, `after-tile-read.json`, `final-B-read.json`, `final-summary-two.json`.
- Held-click chains at 3.5 s and 6 s have zero automatic question or feedback entries. This proves the Curiosity replacement, not the Refine's requested automatic chain.
- `voice/lines.json` equals allLines(): 165 unique lines. Browser voice is the current fallback; missing recorded clips were reported by the bundler and no recorded-take quality claim is made.

## Engine changes wanted
`scripts/audit_tool.py`, MODES_JS: add `nav .workstations button` to its header-only mode selectors. The current audit cannot automatically discover these Curiosity workstations. Both other workstations have explicit audit states; its automatic per-mode control walk remains limited. No shared script or kit file was edited.

## Audit
The single full audit completed within its 2,400-second limit, with 71 inspected frames and 267 mechanical leads. Report: `fix-audit/audit.md`; every bullet has a disposition in `audit-disposition.md`. No full audit was repeated. The final bundle differs from the audit snapshot only by the scoped geometry/accessibility repairs below; both hashes are recorded in `final-validation.json`.

- **FIXED: 1000 × 625 New month clipping.** The short side panel now reserves 264 px. New month ends at x=995 within the 1000 px viewport. `flow-fair-1000.json` and `after-flow-frames/flow-fair-1000.png`.
- **FIXED: marks touching wrapped headings at 760 and 375.** Marks now live in the diagram row, with enough row height to contain them. All three heading/mark intersections are zero at 680, 800, 760, 1000, 1366, 1920 and 375. All markers remain 24 × 24 px; all tested controls are visible, at least 60 px and tappable. `flow-fair-*.json` and `after-flow-frames/`.
- **FIXED: projector Bee caption/On-Off overlap.** The switch uses separate grid rows for state and caption. Intersection is zero for both On and Off at 1920 × 1080. Main projector type remains 18/20/17/19 px. `audit-fixed-bee-False.json`, `audit-fixed-bee-True.json` and matching `after-audit-frames/` images.
- **FIXED: Manual close/heading overlap and covered keyboard targets.** A sixty-pixel title row gives zero close/heading intersection at 680, 1366 and 375. The open drawer makes the workbench inert and keeps Tab inside; Escape restores the workbench and focus to Manual. `audit-fixed-manual-*.json` and the Manual frames in `after-audit-frames/`.
- **Intentional: compact count/button overlap.** The readout belongs inside the large classmate hit area; count text and the painted classmate remain visually separate. This is the settled compact-bank pattern, including the blue Before numbers.
- **Intentional: font-size-zero utilities.** Their visible icons, accessible names and title labels remain. **Intentional: Manual covering #board.** The requested drawer covers the workbench while open; closing restores it.
- **Settled: three first-hint cuts on quick mode taps.** BASELINE 16 permits these. There are no mode welcomes or automatic question chains to restore.
- The 29-control single-click/keyboard walk had no console errors or lost-focus failures. Ten repeated-input checks passed. Final resize stress had no exceptions or controls left disabled; Motion off had no endless animation.
- After the audit, only affected geometry was re-shot: `after-audit-frames/` and `after-flow-frames/`. An intermediate phone placement still overlapped Q3 by 48 square pixels; the structural diagram-row repair reduced it to zero. Gold and Before stickers remain 12 × 12 px at all three named compact sizes, including a full twenty-star phone column.
- `final-validation.json` records all final assertions, source/bundle hashes, unchanged Refine hash, and closed ports 9910, 9911 and 8715. No commits were made. Generated host.html was removed.

## The real material
- Curio Class, Line Leader Picker, `tools/line-leader-picker/spec.md`: authored fictional animal class, twenty-day model and four rule definitions. Content CC BY 4.0, as stated in the original tool's licence header. Interpreter `src.html`: MIT. Named in the Manual and tool.draft.json.
- Existing illustration collection: “Illustrations generated with OpenAI gpt-image, edited for Curio Class”; supplied Curio Class content, CC BY 4.0. No art downloaded, regenerated or removed. Jar paintings are explicitly schematic; chart counts are exact.
- No empirical dataset, new real-world fact, quoted standards text or outside download was added. No data-gathering time was used. Model results were checked against the independent MIT Python implementation in `validate.py`: expected C zeros 7.169718448, sample mean 7.171 over 10,000 months. The browser interpreter gave 7.14 over a separate 1,000 seeds. These are model checks, not two empirical sources.
- Runtime network resource list is empty in `final-state-patterns.json`. The bundle is 1,252,995 bytes and self-contained. Source licence references were checked in the existing local files on 2026-11-06.

## Curiosity decisions and limits
- No unattended question was sent. The brief determined the choices: explicit Read, optional evidence, no quiz gate, wooden instrument controls, Manual and engraved plate, no invented catalogue number.
- The legacy spec and concepts file have no Line Leader Curiosity entry or plate number. `curiosity:true`, `plate:null`; the visible plate omits an unassigned number. The owner must assign that metadata later.
- Lesson-creep search: “sticker” names turn-count marks and animation helpers, never rewards. “grade” occurs only in the Manual's statement that observations are not graded. No goal, score, level, badge, finish screen or quiz was added. Program step numbers are the two executable instructions, not lesson progress.

## Short test
- Would a kid open it without an assignment? Plausible from the animal cast and immediate rule changes; not independently validated in this fix.
- Would an adult play for fun? Uncertain. The replacement/rotation comparisons and counterfactuals are interesting, but the supplied four-rule scope is limited.
- Is the real material the interface? Yes: the executable rules, actual turn counts and Before outlines are the working material.
- Does it work without a score or finish line? Yes. No answer or verdict is required to continue exploring.
- No new ten-minute human-play validation or owner desk-review approval is claimed. The four reference instruments were opened and used; their frames are in `after-break-frames-contact.jpg`.

## Frames looked at
All before and targeted-after PNGs were inspected directly or in the contact sheets for `before-frames`, `after-functional-frames`, `after-sizes-frames`, `after-break-frames` and `after-compact-frames`; successful phone reproduction is in `before-phone-frames/`. Final values, all 71 audit frames, and all scoped repair frames were inspected in their contact sheets and selected full frames. The current final chart/evidence frames are in `after-flow-frames/`. An initial phone harness lookup used the outer window incorrectly; its successful re-run supplied the phone numbers above. Initial host favicon 404s were harness-only and corrected for subsequent drives.

## Left open
- The exact automatic narration chain, automatic tile/how queue, and returning Who quiz are intentionally not implemented; the Curiosity brief wins.
- The Curiosity plate number and concept entry are absent from the supplied spec. No number was invented.
- Recorded narration remains absent; Read uses browser voice. No recording or installation was attempted.
- The audit engine still discovers modes through header selectors. Explicit workstation states and targeted drives cover the other workstations; a full automatic per-mode control walk is not claimed.
- A new ten-minute human-play appeal check was not validated; the short-test answers above state that limit.
