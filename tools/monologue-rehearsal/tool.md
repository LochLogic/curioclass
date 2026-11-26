# Monologue Rehearsal: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: monologue-rehearsal

#### Built

Built the five-mode offline acting studio from the kit starter: four monologues, six circumstances, three independent
scores, sixteen tactics, a live prompter, four audiences, a real listener's script and saved comparison records.
Includes automatic device saving, immutable performance plans, reflection boxes and confirmed Clear all.
No commits, branch changes, recordings, shared-file edits or polish round.

#### Numbers check

PASS: spoken words 207 / 179 / 208 / 161. Mrs Hale has 163 space tokens including two unspoken cut markers.
The Shakespeare source line counts are 25 / 24 / 26; Viola's spec says 24, but its exact source text has 25.
At 150 words/minute, displayed estimates are 83 / 72 / 83 / 64 seconds, rather than the spec's rounded card estimates.
PASS: marks 30, 62, 110, 150 and flags 33, 147 give one of four matches, with flag 147 unplanned.
PASS: teal/panel 8.96:1, teal/section 8.49:1, ink/teal 9.56:1; script/background 16.32:1; gold/background 13.49:1.
Evidence: Scratch content.py, numbers.txt and direct Gutenberg source downloads. The spec was not edited.

#### Feel check

Walked the full actor/listener workflow with held pointer input and with keys only, and inspected the resulting frames.
Best moment: the pale bracket connects a gold listener flag to a teal planned change while an unplanned flag remains
visible as separate evidence. Want agreement and the partner's own word turn the overlay into a specific rehearsal record.
Flat moment 1: crowded compact controls consumed the prompter. Changed short landscape to A/B/C buttons and a shorter
script heading; the 20-pixel prompter now has 181 pixels of height at 680x425, with Start/Back/Next in view.
Flat moment 2: the score desk opened with intent boxes before actionable beat controls. Moved the word tools and current
beat editor first, kept whole-speech want/obstacle lower, and made the phone sheet explicit.
Compared painted Choose and rehearsal frames with Snowy Mail Route and Beat Lab. The paintings, typographic script and
rehearsal lighting have comparable finish; rewards remain evidence and a clearer performance, appropriate to grades 9-12.
Side-by-side frame: _scratch/monologue-rehearsal/bar-comparison.jpg. No human classroom performance was evaluated.

![Monologue Rehearsal beside Beat Lab](S:/CurioClass-codex/_scratch/monologue-rehearsal/bar-comparison.jpg)

#### Done when

1. PASS: Choose cards, Prepare script, Rehearse prompter, partner script and Compare overlay are the largest regions at
   1366x768 and 680x425. Final compact frames and the audit matrix are listed below.
2. PASS: direct source extraction preserves the three Shakespeare texts and their line endings. The Glaspell cut follows
   the exact supplied wording, commas, ellipses and cut markers; no voice narrates the texts.
3. PASS: marks, stresses and pauses place/remove; all three versions are independent. Held-input checks cover copying to
   both destinations and keyboard word/gap navigation. Keyboard-only workflow adds a beat and reaches a saved reflection.
4. PASS: partner DOM has no active stress, pause, gap, beat-editor or actor-bar markup. Read's logged text is only the
   current listener instruction. No microphone/camera API or network call is present.
5. PASS: sample gives one of four and the correct extra word. Zero-plan and zero-flag frames show their specified lines;
   31 attempted flags stay capped at 30 and the strongest-moments message appears. Tapping a flag again removes it.
6. PASS: Start, Next and Back update immediately. Space advances and Shift+Space returns without scrolling the page;
   switching versions preserves the available beat number. The elapsed timer continues with Motion off.
7. PASS: saved take and reflection survive reload. Earlier and later records open separately; Clear all cancel retains
   work, and confirmation removes the localStorage key. All storage access is guarded.
8. PASS: five runs at held-click, two-second action spacing give every how line once, landed five times and wantRead five
   times while Compare stays current. Leaving Compare drops unstarted result lines. Targeted first-handoff check confirms
   welcomeCirc and the first Start's breath cue now begin immediately in their intended phases.
