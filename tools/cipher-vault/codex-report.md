# Codex report: cipher-vault (Curiosity No. 11)

## Built

Cipher Workbench is a single offline codebreaker's bench, not a lesson flow. Built in `S:\CurioClass-codex`; writes were confined to `tools/cipher-vault/` and `_scratch/cipher-vault/`. No commits, deployment, shared-engine edits or polish round.

Six machines: brass Caesar disk and Fan; standard and Leeson pigpen; 26-shape substitution and Poe's historical alphabet; Vigenere tableau; Enigma I with six orders of three rotors, rings, reflector B, double stepping and up to ten plugboard cables; additive pad with uniform random key generation.

Five analysis instruments: live frequency counter and movable English ghost; coincidence splitter and adjustable column ghosts; consecutive trigram gaps and factor counts; movable crib; cancellable exhaustive rotor search. Input/output selection, stacking via Swap, four case files, four practice sheets, twelve locally saved partner boxes, maker's plate, lower-left Manual and a separate Motion/Sound/Read power panel.

Source, metadata, notes, voice lines, audit states, art manifest and handoff are present. The generated `cipher-vault.html` bundles kit and material. Final bundle: 136,883 bytes (0.137 MB) against the 2 MB goal. SHA-256: c3d97e29f05fb7b8006e42b653edf53b7b97ba5b2d799a4ec6510ba4d4060330.

## The real material

Gathered and checked on **5 November 2026**. Raw evidence is in `_scratch/cipher-vault/data/`; `gather.py` and `pack.py` reproduce gathering and packing. No modern prose, photographs, corpus or third-party emulator code is imported into the instrument. Historical originals are used directly; modern history is paraphrased. No dataset is silently thinned.

