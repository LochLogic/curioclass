# Cipher Vault: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: cipher-vault (Curiosity No. 11)

#### Built

Cipher Workbench is a single offline codebreaker's bench, not a lesson flow. Built in `S:\CurioClass-codex`; writes were confined to `tools/cipher-vault/` and `_scratch/cipher-vault/`. No commits, deployment, shared-engine edits or polish round.

Six machines: brass Caesar disk and Fan; standard and Leeson pigpen; 26-shape substitution and Poe's historical alphabet; Vigenere tableau; Enigma I with six orders of three rotors, rings, reflector B, double stepping and up to ten plugboard cables; additive pad with uniform random key generation.

Five analysis instruments: live frequency counter and movable English ghost; coincidence splitter and adjustable column ghosts; consecutive trigram gaps and factor counts; movable crib; cancellable exhaustive rotor search. Input/output selection, stacking via Swap, four case files, four practice sheets, twelve locally saved partner boxes, maker's plate, lower-left Manual and a separate Motion/Sound/Read power panel.

Source, metadata, notes, voice lines, audit states, art manifest and handoff are present. The generated `cipher-vault.html` bundles kit and material. Final bundle: 136,883 bytes (0.137 MB) against the 2 MB goal. SHA-256: c3d97e29f05fb7b8006e42b653edf53b7b97ba5b2d799a4ec6510ba4d4060330.

#### The real material

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

#### Break the instrument

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

#### Voice walk

Only the first “Drag the inner ring.” hint is automatic, once per load; Read speaks the machine/setting, first 80 output characters and visible instruments' main readouts. This follows the Curiosity brief over the spec's event-speech list. There is no event praise or machine-by-machine welcome.

Held-click paths, two-second repeated taps and Read interruption were checked. The audit's rapid duplicate Wheel click cut was fixed: unchanged machine selections no longer hush speech, and the hint now uses the kit's one-time welcome machinery. Final two 0.7-second held taps logged one spoken hint without a cut. Focused symbol-bank letters assign glyphs; outside that input context, tool shortcuts and Encode still work. Focused rotor keycaps accept physical letter keys.

The bank target is gravel-ranger. No audio was recorded; actual narration is the kit's available device-voice fallback. Sound gates synthesized mechanical sounds and narration; Read still works independently. Motion uses the kit and stops rocking/drum animation without delaying results.

#### Short test

This is an agent assessment from an anchor-grade perspective and an adult perspective, supported by actual interaction and a ten-minute automated walk. It is not a recruited child/adult study or a claim about measured month-long retention.

1. **Would a kid open it unassigned? Yes, plausibly:** a turn visibly changes a secret, with no introductory reading or gate. The phrase is its own payoff.
2. **Would an adult play for fun? Yes:** historically distinct alphabets, actual rotor/ring/cable behavior, distribution matching, period inference, exhaustive crib search and same-device partner messages offer substantial room for experiments.
3. **Is the real thing the interface? Yes:** working rings, exact glyphs/tableau, advancing wirings, live counts, gaps and hypotheses are the surface. No painted data or decorative answer picture.
4. **Does it work without a score or finish? Yes:** every case and practice sheet is available in any order; nothing depends on completion. Boxes are physical message containers, not a campaign.

![Workbench beside Elements Inspector](../../_scratch/cipher-vault/frame-comparison.png)

Compared with Elements Inspector's atom/spectrum density, this uses real brass/alphabet relationships and the same confidence in live material. Its intentional weakness is compact-view density: a short preview is useful for turning/reading, but detailed reference cards and multiple instruments need internal scrolling.

#### Lesson creep check

Searched source and voice lines for every required term. All absent except two instances of **points**, both describing a reflector with no fixed points in the Manual. These are mathematical, not rewards. No score, goal, room order, lock ladder, sticker book, timer, quiz, finish screen, mode pills or kit header was retained. Original PAD tails remain only because the revised spec explicitly asks for the exact practice texts.

#### Done when

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

#### Audit leads

The single required audit completed: **356 raw snapshot leads**, including 332 repeated small-target entries, two scroll-panel entries, one plate/status overlap, ten small-text entries, five hidden SVG-text entries, five hint entries and one rapid-click speech cut. No audit rerun or polish round.

Every category is answered in `_scratch/cipher-vault/audit-response.md`. Subsequent build fixes cover desktop target sizes, plate/status sizing/layout, glyph axis type, the actual SVG pivot defect, visible phone rotor transport and rapid duplicate-selection speech. The audit's empty/hidden wheel hint is intentional under this brief. Remaining compact targets and panel scrolling are real limits, not claimed clean. Audit Motion-off and resize stress checks had no exceptions or stuck controls. All 27 default held-click paths retained focus.

#### Frames looked at

All four model frames; all first/core/validation frames; all 26 audit frames on five contact sheets, with problem regions separately inspected; final phone/wheel/rotor/bombe/plugboard/grayscale frames; the five sustained-walk frames; latest substitution and front frames; final integration frame. Scratch contains originals, labelled sheets and the side-by-side comparison. Earlier defective wheel frames are preserved as evidence; final wheel frames supersede them.

#### Art made

No painted images. Exact SVG brass geometry and lettering, 26 substitution shapes, two pigpen families, tableau, counts and diagrams; CSS paper, wood, lampboard, sockets, drums and engraved plate. `art/prompts.json` records the code-only decision; no placeholders, people, downloaded artwork or image-generation claims.

#### Engine changes wanted

None required. A bank-voice selector without recorded clips would improve fidelity to gravel-ranger, but this build does not edit the kit or record audio.

#### Left open

