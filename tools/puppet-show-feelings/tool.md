# Puppet Show Feelings: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: puppet-show-feelings

#### Built
Three teacher-led K-2 modes in one offline file: the six-scene puppet story with three endings; Backstage with nine settings, audience reveal and six Try it targets; Like me with six personal connection prompts and a changeable ending vote. No commits or polish round.

#### Numbers check
Recomputed all 27 nearest-prototype cases, all five hand-set ties, scene presets, feeling totals and contrast before implementation. All agree with the spec. Totals: sad 4, worried 7, calm 3, proud 3, happy 5, excited 5. Contrast: 5.2986, 4.9373, 14.9801 and 6.0570. Evidence: `numbers.json` in Scratch.
Tilt is 28/0/-18 degrees with 250 ms easing. Bounce is 0, 12 at 1.2 Hz, or 34 at 2.2 Hz before stage scaling. Babble uses 260/150/95 ms syllables and .85/1/1.15 pitch multipliers, two or three blips per syllable.

#### Feel check
Best moment: change only the head from Down to Straight to Up and the same quiet line reads sad, calm and proud. The audience reveal makes the class commit to a reading first; Try it gives a specific check and spoken praise.
Flat moment 1: the compact ending tiles covered Pom. Moved them down to the ledge, keeping all three in view and Pom's head visible.
Flat moment 2: the tall tree was behind the curtain, so the stuck-kite scene did not show its cause. Redrew the park with the whole tree inside the opening and placed the kite in its branches.
Also redrew both open mouths from their closed references to preserve identity. Fixed tall-layout theater proportions and Like me's small puppet, then widened its ring so extreme tilts stay clear of cards. Ending kites now stay visible in front of Pom; the high kite clears the curtain. The Line button shows a scene miniature and the worried icon has raised inner brows.
Opened Snowy Mail Route and Beat Lab before building. The side-by-side `bar-comparison.png` and final theater frames show comparable scene richness: knit texture, layered cardboard, painted curtains, a leafy park and shelf art. Pom's continuous tilt and bounce are the main feedback, rather than a numeric display. A teacher-led whole-class conversation is still needed for the intended 15 to 20 minutes.

#### Done when
1. PASS with compact layout interpretation: Pom is the central character at 1366x768 and 680x425. All nine controls stay visible. Short landscape uses side-by-side controls as STANDARDS directs; larger layouts put them below.
2. PASS: clicked every combination and compared all 27 results to the table; presets and scene settings recomputed. `gameplay.log`.
3. PASS: measured the 250 ms tilt transition and timing/pitch logs; bounce preserves phase while amplitude and frequency blend. `smoke.log`, `gameplay.log`.
4. PASS: changes interrupt old babble immediately, update the pose and hide the audience card. Tested during active playback.
5. PASS: all three endings reached with real clicks; choice scene alone disables Next, ending controls remain after choosing, Play again restarts.
6. PASS: all six targets met and cycled; all six praise events logged as spoken. `final-checks.log`.
7. PASS for queue behavior: Show logs scene, then babble, then question. Five-action Backstage run spoke each how-to once; audience events spoke at two-second pace. Read preserved a queued audience result. Sound quality has not been auditioned.
8. PASS: visible controls measured at least 60 px in every mode and required size. Chosen controls have a thick border and check, feeling icons include words.
9. PASS: Motion off stays stationary with immediate tilt, unchanged syllable durations and no infinite CSS animation. Keyboard and grayscale frames inspected.
10. FAIL for literal storage wording: tool makes no network calls and saves no lesson state. The shared kit persists Motion preference as required by the contract, an exception to the spec's literal nothing-saved wording. The iframe host's favicon 404 is outside the tool.

#### Wave lessons
- PASS: Hint and voice: checked immediate hints, Read, stale cancellation, `V.heard`, two-second actions and choice-scene disabled Next. Browser speech fallback only.
- PASS: Focus and layout: controls stay in place; reveal moves focus to Again before hiding; scene 5 moves it to an ending before disabling Next. No focus on load.
- PASS: Sizes: one full three-mode pass at all eight sizes, followed only by targeted repairs. All controls and hint visible.
- PASS: No giveaways: audience feeling stays hidden until asked and hides on every setting change. Try it is a requested practice target, not a concealed-answer quiz.
- PASS: Honest numbers: no score or diagnostic meter. Notes identify the table as a simplified classroom model.
- PASS: Standards: students read cues, direct cues, choose an ending and connect a feeling to their own experience. TH:Re7, TH:Re8 and TH:Cn10 each have an interaction. No family engine.
- PASS: Motion off: RAF keeps timing without displacement; the breeze loop is removed, not sped up.
- PASS: Short choices visible: all nine controls, six feeling cards and three ending options fit; no choice scroll panels.
- PASS: Resize during action: passed in the single audit: no exceptions and nothing left disabled.
- PASS: Delayed welcome: each mode has scoped welcome behavior and cancels stale work on entry or a meaningful first action.
- PASS: Unknown as unknown: hidden audience card gives no unasked result.
- PASS: One look, one meaning: consistent face-plus-word feelings and check-plus-border selections.
- PASS: Badge truth: audience card uses the current lookup; target check uses the same lookup.
- PASS: Hint restores: Show, Backstage, Try it and ending vote immediately restore the appropriate hint when their state changes.
- PASS: No copying answer words: students read the puppet before revealing the audience result. Like me is explicitly a named-feeling connection prompt.

#### Audit leads
The single full audit exited successfully within its 40-minute limit, with 10 leads. All default sizes, Motion off and mid-action resizes were clean. The nine authored states covered all three modes at every size.

- Two `#feelings` keep-region leads: the ring parent deliberately contains an empty center around Pom. Replaced the parent keep with the six actual buttons. The final layout also widens the ring and keeps the tilted face clear; all six cards remain visible and at least 60 px.
- Four welcome leads, `#reveal`, `#back`, `#next`, `#again`: retained the chosen action's narration instead of queuing a stale welcome behind it. Back and Again narrate the visible premise themselves. Next and Show me deliver their requested result. This follows the shared voice priority rules.
- Three quick mode-tap leads: confirmed and fixed. A selected mode now returns without hushing its welcome. Each mode's welcome spoke once without a cut in the 0.7-second repeat check.
- One quick Next lead: the Whoosh event is intentionally interrupted when Next advances again. Returning it in the new scene would be stale and would violate the spec's immediate navigation rule.

The audit's automatic mode finder saw zero modes because it searches only inside headers. Authored states cover the separate navigation bar. Explicit checks also exercised all 27 settings, all six Like me cards and all three votes, including narration at a two-second pace.
After the audited bundle, final fixes received 21 targeted frames and checks, not a second full audit. They cover the mode guard, target praise, ending prop placement, new-kite redraw, Line pictures, worried icon and Like me ring. `quick-modes.log` confirms three praise events for three successive valid changes; the earlier synchronous probe in `repairs.log` returned before the queue pumped and is not used as speech evidence.

#### Frames looked at
All build screenshots inspected, including full three-mode size set; compact choices and challenge; all three endings; all 27 settings result; voice, Read, focus and keyboard checks; Motion off; grayscale; tall layout fixes; generated art sheet; final tree redraw; and bar comparison. Also inspected all 81 audit frames and 21 final targeted frames: repair-frames (12), quick-mode-frames (4) and ring-frames (5).
Evidence is under `_scratch/puppet-show-feelings/`; logs include full-0/1, gameplay, smoke, final-voice, final-checks and tree.

#### Art made
Ten final WebPs total 478.6 KB. The final self-contained bundle is 1145 KB, below 2 MB. Voice manifest: 88 unique lines. No placeholders.
Ten final images: theater, park, Pom and Dot closed/open, red kite, new kite, stick and shelf. Both open-mouth puppets, the park and the new kite were redrawn using references. No generated people. Prompt provenance and raw images are retained.

#### Art still to paint
None. All ten specified images are used.

#### Engine changes wanted
No runtime engine changes. Audit helper request: in `scripts/audit_tool.py`, extend `MODES_JS` with `nav .seg button` so its automatic mode walk finds the separate mode bar. No shared file was changed.

#### Left open
The specified smooth-narrator / Algieba identity is in the voice manifest, but there are no recorded clips because the build instructions prohibit recording. Browser speech supplies narration. A later voice pass and speaker/headphone listening check remain; muted browser automation verifies queues and synthesis timing, not sound quality.
The 15 to 20 minute classroom pace and children's interpretation of the simplified cue model need a teacher-led trial. Build instructions and STANDARDS compact layout take precedence over the spec's below-stage wording at 680x425.
The full audit precedes the final targeted fixes and was not rerun, following the build brief. The audit mode-discovery limitation is documented above. All owned browsers and host servers are closed; the generated tool host.html was removed.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: puppet-show-feelings

#### Played

Cold K-2 solo/projector play preceded builder notes and source: all three modes, six story beats, three endings, cue controls, target and vote. Rich, inviting theater; directing one head change is the strongest teaching moment.

#### Findings fixed

