# Illusion Lab: build handoff

## Structure
`src.html` starts from the shared starter and uses kit:curio plus kit:theme-912. The tool owns the rail, responsive workbench,
six station state machines, exact canvas stimuli, original picture pairs, result charts, Why cards and Notebook.
Search for renderLines, renderShadow, renderEye, renderChange, renderCount, renderWords and renderCompare.
Curio.voice owns narration. `state.measuring` hushes speech and disables Read. No recorded audio is included.
The visual pathway and charts use code because their values and moving parts must remain exact.

## State and timing
`illusion-lab-v1` stores only first and latest complete runs plus run counts, with try/catch. Unfinished work is discarded on a rail change.
Line and shadow movement gates count total distance moved; endpoint submissions are refused or replayed.
Count Backward uses real elapsed time and actual counting responses. Word Lists preserve the specified visual presentation timings.
Leaving the page during a timed memory run starts a fresh run, avoiding background-tab timing distortion.
All fourteen change frames are composed and loaded before Start. A scene's gray blank is computed from its base image.
Change input supports mouse location or a keyboard crosshair. Repeated completed scene sets are practice and not saved.
An actual alternation is required before a find can count. A premature correct-location guess is a miss and resumes the scene.
This closes a build-test shortcut that could otherwise save a correct find from only one picture.

## Open questions and choices
- Sensitivity: retain the spec's open disagreement on cultural explanations, with a fresh review before any release. No society is named or ranked.
- Eyewitness: retain the historical 1989 to 2020 denominator. Do not silently substitute current exoneration totals.
- Source correction: the original Loftus and Palmer paper separates the speed estimates (experiment 1) from the later glass reports
  (experiment 2, different participants). The card now explicitly distinguishes those experiments instead of implying one continuous group.
- Contradiction: “Do-step controls never show numbers” conflicts with counting choices, trial progress, inhibition values and receptor counts.
  Retained the numeric task content required by those stations. Line and swatch values remain hidden until Compare.
- Contradiction: “lures named only in Compare” conflicts with showing the lure as an ordinary recognition-test word.
  The theme is hidden before the lists; the recognition lure is shown as an unmarked test item and identified only in Compare.
- Contradiction: the source's “720 ms cycle” is the image-plus-blank half-cycle. Full A/blank/B/blank cycle is 1,440 ms.
  Implemented 560 ms image plus 160 ms blank per alternation, approximately 1.389 blanks per second.
- Numeric discrepancy: absolute four-percent hit-box padding produces 1.68% to 8.40% frame areas before moved-position unions,
  rather than 0.8% to 6.2%. Kept the explicitly specified geometry and documented computed random-hit odds in Scratch.
- Voice instruction windows: task entry, a paused kind choice and inter-trial prompts are outside active measurements.
  Read is unavailable during active adjustment, flicker, word presentation and counting. No-gap Start waits for its instruction.
- STANDARDS takes precedence over the exact llHow, ssHow, ssB and scHow wording: entry lines now name only currently enabled controls.
  Lock instructions appear after sufficient movement; Spotted it appears in the running hint. This avoids telling a student to use a disabled control.
- Notebook uses the specified table; the cold review moved Go into the station cell after confirming the pinned column covered results. Its nbHow line now explains horizontal scrolling. Unfinished stations
  show no comparison answer. On short screens the navigation rail uses two columns so every station remains available at 44 pixels.
- The no-gap instruction has both a minimum reading window and a voice-queue guard. Muting or pressing Read cannot shorten that window.
- The brief's write boundary prevents rebundling the two bar tools. Opened their existing bundles without changing their folders.
- The brief's stop-on-report rule takes precedence over the guide's request to start a report early. The report is written after all checks.
- Art uses the user-requested image tool rather than older Gemini-specific art wording. All assets depict no people.
- The first bench and classroom candidates introduced unrelated bust/inkblot material. Both were redrawn or edited before use.
- The final classroom painting placed its narrow shelf at y 0.35. The plant is drawn four percent lower, still entirely inside
  the spec's original hit box plus its four-percent padding. The hit box itself stays unchanged. The living-room window was repainted
  as bare plaster so the moving frame hangs on a wall. These keep the object placements physically plausible.

