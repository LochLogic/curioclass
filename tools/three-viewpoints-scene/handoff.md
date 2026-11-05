# Three Viewpoints Scene build handoff

## Structure
`src.html` starts from the kit starter. CSS defines the rehearsal room, beat board and each mode's responsive focus. The script loads `scene-lines.json`, restores validated local work, initializes Curio.voice, computes checks, renders the board and curve, then wires editing, offers and the cue runner. Stable board signatures preserve card elements during playback and pause updates. `window.__tool` exposes state, analysis, editing and playback hooks for checks.

`scene-lines.json` contains exactly the spec's 40 options, their estimates, tensions, need/turn tags and offer locks. It is inlined by the bundler. `voice/lines.json` has every allLines string and character bank assignments. All runtime assets are bundled and offline.

## Timing and tricky parts
Playback uses a cancellation token so Stop, a card jump or an edit cancels a pending pause, voice or cue without a stale continuation. A pause value is read on entry to each beat, including empty beats in Play scene. Editing stops playback; pause changes keep it running. Perform requires all six beats populated and waits on the chosen role, or every role in All three live. Run time includes live waits and pauses, measured from Start to the final Done. Planned time is captured at Start.

The narrator is hushed before playback. Character lines use V.say events with hint false. The live-cue instruction remains on screen and in Read, with no narrator interrupting a performance. Read first stops playback, then reads the current stopped-state hint. Browser speech is held to at least the estimated duration when it returns early. Motion off changes no timing.

Offers are triggered by cumulative successful placements, including an auto-placed accepted offer. A full target beat still unlocks its offer, with instructions to cut a line and add it from the picker. Passed offers reopen in Offers. Reset asks before clearing local work. Corrupt or inaccessible storage does not prevent play.

## Open question decisions
- Took the spec's proposed character bank voices: Maya `big-sister`, Mr. Ortiz `friendly-dad`, Ms. Dale `firm-captain`; Jules is `casual-peer`. Did not choose the pitched-browser alternative. Build forbids recording, so these assignments are recorded in the manifest for future clips. Unrecorded lines use available English browser voices at pitch one. The tool routes roles to different available names where possible. A machine with one English voice cannot supply three distinct timbres.

## Art
Four illustrations generated during this build with the image tool, not FLUX. Warm painted black-box stage and three keyed prop cutouts. Ms. Dale's first candidate added a desk and theatrical accessories; rejected it and generated the single-chair version. All finished assets inspected at their final sizes. Despill applied through `scripts/art.py --rekey`. No people in the used images. Prompts and raw originals are retained.

## Responsive choices
At laptop widths the six beats, curve and Play remain in view. Under 900 px the board is two rows of three. At 680x425 the props become a slim strip and Add becomes a 44 px plus button in each beat heading. Tighten uses compact headings and puts beat times on the curve; its card lists scroll within their beat. At 375 px the board is a vertical list, the curve is above it, and Play/Stop stays fixed at the bottom. Perform's Done and Back controls also stay at the bottom on phones. Long dialogue is abbreviated on board cards with the full line in its title and selected-card panel; the picker and live cue show it fully.

## Verification pointers
Scratch contains `numbers.json`, 24 rule/state assertions, held-input scene building, reload/reset evidence, playback jump/Stop evidence, keyboard building, two-second voice logs, twelve size frames, targeted rechecks, grayscale/Motion-off, seven-option picker, crowded-board and full twelve-cue live-run evidence. The full live test used simulated delivery intervals and completed in 48.2 s against a 58.4 s plan. Headless Chrome was muted, so this is not a by-ear review.

## Engine changes wanted
- `kit/curio.js`, `speakOne` and Curio.voice item options: support an optional bank/role voice assignment on each line, preserving queue cancellation and Read priority. This tool currently routes browser utterances while waiting for role-specific bank clips. A shared supported selector would remove that workaround.

## Remaining review attention
- Bank recordings are absent by Build instruction; available browser voices and durations vary. Review actual character delivery by ear later.
- Compact and maximally crowded boards deliberately use inner card scrolling. A full four-line beat cannot expose every 44 px card plus its controls in the 680x425 two-row layout. Check this tradeoff in the cold review.
- The phone picker keeps all seven options in three readable columns. The narrow board uses a vertical scroll region as specified; its header and transport stay outside that region. The hint and earlier character cards can require scrolling back into view.
- The school's transport and budget figures are fictional circumstances. Dialogue about fuel savings is not a measured transport model.

Build only. No commits, no branch changes, no polish round.

## Audit outcome and targeted repairs
The single mechanical audit completed with 223 repeated leads, 97 PNGs, clean Motion off and clean resize/stuck-control checks. The full audit was not rerun after repairs. Every lead is answered by category in codex-report.md.

Post-audit repairs reserve space outside the phone scroll area for Play and Done/Back, expose all seven phone picker options, move Jules's offer above secondary editing controls, keep desktop hints and Play sticky, enlarge the Tighten card area, and give Read a 44 px minimum width. Intentional card abbreviations now declare text-overflow and retain their full title. Repeated taps on the active mode no longer cut the welcome. Empty Perform cannot queue the Start instruction. Repeated Hear uses a token to prevent stale light/voice cleanup. Card jumps update the selected card so subsequent edits affect that line. The allGreen event waits for a populated board as well as four green checks. A tiny numerical tolerance protects the exact pacing limits.

Targeted real-input checks confirmed visible compact offer buttons, all seven phone choices, six phone placements and six live cues through the recap with no transport overlap, mixed live/voiced roles, a valid 30-second boundary, same-mode welcome continuity, and selected-role hover contrast. Final Tighten checks at 1366, 1000, 760 and 680 retain the hint and expose a complete 44 px card in each populated beat. Multiple cards still scroll in dense or compact beats. All targeted browser checks were free of console errors and exceptions.