- blocker, general, Backstage Read: disclosed the hidden answer. Read now describes settings until Audience says is open; real Read logs verify it.
- blocker, general, Try it: opening an already-matching target and repeatedly tapping its selected setting earned praise. Neither can now earn a check or praise without a changed setting.
- should fix, general, voice: initial theater tap did not play the opening; change instruction arrived too late after babble; Line babbled over narration. Added opening playback, shortened and prioritized the first-change instruction, and sequenced Line narration before babble.
- should fix, general, stale voice/state: stop old audience speech on a setting change, stop babble on audience reveal, validate praise against the current mode/settings, and resume a matched target's advance after mode return.
- should fix, general, Like me: closing the vote left its text in the memory prompt; opening it could leave an unrelated instruction. Restored the current prompt on close, show the vote instruction on open, and stop stale vote speech.
- should fix, general, solo/privacy: personal prompts now invite telling Pom or passing; Motion's tooltip states its preference stays on this device.
- should fix, general, compact Backstage: the down-tilted nose crowded the 1000x625 stage edge. Shifted that pose inward with the same 250 ms easing; retained its size and rechecked compact extremes.
- polish, general, ending/art: replaced the heavy bark branch with a slender painted twig; rekeyed cutouts with despill. The new kite unfolds at Pom's mouth while the original red kite remains stuck, making that choice's outcome clearer.

#### Findings left

- blocker, general, Try it: a blind exhaustive sweep still earns automatic target praise. This follows the spec's mandatory check on every matching change. Preventing it needs a changed assessment/attempt rule, so no unapproved gate was added. It is not a mastery check; notes and handoff now say so.
- should fix, general, voice production: the specified Algieba recordings are absent. CODEX-BUILD.md explicitly says not to record audio, so the browser fallback stays and a later authorized voice pass is needed.
- polish, general: very fine key-color edging remains on some lossy cutouts at magnification; the pictures retain their texture and look coherent at the tested display sizes.

#### Break it

- Try it, pre-fix: prepare sad, enable Try it, tap selected Down repeatedly. Four praise starts without four changes. Post-fix: no check, no praise, and the unchanged taps do not increment changes.
- Try it, post-fix blind 27-setting sweep: earned sad and calm praise without consulting the target or reading cues. Open blocker above. No score, best record, saved success or timer score exists.
- Audience says: all 27 actual-click combinations agree with the spec table. Changing settings hides the card; Read no longer supplies its hidden label. Repeated reveals are explanations, not assessment passes.
- Show me: immediate reveal and rapid Next/Back remain allowed by the spec; they carry no success claim. Scene 5 alone blocks Next until an ending is chosen. All endings were played.
- Like me and ending vote: all choices are preferences, no correct-answer gate. Changing/closing a vote restores the appropriate instruction. Passing on a personal memory is explicit; no question assumes the child made a mistake.

#### Voice walk

Held clicks, Sound on, default Motion, two-second gaps: theater, Next/reveal through worried and sad, ending choice, Dot/reveal, Backstage changes/Audience says, Like me/proud, vote/Dot.
Main sequence and final counts: Show welcome; Whoosh/excited reveal; stuck/worried reveal; tugs/sad reveal; ending scene and Dot/excited reveal; Backstage welcome, change how-to, audience results and one-change teaching; Like me welcome and proud prompt; vote how-to and Dot preference. Each mode welcome, change how-to and vote how-to started once. Five-change check: change/flip how-to expected 1 each, observed 1 each; audience events expected 5, observed 5. Logs: latest-main-voice.json and final-repeat.json in Scratch.
An 18-second paced opening separately logged scene line, six middle-speed babble syllables, question, then happy reveal in that order. Rapid navigation intentionally cancels unfinished story lines; it never replays them in the next scene.

| Line | Kind | Expected | Started |
|---|---|---|---|
| Show, Backstage, Like me welcomes | welcome | 1 each | 1 each |
| Change / one-change teaching | how | 1 each in five changes | 1 each |
| Audience result | event | 5 in five reveals | 5 |
| Scene question | event | 1 in paced opening | 1 |
| Target praise | event | all 6 feelings | all 6, 9 matching changes |

Read during speech and across mode switches was tested; hidden-result Read stays neutral. Sound-off Read and six-target results: Sound-off Read spoke the neutral settings/hint. All six targets praised, with repeated praise only for genuine matching changes (six-targets.json); no-op/open-only retest stayed unearned. Sound-off speech consumes no how-to.
No recorded clips exist; browser synthesis supplies narration. Muted automation verifies requested starts/queues and timing, not the audible quality or the specified Algieba performance. Recording was prohibited by the build brief.

#### Facts checked