- Compact preview/phone targets below 44 px and small reference-card type. Counter ghost fader, multiple analyzers and short-preview rotor controls can require internal scrolling. Keyboard equivalents remain available. A future review must judge these honestly; no polish round was started here.
- Actual school Chromebook hardware performance and independent human short-test research were not available unattended.
- Exact gravel-ranger recording, persistent lamp hum and a richer spring timbre are not bundled. Existing sounds are synthesized ticks, rotor clicks, bombe whirr, seal thump and box tone.
- The 1930 reflector-A example is omitted, not replaced by invented historical material. Kahn's broader reused-Confederate-key claim and additional unconfirmed historical details were not promoted to verified findings.
- Native/hard-history sensitivity still needs the normal fresh cold review before any live push. No live push occurs in this build.
- Open questions followed their stated lean: keep REMEMBER DEATH, state Mary's 1587 execution plainly, add no case read mark, retain the initially disconnected plugboard. No user answer was required.
- The user-required stop-on-report rule overrides the regular brief's instruction to start the report early. This report is written last; no work follows its creation.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: cipher-vault
#### Played
Cold opening and all six machines before builder notes; Grade 7 and adult perspectives. Shift-three English is a strong immediate reward. Four historical cases and four practice sheets opened freely. A separate 602.3-second, 120-sequence sustained walk had no exceptions. This is an agent assessment, not a recruited child/adult study.
#### Findings fixed
- **Blocker, general, numeric controls:** fractional rotor rings printed `undefined`; fractional splitter periods created malformed columns. Round/clamp live and saved settings; empty and out-of-range values stay usable.
- **Blocker, general, analysis state:** old bombe survivors survived case changes; keyboard and cable edits could leave stale candidates. Invalidate on relevant changes; Output searches transfer their actual source to Input before Run.
- **Blocker, general, seal estimates:** short pads counted full-length key spaces, empty keys implied encryption, and symbol ciphertext appeared too short because its glyphs were not counted. Count effective key letters/glyphs; show empty-key identity, actual Poe mapping count, and fixed-ring/cable assumptions beside the estimate.
- **Should fix, general, readouts:** Input count depended on Tools read; an empty rotor crib claimed no collision. Count the input independently and state insufficient text honestly.
- **Should fix, general, stale rotor output:** settings changed without labelling old output; subsequent typing could use the old session. Mark PRESS RUN and reset the typing session.
- **Should fix, general, access/layout:** undersized compact controls, hidden newly opened analyzers, tiny tableau, redraw focus losses. Restore 44 px targets, reveal the chosen tool, retain symbol/factor focus, pin rotor transport and fit three draggable, announced window drums. Keep the source selector visible and keyboard search results focused. At 600 letters, keep the tape limit and first counter label readable.
- **Polish accepted, general, flat square:** enlarged the actual key-row/plain-column/cipher crossing; the reference square keeps legible letters and follows that crossing. Counter coordinates and collision-free labels now follow actual pixels. Kept the brass, tapes, lampboard, glyphs, cases and open structure.
- **Should fix, general, provenance:** name the owner-material CC BY 4.0/code MIT licences, link Hemstreet's primary record, qualify practice prose as illustrative, and name sensitive history in teacher notes.
#### Findings left
No known blocker or should-fix left. Physical Chromebook certification and the requested recorded voice remain unavailable; scope and evidence are below.
#### Break it
No score, quiz, pass gate or campaign meter exists. Sweeping all wheel settings and Fan is the intended instrument, not a cheat.
52/52 targeted browser checks plus 100 independent string-oracle rotor vectors passed. `AAAAA → BDZGO`; `ADU → ADV → AEW → BFX`; all six machines round-trip punctuation and digits and accept empty input.
Tried ±999, fractional and empty numeric fields; ghost and column offsets 0/25; 26-notch wraps; empty/40-letter square keys; 600/601-letter tapes; random and repeated pads; rapid input; sorting and analysis-source switches.
Tried stale case/search candidates, search on Output, resize while searching, Stop, cable edits, ten/eleven cables, survivor selection and Run. The weather search leaves BOX over 27 crib spots; six orders test 105,456 starts (260 ms in the targeted local run).
Tried twelve/thirteen boxes, matching output, Peek/Delete cancellation and confirmation, reload, and blocked storage. They behaved as labelled. The saved tape survived reload; blocked storage still decodes and shows one status line.
Real pointer drag gives wheel shift three and THE DIE IS CAST. Real window drag gives AAD; Up/Down wraps to Z with focus and announced value retained.
At 4x CPU throttle, 120 local frame intervals averaged 16.94 ms with one 50 ms maximum. This supports smooth local use, not a strict all-frame 60 fps or school-hardware certification.
Evidence: `review-final-core.json`, `review-oracle.json`, `review-seal-results.json`, `review-stress.json`, `review-drag.json`, `review-window-*.json` in Scratch.
#### Voice walk
Sound on, held clicks, two-second gaps: five wheel notches, Read, Square, Read, Rotors, Read, Sound off, Read. No machine welcome or event praise was added: the Curiosity brief permits the first hint once, then Read only.
| Line | Expected | Logged |
|---|---|---|
| Drag the inner ring. | Once | 1 spoken |
| Wheel, shift/output/counter | Read press | 1 read |
| Square, key/output/counter | Read press | 1 read |
| Rotors, windows/output/counter | Read presses, including Sound off | 2 reads |
`review-voice.json` contains the exact sequence. The device speech fallback is used; gravel-ranger is a target bank voice, not a claimed recording. Changing rotor settings now makes Read name the pending Run before the prior output.
#### Facts checked
Checked 5 November 2026; complete named URLs, rights bases and independent checks are in `review-facts.json`, the Manual and `tool.draft.json`. Contemporary prose, photographs and corpora are excluded; the historical originals are whole, not sampled.
| Material or claim | Named source and rights basis |
|---|---|
| Caesar method/phrase; Augustus next-letter/AA variant | Suetonius Julius 32/56 and Augustus 88, public-domain Loeb; Gutenberg 6400 independent translation. Modern A-Z reconstruction is explicit. |
| Leeson, 1794, REMEMBER DEATH and three-grid key | Trinity burial record plus Hemstreet 1899, [Gutenberg 39789](https://www.gutenberg.org/ebooks/39789), public domain in USA; no Trinity prose copied. |
| Poe, 1843; complete 203-glyph, forty-one-degree cipher | [Gutenberg 2147](https://www.gutenberg.org/ebooks/2147), public domain in USA, and Poe Society's 1845 Tales; reconstructed cipher exactly matches the bundled original. |
| Vicksburg text/date/probable Walker attribution; 2009 opening/2010 publicity | [Catherine M. Wright, museum curator](https://acwm.org/wp-content/uploads/magazine_message_in_a_bottle_article.pdf), checked against FOHBC 2011. Only the public-domain 1863 dispatch is reused; ciphertext is recomputed. |
| Surrender and slavery context | National Park Service, July 4, 1863: Slavery Ends in Vicksburg; Smithsonian National Museum of American History, Battle of Vicksburg. Government factual history, original summary. |
| Three wirings, B, notches, double step, never-self property | [Crypto Museum wiring](https://www.cryptomuseum.com/crypto/enigma/wiring.htm), David Hamer rotor table and National Museum of Computing. Factual values only; no museum software/art/prose copied. |
| 1930 exclusion | [Frode Weierud's original-manual account](https://cryptocellar.org/enigma/e-message-1930.html) requires A. The B-only machine cannot reproduce it; retained the permitted omission. |
| English ghost | [Peter Norvig, Mayzner Revisited](https://norvig.com/mayzner.html): all 26 factual percentages. No corpus bundled or corpus licence claimed. |
| Al-Kindi, ninth century, oldest known description | Broemeling, The American Statistician 65(4), 2011, DOI 10.1198/tas.2011.10191; University of Nizwa historical account. Facts paraphrased, no article text imported. |
| Kerckhoffs/key secrecy | La cryptographie militaire (1883), second desideratum, public-domain original hosted by Petitcolas. |
| Venona duplicated pads | NSA overview and CIA Venona introduction/chronology, US government public-domain histories. |
| Mary: 57 letters, dates, authors, separate trial evidence | Lasry/Biermann/Tomokiyo 2023 DOI 10.1080/01611194.2022.2160677 and American Technion Society; NLS last letter, Inner Temple original brief and Folger for 1586/1587. Original factual summaries only. |
| Pad conditions/AES | Shannon 1949 theorem, paraphrased; NSA/CIA; NIST FIPS 197, public domain. Modern protection is not claimed for these machines. |
| Practice material/math | Whole owner sheets, CC BY 4.0 under repository content licence; code MIT. Independent computation: 296/259/50/21 letters; IC 8.826546 → 8.8, 20/23 gaps, ENRAVEN at offset 53, all three pad keys, 26!, 26!/6!, 26^n, 6×26³. |
Practice padding tails are retained because the brief requires exact original sheets. Their prose is explicitly illustrative: counting and gaps suggest candidates, never guarantee arbitrary-message recovery.
#### Sensitivity
Retained the brief's leans: REMEMBER DEATH without gore; Mary's 1587 execution stated plainly; no read/completion marks; plugboard initially disconnected. Vicksburg names slavery and leaves Walker attribution probable. Poe's racist character dialogue is not reproduced. Al-Kindi is credited; oldest known is qualified. A cultural reviewer should examine these historical framings and non-European attribution; no people art is used.
#### Short test
1. **Unassigned kid? Yes, plausibly.** A drag makes readable English within seconds, then personal messages and cases are freely available.
2. **Adult fun? Yes.** Real ring/cable behavior, ambiguous pads and hypothesis-driven analysis offer genuine depth.
3. **Real material is the interface? Yes after fixes.** The square's actual crossing, readable reference letters, live counts, glyphs, drums and tapes carry the action.
4. **Works without score/finish? Yes.** Nothing is locked or marked done; the readable material is the reaction.
![Own frame beside Elements Inspector](../../_scratch/cipher-vault/review-evidence-frames/review-comparison.png)
This comparison is about material and density, not copying the older tool's header. Source/voice lesson-creep search found only “fixed points,” a mathematical reflector property; no reward terminology or em dashes.
#### Flattest moment left
An empty pad strip is quiet until there is a tape and key. The weakest active moment, the tiny square with a small changing formula, was lifted using the actual crossing rather than a game layer. Compact reference/key banks still scroll locally.
#### Graphics
All six code-drawn machines and cases inspected at final sizes; no painted assets, people or placeholders. Preserved brass shading, paper, glyph geometry, lamps, wood and drums. Viewed all 38 audit PNGs on seven contact sheets and inspected affected states at full size; 13 targeted post-repair frames and the final 600-letter frame verify the repairs.
Final standalone bundle: 152,078 bytes, no remote assets or external CSS. SHA-256: `2e38cfe8688dc8242d6e37a827999591a40869ebadd6afa334da414f2244e841`. Measured text contrasts range from 6.35:1 to 13.32:1.
#### Audit
One bounded full audit completed in 844.0 seconds with exit 0, Chrome 9951 and host 8755, using a Scratch profile. Its 88 raw leads remain preserved in `review-audit/`; they are not presented as a clean mechanical audit. No full rerun was made.
Confirmed and repaired: compact tape/crib targets, zero-font label, analysis source visibility, primary Use key/result access and wrapped footer. Targeted final geometry checks show visible measured controls at least 44 px, no horizontal page overflow and readable labels. The final 600-letter check retains 46/44 px input/output tapes and the complete counter label.
Rejected with evidence: 32 SVG/modal hit-test leads describe visible engraved text or the intentional Manual overlay; retired first hints and absent lesson welcomes obey the Curiosity brief; complete key/reference banks intentionally scroll locally. Exact grouping and reasons: `review-audit-response.md`.
No exceptions or stuck controls in audit resize stress; no infinite Motion-off animation. All 27 default held-click paths retained focus and survived Enter twice; repeated/rapid speaking controls were clean. Final port check confirms 8755 and 9950-9957 closed.
#### Done when
Spec 1-5 and 8 pass with the explicit permitted 1930 omission. Spec 6 and keyboard/Read portions of 7 were checked at all standard sizes including the phone iframe; main controls and tapes stay on the bench, long reference banks scroll locally.
#### Left open
Strict all-frame 60 fps / real Chromebook performance remains unverified; the local throttle measurement is reported above. Spec 9 passes as an agent short-test assessment with frame comparison and no remote runtime request.
No commits, publication, shared-code edits or new topics. Work stayed in the authorized root and two folders; a failed Chrome startup probe requested a temporary external profile, verified absent, with no file written there. Final report creation is the last work action, as the user's stop rule requires.

<!-- end part -->

## Refine

<!-- part: refine.md -->

OPEN (round 1, Claude Refine 2026-11-06; Codex fixes next)
Counts: blockers 2 (general 1, family 1), should fix 19 (general 10, family 9), polish accepted 18

### Refine: cipher-vault

Merged from `refine/teaching.md`, `refine/play.md`, `refine/craft.md` (round 1, 2026-11-06). Judged as a Curiosity
(CODEX-CURIOSITY.md, BASELINE). Frames: Teaching `S:/CurioClass-codex-scratch/cipher-vault/teaching/`, Play
`.../cipher-vault/play/frames/`, Craft `.../cipher-vault/craft/`, shared audit `.../cipher-vault/audit-r1/`.
Integrator spot-checks: src.html 921-931, 1037-1045, 1062-1089, 1260-1450, 1687-1694 read; both blockers confirmed in
code. No sensitivity.md yet: the sensitivity items below go to the fresh-agent review.

#### Blocker
1. **Encode toggle prints a sealed box's key and turns sheets into answer keys.** src.html:924-926 (`renderSymbols`:
   in Encode every glyph is labelled with `encoderLetter`, from `state.symbolKey` or `MATERIAL.poeKey`), 1427-1450
   (`openBox` never replaces `state.symbolKey`, so the sealer's key is still loaded), 1687-1694 (`#direction`, also key
   E). A partner opening a sealed Symbols box presses E once and the key card shows the sealer's letter under every
   glyph; the same press labels all 26 glyphs of the counting sheet and Poe's whole key on the Gold-Bug. It is not
   recorded as a Peek, so the shelf still says "sealed" or "open" as if earned. Seen: Teaching gv.json `symbox-encode`
   (card read `DXWAGOKEUSZQHPBMCLNJITVFRY`), `teaching/frames/counting-encode.png`. Fixed looks like: while a box, the
   counting sheet or the Gold-Bug is on the bench, Encode never shows the hidden key (switch the card to a fresh key for
   the student's own writing, or treat the switch as a Peek and mark the box "peeked"); `openBox` loads the box's own
   symbol key instead of relying on what happens to be in state. Wheel, Square and Pad boxes already reset their keys;
   check Grid and Rotors give nothing away the same way (Rotors: see should fix 4). (general)
2. **Glyph counter bars are labelled by key-card position, so Poe's digit glyphs are mislabelled.** src.html:1043-1044
   (`barChart`: any non-letter bar gets `${i+1}`), 1066-1067 (aria "glyph N"). Poe's alphabet is digits and marks, so
   the position numbers read as glyphs: the tallest bar (33, glyph `8`) is labelled **5**, and glyph `5` occurs 12
   times. Sorted puts "5" on the top bar. The spec's own path (Things to do 4: count the symbols, guess E) leads the
   student to assign E to the wrong symbol, and every later guess builds on it. On the counting sheet the numbers 1 to
   26 match nothing on the key card, so the frequency attack needs an undocumented bar click. Seen: Play
   `play/frames/d08-case-poe.png`, `p02-poe-sorted.png`; Teaching `teaching/frames/poe-loaded.png`,
   `counting-loaded.png`. Counts themselves are right (8:33, ;:26, 4:19, ‡ and ) 16, *:13, 5:12, 6:11 match Poe).
   Fixed looks like: draw each glyph under its bar with `glyphSVG` (as the key card does), on every bar or at least on
   every labelled bar, for Poe and the drawn shapes alike; aria names the glyph (Poe's character, or "symbol N" matching
   the card's own label). (family:curiosity)

#### Should fix
1. **RAVEN and Vicksburg open already solved.** src.html:1330-1339 (RAVEN: `split = 5`, crib THE SAME at `offset = 53`,
   three tools open), 1299-1307 (Vicksburg: PEMBERTON at `offset = 4`), 1083 (`colGhosts = cols.map(guessShift)`).
   RAVEN loads with `KEY GUESS RAVEN`, a `Use key` button, length 5 lit and the crib reading ENRAVEN; two clicks decode
   it. Vicksburg loads with `IMPLIED KEY HESTERBLU` while its card says "Slide the crib PEMBERTON". Things to do 6 and 7
   never happen; the finding is handed over before the first move. Seen: Teaching `frames/raven-loaded.png`,
   `frames/wheel3.png`, checks.json `vicksburg`; Play `d11-sheet-raven.png`, `d11b`, `d09-case-vicksburg.png`. Fixed:
   open RAVEN at length 1, offset 0, no key guess shown until the student picks a length; open Vicksburg with the crib
   at offset 0. The checked numbers (8.8 at 5, 20 of 23, ENRAVEN at 53, HESTERBLU) must still appear when the student
   gets there (Done when 3). Weather sheet: see Settled calls. (family:curiosity)
2. **Splitter offers a key guess from 2 or 3 letters per column.** src.html:1083-1087. On the 12-letter default tape at
   length 5 it shows "BUMPINESS 0.0 AT LENGTH 5", "KEY GUESS DSDND" and `Use key`, while the Counter beside it says "Too
   few letters". An estimate whose assumption (enough letters per column) does not hold; a partner cracking a short box
   gets a confident wrong key. Seen: `audit-r1/state-three-tools-1366x768.png`, Craft 7. Fixed: under 10 letters per
   column (the threshold the seal card already uses, src.html:1387) show "Too few letters per column" in place of the
   key guess and no `Use key`; an empty tape says "No letters" rather than "BUMPINESS 0.0" (Play nit, `p14`).
   Weighed as should fix, not blocker: the guess is the best fit on the data and `Use key` shows nonsense at once, so it
   does not lead work silently astray the way blocker 2 does; it still needs the guard. (family:curiosity)
3. **Sealing leaves the secret on the bench.** src.html:1409-1422 (`sealBox`). After Seal the input tape still reads
   MEET AT THE OAK and the wheel still shows SHIFT 07 under "Sealed · hand this device to your partner". Seen: Play
   `d20-sealed-then-shelf.png`. Fixed: on Seal, clear the tapes and reset the machine to its zero setting (or put the
   box's cipher on the tape), so the bench is safe to hand over. (family:curiosity)
4. **Rotor box key count overstates the search six times and ignores the plugboard.** src.html:1389-1391
   (`1.05456 × 10^5`, "six rotor orders"), 1439-1441 (`openBox` hands the partner the sealer's order, rings and plugs;
   only the start is reset). The real search is 17,576 starts; with plugs set the bombe is silently off but the card
   still claims a count. Seen: Teaching gv.json `rotorbox` (sealed III I II, rings 5 6 7, start H I J; opened with the
   same order and rings, start AAA). Fixed: either hide order, rings and plugs on open and count what is hidden, or
   keep handing them over and count 17,576 with the plugboard line stated plainly. Card and box must agree. (general)
5. **Switching to Encode wipes a glyph tape with no way back.** src.html:1690
   (`if (!state.decode && /[\uE000-\uE0FF]/.test(state.input)) state.input = ''`). One stray E on the counting sheet or
   the Gold-Bug loses the 296- or 203-glyph tape; toggling back leaves it empty, and re-opening the sheet clears every
   assigned letter. Status says nothing. Seen: Teaching `counting-encode` (`input: 0`). Fixed: keep the glyph tape and
   the assigned letters and restore them on the way back to Decode (blocker 1's fix can share this). (general)
6. **Square tableau is rebuilt on every update and misses 60 fps at 4x.** src.html:943-967 (`renderTableau` rewrites
   729 SVG text nodes and forces two layouts per `update()`). 600-letter tape, three tools: 31 ms per update at 4x,
   median 50 ms frames (20 fps), 40 ms keystroke latency; every other machine is under 1 ms. Done when 7 fails for this
   machine. Seen: Craft `perf`, `perf2` probes. Fixed: draw the 26 by 26 letters once; move only the highlight rects
   and the chosen-letter fill. (general)
7. **Rotor keyboard is below the fold at 680x425 and 375x812.** Rotors page, `.machine`. Only a sliver of the lamp row
   shows; the 26 typing keys need a scroll inside the machine (Done when 6; Things to do 8). Seen:
   `audit-r1/state-rotors-680x425.png`, `state-rotors-375x812.png`, `state-weather-search-680x425.png` (Play 7,
   Craft 6). Fixed: in short boxes give the lampboard and keys the height; put Run, Set back, Plugboard and ring fields
   in one compact row. (general)
8. **Symbol cracking: the guessed letters cannot be read against the cipher.** Symbols decode (Poe, counting sheet):
   `.tape-face` and `#output` are separate tapes. After E, T, H the output is `...THE...H...H..TE...` with the glyph
   beside THE on another tape, 21 of 203 glyphs per row and no scroll cue (scrollHeight 448 vs 62 visible). Seen: Play
   `p01-poe-ETH.png`, `d10-sheet-counting.png`. Fixed: under Symbols and Grid decode, show stacked pairs (glyph over its
   letter or a dot), as the crib tape already does, with whole rows and a scroll cue. (family:curiosity)
9. **Tools read Input by default, so the machine never moves the bars.** src.html:633 (`toolsRead:'input'`). In Encode,
   turning the wheel or growing the Square key changes only the output; the Counter, Splitter and Repeats sit still, so
   Things to do 5 ("watch the bars flatten as the key grows") and found item 1 are invisible. Seen: Play
   `d24-square-key.png`. Fixed: tools read the ciphertext side by default (input in Decode, output in Encode), with the
   select as an override. (family:curiosity)
10. **The English ghost silently freezes on ordinary pasted text.** src.html:1074 (ghost disabled unless the tape is
    only `[A-Z\s.,'!:;?\-]`). One digit, double quote, parenthesis or curly apostrophe disables the fader and chart drag
    with no message, and the ghost stays drawn at its old offset. Things to do 2 ("paste a paragraph") hits this every
    time. Seen: Teaching g2.json `ghost-digit`, `ghost-curly`. Fixed: the ghost works on the letters already counted;
    disable it only in Sorted (see polish 4) and on Symbols/Grid tapes. (general)
11. **Vicksburg date is wrong against its cited source.** src.html:1268 ("The museum dates opening to 2009"). The cited
    American Civil War Museum article (Catherine M. Wright) says the conservator opened the bottle and removed the
    message in December 2008; only the photograph reached the museum in January 2009. Fixed: "The bottle was opened in
    December 2008; the message was read in 2010." Check notes.md and tool.draft.json for the same date. (general)
12. **Read never speaks the first-run hint.** src.html:1627-1633 (`readText`), `hint:false` on `Curio.voice`. A fresh
    Read says machine, setting and output but never "Drag the inner ring."; CODEX-CURIOSITY says the hint is spoken once,
    then when Read is pressed. Seen: audit one-click row 4, Craft `voice_soundoff_read`. Fixed: while `#hint` shows,
    Read speaks it first. (family:curiosity)
13. **The hint is spoken after its moment has passed.** src.html:1636-1637 (`welcome` on any first tap on the Wheel),
    911 (`setShift` clears `#hint`). A first drag or Right press clears the hint, then "Drag the inner ring." plays
    (1325 ms after three Right presses already reading THE DIE IS CAST). Seen: Craft vlog,
    `craft/wheel-dragged-cw.png`. Fixed: the line's `valid` is "the hint is still showing". (family:curiosity)
14. **The hint runs over the inner ring's letters at compact sizes.** src.html:415 (`#hint { font-size:30px }` in the
    compact query), 520. At 680x425, 800x500 and 1000x625 "Drag the inner ring." is wider than the hub and sits on the
    D and J; the disk is about 155 px with 7 px letters at 680x425. Seen: `audit-r1/size-680x425.png`,
    `size-1000x625.png`, `craft/zoom-hint-680.png`, `play/frames/zoom-680-hint.png` (Play 8, Craft 4). Fixed: keep the
    hint inside the hub at every size (smaller, or two lines) and give the disk more of the compact height. (general)
15. **Counter and tape disagree on Grid and Symbols.** src.html:1069. With a letter tape the Counter reads "LETTERS 0 ·
    Too few letters" on a 1 to 26 axis while the tape says "12 LETTERS". Seen: `audit-r1/state-grid-1366x768.png`,
    `state-symbols-680x425.png`. Fixed: say what was counted ("SYMBOLS 0 · the tape holds letters") or count what the
    tape holds. (family:curiosity)
16. **Rotors opens with its windows at A A M, not A A A.** `update()` leaves `state.positions` at the end of the default
    tape. Typing AAAAA gives BTMCD while the Manual says AAAAA becomes BDZGO. Seen: Play `d22-rotors-type.png`. Fixed:
    on arrival the windows show the start setting (or a "START AAA" readout beside STEP), so the first press matches the
    Manual. (family:curiosity)
17. **Letter keys act as shortcuts while a student types on Rotors.** document keydown, src.html:2014 onward. Typing
    HELLO after clicking the Rotors button flips to Encode (E) and opens the Case file (O); on the wheel W replaces the
    input tape with no undo. Seen: Play `p04`, `p05`. Fixed: on Rotors, letter keys press the machine whenever no text
    field has focus (shortcuts there stay on digits and Escape); Swap gets an undo (one step back to the previous tape).
    Rebinding the spec's letter shortcuts elsewhere is under open questions. (general)
18. **Status still says "press Run tape" after Run.** src.html:1868 (survivor click); `runRotors()` never updates the
    status. Seen: Play `d14-weather-survivor-run.png`. Fixed: Run sets a status that matches the state. (general)
19. **Manual and seal card read at a college level for a band that starts at grade 5.** `showManual()` src.html:
    1581-1626, `keyCount()` 1374-1398, `showSeal()`, notes.md "Key skills": "arithmetic mean of the columns' indices of
    coincidence", "injective mappings", "rejection-sampled crypto.getRandomValues", "25 nonidentity shifts", "KEY COUNT
    2.6 × 10^1" for 26, "Non-ASCII letters", "6,000-character safety bound". Seen: Play `d17-manual.png`, `d19-seal.png`,
    `audit-r1/state-manual-1366x768.png` (Teaching 7, Play 11). Fixed: a plain first sentence per entry a sixth grader
    can use ("Bumpiness: how often two letters picked from a column match. English scores about 6.6, random letters
    about 3.8."), exact terms and formulas after it; small counts as plain numbers, large ones with superscripts.
    (general)

#### Polish accepted
1. **Pace the bombe with Motion on.** `runBombe()`: 82 ms for one order, 432 ms for six; "watch 17,576 settings fall to
   one" is over in a blink (Play 13, `d13`, `p08`). With Motion on, step TESTED and the survivor count over about 1.5 s
   with the drums turning; the search stays fast; Motion off shows the result at once. (family:curiosity)
2. **Event messages beside their instrument.** `#status` src.html:205, 607: "Box open · Untitled", "One setting left ·
   tap it, then Run tape", "600 letters is the limit" appear only in 10 px on the plate (Play 14, Craft 9,
   `d21-open-box.png`, `audit-r1/state-weather-search-1366x768.png`). Show each beside what caused it (a stamp on the
   output tape when a box opens, the bombe line in its panel, the limit at the input count); keep the plate for the
   plate. (family:curiosity)
3. **Tool panel sticky header.** `.analysis-top` / `.analyzers`: with two or more tools, CRIB SLIDER and BUMPINESS hide
   under the "Tools read" bar and slivers of controls show above it (Play 15, Craft 8,
   `audit-r1/state-three-tools-1366x768.png`, `craft/zoom-three-tools-head.png`). Opaque header pinned at top 0 with the
   panel's padding inside it. (general)
4. **Sorted mode keeps the English model.** src.html:1039 (`if (!sorted)` skips the ghost). Draw the sorted English
   profile (E T A O I N...) beside the sorted bars, so found item 1 and "the biggest bar is probably E" can be seen.
   (general)
5. **Explain the PAD tails.** material.json `counting` ends `PAD YIWG`, `raven` `PAD LPVO`, `weather` `PAD CHRL`; a
   solved sheet looks like a broken decode (Teaching 9, Play nit, `d14`). One line on each sheet's card ("Ends with PAD
   and four filler letters, as real operators padded messages"). Keep the tails: the checked numbers depend on them.
   (general)
6. **Splitter: multiples of the key length spike too.** RAVEN reads 8.8 at 5 and 9.1 at 10 (Teaching 12,
   `frames/raven-loaded.png`). Add to the Manual's Splitter entry: "Multiples of the key length spike too; the smallest
   spike is the key." (general)
7. **Name the ghost fader.** It reads only "00" (Play 16, `d01`). Label it "English ghost" in the readout.
   (family:curiosity)
8. **Pad as stacked columns.** The Pad is a strip of key letters on a mostly blank card (`d16-sheet-pad-choose.png`).
   Stack cipher, key and plain letters in columns so the letter addition is the picture. (family:curiosity)
9. **Grid key card shows the grids.** It lists 26 glyphs (`d25-grid-encode.png`); draw the two grids and two crosses
   (three grids for Leeson) the shapes come from. (family:curiosity)
10. **Tapes show whole lines or a scroll cue.** Output cut half a line at the bottom (`d28`, `d29`). (general)
11. **Tableau card cut mid-column at the right edge** (`d24`, `d09`): fit it or show a clear scroll edge. (general)
12. **Symbols in Encode** still says "0 ASSIGNED" and shows the A to Z strip that does nothing there (`d26`): hide
    or relabel both in Encode. (family:curiosity)
13. **375x812 Symbols** has an empty band between the glyph controls and the output tape while the counter is cut
    (`audit-r1/state-symbols-375x812.png`): close the gap. (general)
14. **Range controls announce their meaning.** `#ghost` and the column sliders announce 0 to 25; add `aria-valuetext`
    ("Ghost shift 3, A to D", "Column 2 key S"), as the wheel already does (Craft 10). (general)
15. **Rotor ring fields as dials.** Bare inputs reading "1"; the spec reads "rings 01 to 26". Two-digit monospace dial
    with Up / Down like the windows (Craft 11, `audit-r1/state-rotors-680x425.png`). (family:curiosity)
16. **Nit: short practice texts score above 6.6.** RAVEN plaintext IC × 100 is 8.56, counting 7.19. One clause in the
    Manual's Splitter entry: "short, repetitive texts score higher." (general)
17. **Nit: Read speaks "IC × 100".** src.html:1086, 1630. Read says "Bumpiness 8.8 at length 5" (the spec's spoken
    form), not the unit tag. (general)
18. **Nit: plate at 680x425** wraps to "Cipher / Workbench" with the screw heads on the text (Play nit, Craft 13,
    `audit-r1/size-680x425.png`): one line, screws clear. (family:curiosity)

#### Settled calls
- **Both blockers stand.** Teaching rated the glyph labels should fix (a lookup step); Play rated it blocker (the label
  names a different real glyph). Integrator read src.html:1043-1044: the label is `i+1`, and Poe's alphabet contains the
  digits 1 to 9, so it misleads, not just inconveniences. Blocker, under REFINE Rounds (a readout that misleads).
- **Splitter guess (should fix 2) is should fix, not blocker.** See its note: the output disproves a bad guess at once.
- **Weather sheet opens as built.** Crib WEATHERREPORT and All crib spots stay on: Things to do 10 is watching the bombe
  run on that crib, and 27 crib spots is a checked number. Only RAVEN and Vicksburg change.
- **Keep the checked readouts.** Pre-solved fixes change the starting state only; 8.8 at 5, 20 of 23 gaps, ENRAVEN at
  53, HESTERBLU, the bombe's B O X and the three pad readings must all still be reachable (Done when 3). Keep `Use key`
  (once enough letters per column).
- **Leeson stays readable on load.** Pigpen has no key; the bench showing REMEMBER DEATH is honest and is the point of
  found item 3 (Kerckhoffs). Do not add a tap-to-reveal step.
- **Standards (BASELINE rule 2):** Teaching found MS-SYS-SE-32 and 33 not taught here (cryptanalytic attacks only),
  consistent with the spec's "second card ... takes over no card". No activity is added. If the map credits this tool
  with either code, move them to the lesson tool; 2-NI-06 is taught well.
- **No goal, score or finish** comes in with any fix: the bombe pacing, stamps and pairs views are readouts, not
  rewards.
- **Voice event lines:** the build follows CODEX-CURIOSITY (hint once, then Read) over the spec's four event lines;
  do not add them. The spec line goes to open questions.
- **Sensitivity, not judged here:** the Vicksburg case and its Confederacy and slavery line and Pemberton's surrender;
  Mary, Queen of Scots' trial and execution; the Leeson REMEMBER DEATH stone for grades 5 to 12; the al-Kindi
  attribution and wording (Baghdad, Arab contributions); the map reach to social-studies-10-world-war-ii-and-the-
  holocaust from technical-only Enigma content. All go to the fresh-agent sensitivity review (`refine/sensitivity.md`).
  Codex does not change these texts in this round except the Vicksburg date (should fix 11).

#### To the spec's open questions
- **A rotor case.** The 1930 manual example was dropped (needs reflector A); the rotor machine has only the invented
  weather sheet, while "a German field message" is promised in the first two minutes. Add UKW-A as a selectable
  reflector (wiring on the cited Crypto Museum page) so the 1930 message decrypts exactly, or find another verified
  Enigma I / UKW-B message? Either changes the honesty note "reflector B only" (Play 12).
- **The real Vicksburg slip.** The museum article prints the slip's ciphertext, including a clerk's doubled group
  `FEQT FEQT`; use the real slip with its errors noted instead of the recomputed one? Changes the case material and an
  honesty note (Teaching 10).
- **Letter shortcuts.** The spec binds E, W, F, C, S, R, K, B, O, X, M to bare letters; kids type letters first. Move
  them off bare letters (or behind a modifier) bench-wide? Should fix 17 handles Rotors and Swap's undo inside the spec.
- **Voice section.** The spec lists four event lines; the Curiosity brief allows only the hint and Read. Update the
  spec's Voice section to match the build (Craft nit 12).
- **Fan on the bench.** The Fan opens as a modal over the wheel; a fan beside the disk would keep the brass in view
  (Play 16). A layout change to the spec's `Fan` control.

#### Not taken
- Leeson output covered until each shape is tapped (Teaching 11): settled above; pigpen is keyless and the bench is honest.
- Fan as a bench fan instead of a drawer (Play 16): a layout redesign; sent to open questions, not to Codex.
- Real Vicksburg slip, UKW-A rotor case, spec voice lines: spec changes; sent to open questions.

<!-- end part -->

<!-- part: refine/craft.md -->

### Craft lens: cipher-vault (Cipher Workbench, Curiosity No. 11), round 1

Cold lens, 2026-11-06. Judged against CODEX-CURIOSITY.md and VISION "Curiosities: the second shape", plus STANDARDS and
BASELINE. Bundle `tools/cipher-vault/cipher-vault.html` as built (not re-bundled). Own probes: CDP scripts in
`S:/CurioClass-codex-scratch/cipher-vault/craft/` (`probe.py`, `run2.py` to `run4.py`), Chrome on port 9431, muted,
closed after. Frames cited are in that folder or in the shared audit folder `audit-r1/`.

Counts: blocker 0, should fix 7, polish 4, nit 2.

#### Should fix

1. **Square tableau is rebuilt on every update, and misses 60 fps at 4x.** `src.html:943-967` (`renderTableau`)
   rewrites 729 SVG `<text>` nodes and forces two scroll layouts on every `update()`. With a 600-letter tape and three
   tools open, one `update()` costs 5 ms at 1x and 31 ms at 4x CPU slowdown (every other machine is under 1 ms at 4x).
   One key change per frame at 4x ran at a median 50 ms frame (20 fps, 59 of 59 frames over 20 ms); a single keystroke
   in the tape takes 40 ms to reach the screen at 4x. Done when 7 fails for this machine. Better: draw the 26 by 26
   letters once and move only the three highlight rects and the chosen-letter fill. Check: `perf` and `perf2` probes
   (probe-results in the craft scratch). Tag: general.

2. **The first-run hint is spoken after its moment has passed.** `src.html:1636-1637` (`welcome` fires on any first
   tap while the Wheel is up) with `setShift` clearing `#hint` (`src.html:911`). A student whose first action is
   dragging the ring, or pressing Right on the focused wheel, sees the hint vanish and the ring move, then hears "Drag
   the inner ring." (vlog: spoken at 1325 ms after three Right presses that already read THE DIE IS CAST; spoken at
   2396 ms after a real drag). STANDARDS: a line whose moment has passed is dropped, and the spoken line matches the
   screen. Better: `valid` = the hint is still showing. Frame: `craft/wheel-dragged-cw.png` (hint already gone).
   Tag: family:curiosity.

3. **Read never speaks the first-run hint.** `src.html:1627-1633` (`readText`) and `hint:false` on `Curio.voice`.
   On a fresh page Read says "Wheel. Decode. SHIFT 00 · A to A. Output: WKH GLH LV FDVW. LETTERS 12 · Too few letters
   to read the bars." and never "Drag the inner ring." CODEX-CURIOSITY: the hint is spoken once, "then only when Read
   is pressed". A student who cannot read the brass, and whose first tap was Read or a non-wheel control, has no way to
   hear what to do. Better: while `#hint` has text, Read speaks it first, then the readout summary. Check: audit
   one-click row 4 and `voice_soundoff_read` probe. Tag: family:curiosity.

4. **The hint text runs over the inner ring letters at the preview sizes.** `src.html:415` (`#hint { font-size:30px }`
   inside the compact media query). At 680x425, 800x500 and 1000x625 "Drag the inner ring." is wider than the hub and
   sits on top of the inner ring's D and J. Better: keep it inside the hub (smaller size, or two lines). Frames:
   `audit-r1/size-680x425.png`, `audit-r1/size-1000x625.png`, zoom `craft/zoom-hint-680.png`. Tag: general.

5. **Two readouts disagree on Grid and Symbols.** `src.html:1069` (`renderCounter`). On Grid or Symbols the Counter
   counts glyphs only, so with the default letter tape it reads "LETTERS 0 · Too few letters to read the bars." with a
   1 to 26 axis, while the input tape beside it reads "12 LETTERS". A readout must say what it counted: "SYMBOLS 0"
   (and say the tape holds letters, not symbols), or count what the tape holds. Frames:
   `audit-r1/state-grid-1366x768.png`, `audit-r1/state-symbols-680x425.png`. Tag: family:curiosity.

6. **The rotor keyboard and lampboard are below the fold at 680x425 and 375x812.** Mode Rotors. Only a sliver of the
   lamp row shows; the 26 typing keys (Things to do 8, "type on the rotor machine") need a scroll inside the machine.
   STANDARDS: the main controls are visible without scrolling at every size. Better: in short boxes put the keyboard
   first and fold the ring fields and order selects behind the window row. Frames: `audit-r1/state-rotors-680x425.png`,
   `audit-r1/state-rotors-375x812.png`. Tag: general.

7. **Splitter gives a key guess with no small-sample guard.** `src.html:1083-1087`. With the 12-letter default tape the
   Splitter at length 5 shows "BUMPINESS 0.0 AT LENGTH 5" and "KEY GUESS DSDND" with a `Use key` button, from 2 or 3
   letters per column, while the Counter beside it says "Too few letters". The seal card already knows the threshold
   ("Too few letters per column for reliable counting", `src.html:1387`). Better: the same note on the Splitter under
   10 letters per column, and no `Use key` offer there. Frame: `audit-r1/state-three-tools-1366x768.png`,
   `craft/manual-1366.png` (behind the drawer). Tag: family:curiosity. Teaching lens may rate this a blocker under the
   "readout that misleads" rule; from Craft it is at least should fix.

#### Polish

8. **Analyzer panel's sticky header lets scrolled content show around it.** `.analysis-top` in the tool panel. With
   several tools open, the BUMPINESS line is cut under the "Tools read" bar and the edges of scrolled-away controls
   peek out above it at the panel's top edge (the audit's overlap rows on three-tools and weather-search). Better: an
   opaque header pinned at `top:0` with the panel's padding inside it. Frames: `audit-r1/state-three-tools-1366x768.png`,
   `audit-r1/state-weather-search-1366x768.png`, zoom `craft/zoom-three-tools-head.png`. Tag: general.

9. **Event messages live in small muted type on the plate, far from the action.** `#status` in the plate
   (`src.html:607`) carries "One setting left · tap it, then Run tape", "600 letters is the limit" and the seal and box
   messages at about 10 to 11 px in the lower-left corner, while the bombe and tape are top and right. A student running
   the bombe will not look there. Better: show the event beside its instrument (the bombe readout, the input tape
   count) and keep the plate for "Stays on this device". Frame: `audit-r1/state-weather-search-1366x768.png`.
   Tag: family:curiosity.

10. **Range controls announce bare numbers.** The English ghost slider (`#ghost`) and the column ghost sliders announce
    0 to 25, not a letter or shift, while the brass wheel announces "Shift 3, A to D". Better: `aria-valuetext` such as
    "Ghost shift 3, A to D" and "Column 2 key S". Check: focus walk (`walk_wheel`, `three-tools`). Tag: general.

11. **Rotor ring fields are bare inputs reading "1".** The ring settings show as large empty dark boxes with a single
    digit, unlike the spec's "rings 01 to 26" readout and the engraved look of the window row. Better: a two-digit
    monospace dial (01 to 26) with Up / Down like the windows. Frame: `audit-r1/state-rotors-680x425.png`,
    `audit-r1/state-weather-search-1366x768.png`. Tag: family:curiosity.

#### Nit

12. **Spec and build disagree on voice lines.** spec.md "Voice" lists four event lines ("One setting left. Tap it, then
    Run." and three more); `voice/lines.json` has only the hint and notes the omission under CODEX-CURIOSITY.md, which
    does say voice speaks the hint and then only Read. The build follows the brief; the spec line should be updated so
    the next round does not re-flag it. `voice/lines.json` matches `allLines()` word for word. Tag: family:curiosity.

13. **The plate wraps to two lines at 680x425** ("Cipher" / "Workbench" with the screw heads crowding). Frame:
    `audit-r1/size-680x425.png`. Tag: family:curiosity.

#### Checked and clean

- Contract: one file, 152 KB bundle (no images, fonts or audio); no network requests in any probe (CDP Network log,
  every machine, bombe, drawers); no console errors or exceptions in any probe; kit used for voice, Motion and Sound
  (`Curio.voice`, `Curio.onMotion`), no kit header or lesson frame. Manual source links are ordinary outbound links, not
  requests.
- Engine: AAAAA to BDZGO at I II III, B, AAA; double step ADU to ADV, AEW, BFX; bombe 17,576 settings in 77 ms, all six
  orders 105,456 in 406 ms (1,349 ms at 4x), one survivor I II III B O X. Wheel, Grid, Symbols, Rotors and Pad
  `update()` under 1 ms at 4x with 600 letters and three tools.
- 600-letter limit: "600 LETTERS · LIMIT" and "600 letters is the limit". Storage blocked: "Storage blocked · plays
  without saving", tool plays.
- Access: Tab reaches every control on all six machines (focus walks `walk_*`), amber 3 px focus ring on every stop;
  the wheel is a `slider` with "Shift 0, A to A"; rotor windows are spinbuttons; pigpen, symbol and plugboard keys are
  labelled buttons. No target under 44 px at 1366x768, 1000x625 or 680x425 on any machine. Keys 1 to 6, C, S, R, K, B,
  O, M work with no field focused; Escape closes every drawer and focus returns to the opener (Case file, Boxes,
  Manual, Fan, Seal). Wheel drag direction matches the ring's turn (`craft/wheel-dragged-cw.png`).
- Look rules: the bench fills the screen, no header bar or pill panel; readouts are monospace with units (all
  `*-readout`, tapes, windows); Manual and plate lower-left; Motion, Sound and Read on their own panel top-right (as the
  spec places it), with `aria-pressed`. Motion off: audit clean; Fan lists all 26 shifts at once in calm.
- Words: no em dashes in src, bundle, notes or tool.draft.json; "Curio Class" never "Curio" alone; classroom-safe;
  privacy stated on the plate ("Stays on this device") and in notes. Lesson creep search (score, points, level, goal,
  sticker, badge, correct, wrong, try again, complete, well done): only CSS `pointer` and "point" in prose.
- Art: `art/prompts.json` has no assets and no `art:` tokens are used; everything is drawn in code, as the brief allows.

#### Voice check

Sound on, Motion on, held clicks (120 ms), fresh page per run.

| Line | Kind | Expected | Spoken |
|---|---|---|---|
| "Drag the inner ring." | how-to (first-run hint) | once per load, only while the hint shows | once across 5 Increase shift + 5 Counter taps; but also after the hint was already gone (finding 2) |
| Read (machine, setting, output, tool readouts) | read | every press, Sound off too | every press, Sound off too; never includes the hint (finding 3) |

- Repeats: the hint line never repeats; Read speaks each press. No event lines exist (nit 12).
- Stale: Increase shift then Grid 0.2 s later: the hint started at the first tap, nothing queued after. After a drag or
  arrow-key first move, the hint plays with the hint gone (finding 2).
- First tap: Grid or Symbols first: nothing (the hint is the Wheel's only); Sound first: nothing; Read first: the
  readout summary only; a wheel control first: the hint at once.
- Read cut: Read 0.25 s into the hint stops it and speaks; a following tap and machine change start cleanly.
- Order: no line out of order (there is one line).

#### Audit pilot

- **Leads confirmed:** `#hint` under the ring at 680x425, 800x500, 1000x625 (finding 4); rotor keyboard cut by the
  machine's scroll at 680x425 and 375x812 (finding 6); the three-tools and weather-search overlaps are the sticky tool
  header over scrolled content (finding 8, real but polish).
- **Leads wrong or noise:** the ring letters "under circle" (SVG letters drawn on brass discs); "hint out of view" on
  every non-Wheel state (the hint belongs to the brass wheel, which is hidden there); "welcome not heard" after a first
  tap on Case file, Boxes, the machine buttons, Fan, Seal, Manual (a Curiosity has no welcome; the hint lives on the
  brass); the Manual keep-region rows (a modal drawer); the symbol card and letter strip "cut sideways" at 680x425 and
  375x812 and the column sliders below the scroll at 375x812 (deliberate scroll strips, every item reachable).
- **Missed by the audit:** the Square's 31 ms update at 4x (finding 1); the hint spoken after its moment (2); Read not
  speaking the hint (3); Counter "LETTERS 0" against the tape's 12 LETTERS on Grid and Symbols (5); the Splitter key
  guess from 2 or 3 letters per column (7); event messages parked on the plate (9); range values announced as bare
  numbers (10).

<!-- end part -->

<!-- part: refine/play.md -->

### Play lens: cipher-vault (Cipher Workbench, Curiosity No. 11), round 1

Played on the bundled `tools/cipher-vault/cipher-vault.html` with `scripts/drive.py` (port 9421), real drags and clicks
where it matters, JS only to set up state. My frames: `S:/CurioClass-codex-scratch/cipher-vault/play/frames/`.
Shared audit: `S:/CurioClass-codex-scratch/cipher-vault/audit-r1/`. Judged as a Curiosity (CODEX-CURIOSITY.md,
VISION "Curiosities: the second shape"), not against lesson norms.

#### Short test

- **Would a kid open it unassigned?** Yes, nearly. Dragging the brass ring until WKH GLH LV FDVW turns into THE DIE IS
  CAST works with nothing read (`d01-drag-ring.png`: a real counter-clockwise drag lands on SHIFT 03 and the hint goes),
  and secret messages for a partner are a strong pull. What holds it back is below: the Gold-Bug, the most kid-shaped
  case, is hard to actually work, and the partner game leaks its own secret.
- **Would an adult play for fun?** Yes. Real Enigma I wirings, a crib with red "never itself" cells, a working
  exhaustive bombe (17,576 in about 80 ms, 105,456 in 432 ms), a splitter with real IC. This is the strongest part.
- **Is the real thing the interface?** Yes for the wheel, the tableau, the rotor box and the crib. Weaker for the Pad
  (a strip of letters on a blank card) and the Grid (a glyph list, not the grids the shapes come from).
- **Does it work with no finish line?** Yes. Nothing is locked, scored or marked done; cases open in any order
  (`d05-cases.png`). One risk to depth: the practice sheets open already solved (finding 4).

No question fails outright, so no short-test blocker. The one blocker is a misleading readout.

#### Findings

##### 1. Gold-Bug counter labels name the wrong glyph (blocker, family:curiosity)
- Where: `src.html:1044` (glyph bars labelled `${i+1}`, the key-card position), Symbols with the Poe case.
- What: Poe's alphabet is made of digits and marks, so the position numbers under the bars read as glyphs. The tallest
  bar (33) is labelled **5**, but it is glyph **8**; glyph 5 occurs 12 times. Sorted makes it worse: the top bar reads
  "5" (`p02-poe-sorted.png`). The spec's own path ("count the symbols, guess E") leads a student to assign E to 5, and
  every later guess builds on that. A readout that misleads when its assumption (labels are not glyphs) fails.
- How: `d08-case-poe.png`, `p02-poe-sorted.png`; counts checked from the material key (E = "8").
- Better: label each bar with the glyph itself (draw it with `glyphSVG`, as the key card does), for both Poe and the
  drawn-shape alphabet.

##### 2. Symbol cracking: the output cannot be read against the cipher (should fix, family:curiosity)
- Where: Symbols decode (Poe case, counting sheet); input tape `.tape-face` and `#output` are separate tapes.
- What: after E, T, H the output reads `...THE...H...H..TE...THE.E...` with every other symbol a dot
  (`p01-poe-ETH.png`). To guess the next letter the way Legrand does (`;48;(88` becomes THE TREE) the student needs the
  glyph that sits beside THE, but the cipher is on another tape, spaced wide, and only 21 of its 203 glyphs show in one
  row (scrollHeight 448 vs 62 visible, no scroll cue). The counting sheet's glyph tape shows a half-cut second row
  (`d10-sheet-counting.png`). Things to do 4 is the most kid-shaped activity on the bench and it stalls here.
- Better: under Symbols and Grid decode, show the output as stacked pairs (glyph over its guessed letter or a dot),
  like the crib tape already does, so patterns and neighbours are visible together.

##### 3. Tools read Input by default, so the machine never moves the bars (should fix, family:curiosity)
- Where: `src.html:633` (`toolsRead:'input'`), `#tools-read`.
- What: turning the wheel or growing the Square key changes only the output tape; the Counter, Splitter and Repeats
  read the input and stay still. Things to do 1 and 5 ("watch the bars flatten as the key grows from 1 to 10"),
  and found item 1 (a Caesar shift only slides the bars) are invisible until a student discovers the small
  "Tools read" select. With Encode on, the interesting text is the output.
- How: `d24-square-key.png` (Encode with LEMON, counter shows plain-text counts), code path `analysisText()`.
- Better: tools read the ciphertext side by default (input when decoding, output when encoding), with the select
  as an override; or show both as two bar colours.

##### 4. Sheets and Vicksburg open already solved (should fix, family:curiosity)
- Where: `loadCase` / `loadSheet`, `src.html:1304` (`offset = 4`), `src.html:1338` (`offset = 53`), splitter at 5.
- What: the cheap pass (REFINE, Rounds). RAVEN opens with Splitter at 5, `KEY GUESS RAVEN` and a `Use key` button, and
  the crib at offset 53 already reading ENRAVEN (`d11-sheet-raven.png`); two clicks decode it (`d11b`). Vicksburg opens
  with PEMBERTON at offset 4 already showing HESTERBLU while the case card says "Slide the crib PEMBERTON"
  (`d09-case-vicksburg.png`). The weather sheet opens with the crib laid at the right length and All crib spots on.
  The finding is the reward; here it is handed over before the first move.
- Better: open sheets at length 1 and offset 0, with no key guess until the length is chosen, so the jump to 8.8 at 5
  and the HESTERBLU moment are the student's own.

##### 5. Sealing leaves the secret on the bench (should fix, family:curiosity)
- Where: `sealBox()` `src.html:1409`.
- What: after Seal the input tape still reads MEET AT THE OAK and the wheel still shows SHIFT 07, while the status says
  "Sealed · hand this device to your partner" (`d20-sealed-then-shelf.png`). The partner sits down to the answer.
- Better: on Seal, clear the tapes and reset the machine to its zero setting (or put the box's cipher on the tape), so
  the bench is safe to hand over.

##### 6. Letter keys are shortcuts when no field has focus (should fix, general)
- Where: document keydown, `src.html:2014` onward.
- What: on Rotors, a student who clicks the Rotors button and types HELLO on the real keyboard flips Decode to Encode
  (E) and opens the Case file (O) (`p04` result: direction "Encode", drawer "Case file"). On the wheel, S toggles
  Splitter, W swaps tapes, E flips direction (`p05`). W replaces the input tape with the output with no undo. The
  rotor machine's natural action is typing; it only works once a rotor key has focus.
- Better: on Rotors, letter keys press the machine whenever no text field has focus; elsewhere keep single-letter
  shortcuts off the letters a kid types first, or require the shortcut panel, and never bind a destructive action
  (Swap) to a bare letter.

##### 7. Rotor keyboard hidden at 680x425 and 375x812 (should fix, family:curiosity)
- Where: `.machine` Rotors page, compact layouts.
- What: only the top of the lampboard shows; the typing keys sit below inside the machine's scroll box
  (`audit-r1/state-rotors-680x425.png`, `state-rotors-375x812.png`, `state-weather-search-680x425.png`). The machine's
  main control is out of sight at the iframe size (Done when 6).
- Better: at compact sizes put Run / Set back / Plugboard and ring inputs in one row and give the lampboard and keys the
  height; ring inputs can be smaller.

##### 8. 680x425 wheel: tiny letters and the hint across the ring (should fix, family:curiosity)
- Where: `#hint` `src.html:520` (13 px in the SVG, not scaled with the disk), wheel at compact size.
- What: the disk is about 155 px across, its letters about 7 px, and the first-run hint runs over the inner ring's
  letters (`play/frames/zoom-680-hint.png`, from `audit-r1/size-680x425.png`; same at 800x500 and 1000x625). The first
  screen's one instruction is the hardest thing to read on it.
- Better: give the disk more of the compact height (the tool panel can shrink), and fit the hint inside the inner
  boss at every size.

##### 9. Rotors opens with its windows at A A M, not A A A (should fix, family:curiosity)
- Where: `update()` sets `state.positions` to the end of the default tape when Rotors is selected.
- What: typing AAAAA gives BTMCD (`d22-rotors-type.png`), while the Manual says "start AAA. AAAAA becomes BDZGO".
  The windows are honestly where the machine ended, but nothing on screen says so, and a student checking the Manual
  thinks the machine is wrong.
- Better: show the start setting in the windows on arrival (or a "START AAA" readout beside STEP), so the first press
  matches the Manual.

##### 10. Status stays "press Run tape" after Run (should fix, general)
- Where: survivor click `src.html:1868`; `runRotors()` never updates the status.
- What: after tapping the survivor and Run tape, the plaintext is on the output tape but the plate still says
  "Setting loaded · press Run tape" (`d14-weather-survivor-run.png`). Words must match the state (POLISH).

##### 11. Manual and seal card words are past grade 5 (should fix, general)
- Where: `showManual()`, `keyCount()`, `showSeal()`.
- What: "25 nonidentity shifts", "KEY COUNT 2.6 × 10^1" for 26, "injective mappings", "rejection-sampled",
  "Non-ASCII letters", "a 6,000-character safety bound", "bounding lines" (`d17-manual.png`, `d19-seal.png`). The
  band starts at grade 5; a student who opens the Manual alone gets lost in its first paragraph.
- Better: plain first sentences per entry ("26 settings. Trying them all takes a minute."), with the exact terms
  after; write small key counts as numbers and use superscripts for large ones.

##### 12. No rotor case: the bench's best machine has only an English practice sheet (should fix, family:curiosity)
- Where: Case file (`d05b-cases-scrolled.png`), note "1930 manual example omitted: it needs reflector A".
- What: the spec's first two minutes promise "a German field message"; the rotor machine now has only the invented
  weather report. Real material is load-bearing (VISION quality 5).
- Better: add UKW-A as a selectable reflector (its wiring is published beside B on the Crypto Museum page already
  cited) so the 1930 message decrypts exactly, or find another verified Enigma I / UKW-B message.

##### 13. The bombe is over before it can be watched (polish, family:curiosity)
- Where: `runBombe()`; 82 ms for one order, 432 ms for six (`d13`, `p08`).
- What: Things to do 10 is "watch 17,576 settings fall to one"; the drums and the TESTED count are gone in a blink.
  The climax of the Rotors bench is flat.
- Better: with Motion on, pace TESTED and the survivor count over about 1.5 s with the drums turning; Motion off shows
  the result at once (the search itself stays fast).

##### 14. Every event lands in 10 px on the plate (polish, general)
- Where: `#status` `src.html:205`, inside the maker's plate lower-left.
- What: "Box open · Untitled" (the partner's crack, `d21-open-box.png`), "One setting left · tap it, then Run tape",
  "600 letters is the limit" all appear only there, far from the action, in 10 px. Opening a partner's box is the peak
  of the partner game and it is a status line.
- Better: show the event beside what caused it (a stamp on the output tape when a box opens, the bombe line in its
  panel), and keep the plate for the plate.

##### 15. Tool panel: sticky header covers scrolled tools (polish, general)
- Where: `.analyzers` with two or more tools open.
- What: CRIB SLIDER, its Guess field and BUMPINESS are hidden under the "Tools read" bar after the panel auto-scrolls,
  and slivers of controls show above the panel's top border (`play/frames/zoom-d28-top.png`, `d28-all-tools-600.png`,
  `audit-r1/state-three-tools-1366x768.png`).

##### 16. Smaller polish
- Ghost fader has no label on screen, only "00" (`d01`). Name it "English ghost" in the readout.
- Pad is a strip of key letters on a mostly blank card (`d16-sheet-pad-choose.png`). Stack cipher, key and plain
  letters in columns so the letter addition is the picture.
- Grid key card lists 26 glyphs (`d25-grid-encode.png`); draw the two grids and two crosses the shapes come from.
- Tapes cut half a line at the bottom (output third line in `d28`, `d29`); show whole lines or a scroll cue.
- Tableau card is cut mid-column at the right edge (`d24`, `d09`).
- Fan opens as a modal over the wheel (`d03-fan.png`); a fan on the bench beside the disk would keep the brass in view.
- Symbols in Encode still says "0 ASSIGNED" and shows the A to Z strip, which does nothing there (`d26`).
- 375x812 Symbols: an empty band between the glyph controls and the output tape while the counter below is cut
  (`audit-r1/state-symbols-375x812.png`).

##### 17. Nits
- Plate screws (the ⊖ marks) sit on the wrapped plate text at 680x425 (`audit-r1/size-680x425.png`).
- The weather plaintext ends "PAD CHRL" (padding tail), which reads as a broken decode (`d14`).
- An empty tape reads "BUMPINESS 0.0" rather than saying there are no letters (`p14`).

#### For the sensitivity review (not judged here)
Leeson's REMEMBER DEATH stone; the Vicksburg dispatch and its Confederacy and slavery line; Mary, Queen of Scots'
trial and execution in the Manual.

#### Checked and fine
Real drag decodes at shift 3 and clears the hint (`d01`); clockwise drag steps back (`d02`); Fan click sets the
shift (`p11`); all four cases and four sheets load in any order; Use key decodes RAVEN; bombe leaves B O X at @10 and
decodes the weather report; three pad keys give the three readings (`d16`); a sealed Wheel box opens when the output
matches (`d21`); 600-letter tape with all five tools at 1366 shows the limit line (`d28`); Motion off bombe and
default (`p06`, `p07`); rotor order select swaps rather than duplicating (my first duplicate test used a non-bubbling
event and was wrong). Read speaks machine, setting, output and the open readout (`p10`). Console clean in every shot.

#### Counts
blocker 1 · should fix 11 · polish 4 (plus 8 small polish items under 16) · nit 3

#### Audit pilot
- **Confirmed:** the `#hint` "under circle" lead at 680x425, 800x500 and 1000x625 (finding 8); `#keyboard` cut by a
  scroll panel at 680x425 and 375x812 (finding 7); the three-tools and weather-search overlaps with `#tools-read`
  (finding 15, it is the sticky header over scrolled tools).
- **Wrong or noise:** the single ring letters "under circle" (SVG letters over the brass disk, drawn correctly); "hint
  out of view" on other machines (the hint belongs to the wheel); Manual keep-region leads (a modal drawer); "welcome
  not heard" on first taps of Case file, Boxes and other machines (right for a Curiosity: the hint is spoken once on
  the wheel, then only on Read); sideways-scroll symbol and letter strips at compact sizes (deliberate scroll rows).
- **Missed:** the Gold-Bug bar labels (finding 1), the separated symbol tapes (2), Tools read default (3), pre-solved
  sheets (4), the secret left on the bench after Seal (5), letter shortcuts while typing (6), rotor windows at AAM (9),
  stale status (10), the bombe's invisible run (13).

<!-- end part -->

<!-- part: refine/teaching.md -->

### Refine lens: Teaching, cipher-vault (Cipher Workbench, Curiosity No. 11)

Cold lens, round 1, 2026-11-06. Judged against docs/agents/CODEX-CURIOSITY.md and VISION.md "Curiosities: the second
shape", plus REFINE.md Teaching, STANDARDS.md and BASELINE.md. Bundle `tools/cipher-vault/cipher-vault.html` as built.
My frames and check scripts: `S:/CurioClass-codex-scratch/cipher-vault/teaching/` (frames/, checks.json, gv.json,
g2.json). Shared audit: `S:/CurioClass-codex-scratch/cipher-vault/audit-r1/`.

Counts: 1 blocker, 6 should fix, 5 polish, 2 nits.

#### Findings

##### 1. Encode toggle shows the whole secret key in Boxes and practice sheets (blocker, general)
- Where: src.html:921-931 (`renderSymbols`, Encode labels each glyph with `encoderLetter`), 1427-1450 (`openBox` keeps
  `state.symbolKey`), 1687-1694 (direction toggle).
- What: a partner opening a sealed Symbols box presses E (or Decode/Encode) once and the key card prints the sealer's
  letter under every glyph. The same toggle turns the counting sheet's 26-glyph puzzle and the Gold-Bug into a printed
  answer key. Boxes is the bench's one hidden-information activity ("sealed boxes let a partner try to crack your
  message"), and the toggle is not recorded as a Peek, so the box still shows "sealed" or "open" as if earned.
- How seen: gv.json shots `symbox-encode` (sealed a fresh New key box, opened it, clicked #direction: card read
  `DXWAGOKEUSZQHPBMCLNJITVFRY`) and `counting-encode` (frame `frames/counting-encode.png`: every glyph labelled).
- Better: in Encode with a box or sheet loaded, use a fresh key (or the partner's own key) rather than the hidden one,
  or count switching to Encode on a box as a Peek.

##### 2. Switching to Encode wipes a glyph tape with no way back (should fix, general)
- Where: src.html:1690 (`if (!state.decode && /[\uE000-\uE0FF]/.test(state.input)) state.input = ''`), 1771.
- What: a student halfway through the counting sheet or Gold-Bug who presses E (one stray key; E is a shortcut) loses
  the 296- or 203-glyph tape. Toggling back leaves an empty tape; the only recovery is re-opening the sheet, which also
  clears every letter they assigned (`loadSheet` resets `symbolMap`). The status line says nothing.
- How seen: `counting-encode` returned `input: 0` after one click; frame shows 0 LETTERS.

##### 3. The Counter's English ghost silently freezes on ordinary pasted text (should fix, general)
- Where: src.html:1074 (`$('ghost').disabled = ... !/^[A-Z\s.,'!:;?\-]*$/.test(analysisText())`), 1807.
- What: one digit, double quote, parenthesis or curly apostrophe anywhere on the tape disables the ghost fader and the
  chart drag, with no message. "Count anything: paste a paragraph" (spec, Things to do 2) is the core counting move,
  and most pasted paragraphs contain one of these. The ghost stays drawn at its old offset, so it looks alive.
- How seen: g2.json `ghost-digit` (`IN 1863 ... "HOLD ON"`: ghostDisabled true, 55 letters) and `ghost-curly`
  (`IT’S ...`: ghostDisabled true). The text already has letters only counted; the ghost needs only letters too.

##### 4. Glyph counters are labelled 1 to 26, so "count the symbols, guess E" needs a lookup the card does not show (should fix, family:curiosity)
- Where: src.html:1037-1045 (`barChart`: non-letter bars get the index `i+1`), 1066.
- What: on the Gold-Bug and the counting sheet the bars read 1, 2, 3... while the key card shows no numbers. To learn
  that bar 5 (33) is Poe's `8` the student must click the bar (undocumented on screen) or hover for a title. Poe's own
  table lists the characters themselves. The frequency attack (the main thing these two sheets teach, and the
  attack side of the anchor) is one hidden step harder than it should be.
- How seen: `frames/poe-loaded.png` (bars 1 to 20, card shows glyphs only), `frames/counting-loaded.png`,
  `frames/leeson-loaded.png`. Counts themselves are right: 8:33, ;:26, 4:19, ‡ and ) 16, *:13, 5:12, 6:11 match the
  table in Poe's story (checked in Python on material.json).
- Better: draw each glyph under its bar (the SVG glyphs already exist), and in Sorted mode show the sorted English
  profile beside the sorted glyph bars so "biggest bar is probably E" can be seen, not remembered.

##### 5. RAVEN and Vicksburg open already solved (should fix, family:curiosity)
- Where: src.html:1330-1339 (RAVEN: split 5, crib THE SAME at offset 53, three tools open), 1299-1307 (Vicksburg:
  PEMBERTON preset at offset 4), 1083 (`colGhosts = cols.map(guessShift)`).
- What: the RAVEN sheet loads with `KEY GUESS RAVEN` and a `Use key` button at the top of the panel, length 5 lit,
  columns labelled R A V E N, and the crib showing ENRAVEN. Vicksburg loads with `IMPLIED KEY HESTERBLU` while the case
  card says "Slide the crib PEMBERTON". Things to do 6 and 7 (Repeats finds the gaps, the Splitter at 5 makes five
  Caesars, slide the crib and watch the key appear) never happen; the student reads an answer. Sweeping the cheap
  way (REFINE Rounds) costs zero moves here. Curiosity rules say the "Things people have found" are found, not shown.
- How seen: `frames/raven-loaded.png`, `frames/wheel3.png` (Vicksburg state carried over), checks.json `vicksburg`.
- Better: open sheets at length 1 and offset 0 with ghosts at A, so the student finds the bumpiness spike, the factor,
  and the crib spot. Keep auto-fit as a button ("Fit ghosts") rather than the starting state.

##### 6. Seal card key count overstates a rotor box by six times (should fix, general)
- Where: src.html:1389-1391 (`1.05456 × 10^5`, "six rotor orders"), 1439-1441 (`openBox` hands the partner the
  sealer's order, rings and plugboard; only the start is reset).
- What: the partner gets the rotor order, so the real search is 17,576 starts, and with the plugboard set the box
  silently disables the bombe but the card still says "Fixed-ring starts only". A meter that misleads when its
  assumption does not hold is a blocker class item in REFINE Rounds; I rate it should fix because the card also says
  "Bench estimate, not a real security rating". Either hide order and rings on open, or count what is actually hidden.
- How seen: gv.json `rotorbox`: sealed order III I II, rings 5 6 7, start H I J; opened box had order [2,0,1], rings
  [4,5,6], start [0,0,0].

##### 7. Manual and notes read at a college level for a grade 5 to 12 bench anchored at 6-8 (should fix, general)
- Where: src.html:1581-1626 (Manual), notes.md "Key skills".
- What: "arithmetic mean of the columns' indices of coincidence ... sum f(f−1) divided by N(N−1)", "26!/6! ... injective
  mappings", "rejection-sampled crypto.getRandomValues", "chi-square", "Ring numbers shift the wiring, not the visible
  notch letters", "Separate a changing rotor state from an initial setting". The math is right and should stay
  reachable, but each entry needs a plain first sentence a sixth grader can use ("Bumpiness: how often two letters
  picked from a column match. English scores about 6.6, random letters about 3.8.") with the formula after it.
  Respecting the kid is not the same as writing for a cryptographer.
- How seen: read in source; Manual drawer frames `audit-r1/state-manual-1366x768.png`.

##### 8. Vicksburg date is wrong against its own cited source (should fix, general)
- Where: src.html:1268 ("The museum dates opening to 2009").
- What: Catherine M. Wright's museum article (the cited source, acwm.org PDF, pp. 4-5) says the conservator examined
  the bottle in December 2008 and removed the message then; only the photograph reached the museum in January 2009.
  The bench should say the bottle was opened in December 2008 (and the message read in 2010, publicized 25 December
  2010, which it gets right).
- How seen: fetched and read the article PDF.

##### 9. Padding tails print as words on the solved sheets (polish, general)
- Where: material.json `counting` ends `... TO COUNT. PAD YIWG`, `raven` ends `PAD LPVO`, `weather` ends `PAD CHRL`.
- What: a student who solves the counting sheet ends on "PAD YIWG" and will reasonably think they made a mistake, or
  connect it to the Pad machine. The only explanation is one clause in Sources ("Padding tails preserve the original
  comparison texts"). Say so on the sheet's card (for example "Ends with PAD and four filler letters, as real
  operators padded messages"), or drop the tails if the checked numbers still hold.

##### 10. The real Vicksburg cipher slip is legible and published, but the bench uses a recomputed one (polish, family:curiosity)
- Where: src.html:1267, 1300.
- What: the museum article prints the slip's ciphertext (`SEAN WIEUIIZH DTG CNP LBNXGK OZ BJQB FEQT FEQT XZBW ...`),
  which nearly matches the bench's recomputation (`SEA'N WIEUIIZH, DTG CNP LBHXGK ...`), including a real clerk's
  doubled group `FEQT FEQT`. Real material is load-bearing in a Curiosity; the real slip, with its errors noted, is a
  better case than a clean reconstruction. Not wrong as built: the reconstruction is labelled honestly.

##### 11. Leeson's stone reads itself (polish, family:curiosity)
- Where: src.html:1294-1297, 756-763.
- What: the case loads in Decode and the output tape shows REMEMBER DEATH at once, so "Read James Leeson's gravestone
  with the pigpen grid" (Things to do 3) is done by the bench. Pigpen has no key, so this is honest; but the student
  learns that by seeing the answer, not by matching shapes. Opening with the output covered until the student taps
  each shape on the card (or loads it in Encode-from-card) would keep the lesson.
- How seen: `frames/leeson-loaded.png`.

##### 12. Splitter bar at length 10 is taller than at 5, unexplained (polish, general)
- Where: src.html:1081, Manual "Things people have found".
- What: on RAVEN the bumpiness bars are 4.7 4.7 4.6 4.7 **8.8** 4.5 5.0 4.4 4.4 **9.1** 4.2 4.4: the tallest bar is 10,
  not 5. Correct maths (multiples of the period also spike), but a student hunting the tallest bar picks 10. One
  "Things people have found" line ("Multiples of the key length spike too; the smallest spike is the key") fixes it.
- How seen: g2/gv `splitter12` and `frames/raven-loaded.png`.

##### 13. Sorted mode hides the English model (polish, general)
- Where: src.html:1039 (`if (!sorted)` skips the ghost).
- What: "A Caesar shift slides the bars without changing their sorted heights" is the bench's best found thing, but in
  Sorted the comparison English profile disappears, so the student cannot see it match. Draw the sorted English
  ghost (E T A O I N...) in Sorted mode.

##### 14. Plain English IC on the practice sheets is well above the stated "about 6.6" (nit, general)
- Where: Manual Splitter paragraph (src.html:1591), material.json.
- What: the RAVEN plaintext's own IC × 100 is 8.56 and the counting text's 7.19 (repetitive practice prose). A student
  comparing will see "English 6.6" and an English sheet at 8.6. A short note ("short, repetitive texts score higher")
  would cover it.

##### 15. Read speaks "IC × 100" (nit, general)
- Where: src.html:1086, 1630. Read reads the splitter readout verbatim, `BUMPINESS 8.8 AT LENGTH 5 · IC × 100`; the
  spec's spoken form is "Bumpiness 8.8 at length 5". A voice says "I C times one hundred". Craft may own this.

#### Standards (BASELINE rule 2)

Anchor module computer-science-6-8-cyber-attacks-and-defense ("Common attacks and the CIA triad"): MS-SYS-SE-32 (per
CSTA's alignment pages, the consequences of ignoring confidentiality, integrity and availability when handling data)
and MS-SYS-SE-33 (evaluate common cyber attack types and their preventions).
- Confidentiality and the cost of breaking it are taught well by doing: weak keys fall to the Fan, Counter and bombe;
  a reused pad becomes a Vigenere key; Venona is in the Manual. Integrity and availability are not exercised anywhere.
- Attacks taught are cryptanalytic (brute force, frequency, known plaintext, crib), real and hands-on, but not the
  "common cyber attacks" of the 6-8 standard (phishing, malware, password guessing), and no modern prevention is
  practised.
- The 2017 crosswalk 2-NI-06 (apply multiple methods of encryption) is taught thoroughly by all six machines.
- Verdict: consistent with the spec's own call ("a second card ... takes over no card"). Not a finding as long as the
  map lists this tool as a second card and the lesson tool owns MS-SYS-SE-32 and 33. If the map credits this tool
  with either code, that is a should fix: move them to the lesson tool. No thin activity should be added here.

#### Done when (Teaching-relevant items)
1. PASS: shift 3 reads THE DIE IS CAST, every notch re-decodes (`audit-r1/state-wheel-three-1366x768.png`).
2. PASS: AAAAA to BDZGO; ADU to ADV, AEW, BFX; 1930 example dropped with reason (reflector A, confirmed at Weierud's
   cryptocellar page).
3. PASS: bumpiness 8.8 at 5, 20 of 23 gaps, THE SAME at offset 53 gives ENRAVEN, bombe leaves only B O X at @10 over 27
   spots (17,576 tests, 71 ms; all six orders 105,456 tests, 432 ms, one survivor), all three pad keys decrypt.
4. PASS: all cases and sheets load in any order; nothing locked or marked.
5. Seal/open works; Encode giveaway (finding 1) undermines it.
8. PASS: no score, goal, level or finish; lesson creep words absent from src.html.

#### Facts spot-checked against a second source (13)
1. Enigma I wirings and test vector AAAAA to BDZGO: computed in the bench, matches the standard published vector.
2. Double step ADU, ADV, AEW, BFX: computed, matches the standard published sequence.
3. Norvig letter percentages, all 26: match norvig.com/mayzner.html exactly.
4. 1930 manual example uses Umkehrwalze A: confirmed at cryptocellar.org (Weierud).
5. Leeson died 28 September 1794 aged 38; key of three series, one dot, two dots, none, I standing for J: confirmed in
   Hemstreet 1899 (Gutenberg 39789); the bench's grid code matches it; REMEMBER DEATH decodes.
6. Gold-Bug: 1845 Tales text reads forty-one (eapoe.org); a later Poe correction to twenty-one is attested (Kern, The
   Nation, 1913, on eapoe.org). Bench claim holds.
7. Gold-Bug cipher counts (8:33, ;:26, 4:19, ‡ 16, ) 16, * 13, 5 12, 6 11): match Poe's table; cryptogram decodes to
   the plaintext character for character (checked in the bench).
8. Vicksburg plaintext wording ("I have sent some caps. I subjoin despatch from Gen. Johnston."): matches the museum
   article. Opening date: does not match (finding 8). AP story 25 December 2010: matches.
9. Vicksburg key MANCHESTER BLUFF: recomputed ciphertext nearly matches the slip printed in the museum article.
10. Mary, Queen of Scots: 57 letters, Lasry, Biermann and Tomokiyo, misfiled in the BnF archive: confirmed by multiple
    2023 news reports (WGBH, PopSci); 1578-1584 is in the paper's title.
11. 26! = 4.03 × 10^26, 26!/6! = 5.60 × 10^23, 6 × 26^3 = 105,456: recomputed.
12. Caesar shift 3 (Suetonius, Julius 56) and Augustus AA for X (Augustus 88, Loeb): consistent with the Loeb text as
    I know it; not refetched.
13. Weather sheet decrypts at I II III, B, rings A, start B O X: computed.

#### Sensitivity review (rule 5): flag, not judged
- Vicksburg case and history: Confederate dispatch, "The Confederacy fought to preserve slavery", Pemberton's surrender.
- Mary, Queen of Scots: trial and execution stated plainly.
- Leeson stone: REMEMBER DEATH memento mori for grades 5 to 12 (spec open question).
- Al-Kindi attribution and wording ("Baghdad", Arab contributions).
- Map reach to social-studies-10-world-war-ii-and-the-holocaust: the bench's Enigma content is technical only; a
  reviewer should confirm that listing is appropriate.

#### Audit pilot
- Leads confirmed: none are Teaching leads. The audit's clean rows I relied on: first screen at 1366x768 shows the
  hint and DECODE wheel; wheel-three state shows THE DIE IS CAST; no console errors or exceptions in any state.
- Leads wrong or noise for this lens: the "text hidden under circle" rows at small sizes are the wheel's own letters
  inside its rings; "hint out of view" in other machine states is the wheel hint correctly hidden on another page;
  manual-state "keep region covered" rows are the modal drawer by design.
- What it missed (all Teaching): the Encode giveaway on boxes and sheets (1), the destructive Encode wipe (2), the
  ghost freezing on digits and quotes (3), numbered glyph bars (4), pre-solved sheets (5), the rotor box key count (6),
  the wrong Vicksburg date (8), the PAD tails (9). None are mechanical; they need the state walked by intent.

<!-- end part -->

## Fix

<!-- part: polish.md -->

### Polish: cipher-vault (Codex fix, round 1)

Evidence root: `../../_scratch/cipher-vault/`. Before: `fix-before-a/`, `fix-before-b/` and their JSON results/logs. After: `fix-after-a/`, `fix-after-b/`, `fix-proof-a/`, `fix-proof-b/`, `fix-proof-c/`, `fix-final-a/`, `fix-final-b/`, `fix-last/`. Each named shot also has `<name>.numbers.json` at the evidence root. All final claims below use viewed frames or captured numbers. One performance requirement remains open.

#### Blocker

1. **FIXED. Encode exposes hidden keys.** Before `b1-box`: wrong key loaded, visible encoder alphabet, box unpeeked. Boxes now load their own symbol key; Encode/New key use a separate fresh writing workspace. Decode restores cipher and guesses. `final-symbol-box-cheats`: toggle, New key and a Wheel/direction/Symbols detour all use unrelated keys, leave the box unopened and restore its actual key/tape. Counting and Poe pass the same three attempts in `proof-b1-cheats`.
2. **FIXED. Wrong Counter glyph labels.** Before `b1-b2-poe` recorded glyph 8/count 33 labelled 5. The retained bar nodes now draw actual glyph SVGs and name the glyph in aria. `last-poe-sorted`: tallest bar title `8: 33`, label `8`; `proof-counting-glyphs`: 296 symbols, 26 drawn labels. `last-phone-labels.png` verifies the final compact glyph sizing.

#### Should fix

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

#### Polish accepted

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

#### Settled calls

- Both blockers were treated as blockers. Weather retains WEATHERREPORT and All crib spots; its only survivor remains B O X over 27 spots. Leeson remains readable on load.
- No goals, scores, levels, quiz, finish, kit header or automatic event voice added. Voice remains hint once, then Read. No new event recordings or lesson welcome.
- MS-SYS-SE-32/33 are not newly claimed here; this Curiosity remains the second card. The map is outside the authorized edit scope. The eventual integrator must remove any unsupported map credit rather than add a thin activity.
- Mary, al-Kindi and the sensitive history/context are retained. Only the authorized Vicksburg chronology changed. No new sensitivity verdict is claimed; `refine/sensitivity.md` is absent.
- Open questions remain open: reflector A/1930 case, damaged Vicksburg slip, bench-wide shortcut rebinding, spec voice section and Fan layout. No added feature/topic.

#### Cheats tried

- Encode toggle, New key and machine/direction detour on a sealed symbol box, the counting sheet and Poe: only unrelated writing keys appeared. Returning restored the tape/guesses; no box opened by these attempts. Nine attack paths, all closed.
- Splitter lengths 1 to 12 on six short/empty tape sizes:51 insufficient-data cases; Use key hidden and direct clicks inert. Choosing a supported length with enough text remains deliberately useful.
- Grid has no hidden key; its immediate readable output is intentional. Rotor order/rings/cables are public on its box, and its count now includes only the hidden starts. Wheel zero and a weak chosen key remain honestly weak, not falsely secure.
- Weather's known crib producing B O X is the specified open demonstration, not a score. Stop during the paced search canceled it. No success badge or finish was introduced.

#### Voice walk

- Held clicks 120 ms, 2 s gaps. Fresh Read: Drag the inner ring, Wheel, Decode, current shift, output, Counter. One Read log entry. Same result with Sound off and at 680x 425.
- Three increases to shift 3: no stale automatic hint after it disappeared. Output THE DIE IS CAST. Original before log had the late automatic line.
- RAVEN after selecting length 5: Square, Decode, Key A, first 80 output characters, Bumpiness 8.8 at length 5, 5 divides 20 of 23 gaps, implied ENRAVEN at 53. No spoken unit tag.
- `allLines()` equals `voice/lines.json`: exactly Drag the inner ring. Browser speech fallback remains; no audio was recorded. Logs are evidence of started Read/speech, not a new listening study.

#### The real material

- No dataset or historical ciphertext changed. Practice sheets/drawn shapes remain Curio Class CC BY 4.0, code MIT; source and rights records remain in the Manual and `tool.draft.json`. The optimized counts are computed from the same bundled 2,705-byte material file. No corpus, modern prose, photograph or new art imported.
- Chronology rechecked 6 November 2026: [Catherine M. Wright, American Civil War Museum, Message in a Bottle](https://acwm.org/wp-content/uploads/magazine_message_in_a_bottle_article.pdf), printed page 5 gives December 2008 removal and January 2009 photograph; page 7 dates the publicity to December 2010. Compared with [FOHBC, Civil War Message-in-a-bottle](https://fohbc.org/wp-content/uploads/2012/12/CivilWarMessageInABottle_MayJune2011.pdf) and [the museum's educator record](https://acwm.org/wp-content/uploads/ACWM_Vicksburg.pdf), which give inconsistent later dates. The specific curator account is used for opening; an exact decipherment year is omitted. Modern articles are copyrighted, no licence grant assumed: facts are summarized in original words, no article prose/images bundled. The 1863 dispatch itself is public domain. Raw PDFs/fetch record in `data/fix-*`.
- Mathematical changes: key counts are exact arithmetic on the stated hidden settings; coincidence is independently checked against a Python Counter oracle, 120 comparisons with maximum error 0. English percentages, glyph mappings and Enigma wirings retain their named original sources/licence/rights basis in the Manual and metadata.
- Unattended choice: use the source-confirmed publicity date rather than asking about the conflicting decipherment year. Curiosity voice and open exploration override lesson expectations throughout.

#### Engine changes wanted

None. Shared kit, scripts and docs were not changed. All repairs are local to this tool.

#### Audit

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

#### Left open

- Should fix 6: strict sustained 60 fps under the worst tested 4x workload is not proved. Static reference drawing is repaired; slow frames remain.
- Compact rotor keys/ring controls are smaller than 44 px so the full instrument fits 680x 425 and 375x 812; desktop targets and keyboard access remain. Phone plate text is now 10 px after the audit repair. Do not describe these as a fully target-size-clean audit.
- Pending fresh sensitivity review, spec/map questions above, recorded gravel-ranger voice and physical Chromebook measurement are outside this repair's completed claims.
- The first phone-before capture targeted the host by mistake; it is explicitly not used as a before proof. Early temporary oversized nested chart glyphs were caught in viewed frames and repaired with explicit SVG viewport dimensions; `last-phone-labels` and `last-poe-sorted` verify that repair.
- No commits, uploads or deployment. `refine.md` and its review folder were left untouched. Final source is one offline file; automatic network code absent, em dashes 0. Lesson-word hits: score only means coincidence statistic, points only means geometric fixed points.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Cipher Workbench handoff

#### Refine repairs, 6 November 2026
This checkout now includes the round-one repairs and bounded reproduction helpers under `_scratch/cipher-vault/fix-*`. Use `polish.md` for the verified disposition; the older build and cold-review sections below are history. No commits or deployment were made.

Encode on Symbols now opens a separate writing workspace and stores the cipher workspace in local state, including guesses. Machine switching also enforces this boundary. Sealing opens the new box with hidden settings reset. Rotor boxes disclose order, rings and cables, so their seal card counts only 17,576 starts. The Counter defaults to ciphertext, labels actual glyphs, and uses the counted letter alphabet for pasted prose. Splitter key guesses require ten letters per column and an explicitly selected length. Square builds its reference letters once. Rotor typing takes letter keys throughout its page, and rings are two-digit keyboard dials.

Compact rotor controls trade target area for showing the complete lampboard and 26 typing keys in the specified short previews; all keys remain focusable and desktop keys remain 44 px. The mechanical audit's small-target leads must be read with this explicit limitation. Historical sensitivity text, except the corrected Vicksburg date, is retained as the settled call requires. The pending fresh sensitivity review is not claimed as passed.

The single fix audit completed with 252 raw leads and no interaction/resize exceptions. Its confirmed desktop ring-height and phone plate-size leads were repaired and re-shot. Rings are 44 px tall on desktop, with a side transport at 1280x720 to keep all typing keys visible; the phone plate is 10 px. Bombe events now render before scrolling its survivor into view, preventing a newly added message from pushing that control below the panel. The survivor is fully visible and hit-testable at 1366x768, 680x425 and 375x812 in `fix-audit-repair`.

The strict 60 fps requirement remains open. The repaired Square retains its tableau/bar nodes and matches 120 independent coincidence calculations, but the 600-letter, three-tool, 4x Encode stress probe still has slow frames: median 16.7 ms, p95 33.4 ms. The report marks that should-fix NOT FIXED in full. Do not claim an exit PASS or school-hardware certification from this repair.

Build only. No commit, deployment or polish round was performed. All evidence and helpers are under `_scratch/cipher-vault/`.

#### Source map
`src.html` contains instrument CSS, semantic controls, exact SVG material, cipher mathematics, analysis instruments, local boxes and source Manual. `material.json` is loaded by the bundler's json token. The finished `cipher-vault.html` is one offline file. `_scratch/cipher-vault/pack.py` reproduces the material from the owner spec and gathered original texts, including a printed-cryptogram assertion for Poe.

#### Tricky parts
Enigma steps before encryption and uses displayed-letter notch positions independently of ring offsets. The two forward and reverse transformations include the ring offset; double stepping is intentional. Crib search uses binary lifting to skip to a crib offset, then rejects mismatches early. The search is cancellable and snapshots settings so no stale results should be applied.

Symbols and pigpen are stored as private-use character tokens and drawn exactly as SVG on tapes. The Leeson variant is three grids with shared I/J; the standard pigpen alphabet has two grids and two crosses. Poe's dash is rendered as a short rule; no em dash is used. Notes and keys are not sanitized into HTML without escaping.

#### Spec decisions
The Curiosity brief overrides old lesson shaping, score and automatic event speech. The report is written last, because the user's explicit stop-on-report instruction overrides the regular brief's instruction to start it early. The user required seven preview lines rather than the prior build convention. No painted images were necessary for the exact working mechanisms.

The incompatible 1930 reflector-A case is omitted as explicitly permitted. The source check changes Leeson's grid and the Vicksburg transcript. Hard-history context is plain; a cold reviewer must still assess its sensitivity before a live push. This build does not push anything live.

#### Engine changes wanted
None required. The kit has no selector for the requested gravel-ranger bank voice without recorded clips; this build uses the permitted browser fallback and identifies that limitation in the Manual.

#### Cold review repairs, 2026-11-05
Fractional ring/period values are rounded and clamped, including saved settings. Input letter counts use the tape's alphabet independently of analysis selection. Bombe candidates are invalidated on material/settings changes, and a candidate found on Output transfers that source to Input before Run. Rotor setting edits start a fresh typing session and label the existing output as pending Run. Empty cribs do not imply a valid match.

Newly opened tools scroll into the analysis panel. Compact controls retain 44 px targets with local key-bank scrolling; rotor transport remains pinned inside its box. Window drums accept real vertical drags, taps and Up/Down/Home/End, so all three starting windows fit the compact box. The tableau now has legible reference letters and an enlarged actual crossing. Counter coordinates follow its real pixel size. Symbol and repeat-factor keyboard focus survive redraws. Read retains the quiet Curiosity voice policy.

Review evidence is prefixed `review-` in Scratch. The old build audit and its remaining-limit prose below describe the pre-review build; use the cold review report and review-audit for current disposition.

The cold review's single audit completed in 844 seconds with 88 raw leads. Confirmed tape/crib target, source-label and panel-access issues were repaired and checked in thirteen targeted states, with no full audit rerun. `review-audit-response.md` distinguishes actual faults from SVG hit-test artefacts, intended modal coverage, long reference banks and inapplicable lesson welcomes. Final extreme-tape checks also keep the first bar's 600 label inside the chart and the tape-limit message inside its header. The 52 functional assertions, 100 independent rotor vectors, six seal-estimate cases and 602-second walk are retained. Local 4x frame intervals averaged 16.94 ms, maximum 50 ms; no strict school-hardware certification is claimed.

#### Sensitivity
The cold review retains REMEMBER DEATH as the brief leans, without gore. Vicksburg's case history names the Confederacy's defense of slavery and keeps the dispatch's sender attribution tentative; no historical outcome is scored. Poe's cryptogram is fiction, and the bench does not reproduce the story's racist character dialogue. Al-Kindi is credited with the oldest known description rather than declaring an absolute first. Mary's 1578-1584 letters are distinguished from the 1586 trial evidence; the 1587 execution is stated plainly. A cultural reviewer should check these framings and the attribution of non-European cryptanalysis. No people imagery is used.

#### Build verification and remaining limits
The independent Python oracle and browser checks are in Scratch, including 100 varied rotor vectors, reciprocal transforms, six machine round trips, real wheel input, the 27-spot weather search, the six-order 105,456-setting search, box persistence and confirmations, Unicode pass-through, input limits and 4x CPU measurements. `play-log.json` records 600 seconds and 120 input sequences without exceptions. It is an automated instrument walk, not a recruited child/adult study.

The single mechanical audit has 356 snapshot leads. `_scratch/cipher-vault/audit-response.md` answers every category and distinguishes subsequent build fixes from remaining limits. Compact key banks and some short-screen controls are below 44 px. The Counter fader and multiple tools can need internal scrolling. The short-preview tableau is small. Actual school Chromebook hardware remains unmeasured. These limits are carried forward explicitly; this is not an audit-clean or release-ready claim.

Final build fixes include the SVG ring pivot, thumbwheels incrementing the displayed window, retained bombe statistics after Run, ASCII-only case folding, bounded large-key scientific notation, visible phone rotor transport, accessible symbol mapping labels, Counter glyph selection and preserving the Peek mark after a later match. The final smoke frames are under `_scratch/cipher-vault/latest/`.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-07)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-07)
- 2026-11-25: refine.md folded in (last changed 2026-11-07)
- 2026-11-25: refine/craft.md folded in (last changed 2026-11-07)
- 2026-11-25: refine/play.md folded in (last changed 2026-11-07)
- 2026-11-25: refine/teaching.md folded in (last changed 2026-11-07)
- 2026-11-25: polish.md folded in (last changed 2026-11-07)
- 2026-11-25: handoff.md folded in (last changed 2026-11-07)
