# Codex report: medical-test-paradox

## Built
Build only. Four modes, seven cases, seeded random towns, a pooled convergence chart, six question matches,
an addition-rule overlap, a conditional-independence tree, prediction locks and accessible chart summaries.
Five generated paintings, kit theme and Curio.voice. No commits, deployment or polish round.
The probability engine specified by the spec is absent; local mechanics are the documented workaround.
The completed report is written last because the prompt requires stopping at that point.

## Numbers check
Independent Python calculations: Scratch/numbers.json and source-numbers.json.
C1: TP 90, FN 10, FP 891, TN 9009; positives 981; 9.1743119%; negative predictive value 99.889123%; union .0991.
C2: TP 2700, FP 630, 81.081081%; C3: TP 99, FP 999, 9.016393%; C4: TP 81, FP 80.19, 50.251256%.
C5: TP 4500, FP 450, 90.909091%; C6: 100%; C7: TP 50, FP 4950, 1%.
C4's full-town final classification is TP 81, FN 19, FP 80.19, TN 9819.81. The tree's second-stage negatives
are 9 and 810.81 because only first positives take that second test; the grid also includes first negatives.
Slider extremes: 0.10% and 99.9000999%. All calculations use unrounded values.
The 300-group independent multinomial check gave a pooled mean of 9.17131%, SD .09003 points and worst error
.26442 points. Single towns gave SD .91669 points, with 1st/99th percentiles 7.08418%/11.33201%.
These agree with the spec's approximate random-run claims; seeds differ, so exact sample summaries differ.
Contrast: brand/panel 5.264, brand/section 4.988, brand/stage 5.616, dark ink/brand 5.522, ink/stage 15.688.
The actual slightly lighter slate icon color gives 5.834:1 on stage, above the graphics minimum.

## Facts checked
- Sensitivity is TP/(TP+FN), specificity TN/(TN+FP), PPV TP/(TP+FP), and NPV TN/(TN+FN).
  Source: Shreffler and Huecker, StatPearls NBK557491, checked through its indexed NCBI text on 2026-11-05:
  https://www.ncbi.nlm.nih.gov/books/NBK557491/ . Direct opening hit NCBI's browser check.
- Prevalence changes predictive value under the model. Source: the same StatPearls article and the worked
  natural-frequency arithmetic in Gigerenzer et al., https://pubmed.ncbi.nlm.nih.gov/26161749/ .
- The study credit is 2007, volume 8(2), pages 53-96, verified on PubMed. The DOI contains 2008; this does not
  change the journal's publication year. The tool uses the 2007 credit.
- The statement about physicians doing better with natural frequencies is supported by APS's October 17, 2008
  release, paragraphs describing the screening study. It is scoped to the example, not all physicians:
  https://www.psychologicalscience.org/news/releases/just-a-numbers-game-making-sense-of-health-statistics.html .
- Addition and conditional-probability rules, independence and multiplication along branches: CCSS HSS-CP,
  checked at https://www.thecorestandards.org/Math/Content/HSS/CP/ .
- Every displayed case value is a fictional model input or a computation from those inputs. Glimmer fever is
  explicitly fictional. The repeat-test assumption is stated, and the coin example is verified algebraically.

## Break it
- Prediction sweep: all values 0 through 100 left the result hidden before reveal. No accuracy meter or progress
  reward exists for sweeping. Revealing locks the attempted prediction; changing the hidden input and clicking
  reveal again did not alter the locked value.
- No score, badge, best score or stored mastery state exists. Cases are comparisons rather than a pass gate.
- The untouched 50% default is already near C4's answer. The close-prediction voice now describes numerical
  closeness rather than claiming the student used the skill. Chance success cannot award a mastery claim.
- Question matching: a wrong drop sprang back and gave the fraction it actually asks about. Real drag input and
  keyboard selection both matched correctly. Trying every option can obtain instructional feedback, as specified,
  but cannot create a score or completion claim. Numerically identical numerator/denominator pairs are accepted.
- Random runs: identical seed 12345 returned identical counts; seed 12346 changed them. The 100-town C1 chart
  ended at 9.082080%, only .092232 points from 9.174312%, in 1897.5 ms.
