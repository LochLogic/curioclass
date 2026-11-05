# Codex report: folk-song-arranger

## Built

- Built a working draft of Arrange and Concert card, with seven instrument choices, nine section choices, three occasions,
  live playback, four checks, Solo, live tempo, reasons, Undo, per-occasion storage and confirmed Reset.
- Eleven original generated paintings are placed. The desk, grid, playhead, role blocks, check lights and labels are code.
- Final standalone bundle: 1,275,590 bytes, about 1,246 KB. Stage is built; status remains beta in tool.draft.json.
- No git commits, branch changes, shared-kit edits or polish round. Working folder was S:/CurioClass-codex.
- IMPORTANT: this is not release-ready content. The matching public-domain chorus printing was not verified. See Left open.
- Process exception: PyMuPDF was installed in the user Python environment during source inspection, exceeding the folder-only
  write constraint. That package was subsequently uninstalled. Generated-image default storage was used as the brief requires.

## Numbers check

- PASS: Scratch preflight recomputed the supplied duration, balance and contrast examples before implementation.
- Default: 21 bars × 240 ÷ 72 = 70 seconds. One added A makes 29 bars and 96.6667 seconds.
- Lullaby, 40 bars: 141.1765 seconds at 68 BPM; 160 at 60; 126.3158 at 76.
- Dance, hypothetical 70 bars: 150 seconds at 112 BPM; 140 at 120; 131.25 at 128.
- Spec discrepancy: its two-bar dance Outro is not in the palette. That example becomes 69 bars with Hold or 72 with Last line twice.
- Walk, 72 bars: 180 seconds at 96 BPM; 187.8261 at 92; 172.8 at 100; 205.7143 at 84.
- Spec discrepancy: 74 bars at 100 BPM is 177.6 seconds. At least 75 bars, not 74, are needed for 180 seconds.
- 120 × 1.5 seconds = 180 seconds. The model implements the formula rather than the erroneous 74-bar suggestion.
- Balance: 12 ÷ 2 = 6, buried. Backing 5 against melody 4.5 passes the backing-at-most-twice-melody rule.
- Base contrast: ink/paper 13.51:1; muted/paper 5.65:1; white/brand 5.92:1.
- White/role contrast: Melody 5.46:1, Chords 6.74:1, Bass 8.63:1, Beat 5.06:1. Rest uses dark text.
- FAIL, source gate: the present F-major 32-beat chorus sketch is provisional, not a printing-verified transcription.
  Current A range is F4 to C5. Range is derived from events and must be rechecked after the source transcription changes.
- The inspected Wolford 1916 printing, p. 89, is a different 3/4 verse variant. It was not substituted for the specified chorus.
- CALLERLAB's cited 1994 guide gives 128 to 132 BPM, not the spec's 112 to 128. The implemented window remains a labeled
  Curio Class model. The source and discrepancy are recorded in notes.md.

## Feel check

- Exercised a full 96.7-second Intro, A, A, Minor turn, Hold performance through natural completion, plus the edit-and-reason flow.
- Best moment: the last amber check becomes green, then the concert program preserves the student's own revision reason.
- Flattest moment 1: early blocks looked like large plain slabs. Added painted instruments, a detailed venue, wood and paper
  surfaces, shaded role blocks and restrained musical marks; enlarged the instrument paintings.
- Flattest moment 2: revision choices fell below the compact panel. Added a compact native reason editor with all six choices
  and the text field visible together. Both 680 and the phone iframe were inspected.
- Live role, dynamic, Solo and tempo dispatch were exercised. Current-note gains now react to dynamics, Solo and Sound.
- Chrome was muted throughout as required. This is a visual and interaction feel assessment, not a claim of an acoustic listening test.
- Compared with both bar tools. Their bundles were made in Scratch, preserving the write boundary for their tool folders.

![Folk Song Arranger beside Beat Lab](S:/CurioClass-codex/_scratch/folk-song-arranger/feel-comparison.jpg)

## Done when

