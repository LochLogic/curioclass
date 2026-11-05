# Codex report: music-history-radio

## Built

Build only: an offline radio with Dial, Mixing desk and six-round Mystery station modes, all eight bars of
The Traveler, twelve arrangements, true-time strip, feature rows, simplified notation, static and a tuning eye.
The owner-added station is Javanese gamelan, anchored to a documented 1889 encounter rather than an origin date.
Its sourced facts, parallel-tradition framing and simplified tuning are explained in notes.md and handoff.md.
Only this tool and its Scratch folder were written. No git commit, branch change, deployment or polish round.

## Numbers check

- Scratch numbers.json recomputes the supplied arithmetic: eight four-beat bars, 24 notes, all sixteen
  beat-one / beat-three pitches are chord tones. Organum totals 42 beats, or fourteen 3/4 bars.
- Signal is 1 at a mark, .7 at the 15 percent lock edge, and 0 at a midpoint. Browser boundary checks passed.
- Swing: 13.6 s; disco: 17 s; hip hop: 22.1739 s. All twelve compiled loops are under 30 s.
- Chant's supplied 9.6 to 23.6 s pre-gap range is inconsistent with 24 notes at .4 to .9 s, which gives
  9.6 to 21.6 s. This deterministic arrangement is 17.46 s including its gap. The spec was left unchanged.
- 11 cubed is 1,331; the owner's twelfth station makes 12 cubed, 1,728 combinations.
- Nine years spans 2.25 px at 300 px and 6.75 px at 900 px on an 800-2000 strip.
- Contrast: brand / background 9.04, brand / panel 8.06, ink / panel 13.04, muted / panel 6.71,
  dial text / cream 12.03, needle / cream 4.97. Spec ink 14.62 uses background rather than panel.

## Feel check

Best moment: the sealed mystery becomes a specific station, the two giveaway rows light up and the year gap
appears beside Next station. Compare preserves the bar position while the arrangement changes.
Flattest moment 1: the first compact layout crowded the knob and Station controls; a measured radio fit,
short landscape header and internally scrolling dial repaired it.
Flattest moment 2: the mystery result initially sat below the compact panel fold; the gap and final count now
also sit beside the primary action. Six real held-click rounds completed, with six distinct stations.
The side-by-side Scratch feel-comparison.jpg puts the radio beside Beat Lab. The radio has richer painted
materials and scene depth; it does not look plainer. Snowy Mail Route was also bundled into Scratch and viewed.
The student-path run was muted. Historical timbre and musical satisfaction have not been verified by ear.

## Done when

1. FAIL for the full by-ear criterion: all twelve plans preserve the 24-note contour across eight bars,
   including hip hop; every sound recipe reached the live audio graph without exceptions. No by-ear check occurred.
2. PASS: scripted .15 / .151 / .5 gap checks verify lock and strength; real jittered knob drag changed both.
3. PASS with limitation: A disables Flip until B locks; queued Flip applied at a bar without resetting its
   position. The 150 ms scheduling window can defer a very late request by one extra bar.
4. PASS for scripted plan coverage: all 1,728 mixes and 232,380 events compiled with finite pitches, times,
   durations and gains. Every sound recipe was smoke-tested live; this is not exhaustive listening to every mix.
5. PASS: six distinct rounds, absolute gaps, two highlighted rows, final count and New set; no set storage.
6. PASS for visual focus: the radio dominates the painted stage in both modes; the mystery strip spans it.
   The 680 px scene uses compact controls and hides the postcard.
7. PASS for live controls and pause; queued desk choices update the panel immediately. Strict next-bar
   timing has the scheduling-window limitation described under item 3.
8. PASS for queue / once behavior: twelve idents started once at a held-click two-second pace; repeat visits
   were silent with reason heard, and the queue emptied. Read interruption recovered. Music ducks during speech.
   How lines are deferred while music plays; Read remains available. Narration uses browser fallback.
9. PASS for primary layout: every named viewport checked; radio, strip and panel fit on both main laptop sizes,
   and 375 px page width equals scroll width. Secondary panel text / notation can require scrolling at small sizes.
10. PASS: fifteen paintings load, including the added postcard. All reviewed; no people or fake lettering remain.

## Wave lessons

- Hint / voice: PASS, hints update synchronously; kit validity / scope guard speech. Two-second held-click
  idents all start once. Stale idents are intentionally cut when their station changes.