9. PASS: nine generated images load, with no people or lettering. Final-size inspection caught a figurative stone relief
   on the first Roman painting; one redraw replaced it with geometric and leaf ornament.

#### Wave lessons

- Hint and voice: PASS. Synchronous hints name the next control; Read uses that hint. Curio.voice owns heard-state,
  stale scopes, Read priority and Sound behavior. See voice-results.json and handoff-voice-results.json in Scratch.
- Focus and layout: PASS in keyboard workflow. No focus is taken on load; roving word targets avoid hundreds of Tab stops.
  Local mark changes keep the script node; rebuilt version/tab/history controls restore focus with preventScroll.
- Sizes: PASS for main controls and hints across the required matrix, including 375 through the host. Dense preparation
  panels and long records scroll; the phone uses a beat sheet. Caption scrolling at the smallest preview is noted below.
- No giveaways: PASS. Listener text contains no actor marks; wants shuffle, and no option is marked correct.
- Honest numbers: PASS. Reader names the 150-word/minute assumption; comparison explains its matching window and is not a grade.
- Standards: PASS. Circumstances and score teach TH:Pr4, the audience/live performance teaches TH:Pr6, Connect teaches TH:Cn10.
- Motion off: PASS. The quiet indicator explicitly stops; timing and rehearsal state continue. Motion-off frame inspected.
- Short choice sets: PASS. Four pieces, four audiences, three versions and seven listener wants remain selectable in view;
  the short landscape response layout keeps Save visible. Long circumstances and records are intentional scroll panels.
- Resize mid-action: PASS. The full audit resized after inputs in every state and walk click; no exception or stuck control.
- Delayed welcome: PASS. No welcomeAfter. First mode/action changes invalidate old instructions; targeted handoff passed.
- Unknown as unknown: PASS. No listener evidence is invented. Before a take there is no Compare; unset closest want is stated.
- One look, one meaning: PASS. Actor bars, listener triangles and pale brackets remain distinct in grayscale.
- Badge truth: PASS. Counts come from saved flags and unique matched marks; no planned changes is explicitly named.
- Hint restores with state: PASS. Mode/tab switches and Clear all restore the current action instruction.
- No answer by copying: PASS. Wants are hypotheses chosen privately by the actor, then independently by the real listener.

#### Audit leads

The single full audit finished in 586 seconds with 27 leads. All 73 audit PNGs were inspected.
Ten field-naming leads: FIXED with explicit aria-labels, in addition to the existing enclosing labels. Targeted names pass.
Twelve scroll-panel leads: retained by design. These are six long circumstances with fact disclosures and the long
comparison/history/reflection form, rather than a hidden short answer set. The spec places the script first and asks
for all these fields; long forms scroll while the script, mode controls and hint remain visible.
Four first-card welcomes not heard: expected. The spec explicitly makes welcomeChoose stale when any card is tapped.
The reader and Choose this one appear immediately, with no delayed welcome or narrated monologue.
One quick active-Choose interruption: FIXED. Tapping the current mode leaves its running welcome intact; a fresh held
two-tap check logs one uninterrupted welcome. One-beat hints were also fixed to omit disabled Back/Next instructions;
the added conditional instruction, first breath and visible phone privacy notice passed targeted checks.
Runtime, resize recovery, Motion off and repetition checks were clean. The full audit was not repeated after these
targeted fixes. No console errors, warnings or exceptions occurred in the final targeted drive runs.

#### Frames looked at

Inspected every image in first-frames (6), functional-frames (5), matrix-frames (26), phone-frames (9), targeted-frames (4),
final-frames (2), the keyboard frames (2), voice-final.png, all nine final WebPs, the art sheet and both reference frames.
Contact sheets are in Scratch; representative 680x425 and 375 frames were also inspected at native size.
Also inspected all 73 audit PNGs through audit-sheet-0.jpg to audit-sheet-19.jpg, and all three post-audit-frames.
The final phone Choose, Score and Rehearse frames verify the common privacy footer after its targeted change.

