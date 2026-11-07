# Polish: cipher-vault (Codex fix, round 1)

Evidence root: `../../_scratch/cipher-vault/`. Before: `fix-before-a/`, `fix-before-b/` and their JSON results/logs. After: `fix-after-a/`, `fix-after-b/`, `fix-proof-a/`, `fix-proof-b/`, `fix-proof-c/`, `fix-final-a/`, `fix-final-b/`, `fix-last/`. Each named shot also has `<name>.numbers.json` at the evidence root. All final claims below use viewed frames or captured numbers. One performance requirement remains open.

## Blocker

1. **FIXED. Encode exposes hidden keys.** Before `b1-box`: wrong key loaded, visible encoder alphabet, box unpeeked. Boxes now load their own symbol key; Encode/New key use a separate fresh writing workspace. Decode restores cipher and guesses. `final-symbol-box-cheats`: toggle, New key and a Wheel/direction/Symbols detour all use unrelated keys, leave the box unopened and restore its actual key/tape. Counting and Poe pass the same three attempts in `proof-b1-cheats`.
2. **FIXED. Wrong Counter glyph labels.** Before `b1-b2-poe` recorded glyph 8/count 33 labelled 5. The retained bar nodes now draw actual glyph SVGs and name the glyph in aria. `last-poe-sorted`: tallest bar title `8: 33`, label `8`; `proof-counting-glyphs`: 296 symbols, 26 drawn labels. `last-phone-labels.png` verifies the final compact glyph sizing.

## Should fix

