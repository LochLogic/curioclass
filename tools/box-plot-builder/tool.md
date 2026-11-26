# Box Plot Builder: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: box-plot-builder

#### Built
Three offline newsroom modes: Explore, Build and Headline. Nine original generated paintings, precise engine charts,
strict positional card work, bounded attempts, separate Build progress per set, and an earned fourteen-field report.
Files include readable src.html, bundled HTML, tool.draft.json with stage built, notes, handoff, preview.svg,
voice/lines.json, art/prompts.json, nine finished WebPs and eleven audit states.
All work used S:\CurioClass-codex. Authored files stayed inside the tool and its Scratch folder.
Chrome ports used: 9970 through 9977. Host: 8775. No commits, deployment or polish round.
The complete report was written last to honor the user's explicit report-and-stop condition.

#### Numbers check
Independent Python recomputation: `_scratch/box-plot-builder/check_data.py` and `numbers-check.log`.
The five source arrays also match the independently extracted spec arrays exactly.

| Set | n | Min, Q1, Median, Q3, Max | Sum | Mean | MAD |
|---|---:|---|---:|---:|---:|
| San Diego | 30 | 71, 73, 74, 81, 94 | 2321 | 77.366667 | 5.313333 |
| Chicago | 31 | 62, 70, 75, 81, 89 | 2331 | 75.193548 | 5.619147 |
| Miami | 31 | 88, 91, 92, 92, 93 | 2842 | 91.677419 | 0.888658 |
| Denver | 31 | 78, 88, 93, 97, 102 | 2842 | 91.677419 | 5.321540 |
| Luka | 70 | 16, 29, 34, 39, 73 | 2370 | 33.857143 | 6.375510 |

IQRs: 8, 11, 1, 9 and 10. Displayed distance totals round to 159.4, 174.2 and 446.3 for the Build sets.
All specified bin widths were independently counted. San Diego width two gives the supplied counts.
San Diego 94 to 110: mean +0.533333, median unchanged. Moving 71 to 110: median +0.5.
Replacing the five hot-spell days with 74: mean -2.733333, median unchanged, IQR -6.
Luka 73 to 34, Chicago 89 to 110 and Miami 88 to 110 match the specified mean changes.
Miami and Denver have the same sum and mean. No numerical correction to the dataset was needed.
The Sources footer says eleven claims, although its table contains twelve claim rows; this is a documentation tally.

#### Facts checked
Checked against the named sources and frozen values supplied in the spec, without re-downloading the datasets.
- Four temperature series: NOAA NCEI GHCN-Daily, stations USW00023188, USW00094846, USW00012839 and USW00003017;
  the spec's paired NWS CF6SAN, CF6ORD, CF6MIA and CF6DEN monthly reports.
- TMAX, airport station method and Fahrenheit units: NOAA GHCN-Daily documentation and NWS F-6 temperature headings.
- Luka's points, 82 team games minus 12 missed, 70 observations and the far-off 73-point game:
  Basketball-Reference and ESPN 2023-24 regular-season logs, as supplied in the spec.
- Median-of-halves quartiles, leaving out an odd median: Illustrative Mathematics Grade 6 Unit 8 Lesson 15.
- Whiskers to minimum and maximum: IM Unit 8 Lesson 16. The local adapter implements this school convention.
- Mean absolute deviation: IM Unit 8 Lessons 11 and 12. Totals and average distances were independently recomputed.
- Shape-based choice of center and spread: IM Lessons 14 and 18 and OpenStax Introductory Statistics 2e section 2.6.
  The tool uses the specified contextual reasons, without claiming a universal rule.
- Headline means, IQRs, ranges and the San Diego below-mean count are derived from the frozen NOAA observations.
- Standards: CCSS 6.SP.4 and 6.SP.5a-d, as mapped in the spec.
- Privacy statement: code inspection confirms only localStorage for the class data, with try/catch and Clear.
Palette ratios on paper were recomputed: ink 14.16, muted 5.69, teal 5.91, rust 5.25, dots 7.85,
focus 5.15, ok 4.78 and warn 6.54. Ring 3.64 and button line 3.77 are non-text contrasts.

