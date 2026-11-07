# Codex review: puppet-show-feelings

## Played

Cold K-2 solo/projector play preceded builder notes and source: all three modes, six story beats, three endings, cue controls, target and vote. Rich, inviting theater; directing one head change is the strongest teaching moment.

## Findings fixed

- blocker, general, Backstage Read: disclosed the hidden answer. Read now describes settings until Audience says is open; real Read logs verify it.
- blocker, general, Try it: opening an already-matching target and repeatedly tapping its selected setting earned praise. Neither can now earn a check or praise without a changed setting.
- should fix, general, voice: initial theater tap did not play the opening; change instruction arrived too late after babble; Line babbled over narration. Added opening playback, shortened and prioritized the first-change instruction, and sequenced Line narration before babble.
- should fix, general, stale voice/state: stop old audience speech on a setting change, stop babble on audience reveal, validate praise against the current mode/settings, and resume a matched target's advance after mode return.
- should fix, general, Like me: closing the vote left its text in the memory prompt; opening it could leave an unrelated instruction. Restored the current prompt on close, show the vote instruction on open, and stop stale vote speech.
- should fix, general, solo/privacy: personal prompts now invite telling Pom or passing; Motion's tooltip states its preference stays on this device.
- should fix, general, compact Backstage: the down-tilted nose crowded the 1000x625 stage edge. Shifted that pose inward with the same 250 ms easing; retained its size and rechecked compact extremes.
- polish, general, ending/art: replaced the heavy bark branch with a slender painted twig; rekeyed cutouts with despill. The new kite unfolds at Pom's mouth while the original red kite remains stuck, making that choice's outcome clearer.

## Findings left

- blocker, general, Try it: a blind exhaustive sweep still earns automatic target praise. This follows the spec's mandatory check on every matching change. Preventing it needs a changed assessment/attempt rule, so no unapproved gate was added. It is not a mastery check; notes and handoff now say so.
- should fix, general, voice production: the specified Algieba recordings are absent. CODEX-BUILD.md explicitly says not to record audio, so the browser fallback stays and a later authorized voice pass is needed.
- polish, general: very fine key-color edging remains on some lossy cutouts at magnification; the pictures retain their texture and look coherent at the tested display sizes.

## Break it

- Try it, pre-fix: prepare sad, enable Try it, tap selected Down repeatedly. Four praise starts without four changes. Post-fix: no check, no praise, and the unchanged taps do not increment changes.
- Try it, post-fix blind 27-setting sweep: earned sad and calm praise without consulting the target or reading cues. Open blocker above. No score, best record, saved success or timer score exists.
- Audience says: all 27 actual-click combinations agree with the spec table. Changing settings hides the card; Read no longer supplies its hidden label. Repeated reveals are explanations, not assessment passes.
- Show me: immediate reveal and rapid Next/Back remain allowed by the spec; they carry no success claim. Scene 5 alone blocks Next until an ending is chosen. All endings were played.
- Like me and ending vote: all choices are preferences, no correct-answer gate. Changing/closing a vote restores the appropriate instruction. Passing on a personal memory is explicit; no question assumes the child made a mistake.

## Voice walk

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

## Facts checked

- All 27 authored classifications and all story/ending presets: independently transcribed spec table and actual-click results. Counts: sad 4, worried 7, calm 3, proud 3, happy 5, excited 5. Head-only quiet walk: sad, calm, proud. Independent squared-distance computation confirms the five specified ties and no non-nearest selections.
- Tilt 28/0/-18 degrees, easing 250 ms; bounce 0/12/34 scaled px at 0/1.2/2.2 Hz; babble 260/150/95 ms, pitch .85/1/1.15: spec's authored animation model, inspected in source and sampled in babble logs. These are not measured human thresholds.
- Posture/movement can convey emotion, with varied patterns: [Dael, Mortillaro and Scherer (2012), University of Geneva](https://archive-ouverte.unige.ch/unige:97844).
- Posture/movement also reflect activation and individual actor differences: [Wallbott (1998), University of Salzburg](https://uni-salzburg.elsevierpure.com/en/publications/bodily-expression-of-emotion/).
- Slow sadness and faster happiness/fear vocal cues, interpreted probabilistically: [Juslin and Laukka (2003)](https://pubmed.ncbi.nlm.nih.gov/12956543/), Table 11 in the [paper](https://www.brainmusic.org/EducationalActivities/Juslin_emotion2003.pdf). The six-label table is an authored simplification, not a validated emotion detector.
- Recognition, preferences and personal connection: [NCAS Theatre K-2, pages 6, 7, 9](https://nationalartsstandards.org/sites/default/files/2021-11/Theatre%20at%20a%20Glance.pdf), checked against Show, ending choice and Like me activities. All three module codes have actions.
- Story and ending preferences: original fiction from the spec, not historical or scientific facts. No health, law, finance or safety instructions are taught.
- Palette contrast independently recomputed: 5.30:1, 4.94:1, 14.98:1, 6.06:1 (white/brand, brand/paper, ink/paper, muted/paper).

## Sensitivity

No named culture, religion, hard history or human figures. A cultural reviewer should check that a simplified posture/speech model does not imply universal rules across cultures or neurotypes. Personal disclosure is optional on screen; notes discourage inferring children's actual feelings from their movement. All ten art assets are marked people:false.

## Flattest moment left

Like me still depends on a spoken conversation; clicking cards alone is brief. The new-kite ending was the flattest visible payoff and now has an unfolding replacement, a mouth-level prop and the still-stuck original.

## Graphics

All ten final assets and their in-scene use inspected: theater, park, both Pom poses, both Dot poses, both kites, stick and shelf. One stick redraw, no new topic/assets, all cutouts rekeyed. No missing art tokens or human figures. Final bundle: 1160.2 KB. Compared fresh Beat Lab and Snowy Mail Route frames; kept the strong handmade stage and large sock character.

## Audit

One final audit completed within its 40-minute limit, seven leads. Two phone leads are a missing iframe execution context and its missing hint; independent drive.py host frames cover the phone, so automated phone coverage is unavailable. Four first-tap welcome skips are intentional because Reveal, Back, Next and Again speak their own current line. Quick Next cancels Whoosh when advancing, as the spec requires. Repeats, keyboard/focus checks, Motion off and resize stress are clean. The automatic mode finder sees zero modes in the separate navigation bar; authored states cover all three, with explicit main-path and Backstage repeat tests.
All 78 audit frames were inspected on labeled sheets, with the crowded compact face opened full size. The pose was repaired afterward and only the three affected compact sizes were re-shot, plus phone fallback frames. Nine post-audit frames verify both head extremes at 1000x625, 800x500 and 680x425, plus the three phone modes. No tool exception or console warning was observed; the temporary host alone requested a missing favicon. No second audit or full review was run.

## Left open

The spec-level sweep blocker and unavailable recorded narrator are explicit above. No shared kit/script changes, commits or external publication. All work remains in the named tool and Scratch folders; the standalone phone host was removed. Owned ports 9960, 9961, 9963 and host 8765 are closed; no host.html remains.
Initial read/setup shell calls used tool wait thresholds rather than process timeouts; subsequent commands used explicit process limits. No command, including the audit, timed out.