1. **FIXED. Pre-solved RAVEN/Vicksburg.** Before RAVEN length 5, offset 53, RAVEN guess; Vicksburg offset 4. After `final-raven-default`: length 1, offset 0, hidden column guesses and Use key. `s1-s11-vicksburg` after: offset 0. Choosing 5 restores 8.8, RAVEN and 20/23; moving to 53 gives ENRAVEN; Vicksburg at 4 gives HESTERBLU (`proof-raven-reachable`, `proof-vicksburg-date`, `final-raven-read`).
2. **FIXED. Too-short Splitter estimates.** Before `s2-short`: DSDND from 12 letters at length 5. After: no key guess or Use key under ten letters in any column; empty tape says No letters. `last-sweep-guard`: all 51 insufficient-data cases across lengths 1 to 12 kept Use key hidden, and even a direct click changed no key. `last-math-parity`: 120 independently computed coincidence values, maximum error 0.
3. **FIXED. Secret left on the bench after Seal.** `s3-seal` before: readable MEET AT THE OAK, shift 7. After: cipher TLLA HA AOL VHR, shift 0. Seal now opens the newly stored cipher with its hidden settings reset before inviting handover. This also resets Square, Pad and rotor starts through the same open path.
4. **FIXED. Rotor box estimate.** Before `s4-rotorbox`: 105,456 claimed while order/rings/cables were supplied. `proof-seal-card`: 17,576 hidden starts, with order/rings/cables explicitly given and the plugboard restriction stated. Connected-cable card checked in `s4-rotorbox`; search remains disabled with cables.
5. **FIXED. Glyph tape lost by Encode.** Counting reproduced as 382 stored characters/296 glyphs becoming empty. After the round trip all 382 characters and the E guess remain (`s5-counting`). Poe's original ASCII-symbol tape did not erase in my original attempt; it instead exposed its key. Its 203 characters and guesses now also return after writing (`proof-b1-cheats`, `final-storage`).
6. **NOT FIXED in full. Square performance.** The cause is repaired: its 728 reference letters are built once; only highlights/fill move. Bars/column nodes also persist and counting no longer repeatedly splits strings. Original local update median was 4.4 ms without throttling on the 478-letter reproduction tape. At 1366x 768, 600 letters, three tools, Encode with changing keys and 4x CPU slowdown: zero added tableau nodes, update median 8.4 ms, p 95 12.1 ms; frame median 16.7 ms but p 95 33.4 ms and maximum 116.6 ms. Thus I cannot claim sustained 60 fps. `proof-4x-square.numbers.json`, `fix-performance/proof-4x-square.png`. Further performance work remains; no school-hardware certification.
7. **FIXED. Compact rotor keyboard.** Before 680x 425: keyboard y 406 to 450, beyond machine bottom 305. After: keyboard y 201 to 255 inside the machine; at 375x 812, y 268 to 322 inside the machine. Both viewed in `fix-after-a/s7-rotors-*`. All 26 keys are present, with order/windows/rings and transport above/beside them. The first phone before attempt evaluated the host instead of its iframe and failed; its corrected run occurred after the first repair, so it is not presented as an original phone before frame. Small compact targets remain a limitation noted below.
8. **FIXED. Unaligned glyph guesses.** Symbols/Grid Decode now pairs every glyph with its letter or dot on the output tape, with an explicit scroll cue. Before `s8-poe-pairs`: separate glyph/letter tapes; after the same E/T/H assignments, THE sits below its own symbols. `last-grid-pairs`: REMEMBER DEATH and 14 paired positions including the space.
9. **FIXED. Tools stuck on Input in Encode.** Ciphertext is the default source, following Input in Decode and Output in Encode; explicit Input/Output overrides remain. `s9-square-counter` changed from unchanged bars/Input to changing bars/auto. Rechecked with the retained bars in `final-square-counter`.
10. **FIXED. Ghost freezes on pasted punctuation.** Before `s10-ghost`: disabled with digits, curly quotes and parentheses. After `final-ghost`: enabled; Ghost shift 3, A to D. It uses the letters actually counted; Sorted and glyph alphabets disable shifting.
11. **FIXED. Vicksburg chronology.** The original 2009 opening claim appears in the before Manual JSON. The curator dates removal to December 2008; the revised case, notes and source record use that date. I say the decoded message was publicized in 2010, rather than asserting an unconfirmed exact decipherment year. The sources disagree on that year. `final-date.png` and its full text result prove the final wording; source details below.
12. **FIXED. Read omits the hint.** Original `s12-read-hint` lacked it. Fresh held Read now starts Drag the inner ring, including at 680x 425 and with Sound off (`last-hint-read`, `last-soundoff-read`). Each log contains one Read entry.
13. **FIXED. Stale hint narration.** Welcome eligibility and validity require the hint still to be present. Before three Right/increase actions: hint already gone but its automatic line spoke. After the same held-click pace: empty hint, no stale line (`s13-stale-hint`).
14. **FIXED. Compact hub hint.** Original widths were 106.9/156.4/238.8 px at 680/800/1000. Final two-line widths are 58.25/83.66/125.98 px, inside the hub; it also clears the center pin. Disk diameters increased from 162/237/362 to 172/247/372 px. Viewed `final-hint-680`, `final-hint-800`, `final-hint-1000`.
15. **FIXED. Counter/tape disagreement.** It counts the alphabet the tape actually holds. `s15-grid-count` changed from LETTERS 0 versus tape 12 to LETTERS 12 versus tape 12. Glyph tapes say SYMBOLS 296/203, with matching actual glyph labels (`last-phone-labels`, `last-poe-sorted`).
16. **FIXED. Rotor arrival at AAM.** Arrival now displays start AAA and step 0. `final-rotor-vectors`: typing AAAAA gives BDZGO; independent stepping from ADU gives ADV, AEW, BFX. Whole-tape Run still displays the resulting windows.
17. **FIXED. Letter shortcuts interrupt rotor typing; no Swap undo.** Before HELLO changed direction/opened Cases. After `s16-s17-typing`: input HELLO, output ILBDA, Decode unchanged, drawer closed. Rotor letters type anywhere outside a text field. `proof-swap-undo`: button becomes Undo swap and restores the previous tape. An empty previous tape is also a valid undo state.
18. **FIXED. Run leaves stale status.** Before `s18-bombe-run`: press Run tape even after running. After: Tape run, 50 letters, beside the output, with the weather plaintext. Bombe statistics remain available.
19. **FIXED. Dense Manual/seal language.** Each mechanism starts with a plain action/explanation; mathematical terms follow it. Bumpiness starts with matching two letters, random key explains equal chances, small counts use plain numbers and larger seal counts use superscripts. Viewed `proof-plain-manual`, `proof-seal-card`, `s19-manual`, `s19-seal`; final source retains the precise definitions and limitations.