#### Break it
Forty-eight functional assertions passed in `functional-result.json`; targeted later fixes have separate evidence.
- n: empty input uses no attempt; September 31 fails; two misses supply the answer with Sam showed.
- Facts chips: wrong then correct cannot change Sam fixed into found. Choices shuffle and each row advances once.
- Median: equal-valued cards in the wrong positions fail. Both even-middle cards are required.
- Quartiles: San Diego card seven fails even though it also shows 73. Two misses supply the positional answer.
- Ends: choosing the two actual ends is the intended skill. Other card positions consume attempts.
- IQR: range and Q3 alone fail; after two misses the working is supplied without independent credit.
- Mean: median, total, n-minus-one division and 77.3 truncation fail. The specified tenths answers pass.
- MAD: IQR, half-range, total distance and the supplied n-minus-one divisors fail. The specified tenths pass.
- Pair and reason: always choosing Median and IQR fails Chicago. Wrong choices remain Sam fixed.
- Headline: picking before the IQR gate does nothing. A wrong headline cannot be replaced with the right one.
  A and C have matching wording and length with city order reversed; button positions shuffle on entry.
- Report: supplied fields never count as independently found. There is no saved best score.
- Found and fixed a reset exploit: Start over previously laundered help into found credit. Help history now lasts
  for this page session, disclosed beside Start over. `reset-cheat-result.json` confirms both supplied n and a
  fixed chip retain their help marks after reset and correct re-entry. Reload begins a new practice session.
- Found and fixed an engine boundary loss: a dot at the fixed upper endpoint disappeared from histogram counts.
  A chart-only endpoint adjustment now retains all thirty observations while canonical statistics stay exact.
- Large class inputs now use bounded histogram bin counts and scaled axis labels. The wide-range test retained
  three observations in twelve bins, with no console errors. See `edge-final-result.json` and `class-labels.log`.
- Accessible chart alternatives no longer supply an automatic observation count before the counting task;
  they retain the raw values. Dataset switches also refresh bin units and the contextual day/game/value hint.

#### Voice walk
Held clicks used 120 ms presses at a two-second pace. Chrome was muted. Speech used a deterministic timing stub
through the actual kit queue; this tests narration order and stale-line handling, not recording or voice quality.
The successful student path included a real whole-pixel, timing-jittered drag, Histogram, Build and Headline.
Main how lines heard: meanMoved, histo, wBuild, facts, lineUp, midEven, quart, ends, iqr, mean, mad, pick,
wHeadline and pickHead. Result lines preceded their following prompts; filed and headRight were heard.
The initial welcome was skipped by the first drag's own teaching line, permitted by BASELINE rule 16.
Chicago side path heard midOdd, selected its middle through keys, and used Read on the current hint.
How lines already heard stayed silent on repeats. The recorded path had zero tool console errors.
Found and fixed simultaneous IQR results replacing one another in the queue: event instances now have unique keys.
`headline-voice-fix.json` confirms both Right results are spoken before pickHead.
Evidence: `voice-walk.json`, `walk-retry.log`, `headline-voice-fix.json`, `targeted-fixes.log`.
news-reader/Rasalgethi is configured; no recordings were made, as instructed. Browser speech remains the fallback.

#### Feel check
Played the complete student path through actual held input. The best moment is dragging the hot day to 110,
seeing the rust marker travel while teal holds, then filing a report whose individual fields carry honest credit.
The two flattest moments were the static-looking distance calculation and a report that hid its last rows.
Added the distance-line drawing and an 850 ms running total; shortened report typesetting so all fourteen fields fit.
The targeted report fit check passed, and its frame was inspected. No celebration was added beyond the specified chime.
Later cases change parity, shape and the effect of an unusual game; Headline adds equal means with different spreads.
`feel-comparison.png` puts this tool beside Beat Lab. Both bar tools were bundled into Scratch copies and opened.
The newspaper art, material detail and restrained chart styling hold their own; the required compact grid is denser.

#### Done when
1. PASS: independent calculation, functional assertions and a real drag show +0.53 °F with median unchanged;
   crossing the middle changes median by 0.5. Put back restores data and removes changes.