- Focus / layout: PASS, controls are built once. Keyboard-only Power, Compare, station change and Flip retained focus.
- Sizes / targets: PASS after targeted repairs: tested buttons are at least 44 px; no small buttons in final checks. Main controls fit; the needle hit area extends to 44 px at compact sizes.
- No giveaways: PASS, Mystery conceals ident, active year pin, dial, postcard and notation; only generic prompts remain.
- Honest numbers: PASS, the dial labels its equal spacing; the true-time strip is to scale; 1889 says encounter.
- Standards: PASS, solo listening comparison / prediction practices MU:Re7; feature contexts and date reveals practice MU:Cn11.
- Motion off: PASS, the completed smaller audit reports no infinite animation. The visual glow animation is disabled; musical time does not change.
- Short choice sets visible: PASS, primary controls stay in view; era knobs each expose one selected value with arrow-key access.
- Resize mid-animation: PASS, the smaller audit reports no exceptions or stuck controls. The measured fit reads the existing state without rebuilding controls.
- Delayed welcome: PASS, welcomeAfter is not used; the Power tap's ident supersedes a welcome.
- Unknown stays unknown: PASS, Mystery has a sealed postcard, neutral prompts and no active year marker.
- One look / one meaning: PASS, tuning eye shape plus explicit lock text distinguish a lock from static, including grayscale.
- Badge truth: PASS, next-bar status is separate from the audible setting; the mixed dial follows Sound.
- Hint restores: PASS, tune / reveal / next / mode render their action hints synchronously.
- No copying an answer: PASS, the hidden listening mode offers a year estimate, with no era names in clues before reveal.

## Audit leads

The first attempt stopped after 40 frames because audit-states.json used the driver's unsupported End key.
The state now uses ArrowRight. One smaller retry with --no-walk completed: audit-retry/audit.md, 65 frames,
107 leads. Motion off and resize recovery were clean. The full automatic control-walk remains uncompleted.

Every listed lead is covered by these dispositions, grouped by the common cause and selectors:

- Both small-target Dial tab leads: fixed with a 44 px minimum width. Final compact checks found no small buttons.
- All under-10-px leads for strip-title, time ends, air, playhead, station-number, TUNING, VOLUME, footer-note,
  key-help, changed, UNIDENTIFIED BROADCAST, ah and SAMPLE / KICK / SNARE: raised to at least 10 px.
  Main feature sentences and buttons remain at least 11 px in the compact preview.
- All guess / strip-title / time-year / year-label overlap leads: fixed by giving the 44 px pin input its own
  strip area, with separate caption and end-label space. Final input and strip bounds match exactly.
- All phone feature-label / paragraph / changed versus hint overlap leads: fixed by scrolling main above a
  separate footer row. Final phone main ends at y=754 and footer starts at y=754, in all three modes.

Additional core repairs restore the station dial when Mystery reveals, hide covered controls from focus,
fix the no-Power reveal hint, preserve the power lamp while paused, and support Space from a slider.
Only affected screens were rechecked after these changes. The full audit was not rerun.
The audit host emitted a connection-reset traceback when a browser connection closed; its completed report
has no page runtime / resize exception leads. The final held-click / phone / keyboard batches had zero browser errors.

## Frames looked at

First frames: Dial, desk and compact preview. Functional frames: both compact modes, full set, mystery start,
sound-graph checks and two-second voice run. Size frames: 680x425, 800x500, 1000x625, 1280x720, 1366x768,
1920x1080, 760x900, hosted 375x812, grayscale, Motion off, keyboard path and a real jittered knob drag.
Targeted frames include the final laptop panels, added station, compact reveal, hosted phone modes and Read interruption.
All 105 audit PNGs were inspected in contact sheets, including the 40 from the aborted attempt.
Final affected-screen checks were also viewed; their browser runs reported zero errors.

## Art made

Fifteen images generated with the built-in image tool, saved in art/raw and converted only with art.py --rekey.
Total finished art: 529.57 KB. Bundle: 875.87 KB, below 2 MB. Full prompts / provenance in art/prompts.json.
The Classical postcard was redrawn once because its first candidate included a figurative decorative bust.
Radio and knob edges were despilled through the same art pipeline. No art was downloaded.

## Art still to paint

None. No people were requested or retained.

## Engine changes wanted

See handoff.md: music-studio.js play needs an explicit clock start / pre-commit boundary hook and documented
custom-voice buses to absorb this radio's variable-phrase conductor. No engine or other shared file changed.
rhythm.js is absent, so drums remain a local extension using the shared audio context.

## Left open

- Full by-ear arrangement and balance review, especially formant choir, the sampled loop and gamelan model.
- Very late Flip / desk requests can move one boundary later because the next boundary is already scheduled.
- Recorded news-reader character is not guaranteed by browser speech. No recordings were created, as instructed.
- Fresh cultural-content review of the added gamelan station belongs in the next cold review before shipping.
- The full automatic control-walk did not complete. No full audit rerun followed the targeted CSS repairs.

Source has 1608 lines, maximum 145 characters per line, with no em dashes. All test Chrome / host processes are closed, ports 9980, 9981 and 8785 are closed, and host.html is removed.