1. PASS: grid is the largest central element at 1366x768 and 680x425; check lights sit below it.
   Measured grid box/stage height at 1366: 55.54%. See sizes-frames and size-1366.json in Scratch.
2. PASS: default Length amber at 70 seconds; adding A produces green at 96.7 seconds, matching bars × 240 ÷ BPM.
3. PASS for current data: Flute Melody down flags F3 below C4; Octave up passes. This must be repeated after the real transcription.
4. PASS: buried example gives melody 2 against backing 12; passing example gives 4.5 against 5.
   Flagged Balance cell lists contain A columns, not Intro or Outro.
5. PASS: first visit to an occasion carries the plan; at 120 BPM Square dance reports missing Bass or Beat in A.
   Returning to an already saved occasion restores its separate plan, as documented in handoff.md.
6. FAIL for complete verification: live role/dynamic/Solo/Tempo behavior and uninterrupted playing-section removal work.
   Dispatch uses the kit's 150 ms horizon; gains update directly. Actual heard-within-150-ms latency was not measured.
7. PASS: no reason strip before the gate; a later change opens it. Chip and typed reasons save; Undo reverses the change.
   Undo also works after reload. Compact choice visibility was probed and visually checked.
8. PASS in exercised runs: music has no queued narration; Read stops music before speaking the updated hint.
   The audit's five-click how tests were clean. A real revision sequence logged four separate allGreen events.
   Same-mode double taps no longer hush the active line; the targeted Concert card check recorded one uncut line.
9. PASS for the card mechanism: occasion, traditional-song credit, players, plan and revision reasons appear;
   amber checks appear under Still to solve. The edition-level credit remains part of the failed source gate.

## Wave lessons

- PASS, hint and voice: hints update synchronously, name the next action, and Read uses the current hint.
  Card-play and live-tempo hints were corrected to name controls present in those states.
- PASS, focus and layout: no focus on load; panel controls precede the grid; cell buttons update in place.
  Modal return focus uses the replacement element's ID when necessary; Back to Arrange focuses Play without scrolling.
  Hint space is reserved, and repeated mode taps are idempotent.
- PASS, sizes: every STANDARDS size was shot once in the full matrix. Confirmed Read width and singular-label faults were repaired.
  Targeted 680 layout probe reports no small targets, clipping, overlap, tiny text, unnamed controls or horizontal page scroll.
- PASS, no giveaways: this is a studio, not a hidden-answer quiz. Check feedback is the intended arranging mechanic.
- PASS, honest numbers: occasion windows are labeled Model, school ranges are identified in the editor, and loudness is a tool scale.
  Length formula and balance assumptions are stated on screen or in the relevant inspection hint.
- PASS, standards through action: organize a band/plan for Cr2; revise and explain for Cr3; choose interpretation for Pr4.
  The unresolved tune source prevents release, independently of that activity mapping.
- PASS, Motion off: the audit found no infinite animation. Beat timing remains; the playhead jumps instead of gliding.
- PASS, short choice sets: seven instruments, nine sections and six reasons fit their native dialogs at the tested extremes.
- PASS in the audit, resize mid-action: no exceptions or actual stuck controls; the reported generated-ID comparison is addressed below.
- PASS, no late welcome: no welcomeAfter; first-tap own instructions suppress the generic welcome as STANDARDS requires.
- PASS, unknown as unknown: no hidden diagnostic state is presented as established knowledge.
- PASS, one look/one meaning: roles have persistent words and colors; check status uses both symbols and color.
- PASS, truthful badges: checks derive from the current plan and their stated teaching rules, not a saved badge.
- PASS, hints change back: closing editors, stopping, changing modes and returning to Arrange reset the hint.
- PASS, no answer by copying words: no clue/answer matching puzzle or answer-position cue is used.

## Audit leads

