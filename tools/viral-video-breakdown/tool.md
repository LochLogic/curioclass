# Viral Video Breakdown: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: viral-video-breakdown

#### Built

Three modes for grades 6-8: label an eight-shot film, investigate its five reposts, then write an evidence-informed ethical verdict. Eight original paintings, original synthesized music/effects, live synchronized comparison, a redrawable copy tree, finding chips, three checked claims, local saves and copied verdict text are implemented.

The kit owns motion, sound settings and narration. No family engine, network dependency, commits, shared-file edits or polish round. Deliverables and evidence stay in the two authorized tool and Scratch folders. Handoff documents every unattended interpretation.

#### Numbers check

- Independently recomputed: 2+3+2+3+2+2+3+3 = 20 seconds; deleting the end card gives 17; 17/1.25 = 13.6. Posting times 0,6,9,14,20,26 hours strictly increase. See `../../_scratch/viral-video-breakdown/numbers.json`.
- Shared comparison time is original time. R5 clip time is original time/1.25. Real drags on either clock moved both; original 17 seconds maps to R5 13.6 seconds.
- The unspecified frame rate is assumed to be 30 fps: the four-frame sticker edge lasts 0.1333 original seconds. This is in handoff, not a new case fact.
- WCAG recomputation: ink/background 16.006, ink/panel 14.313; muted/background 7.973, muted/panel 7.129; brand/background 5.675, brand/panel 5.075; missing/background 10.383; added/background 11.417. Rounded spec values agree.
- Final embedded HTML: 1,221,409 bytes, 1192.78 KiB. Art: 836,324 bytes, 816.72 KiB. Voice assets: 0 bytes. Total is below the 2 MB goal.

#### Facts checked

The following are fictional case facts from `spec.md`, Content, not claims about real people or videos. Content arrays and independent expected test arrays were compared.

| Student-visible case fact | Source and verification |
|---|---|
| Nina is 13; original @ninabakes, Grandpa's 5 a.m. bread, portrait 9:16, 20 seconds, 42,000 views in 30 hours | Spec Content original; rendered title, metadata and duration checked |
| Grandpa Teo, 42 years baking; up at four; bread rising before others wake; patience; favorite smell | Spec original VO and end card; four captions placed on shots 1,2,6,7 only, never narrated as dialogue |
| Street: wide, eye level, ambient+VO, sets place, 2 seconds; Nina wants it to feel early | Spec shot 1; exact label result and note checked |
| Dough: close, high, VO, shows work, 3 seconds; flour looks like snow | Spec shot 2; exact label result and note checked |
| Trays: wide, overhead, music, time passing, 2 seconds; overhead shows how many | Spec shot 3; exact label result and note checked |
| Oven: medium, eye level, effect+music, makes you feel, 3 seconds; glow is best | Spec shot 4; exact label result and note checked |
| Crust: extreme close, eye level, effect+music, makes you feel, 2 seconds; phone close for sound | Spec shot 5; exact label result and note checked |
| Apron: close, eye level, VO+music, makes you feel, 2 seconds; older than Nina's mom | Spec shot 6; exact label result and note checked |
| Shelves: medium, low, VO+music, time passing, 3 seconds; bread looks like skyline | Spec shot 7; exact label result and note checked |
| End card: graphic, n/a angle, music, gives credit, 3 seconds; maker and subject named | Spec shot 8; graphic/n/a choices and credit checked |
| R1 @breadlovers_daily, +6h, 310,000 views, original source, via sticker, credit/meaning kept, asked by message, no money | Spec repost row R1; captions, card, comparison and verdict record checked |
| R2 @hustle.mindset, +9h, 2,400,000 views, copied R1, crop/sticker remnant/end cut/new music, false office-job-at-50 story, no credit/permission/money | Spec R2; crop, four-frame remnant, audio, caption and record checked |
| R3 @dailyfeels, +14h, 1,100,000 views, copied R2, same crop/music, RIP on shot 7, false closure story, no credit/permission/money | Spec R3; sticker, caption, audio and record checked |
| R4 @citynewsnow, +20h, 650,000 views, original source, full credit/end, false saved-bakery banner, meaning stretched, no permission, account ads | Spec R4; banner, retained credit, caption and record checked |
| R5 @flourpower_shop, +26h, 90,000 views, copied R3, 1.25 speed, flour logo over RIP remnant, same music, advertising, no credit/permission, flour sales | Spec R5; mapped clock, logo/remnant, caption, audio and record checked |
| Nina welcomed appreciation but rejected the invented office job and unasked flour ad; she wants her name and story right | Spec Nina statement, displayed first in Verdict as one perspective |