2. PASS: shared fixed axes and engine data; supplied width-two counts pass. Histogram blocks dragging.
   Endpoint and wide custom-range counting fixes passed targeted browser assertions.
3. PASS: n and one-try facts tested on all three Build sets; no visible count or automatic accessible count supplied.
4. PASS: ten ordered columns, strict card positions, duplicate-value rejection, help after two misses and range boxes.
   The engine addition is implemented as a tool-local adapter because shared writes are forbidden.
5. PASS: correct means and MADs and the specified wrong strategies are covered by the functional assertions.
6. PASS: the three prescribed pair/reason combinations and wrong-pick locks were exercised.
7. PASS: the successful held-input path computed both IQRs and printed headline A with both spreads and ranges.
   Wrong-pick locking was tested; the other verdict strings and per-entry shuffling were checked in source.
8. FAIL, incomplete verification: final layouts are live immediately and synchronous paths can advance during
   animation, but the complete real-input mid-animation and resize matrix did not finish in the mechanical audit.
9. FAIL against the complete matrix: all required Explore sizes were viewed, all modes were played at 1366,
   Luka's seven-row compact grid fits 680x425, and phone Explore/Headline fit. Every Build step at every size
   was not verified. Individual compact visual cards also shrink below the spec's literal 64 by 44 dimensions.
10. PASS for the exercised paths: current hints, once-only how lines, ordered events, privacy text and offline assets.
    Main walk and targeted fixes had no tool console errors. The phone host alone requested a missing favicon.

#### Wave lessons
- Hint and voice: PASS on the held main/side paths and the repaired simultaneous-result check. Read used the current hint.
- Focus and layout: PASS on a complete keyboard-only Build, earning fourteen fields with zero mouse events.
  Nothing takes focus on load; deliberate focus transfers use preventScroll. The final report fits at 1366.
- Sizes: FAIL against the strict complete-state requirement. All Explore sizes are viewed; compact grid cards use
  one large selection surface but have smaller visual cells. Full audit coverage is outstanding.
- No giveaways: PASS for tested attempts, duplicate cards, one-pick gates and reset laundering; count alternatives sanitized.
- Honest numbers: PASS. Tiles explicitly report changes from original data; help credit survives reset; class scale is labeled.
- Standards: PASS for student actions covering counting, attribute/method/units, all three charts, center/spread and shape.
  Shared range-whisker API/documentation remain unchanged, explicitly recorded as wanted engine work.
- Motion off: PASS. The grayscale calm frame reports zero running infinite animations; all mark distinctions remain readable.
- Short choices: PASS in the exercised states. Facts rows appear sequentially with their complete choice sets.
- Resize mid-animation: FAIL, unverified after the audit transport failure; no timing lock is used in tool logic.
- Late welcome: PASS on the logged path; no welcomeAfter option. First-action welcome skipping remains permitted.
- Unknown stays unknown: PASS. Build hides the box summary until positional work supplies it.
- One meaning per style: PASS. Named rust/dashed/diamond Mean and teal/solid/square Median survive grayscale.
- Truthful badges and changing-back hints: PASS in reset, wrong-answer and set/mode transitions exercised.
- No copying clue wording: PASS against the prescribed source-card codes; TMAX is not expanded beside the answer chips.

#### Audit leads
Audit run once: `scripts/audit_tool.py box-plot-builder _scratch/box-plot-builder/audit --port 9977 --host-port 8775`.
It failed on its first size with a Chrome protocol TimeoutError and emitted no audit.md or actionable leads.
See `audit-run.log`. Eleven real-input audit states are supplied for cold review. The audit was not rerun.
Earlier drive failures and a smaller retry also show connection reset/refused errors. Later focused runs recovered
the evidence described above. These successful checks do not turn the unfinished mechanical audit into a pass.
Fixes after that failed attempt were checked narrowly, with syntax/static checks and the cited targeted frames.
The host's favicon 404 is outside the embedded tool; it is the only warning in the successful phone batch.