- Run interruption: changing p to .30 after nine completed towns kept all nine chart points and marked stopped.
  The original expected reference is retained for that partial chart. The new town settings take effect at once.
- Zero positives: N=1000, p=.001, se=.5, sp=.999, seed 4 gave TP=FN=FP=0 and TN=1000. The result explicitly
  said there was nothing to divide; no NaN percentage was presented as a probability.
- Slider interruption during a beat canceled old work and retained the new 30% prevalence and 81.08% result.
  Retapping reveal and later stale callbacks could not overwrite the new state.
- Table row taps retained focus on the same DOM button. The tree and table redraw from the same unrounded data.
  Evidence: math-results.json, cheat-results.json and the interaction/extra/keyboard frames in Scratch.
- Comparing the C4 grid with its readout exposed a mismatch: the grid originally showed first-test counts.
  It now shows the full-town two-test classification and labels its plus as positive twice; the browser probe
  returned 81, 19, 80.19 and 9819.81 with 50.25%. C4's question explicitly asks about two positives.
- Number boxes round to their advertised 0.1% precision: entering 1.23 gave p=.012, not a hidden 1.23% value.
  Public hooks also accept C1-C7 case IDs and natural row/column labels without crashing.
- Random-town Chances uses the displayed first-town counts, then the assumed repeat-test rates. Seed 12345
  at p=.012 gave 116 caught cases and 104.4 expected double positives; 1.29% x 89.92% x 90% agrees at 1.044%.
  An empty condition branch uses the assumed rate on its zero probability mass, without division by zero.
- Convergence is visible while running, including its zero-point start. Phone, preview and portrait chart probes
  had empty layout-failure arrays. A 100,000-person, 100-town run completed in 1783.3 ms without blocking controls.

## Voice walk
Browser fallback only; no recordings were requested or made. The 14-line inventory equals the tool's L table.
The metadata selects curious-librarian/Aoede; the browser supplies its available voice in this build.
Initial held-click testing exposed a queued Positives only instruction displaced by the next action.
Reveal now hushes the stale prediction line so the next instruction can start. Surprise is queued ahead of the
follow-up instruction; coin is queued ahead of its follow-up. Side-path tests covered Sound off, Read, reset,
mode switching during Read and Sound back on. Sound-off lines remained unmarked and Read logged the current hint.
The final held-click, 2.1-second path started these lines in order: wTown, predictHow, positivesHow, surprise,
wTable, wSecond, wCases, coin. All mode welcomes and required action instructions started. Later optional
afterPositive and afterTable follow-ups were dropped when their mode was left; they were stale at that point.
Speech cuts after a real action reflect the state change. No required mode welcome was lost or repeated.
Evidence: voice-final.json and voice-side.json. This verifies the scheduler log, not a listening review of Aoede.
Changing prevalence stopped the old false-alarm claim before the new 90.91% result. Leaving Coin stopped its
event claim, and changing Table question dropped old answer feedback. These context changes retain valid how lines.

## Feel check
Best moment: the raspberry positives remain while the huge negative crowd fades, leaving 90 caught cases against
891 false alarms and the student's locked prediction beside 9.17%. The 81 versus 80.2 split on the next test is
the stronger second reveal. This feels like a probability instrument suitable for Grade 10, with no confetti.
Flattest moment 1: Cases originally put a wall of story before the prediction, and Show answer fell below the
small preview. Numerical settings and prediction now come first, with the story below the action. The glossary
opens in a dialog so its chips do not compete with the round's controls.
Flattest moment 2: the repeat tree became tiny in short windows. A separate vertical tree now draws at the actual
available size, with abbreviated branch labels and readable count text. Counts and Chances remain immediate.
Both bar tools were bundled into Scratch and opened, without writing to their tool folders. The side-by-side
comparison is Scratch/feel-comparison.png, using this tool's positive reveal and Beat Lab's instrument screen.
The exact chart grid appropriately has less painted detail than a scene. The pro frame, responsive tree, animated
sort, retained prediction and five paintings give it comparable care within this spec's numerical scope.