- All 27 authored classifications and all story/ending presets: independently transcribed spec table and actual-click results. Counts: sad 4, worried 7, calm 3, proud 3, happy 5, excited 5. Head-only quiet walk: sad, calm, proud. Independent squared-distance computation confirms the five specified ties and no non-nearest selections.
- Tilt 28/0/-18 degrees, easing 250 ms; bounce 0/12/34 scaled px at 0/1.2/2.2 Hz; babble 260/150/95 ms, pitch .85/1/1.15: spec's authored animation model, inspected in source and sampled in babble logs. These are not measured human thresholds.
- Posture/movement can convey emotion, with varied patterns: [Dael, Mortillaro and Scherer (2012), University of Geneva](https://archive-ouverte.unige.ch/unige:97844).
- Posture/movement also reflect activation and individual actor differences: [Wallbott (1998), University of Salzburg](https://uni-salzburg.elsevierpure.com/en/publications/bodily-expression-of-emotion/).
- Slow sadness and faster happiness/fear vocal cues, interpreted probabilistically: [Juslin and Laukka (2003)](https://pubmed.ncbi.nlm.nih.gov/12956543/), Table 11 in the [paper](https://www.brainmusic.org/EducationalActivities/Juslin_emotion2003.pdf). The six-label table is an authored simplification, not a validated emotion detector.
- Recognition, preferences and personal connection: [NCAS Theatre K-2, pages 6, 7, 9](https://nationalartsstandards.org/sites/default/files/2021-11/Theatre%20at%20a%20Glance.pdf), checked against Show, ending choice and Like me activities. All three module codes have actions.
- Story and ending preferences: original fiction from the spec, not historical or scientific facts. No health, law, finance or safety instructions are taught.
- Palette contrast independently recomputed: 5.30:1, 4.94:1, 14.98:1, 6.06:1 (white/brand, brand/paper, ink/paper, muted/paper).

#### Sensitivity

No named culture, religion, hard history or human figures. A cultural reviewer should check that a simplified posture/speech model does not imply universal rules across cultures or neurotypes. Personal disclosure is optional on screen; notes discourage inferring children's actual feelings from their movement. All ten art assets are marked people:false.

#### Flattest moment left

Like me still depends on a spoken conversation; clicking cards alone is brief. The new-kite ending was the flattest visible payoff and now has an unfolding replacement, a mouth-level prop and the still-stuck original.

#### Graphics

All ten final assets and their in-scene use inspected: theater, park, both Pom poses, both Dot poses, both kites, stick and shelf. One stick redraw, no new topic/assets, all cutouts rekeyed. No missing art tokens or human figures. Final bundle: 1160.2 KB. Compared fresh Beat Lab and Snowy Mail Route frames; kept the strong handmade stage and large sock character.

#### Audit

One final audit completed within its 40-minute limit, seven leads. Two phone leads are a missing iframe execution context and its missing hint; independent drive.py host frames cover the phone, so automated phone coverage is unavailable. Four first-tap welcome skips are intentional because Reveal, Back, Next and Again speak their own current line. Quick Next cancels Whoosh when advancing, as the spec requires. Repeats, keyboard/focus checks, Motion off and resize stress are clean. The automatic mode finder sees zero modes in the separate navigation bar; authored states cover all three, with explicit main-path and Backstage repeat tests.
All 78 audit frames were inspected on labeled sheets, with the crowded compact face opened full size. The pose was repaired afterward and only the three affected compact sizes were re-shot, plus phone fallback frames. Nine post-audit frames verify both head extremes at 1000x625, 800x500 and 680x425, plus the three phone modes. No tool exception or console warning was observed; the temporary host alone requested a missing favicon. No second audit or full review was run.

#### Left open

The spec-level sweep blocker and unavailable recorded narrator are explicit above. No shared kit/script changes, commits or external publication. All work remains in the named tool and Scratch folders; the standalone phone host was removed. Owned ports 9960, 9961, 9963 and host 8765 are closed; no host.html remains.
Initial read/setup shell calls used tool wait thresholds rather than process timeouts; subsequent commands used explicit process limits. No command, including the audit, timed out.

<!-- end part -->

## Refine

<!-- part: refine.md -->

OPEN (round 1, Claude Refine 2026-11-05; Codex fixes next)
Counts: blockers 2 (general 2, family 0), should fix 8 (general 8, family 0), polish accepted 10

### Refine: puppet-show-feelings

Lenses: refine/teaching.md, refine/play.md, refine/craft.md (no sensitivity review needed: nothing cultural, Native or
hard-history). Frames: audit = S:/CurioClass-codex-scratch/puppet-show-feelings/audit-r1/, play = .../play/,
craft = .../craft/. Spot-checked by the integrator: items 1, 2, 3 and 4 (src.html lines read; audit frames
state-like-feeling-1366x768.png and state-ending-0-1366x768.png opened).

#### Blocker
1. **Show's first screen: the hint's own instruction skips the welcome and all of scene 1.** src.html:881-883 (only a
   tap on the painted theater starts the show), :886 (first hint "Welcome to the puppet show! Watch Pom. Then tap
   Next."), :451-454. Nothing plays on load. A child who does what the hint says (Next, or the right arrow) lands on
   scene 2: the happy baseline scene is never narrated, babbled or asked about, and the welcome is never heard. A
   first Show me speaks only "Pom feels happy." with no scene. Seen: play frames/first-next.png (log: only "Whoosh!"),
   craft f2/c-first-key, f2/c-first-reveal, f2/c-first-stage2, audit one-click rows 6-9. Fixed looks like: while the
   show has not started, the first tap on Next, the right arrow, Show me, Again or the theater plays the opening
   (welcome, scene 1 line, babble, question) instead of advancing or revealing; and the waiting hint names an action
   that really starts it (for example "Tap Pom to start the show."). Keep the spoken welcome line as is if the hint
   changes, or change both so the words match. (general)
2. **Backstage Line 5 is dead: Pom never babbles and the narrator names ending buttons that are not there.**
   src.html:401 (scene 5 `n:0`), :822-835 (`#line` cycles `%6`, index 4 included), :689 and :819. On "Line 5" the
   narrator says "What happens next? Tap an ending." and the hint adds "Tap Say it."; every change and Say it babble 0
   syllables, so the Voice row does nothing and Done when 3 fails on that line. Seen: craft f1/c-line5 (babbleLog
   empty) and f1/c-line5-change (`[..,0,150],[..,0,150],[..,0,95]`). Fixed looks like: `Line` skips scene 5 (cycles the
   four scenes and the chosen ending, five lines), the button label and picture follow, and no Backstage line names
   the endings. (general)

#### Should fix
1. **Backstage first change: the voice waits behind the how line, and the flip line lands before any reading and gets
   cut.** src.html:685-696. On the first change the narrator says "Say a clue. Tap Audience says." (about 2.9 s), only
   then Pom babbles (Done when 4 "acts at once" only half holds), then "Only one thing changed, and the feeling
   changed!" plays before the class has seen any reading. A teacher tapping Audience says, as told, cuts the flip line
   after about 0.3 s; it is marked heard and never returns. From the default the very first Head Down flips, so the
   line is spent on tap one. Seen: craft f1/c-back-aud5 (flip 9320, audience 9651, then flip silent x3),
   f1/c-back-head5 (first babble 9415 for a tap at about 6.4 s), play frames/backstage-first-change and
   backstage-flip-walk, teaching vlog.json (9.4 s). Fixed looks like: Pom babbles at once on every change; the how
   line follows the babble and uses the spec's wording without "clue": "What do you see now? Say it. Then tap Audience
   says."; the flip line is spoken once, right after "The audience sees X." on the first Audience says that follows a
   change which flipped the reading (and stays unheard if it was cut before it finished). (general)
2. **Like me: Pom is cut off mid-body with a hard straight edge in mid-air.** src.html:124-125 (`.shelf
   .puppet-window { inset:8% 0 18% }`). The sock ends in a horizontal cut below the shelf board, floating over the
   wall (POLISH.md Art: never crop a character mid-body). Seen: audit state-like-feeling-1366x768.png (integrator
   opened it: confirmed), state-like-vote-1366x768.png, state-like-feeling-680x425.png, play frames/like-sad-1366.png.
   Fixed looks like: the cuff hidden behind the shelf board or a drawn ledge, as Show and Backstage hide it, at every
   size. (general)
3. **Ending "Dot helps": Dot is mostly behind the left curtain and the stick crosses Pom's face.** src.html:55
   (`.dot { left:0 }`), :70 (`#stick`). Only Dot's eye patch and a strip of purple show; the stick runs over Pom's eye
   and mouth instead of up to the kite. Seen: audit state-ending-0-1366x768.png (integrator opened it: confirmed),
   state-ending-0-375x812.png, play frames/ending0-1920.png. Fixed looks like: Dot fully inside the opening beside Pom
   (about left 12 to 18 percent), the stick from Dot up toward the tree and kite, clear of Pom's face. Placement
   only, no new art. (general)
4. **Sad and worried faces look alike at button size; calm reads as sleepy.** src.html:460-468 (`face()`). Both are
   slanted brows over a down curve; scenes 3 and 4 are exactly worried then sad, and pre-readers rely on the face.
   Seen: play zoom-faces.png, audit state-like-feeling-1366x768.png and -375x812.png (integrator: confirmed at
   1366). Fixed looks like: worried with raised, pinched inner brows and a small wavy or open mouth; sad with drooping
   outer brows and a clear frown; simple dot eyes on all six so they read as faces; check at 27 px and 38 px.
   (general)
5. **Like me prompt never links the feeling to Pom's story (TH:Cn10).** src.html:732 and the `life` lines (about
   :423). "When did you feel worried? Tell Pom, or pass." is a generic feelings chat; Cn10.1 asks the child to relate
   a character's feeling and experience to their own. Seen: teaching likeme.json, audit state-like-feeling-1366x768.png.
   Fixed looks like: each prompt names Pom's moment first, for example "Pom felt worried when the kite got stuck.
   When did you feel worried? Tell Pom, or pass." (happy scene 1, excited scene 2, worried scene 3, sad scene 4,
   proud A new kite, calm Wait for the wind). Update voice/lines.json and record lines to match. (general)
6. **Ending vote hands the child the reason instead of asking for it (TH:Re8).** src.html:738-747, :855. A vote at
   once replaces "Tap the ending you like. Tell Pom why." with the narrator's own reason ("Some people like it when a
   friend helps.") about 4 s later. Seen: teaching likeme.json (13.8 s then 18.0 s), audit state-like-vote-1366x768.png.
   Fixed looks like: a vote first shows and speaks "Why do you like that ending? How did it make you feel?"; the
   "Some people like..." line comes on a second tap of the chosen tile (the hint names that tap), so the class's own
   reasons come first. Keep all three vote lines. (general)
7. **Like me notes say nothing about a serious disclosure.** notes.md, Like me and Good to know. Asking five-year-olds
   in front of a class when they felt sad or worried can surface something serious. Fixed looks like: one or two
   sentences: model a small example first, keep it light, and if a child shares something worrying, talk privately
   and follow the school's procedure. (general)
8. **Praise and audience lines are not natural English for K-2.** `praise` and `audience` lines (src.html about
   :422-423, :655). "Yes! That's sad!" sounds like cheering that something is sad; "That's worried!" and "That's
   calm!" are not English; "The audience sees worried." has the same problem. Seen: teaching vlog.json (42.9 s).
   Fixed looks like: "Yes! Pom looks sad!" and "The audience sees a sad Pom." (all six), with voice/lines.json and
   recordings to match. (general)

#### Polish accepted
1. **Show me names the clues, not only the word.** src.html:584, :813. The story text already gives most feelings
   away, so a child can answer without looking at Pom. Reveal card and line: "Pom feels worried. Head down, fast
   voice." (built from the scene's settings and `labels`). (general)
2. **Show me keeps Pom's babble running.** src.html:807-815 (`stopBabble()` in the reveal). A tap mid-babble loses the
   voice clue. Stop only the narrator's lines; let the babble finish. (general)
3. **Head and Bounce icons drawn, not emoji.** src.html:777-778. Rotated sock emoji barely show a tilt and the Small
   and Big arcs (`'⌒'`, `'◠'`) read as one mark (play zoom-controls.png, craft zoom-controls.png). Small drawn SVG
   icons: a sock drooping, level, lifted; a low arc and a tall arc. (general)
4. **"What changed" row readable from the back of the room.** src.html:120, :178, :258, :682. 18 px or more in every
   layout, with the row's icons on each side of the arrow (spec: "icon arrows"). (general)
5. **Backstage Pom bigger.** At 1366x768 Pom fills about a fifth of a mostly empty stage (play
   frames/backstage-flip-walk.png), so the tilt difference is subtle when projected. Enlarge Pom (or crop the stage
   closer) while Done when 1 still holds at 1366x768 and 680x425. (general)
6. **Stage sign text spills over the sign top** at 680x425 and 375 (play frames/show-ending-choice-680.png, audit
   state-ending-0-375x812.png). Clamp the font so it fits the sign. (general)
7. **Check mark on Try it and Ending vote when on.** src.html:357, :378; spec: chosen controls show a check icon
   (audit state-backstage-match-680x425.png, state-like-vote-1366x768.png). (general)
8. **Chosen mode button wraps to two lines at 680x425** ("✓ ☷" over "Backstage"). src.html:36, :150. Keep it on one
   line. (general)
9. **Audience card flush on the stage's right edge at 375 wide.** src.html:260 (`right:0`). Inset it. (general)
10. **Screen reader noise.** src.html:286-288 (`#dots` aria-label on a plain div: give it `role="img"`), :318 (mode
    button emoji read aloud: `aria-hidden` on the icon span). (general)

#### Settled calls
- Severity: Play and Craft rated the first-screen skip and Craft rated the dead Line 5 as should fix. Raised to
  blockers: the default mode's first instruction skips the baseline scene, and Line 5 fails Done when 3 and names
  controls that are not on screen.
- Flip line timing: Craft wanted it right after the change; Teaching and Play wanted it after a reading. Settled on
  after "The audience sees X." following a flipping change: it confirms what the class just saw and cannot be cut by
  the tap the hint asks for.
- Line cycle: Craft offered "skip scene 5" or "give it babble". Settled on skip: the spec gives scene 5 no babble and
  its line is about the ending buttons, which Backstage does not have.
- Sad/worried faces: Teaching filed polish, Play should fix. Should fix: the tool's two key scenes depend on it.
- Dot: Craft filed polish, Play should fix. Should fix: the friend is the point of that ending.
- Keep "Tell Pom, or pass." over the spec's "Tell a friend." (notes.md explains it; safe for a child alone).
- Try it can be met by sweeping buttons: leave it. There is no score; notes say so honestly.
- Two quick Next taps dropping "Whoosh!" is correct (the newer scene's line plays). The audit's "0 modes" note is wrong.
- No new art is needed for any item; Dot and the Like me crop are placement fixes.

#### To the spec's open questions
- Spec text drift to settle after this round: Line cycles five lines, not six (Blocker 2); the after-change line,
  praise, audience, Like me and vote-why lines change (Should fix 1, 5, 6, 8); art came from gpt-image, not the local
  FLUX route the spec names (craft nit 11). Update the spec's Voice and Art sections so later agents do not "fix" them
  back.

#### Not taken
- "all by herself" to "all on Pom's own" (teaching nit 8): reads clunkier; one pronoun is harmless.
- Spec-drift note in notes.md (craft nit 11): sent to the spec's open questions instead.

<!-- end part -->

<!-- part: refine/craft.md -->

### Craft lens: puppet-show-feelings (round 1)

Cold Craft lens, 2026-11-05. Bundle `tools/puppet-show-feelings/puppet-show-feelings.html` as built (not re-bundled).
My frames and logs: `S:/CurioClass-codex-scratch/puppet-show-feelings/craft/f1/` and `f2/` (shots1.json, shots2.json
beside them). Shared audit: `S:/CurioClass-codex-scratch/puppet-show-feelings/audit-r1/audit.md`.

#### Findings

##### should fix

1. **Backstage, Line 5 is a dead line: Pom never babbles, and the narrator names a control that is not there.**
   Where: src.html:401 (scene 5 `n:0`), src.html:822-835 (`#line` cycles all six, index 4 included), src.html:689 and 819
   (babble uses `scenes[state.line].n`). What: `Line` reaches "Line 5", the narrator says "What happens next? Tap an
   ending." and the hint reads "What happens next? Tap an ending. Tap Say it." in Backstage, where there are no ending
   buttons. On that line every change and `Say it` babble 0 syllables, so the Voice row (Slow, Middle, Fast) has no
   effect you can see or hear, `Say it` does nothing, and Done when 3 fails there. How: `f1/c-line5` log (line spoken,
   hint as quoted, babbleLog empty) and `f1/c-line5-change` (babbleLog `[..,0,150],[..,0,150],[..,0,95]` for Head,
   Say it, Voice; frame shows Pom silent). Better: skip scene 5 in the Line cycle (five lines: four scenes and the
   chosen ending), or give it real babble and a line that does not name the endings. Tag: general.

2. **Following the first hint skips the welcome and all of scene 1; a first tap on Show me gives the answer first.**
   Where: src.html:451-454 (`speaks` includes `#next, #back, #again`), src.html:881-883 (only a tap on the theater
   starts scene 1), src.html:886 (first hint "Welcome to the puppet show! Watch Pom. Then tap Next."). What: nothing
   plays on load; Pom bobs silently. A child doing what the hint says (tap Next, or press the right arrow) jumps to
   scene 2: the welcome is never heard and scene 1's line and question are never spoken. A first tap on `Show me`
   speaks only "Pom feels happy." with no welcome and no scene. Only a tap on the painted stage plays the intended
   opening (welcome, then scene 1 about 4.4 s later, babble, question). How: audit table rows 6-9 ("not heard" for
   Show me, Back, Next, Again), confirmed on my own runs: `f2/c-first-key` (ArrowRight: only "Whoosh!"),
   `f2/c-first-reveal` (only "Pom feels happy."), `f2/c-first-stage2` (stage tap: welcome, scene line, question).
   Better: on the first tap of Next/arrow/Show me, play scene 1 (welcome, line, babble, question) instead of
   advancing, or have the welcome and scene 1 start on the first tap anywhere. Tag: general.

3. **Backstage's key teaching line arrives about 4 s after the tap and is cut by the action the hint asks for.**
   Where: src.html:690 (`flip` queued only after the babble finishes), src.html:694-696 (the first change waits for the
   "Say a clue" line before it babbles). What: on the first change the sequence is "Say a clue. Tap Audience says."
   (about 2.9 s), then the babble, then "Only one thing changed, and the feeling changed!". A teacher who taps
   Audience says, as told, at a 4 s pace cuts the flip line after about 0.3 s; it is logged as spoken and is silent
   for the rest of the page load. The first change's babble also waits about 3 s behind the how line (Done when 4,
   "acts at once", only half holds: the pose moves at once, the voice does not). How: `f1/c-back-aud5` log: flip
   spoken at 9320, "The audience sees worried." at 9651, then flip `silent` at 14762, 23101, 31371; `f1/c-back-head5`
   babbleLog first entry at 9415 for a tap at about 6.4 s; `f2/c-keys-back` shows the same cut (flip spoken 8270,
   next flip dropped). Better: say the flip line right after the change (before or instead of the babble), or let it
   come back when it was cut early. Tag: general.

##### polish

4. **Bounce icons Small and Big read as the same mark.** Where: src.html:778 (`'⌒'`, `'◠'`). What: at 1366x768 both
   are a thin arc of almost the same size; the spec asks for a small arc and a big arc. The Head icons (a pair-of-socks
   emoji rotated 28, 0 and -18 degrees) also barely show a tilt. How: `craft/zoom-controls.png` (crop of
   `f1/c-line5-change`). Better: drawn SVG icons (a low and a tall arc; one sock drooping, straight, lifted), like
   the drawn feeling faces. Tag: general.

5. **"What changed" row is 14 px (12 px in the short layouts), plain text arrows.** Where: src.html:120, 178, 258,
   682. What: the spec calls for icon arrows; on a projector for K-2 the row is unreadable from the back of a room.
   How: `audit-r1/state-backstage-audience-1366x768.png` (bottom of the console). Better: 18 px or more with the
   row's icons ("sock Down to sock Up"). Tag: general.

6. **Dot is mostly hidden in the Dot helps ending.** Where: src.html:55 (`.dot { left:0 }`) inside the clipped puppet
   window. What: Dot sits at the window's left edge behind the tied curtain; only an eye patch and part of the body
   show, and the stick floats across Pom's face. How: `audit-r1/state-ending-0-1366x768.png`. Better: move Dot in
   from the curtain (about left 12 to 18 percent) so both puppets read. Tag: general.

##### nit

7. Try it and Ending vote, when on, show a thick border and tint but no check mark (spec: chosen controls show a check
   icon). src.html:357, 378; `audit-r1/state-backstage-match-680x425.png`, `state-like-vote-1366x768.png`. general.
8. At 680x425 the chosen mode button wraps to two lines ("✓ ☷" over "Backstage"). src.html:36 and 150;
   `audit-r1/state-backstage-match-680x425.png`. general.
9. At 375 wide the audience card sits flush on the stage's right edge (`right:0`, src.html:260).
   `audit-r1/state-backstage-audience-375x812.png`. general.
10. `#dots` has an `aria-label` on a plain div (no role), and the mode buttons' emoji are read aloud by screen readers
    ("performing arts Show"). src.html:286-288, 318. general.
11. Spec drift in words, settled in notes for one of them: the after-change line is "Say a clue. Tap Audience says."
    (spec: "What do you see now? Say it. Then tap Audience says."), the Like me prompt is "Tell Pom, or pass." (spec:
    "Tell a friend."; notes.md explains it, fine). Art was drawn with gpt-image (prompts.json `source`, src.html:11),
    not the local FLUX route the spec names. Worth a line in the spec or notes so later agents do not "fix" them back.
    general.

#### Checks that passed

- **Contract:** one file, 1,188,058 bytes (under the 2 MB goal); no `http` URL anywhere in the bundle; no resource
  requests after load (`performance.getEntriesByType('resource')` empty, `f1/c-contract`); kit used (`Curio.voice`,
  `Curio.init`, kit css); no console errors or exceptions in any of my 24 shots or in the audit.
- **Frame times:** 240 frames at 1366x768, median 16.7 ms, p95 16.8 ms in Show and 16.7 ms in Backstage on Big bounce
  and Fast voice (`f2/c-fps-show`, `f2/c-fps-back`). Headless Chrome with GPU off; 60 fps held.
- **Ease:** Head Up to Down eases -18 to 28 degrees in about 250 ms (`f2/c-ease`), matching the spec.
- **Motion off:** body gets `calm`, kit sets transitions and animations to 0.01 ms; kite moves 0 px over 500 ms between
  scenes, breeze has no animation (`f2/c-calm-kite`); the new-kite unfold resolves at once (`f2/c-calm-ending1`).
  Audit "Motion off" row clean.
- **Access:** focus ring 4 px solid #9638a9 on Tab (`f1/c-tab`); every tool control 60 px tall (audit, every size;
  `f2/c-like-sizes`); H, V, B step the rows and A shows the audience card (`f2/c-keys-back`); arrows move scenes in
  Show; chosen Head/Voice/Bounce and feeling cards show a check and thick border; feelings always pair face and word.
  Contrast recomputed: white on brand 5.30, muted on panel 6.25, changed row #4d5f55 on #f7edda 5.86, gold text 9.53.
- **Lines:** `allLines()` (115) and `voice/lines.json` (115) match word for word, no line on either side only.
- **Art:** all 10 `art:` tokens have prompts.json entries, all `people: false`; no people in any picture.
- **Words:** no em dash in src.html, notes.md, lines.json, prompts.json; "Curio Class" never shortened; nothing stored
  but the kit's Motion preference, which the Motion button's title and notes.md both state.

#### Standard voice check

Held clicks (0.12 s), Sound and Motion on, 1366x768.

| line | kind | expected | spoken | run |
|---|---|---|---|---|
| Welcome (Show) | how | once, on first plain tap | once (stage tap); never on first Next/Back/Again/Show me/arrow | f2/c-first-stage2, f2/c-first-key, audit |
| scene lines | event | every scene | 5 of 5 | f1/c-show-next5 |
| How does Pom feel? | event | every scene | 5 of 5 | f1/c-show-next5 |
| Welcome (Backstage) | how | once | once | f1/c-back-head5 |
| Say a clue. Tap Audience says. | how | once in 5 changes | 1, then hint only | f1/c-back-head5 |
| Only one thing changed... | how | once | 1 (cut after 0.3 s when Audience tapped), then silent | f1/c-back-aud5 |
| The audience sees X | event | 5 of 5 | 5 of 5 | f1/c-back-aud5 |
| Make Pom look X | event | each new target | 7 of 7 | f1/c-try6 |
| Yes! That's X! | event | every target met | 6 of 6, all six targets cycled | f1/c-try6 |
| Welcome (Like me) | how | once | once | f1/c-like5 |
| When did you feel X? | event | 5 of 5 | 5 of 5 | f1/c-like5 |
| Tap the ending you like. | how | once | once | f1/c-like5 |
| ending vote lines | event | 5 of 5 | 5 of 5 | f1/c-like5 |

- Stale lines: three Next taps 0.2 s apart, then Backstage, then Show: each line cut by the next, nothing played after
  its moment (`f1/c-stale`). Line 5 in Backstage names absent ending buttons (finding 1).
- Read during a line stops it and speaks scene line plus hint (`f1/c-read-during`); Read with Sound off speaks
  (`f1/c-read-soundoff`). Sound off then on brings the skipped welcome once (`f1/c-first-sound`). Sound alone says
  nothing (audit row 2).
- Order: lines followed the actions in every run.

#### Audit pilot

- **Leads confirmed:** the four "welcome not heard" rows (Show me, Back, Next, Again): confirmed and widened to the
  arrow key and to scene 1 being skipped (finding 2).
- **Leads wrong or harmless:** "#next: event line cut (hush) and never heard whole: Whoosh!" is the intended
  behaviour (a new Next tap cuts the old scene, spec "a tap during a line stops it and goes"; the newer scene's line
  plays). The audit's note "this one has 0 modes" is wrong: the tool has three mode buttons.
- **Missed:** the audit walked only the ten Show and header controls, none of Backstage's (Head, Voice, Bounce, Say
  it, Line, Audience says, Try it) or Like me's, so it could not see the dead Line 5 (finding 1) or the cut flip line
  (finding 3). Also icon legibility (finding 4), the hidden Dot (finding 6) and missing check marks on toggles (7).

<!-- end part -->

<!-- part: refine/play.md -->

### Play lens: puppet-show-feelings (round 1)

Cold Play lens, 2026-11-05. Played twice: as a K-2 child alone at home (rule 4), and as a teacher projecting it.
Shared audit: S:/CurioClass-codex-scratch/puppet-show-feelings/audit-r1 (its size, state, Motion off and resize rows are
clean and cited, not re-shot). My frames and logs: S:/CurioClass-codex-scratch/puppet-show-feelings/play/
(frames/, out2.txt, out3.txt, shots1-3.json, zoom-*.png).

Counts: blocker 0, should fix 4, polish 5, nit 1.

#### Should fix

1. **Show, first screen: the first instruction skips the first scene.** (src.html:886, 451, 881-883; general)
   On load nothing plays (idle-8s: empty voice log, no babble after 8 s). The hint says "Welcome to the puppet show!
   Watch Pom. Then tap Next." A child who does what it says taps Next and lands on scene 2: scene 1 (Pom and the new
   kite, the happy baseline) is never narrated, babbled or asked about (frames/first-next.png, log: only "Whoosh!").
   The scene only starts from a tap on the theater or Again, and neither is named anywhere; a tap on Motion or the
   Show button also leaves it unplayed (audit one-click table). Better: any first tap starts scene 1 (or Next on an
   unplayed scene 1 plays it), and the waiting hint names the real action, for example "Tap Pom to start the show."