#### Frames looked at
All paths below are under `_scratch/box-plot-builder/`.
- `reference-frames/`: snowy-mail-route and beat-lab; `art-contact.png`, `people-contact.png`, `feel-comparison.png`.
- `initial-frames/`: explore-1366, drag-1366, build-1366 and headline-1366. Early dataset placeholders were replaced.
- `functional-frames/functional.png`; `grid-frames/` both Luka frames, including the pre-fix clipping failure.
- `real-drag.png`, `student-report.png`, `student-headline.png`; the report's pre-fix hidden rows were inspected.
- `compact-luka-fixed.png`, `report-fit-fixed.png`, `headline-voice-fixed.png`, `keyboard-only-report.png`.
- `phone-frames/`: phone-explore and phone-headline, through a 375x812 iframe host.
- `remaining-frames/`: Explore at 800, 1000, 1280, 1920 and 760 widths, plus calm-gray.
- `edge-final-frames/histogram-edges-fixed.png`, `class-labels-fixed/histogram-edges-fixed.png`,
  and `reset-cheat-frames/reset-cheat-blocked.png`. The original wide-input axis crowding was corrected.

#### Art made
Nine generated images, all final WebPs embedded. Binary art: 346606 bytes, 338.5 KiB.
Final bundle: 830060 bytes, 810.6 KiB. Recorded voice: 0 KB. Below the 2 MB goal.
Three Sam poses have people true and ref links. Fresh-agent representation review passed; evidence is in Scratch.
No redraws were necessary. Final-size assets and contact sheets were inspected. Prompts and raw originals are retained.
Credit is included in tool.draft.json and the HTML comment.

#### Art still to paint
None. The configured narrator still needs recordings in a later authorized voice-production step.

#### Engine changes wanted
See handoff.md: add optional range whiskers to Chart.drawBox and family docs; clamp engine drags; expose drag cancel;
include an exact fixed upper endpoint in the final histogram bin. This build changes no shared engine file.