## Done when
1. PASS: C1 TP 90, FN 10, FP 891, TN 9009 and 90/981 = 9.17%; live browser plus independent Python.
2. PASS: C2 81.08%, C3 9.02%, C5 90.91%, C7 1.00%; math-results.json.
3. PASS: C4 tree leaves 81 and 80.2 on average; 50.25%; first-second and second-1000 frames.
4. PASS: Positive 90/981, Has it 90/100, addition .0991; first-table and fixed-table-680 frames.
5. PASS: seeded repeat/change and pooled convergence checks described above.
6. PASS: 100,000 people tested and drawn without exceptions; the legend states ten people per square with remainders.
7. PASS: Town/Cases grid, Table table and Second test tree are the main stage focus at 1366x768 and 1000x625.
8. PASS: the test pauses for prediction; locking/skipping continues; changing a slider cancels a beat; stopped
   convergence charts retain their completed points. Targeted preview/phone prediction frames show the pause.
9. PASS: filled/outline and plus signals remain distinct in grayscale; all five paintings load. C4 and Second test
   use two cassette images. Tall Town uses the painted band; short Town hides it as specified.
10. PASS with secondary scrolling: every required size keeps the grid and primary result visible. All seven case
    choices and all six Table questions are visible in their layouts. Story and addition details can require panel
    scrolling at short sizes; the glossary opens in a dialog. A keyboard-only C1 path used Enter, Shift-Tab, Shift-Tab, Enter,
    ending at 9.17% with prediction 50. Table Enter/Tab/Enter selected the Negative column and 99.89%.
    No required narration names a disabled control. No focus is taken on load.
11. PASS: all offline tool drive batches were free of console errors, warnings and exceptions. No external src/href,
    unresolved art token or authored em dash was found. Parent-host favicon noise was fixed in its test wrapper.

## Wave lessons
- Hint/voice PASS: immediate hints, Curio.voice heard-state scheduling and held-click main/side paths.
- Focus/layout PASS: stable table and question controls, no initial focus, preventScroll focus moves on reveal,
  reserved hint space and final small-screen visual corrections.
- Sizes PASS: all eight required sizes checked; 44 px targets; targeted table/tree/prediction repairs verified.
- No giveaways PASS: no percent or count answer before a case reveal, no predictive meter to sweep, no score.
- Honest numbers PASS: expected versus random labels, seed, ten-per-square scale and conditional-independence note.
- Standards PARTIAL: the specified conditional-probability, table, addition, independence and tree content is built;
  B.9 counting remains outside this tool, as the spec explicitly states. No thin counting feature was added.
- Motion off PASS: calm frame reported zero infinite animations and preserved the test's instructional pacing.
- Short choices PASS: seven case cards and six question choices are all laid out, with no hidden carousel.
- Resize mid-action PASS: resize-sort drive had no exception; the audit's resize checks are recorded below.
- Welcome timing PASS: mode welcomes start on entry and the first action does not wait; no welcomeAfter used.
- Unknown as unknown PASS: pre-test readout/counts show question marks; prediction result stays hidden.
- One look/one meaning PASS: fill means condition, plus means test-positive, both retained in grayscale.
- True badges PASS: there is no success or permission badge; labels derive from counts and actual run status.
- Reversible hints PASS: reset and mode switches update hints immediately; Read uses the current hint.
- No copied-word answer PASS: the Table task maps a sentence's denominator to numeric fractions, not label pairs.

## Audit leads
The full audit ran once and completed within its 40-minute cap, with 22 leads. No full audit was rerun.
All eight initial size checks, Motion off, resize stress and five held-click tests were clean. Leads answered:
- Eight overlap leads: the same 760-wide Table collision repeated for mode entry and Has it. Fixed with a bounded
  panel allocation and compact table spacing. The targeted audit measurement reported no overlaps or clipping.
- Four cut-choice leads: three Cases layouts plus the preview prediction panel. Fixed by putting settings and
  prediction first, keeping Show answer visible, and moving glossary chips into their dialog. Targeted measurements
  at 680, 800, 1000 and 375 widths were clean, including C4's longer prediction setup.