2. **Like me: Pom is cut off mid-body with a hard edge in mid-air.** (src.html:124-125, `.shelf .puppet-window`;
   general, a POLISH.md Art lesson: never crop a character mid-body)
   The sock ends in a straight horizontal cut below the shelf, floating over the wall, at every size I looked at
   (audit state-like-feeling-1366x768.png, state-like-vote-1366x768.png, state-like-feeling-680x425.png,
   frames/like-sad-1366.png). Better: hide the cuff behind the shelf board or a ledge, as Show and Backstage do.
3. **Ending "Dot helps": Dot is mostly hidden behind the left curtain, and the stick runs across Pom's face.**
   (src.html:55, 70; general)
   At 1366x768 only Dot's eye patch and a strip of purple show (audit state-ending-0-1366x768.png); at 1920x1080 and
   375 she is half behind the curtain (frames/ending0-1920.png, audit state-ending-0-375x812.png). The ending is about a
   friend helping, and the friend is barely on stage. The stick crosses Pom's eye and mouth instead of reaching the
   kite in the tree. Better: Dot fully inside the opening beside Pom, the stick from Dot up to the tree.
4. **Sad and worried faces look the same at button size.** (src.html:460-468; general)
   Both are a slanted brow pair over a down-curved mouth; at the 38 px Like me size they are hard to tell apart, and
   calm reads as sleepy (play/zoom-faces.png, audit state-like-feeling-1366x768.png). K and grade 1 children who
   cannot read the word rely on the face, and these two are the feelings the tool most needs them to separate
   (scenes 3 and 4 are worried then sad). Better: worried with raised, pinched inner brows and a small wavy or
   flat-open mouth; sad with drooping outer brows and a clear frown; add simple eyes so faces read as faces.