#### Left open
- The mechanical audit and the full intermediate-state resize/mid-animation matrix remain incomplete.
- Compact visual cards cannot meet literal 64 by 44 dimensions in ten columns beside a panel at 680x425.
- Our class is a longer optional form and can require panel scrolling; full phone form/extreme combinations remain open.
- Actual narrator sound quality is unverified because no recordings were made; speech testing used timed browser stubs.
- Final small hint/bin-label and accessible-count changes were syntax/static checked rather than repeating the full walk.
All started drivers finished, the host was stopped, host.html was removed, and no assigned Chrome/host ports were listening.
No cold review or polish round was started. Build-only work stops here.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: box-plot-builder
#### Played
Cold Grade 6 solo play: real-dot drag, Histogram, all five San Diego Build steps and Headline before reading builder files. A strong newsroom with an earned result; later checked all three Build sets, keyboard-only completion and projector/phone views.
#### Findings fixed
- Blocker, general, Build: Start over erased first-miss counts, allowing unlimited guesses. Attempts now survive resets alongside help marks.
- Blocker, family:data-desk, Pick: pair feedback disclosed the next shape answer. Explanation now waits for the reason commitment.
- Blocker, family:data-desk, Our class: a trailing comma silently became zero. Empty separators are discarded; comma-only input is rejected.
- Should fix, general, voice: long obsolete how-to speech delayed or displaced the next step's instruction. Stale how-to speech now yields to actions; event speech retains its queue. Added the missing File how-to and contextual day/game/value welcomes.
- Should fix, family:data-desk, charts: nearby box labels collided, and tall dot stacks crossed headings. Spaced labels retain fine leaders to exact marks; local dot fitting respects the actual plotting frame. Keyboard point selection now refits the kit's finished redraw too.
- Should fix, general, layout: compact Put back was clipped, small header targets were under 44 px, class input crowded laptop controls, and phone MAD/Pick retained an unnecessary completed grid. Fixed these layouts without changing topics or the laptop palette.
- Should fix, general, focus: File hid its focused control and Headline rebuilt verdict buttons. Focus now enters the report; verdict buttons keep their identity.
- Should fix, general, state/voice: partial Headline checks addressed a now-readonly city, a histogram set switch could invite dragging, and dragging home left a movement hint. Added city-specific how-to lines and matching validity/reset guards; sports titles now use for rather than in a person.
- Blocker, general, repair check: kept Headline identity private rather than exposing a stable answer index in a DOM attribute.
- Polish, general: the report's flat lead only named measures, and the phone payoff showed a cropped title. It now prints actual selected statistics and uses the phone's available height.
- Polish, general: strengthened the headline's paper veil and replaced the weak Aa class-card graphic with a shaded notebook, pencil and tiny chart.
#### Findings left
- Nit, art: faint green edge residue on Sam's cutouts. Despill configured, but the permitted rekey environment was denied execution twice; original paintings retained.
- Spec conflict: literal 64 by 44 cards cannot fit ten columns beside a panel at 680x425. Retained ten columns, readable values and the large shared keyboard/pointer selection surface; no scope-changing layout feature added.
#### Break it
- n: empty, September 31, Luka 82 and repeated misses; two misses supply help. Reset after one miss now retains the first attempt, blocking unlimited guesses.
- Measured/how/units: wrong then correct and all-options sweeping remain Sam fixed. All three source-card contexts were checked.
- Median/quartiles: same-valued wrong positions, repeated taps and sweeping cards fail. Both even-middle cards are required; supplied fields do not earn found credit.
- Min/max: the actual endpoints are the intended skill; wrong positions consume attempts and retain help credit.
- IQR: range, Q3 and Check mashing fail; both city gates require their own exact IQRs. Supplied answers cannot be turned into found credit.
- Mean/MAD: rejected median, totals, truncated mean, n-minus-one quotients, IQR and half-range on all three sets. Accepted the specified tenths answers. Evidence: numbers-*.json and post-*.json in Scratch.
- Pair/reason: always Median/IQR fails Chicago; each reason differs. One pick locks the field; pair feedback no longer reveals the reason.
- Headline: premature selection is blocked; mean-only and reversed-city guesses get their own explanations; every option was held-clicked and a wrong-then-right sweep stays locked. Four options remain distinct and focus stays on the chosen option.
- Report: a full mashing route earns zero of 14; normal routes earn 14. No best-score meter or saved score exists. A real keyboard-only route also earned 14 with zero exceptions.
- Explore tiles are changes, not scores: real 94 to 110 drag gives mean +0.53 and median 0; crossing the middle gives +0.5 median, Put back restores all. Histogram retains the endpoint observation.
- Custom data: trailing comma now preserves exactly three observations. Sixty identical values stay inside the plot after local stack fitting; all 60 observations remain present. Real keyboard selection also keeps all dots fitted and its ring centered on the selected dot: ring-proof-fixed/fitted-selected-dot.png and ring-proof.json. Clear/privacy and the bounded class entry were inspected.
#### Voice walk
Actual browser speech through the unmodified kit queue, muted Chrome, 120 ms held clicks at a two-second action pace. Main path: drag, Histogram, bins, Dot plot, Put back, Build Facts/Box/Mean/MAD/Pick/File, Headline IQRs and headline.
Heard in order: meanMoved, histo, wBuild, facts, lineUp, midEven, quart, ends, iqr, mean, mad, pick, file, filed, wHeadline, pickHead, headRight, with Right results between the relevant prompts.
The first drag may skip the initial welcome. Obsolete how-to speech is cut when its action has happened; no earlier how-to carries into a later step. Several instructions start once and are cut before finishing at this pace; the log records those cuts. Mode changes hush speech as specified.

| Line group | Kind | Expected | Heard |
|---|---|---:|---:|
| Main how lines above | how | 1 each | 1 each |
| Right | event | 17 | 17 |
| Filed / headRight | event | 1 each | 1 each |
| Histogram, five taps on a fresh page | how | 1 | 1 |
| Chicago middle-card side path | how | 1 midOdd | 1 |