## Sensitivity
Cross-cultural perception research and wrongful convictions need fresh review. Check the culture card for treating the 1960s hypothesis
as a disputed explanation rather than a societal ranking. Check Eyewitness for humane wording and historical-denominator clarity.
The tool depicts an anatomical eye and teaches sensory cells. No individual is assigned a body, intelligence or personality label.
The Eyewitness closing question is conditional because not every student reports a false word. No personal account is requested.

## Engine changes wanted
None required. Future recorded calm-professor clips would make the named voice consistent across browsers, but recording was prohibited in this build.

## Scope
Build only. No commits, shared engine edits, publication or polish round. Validation artifacts, scripts, profiles and contact sheets live in
`_scratch/illusion-lab/`. The generated `illusion-lab.html` is the single offline deliverable; edit `src.html`, then bundle again.
The full audit ran once. Its frozen host bundle predates the repairs; `post-audit/checks.json` records 120 final targeted assertions.

## Cold review changes, 2026-11-07
Manual Flip now shares the 720 ms minimum cycle with automatic flicker; rapid clicks cannot create fast blank flashes.
Wrong-kind retries still resume the scene and use the specified three-miss limit. They are recorded as corrections,
excluded from uncued-find averages. Earlier records with misses and no kind history are shown as earlier-method finds,
excluded conservatively without changing their stored first/latest numbers.
Eye prompts concern neighboring output contrast, not absolute input-to-output change. eyeGuide names the next enabled
action after every model change. Seven distinct code symbols and shaded pathway cards lift the diagram without adding anatomy.
Compact line, shadow, recall and word-reference charts reflow at actual pixel size rather than hiding their final points off screen.
Count first/digit dots use numbered markers and a separate legend. Shadow Compare leads directly to Bridge.
New how-to lines cover recall, the next counting trial, the second list and familiarity tags. State transitions hush stale speech.
Word recall names the unshown theme specifically; Eyewitness states what was typed without inferring how it felt.
The primary Loftus and Palmer table gives 40.8 mph, corrected in notes; the public rounded figure remains about 40 mph.
The buoy was edited with the built-in image generator, preserving its painted metal while removing attached water.
Raw prompt, original copy, rekeyed asset and final scene evidence are in this tool and its Scratch folder. No audio was recorded.
Unattended choice: preserve all six stations, original timings, exact stimuli and the three-miss learning loop. Measurement
validity labels clarify corrected observations; they add no score, topic or mode. No shared kit change is needed.
READ_HINTS contains the fixed live hints used by Read; Curio.voice receives those alongside the event/how table.
allLines and voice/lines.json now agree on 57 strings. The first familiarity-tag how-to interrupts the earlier test how-to.
The Peterson explanation now avoids attributing a decay conclusion to a paper that fitted a fluctuation model;
Keppel's near-perfect first-trial claim is qualified as the stronger-learning experiment. Sources and note links were checked anew.

Cold audit follow-up: Notebook Go buttons share each station cell, so they cannot cover first/latest/comparison text.
The failed no-gap result says Not found, rather than reporting a misleading zero-alternation speed. Corrected and legacy
no-gap results carry the same validity labels as Compare. The existing first/latest payloads remain intact.
Why and Compare restore focus to their active tab if the initiating button was removed.
Bridge off hushes and names its actual state; reveal trial and pressed toggles survive a Why/Compare return.
Live manual and Motion-off changes name Flip immediately. Completing a kind choice hushes its obsolete instruction.
Cold review audit ran once with the requested 2400-second limit. It did not finish the resize-stress phase.
Its 52 saved leads comprise 18 intentional reset-dialog occlusions, 16 spec-required skipped welcomes,
17 instances of the Notebook pinned-column defect and one Why focus-loss defect. Both confirmed defects are repaired.
Windows taskkill denied the watchdog's process-tree cleanup; the audit Chrome was closed through CDP and the identified
audit Python process was stopped directly. Host and browser ports were then verified closed. No second audit was launched.
Final native repair walks and scoring checks use a scratch bundle byte-identical to the delivered bundle; Notebook,
focus-return and percentage-axis checks use the delivered bundle. Wide counting charts now include 0/50/100 percentage ticks.