#### Polish

5. **"Only one thing changed, and the feeling changed!" is spent on the first tap.** (src.html:685-691; general)
   From the default (Up, Middle, Small: happy) the very first change, Head Down, flips the reading to worried, so the
   one-time line plays before the child has seen any reading at all (frames/backstage-first-change log: welcome,
   "Say a clue...", flip line). It never plays again (backstage-flip-walk: second flip "silent"), so the Down-Slow-Still
   walk the teacher notes describe never gets it. Better: speak it on the first flip after Audience says has been
   shown once, when the child has a reading to compare against.
6. **The first Backstage change speaks before Pom performs it.** (src.html:694-696)
   The narrator says "Say a clue. Tap Audience says." first and Pom only babbles after the line ends, so the child is
   asked for a clue about a performance not yet seen or heard. "Clue" is also an abstract word for kindergarten.
   Better: Pom babbles at once, then "What did Pom do? Say it. Then tap Audience says."
7. **Show me cuts Pom's babble.** (src.html:807-815)
   The question card and Show me are live from the start of the scene; a tap while the narrator or Pom is talking
   stops the babble, so the voice-speed clue is lost and the answer comes with no performance. Better: keep the babble
   running when Show me is tapped (only the voice lines need to stop), or hold the reveal until the babble ends.
8. **Head icons don't show up and down.** (src.html:777)
   A rotated sock emoji at 24 px reads as three slightly different socks, not Down, Straight, Up (play/zoom-controls.png,
   audit state-backstage-audience-1366x768.png). Voice (snail, shoe, hare) and Bounce (dot, small arc, big arc) read
   well. Better: a small drawn Pom head with a clear down, level and up tilt, or the sock plus an arrow.
9. **Backstage Pom is small for the job.** At 1366x768 Pom fills about a fifth of a wide, mostly empty stage
   (frames/backstage-flip-walk.png, frames/tryit-sweep.png), so the 18 to 28 degree tilt difference is subtle from the
   back of a room. Done when 1 holds, but a bigger Pom (or a stage cropped closer) would make the clues land for a
   projected class.

#### Nit

10. **Stage sign text spills over the sign top** at 680x425 and 375 ("Pom" clipped at the sign edge):
    frames/show-ending-choice-680.png, audit state-ending-0-375x812.png.

#### What works

- The full Show run as a solo child (frames/show-full-run, out2.txt): every scene line, the question each scene, the
  reveal, the ending choice and its line in order, babble at the right speeds (150, 95, 95, 260, 260 ms). Next is
  disabled on scene 5 and no line names it. Pacing is about 12 s from scene start to the question: room to guess.
- Try it praises a met target and moves on after 2 s (tryit-sweep). It can be solved by sweeping buttons; the notes
  say so honestly and treat it as exploration, which fits K-2.
- Audience card hides on every change; Read describes only the settings while it is hidden, so it gives nothing away.
- Like me: "Tell Pom, or pass." keeps it safe and solo-friendly; the vote has no counts.
- Feel: the cardboard theater, the kite moving between scenes and the three ending pictures are charming, and the
  three-ending choice is the moment a child would replay for.

#### Audit pilot

- Leads confirmed: "welcome not heard" after a first tap on Next (part of finding 1: the real cost is that scene 1 is
  skipped, not just the welcome).
- Leads wrong: Next two quick taps "event line cut (hush)": the second Next changes the scene, so dropping "Whoosh!"
  is correct. "Welcome not heard" after Show me, Back and Again: those taps speak their own lines, which is right.
- Missed: the first screen never starts the show on its own and its hint points at the control that skips scene 1;
  the Like me mid-air crop; Dot hidden by the curtain; sad and worried faces alike; the flip line's timing. Also a
  harness note: drive.py's plain `wait` showed the voice queue stalled after the first line (out2.txt stage-tap-2),
  but with the page polled every second the same tap ran normally (out3.txt diag-stage), so it was not reported.
- Nothing cultural, Native or hard-history: no sensitivity review needed.

<!-- end part -->

<!-- part: refine/teaching.md -->

### Teaching lens: puppet-show-feelings (round 1)

Cold lens, 2026-11-05. Read spec.md, src.html, notes.md, art/prompts.json, audit-states.json, the shared audit
(S:/CurioClass-codex-scratch/puppet-show-feelings/audit-r1) and the NCAS Theatre at a Glance PDF (K to 2 rows of
TH:Re7.1, TH:Re8.1, TH:Cn10.1). Own runs: drive.py on port 9881, shots in
S:/CurioClass-codex-scratch/puppet-show-feelings/teaching/ (shots.json, shots2.json, out/, vlog.json, show5.json,
likeme.json, read.json).

