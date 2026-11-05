# Codex review: band-practice

## Played
Cold Grade 7 solo play came before the builder report, handoff, notes and source: Rehearse, a full Solo break and a full Ghost race, including wrong taps. The large trace and missing-part audio give the practice a purpose. Checked the projection view against Beat Lab and Snowy Mail Route without changing those tools.

## Findings fixed
- Blocker, family:rhythm, `receiveTap`: a late drifting bass tap could match one note but sound a later note or chord. Sound now follows the matched chart position. Browser oscillator test confirms the fifth instead of the octave.
- Blocker, family:rhythm, `updateGhost`: the comparison used differently settled portions of the performances and stopped updating when notes were missed. It now compares the same resolved chart notes and updates on expiration. A silent player correctly falls 150 ms behind the zero-error ghost.
- Should fix, general, result desk: Solo break hid its fitted tempo and landing below the panel fold; Ghost race foregrounded hit-only error rather than its penalized race score. Both now show their own earned result beside the pad, including on the phone.
- Should fix, general, stopped setup changes: a new Song or Part relabeled the old trace and summary. Stopped Song, Part and Speed changes now clear that evidence and select the correct ghost.
- Should fix, general, instructions: Ghost race could recommend its disabled Speed slider. That recommendation is now limited to modes where Speed is available. Mixer narration cannot say fewer players after everyone is restored; Clear bests names the appropriate next mode and confirms the action beside the pad, even with its panel scrolled.
- Should fix, general, stale state: mode/start transitions clear old feedback and color; quiet mode changes discard pending Read. A zero average now says with the band.
- Should fix, general, trace: dense offscale numbers covered notes in compact views, and late bar averages could cover the footer. Compact annotations now show a range and count, with every exact value in the trace title and accessible description. Plot margins keep averages clear of the footer.
- Polish, graphics: redrew the oversized shaker as a hand-sized wooden egg on a worn stool, retaining the room's painted style and warm light. The other four paintings remain.
- Updated notes, handoff and audit states for the revised result presentation. No new music topics or modes.

Independent checks: 24 browser rule checks passed; 40 ms early, 40 ms late and zero keep the right signs; sparse Waltz bass gives 7 hits, 1 miss and 1 extra, with 18.75 ms race error. Ghost save/load/improve/clear and phase-preserving Speed/Part/mute changes passed.

Recomputed the spec's durations, 4.2 s calibration span, 78.125 ms tight window, t critical values, drift examples and WCAG ratios in Python. Cyan/background is 9.863:1; ink/background 15.972:1; muted/background 7.130:1. The browser fit independently gives 99.802 BPM, displayed as 100. Seeded 3,000-trial steady conditions give 95.2 to 100 percent steady/uneven; the separate twenty-run check had no false directional calls.

A complete real-clock Solo break had 96 hits, no misses or extras, zero scheduled band notes in bars 5 to 8, and a 0 ms return-clock error. The fitted fast player read 100 against 96. Actual held Space, repeat suppression, J/F, pointerdown, pad focus and keyboard-only start/tap/stop passed. No network requests or runtime exceptions in that run. An actual eight-click calibration accepted 80 ms; uneven/clamp/timestamp tests passed.

Voice checks use the kit log. Counts below used a short speech-completion stub at a two-second action pace; the final audit uses browser narration.

| Line | Kind | Expected | Spoken |
| --- | --- | --- | --- |
| traceHow | how, five takes | 1 | 1 |
| noTaps | event, five takes | 5 | 5 |

Read waited through a take, spoke after Stop and worked with Sound off. No narration started during the full clocked take. All 19 fixed narration strings match `voice/lines.json`.

## Findings left
No confirmed blocker or should-fix remains. The audit's 16 mechanical leads were checked: six are the modal intentionally covering its underlay; five are welcomes skipped for Play, the three mixer how-to lines and calibration; five are Clear bests focus/unchanged flags across the three modes. Real held clicks after scrolling that button into view clear a seeded best, retain focus and keep the button visible in every mode. The unscrolled audit coordinates do not exercise that control. The direct frames did confirm that its hint could be above the scrolled panel; that confirmation is now repeated visibly beside the pad. Existing recording/engine limitations are listed below.

## Flattest moment left
Night Bus drums has one playable hit per bar. It is the least busy role, but retaining that space is the specified one-drop ensemble lesson. The formerly flat Solo break result now lands visibly beside the pad.

## Graphics
All five finished paintings were inspected individually and in use: room, drums, bass, keys and shaker. One redrawn, none missing, none containing people. Built-in image generation; full house style and replacement asset prompt are in `art/prompts.json`, with selected raw art at `art/raw/shaker.png`. Final painting: `art/shaker.webp`.
Final art 290,938 bytes (284.1 KiB); final offline bundle 472,416 bytes (461.3 KiB). No missing art or network dependencies.
Changed preview, laptop, grayscale, Motion off and 375 px iframe frames were opened. Audit frames were inspected through numbered contact sheets, with problem frames opened directly. The central trace and painted band were retained, not flattened.

## Audit
Completed once within its 40-minute limit. `review-audit/audit.md` records 16 leads, all answered above. All eight size checks, listed states, Motion off, repeated speech and quick taps were clean. Resize stress completed without exceptions or disabled controls left stuck. All 61 audit PNGs were opened via 16 contact sheets; modal and result frames were also inspected directly. The audit predates only the two-line visible Clear bests confirmation fix. Its three affected mode frames were re-shot with held clicks, successful clearing, retained focus, visible feedback and no console errors. No second audit or polish round.

## Left open
- No narration recordings or unmuted headphone listening judgment. Browser speech is the existing fallback; every test Chrome used mute-audio, as required.
- The absent shared rhythm engine/document remain the precisely described requests in `handoff.md`; kit and docs were outside the write scope.
- Compact layouts scroll secondary settings and the long summary. Play, Part, the trace and 120 px pad stay visible; the phone pad ends at 783.5 px in its 812 px host.
- Ghost race's exclusion of extra taps from its score is specified and retained; extras remain visible. Compact offscale numbers are grouped on canvas, with exact values retained in the title and accessible description.
- One cold review pass, then affected rechecks and one final audit. Only `tools/band-practice/` and `_scratch/band-practice/` were authored. No commits, shared-file changes, or leftover owned Chrome/server processes.