## Polish accepted

1. **FIXED. Bombe pace.** Motion on: actual tested counts advance over 1,515 ms (`proof-bombe-pacing` samples). Motion off: one order 58 ms, six orders 783 ms (`proof-bombe-calm`). Stop during the paced run leaves no candidate (`final-bombe-cancel`).
2. **FIXED. Local event readouts.** Box/seal/run messages stamp the tape; search messages appear in the bombe panel; 600-letter limit appears in the input count. The plate carries the plate. Seen in `s3-seal`, `s18-bombe-run`, `proof-600`, `proof-bombe-pacing`.
3. **FIXED. Sticky header.** Opaque header at panel top with padding inside. `proof-three-tools-sticky`: panel top 138, header 139, opaque rgb(36,40,44); viewed at a 250 px panel scroll.
4. **FIXED. Sorted English model.** Sorted letter bars retain the independently sorted English profile, with shifting disabled. `proof-sorted-english`: 26 ghost outlines. Glyph charts retain no English model.
5. **FIXED. PAD tails.** Each affected practice card names PAD and its four filler letters, without introducing a new unsupported historical claim. All original tails and checked material remain intact. `final-sheet-cards`.
6. **FIXED. Multiple period spikes.** Splitter Manual explains that multiples spike too and to test the smallest spike. `proof-plain-manual`; no claim that the smallest apparent spike always guarantees the key.
7. **FIXED. Fader name.** English ghost appears beside its value, including the compact Counter. `last-phone-labels`, `final-ghost`.
8. **FIXED. Pad columns.** Cipher/key/plain letters stack in aligned columns (`proof-pad`). All three named readings still decrypt exactly after stripping spacing; three true results saved.
9. **FIXED. Whole pigpen grids.** Four source diagrams for the standard alphabet, three for Leeson, above their matching individual glyphs (`proof-grid-origins`, `proof-leeson`).
10. **FIXED. Tape scroll cue.** Output has an explicit vertical-scroll readout and tapes have a scroll edge/track; paired letters scroll with glyphs. See final phone and long RAVEN frames. Partial extra rows are not presented as complete rows.
11. **FIXED. Tableau right edge.** Its full width fits the reference card; long content can scroll vertically. All A to Z columns are visible at 1366 (`final-mode-square`, `final-raven-read`). The separate crossing lens remains legible in compact views.
12. **FIXED. Encode labels.** Writing key replaces 0 ASSIGNED; assignment strip, Clear and selected-glyph prompt hide in Encode. `b1-box` after and `final-storage`.
13. **FIXED. Phone Symbols gap.** Specificity corrected; machine row 174 px. Counter chart ends 626, readout 648, panel bottom 651 at 375x 812. All visible in `last-phone-labels.png`; the blank band is gone.
14. **FIXED. Range meanings.** `final-arial-rings`: Ghost shift 3, A to D; Column 2 key S. These update with the faders.
15. **FIXED. Ring dials.** Two-digit monospace spinbuttons support tap, Up/Down and Home/End. `final-arial-rings`: Ring 26, aria value 26; final desktop rings are 44 px tall (`audit-repair-rotors-1366/1280`), with 32 px compact dials.
16. **FIXED. Short-text bumpiness note.** Manual explains that short, repetitive texts score higher. `proof-plain-manual`; 120 reference computations still match exactly.
17. **FIXED. Spoken bumpiness.** Held Read log says BUMPINESS 8.8 AT LENGTH 5 and omits IC times 100 (`final-raven-read`).
18. **FIXED. Plate wrap/screws.** One line at 680x 425 with screws outside the text (`final-hint-680`); 760 px plate also fits (`final-760-plate`). Phone uses two 10 px plate lines (`audit-repair-plate-phone`).

## Settled calls