Not a Curiosity. Nothing cultural, Native or hard-history: no sensitivity review needed (the Like me memory prompt is
a disclosure question, covered below as a notes item, not a sensitivity item).

#### Standards against the NCAS wording

- **TH:Re7.1** (K: express an emotional response to characters; 1: recall choices made; 2: recognize when artistic
  choices are made). Taught well. Show asks "How does Pom feel?" every scene; Backstage has the student make one
  choice at a time and watch the reading change; the "what changed" row names the choice. Pass.
- **TH:Re8.1a** (K: identify preferences; 1: explain preferences and emotions; 2: explain how personal preferences
  and emotions affect an observer's response). K is taught (ending choice, ending vote). Grades 1 and 2 are thin: see
  finding 2.
- **TH:Cn10.1** (K: similarities between characters and oneself; 1: identify character emotions and relate them to
  personal experience; 2: relate character experiences to personal experiences). Like me never connects to Pom or
  the story: see finding 1.

#### Findings

1. **should fix** (general). Like me, src.html:732 and :423 (`life` lines). The card prompt is "When did you feel
   worried? Tell Pom, or pass." with no link to Pom. Cn10.1.1 asks the child to identify a *character's* emotion and
   relate it to their own; Cn10.1.2 to relate the character's *experience*. As built it is a generic feelings chat.
   Every feeling already has a story moment, so the fix is cheap: "Pom felt worried when the kite got stuck. When did
   you feel worried?" (happy scene 1, excited scene 2, worried scene 3, sad scene 4, proud A new kite, calm Wait for
   the wind). Seen: likeme.json (spoken lines), frame audit-r1/state-like-feeling-1366x768.png.

2. **should fix** (general). Like me ending vote, src.html:738-747 and :855. Tapping an ending at once replaces the
   prompt "Tap the ending you like. Tell Pom why." with the narrator's own reason ("Some people like it when a friend
   helps."), spoken about 4 s later (likeme.json: 13.8 s then 18.0 s). The child is handed the why instead of giving
   it, so Re8.1.1 (explain preferences and emotions) and Re8.1.2 (how your own preferences and emotions shape your
   response as an observer) are only mentioned. Better: on a vote, first "Why do you like that ending? How did it make
   you feel?" and keep "Some people like..." as the follow-up (or behind a second tap), so the class's own reasons
   come first. Seen: likeme.json, frame audit-r1/state-like-vote-1366x768.png.

3. **should fix** (general). notes.md, Like me and Good to know (rule 8). The prompt asks five-year-olds in front of
   a class when they felt sad or worried. Notes rightly say a child may pass, but they do not name that this can
   surface a serious disclosure (home, loss, fear) or what to do: model a small example first, keep it light, and
   follow the school's procedure and talk privately if a child shares something worrying. One or two sentences.

4. **should fix** (general). src.html:423 and :655 (`praise`), :422 (`audience`). "Yes! That's sad!" reads to a
   child as cheering that something is sad (or the idiom "that's too bad"), and "Yes! That's worried!" and "That's
   calm!" are not natural English. "The audience sees worried." / "sees sad." has the same problem. Plainer for K-2:
   "Yes! Pom looks sad!" and "The audience sees a worried Pom." (or "The audience thinks Pom feels worried."). Seen:
   vlog.json (42.9 s "Yes! That's sad!"). The spec wrote these lines, so the change touches voice/lines.json too.

5. **polish** (general). Show, Show me, src.html:584 and :813. The reveal gives only the word ("Pom feels worried.").
   The story text already carries most feelings ("Oh no! The kite is stuck"), so a child can answer from the words and
   never look at the puppet, which is the whole idea of the tool. Better: the reveal names the clues too, on the card
   and in the line: "Pom feels worried. Head down, fast voice." That makes the default mode teach Re7 the way
   Backstage does.

6. **polish** (general). Backstage first change, src.html:690. "Only one thing changed, and the feeling changed!"
   plays after the babble, before Audience says (vlog.json: 9.4 s, card at 26.3 s). It tells the class the reading
   flipped before they have said what they see. Better: speak it once right after the first Audience says that
   follows a flip, where it confirms instead of tips.

7. **polish** (general). Feeling faces, src.html:460-468. At the small sizes the sad and worried faces are nearly the
   same frown (frame audit-r1/state-like-feeling-375x812.png, the worried card beside sad). Pre-readers lean on the
   face, not the word. Better: give worried a wavy mouth and raised inner brows so it differs from sad at 27 px.

8. **nit** (general). src.html:406. "all by herself" is the only pronoun for Pom; everywhere else Pom is just "Pom".
   "all on Pom's own" keeps it consistent.

#### Done when (spec)

| # | check | result | how |
|---|---|---|---|
| 1 | Pom largest, nine controls visible, 1366x768 and 680x425 | pass | audit frames size-1366x768, state-backstage-audience-1366x768 and -680x425 |
| 2 | 27 settings and every scene read as the table | pass | logic shot: `feeling()` against the spec table, 0 mismatches; all 8 scenes/endings and 6 presets match |
| 3 | ease from where it is; babble Slow 260, Middle 150, Fast 95 ms | pass | ease shot: tilt -18 to 28 over about 160 ms (4, 17.8, 23.2, 27.1, 28); babbleLog ms 150/260/95, pitch 1/0.85/1.15 |
| 4 | a tap during babble acts at once and hides the card | pass (code and audit) | change() bumps serial, stopBabble, hides #audience-card; audit held clicks clean |
| 5 | three endings; Next disabled only on scene 5; no line names Next there | pass | showwalk: Next disabled only at index 4; ending how line names the three endings only; show5.json plays A new kite and Dot helps, audit state-ending-2 the third |
| 6 | Try it praises every met target, cycles all six | pass | try shot: all six met in order and wrapped to sad; praise spoken with real input (vlog.json 42.9 s) |
| 7 | how lines once; scene lines and the question every scene | pass | vlog.json: change how once, flip once then silent x4; show5.json: question after every scene, ending how silent the second time |
| 8 | 60 px controls with icon and word; face plus word | pass | audit size rows clean; frames |
| 9 | Motion off: no bounce or ease, babble timing the same | pass | motionoff shot: tilt jumps to 28, translateY(0px) throughout, babble 150 ms |
| 10 | no network, nothing saved | not my lens | no storage calls in src.html beyond the kit Motion preference |

Facts: the table recomputed (sad 4, worried 7, calm 3, proud 3, happy 5, excited 5; 27 cells), tilt angles, bounce
sizes and syllable timings all match the spec. Citations check out (Dael, Mortillaro and Scherer 2012, Emotion 12(5)
1085-1101; Wallbott 1998, EJSP 28, 879-896; Juslin and Laukka 2003, Psych Bull 129(5) 770-814: slow rate for sadness,
fast for fear and happiness). Notes describe this tool truly; Read in Backstage gives only the settings while the card
is hidden (read.json), so no giveaway. Support at home ideas are doable tonight.

Cheap pass: Try it can be met by sweeping H, V and B (notes say so honestly; there is no score, so it is not a
blocker). Like me shows each feeling's preset pose, which is a demonstration, not a quiz answer.

#### Audit pilot

- Leads confirmed: none that bear on teaching. The "welcome not heard" lead (first tap on Show me, Back, Next or
  Again) is real in code (the Show welcome only plays from a stage tap or mode entry), but its teaching cost is small:
  the welcome only says "Watch Pom. Then tap Next." Left to Play.
- Leads wrong: none seen.
- Missed (by design): findings 1 to 4 (standards depth, disclosure note, praise wording), the clue-free reveal, the
  early flip line, and the sad/worried face likeness.

<!-- end part -->

## Fix

<!-- part: polish.md -->

### Polish: puppet-show-feelings (Codex fix, round 1)

Verified: both blockers, seven should-fix items and nine accepted polish items. Two items remain NOT FIXED as detailed below.

Evidence paths below are relative to `_scratch/puppet-show-feelings/`. Before frames and JSON were captured from the incoming bundle, before repairs. Failed iframe-selector shots were replaced by `phone-before/` captures inside the 375x812 host.

#### Blocker
1. FIXED: All first Show actions open scene 1, including Next, right arrow, Show me, Again and theater. The waiting hint says "Tap Pom to start the show." `before-first-next.json` reached state.scene=1 (the second scene) with only Whoosh; first reveal left started false. Every `after-first-*.json` stays at state.scene=0 and logs welcome, baseline, six 150 ms syllables, question, without cuts. Frames: `before/before-first-next.png`, `after-behavior/after-first-next.png` and the four other first-action frames.
2. FIXED: Backstage Line now cycles four speaking scenes plus the selected ending, with the label and picture following. Before Line 5 was the choice prompt with n=0. `after-line5.json` has the Dot ending and n=8 on change and Say it. Frames: `before/before-line5.png`, `after-behavior/after-line5.png`. `check-line-cycle.json` wraps 2, 3, 4, 5, 1, 2, 3 with syllable counts 8, 7, 5, 8, 6, 8, 7; no choice prompt appears.

