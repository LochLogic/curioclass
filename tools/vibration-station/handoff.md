# Handoff: Vibration Station

## Build scope

Build only, no git commits, no polish round. Source, metadata, art prompts, voice text, teacher notes, audit states and one offline bundle are tool-local. Build evidence and people contact sheets are in `_scratch/vibration-station/`.

## Code map

`src.html` starts from the kit starter frame and uses kit CSS, Sound, Motion, Read and `Curio.voice`. Its own sections are responsive layout, source lines, bench synthesis, station interactions, Find out state machine, Reach Sam state machine, and science canvas drawing. Painted images are referenced once in the asset table. The string, arcs, rice, sprinkles, bands, prediction icons, chart and book are drawn in code.

`window.__tool` exposes `state`, `setMode`, `allLines`, `vlog` and `vq` for review. Student progress is in memory only. No debug shortcuts are shown in the tool. Prediction choices shuffle on question entry; repair faults are independent draws with replacement; drum messages shuffle after code creation.

## Tricky behavior

- Q2 needs a real pluck and Hold still within the four-second ring.
- Q3 keeps sticker evidence without filling the page. Rice and sand both work.
- Q5 keeps the touching trial and requires a separated pan before a successful Bang.
- The first repair attempt is permanent in that scene's record. Subsequent fixes cannot upgrade it.
- Code counts stay editable until the first beat; duplicate counts are blocked. The pause, not a Send button, ends a message.
- Held Hum stops on release, cancellation or loss of focus. Microphone input is ignored until the hum investigation's test step.
- Speech and pictures are separate. Actions happen immediately while voice feedback queues. Read uses the current hint.

## Spec decisions and contradictions

- No open questions were listed in the spec.
- String length is called 15 m in Content, but both build instructions and Done when demand a tight yard stop at 12 m. Followed the explicit 12-step yard stop, with the string ending at a nearby park bench. Distances are story values; no numeric distance is displayed.
- CODEX-BUILD overrides BUILD's older “Do not draw art” instruction. All 35 listed assets are drawn with the image tool. It also overrides the older Gemini-only people instruction with OpenAI image generation and `people: true`.
- CODEX-BUILD says do not record audio. The requested bank is authored, but this build uses browser speech and 0 KB recorded audio.
- Voice scope is the mode, with control-visibility and state validity on step instructions. This preserves a result before a later question instead of dropping the result on a numeric step change. Rapid two-second taps can still outrun browser narration; see the report's Voice walk limitation.
- The source list's count of “25 images plus poses” resolves to 35 named output assets when the four hands and two Ben poses are counted explicitly. The manifest lists each one.
- The audit normally demands 60 px everywhere for K-2, while this spec explicitly allows 44 px at 680x425. The compact exception is documented in audit-states.json.

## Sensitivity

No cultural, Native, religious or hard-history content. Children and hands are people assets. The contact sheet supports the BASELINE representation review: inspect age-appropriate clothing, natural hands, consistency of Sam and Ben, and respectful representation without stereotypes. No personal prompts.

The gentle hum prompt invites children to feel their own throat vibrate. It makes no health diagnosis or personal-body inquiry. A fresh people review passed representation and natural hands; the revised puzzled face passed a recheck. Cold review redrew Sam's cheering pose with the same plain shirt and white socks, preserving its joyful full-body pose.

## Engine changes wanted

None. All implementation changes stay tool-local.

## Final build checks

The full audit completed once with 36 leads. The report accounts for each; remaining rapid speech failures are explicit. Focused compact/phone rechecks fixed chart clipping, code-label overlap and completion focus. Actual Sam dragging and Sam/Ben portrait repair taps were exercised. Visible band hit testing follows the painted wire positions.

Microphone validation used an oscillator through a real Web Audio MediaStream, covering the RMS thresholds, sustained test gate, visible stop control after success, release on Next and cancellation of a late permission response. This does not validate classroom microphone hardware or actual acoustic listening. Held Hum remains independent of microphone level. Returning to a repaired scene restores its actual hint; switching chart place resets the untested pose and signal.

The generated bundle is 1613.6 KB, with 1118.3 KB art and 0 KB recorded voice. Browser voice can be outrun at a two-second tap pace; audio-only pre-reader completion has not been independently validated.

## Review next

Read codex-report.md for final test results, image sizes, source verification, audit leads and any remaining limitations. A cold review is the next phase; this session performs no polish round or publication.

## Cold review repairs

- Next acknowledges a tap immediately with an outline and aria-busy, retains the current evidence while speech drains,
  and then advances. Mode changes cancel pending navigation. Material selection uses the same acknowledgement so the
  whole drum-plan line retains its visible choices before the test controls appear. Audit fixtures wait for this state.
- Questions remain valid through their own test; they never carry into another question. Assembly and place/device
  changes clear obsolete speech. Chart/code how-to lines use stable once-only keys. Early Talk does not repeat Sam's welcome.
- String geometry follows the actual object-fit painted bounds, including bottom alignment in tall windows.
  Sam's separate cup fills the poses without a painted cup. Knots and a loose curled end distinguish connection states.
  A missed repair keeps a stopped-shake ring visible until the fault is fixed, including with Motion off.
- The discovery recap fills its cards with larger evidence pairs and existing apparatus pictures. Singular fix wording
  is correct. sam-cheer was redrawn with OpenAI imagegen and resized with the free art.py rekey path, preserving alpha.
- Review evidence, source checks, bounded runners and focused tests are in _scratch/vibration-station/review-*.
  The review audit was launched early while cold browser launches were failing; it is not a final-bundle audit.
  No shared kit changes, commits, paid generation scripts, or recorded audio were made.

## Review validation limits

The cold review fixed the reopened-page summary crash, stale question feedback on a book-page jump, and hearing icons
that reported success from a ready-to-listen pose. A missing page now reopens with its own hint; assembly clears an old
failed outcome; a repaired but untested phone has no heard icon. Focused browser assertions passed.

The one review audit finished within 40 minutes with 31 leads. It started early during cold-driver failures and later
crossed source revisions, so it is not a final-bundle clean audit. Pending-action waits were added to the fixtures.
Mode-by-mode voice checks heard the required instructions and whole explanations, but continuous same-tab attempts
hit the driver's evaluation cap and then the harness's pending-action wait guard at Q5. That retry path was stopped.
Do not claim strict continuous two-second held-input or independent audio-only child validation from these results.

The updated people contact sheet is _scratch/vibration-station/review-people.jpg. Some unchanged small sock-stripe
differences remain across poses. No cultural content or stereotypes were found in the cold people check; the revised
cheer remains clearly identified for the later fresh people/owner look.

Question headers use a neutral inspection icon, so a child cannot copy an outcome pictogram into a prediction.
Empty Hold still buttons are excluded from the first-tap speech-owning selector: their first tap now gets the welcome,
while their apparatus action remains the specified no-op.