#### Art made

Nine environment paintings made with the built-in OpenAI image tool; one Roman-street redraw. Final raw PNGs are in
art/raw, final 1200-pixel WebPs in art, complete prompts and provenance in art/prompts.json. No downloaded images.
Total final art: 1126.2 KiB. Final bundle: 1,642,247 bytes, about 1603.8 KiB, under 2 MB.
Used only the free art.py --rekey form. The ten-line voice manifest is unrecorded, as instructed.

#### Art still to paint

None. No people assets were requested or deferred. The browser narration manifest has no recordings by instruction.

#### Engine changes wanted

None. No family engine is specified and no shared file needed a change.

#### Left open

- Browser speech cannot reproduce the specified soft-breath / Enceladus bank voice without recordings. None were made.
- Some dense Choose captions at 680x425 scroll within their cards. All four card targets remain visible. Long preparation
  settings, performance history and reflection panels also require scrolling, especially in compact layouts.
- Live paired performance quality has not been classroom tested. Scripted partner evidence validates the mechanism only.
- The source heading for Helena places the scene in a palace room; the supplied circumstance says by the palace and asks
  for an outdoor garden painting. The build follows the supplied Content and art; the discrepancy is in handoff.md.
- A mode change after two seconds may discard an unstarted result line, correctly, once its result is no longer current.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: monologue-rehearsal
#### Played
Cold grade 9-12 walk: Choose, reader, Circumstances, Score, Rehearse, four audiences, listener flags, response and Compare before reading builder notes or src.html. It feels like a serious rehearsal desk; the paintings and live script are its strengths.
#### Findings fixed
- Blocker, general, Perform: Prepare remained reachable after handoff, exposing the actor's plan. Disabled actor modes and guarded mode changes until Save.
- Blocker, general, Compare: a regular seven-word flag sweep earned certainty about acting skill. Broad coverage now shows a flag count and notice, suppressing the match ratio and landed narration. Other comparisons describe proximity and closest-want agreement; the limitation sits beside the count.
- Should fix, general, response: a want alone enabled Save. Require a nonblank feeling word as well; updated the audit path.
- Should fix, general, keyboard: Space on Read started the rehearsal. Native controls now retain their Space action.
- Should fix, general, voice: response and unmatched Compare had no spoken next action. Added phase-valid response and Compare how-to lines and synchronized the manifest.
- Should fix, general, content: corrected Helena's escape to tomorrow night and her location to a room in Theseus' palace, following the named source.
- Polish, general, Compare: the empty outcome was a dead end. Added a direct return to Score for the selected take's monologue/version and made the audience reflection allow no change.
- Polish, general, art: redrew mr-class with attentive classmates in the existing painted room; preserved original art in Scratch and marked people: true.
#### Findings left
- Production constraint: narration uses browser fallback. No clips exist for the specified soft-breath bank voice; recording is excluded by the build rules.
- Polish, general: dense Choose captions at the smallest landscape preview and the long preparation/reflection forms scroll. All card choices and primary mode controls remain visible; preserving readable type and script space follows the spec.
#### Break it
- Planned-change result: every seventh word produced a false all-changes claim before repair. Repeated at 1366, 680 and 375 after repair: 30 flags, broad-flag notice, no match ratio and no landed line.
- Want check: tried all six options before saving. No correctness feedback appears; the final choice is logged once, and agreement is explicitly about the closest-want category. Something else requires text.
- Response gate: a want with no feeling word stays unsaved. A nonblank feeling enables Save. No automated claim is made about the quality of the word.
- Flag meter: 31 taps stay capped at 30; tapping a flag again removes it. Inclusive boundary tests accept mark minus 2 and plus 6, reject minus 3 and plus 7, and count a planned boundary only once.
- Partner peek: UI and setMode attempts to return to Prepare remain in Perform; no actor marks are in the displayed DOM, and Read speaks only the instruction.
- Rehearsal timer: not a score and has no pass condition; Motion off preserves elapsed time and leaves zero running infinite animations.
- Reflections: blank or filler entries receive no pass, badge or points. The audience prompt allows no change. Versions remain independent; later edits cannot rewrite a saved take; records/reflections survive reload and Clear all cancel/confirm behaves correctly.
#### Voice walk
Main path: Choose welcome, Viola reader, six circumstance answers, Score and a beat, Rehearse/Start/Next, Perform/hand off, listener flag, Done/want/feeling/Save, Compare/Connect. Held clicks, two-second action pace, Sound on. Log: review-voice-results.json.
Heard in order: welcomeChoose, welcomeCirc, scoreHow, welcomeRehearse, breath, handHow, partnerHow, responseHow, compareHow, landed, wantRead. Five takes: all nine how-to keys once each; landed 5 and wantRead 5. Result dwell allowed the browser fallback's slow queue to finish; leaving the screen earlier drops stale events as intended.
Side path heard singleRehearse and breath; Read during narration and with Sound off spoke only the partner instruction. No actor text or marks were spoken. Space on Read reads without starting rehearsal. Keyboard-only full workflow passed; no runtime errors in the targeted batches.
| Kind | Expected | Spoken |
|---|---:|---:|
| Each of nine main-path how-to keys | 1 | 1 |
| landed event | 5 | 5 |
| wantRead event | 5 | 5 |
#### Facts checked
- Viola text, identity, service to Orsino, ring context and street: [Gutenberg 1526, II.2](https://www.gutenberg.org/cache/epub/1526/pg1526-images.html). Exact excerpt agrees with the archived full source and live passage.
- Marullus text, tribune role, workers, Pompey and triumph context, street in Rome: [Gutenberg 1522, I.1](https://www.gutenberg.org/cache/epub/1522/pg1522-images.html).
- Helena text, Demetrius/Hermia context, tomorrow-night flight and palace-room heading: [Gutenberg 1514, I.1](https://www.gutenberg.org/cache/epub/1514/pg1514-images.html).
- Mrs Hale text, Minnie Foster/Wright, Mrs Peters, winter kitchen and investigation: [Gutenberg 10623, Trifles](https://www.gutenberg.org/cache/epub/10623/pg10623-images.html). The supplied cut joins three speeches, not two; notes correct the attribution of the cut.
- Play dates: [Folger, Twelfth Night](https://www.folger.edu/blogs/collation/twelfth-night/) supports about 1601; [Folger, Julius Caesar](https://www.folger.edu/explore/shakespeares-works/julius-caesar/) supports 1599; [Folgerpedia, Midsummer](https://folgerpedia.folger.edu/A_Midsummer_Night%27s_Dream) gives likely 1595-6. Trifles' source front matter credits the Provincetown Players, Wharf Theatre, August 8, 1916.
- Given circumstances and objectives: Stanislavski, An Actor Prepares (1936), as named in the spec; [Pearson's Stanislavski practitioner guide](https://qualifications.pearson.com/content/dam/pdf/A%20Level/Drama-and-Theatre/2016/teaching-and-learning-materials/Practitioner-guide.pdf) corroborates the teaching approach. Tactic tips and wants are explicitly suggestions, not rules.
- Standards: [NCAS Theatre at a Glance](https://nationalartsstandards.org/sites/default/files/2021-11/Theatre%20at%20a%20Glance.pdf). Circumstances/score practice Pr4, audience/live delivery Pr6, Connect Cn10. No automated assessment of delivery is claimed.
- Independent computation: 207/179/208/161 spoken words, 25/24/26 Shakespeare lines, 83/72/83/64 seconds at an assumed 150 words/minute. Teal contrast 8.96:1 on panel, 8.49:1 on section, ink/teal 9.56:1; script/background 16.32:1. Evidence: review-numbers.json.
- The inclusive 2-before/6-after matching window is the spec's model convention, not a measured rule about listeners. Sample marks 30/62/110/150 with flags 33/147 gives one of four and extra flag 147.
#### Sensitivity
Review Shakespeare's gender generalizations, romantic rejection and shaming as character views; Trifles' gendered isolation and death investigation; optional casting and adaptable body tactics. No personal disclosure is required. Check the new classroom people image and its card crop for natural representation. Ancient Greek/Roman settings are atmospheric stage worlds, not archaeological reconstructions. These matters are also named in handoff.md.
#### Flattest moment left
Typing six circumstance answers remains slower than marking and performing. It earns its space by grounding the actor's choices; no extra game or automatic judgment was added.
#### Graphics
All nine finished images inspected. Preserved the setting paintings, ghost light, theatrical type and overlay shapes. Replaced only mr-class through built-in imagegen; full prompt is in art/prompts.json, raw in art/raw/mr-class.png, final in art/mr-class.webp. Used only free art.py --rekey. Original classroom is archived in Scratch.
Bundle 1,663,484 bytes; finished art 1140.1 KiB. Native 1366 and 375 crops inspected; no lettering or troubling representation found. Grayscale preserves bars, triangles and brackets. Opened both reference tools' frames; the studio retains comparable finish without copying their look. Targeted PNGs inspected: cold-frames (8), review-probe-frames (6), review-recheck-frames (12), review-phone-frames (6), review-last-frames (7), voice (2), keyboard (2).
#### Audit
Single final audit completed within the 40-minute limit: review-audit/audit.md, 76 PNGs, all inspected through 19 contact sheets and native frames. The 17 leads are accounted for: six Circumstances, five Compare and two broad-flag scroll-form leads are intentional long forms, not hidden short answer sets; four skipped first-card welcomes follow the spec's stale-on-card-tap rule. No new blocker or should-fix was confirmed.
Every required size is clean for targets, names, hint, clipping, overlaps and runtime. Motion off, resize recovery, held-click input and rapid taps are clean. The audit's automatic control walk covers Choose; the manual five-mode, five-take voice walk and keyboard path supply the deeper interaction checks.
BUILD wave checks: immediate hints/Read, retained focus, all sizes, private/shuffled listener choices, explicit estimate/model assumptions, standards activities, Motion off, visible short choice sets, resize recovery, no late welcome, unknown evidence shown as unknown, distinct glyph meanings, truthful counts, restored hints and no answer by copying were checked in the evidence above.
Only assigned ports were used. All task Chrome/host ports are closed, host.html is absent, no shared files were edited and no git commits were made.
#### Left open
The tool cannot authenticate live performance or distinguish fabricated human responses without recording, which the spec forbids. It has no grade, mastery gate or best score. Random flags can produce numerical proximity; the revised copy states only that limited fact.
The spec remains unchanged. Its Helena context contradicts its own cited source, its Viola line count is 24 rather than 25, and its cut description says two rather than three speeches. The source-backed content/notes correct these. The classroom people redraw follows the current baseline people rule despite the older empty-room art instruction.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Monologue Rehearsal build handoff

Build only. No commits, branch changes or polish round. The final report records the checks and open leads.

#### Structure

- src.html starts from the kit starter and uses curio.css, theme-912 and Curio.voice. Its layout is real pixels,
  rather than scaling a fixed scene. The top section is responsive CSS; the script contains content adapters,
  Choose, Prepare, Rehearse, Perform and Compare renderers, followed by wiring and the test hook.
- content.json is loaded through `"json:content"`. It contains the four speeches, source IDs, circumstances and
  six wants per speech. Art tokens remain in src.html because art expansion precedes JSON expansion.
- `saved` owns serializable work under `curio-monologue-rehearsal`; `state` owns temporary mode and interaction state.
  Circumstances belong to a monologue. Each of its three versions has independent marks, stress, pauses, beats and
  closest want. Beat settings are keyed by the index of the beat's first token; removing a mark removes that row.
- Every performance snapshots the chosen version and the actor's own want before handoff. Later edits cannot rewrite
  an earlier take. All performances, including different monologues, remain selectable in Compare.
- `match(marks, flags)` uses token indices with the inclusive window [mark - 2, mark + 6]. Each flag chooses its nearest
  mark; ties choose the earlier mark. Several flags may refer to one mark; the headline counts unique matched marks.
- Source verse line endings are retained in the reader, rehearsal and overlay. Score and listener word targets wrap
  within those lines. Score's 44-pixel space-dot targets are deliberately generous, so this view is more spread out.
- The actor's score is removed from active DOM markup in partner view. Read uses only the instruction hint; it never
  narrates the speech or exposes the actor's plan. No microphone, camera or recording API is present.
- Keyboard word navigation uses one roving Tab stop. Arrows move through words and spaces; Enter activates them.
  Native button focus is preserved when marks change. Version switches restore focus with preventScroll.
- At 375 pixels Score has a bottom sheet. Long scripts, circumstances, beat lists and reflection records scroll.
  The short landscape layout uses A/B/C labels and a compact response form with Save visible.
- V welcomes are valid only while their instructions fit. The two event IDs are landed and wantRead. A sequence may
  drop an unstarted result after the student leaves Compare, as required by scope and stale-line behavior.
- The elapsed rehearsal timer stays active with Motion off. Only the quiet rehearsal indicator animates; its CSS loop
  is explicitly disabled in calm mode. Resize repositions the current beat or recomputes overlay brackets.

#### Source and number notes

- Direct Gutenberg text downloads and extraction are in Scratch. Word counts excluding the two cut markers are
  207, 179, 208 and 161. Mrs Hale has 163 space tokens including the two `[...]` markers, which still take indices.
- At 150 words per minute the displayed durations are 1:23, 1:12, 1:23 and 1:04. The spec's rounded card durations
  were 1:25, 1:10, 1:25 and 1:05; this build displays the recomputed estimates and names the assumption in the reader.
- Viola has 25 source lines, rather than the spec's 24. The other Shakespeare passages have 24 and 26. No text or line
  was removed to force the count. The Glaspell cut follows the supplied wording and cut markers exactly.
- Cold review corrected Helena's context to tomorrow night and a room in Theseus' palace, following Gutenberg 1514,
  Act I scene I. These correct the supplied Content wording. The requested outdoor garden painting stays atmospheric,
  not documentary proof. The spec remains unchanged; its source heading supports the corrected fact panel.
- Computed contrast: teal on panel 8.96:1, teal on section 8.49:1, dark ink on teal 9.56:1, script on black 16.32:1,
  gold flags on black 13.49:1. The sample matching rule produces one of four matches and an unmatched flag at 147.

#### Open questions resolved

The spec has no explicit open-question section. Choices follow its stated leaning: three versions, real partner
evidence, a nearest-mark matching window, shuffled listener wants, local saving and no recording. The tie-break for
equally near marks uses the earlier mark; the spec leaves that tie unspecified. No extra topic or game mode was added.

#### Art

All nine assets were made with the built-in image tool during this build, using the house style in art/prompts.json.
Raw PNGs are in art/raw and final 1200-pixel WebP assets are in art. The Roman street was redrawn once to replace
figurative arch carvings with geometric and leaf ornament. The original is archived in Scratch. Cold review replaced
the weakest audience image, mr-class, with attentive classmates in the same room and painted style. It is marked
people: true, with its full prompt and asset-specific house style in prompts.json. Other settings remain empty.

The spec's FLUX production note was superseded by the user's explicit request to use the image tool. All sources
credit OpenAI gpt-image. No images were downloaded and no paid art.py generation form was used, only --rekey.

#### Engine changes wanted

None. No shared kit, source docs, scripts or other tool files were changed.

#### Verification and remaining limits

Scratch contains bounded command helpers, source downloads, arithmetic, the full interaction results, the narration
log, standard-size frames, phone frames through host port 8795, the bar comparison and the final audit output.
Chrome debugging was restricted to ports 9990 and 9991. Test Chrome and host processes are closed by their helpers.

No voice recordings were made, following the build-only instruction. The twelve-line soft-breath / Enceladus manifest
is ready; current speech is the kit's browser fallback and cannot reproduce that bank voice exactly.

The conditional one-beat welcome is derived from the existing rehearsal instructions. It avoids naming Next
when no change is planned. Active mode taps leave current speech intact. Editable fields have explicit accessible
names in addition to their enclosing labels. The phone footer keeps the local-device privacy statement visible.

At the smallest landscape size, the long circumstances, score settings, performance list and Connect prompts require
panel scrolling. Some dense Choose-card captions also scroll within their cards; the four card choices stay in view.
No human classroom pair supplied listening evidence during this build. Automated held-click flows exercised the
actor and listener roles, and the frames were visually inspected. Live delivery and listening quality need classroom use.

The user's instruction to stop as soon as codex-report.md is written takes precedence over the brief's request for
an early report file. Interim evidence was kept in Scratch; the report is written as the final build action.

#### Cold review changes

Partner and response phases disable the actor's modes and guard setMode until a response is saved. Save requires both
a want and a nonblank feeling word. The native Space action on buttons works; only non-control Space is a rehearsal
shortcut. Compare now describes nearby flags and closest-want agreement, without claiming proof of understanding.
Its evidence note stays beside the count; Plan a change / Revise a choice in Score returns to that take's work.
The broadFlags guard replaces the ratio and suppresses landed when 12 or more flags cover at least 75 percent of
possible boundaries through the matching window. It leaves raw flags and brackets visible and preserves the record.
Compare and response have how-to narration; the audience reflection allows an unchanged performance.
The input is still a human listener's report. The tool cannot authenticate live acting or distinguish fabricated taps
from real reactions without recording, which the spec forbids. It has no grade, mastery gate, best score or pass badge.

#### Sensitivity

Review the Shakespeare characters' gender generalizations, romantic rejection and public shaming as character views,
not universal truths. Trifles includes gendered isolation and a death investigation; the selected cut contains no
graphic violence. No student needs to disclose personal experiences. Any student may play any character, and physical
tactics can be adapted. A cultural reviewer should check this framing and the ancient Greek/Roman atmospheric settings.
The new classroom image has varied skin tones and one wheelchair user participating in the same group. Review its
natural representation and the final card crop; prompts.json identifies it as a people asset.

#### Cold review verification

The single cold-review audit completed: _scratch/monologue-rehearsal/review-audit/audit.md, 76 frames, all inspected.
Its 17 leads are thirteen intentional long-form scrolling reports and four first-card welcomes made stale by the
reader opening, as the spec requires. No additional blocker or should-fix was confirmed. Standard sizes, targets,
clipping, runtime, Motion off, resize recovery and the audit's held/quick input checks are clean.
The manual five-mode voice walk gives each main-path how-to once and both result events five times across five takes.
The side path covers the one-beat instruction and Read with Sound off. Keyboard-only completion and confirmed Clear all
pass. Snapshot integrity, reload persistence, option cycling, the 30-flag cap, matching boundaries and wide flag sweeps
were rechecked. Evidence is in review-*-results.json, the targeted frame folders and the review-audit frame manifest.
Final bundle: 1,663,484 bytes. Assigned Chrome/host ports are closed; host.html is absent. No commits or shared edits.

#### Audit closure

The single full audit completed in 586 seconds with 27 leads and 73 frames, all inspected. Default sizes, targets,
motion-off behavior, resize recovery, runtime checks and five-click repetition were clean. Ten naming leads were
addressed with explicit aria-labels, and the active-mode welcome interruption was fixed. Twelve scroll-panel leads
refer to the intentionally long circumstances and comparison forms. Four skipped first-card welcomes follow the
spec's explicit stale-on-card-tap rule.

Targeted checks after the audit passed for active-mode speech, one-beat instructions and breath, clearing transient
word/timer state on a new monologue, explicit field names, and the phone privacy footer. Only affected frames were
re-shot; the full build audit was not repeated. The manifest includes one conditional one-beat how-to to avoid
directing a student to a disabled Next control. All test Chrome and host processes were closed; host.html was removed.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-06)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-06)
- 2026-11-25: handoff.md folded in (last changed 2026-11-06)