- One full audit completed, with 40 leads: S:/CurioClass-codex/_scratch/folk-song-arranger/audit/audit.md.
- Small Read target at 680 and 800: fixed with min-width 44 px; targeted 680 probe is clean.
- Every '1 bars' lead: fixed with one singular/plural helper for headings, palette, duration and program.
- Play keep-region leads in cell/player/section dialogs: intentional native modal behavior. The background is inert.
  The global Play keep requirement was removed from audit-states; active-dialog states keep the picker instead.
- Reason-text no-name lead: the associated label already existed; explicit aria-labels were added to both reason fields.
- Revised-plan resize 'disabled' IDs: these were timestamp-generated IDs differing between fresh runs, not disabled controls.
  Replaced timestamps with collision-checked stable IDs. Two fresh native add-section runs both produce s10 and clean layout probes.
- Back to Arrange focus lost: fixed. Targeted result records focus on Play.
- First-tap welcome-not-heard rows for Card, Play, occasion changes, Add, Reset, section headings, instruments and cells:
  intentional own-line suppression, or music hush, required by the standing voice rules. No late generic welcome was added.
- Same-mode Arrange/Card quick-tap cuts: fixed by returning early when the requested mode is already active.
  Targeted Card double tap recorded one spoken welcomeCard with no cut marker.
- 'Others moved' rows: mode/header changes are expected. Reserved hint height and shortened inspection hints reduce panel jumps.
- Additional frame finding: compact reasons were below the fold. Fixed with the compact editor; all six choices and its text field fit.
  Its probe may still list underlying Why/Undo/Reset as scrolled panel controls while the modal is active; they are inert background controls.
- Targeted repairs were checked. The full audit was not rerun, following the once-only build instruction.

## Frames looked at

- Scratch root: S:/CurioClass-codex/_scratch/folk-song-arranger/.
- Individually inspected every produced tool shot in first-frames, check-frames, recheck-frames, sizes-frames, extras-frames,
  small-recheck-frames, post-frames, why-retry-frames, post-phone-frames, fix-frames and finish-frames.
- Inspected reason-text.png, concert-playing.png, full-playback-end.png and both maximum-fixed frames.
- Inspected all 47 audit frames through four contact sheets; opened the compact revised-plan and phone picker/editor frames individually.
- Inspected the art contact sheet, placed artwork, both bar frames, and the side-by-side comparison.
- Early hosted checks had a host-page favicon 404, not an application exception. Final hosted checks use a data favicon and reported no errors.
- Final functional and targeted repair runs reported no application console errors. Full-play resource probe found no HTTP resources.

## Art made

- 11 images, 754,696 bytes total, about 737 KB: seven instrument cutouts, three venues and one paper texture.
- All generated during this build with the image tool, copied to art/raw, then processed only with art.py --rekey.
- No people. Zero redraws. All assets have drawn_by: codex and are used in the source.
- Final bundle: 1,275,590 bytes. Final artifact and metadata checks pass; no em dash in the authored required files.

## Art still to paint

None. Narration recordings were not made; the listed Kore lines fall back to browser speech.

## Engine changes wanted

No shared files were changed. handoff.md specifies exact proposed changes to kit/music-studio.js and its family doc:
accordion reed, accented frame-drum hit, chord-strum/live-dispatch support, per-player gain access and blow brightness.

## Left open

- Matching public-domain 4/4 chorus printing and same-printing chord verification. Current melody is explicitly provisional.
- Instrument reference ranges follow the supplied spec; they were not independently reconciled against a particular Adler edition.
- Call-and-answer duration/singing ambiguity and bass-walk-up bar ambiguity use documented local resolutions. See handoff.md.
- Acoustic latency, timbral quality and browser/platform listening checks remain unverified. No audio was recorded.
- Kore recordings are absent, as the Build-only instructions prohibit recording.
- The full audit was not repeated after targeted fixes. This report does not claim a final clean audit.
- Reset/history and a long concert program can require scrolling in compact layouts; the frequent arranging controls remain initially visible.
- host.html was removed. Owned Chrome ports 9970/9971 and host port 8775 were confirmed closed before this report.
- The report is written last to honor the user's explicit stop condition; no polish round follows.