- Both blockers were treated as blockers. Weather retains WEATHERREPORT and All crib spots; its only survivor remains B O X over 27 spots. Leeson remains readable on load.
- No goals, scores, levels, quiz, finish, kit header or automatic event voice added. Voice remains hint once, then Read. No new event recordings or lesson welcome.
- MS-SYS-SE-32/33 are not newly claimed here; this Curiosity remains the second card. The map is outside the authorized edit scope. The eventual integrator must remove any unsupported map credit rather than add a thin activity.
- Mary, al-Kindi and the sensitive history/context are retained. Only the authorized Vicksburg chronology changed. No new sensitivity verdict is claimed; `refine/sensitivity.md` is absent.
- Open questions remain open: reflector A/1930 case, damaged Vicksburg slip, bench-wide shortcut rebinding, spec voice section and Fan layout. No added feature/topic.

## Cheats tried

- Encode toggle, New key and machine/direction detour on a sealed symbol box, the counting sheet and Poe: only unrelated writing keys appeared. Returning restored the tape/guesses; no box opened by these attempts. Nine attack paths, all closed.
- Splitter lengths 1 to 12 on six short/empty tape sizes:51 insufficient-data cases; Use key hidden and direct clicks inert. Choosing a supported length with enough text remains deliberately useful.
- Grid has no hidden key; its immediate readable output is intentional. Rotor order/rings/cables are public on its box, and its count now includes only the hidden starts. Wheel zero and a weak chosen key remain honestly weak, not falsely secure.
- Weather's known crib producing B O X is the specified open demonstration, not a score. Stop during the paced search canceled it. No success badge or finish was introduced.

## Voice walk

- Held clicks 120 ms, 2 s gaps. Fresh Read: Drag the inner ring, Wheel, Decode, current shift, output, Counter. One Read log entry. Same result with Sound off and at 680x 425.
- Three increases to shift 3: no stale automatic hint after it disappeared. Output THE DIE IS CAST. Original before log had the late automatic line.
- RAVEN after selecting length 5: Square, Decode, Key A, first 80 output characters, Bumpiness 8.8 at length 5, 5 divides 20 of 23 gaps, implied ENRAVEN at 53. No spoken unit tag.
- `allLines()` equals `voice/lines.json`: exactly Drag the inner ring. Browser speech fallback remains; no audio was recorded. Logs are evidence of started Read/speech, not a new listening study.

## The real material