- Three focus-loss leads: C7, C3 and the generic Cases walk after Show answer vanished. Fixed by capturing focus before hiding it and moving
  to the selected card with preventScroll. Real held-click checks ended on case-7 and case-3.
- Three welcome leads: Cases originally used a how entry for its welcome; it now uses V.welcome and targeted logs
  show a spoken welcome. Test everyone and Positives only intentionally replace the initial welcome with the
  action's own instruction, as STANDARDS requires; the main 2-second walk heard every required instruction.
- Two unchanged-control leads: Reset on pristine Table and Second test. These are intentional idempotent actions,
  with kit tones. There is no lost work to reset in those states.
- Two quick-tap cuts: Positives only and Reset. Fixed by retaining still-valid speech and treating a pristine
  reset as a no-op. Final 0.7-second held-tap tests recorded one whole afterPositive and one whole wTown, no cuts.
Fourteen targeted follow-up frames used the same audit measurement function, plus data/focus/voice probes.
All measured overlap, clipping, target, keep-region, name, scroll and hint arrays were empty. The final compact
C4 check put both Reset and Glossary bottoms at 417.94 inside the 425-pixel viewport. Read definition followed
by Escape closed the glossary, restored its prior hint and returned focus to Glossary without a speech wait.

## Frames looked at
All seven first-frames were opened individually, including both bar tools. All ten interaction frames were looked
at through two labeled sheets, with the positive reveal also opened at full size. All twelve full-size frames
were looked at through two sheets; Table and Second test at 680 were also opened individually.
The three initial phone frames exposed the table and Cases issues. All four phone-final frames and all five
targeted fix frames were opened individually. Initial phone-host favicon 404s were confined to the generated
parent wrapper, not the offline tool; the final wrapper adds a data favicon and its five fix shots were clean.
All eight extra frames were looked at through two sheets, and all three keyboard/zero-positive frames through
one sheet. The side-by-side feel comparison was opened. All 81 audit frames were inspected through seven labeled
contact sheets; the 760-wide table failure was also opened individually. All fourteen targeted frames were
inspected through three sheets; the C4 preview, large lab painting and glossary at 680 were also opened directly.
The final C4 preview, Read/close state and full C4 reveal were each opened individually. The final C4 grid and
second-stage tree values were checked separately to ensure their different negative totals are intentional.
The two final person-glyph frames, three stale-speech frames, three compact-chart frames, three final-math
frames and three portrait/timing frames were inspected. Final portrait Cases and chart measurements were clean.
Motion off entered sorting immediately and finished after 889.2 ms, with zero infinite animations.

## Art made
Five assets generated with the built-in image tool. Coin redrawn once because the first cutout retained a green
ground fringe. All five finished assets were inspected in Scratch/art-contact.png; updated coin inspected in
the final case-card frames. No image depicts people. All raw PNGs are in art/raw and final WebPs in art/.
Assets: town-street, test-strip, clinic-hall, lab-rack and coin-flip. Full prompt set: art/prompts.json.
Art totals 238.83 KB. Recorded voice is 0 KB. The final bundle is 755.58 KB, well below the 2 MB goal.
The town band is shown at tall sizes and hidden below 900 px tall as specified. Each case uses its painting;
the twice-tested case and Second test each show two cassette images. Numerical diagrams stay in code.

## Art still to paint
None. No generation failures or missing paintings.

## Engine changes wanted
Supply the absent kit/probability.js and docs/families/probability.md interfaces listed in handoff.md, then migrate
the local mechanics. No shared engine was modified.

## Left open
The shared-engine dependency cannot be satisfied in this checkout without violating the write boundary.
B.9 (+) counting is not taught, as the spec says. Broad module codes are retained and the gap is documented.
The fictional screening framing and historical credit are retained per the spec's leaning.
STANDARDS wins the timing contradiction: Motion off retains the two 950 ms beats and the 880 ms sort beat,
while removing movement. The sort picture changes instantly; the next instruction retains its timing.
The requested named bank voice is not an authored recording; narration relies on the browser fallback.
Temporary host.html was removed after each phone batch. All Chrome and server processes started by the build
were closed. Scratch retains command scripts, JSON probes, profiles, frames and audit evidence for review.
