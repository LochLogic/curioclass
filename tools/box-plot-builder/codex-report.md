# Codex report: box-plot-builder

## Built
Three offline newsroom modes: Explore, Build and Headline. Nine original generated paintings, precise engine charts,
strict positional card work, bounded attempts, separate Build progress per set, and an earned fourteen-field report.
Files include readable src.html, bundled HTML, tool.draft.json with stage built, notes, handoff, preview.svg,
voice/lines.json, art/prompts.json, nine finished WebPs and eleven audit states.
All work used S:\CurioClass-codex. Authored files stayed inside the tool and its Scratch folder.
Chrome ports used: 9970 through 9977. Host: 8775. No commits, deployment or polish round.
The complete report was written last to honor the user's explicit report-and-stop condition.

## Numbers check
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

## Facts checked
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

## Break it
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

## Voice walk
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

## Feel check
Played the complete student path through actual held input. The best moment is dragging the hot day to 110,
seeing the rust marker travel while teal holds, then filing a report whose individual fields carry honest credit.
The two flattest moments were the static-looking distance calculation and a report that hid its last rows.
Added the distance-line drawing and an 850 ms running total; shortened report typesetting so all fourteen fields fit.
The targeted report fit check passed, and its frame was inspected. No celebration was added beyond the specified chime.
Later cases change parity, shape and the effect of an unusual game; Headline adds equal means with different spreads.
`feel-comparison.png` puts this tool beside Beat Lab. Both bar tools were bundled into Scratch copies and opened.
The newspaper art, material detail and restrained chart styling hold their own; the required compact grid is denser.

## Done when
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

## Wave lessons
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

## Audit leads
Audit run once: `scripts/audit_tool.py box-plot-builder _scratch/box-plot-builder/audit --port 9977 --host-port 8775`.
It failed on its first size with a Chrome protocol TimeoutError and emitted no audit.md or actionable leads.
See `audit-run.log`. Eleven real-input audit states are supplied for cold review. The audit was not rerun.
Earlier drive failures and a smaller retry also show connection reset/refused errors. Later focused runs recovered
the evidence described above. These successful checks do not turn the unfinished mechanical audit into a pass.
Fixes after that failed attempt were checked narrowly, with syntax/static checks and the cited targeted frames.
The host's favicon 404 is outside the embedded tool; it is the only warning in the successful phone batch.

## Frames looked at
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

## Art made
Nine generated images, all final WebPs embedded. Binary art: 346606 bytes, 338.5 KiB.
Final bundle: 830060 bytes, 810.6 KiB. Recorded voice: 0 KB. Below the 2 MB goal.
Three Sam poses have people true and ref links. Fresh-agent representation review passed; evidence is in Scratch.
No redraws were necessary. Final-size assets and contact sheets were inspected. Prompts and raw originals are retained.
Credit is included in tool.draft.json and the HTML comment.

## Art still to paint
None. The configured narrator still needs recordings in a later authorized voice-production step.

## Engine changes wanted
See handoff.md: add optional range whiskers to Chart.drawBox and family docs; clamp engine drags; expose drag cancel;
include an exact fixed upper endpoint in the final histogram bin. This build changes no shared engine file.

## Left open
- The mechanical audit and the full intermediate-state resize/mid-animation matrix remain incomplete.
- Compact visual cards cannot meet literal 64 by 44 dimensions in ten columns beside a panel at 680x425.
- Our class is a longer optional form and can require panel scrolling; full phone form/extreme combinations remain open.
- Actual narrator sound quality is unverified because no recordings were made; speech testing used timed browser stubs.
- Final small hint/bin-label and accessible-count changes were syntax/static checked rather than repeating the full walk.
All started drivers finished, the host was stopped, host.html was removed, and no assigned Chrome/host ports were listening.
No cold review or polish round was started. Build-only work stops here.