- No dataset or historical ciphertext changed. Practice sheets/drawn shapes remain Curio Class CC BY 4.0, code MIT; source and rights records remain in the Manual and `tool.draft.json`. The optimized counts are computed from the same bundled 2,705-byte material file. No corpus, modern prose, photograph or new art imported.
- Chronology rechecked 6 November 2026: [Catherine M. Wright, American Civil War Museum, Message in a Bottle](https://acwm.org/wp-content/uploads/magazine_message_in_a_bottle_article.pdf), printed page 5 gives December 2008 removal and January 2009 photograph; page 7 dates the publicity to December 2010. Compared with [FOHBC, Civil War Message-in-a-bottle](https://fohbc.org/wp-content/uploads/2012/12/CivilWarMessageInABottle_MayJune2011.pdf) and [the museum's educator record](https://acwm.org/wp-content/uploads/ACWM_Vicksburg.pdf), which give inconsistent later dates. The specific curator account is used for opening; an exact decipherment year is omitted. Modern articles are copyrighted, no licence grant assumed: facts are summarized in original words, no article prose/images bundled. The 1863 dispatch itself is public domain. Raw PDFs/fetch record in `data/fix-*`.
- Mathematical changes: key counts are exact arithmetic on the stated hidden settings; coincidence is independently checked against a Python Counter oracle, 120 comparisons with maximum error 0. English percentages, glyph mappings and Enigma wirings retain their named original sources/licence/rights basis in the Manual and metadata.
- Unattended choice: use the source-confirmed publicity date rather than asking about the conflicting decipherment year. Curiosity voice and open exploration override lesson expectations throughout.

## Engine changes wanted

None. Shared kit, scripts and docs were not changed. All repairs are local to this tool.

## Audit

The required audit ran once, exited 0 in about 15 minutes and wrote `fix-audit/audit.md`: 252 raw leads. Its complete size/state/resize/Motion frames were viewed via `fix-audit-contacts/`. No full audit rerun was performed. Each new lead category is answered here:

- **Desktop ring height: confirmed and repaired.** The audit found 30 px rings. Final rings are 44 px at 1366x 768 and 1280x 720. A side transport at 1280 keeps the complete keyboard visible. `audit-repair-rotors-1366/1280` measured all three rings 44 px and keyboard/Run entirely inside the machine. Compact rings remain 32 px, intentionally listed below as an unresolved target-size limitation.
- **Phone plate size: confirmed and repaired.** 9 px became 10 px. The final two-line name stays inside its 48 px plate, with screws clear (`audit-repair-plate-phone`).
- **Bombe survivor shifted out of view: confirmed in the audit frames and repaired.** The new event line was added after the old scroll measurement. It now renders before positioning the survivor below the opaque header. Final 1366/680/375 captures all report `visible:true`, `hit:true`; at 680 the button is y 253 to 297, inside the panel ending 305 (`audit-repair-search-*`). Status stamps also receive a full-text title when space calls for an ellipsis.
- **Compact targets below 44 px: real, left open.** Rotor order/windows/rings, transport and typing keys are dense enough to fit the required previews. The full keyboard is visible and keyboard-operable, but this is not a 44 px-target pass. No target-size exemption or engine rule was invented to clear the audit.
- **Symbol/letter banks cut short: intended scrollable reference banks.** All 26 choices remain present, individually named and reachable by Tab; letter assignment also works from the focused key card. The banks retain 44 px targets. Their horizontal scrolling is visible in the compact frames; no missing choice is claimed as fixed by hiding it.
- **Wheel text hit under circles: SVG hit-test artefact.** Wheel lettering has pointer-events:none so dragging reaches the disk behind it. Viewed frames show its letters painted above the circles. Manual text/keep-region coverage is the intentional modal covering the bench, with Close focused.
- **Hint out of view: expected owned-hint states.** The compact wheel displays `#compact-hint`; the original `#hint` retains the text for Read but is not the painted copy there. After the first turn, the hint is deliberately gone; off Wheel it is not applicable. Compact held Read still begins with the hint. No welcome, goal or header was added to satisfy this lesson-shaped lead.
- **Sticky-header overlaps: clipped content behind an opaque header.** The referenced tool controls/axis labels scroll behind the header rather than paint through it. Viewed three-tool/weather frames confirm the header remains opaque. The actual candidate visibility issue is addressed above.
- **Welcome not heard after 12 first taps: Curiosity policy.** Taps which leave the wheel or remove its hint correctly suppress that line. There is no required lesson premise. The fresh Read and valid first-touch hint are retained. The audit's 27 one-click/Enter-twice rows have no errors or focus losses; all 10 five-click and 10 quick-tap checks are clean.
- **Motion/resize/errors: clean.** No infinite Motion-off animation, resize exception or newly stuck disabled control. Targeted follow-up: eight shots, zero console errors, zero HTTP(S) resource requests in the final bundle; allLines exactly matches the one-line voice file. These follow-ups verify the three local audit repairs, not another audit or a new lens pass.

Final bundle: 168,788 bytes, one offline HTML file. The two blockers are fixed. Should fix 6 remains NOT FIXED in full; the compact target-size limit and pending sensitivity review also prevent an unqualified exit/release PASS.

## Left open

- Should fix 6: strict sustained 60 fps under the worst tested 4x workload is not proved. Static reference drawing is repaired; slow frames remain.
- Compact rotor keys/ring controls are smaller than 44 px so the full instrument fits 680x 425 and 375x 812; desktop targets and keyboard access remain. Phone plate text is now 10 px after the audit repair. Do not describe these as a fully target-size-clean audit.
- Pending fresh sensitivity review, spec/map questions above, recorded gravel-ranger voice and physical Chromebook measurement are outside this repair's completed claims.
- The first phone-before capture targeted the host by mistake; it is explicitly not used as a before proof. Early temporary oversized nested chart glyphs were caught in viewed frames and repaired with explicit SVG viewport dimensions; `last-phone-labels` and `last-poe-sorted` verify that repair.
- No commits, uploads or deployment. `refine.md` and its review folder were left untouched. Final source is one offline file; automatic network code absent, em dashes 0. Lesson-word hits: score only means coincidence statistic, points only means geometric fixed points.
