# Half-Life Dice handoff

The self-contained src.html uses Curio.voice, theme-912 and Plane. Data precedes state, rolling, nuclear balancing, dating and stable event bindings. The tool has no network requests. Geometry observers rebuild Plane at actual pixel size, defer during a drag and preserve focus with preventScroll. No engine files changed.

## Polish changes

Roll uses adaptive square cells for exactly 1,000 dice, as allowed by refine Should fix 1. At 1366x768 faces are 10.8 px; projector faces are 16 px. A 400 ms roll includes a final-face beat with outlined 1s before gray decay marks. Motion off keeps the whole timing. Tracking uses a separate seeded stream and excludes edge cells.

Mark moves in 25-nucleus steps. It accepts exactly 500 after a roll, reports only an observed crossing rounded to a half roll, and explains scatter beyond 0.5 rolls from exact. Before crossing, it asks for more rolls. There is no expected-curve fallback. Roll once reaches the graph end, roll 16 for d20; Roll to 10 still stops at 10.

Header Sound stays on. Counter clicks is separate and starts off. Poisson counts advance a persistent sample stream; Count again lists the next counts. Click times use another seeded stream, about one click per 20 decays, with individual clicks for samples of 20 counts or fewer. Count again preserves a recorded estimate for comparison with each measurement.

Each sample starts with an unplaced ruler pin. Estimate needs movement and locks the reading; Calculate reveals the comparison and logarithm steps. No accuracy verdict is available before Calculate. Minor ruler marks follow logarithmic activity positions, with labels admitted only where they fit.

Nucleons use a touching hexagonal cluster, with exact proton/neutron counts mixed by a seeded shuffle. Protons are filled, neutrons are dark-centered rings. F1 draws three emitted neutrons; N4 adds the mass-zero charge-zero gamma only after a successful Check. Negative proposed charge is labeled Not a nucleus. The energy axis starts at 1 eV and has labeled logarithmic ticks. No prediction action was added to the ladder.

The sources, artifact name and teacher sensitivity notes follow the integrator's settled calls. Carbon dating retains 5,730 years. The spec's 11,020 to 11,920 noise endpoints are tens-rounded versions of 11,023.41 to 11,920.94.

Clear removes only its own mode's progress. The stored key remains curio-half-life-dice, with try/catch and visible device-only privacy wording. Inputs support typing, desktop +/-10 buttons and held +/- repeat.

## Voice changes

voice/lines.json equals V.allLines(), 22 unique strings. wDating changed to: "Pick a sample. Drag the ruler pin, press Estimate, then press Calculate."
The following Read hints were changed or added; none adds automatic narration:
- "Watch Average 20 runs finish. Press Reset for a fresh tray."
- "Drag the line to 500, then read the roll number. Arrow keys move by 25 nuclei."
- "Every roll is done. Press Reset for a fresh tray."
- "Fix the sum that is off, then press Check again."
- "Press Reset to track a die from the start."
- "Roll first, then mark the half-life."
- "Press Estimate first to record your moved ruler pin, then press Calculate."
- "Watch the model counter finish. Then press Calculate to compare this count with your recorded estimate."
- "The line is on 500. Press Roll once until your tray crosses it."
- "Compare your tray with the exact value. Press Average 20 runs to see the crowd settle."
The other automatic lines remain the supplied wRoll, trackTip, wNucleus and tooOld. tooOld is the explicit repeatable event. Roll and Calculate buttons no longer suppress the first welcome. There is no post-roll welcome retry, so a first Track instruction cannot acquire a late welcome; wRoll remains valid during the first roll as requested in refine.

## Engine changes wanted

None. All fixes use local layout, drawing, control and focus code.

## Verification

See polish.md for this round and the scratch polish-* and audit-polish evidence. codex-report.md remains the original build record. The two owner questions remain open: carbon-14 half-life choice and a student action on the energy ladder.