Read with Sound off spoke the current hint. Switching mode during Read released the queue; Sound on then spoke the correct mode welcome. The 29 fixed lines match voice/lines.json exactly. Final main-path rerun completed after all voice edits: voice-post-audit/headline-final.json. Class and Luka welcomes said value and game; partial Headline checks spoke denverOnly or miamiOnly, correctly naming only the editable city.
#### Facts checked
- All 123 daily temperature values checked directly against NOAA NCEI daily-summaries API, stations USW00023188, USW00094846, USW00012839, USW00003017, standard units, matching the spec. Saved as source-*.json in Scratch.
- Recomputed all five sets independently in recompute.py: every count, sum, five-number summary, IQR, mean and MAD matches.
- Quartile rule and IQR: Illustrative Mathematics Grade 6 Unit 8 Lesson 15, https://im.kendallhunt.com/MS/students/1/8/15/index.html.
- Whiskers to extrema: IM Lesson 16, https://im.kendallhunt.com/MS/students/1/8/16/index.html.
- MAD as average absolute distance: IM Lesson 11, https://im.kendallhunt.com/MS/students/1/8/11/index.html.
- Measure selection by shape and context: IM Lesson 18, https://im.kendallhunt.com/MS/students/1/8/18/index.html.
- TMAX definition: NOAA GHCN-Daily README, https://www.ncei.noaa.gov/pub/data/ghcn/daily/readme.txt.
- 73 points at Atlanta on January 26, 2024: NBA official box score, https://www.nba.com/game/dal-vs-atl-0022300634/box-score.
- All 70 regular-season point values and their dates match ESPN's first-party athlete game-log API, season 2024, excluding its All-Star row: https://site.web.api.espn.com/apis/common/v3/sports/basketball/nba/athletes/3945274/gamelog?season=2024. Saved source-espn.json; 82 minus 12 is 70.
- Dallas' 50 wins and 32 losses confirm 82 team games; combined with the 70 played games, this confirms 12 missed. Source: Dallas Mavericks official 2024-25 Media Guide, https://cdn.nba.com/teams/legacy/www.mavs.com/wp-content/uploads/2025/02/2024-25-Dallas-Mavericks-Media-Guide-2.pdf.
- Derived facts: San Diego sum 2321, mean 77.3667, MAD 5.3133, IQR 8; Chicago 2331, 75.1935, 5.6191, 11; Luka 2370, 33.8571, 6.3755, 10. Miami/Denver both total 2842, mean 91.6774; IQRs 1/9 and ranges 5/24. Source: independently recomputed frozen NOAA/ESPN values, recomputed.json.
- Standards 6.SP.B.4 and B.5a-d: https://www.thecorestandards.org/Math/Content/6/SP/.
#### Sensitivity
None for cultural curriculum: this is numerical weather/sports data. Checked all three fictional Sam portraits for consistent adult identity, friendly expression, plausible hands and stereotypes; no substantive concern. Every person asset is marked people:true. Luka is named with his accent and has no generated likeness.
#### Flattest moment left
Mean and MAD still involve consecutive quotient entries. This practice is within the spec; the moving distances and earned numerical report provide the payoff. No extra game or topic was added.
#### Graphics
Inspected all nine finished paintings at source and displayed sizes: three Sam poses, the newsroom desk, four cities and basketball. Preserved the cohesive editorial paintings, material details, light direction, newsprint and teal/rust distinctions. Improved the class notebook drawing, text-on-art contrast and chart label drawing. No missing art tokens or placeholders. Bundle 839273 bytes (819.6 KiB), art 338.5 KiB; below 2 MB.
#### Audit
Audit not finished. Ran once, bounded to 40 minutes, on Chrome 9951 and host 8755. Chrome disconnected with WinError 64 during later Build states, after box-help-path. Saved 71 frames and 14 leads in _scratch/box-plot-builder/review-audit/audit.md; did not rerun.
- Confirmed class-entry clipping at 680x425. Compacted the unit/Show/Clear row at landscape widths; focused final frame places both buttons' bottoms at 375 px and the full entry region at 420 px in the 425 px viewport. Laptop artwork, controls and Put back remain visible.
- Input-name leads are false positives: visible labels are associated by for/id; the helper ignores those associations. The 1 Facts warnings describe an ordinal step heading, not a mismatched observation count.
- Moved-dot overlap leads involve a transparent chart input surface over its readable start text, not colliding painted labels. Facts-chip clipping names the secondary Start over control; all four current answer choices are visible.
- Phone iframe inspection failed; direct same-origin phone frames and Read checks cover the actual tool. Later state, calm, resize and walk sections were not reached; placeholder clean headings are not passes.
- Final narrow rechecks cover the repaired class form, fitted dots, four private verdict choices/focus, rapid card tap, drag-back hint, contextual speech, phone report and all-state score exploits. Final source syntax, exact 29-line inventory, frozen source arrays and inline asset checks passed.
#### Left open
Unattended: take the spec's defaults; no questions requested.
- No shared engine/doc edits or git actions. Range-whisker, clamp and endpoint workarounds remain tool-local, with engine requests in handoff.md.
- Chrome transport failures interrupted the full sports-grid matrix even on its smaller retry. Successful targeted checks do not turn missing combinations into passes.
- Optional class entry can require panel scrolling in the shortest previews/phones. Its laptop controls fit and its input row is compact at every landscape size. Showing the entire editor, six 44 px set choices, graph switches and Put back simultaneously in a 425 px preview would need a disclosure flow beyond the specified persistent panel, or smaller targets; left open rather than adding that feature.
- Narration recordings remain absent; this review checked browser speech behavior, not a recorded news-reader performance.
- Browser/test runs were bounded, including the 40-minute audit. Initial short read commands lacked explicit deadlines; subsequent commands used the bounded wrapper. Browser and host ports stayed within the assigned range. No git commits or shared-file writes; evidence and working report drafts stayed in this tool's Scratch folder.
- Cleanup: Chrome ports 9950 through 9957 are closed, and the generated host.html is absent. Port 8755 still serves this tool folder; process ownership inspection was denied and netstat supplied no listener PID, so the unidentified listener was left untouched.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Box Plot Builder handoff

