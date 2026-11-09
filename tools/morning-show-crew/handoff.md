# Morning Show Crew build handoff

## Structure

The starter's kit imports, metadata and accessibility frame are retained. Tool CSS lays out three modes at real pixel sizes. The main script holds content tables, state, Curio.voice, validity and media renderers, the deterministic schedule and reach model, then static controls and event handlers. Interactive controls are created once; updates change their content and state without replacing them.

`schedule()` computes four daily production records from the plan. `runDay()` commits a snapshot including version validity and content. `results()` uses only committed snapshots. Undo pops one snapshot. This prevents later Make edits from repairing earlier meetings and prevents repeat run taps from inflating reach.

Board cells buy or cancel directly. Full layouts have separate Spanish announcement, Spanish poster, Spanish site and captions rows. The first poster cell buys design; after an earlier day has design, a later cell buys one copy or cancels that day's copies. The desk adjusts quantities and also exposes secondary jobs in compact layouts. Existing published posts/copies persist, so cancel their original unrun purchase to remove them from a plan.

During a day the map shows the new symbolic meetings, while audience numbers retain the previous day until the four-second reveal. Undo and mode changes remain immediate. Repeated taps on the active tab preserve its instruction; navigation from inside a mode focuses the destination header with preventScroll.

## Spec decisions and contradictions

- No open-question section exists. Use the stated facts, house palette and lively-host bank metadata.
- The user requires the image tool; this supersedes the spec's local-FLUX method. All ten required paintings were generated with OpenAI gpt-image and marked people false. No people were needed by these empty-school shots.
- The brief prohibits recording audio. Spanish speaker approval and a recorded Spanish script cannot be supplied unattended. Keep the model job, show the provisional fixed script, and mark the required recording as open. Browser speech previews the variable English script. Fixed lines also use the kit fallback until recordings exist.
- The balanced reference's quoted English-learning share includes Spanish announcements all four days, though its prose omits that job. Including it makes the plan exactly twelve hours. The reference without it gives 48%, not 80%, in that group.
- Reference totals differ by rounding convention. Use per-group rounding and report computed numbers. Do not alter spec.md.
- The family share is not capped at 40%. A legal twelve-hour plan reaches about 45%: Mon poster design and site; Tue Spanish site and eight copies; Wed Spanish poster and eight copies; Thu twelve copies. The spec's statement describes only plans its author tried.
- The source calls all 985 audience units people, although 400 are households. UI and notes distinguish units and exclude households and teachers from auditions.
- A visual shot is allowed to carry its named fact, as the spec leans toward. Wrong text overrides it. This shorthand is explained in notes.
- The multi-day edit uses spare quarter-hour blocks and reserves its finishing half-hour for the first airing. Completed videos need half an hour per further airing, and a day can be paused. This resolves the unspecified allocation order without borrowing hours.
- Small landscape previews and compact phones collapse Spanish/caption subrows into cell annotations and the selected medium's job inspector. Full boards retain the subrows. Main four-media board and Run/Undo remain visible.
- Motion off makes this spec's day animation immediate, overriding the general pacing guidance for that four-second map only. Segment timing stays fourteen seconds.
- Try the week again clears run history while keeping the week plan and all versions, allowing direct revision.
- The user's stop condition takes priority over the brief's instruction to start the final report early. The final report is written only after checks, then work stops.

## Sensitivity

Language access appears in a fictional model. Review the Spanish draft for natural school wording, the exact Thursday deadline, and equivalence to the four English facts. Check that model rates are never read as measured traits of Spanish speakers or language learners. Student categories are disjoint for the model; they do not describe the complexity of real students' identities. No cultural tradition, bodies, religion or hard history is taught.

## Engine changes wanted

None needed for this implementation. The shared kit's fallback cannot reproduce the lively-host recording identity, and Curio.say does not select a language for mixed-language scripts. Approved Spanish audio should be supplied as a fixed clip before release.

## Next work

Cold review evidence is in codex-review.md. Resolve the Spanish recording and speaker check before release. Do not infer release approval from the build or browser-fallback queue checks.

## Cold review changes

The 2026-11-06 cold review retained the painted set and all production/reach rules. It corrected Friday's noOne trigger to test zero heard meetings, rather than zero got-it share. The fixed line now names a whole unreached group. The result board repeats the two-complete-meeting assumption and distinguishes it from measured understanding.

Clock and sign-up overlays use the same cover crop as their images; the clock now includes Friday, and the sheet names the outside-room location and Thursday deadline. Reset stops both playback paths before its dialog. Phone layouts keep the current controls and actions in view; compact week translations/captions remain on the selected desk. The weakest drawing, the audience map, now distinguishes the five contexts and shows dispatch paths. Daily audience counts include the gain in got-it recipients.

Completed board cells use their frozen published validity for warning badges. Editing later versions cannot repaint that history. Same-step fact edits and week purchases preserve a playing, still-relevant how-to line through `keepInstruction`; stale event speech is still stopped. Mode changes, Reset, Read and playback retain their explicit stop behavior.

Audit-frame inspection also found clipping in the 680x425 poster choices, short announcement and Friday attendance explanation. Compact line spacing and redundant fact-category labels were adjusted locally. The transport column now keeps its width when Play becomes Stop. Completing a day clears its pending timer, including when Motion is switched off mid-run. Spanish draft text has lang=es with its English status label marked separately.

The audit snapshot predates these final compact CSS, transport, language-markup and timer corrections. Targeted preview frames and old/new Motion checks verify them without a second full audit; the main voice route is rechecked after the timer correction.

Spanish speaker approval and fixed recording remain a release blocker under the no-recording constraint. No claim of completed audio review is made. See codex-review.md for independent evidence, exact remaining limits and audit disposition.

## Validation pointers

`_scratch/morning-show-crew/validation-summary.json` records 523 model assertions, 21 live-path assertions over 67 real actions, 45 final checks, exact sizes and SHA-256 hashes. `week-final/` covers the final direct-purchase board at all seven desktop/preview sizes and all eight job rows. `audit-followup/` and `audit-voice-followup/` prove the targeted fixes. The single completed audit has 66 leads against an earlier snapshot; the report disposes of each category and retains the phone scrolling exception. No second full audit was run.

## Build scope exception

The reference bar check accidentally regenerated the ignored `tools/snowy-mail-route/snowy-mail-route.html` using the bundler. That was outside the user's write boundary. No reference source was edited, and no git operation was performed. All other created files are inside this tool and its Scratch directory.