#### Should fix
1. FIXED: Every change hushes the narrator and starts babble in its handler; the full how-to follows babble. The flip explanation waits for a completed audience result and is remembered only after completion. Before: `before-flip.json` had no babble at the audience tap. After: babble 3535 ms, how 4539 ms, audience 5686 ms, flip 10758 ms (`after-flip.json`). `check-flip-retry.json` shows a Read-cut flip at 10758 ms and a complete retry at 25983 ms; `check-voice-back.json` has the complete how, result, flip in order. Frames in `after-voice1/`.
2. FIXED: A textured foreground shelf ledge hides the cuff, with the puppet base raised enough to remain visible at tall narrow sizes. Before: `before/before-like-1366.png`, `before/before-like-680.png`, `phone-before/before-phone-like.png`. Final: `after-placement-final/after-like-{680,800,1000,1280,1366,1920,760,375}.png`, all viewed. No scrolling or controls below 60 px in their JSON probes.
3. FIXED: Dot sits at left 15% inside the opening beside Pom; the stick points up toward the tree behind both puppets. The rescued kite was also moved clear of Pom's face. Before: `before/before-dot-{1366,1920}.png`, `phone-before/before-phone-dot.png`. After: `after-placement-final/after-dot-{1366,1920,375}.png`, all viewed.
4. FIXED: All six faces have two dot eyes. Worried has raised pinched brows and a wavy mouth; sad has drooping outer brows and a frown; calm has awake dot eyes and a small smile. Compared at actual 27 px phone/compact and 38 px laptop sizes in the before and final Like me frames above.
5. FIXED: All six Like me prompts name Pom's matching story moment first and retain "Tell Pom, or pass." Worried is visible and voiced in final Like me frames. `check-like-all.json` logs happy, excited, worried, sad, proud and calm once each, all complete; `after-voice2-small/check-like-all.png` was viewed.
6. FIXED: A first vote asks "Why do you like that ending? How did it make you feel?" A second tap on the selected tile supplies the preserved example reason; the hint names that tap. Before: `before-vote.json`. After: `after-vote-first.json`, `after-vote-second.json`, and `after-behavior/after-vote-{first,second}.png`. `check-voice-votes.json` logs all three original reasons after their reason-first prompts; `after-voice2-small/check-voice-votes.png` was viewed.
7. FIXED: Notes now say to model a small everyday example, keep it light, speak privately after a worrying disclosure and follow school procedure. `before-notes.txt` lacked that advice; `static-check.txt` confirms the new procedure text. This is teacher guidance, not a student gate.
8. NOT FIXED (full voice proof incomplete): The code, manifest and live allLines now use "Yes! Pom looks X!" and "The audience sees a/an X Pom." `check-voices-0.json` and `check-voices-3.json` prove all six audience lines and five praise lines, including "an excited Pom". Happy praise was not triggered: that probe began with matching settings, and the no-op guard correctly withheld praise. Its revised literal is present in the live manifest, but I did not hear it, so I am not marking this item fully verified. No recordings existed before this repair, and none were made under CODEX-BUILD's no-recording rule.

#### Polish accepted
1. FIXED: Show me speaks and displays Head, Voice and Bounce clues. `after-voice2-small/check-clue-card-{1366,680,375}.png` were viewed; each shows "Head up, middle voice, small bounce." The six reveal lines follow each scene's preset.
2. FIXED: Reveal hushes only narration; it no longer changes the babble serial or stops running syllables. `check-reveal-mid-babble.json`: mouth talking before=true and immediately after reveal=true, same six-syllable run. `after-voice3/check-reveal-mid-babble.png` viewed.
3. FIXED: Head controls use drawn sock poses and Bounce uses visibly low/high SVG arcs. `after-layout2/after-back-{1366,680}.png` viewed.
4. FIXED: What changed is 18 px in every layout and includes the old and new icons beside the arrow. Final layout JSON reports 18 px; compact and laptop Backstage frames show both icons.
5. NOT FIXED (phone extreme still clips): Pom is enlarged and all nine controls remain visible at 1366x768 and 680x425. Final frames `after-voice3/after-back-{1366,680}.png` and `fix-audit/state-backstage-big-up-{1366x768,680x425}.png` were viewed. CSS height grew from 88% to 104%, laptop width from 26% to 38%. However, the final full-size `fix-audit/state-backstage-big-up-375x812.png` shows the top of Pom's head clipped at the phone stage edge. The main-size improvement is real, but this regression leaves the item open. The mechanical audit does not detect painted-character clipping.
6. FIXED: Sign typography follows theater width, clamped to at least 10 px and kept on one line. `after-layout2/after-ending-680.png` and `after-placement-final/after-dot-375.png` show text inside the painted sign.
7. FIXED: Try it and Ending vote display a check when on. `after-layout2/after-back-680.png`, `after-vote-1366.png`, `after-vote-680.png` viewed.
8. FIXED: Chosen mode is nowrap with reduced compact padding. Backstage stays on one line in `after-layout2/after-back-680.png`.
9. FIXED: Phone audience card has a 3% right inset and is lower so it clears Pom's face. `after-voice3/after-back-375.png` viewed: the card has space from the stage edge and does not cover the eyes.
10. FIXED: Scene strip now has role img and its current scene label; all three mode icon spans are aria-hidden. `static-check.txt`: 1 scene role and 3 hidden mode icons.

#### Settled calls
- Applied both blocker severities: opening skip and silent Line 5.
- Flip follows the audience reading, not the change; interrupted explanations can return.
- Line skips the no-babble ending-choice scene and cycles five lines.
- Applied the sad/worried should-fix priority with visibly different faces.
- Applied the Dot should-fix priority with placement inside the opening.
- Kept "Tell Pom, or pass." and optional disclosure.
- Kept Try it as exploration that can be swept, with no score or mastery claim, as expressly settled. Handoff's older open-blocker wording now records that settlement.
- Kept quick Next interruption behavior and the separate mode navigation.
- No new painted art. The spec's open questions were left untouched.

#### Cheats tried
- Blind Down, Slow, Still sweep: Try it check earned. This is the specifically accepted exploration behavior, not an assessment pass. Notes and handoff say so.
- Eight taps on the already selected Still button: zero extra praise.
- Toggle Try it off/on while matching: zero extra praise.
- Cycle all six targets without changing settings: zero extra praise.
- Sweep settings, leave audience hidden, tap Read: reads only Head, Voice and Bounce plus the instruction, with no hidden feeling answer. `check-cheaps.json`.
- Tap Show me without watching: first tap starts the baseline; a later reveal intentionally supplies word and clues. There is no score, check or saved result for naming it.
- Tap every ending or double tap for the narrator's reason without explaining: preferences and example reasons remain available, with no reflection grade, gate, count or saved result. First tap still requests the child's own reason.
- Read while flip is playing, then Audience says again: the interrupted explanation returns and completes. `check-flip-retry.json`.
- Read first, then Back: starts scene 1 without skipping (`check-extra-start.json`). Seven rapid Line/Say it pairs: every line babbles, no silent scene (`check-line-cycle.json`). The original five startup patterns and these extra paths all ran through the tool handlers.

#### Voice walk
Held clicks were 120 ms with 2 s gaps; listening waits were added for the long story/question beats. All five opening paths log welcome, baseline, babble, question once with no cuts. Backstage change starts babble before the how-to, then Audience says supplies result and flip. The strict 2 s audience tap cuts the how-to, as its log states; a listening walk completes it (`check-voice-back.json`). The flip is not consumed by an interruption. Six life prompts play once each, in happy, excited, worried, sad, proud, calm order, with no cuts. All six audience wordings and five praise wordings were heard in the smaller probes; happy praise lacks an individual voice proof. All three vote reasons played fully on repeated tile taps. The first rapid repeat can cut the reason-first question by design; the separate first-vote listening frame/log shows it completing before a second tap. Logs: `check-like-all.json`, `check-voices-{0,3}.json`, `check-voice-votes.json`.

The manifest equals allLines(): 117 unique fixed lines (`static-check.txt`). Narration remains the existing browser fallback; there are no MP3 recordings to synchronize.

#### Engine changes wanted
No runtime engine change. Existing audit helper request retained in handoff: `scripts/audit_tool.py`, `MODES_JS`, include `nav .seg button` so the separate mode bar is discovered. Authored states and explicit three-mode frames supply coverage here.

#### Audit
The single final audit completed with exit 0 within its 40-minute limit. Report: `fix-audit/audit.md`. All eight sizes and eleven authored states are mechanically clean, Motion off has no infinite animation, resize stress has no exceptions or controls left disabled, and console/error columns are empty. No runtime changes followed the audit.

All 97 audit PNGs were inspected on seven contact sheets (`audit-sheets/`); the 1366, 680 and phone Up/Fast/Big frames and phone Dot ending were also opened full size. That visual review found the phone head crop reported under Polish accepted 5. Default Show and all three modes have current 1366 frames. The separate navigation bar is still missed by automatic mode discovery, as documented under Engine changes wanted; authored states and explicit walks cover it.

Four mechanical leads, each answered:
- Quick `#reveal` twice cuts the welcome when the second tap reveals the feeling. Expected: first tap starts the opening, second acts on the reveal. Full first-tap opening was separately proved.
- Quick `#back` twice cuts the welcome while replaying scene 1. Expected responsive navigation; the new scene line proceeds.
- Quick `#next` twice cuts the welcome while moving to scene 2. Expected newest-scene behavior, as settled in refine.md.
- Quick `#again` twice cuts the welcome while replaying the baseline. Expected immediate replay.
These welcome cuts are permitted by `docs/agents/decisions/BASELINE.md` rule 16 and the unlocked story controls. No input lock or forced listening was added. All five-click checks at a 2 s pace are mechanically clean.

Bundle: 1,162 KB, no bundler failure. No console errors in final targeted batches. The first phone host favicon 404 was a harness request; subsequent host runs use a data favicon. A combined six-example voice probe hit drive's 60 s evaluation limit and was retried once as two smaller probes; both completed. No new recordings exist, so the bundle uses the established browser fallback.