#### Structure
`src.html` starts from the kit starter. CSS builds a newspaper working desk. The inline datasets, line table, state,
range-box adapter, Explore rendering, Build state machine, Headline state and event wiring follow in that order.
The shared kit handles sound, motion and narration. DataTable and Chart handle statistics, dots, histograms and boxes.
Each Build set keeps its own session progress. Only Our class is saved, under `curio-bpb-class`, inside try/catch.
Help history also stays in memory for this page session. Start over resets the build but preserves marks for fields
Sam supplied, so a reset cannot turn copied answers into independently found credit. The button says this on screen.
Cold review also preserves attempt counts across Start over, preventing unlimited first guesses before help is marked.

#### Cold review changes
- Pair feedback waits until the shape reason is committed before explaining the shape. The reason can no longer be copied from the preceding feedback.
- Class number parsing ignores empty comma/space separators rather than turning a trailing comma into a zero.
- Active how-to speech gives way when its step has passed. Results remain whole, and the final File control has its own once-only how-to line.
- Filed reports lead with the actual selected center and spread; focus enters the report for keyboard reading.
- Box labels have separated text positions with fine leaders to their exact marks. Headline text has a stronger paper veil.
- The Our class card now has a shaded notebook and pencil drawing. Existing paintings and the editorial palette are retained.
- Headline buttons retain their DOM identity when the verdict arrives, preserving focus.
- Short previews place the four change tiles on the newspaper margin, keeping Put back and histogram bins in view.
- Long grids get a shorter heading at laptop heights. Dot stacks are fitted locally to their real plotting frame so they cannot draw across the title.
- At phone widths, MAD and Pick give their space to the current graph and controls instead of retaining the completed card grid. The class entry form is compact on laptops.
- A filed phone report uses the remaining screen height, so its lead and earned fields replace the tiny cropped title view.
- Explore welcomes use day, game or value and wait until a draggable dot view is present. A partial Headline check names only the city still editable. Fixed lines are kept exactly in voice/lines.json.
- Dragging back to the original values restores the generic hint and hushes stale movement teaching. Selection rings follow the fitted dot positions too.
- Keyboard point selection refits the finished chart redraw, keeping all 60 equal class values and their selection ring inside the plot.
- The Headline DOM exposes shuffled position only, with no stable option-answer index; button identity is kept privately through each verdict.
- Audit states retain their real click paths; repeated number-spinner presses are represented by input entry events for a bounded audit.
- Reporter edge despill is configured, but the permitted rekey pipeline could not run: its Python environment was denied execution. Original paintings are retained.

