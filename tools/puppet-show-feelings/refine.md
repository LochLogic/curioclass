OPEN (round 1, Claude Refine 2026-11-05; Codex fixes next)
Counts: blockers 2 (general 2, family 0), should fix 8 (general 8, family 0), polish accepted 10

# Refine: puppet-show-feelings

Lenses: refine/teaching.md, refine/play.md, refine/craft.md (no sensitivity review needed: nothing cultural, Native or
hard-history). Frames: audit = S:/CurioClass-codex-scratch/puppet-show-feelings/audit-r1/, play = .../play/,
craft = .../craft/. Spot-checked by the integrator: items 1, 2, 3 and 4 (src.html lines read; audit frames
state-like-feeling-1366x768.png and state-ending-0-1366x768.png opened).

## Blocker
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

## Should fix
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

## Polish accepted
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

## Settled calls
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

## To the spec's open questions
- Spec text drift to settle after this round: Line cycles five lines, not six (Blocker 2); the after-change line,
  praise, audience, Like me and vote-why lines change (Should fix 1, 5, 6, 8); art came from gpt-image, not the local
  FLUX route the spec names (craft nit 11). Update the spec's Voice and Art sections so later agents do not "fix" them
  back.

## Not taken
- "all by herself" to "all on Pom's own" (teaching nit 8): reads clunkier; one pronoun is harmless.
- Spec-drift note in notes.md (craft nit 11): sent to the spec's open questions instead.