#### Left open
- Should fix 8: happy praise's revised literal exists, but its individual spoken proof is incomplete. Exact follow-up: Backstage, Try it on, Next target three times to happy, Head Down then Up, inspect vlog for "Yes! Pom looks happy!". The other five praise lines and all six audience lines have complete spoken entries.
- Polish accepted 5: Up/Fast/Big clips the top of Pom's head on the phone. Bound phone puppet size/base against its full bounce and recheck Up/Big and Down/Big at 375x812. No post-audit runtime repair was made.
- The spec's explicit open questions stay with the integrator. No recordings were made under CODEX-BUILD's rule. Try it stays sweepable exploration by the settled call.

#### Feel check
Best moment: Dot is now visibly beside Pom while the stick reaches into the tree. The two flat moments were a first instruction that skipped the opening and the silent Line 5; both now play. The original painted theater, texture and mouth frames are retained. `fix-bar-comparison.png` puts the repaired scene beside the current Beat Lab frame; the K-2 theater retains comparable visual care. `fix-grayscale.png` preserves legible labels and selected checks. Both were viewed. The existing Beat Lab bundle was opened read-only because writes outside this tool and Scratch are forbidden.

#### Numbers and coverage
All 27 results match the spec table: sad 4, worried 7, calm 3, proud 3, happy 5, excited 5. Immediate change-to-babble-call latency is 0.1 ms in `check-immediate.json`. The final live allLines array equals the 117-line manifest. No art was generated or rekeyed. Default Show and every mode were re-shot at 1366x768. All named phone checks use an actual 375x812 iframe on host port 8715; Chrome used 9910 and audit 9911. Motion-off frames, keyboard opening and grayscale were checked. Existing files and pre-existing work were preserved; no commits or spec/refine edits.

#### Assumptions made unattended
Followed the explicit settled choices: five Backstage lines, flip after a reading, optional passing, original vote reasons on request, and sweepable Try it as exploration. The existing browser narrator stays because CODEX-BUILD prohibits recording; no incompatible clips exist. The spec's open questions remain for the integrator.

Offline static check: zero external src/href resource attributes, zero remote CSS references, zero fetch calls in the bundled HTML (`final-numbers.json`).

#### To the spec's open questions
Left the spec unchanged. Its five-line cycle, revised voice copy and art-route text drift remain assigned to the integrator, as refine.md requests.

#### Not taken
- Kept "all by herself" in the original new-kite ending.
- Did not add a spec-drift note to notes.md; that belongs to the spec's open questions.

Cleanup verified: Chrome ports 9910 and 9911 and host port 8715 are closed; temporary host.html is removed. No git commits were made.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Handoff: Puppet Show Feelings

#### Built
One offline HTML tool with Show, Backstage and Like me. Teacher led for K-2. The supplied 27-cell table drives every audience result. There is no scoring, microphone or saved work.

#### Source map
`src.html` starts from the Curio Class starter structure and shared kit. CSS defines responsive scene layouts. Content tables and fixed narration live at the start of the tool script. The animation loop interpolates tilt over 250 milliseconds and blends bounce amplitude and speed while preserving phase. Babble synthesizes two or three sine and noise blips per syllable and swaps painted mouth frames.

The Show runner uses a serial token so Back, Next, Again, Read and mode changes invalidate delayed babble or questions. Backstage keeps its own settings across mode changes. The audience card is hidden by every setting tap. Try it checks on changes and offers six targets with a two-second advance. Like me prompts and ending votes stay on this page only.

Selected mode taps return early so they do not cut a welcome or reset work. Every valid target change is a praise event, including a second setting combination that still matches. The Line button builds a miniature scene from the existing embedded art. Like me leaves a wider center gap and offsets the puppet by its preset head tilt so the cards do not cover its face.

`window.__tool` exposes state, content, the table, feeling lookup, mode entry, setting changes, ending selection, voice log and babble timing log for review.

#### Art
Ten original assets, made with the built-in OpenAI image tool. Prompts are in `art/prompts.json`; originals are in `art/raw/`; all WebP processing used the free `art.py --rekey <name>` form. Pom and Dot open-mouth frames were redrawn from the corresponding closed frame as references. The park was redrawn to put the whole tree inside the curtain opening, with the stuck kite visibly in its branches. The new kite was redrawn to reduce pink edge paint. No people or human body parts were generated.

#### Build decisions and open questions
- The spec lists no open questions.
- At short landscape sizes Backstage puts the nine controls beside Pom, following STANDARDS' side-by-side compact requirement. At laptop sizes they sit below the stage.
- At 760 pixels wide and tall, Show stacks its story card below the theater so Pom stays large.
- The listed voice identity, smooth-narrator / Algieba, is preserved in `voice/lines.json`. Build instructions prohibit recording audio, so this build uses the kit's browser speech fallback.
- Nothing from the lesson is stored. The shared kit still remembers its Motion preference, as the tool contract requires.

#### Engine changes wanted
No runtime engine changes. For the audit helper, `scripts/audit_tool.py`, `MODES_JS`: add `nav .seg button` to its mode selector. Its header-only selector misses this tool's separate navigation bar, so the authored states and explicit interaction checks supply that coverage. No shared file was changed.

#### Claude Refine repair, November 6, 2026
This section supersedes the older timing and Line-cycle descriptions below. Every first Show navigation or reveal action starts the welcome and baseline scene. Backstage Line cycles the four story scenes and the selected ending; it omits the silent choice scene. Setting changes hush the narrator and babble immediately, then offer the full first-change instruction. Audience says speaks its result before the flip explanation. A local completion flag uses the voice log's cut marker so an interrupted flip can return; the shared engine is unchanged.

Show me names posture, voice and bounce and keeps a running babble alive. Like me recalls Pom's matching story moment. A first ending vote asks the child's reason; a repeated tap on that tile offers the existing example reason. Passing remains welcome. There is no reflection grade or gate. Try it remains the exploration prompt the settled calls explicitly allow to be swept, not a mastery score.

Pom's shelf cuff is behind a drawn foreground ledge. Dot is inside the opening beside Pom, with the stick behind the puppets. Feeling faces have dot eyes and distinct worried, sad and calm cues. Head and Bounce controls and change arrows use SVG. No new painted art or recordings were needed; narration still uses the existing browser fallback and lines.json matches allLines().

##### Repair proof left open
The final visual audit found the Up/Fast/Big Backstage pose clips the top of Pom's head at 375x812. See `_scratch/puppet-show-feelings/fix-audit/state-backstage-big-up-375x812.png`. The main 1366x768 and 680x425 poses and all nine controls are visible. Polish accepted item 5 remains NOT FIXED because of that phone regression. A follow-up should bound the puppet's phone size/base position against the full bounce excursion, then inspect both Up/Big and Down/Big at 375x812.

Should fix item 8 has revised natural-English literals for all six feelings, but its individual happy-praise voice proof is incomplete. The probe started already matching happy, so the no-op guard correctly prevented praise. To verify it: open Backstage, turn Try it on, cycle Next target three times to happy, change Head to Down and back to Up, and inspect the spoken log for "Yes! Pom looks happy!". Other five praise lines and all six audience lines were logged complete. No runtime changes were made after the single final audit.

#### Cold review repairs, November 5, 2026
Read no longer reveals an unasked audience result. No-op setting taps and merely opening/cycling a matching target cannot earn praise. Target praise checks the current mode and settings; successful target advance resumes after returning to Backstage. Line waits for narration before babbling. A first tap on the theater starts the welcome and opening scene. A short first-change instruction replaces an unfinished welcome when needed. Closing Ending vote restores the selected feeling's prompt.

The first-change how-to is now the shorter "Say a clue. Tap Audience says." It starts before the babble and never waits behind the welcome; later changes babble immediately. Line playback waits for narration. Audience says stops the babble before the result. Personal prompts invite telling Pom or passing, so solo play and privacy work on screen.

The new-kite ending unfolds the new prop and keeps the original red kite visibly stuck. The heavy stick was redrawn with the built-in OpenAI image tool as a thin painted twig. All cutouts were rekeyed with edge despill; texture and the original stage were preserved. Motion's tooltip states its preference stays on the device.

The cold audit completed once with seven mechanical leads: two iframe-context leads, four intentional first-tap welcome skips when a control has its own line, and one intentional quick-Next cancellation. The separate mode bar still needs the documented audit discovery improvement. All 78 saved frames were inspected. The compact down-tilted puppet crowded the right edge at 1000x625; a pose-specific left offset now keeps the full face visible, without shrinking Pom. This narrow post-audit fix receives compact-size rechecks, not a second audit.

#### Sensitivity
No named culture, religion, hard history or human figures. Review the simplified feeling map for overgeneralization across cultures and neurotypes. The cited studies support probabilistic cues, not universal readings. Personal memories are optional; invite passing, and do not infer a child's feelings from their posture or speed.

#### Cold review left open
The spec requires automatic praise and a check as soon as settings match. A blind exhaustive sweep can earn that exploration check. Claude Refine's settled call explicitly permits it because there is no score and the notes explain the limitation. This is not an open blocker in the current round. Try it must not be represented as a mastery assessment. No attempt gate, new feature or kit change was made.

#### Next review
The single full audit completed with ten leads. The report dispositions all of them. Final repairs received targeted checks rather than a second full audit: ending props, Line pictures, worried icon, repeated target praise, same-mode welcomes and Like me's ring layout. All 81 audit frames and all follow-up frames were inspected.

Use the report and `_scratch/puppet-show-feelings/` for frame and audit evidence. Review the feel of the simplified cue model with a class, and listen to babble and browser narration through speakers. A later recording pass can supply the specified narrator without changing the queue.

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