#### Decisions and contradictions
- There are no open spec questions. Kept Luka Dončić and the intended school range-whisker convention.
- The spec approves editing `kit/data-desk.js` and its family doc. The user permits writes only in this tool and
  its scratch folder. A local adapter keeps the engine's quartile box and axis and replaces whisker endpoints.
- The brief says to create the report early and stop when it is written. The user's explicit stop condition wins:
  working evidence is kept in Scratch and the complete report is written last.
- CODEX-BUILD requires generated art while BUILD says do not draw. Followed CODEX-BUILD and the user's image request.
- Numeric card sizes of 64 by 44 cannot fit ten columns in a 680-wide view with a 60 percent stage. The grid retains
  ten columns and has one keyboard/pointer selection surface; compact visual cards shrink while text stays readable.
- Facts chip rows appear in sequence so each complete choice set fits without hiding options in a scroll panel.
  Completed rows remain recorded in the final report. This is a layout choice within the ordered Facts step.
- Headline's prohibition on statistic readouts is applied before the editorial decision; the prescribed draft and
  earned final headline necessarily contain their supplied mean, IQRs and ranges.
- Source card uses `TMAX`, as the anti-copy requirement asks, rather than spelling out maximum temperature beside it.
- The configured voice is news-reader/Rasalgethi. No recording is authorized; browser speech is the build fallback.
- Our class uses at most 24 histogram bins, with widths derived from its padded axis. This prevents a wide input
  range from generating millions of bars. Input magnitudes are bounded at one million for this classroom tool.
- Histograms include an exact fixed right endpoint in the final bin. The canonical data table stays exact; a
  chart-only copy nudges that endpoint just inside the last interval for the current engine's bin calculation.
- The plot's accessible alternative retains the raw values but removes the engine's precomputed observation count.
  This keeps the Facts counting task from being answered by reading an automatic count.

#### Engine changes wanted
- `kit/data-desk.js`, `Chart.drawBox`: add `whiskers: 'range'`, choosing min/max and omitting outlier marks only when
  requested. Keep default 1.5-IQR behavior. Document in `docs/families/data-desk.md`.
- `Chart.startDrag` and `keyPoint`: clamp snapped edits to the fixed axis domain. This tool wraps DataTable.set.
- Expose a drag-cancel method. This tool dispatches pointercancel on reset, set switch, mode switch and resize.
- `Chart.histBins`: include a value equal to the fixed domain maximum in the last bin. Default half-open bin
  arithmetic currently drops it. This tool uses a chart-only endpoint adjustment while keeping true statistics.

#### Sensitivity
Sam is a fictional young adult reporter. All three portraits have `people: true`. Review hands, consistent identity,
friendly expression and respectful representation on the Scratch people contact sheet. No cultural or body curriculum.
Luka is named as the real data subject; no portrait or likeness is generated.
Fresh-agent representation check completed: consistent youthful adult identity, plausible hands, friendly expressions,
no stereotypes or child-facing concerns. The contact sheet remains for the owner's review.

#### Build boundary
No git commits, branch actions, shared-file changes, publishing or polish round. All test evidence is in
`_scratch/box-plot-builder/`. The report records remaining limitations and exact checks.

#### Verification left open
The builder's audit failed before collecting leads. The single cold-review audit later collected 14 leads and
71 frames, then stopped during later Build states with a Chrome connection reset (WinError 64). Its partial
audit.md is in Scratch/review-audit. Class-form clipping was confirmed and repaired; focused frames show
Show/Clear within 680x425 and the full laptop controls within 1366x768. The other leads were checked against
real label associations, ordinal headings, the transparent chart input layer and actual visible choices.
Direct review checks cover the required Explore and Headline sizes, keyboard-only completion, phone frames,
Motion off, grayscale, score cheats, data recomputation and real browser speech. The sports-grid size matrix
was interrupted even on its smaller retry. The audit's later states, calm, resize and walk stages did not run;
their placeholder headings are not passes. No second audit was run.
The compact card grid uses a single large selection surface; its individual visual cards are smaller than 44 px.
Our class has a longer entry form and may require panel scrolling. Browser speech is a timing-tested fallback;
the configured news-reader recordings have not been produced or heard.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-07)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-07)
- 2026-11-25: handoff.md folded in (last changed 2026-11-07)
