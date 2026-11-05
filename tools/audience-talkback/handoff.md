# Audience Talkback build handoff

## Structure

src.html starts from the kit starter. It contains the responsive theater, Watch, mixer/notebook, Talkback form,
and dialogs, followed by content, guarded storage, scene playback, music scheduling, rendering and event wiring.
It uses kit/curio.css and kit/curio.js. No family engine is specified. Nothing shared was changed.
scene-audio.json is loaded by src.html and currently contains empty A and B recording arrays.
The standard bundler produces the self-contained audience-talkback.html from art tokens, JSON and kit tokens.

window.__tool exposes state, actions, V.log as vlog, scene playback and switch timing logs, fairResults, and the
music clock. Timers carry a generation token, so an old line cannot advance after a stop, jump or delivery switch.
Voices restart the current line immediately, including during a gap. Other switches do not touch the timeline.
Both original Web Audio loops use one clock, at 72 and 112 beats per minute, with a 150 ms bus crossfade.

Notebook trials collect the union of all elements that differed from their captured Base during that play.
Base cannot change while playing. A row requires five fully completed lines and reaching the ending or stopping
after line 5. This prevents a line-10 jump or quick tap-through from creating an experiment. Multiple changes and
base replays stay in the notebook and retain ratings but are excluded from the chart. Repeated ratings are averaged
per element, with the 0 to 2 mapping written on the chart. Ratings are opinions, never checked against an answer key.

The four mixer nodes and all criteria/rating nodes stay stable under the pointer. Notebook nodes are rebuilt only
when adding or clearing rows. Ratings themselves update their existing buttons. The compact notebook shows only
its latest row; the complete list remains saved. At short landscape sizes, captions occupy the panel's hint area
during playback, leaving more room for the painted stage. The caption moves on resize; the stage moves into the
thumbnail mount on entering Talkback. Entering Swap lab resets its switches to the selected Base. This prevents
finishing Watch B from leaving four differences against Base A before the student's first one-switch trial.
Lab Tab boundaries route mixer and transport, notebook, then line ticks. Focus calls use preventScroll.

## Open question decided

The spec leans toward hearing an acted sample before making all twenty clips. Keep the sample-first route.
The four delivery styles and speaker voices are recorded in voice/lines.json under scene_deliveries.
The build brief explicitly says not to record audio. No sample or full audio set was recorded during this Build.
The current browser speech preview is labeled on screen, with estimated version times. This is a material limit:
browser rate/volume changes do not reproduce the requested acted shaky, laughing, gentle and surprised deliveries.
Autonoe and Gacrux are the intended final voices; the browser cannot select these bank identities.

## Audio completion route

After a future task authorizes recording, make a sample of Kit and Holloway in both styles before the full set.
The ten spoken texts are in voice/lines.json under scene_lines; poses and stage directions remain on screen.
Generate twenty distinct clips with the supplied two voices and four acted styles. The ordinary voice bundler keys
clips by text, so it cannot distinguish the same text in A and B. Put each delivery in scene-audio.json as an object
with src (an inline audio data URI) and duration (seconds), in A and B arrays indexed 0 through 9.
The existing player uses those clips, onended and error guards, with the specified gaps and pre-line-8 pauses.
Measure the sum of all ten actual clips plus nine gaps and the extra pause. Replace the estimate labels on both
Watch buttons. Test all sixteen mixes audibly and confirm no overlap or truncation. Do not silently call these
browser previews the recorded acting comparison. The host uses Curio.voice with knowing-guide / Sadaltager.

## Art and local choices

- Ten images were made with the imagegen tool, as requested. All actors are animals; no people were generated.
- A retry made kit-b-down after its first image call returned no saved output.
- The two kneeling bears were edited to remove extra bicycle wheels. The bike is a separate composited asset.
- All cutouts use the specified flat magenta key, then the free art.py --rekey pass, with edge despill.
- Art prompts include provenance and redraw notes. Source images remain in art/raw. No external image was downloaded.
- The spec's local-FLUX suggestion yields to the user's explicit request to use the available image tool.
- The source numbers and supplied contrast ratios recomputed correctly. Notebook and chart arithmetic is tested.
- The two quality-bar tools were bundled into Scratch using the original bundler's function and copied inputs.
  Their source folders were not written. Paint Mixer lacked handoff/refine files; Art Style Match's source and
  handoff and Near and Far's handoff supplied additional built-neighbor examples. Missing refine files are absent.
- The user says to stop when codex-report.md is written. Progress therefore lives in Scratch/report-progress.md;
  the final report is written only after the checks, instead of the generic brief's early-report suggestion.

## Storage and privacy

Only feelings, watched markers, notebook rows, selected criteria, ratings and verdicts are saved under
audience-talkback. Parsed values are bounded and validated, and user text enters the page through textContent/value.
The display states that notes never leave the device. Failed storage remains usable and reports saving unavailable.
Clear my notes clears all work after a native dialog, leaves the kit's shared Motion preference, and returns to Watch.
Class vote is temporary and independent of any student's verdict.

## Engine changes wanted

None. A future general purpose dialogue-clip bundler could support two deliveries of the same text, but no shared
change is needed to finish this tool: its loaded scene-audio.json already supports separate inline recordings.

## Review focus

See codex-report.md for actual check results, audit lead dispositions and any limits. The principal content gap is
the unrecorded acting. The cold review should also judge the emotion distinction of the final music and voices,
the usefulness of live swapping, compact notebook access and whether criteria judgments transfer to the verdict.
This was Build only. No polish round or git commit was made.

## Build audit closure

The single full audit completed within its 40-minute limit with 46 leads. All eight initial sizes, Motion off,
mid-action resizing, keyboard focus, five held-click repetitions and quick repeats had no runtime failures.
Every lead is answered in _scratch/audience-talkback/audit-responses.md. The 43 state/walk entries and three
expected vote-control shifts are covered individually. Phone lab notes follow the stage; Talkback stacks its form
and replay card. Long verdict forms and optional teacher counters remain scrollable. Talkback uses #talk-hint as its visible
hint, mirroring the hidden common #hint that Read uses. Compact playback uses the hint area for subtitles.

Focused repairs explicitly link each verdict field to its visible label, put compact Replay/Hear controls before
the thumbnail, improve chart label contrast, cancel speech when cards hide, suppress welcomes behind dialogs,
and make saved-criteria hints state-aware. Native vote clicks and reset, a four-change compact notebook, reverse
Tab, Sound changes during a scene, scrolled phone work and Watch B to fair Lab entry were checked separately.
The full audit was not repeated after these changes. The subset phone-state label is corrected to 375x812 for
the cold review. All manual frames and four audit contact sheets were inspected. All started Chrome instances
and host servers were closed, and the generated tool host.html was removed.