- **Caesar:** [Suetonius, Julius 32 and 56, Loeb translation](https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Suetonius/12Caesars/Julius*.html), checked against Gutenberg 6400. Public-domain originals/translations. Sample: reported phrase and shift of three. The displayed ciphertext is a reconstruction, not a surviving message in Caesar's hand.
- **Leeson:** [Trinity's own burial record](https://registers.trinitywallstreet.org/churchyard/history.php?id=350) confirms the inscription and date. [Hemstreet, Nooks and Corners of Old New York](https://www.gutenberg.org/ebooks/39789), public domain in the USA, supplies the original key and inscription. Whole thirteen-letter text, code-redrawn. Actual three-grid variant, one/two/no dots, I/J sharing; the spec's standard two-grid/two-cross card would have been inaccurate for this stone. The initially mistaken book download was unused; correct primary HTML and key/inscription evidence are preserved separately.
- **Poe:** [Gutenberg 2147](https://www.gutenberg.org/ebooks/2147), public domain in the USA; checked against the [Poe Society's 1845 Tales transcription](https://eapoe.org/works/tales/goldbgb.htm). Whole cryptogram and original reading. `pack.py` asserts exact agreement with the printed cryptogram after normalizing its c-symbol to a drawn short rule. Forty-one-degree version, not the later twenty-one revision. No editorial prose copied. The historical key contains the letters actually used; New key returns the full 26-shape writing alphabet.
- **Vicksburg:** [museum curator's Message in a Bottle](https://acwm.org/wp-content/uploads/magazine_message_in_a_bottle_article.pdf), independently checked against the [2011 bottle-collectors account](https://fohbc.org/wp-content/uploads/2012/12/CivilWarMessageInABottle_MayJune2011.pdf). Whole 1863 original plaintext, public domain; contemporary article text/images excluded. Corrected to “I have sent some caps. I subjoin despatch from Gen. Johnston.” Ciphertext is regenerated using the owner-stated MANCHESTERBLUFF key, not copied from the damaged slip. Opening dated 2009, publicity 2010; attribution to Walker is probable. The broader reused-key claim was not independently confirmed and is not presented as a verified finding.
- **Rotors:** [Crypto Museum's wiring tables](https://www.cryptomuseum.com/crypto/enigma/wiring.htm), checked against the University of Amsterdam FEIOG construction/operation account. All three wirings, notches and reflector B are factual values; no licensed software or museum art copied. Raw museum HTML contains the actual wiring strings. The university download had a certificate error; its primary transcript was checked through the web tool.
- **1930 exclusion:** [Weierud's original-manual account](https://cryptocellar.org/enigma/e-message-1930.html) explicitly requires reflector A. The B-only instrument was tested with its published settings and does not reproduce it (output begins OGTGCTMMXEMRTGOSWWHM). Its case is omitted under the spec's explicit fallback, with an explanation in the case file and Manual.
- **English ghost:** [Norvig, Mayzner Revisited](https://norvig.com/mayzner.html). All 26 factual percentages from the spec, not the underlying corpus. No corpus licence was assumed and no corpus was imported. The ghost is a reference model, not a claim that all English follows those exact frequencies.
- **Practice:** four whole original Curio Class sheets from `fefed72e`: 296-letter counting text and shape key, 259-letter RAVEN text, 50-letter weather report, and the 21-letter pad with three keys/readings. Original owner material. No historical attribution. Ciphertexts, IC, gaps and crib letters are computed, not stored answers substituted into readouts.
- **Other history:** public-domain Suetonius Augustus 88 and Kerckhoffs 1883; Al-Kadi 1992 and Broemeling's statistical-history study (facts only, no article text); NSA/CIA Venona histories (US government works, public domain); Lasry/Biermann/Tomokiyo 2023 discovery facts checked against institutional and library accounts; Mary's trial/execution checked against National Library of Scotland and National Museums Scotland. Only original summaries are bundled. The Manual names the references and rights basis.
- **Mathematics and modern comparison:** exact combinatorics, computed IC/chi-square and pad ambiguity; Shannon's secrecy theorem paraphrased, no copyrighted paper text imported; [NIST FIPS 197](https://csrc.nist.gov/pubs/fips/197/final), US government public-domain specification, for AES facts. The pad's claim is explicitly limited to letter content: visible spacing is not hidden. Seal thresholds are labelled heuristics from the owner's synthetic sweeps, not universal security guarantees.

## Break the instrument

- Independent string-based Python oracle: standard vector `AAAAA -> BDZGO`; double step `ADU -> ADV -> AEW -> BFX`; weather ciphertext; all three pad readings; 100 randomized rotor vectors with varied orders, rings and 0-10 disjoint cables. Browser engine matched all 100 and was reciprocal.
- All six machines round-trip `HELLO, WORLD! 123`. Empty input works on all six; empty Vigenere key leaves the tape unchanged; ASCII case folding preserves non-ASCII characters. The 601st letter is rejected. A separate 6,000-character bound is disclosed in the Manual.
- RAVEN: IC average at period five `8.826546...`, displayed `8.8`; 23 consecutive trigram gaps, 20 divisible by five; THE SAME at offset 53 (one-based letter 54) gives ENRAVEN. Splitter's initial chi-square guess is RAVEN.
- Weather: 27 permissible crib placements. Search across one order gives only BOX at offset 10 (one-based position 11). Six-order search at the true spot tests 105,456 starts and leaves BOX, measured 249 ms. Final 27-spot run measured 54 ms. Selecting the survivor and pressing Run with real held clicks reproduces the whole weather plaintext.
- Ring pivot: frame review found a real SVG-origin defect. Initial rocking now has its own wrapper. All 26 shifts keep the inner/outer screen-space centers identical; laptop, 680x425 and 375x812 shift-three frames were checked after the fix. Real pointer drag and arrow keys produce THE DIE IS CAST.
- Rotor thumbwheels increment the visible window, not an earlier start setting. Actual held A key presses give BDZGO and STEP 0005. Plugboard connection, key display and ten-cable bound are implemented.
- Boxes: seal, open/match, twelve-box cap, persisted twelve-box reload and last tape; Peek/Delete modal confirmation, both cancellations and both confirmations. The peek mark survives a later match. Storage-blocked input still plays with a single status line.
- At 4x CPU throttle with 600 letters and Counter/Splitter/Repeats open: 121 sampled frame intervals, mean 16.6659 ms, maximum 16.8 ms. Fifty wheel-setting updates took 54.4 ms after avoiding unchanged chart rebuilds. This is local emulation, not measured school Chromebook hardware.
- Automated sustained walk: 600 seconds, 120 input sequences, no exceptions. No automatic remote requests in the browser trace; no remote assets in the bundle parser; no em dashes in tool files.

Evidence: `oracle.json`, `validation-results.json`, `final-results.json`, `integration-results.json`, `voice-final.json`, `rotor-thumbwheel-final.json`, `rotor-typing-final.json`, `play-log.json`, `static-results.json` and screenshot directories in Scratch.

## Voice walk

Only the first “Drag the inner ring.” hint is automatic, once per load; Read speaks the machine/setting, first 80 output characters and visible instruments' main readouts. This follows the Curiosity brief over the spec's event-speech list. There is no event praise or machine-by-machine welcome.

Held-click paths, two-second repeated taps and Read interruption were checked. The audit's rapid duplicate Wheel click cut was fixed: unchanged machine selections no longer hush speech, and the hint now uses the kit's one-time welcome machinery. Final two 0.7-second held taps logged one spoken hint without a cut. Focused symbol-bank letters assign glyphs; outside that input context, tool shortcuts and Encode still work. Focused rotor keycaps accept physical letter keys.

The bank target is gravel-ranger. No audio was recorded; actual narration is the kit's available device-voice fallback. Sound gates synthesized mechanical sounds and narration; Read still works independently. Motion uses the kit and stops rocking/drum animation without delaying results.

## Short test

This is an agent assessment from an anchor-grade perspective and an adult perspective, supported by actual interaction and a ten-minute automated walk. It is not a recruited child/adult study or a claim about measured month-long retention.

1. **Would a kid open it unassigned? Yes, plausibly:** a turn visibly changes a secret, with no introductory reading or gate. The phrase is its own payoff.
2. **Would an adult play for fun? Yes:** historically distinct alphabets, actual rotor/ring/cable behavior, distribution matching, period inference, exhaustive crib search and same-device partner messages offer substantial room for experiments.
3. **Is the real thing the interface? Yes:** working rings, exact glyphs/tableau, advancing wirings, live counts, gaps and hypotheses are the surface. No painted data or decorative answer picture.
4. **Does it work without a score or finish? Yes:** every case and practice sheet is available in any order; nothing depends on completion. Boxes are physical message containers, not a campaign.

![Workbench beside Elements Inspector](../../_scratch/cipher-vault/frame-comparison.png)

Compared with Elements Inspector's atom/spectrum density, this uses real brass/alphabet relationships and the same confidence in live material. Its intentional weakness is compact-view density: a short preview is useful for turning/reading, but detailed reference cards and multiple instruments need internal scrolling.

## Lesson creep check

Searched source and voice lines for every required term. All absent except two instances of **points**, both describing a reflector with no fixed points in the Manual. These are mathematical, not rewards. No score, goal, room order, lock ladder, sticker book, timer, quiz, finish screen, mode pills or kit header was retained. Original PAD tails remain only because the revised spec explicitly asks for the exact practice texts.

## Done when

| Spec item | Result | Evidence |
|---|---|---|
| 1. First two minutes; shift three | PASS | Real drag, arrow-key path, exact output and final concentric ring frames. |
| 2. Six machines; rotor vectors; 1930 fallback | PASS | Six round trips, 100 independent rotor vectors, physical BDZGO typing and double step. 1930 case explicitly dropped as permitted. |
| 3. Checked numbers, crib search and pad keys | PASS | Independent oracle, rendered 8.8/20-of-23/ENRAVEN; 27 spots; BOX survivor; all three pad readings. |
| 4. All cases/sheets accessible | PASS with permitted exclusion | Four verified cases and all four sheets; incompatible 1930 case openly omitted under the later checking instruction. No locks or completion marks. |
| 5. Boxes, confirmations, cap, reload, blocked storage | PASS | Real confirmation path plus matching/persistence/cap/blocked-storage assertions. |
| 6. Machine and tapes stay in view at three required sizes | PASS | Full audit size sweep and final targeted phone/preview/laptop frames; phone scrollWidth 375. Internal panels may scroll. |
| 7. Performance, keyboard and Read | FAIL for full certification | Local 4x frame/search timing and keyboard/Read checks pass. Actual Chromebook hardware unmeasured; compact controls do not universally meet the 44 px convention and some main controls require internal scrolling. |
| 8. No lesson progression or reward layer | PASS | Source/voice search and frame inspection. |
| 9. Short test, comparison, console/network/dashes | PASS with stated scope | Agent assessment and ten-minute walk; comparison frame; browser traces clean; single offline bundle; zero em dashes. |

## Audit leads

The single required audit completed: **356 raw snapshot leads**, including 332 repeated small-target entries, two scroll-panel entries, one plate/status overlap, ten small-text entries, five hidden SVG-text entries, five hint entries and one rapid-click speech cut. No audit rerun or polish round.

Every category is answered in `_scratch/cipher-vault/audit-response.md`. Subsequent build fixes cover desktop target sizes, plate/status sizing/layout, glyph axis type, the actual SVG pivot defect, visible phone rotor transport and rapid duplicate-selection speech. The audit's empty/hidden wheel hint is intentional under this brief. Remaining compact targets and panel scrolling are real limits, not claimed clean. Audit Motion-off and resize stress checks had no exceptions or stuck controls. All 27 default held-click paths retained focus.

## Frames looked at

All four model frames; all first/core/validation frames; all 26 audit frames on five contact sheets, with problem regions separately inspected; final phone/wheel/rotor/bombe/plugboard/grayscale frames; the five sustained-walk frames; latest substitution and front frames; final integration frame. Scratch contains originals, labelled sheets and the side-by-side comparison. Earlier defective wheel frames are preserved as evidence; final wheel frames supersede them.

## Art made

No painted images. Exact SVG brass geometry and lettering, 26 substitution shapes, two pigpen families, tableau, counts and diagrams; CSS paper, wood, lampboard, sockets, drums and engraved plate. `art/prompts.json` records the code-only decision; no placeholders, people, downloaded artwork or image-generation claims.

## Engine changes wanted

None required. A bank-voice selector without recorded clips would improve fidelity to gravel-ranger, but this build does not edit the kit or record audio.

## Left open

- Compact preview/phone targets below 44 px and small reference-card type. Counter ghost fader, multiple analyzers and short-preview rotor controls can require internal scrolling. Keyboard equivalents remain available. A future review must judge these honestly; no polish round was started here.
- Actual school Chromebook hardware performance and independent human short-test research were not available unattended.
- Exact gravel-ranger recording, persistent lamp hum and a richer spring timbre are not bundled. Existing sounds are synthesized ticks, rotor clicks, bombe whirr, seal thump and box tone.
- The 1930 reflector-A example is omitted, not replaced by invented historical material. Kahn's broader reused-Confederate-key claim and additional unconfirmed historical details were not promoted to verified findings.
- Native/hard-history sensitivity still needs the normal fresh cold review before any live push. No live push occurs in this build.
- Open questions followed their stated lean: keep REMEMBER DEATH, state Mary's 1587 execution plainly, add no case read mark, retain the initially disconnected plugboard. No user answer was required.
- The user-required stop-on-report rule overrides the regular brief's instruction to start the report early. This report is written last; no work follows its creation.