Educational sources were checked live: [Library of Congress motion-picture guide](https://www.loc.gov/static/programs/teachers/getting-started-with-primary-sources/documents/Analyzing_Motion_Pictures.pdf) supports observing image/sound and interpreting intent; detailed shot labels come from the spec, not an invented quotation from that guide. [NCAS](https://www.nationalartsstandards.org/) supplies the listed Re7, Re8, Re9 and Cn11 strands. [Common Sense giving-credit lesson](https://www.commonsense.org/education/digital-citizenship/lesson/lets-give-credit) supports attribution responsibilities. [Copyright Office](https://www.copyright.gov/what-is-copyright/) supplies creator-rights context in teacher notes. Student fairness choices are ethical judgments, not legal fair-use rulings.

Exact account-plus-case-caption searches for all six returned no matches. This is limited index evidence, not proof that no active account exists anywhere. All accounts and counts are explicitly fictional, with no profile links. The spec names were retained; this verification limitation remains open.

#### Break it

`postfix-functional.json` records 149 assertions. An independent expected-case oracle tested 18,630 card/clue-pair combinations, including repeated clues. Only four legitimate evidence sets across the three questions passed; no false accept occurred.

- Shot check: empty picks, wrong picks, omitted sound and every sound-option combination. Multiple sounds require exact matching; wrong choices display chosen/correct labels and Nina's note. Checking all eight unlocks a summary, not a mastery score. Rechecking does not inflate a count.
- Findings: repeatedly opened the same tool and reversed the same pair. Both retain one unique type+unordered-pair chip. Unopened findings cannot prove a claim.
- Claims: empty/one clue, duplicate clue, wrong card, unrelated pair, right words with wrong evidence and a bag of clues. Make is disabled below two; exactly two attachments are allowed. Card and pair/type evidence must both prove the question. Wrong attempts give a specific tool/pair nudge. All three supported claims passed through held clicks.
- Arrows: future parent and self refused; redraw replaces the one parent; the complete correct tree can be drawn. Earlier wrong parents are permitted as hypotheses and do not satisfy claim proof by themselves.
- Verdict: unexplored credit/meaning stay unknown. Asked/money are given case facts. Selecting all obligation chips cannot coexist with nothing. Judgment and prose earn no score; Copy labels incomplete work as a draft. Student reasons are escaped, capped at 100 characters and copied as text.
- Save/Reset: labels survived browser restart. Cancel kept work; confirm cleared labels, arrows, findings, claims and verdicts. Final focused Reset check also verified the visible mode and selectors resynchronize. Storage is guarded by try/catch and device-only wording is visible.

The broad functional run precedes the last presentation and Reset synchronization edits. Those edits received focused checks; a second broad audit was not run.

#### Voice walk

Fourteen guide lines match `voice/lines.json`; curious-librarian/Aoede is configured. No recordings were made, as required. Browser speech fallback and kit speech logs were exercised; there is no claim of recorded-bank listening quality.

Held-click main path: welcomeVideo; Play makes that welcome stale; checkHow on first labeling; allShots after eight checks; welcomeReposts; comparison how; arrow how; claim how; claimRight for each of three supported questions; welcomeVerdict; verdict how. Actual text and ordered event logs are retained in `walk/`. Picker guidance was tested separately after its layout change: Choose findings, picker how, Back to claim.

Five refused-arrow events at a two-second pace each started immediately. Five repeated how triggers produced one how line. Claim events use the same immediate-event path, and the full walk heard claimRight for all three questions. Three focused mode-retap tests produced one uncut welcome each after fixing active-mode reentry.

No guide line started during clip playback in two-second checks or the full 20-second run. The full film ended at 20 with no owned audio nodes; stopped and cropped tracks also left zero nodes. Pair changes during playback did not start speech. Read stops the clip and updates the hint before speaking it. Motion off preserved a two-second content clock and suppressed idle movement.

#### Feel check

Played the whole case with held clicks: eight checked shots, summary, six opened tools, five arrows, three proved claims, five reasoned verdicts and Copy. Clipboard feedback was Verdict copied. This was the student-path run, not just direct state injection.

Best moment: scrub to the shelf and uncover the RIP corner under the flour logo, then see it line up despite R5's faster playback. The art, crop outline and matched music give the inference a physical payoff.

Two flattest moments were hunting for offscreen feedback after a shot check and managing a long pile of clue chips. Compact feedback now floats over the film, and Choose findings opens a compact two-selection picker. The final phone claim button ends at y749.7 in 375x812; the tree remains stable across a five-second test. Narrow Verdict uses readable records instead of broken table words.

Snowy Mail Route and Beat Lab were bundled/opened from Scratch copies. `feel-comparison.jpg` places this tool beside Beat Lab; both the comparison and eight-image contact sheet were inspected. The paintings carry the atmosphere without points or confetti. The investigation sustains the session better than repeating shot labels; later rounds change from visual analysis to provenance and then ethical judgment.

#### Done when

| Spec item | Result and evidence |
|---|---|
| 1. Dominant player/strip and case cards/tree at 1366x768 and 680x425 | PASS: captured all three modes at both sizes; film is central, six cards/tree are the case focus. Summary intentionally overlays the film. |
| 2. All eight checks match Content | PASS: independent expected arrays, all sound combinations and Nina notes in 149-assertion suite |
| 3. Live jumps/Stop; locked Compare; R5 mapping | PASS: held Play/thumbnail/Stop, native drags on both clocks, 17 to13.6 end mapping |
| 4. Answer-pair differences and correct chips | PASS: actual Compare, Sound and Captions tools opened; crop, sticker, credit, music, caption and logo clues checked; duplicate/reversed chips rejected |
| 5. Refuse future; draw correct tree | PASS: future/self refusals plus full five-arrow tree and redraw tests |
| 6. Correct card plus two proving clues only | PASS: 18,630 adversarial combinations, four valid sets, all three claims in held walk |
| 7. Case-derived table, Nina first, Copy | PASS: unknown before evidence, known after arrow+finding, given permission/money facts, held copy and draft checks |
| 8. Speech exclusion and repetition | PASS: full-film and two-second no-speech tests, five how repeats once, five refused events heard, three claimRight events in full walk |

These passes name their evidence snapshot. Final summary hint-only and final caption visual captures remain incomplete as described below.

#### Wave lessons

| BUILD.md lesson | Result and check |
|---|---|
| Hint and voice | PASS: immediate panel hints, Read stops/updates first, V.heard how guards, two-second refusal walk; final summary hint source updated, reshoot incomplete |
| Focus and layout | PASS: keyboard-only mode path, focused control preserved, native modal return focus, stable hint height and Sound/Read widths; thumbnail duration overlap fixed |
| Sizes | PASS for inspected states: all three modes at 680x425,800x500,1000x625,1280x720,1366x768,1920x1080,760x900,375x812; zero horizontal overflow. Real host phone captures and 44 px primary controls. Phone document scroll reaches footer; Verdict records have their own scroll. |
| No giveaways | PASS: no correctness flags on cards, no score, inference requires evidence rather than word matching; wrong combinations fail even with the right card |
| Honest numbers | PASS: fictional metrics labeled, waveform explicitly illustrative, original-time alignment and separate R5 clip clock; no invented confidence meter |
| Standards | PASS: students analyze shot/sound choices (Re7), interpret changed intent (Re8), apply criteria and reasons (Re9), judge credit/permission/commercial context (Cn11) |
| Motion off | PASS: idle loop disabled, mode/arrow changes immediate, content timing retained; all art present |
| Short choices stay visible | PASS in focused checks: category tabs expose each short label set; picker fits up to twelve findings at680x425; over twelve scroll as a growing collection. Five separate verdict records scroll, while closing choices and Copy remain visible on phone. |
| Resize mid-animation | PASS: audit resize stress completed without exception or locked controls |
| No delayed welcome | PASS: no welcomeAfter; first actions stale the intro; active-mode retaps now preserve one welcome; final three-mode tests show no cut |
| Unknown as unknown | PASS: credit/meaning require case work; no invented known result before evidence |
| One look, one meaning | PASS: missing amber and added green each have word labels; original/source/destination markers remain distinct; grayscale frame inspected |
| Badge says what is true | PASS: checked-shots counts checks, supported-claims counts proofs, no fairness/completion grade; draft Copy labels omissions |
| State hints change back | PASS: close comparisons/picker returns appropriate hint; final Reset clears feedback and returns visible Video; pending arrow cancels on mode change |
| No answer by copied words | PASS: evidence gate needs specific pair/type relationships; correct answer text plus unrelated clues fails |

#### Audit leads

One audit completed within its 40-minute limit on port9981/host8785. It emitted 169 leads on the pre-fix snapshot. `../../_scratch/viral-video-breakdown/audit-dispositions.md` answers every raw bullet and flagged walk row individually: 186 disposition entries, zero unclassified. Repeated sizes share fixes; the audit was not rerun.

- Fixed: end-card thumbnail/duration collision; offscreen compact Reset; tiny/overlapping miniature graphics; Via annotation collision; singular finding grammar; modal opacity; same-mode welcome cuts; header Sound width shift. Final targeted captures or geometry checks cover the relevant fixes.
- Intentional: captions in board previews truncate with ellipsis, full title/accessibility text and Captions tool; tiny painted previews are presentational while Compare is readable; background text behind dialogs is covered; summary occupies the film; RIP corner/logo overlap is the clue. Five verdict records are a scrollable record set, not hidden competing answer options.
- Tree keep-region flags included its own legend. Final bounds were visible at680x425; phone SVG block sizing also stopped a ResizeObserver growth loop, proven stable at346 px case height.
- Intro lines cut by Play/thumbnail/first labeling or opening a clue tool are intentional staleness. Actual repeated-mode cuts were fixed. Motion-off and resize-stress audit stages were clean.
- FAIL: audit phone attachment returned iframe context not found. Three orphan host children on8785 were found later; collision is a likely cause, not proven. Clean independently hosted final phone checks passed afterward. This does not turn the failed audit attachment into a pass.

#### Frames looked at

All-size three-mode matrix, film/result/summary, all eight art assets, key answer-pair comparisons, caption and sound panels, tree, claims, evidence picker, unknown and completed Verdict, phone modes, keyboard focus and grayscale were inspected. All 68 audit PNGs were reviewed through twelve contact sheets, with critical original frames opened separately. Every successful capture batch was reviewed, including the final375x812 claim frame. Failed captures produced no frame to inspect.

Evidence locations: `frames/`, `walk/`, `side-frames/`, `postfix-frames/`, `last-frames/`, `final-smoke/`, `sheets-audit/` and `feel-comparison.jpg`, all under the authorized Scratch folder. Successful capture runs reported zero JavaScript exceptions, console errors or warnings; driver disconnections are recorded separately.

#### Art made

Eight OpenAI image-tool paintings in a consistent warm cinematic gouache style: street, dough, overhead trays, oven, crust, apron, sunrise shelves and detective desk. Seven9:16 shots and one16:9 backdrop. Each has `people:false`, no cutout and Codex generation provenance. End card, text and analytical overlays are code.

All eight were generated during Build, inspected, converted only through `scripts/art.py --rekey`, and embedded. No redraws were needed. Originals and prompts are retained. Art816.72 KiB; total1192.78 KiB; recorded voice0 KiB against the2 MB goal. The user's image-tool instruction takes precedence over the spec's local-FLUX preference.

#### Art still to paint

None. No people are drawn, consistent with the spec. No labeled art placeholders remain.

#### Engine changes wanted

None. The host cleanup correction is in the tool's Scratch helper only; no shared script or kit edit.

#### Left open

- Fixed voice assets intentionally unrecorded under the brief. Fourteen lines are supplied with browser fallback; recorded voice quality is not verified.
- Final summary hint-only visual reshoot failed by CDP timeout, then connection reset. Prior summary layout and actual student path exist, but that last visual check is open.
- Final caption placement capture timed out. The exact final source renderer passed Node syntax and all eight caption-presence checks, including text on shots1,2,6,7; this is not a substitute visual capture.
- Audit is a pre-fix snapshot with a failed phone attachment. It was not rerun. Last presentation and Reset changes have focused evidence rather than a fresh full audit or full-path rerun.
- Negative public searches cannot establish that all six handles are inactive across every platform. Fiction labeling is explicit; the stronger spec account-verification claim is not made.
- The initial read of the mandatory brief was a short unbounded command (0.15 seconds). Subsequent implementation/test shell commands used hard timeouts, including120-second bundles,300-second drive batches and2400-second audit. This initial procedural exception is recorded rather than concealed.

Final checks found no external resources, unresolved art/kit tokens, em dashes or temporary host.html. Maximum source line152 characters. All ports9980-9987 and8785 are closed; owned process cleanup reports zero remaining. Final bundle SHA-256: `e72801dc379ff2f7237dac8f3d6f4cbee461bff403f1c9be3f865439861dc1ee`. Evidence map: `../../_scratch/viral-video-breakdown/README.md` and `validation.json`.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: viral-video-breakdown
#### Played
Cold grade-7 play preceded the builder report, handoff, notes and source. Played the film, all eight labels, comparisons, three claims, five arrows and verdict. Strong bakery atmosphere and inherited-edit reveal; finishing the verdict felt flattest. One review pass, no commits, project edits confined to the tool and its Scratch folder.
Review verdict: BLOCKED by the claim-guessing route described below.

#### Findings fixed
- Should fix, general, The reposts: wrong-claim nudges supplied exact answer-pair recipes. Replaced them with specific observation prompts without card IDs or attachment recipes. The deeper guessing blocker below remains.
- Should fix, general, The video/voice: eight wrong checks triggered “Now you know” and green checkmarks. The event now accurately describes inspection, and thumbnail badges say “notes,” with accessible “not a score” text. Summary remains unscored, as specified.
- Should fix, general, laptop verdict: tall call/reason rows hid later reposts. Put those controls beside each other; all five rows fit at 1280x720 and 1366x768 without shrinking 44 px targets. Small viewports retain readable scrolling records.
- Should fix, general, modal access: opening evidence, findings or Reset made the header Read control inert. Added the same Read action inside each dialog; Read stops a playing pair before speaking. Reset now supplies a current action hint, and Cancel/Escape restores the old hint and stops stale Read.
- Should fix, general, copied-state truth: editing a copied verdict left “Verdict copied” visible. Edits now invalidate that status and old fallback text; an async copy of an older draft is identified. An unselected closing obligation also keeps Copy labeled as a draft.
- Should fix, general, audit repairs: separated via credit from its annotation at 680/800 and checked 1366; kept Make and supported status inside 680; raised summary timings and phone comparison watermark to 10 px; fitted the phone end-card name. Covered summary controls are now inert, the old note closes, and Back restores Play focus. The phone fallback is selected, read-only, scrollable text with all 338 test characters accessible.
- Polish, general, flattest moment: the closing card now visibly assembles the student's own obligations into a sentence. Compact landscape hides the duplicate sentence to keep Copy visible.
- Polish, general, weakest art: redrew shot-crust as a tighter crust-height macro with cooling fissures, flakes and blisters, preserving amber/blue light and the painted bakery style. Kept the other seven paintings and all analytical graphics.

#### Findings left
- **Blocker, general, claims:** opening the required two findings and cycling answer cards can earn a supported claim without interpreting evidence. Reproduced through actual UI controls before and after the scoped fixes. The spec mandates findings on opening and card-plus-two-clue validation. An observation/explanation response gate would be a new mechanic; CODEX-REVIEW says not to add it. Teacher notes and handoff now explicitly identify this assessment limit. **Not ready as a mastery check.**
- Polish, general: five verdict records still require scrolling in preview/phone layouts. Their own call choices are native selects; the closing choices and Copy remain visible. Kept the readable record treatment rather than squeezing the text and controls.

#### Break it
- Shot checks: tried empty picks, the first option everywhere, wrong categories, every sound subset including all four, and repeated checks. 128 independent sound combinations matched the maker table. All-wrong work opens only the specified inspection summary, now without mastery praise. Rechecks do not inflate a score; none exists.
- Findings: reopened one tool repeatedly and reversed its pair; one unique unordered-pair/type chip remained. Same-card comparisons create no clue. The spec's on-open collection is the claim blocker, not evidence of interpretation.
- Claims: empty/one, duplicate, unopened and irrelevant clues fail; 18,630 independent question/card/clue combinations produced exactly four legitimate evidence sets, zero logic mismatches. Nevertheless, correct evidence plus cycling cards reaches acceptance: blocker left above. Removing the exact recipe from failure feedback does not erase that result.
- Arrows: future and self sources refused; earlier wrong sources remain explicitly labeled hypotheses. Redrawing replaces one parent. Held clicks completed Original->R1/R4, R1->R2, R2->R3, R3->R5, with arrows pointing back from copy to source.
- Comparison clocks: real whole-pixel drags on either slider, including traversing the track, kept both at 14.50 original seconds and R5 at 11.60 clip seconds. Sweeping changes the view; it awards no score.
- Verdict: tried every obligation including nothing; nothing excludes other obligations. Empty or incomplete work copies as a draft. Five calls/reasons without obligations also remain a draft. Correctly labeled copies become edited after changes. No semantic grading of fairness or prose is claimed. HTML-looking reasons stay escaped; input limit is 100 characters.
- Reset: Cancel/Escape keep work; confirmation clears the saved case. Read names the current confirmation choices. No best score, hidden completion award or reflection assuming an unmade mistake exists.

#### Voice walk
Sound on, default settings, real 120 ms held clicks with 2 s gaps. Film: Play, Stop, all eight labeled/checks, How it works. Reposts: pairs, Compare/Captions/Sound, arrows, findings, three supported claims. Verdict: Nina first, native keyboard call, reasons, obligations, Copy. Bounded batches reload the saved case; welcome/how counts below are per page load.
Actual started lines: checkHow, allShots; welcomeReposts, compareHow, arrowHow, claimHow, chooseFindings, claimRight, welcomeVerdict, verdictHow. The first Play skips welcomeVideo as BASELINE 16 permits; its premise remains in the hint and Read. Remaining claim batches heard their appropriate instructions and claimRight. No guide speech started during content playback. Lines cut when their next real action made them stale are recorded, not mistaken for uninterrupted playback.

| Line | Kind | Expected / heard in repeat test |
|---|---|---|
| checkHow | how | 1 / 1 across five selections |
| arrowRefused | event | 5 / 5 |
| claimRight | event | 5 / 5 |
| claimNudge | event | 5 / 5 |
| compareHow, arrowHow, claimHow, chooseFindings, verdictHow | how | once per applicable page walk |

Modal Read stopped pair playback, spoke the stopped-state hint and left no queued line. Fourteen catalog lines match allLines; no recordings were made. Browser fallback timing was tested, not bank-recording quality.

#### Facts checked
Specific people, captions, accounts, counts, edits and statements are fiction authored by Curio Class, checked against the named Content rows in [spec.md](spec.md), not asserted as real events.

| Fact | Named source and check |
|---|---|
| Nina 13; @ninabakes, Grandpa's 5 a.m. bread, 9:16, 20 s, 42,000 views/30 h; Teo's 42 years, up at four, patience and favorite smell | Curio Class spec, Original/voice-over/end card; exact displayed data and four caption placements checked |
| Shot 1: wide/eye level/ambient+voice-over/sets place/2 s; early note | Curio Class Content shot 1; independent expected labels and note |
| Shot 2: close/high/voice-over/work/3 s; flour like snow | Curio Class Content shot 2; independent labels, note and painting |
| Shot 3: wide/overhead/music/time passing/2 s; number of loaves | Curio Class Content shot 3; independent labels, note and overhead painting |
| Shot 4: medium/eye level/effect+music/feeling/3 s; oven glow | Curio Class Content shot 4; independent labels, note and painting |
| Shot 5: extreme close/eye level/effect+music/feeling/2 s; close phone for crackle | Curio Class Content shot 5; labels, note and revised outside-crust image |
| Shot 6: close/eye level/voice-over+music/feeling/2 s; old apron | Curio Class Content shot 6; independent labels, note and painting |
| Shot 7: medium/low/voice-over+music/time passing/3 s; bread skyline | Curio Class Content shot 7; independent labels, note and low-angle painting |
| Shot 8: graphic/no camera angle/music/credit/3 s; Nina and Teo named | Curio Class Content shot 8; exact check and end-card text |
| R1: +6 h, 310,000 views, from Original, via sticker, credit/meaning kept, asked, no money | Curio Class repost R1; card, caption, frame and given verdict facts |
| R2: +9 h, 2,400,000 views, from R1; cropped name/sticker, removed end, changed music/false office-job-at-50 story; no credit/asking/money | Curio Class repost R2; first-frame remnant, captions, sound and claim proof |
| R3: +14 h, 1,100,000 views, from R2; same crop/music, added RIP, false closure; no credit/asking/money | Curio Class repost R3; shot-7 sticker, caption and sound |
| R4: +20 h, 650,000 views, from Original; name/end retained, false saved-bakery banner, no asking, account ads | Curio Class repost R4; board/banner, full frame and given verdict facts |
| R5: +26 h, 90,000 views, from R3; same crop/music, flour logo over RIP corner, 1.25 speed; no credit/asking, flour sales | Curio Class repost R5; aligned clocks, inherited corner, caption and proof |
| Nina liked the appreciation but rejected the invented job story and unasked ad; wants her name and story right | Curio Class Nina statement; exact text shown first, as one perspective |
| 20 s total; 17 s without end card; 17/1.25=13.6 s; increasing 0,6,9,14,20,26 h; contrast values | Independent numbers.py recomputation against spec Sources and its WCAG formula; all match |
| Observe visual/sound details, infer purpose and question provenance | [Library of Congress, Analyzing Motion Pictures](https://memory.loc.gov/static/programs/teachers/getting-started-with-primary-sources/documents/Analyzing_Motion_Pictures.pdf); precise maker labels are the fictional notes, not a LOC quotation |
| Re7 analysis, Re8 interpretation, Re9 criteria, Cn11 societal context | [National Core Arts Standards](https://www.nationalartsstandards.org/); each is practiced in labeling, provenance or reasoned verdicts |
| Credit recognizes creators and shows respect | [Common Sense Education, Giving Credit](https://www.commonsense.org/education/digital-literacy/giving-credit), checked live |
| Original human-authored fixed works have copyright; permission/credit and legal exceptions are distinct | [U.S. Copyright Office, What is Copyright?](https://www.copyright.gov/what-is-copyright/), checked live; the tool's ethical choices are not legal rulings |

#### Sensitivity
No Native, cultural-tradition, religious, hard-history or body content. No people appear in these deliberately observational bread shots. A sensitivity reviewer should confirm the false RIP sticker cannot be mistaken for an actual death announcement and that family work and a young maker's rights are treated respectfully. Handle searches found no evidence of this fictional case but cannot prove global inactivity; accounts are explicitly fictional and unlinked.

#### Flattest moment left
Repeated four-category labeling is slower than the inherited-edit investigation. Kept the specified eight-shot analysis and no-score feedback. The closing sentence now reflects the student's choices; no extra game or topic was added.

#### Graphics
All eight paintings, code end card, crop/credit/sticker/logo/banner overlays, waveform, arrows and phones inspected, including maximum-size art sheets, 680 preview, laptop and true 375 iframe. One crust redraw, no missing art or people flags. OpenAI built-in [imagegen skill](/C:/Users/Cory/.codex/skills/.system/imagegen/SKILL.md); full prompt in art/prompts.json, selected raw in art/raw/shot-crust.png and final art/shot-crust.webp. Bundle 1,264,595 bytes (1235.0 KiB); art 865,282 bytes (845.0 KiB). No graphics were stripped to clear checks.

#### Audit
The one final audit completed within its 40-minute deadline: 154 mechanical leads, 100 PNGs inspected, zero console errors. Motion off, mid-action resizing, one held click per control, repeat and quick-tap tests were clean. The confirmed geometry/type/focus repairs above received focused re-shoots, not a second audit. Compact summary was reached by scrolling to its button; its Shift-Tab lands on Read and Back returns to Play.
Every raw lead has a disposition in [_scratch/review-audit-dispositions.md](../../_scratch/viral-video-breakdown/review-audit-dispositions.md). Preview caption ellipsis, scrolling verdict records, phone footer Reset and modal background occlusion are intentional; thumbnail-box intersections and the unused SVG legend region are geometry false positives. Seventeen first-tap welcome flags are permitted by BASELINE 16, with premise available in hint/Read. Two added state fixtures assigned both selectors before dispatching Change; the first handler reset the second value, invalidating their focus/disabled-control leads. Corrected sequential fixtures directly reached R3/R5 ad trace and all three supported claims. Shared audit improvement is named in handoff; shared scripts were untouched.

Wave lessons checked directly: hint/Read and restored hints; focus through rebuilds and stable held-click layout; 44 px targets and all prescribed sizes; no-giveaway tests (claim blocker remains); honest timing/fictional counts and hypothesis arrows; solo standards tasks and matching notes; no infinite calm animations. Short label/obligation sets remain visible; long verdict records scroll. Resize is clean, welcomes do not arrive late, unknown parentage stays hypothetical, amber means missing and mint means added, badges say notes, and nudges no longer prescribe answer-card matches. Main-path hearing and independent event repeats are documented above.

#### Left open
The claim-guessing blocker needs a spec decision permitting an independent observation response. Do not infer a shipping pass from this review. Recorded voice quality remains unverified under the no-recording rule. The initial brief/memory reads lacked an explicit timeout wrapper; malformed command strings also failed immediately. Subsequent executable checks used hard child-process deadlines. A first host-only favicon 404 was removed from the test harness; the repeated phone check had zero errors. No commits or shared-file edits. Unattended decisions followed the spec: preserve the defined claim mechanism, report its blocker, and retain readable scrolling for independent verdict records.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Viral Video Breakdown build handoff

#### Structure

src.html starts from the kit starter and retains its kit stylesheet, script, modes and shared controls. Tool CSS lays out at actual viewport size. Content tables are SHOTS, CARDS, CAPTIONS and NINA. Rendering, playback, evidence, claims and verdict logic follow those tables. All student text is escaped before insertion. The built HTML embeds every asset.

The case has no family engine. Curio.voice owns narration, and the Curio Class kit supplies motion, sound settings, the audio context and tones. Noise effects are original synthesis through that shared context.

#### Decisions and ambiguities

- The user requires image-tool artwork. The spec's local FLUX preference is superseded by that instruction; all eight paintings use OpenAI gpt-image, with people:false.
- The original is called a 5 a.m. video while its caption says Grandpa gets up at four. Both are retained: waking and baking can occur at different times.
- The final graphic has no shot size or angle. The label controls offer graphic and n/a on shot 8 rather than require a false camera label.
- Four frames need a frame rate, which the spec leaves unspecified. Assume 30 fps, so the inherited sticker edge is present for 0.1333 original seconds. Scrub at 0.00 s to inspect it.
- The spec asks for voice/lines.json and says not to record. All 14 lines are listed for curious-librarian/Aoede; browser speech is the current fallback.
- The copy tree is a student hypothesis, not a scored check. An earlier but wrong parent can be drawn; claim proof still needs the specified evidence pair and types.
- A claim attaches exactly two findings. This prevents a pile of unrelated clues from counting as proof; adding a third requires removing one first.
- Music waveforms are illustrative envelopes of the synthesized tracks, explicitly labeled. R5 is aligned in original time, with its shorter clip time shown separately.
- The tiny preview cards show five caption lines with an ellipsis. The full caption is in the title and in the Captions comparison. This reserves room for the six cards and the tree together.
- Miniature film graphics are proportionally scaled and presentational. The card's accessible name includes the full account, caption and views. Compare contains the readable full-size watermark, stickers, banner and logo.
- At phone width the verdict list scrolls above the closing chips. The closing chips and Copy remain on screen; all five verdict records remain in the list.
- Repeated refusal and claim events use immediate kit narration so a prior how-to cannot swallow them. Read first stops content and updates the hint to the stopped state.
- Choose findings opens a three-column picker. Up to twelve saved chips fit without scrolling at 680x425; longer evidence collections scroll. The panel lists the two attached findings after the picker closes.
- The compact header keeps Reset and the device-only privacy notice visible. The phone header has a small device-only notice beside its title.
- Fairness is open judgment. Copy remains available for drafts and explicitly labels missing calls or reasons, with no completion award.
- No open-question section appears in the spec. Unattended choices are documented here rather than sent as questions.

#### Sensitivity

The case concerns a fictional 13-year-old maker, a grandfather and misleading commercial use. No people appear in the art. Review the false RIP caption as misinformation, not as a true death announcement. Permission and credit are discussed as ethical factors, without presenting this exercise as a legal fair-use ruling. Review the bakery setting for ordinary, respectful representation of family work.

#### Engine changes wanted

No kit change. Shared audit suggestion only: in scripts/audit_tool.py, Audit.steps, surface the audit_error returned by Audit.ev for a failed custom JS step and stop that state, instead of continuing into misleading focus/disabled-control leads. The reviewer did not edit shared scripts.

#### Art still to paint

None. All eight requested images are present. Prompts, generation credit and people flags are in art/prompts.json; originals are in art/raw/.

#### Evidence

Build evidence, number recomputation, art contact sheet, bar-tool copies, commands, frames and mechanical audit live in _scratch/viral-video-breakdown/. See codex-report.md for final check outcomes and limitations. No shared files, commits, branch changes or polish round are part of this build.

#### Cold review changes, 2026-11-07

The reviewer played first, then read this handoff. Claim nudges now describe the observation to make instead of supplying exact answer-pair recipes. The eight-checked event describes inspection rather than claiming mastery after wrong labels. Laptop verdict rows put call and reason beside one another, and the closing card echoes the student's selected obligations. Short landscape hides that extra echo to keep Copy visible. The crust painting was redrawn with a tighter, blistered outside surface in the existing amber/blue style, through the imagegen skill; its full prompt is in art/prompts.json and its raw image remains in art/raw/shot-crust.png.

The final audit confirmed a narrow via-sticker/annotation collision, a clipped compact claim button, undersized summary timings and phone watermark text, and a clipped phone end-card name. These received local layout/type repairs. The opaque summary now makes covered film controls inert, closes the old note, and returns the phone to the top; visible label actions return to the film. Back to film focuses Play. Copy clears stale status after edits, identifies drafts with no closing choices, and gives a selected read-only fallback that remains usable in the phone's scrolling panel.

Two added audit-state scripts incorrectly assigned both selector values before dispatching Change; the first event reset the second selector. Their setup is now sequential and duplicate state names are removed. Affected states received focused drive checks after the single audit; the full audit was not repeated.

There is a remaining assessment blocker: opening the two specified evidence tools and cycling card choices can produce a supported claim without explaining the evidence. This was reproduced through the UI, not inferred from code. The spec explicitly awards clue chips on opening and defines the check as card plus two clues. Requiring an independently interpreted observation or explanation would add a response mechanic, so the reviewer left that change open rather than altering the spec. Teacher notes now state the limit. Do not use supported-claim counts as mastery scores.

#### Test harness notes

Keep the tree SVG as a block with a fixed 60 px phone height. Its auto-height layout initially fed back into ResizeObserver; the final phone height remains 346 px across a five-second stability test, with Draw arrow fully visible. Voice-over captions belong only to shots 1, 2, 6 and 7, matching their Sound entries.

The single audit finished with 169 leads on its pre-fix snapshot. Geometry, singular finding counts and repeated-mode welcome cuts were fixed with targeted checks. The phone audit did not attach to its iframe. Three orphan drive.py host processes sharing port 8785 were found during final cleanup; a port collision is a likely cause of that attachment failure. They were terminated only after their exact tool and host-port command lines were matched. A clean, separately hosted final phone run passed all three modes and the finding picker.

The scratch responsive helper now closes the actual matching host children rather than relying only on the launcher's PID. No shared scripts were changed. All assigned ports were checked closed before the final report. The audit was not rerun, following the one-audit instruction. Full lead dispositions are in _scratch/viral-video-breakdown/audit-dispositions.md.

The final phone claim view compacts the selected case card and hides the investigation tree while attaching evidence; Make the claim ends at y749.7 in a 375x812 viewport. The footer remains reachable by normal document scrolling. Reset now resynchronizes the visible mode, timeline, selectors, feedback and copied output. Retapping the active mode preserves its welcome instead of restarting it.

The final summary hint-only reshoot failed by CDP timeout and then connection reset. Its earlier layout and full student path were captured. A separate final caption capture timed out; the exact source renderer was checked in Node instead, confirming caption presence only on shots 1, 2, 6 and 7. Neither failed capture is claimed as a visual pass.

#### Cold review validation, 2026-11-07

The separate cold-review audit completed once with 154 leads and 100 frames, with no console errors, resize exceptions or stuck controls. Its full lead register is _scratch/viral-video-breakdown/review-audit-dispositions.md; this supersedes none of the historical build audit records above. Focused repair evidence is in audit-fixed/ and phone/, with current JSON geometry and voice-event logs alongside. The 680 summary is reachable by scrolling to How it works; Back restores Play, and covered controls are inert. The corrected ad-trace fixture displays R3 and R5, and the supported-claim fixture reaches all three accepted claims. The claim-guessing blocker remains open.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-08)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-08)
- 2026-11-25: handoff.md folded in (last changed 2026-11-08)
