# Teaching lens: flipbook-studio (round 1)

Cold read of spec.md, src.html, notes.md, art/prompts.json, voice/lines.json, audit-states.json and the shared audit
(`S:/CurioClass-codex-scratch/flipbook-studio/audit-r1`). Checks ran through `scripts/drive.py` (port 9831), shots and
frames in `S:/CurioClass-codex-scratch/flipbook-studio/teaching/` (`shots.json`, `frames/`). No console errors in any
shot. Not a Curiosity: judged as a lesson tool.

## Findings

### 1. On ones and on twos are taught at film's 24 per second, but the tool runs at 12 by default
- Where: src.html:457-460 (Why notes), preset `twos` (src.html:1144), notes.md "A 5-minute start".
- What: the Why card says twos "still look smooth for most motion" and ties twos to 24 per second. Every starter
  plays at 12 per second, so On twos here gives 6 new drawings a second: the Real bounce just plays in slow motion,
  choppy (frame t9: "12 drawings, 24 frames, 2.0 seconds at 12 per second"). A student who presses On twos sees the
  opposite of what the card says, and the 5-minute start then asks "what feels heavier now?" about a change that only
  halves the speed. At this tool's 12 per second, its "ones" already equal film's twos. The only screen hedge is
  "This book's frame rate can be different"; notes.md says it plainly ("at this tool's default 12 fps it produces 6
  drawings per second"), but the student never sees that.
- Better: say it where the student acts. For example, the Why note: "At 12 per second, this book on ones already looks
  like film on twos. To see film's twos, tap 24, then On twos." and a hint after On twos at 12 or less naming the
  drawings per second. If the integrator prefers, starting the bounce starters at 24 per second on twos would make
  the vocabulary true by default, but that changes the spec's Content (open question, not builder work).
- How seen: frame `teaching/frames/t9-twos-12.png`; Why text in `audit-r1/state-timing-help-1366x768.png`; preset
  readouts recomputed below.
- Level: should fix. Tag: general (a named technique taught under a different rate than the one on screen).

### 2. MA:Cr2.1.6-8 is only lightly taught: nothing asks the student to plan or propose
- Where: spec "Who and how" glosses Cr2.1 as "develop, refine and model"; the standard's text is "Organize (gr 6) /
  Design (gr 7-8), propose, and evaluate artistic ideas, plans, prototypes, and production processes for media arts
  productions, considering expressive intent". notes.md "Sources and standards".
- What: the tool has organizing (reorder pages, Copy page) and evaluating (compare Real and Even bounce), but no step
  where the student plans a motion before drawing it. Animation's own planning process, keys then in-betweens, is
  absent: "Hold the key" (src.html:341) uses the word key without the tool ever saying what a key drawing is.
- Better: one real planning activity, not a thin one. For example a Try this card, with a matching line in notes,
  "Plan a jump: draw the start, the top and the landing first (your keys), then add the drawings in between with onion
  skin, closer together near the top." and one Why sentence defining a key drawing (Williams, Survival Kit, "Keys,
  extremes and breakdowns"). Then "Hold the key" means something. If the integrator judges that out of scope, move
  Cr2.1 to the tool that plans (storyboard-studio is 9-12, so it needs a 6-8 home) per BASELINE rule 2.
- How seen: code read of every control and card; standard text from the NCAS-based grade 6-8 listing.
- Level: should fix. Tag: general.

### 3. The bowling ball card asks for a move the hold controls cannot make
- Where: src.html:466, "fewer frames at the top, longer hold on the floor".
- What: every Real bounce hold starts at 1, the minimum, so "fewer frames at the top" cannot be done with the hold
  handles the card sits beside. A solo student tries minus on a top drawing, gets "This hold is already 1 frame", and
  is stuck. The only way is Delete page in Draw, which the card does not name.
- Better: "Make the Real bounce feel like a bowling ball: hold the floor drawings longer, then delete one top drawing
  in Draw so it hangs less in the air." (or start the card from On twos so tops can drop to 1).
- How seen: tried it (changeHold to 0 on a hold-1 drawing returns the "already 1 frame" hint, src.html:1119-1124).
- Level: should fix. Tag: family:flipbook (hold-only editing).

### 4. Intent prompts are hidden behind Why / Try this; a solo student never meets one
- Where: starter lines and hints (src.html:1028, voice `starterBlink`), Try this cards inside the Why dialog; at
  heights under 650 px the Why button moves into the Timing dialog (secondary rows).
- What: Cr3.1 is "refine for intent". The Blink starter's line says "drag the hold handles and press Play" with no
  intent to aim for, though its card says "calm or startled?". The bounce line does set a compare task (good). A
  student at home reaches an intent only if they open Why / Try this.
- Better: give the Blink starter a goal in its hint, e.g. "Here is a calm blink. Tap Time, drag the first hold down
  to 2 and press Play: now it is nervous." and show one Try this card under the presets in Time at sizes where it fits.
- How seen: `teaching/frames/t7-blink-time.png`, hint text returned by the shot.
- Level: polish. Tag: general.

### 5. Spacing chart on the Blink shows one red dot on the nose
- Where: drawChart (src.html:650), Blink starter in Time.
- What: the four blink drawings share one bounding-box center, so the chart draws a single dot with four crowded
  numbers between the eyes. It is accurate (the face does not travel) but reads as a stray mark, and the real lesson
  (a blink is all timing, no travel) is not said.
- Better: when every dot coincides, draw one dot and a caption line such as "These drawings do not travel: the change
  is in shape, so timing does all the work."
- How seen: `teaching/frames/t7-blink-time.png`; centers recomputed: all four [480, 350].
- Level: polish. Tag: family:flipbook.

### 6. Ease the ends on a looping bounce slows only one of its two tops
- Where: preset `ease` (src.html:1145), spec Content.
- What: holds become 3,2,1,...,1,2,3 by position in the book. Real bounce has tops at drawings 1 and 7; drawing 1 gets
  3 frames, drawing 7 gets 1, so the two bounces get different hang times. A student may take this as what slow in and
  slow out means for a bounce.
- Better: the hint after the preset says what it did: "Ease the ends slowed the first and last drawings of the book.
  For a bounce, hold each top drawing longer by hand." (no spec change).
- How seen: readout "12 drawings, 18 frames, 1.5 seconds" with holds 3,2,1,1,1,1,1,1,1,1,2,3 (shot t1).
- Level: polish. Tag: family:flipbook.

### 7. Teacher notes say "the spec"
- Where: notes.md "Good to know": "The Blink starter retains the spec's explicit 8-frame first hold until edited".
- What: internal build jargon in teacher-facing notes; a teacher does not know what "the spec" is.
- Better: "The Blink starter opens with an 8-frame hold on its first drawing (a calm blink). Editing it switches to the
  1 to 6 frame range."
- Level: polish. Tag: general.

### 8. Support at home: the rolled ball does not start slow
- Where: notes.md "Support at home", third idea.
- What: a gently rolled ball leaves the hand at its fastest and slows down; "starts slow, moves quickly and stops" is
  not what a family will see, and it does not match either starter.
- Better: "Drop a ball and let it bounce. Watch where it seems to hang at the top and where it rushes at the floor,
  then compare with Real bounce." (matches the tool and can be done tonight).
- Level: polish. Tag: general.

### 9. "twos are half the drawing"
- Where: src.html:459.
- What: should be "half the drawings" (spec has the same slip).
- Level: nit. Tag: general.

## Done when (tested)

| # | Result | How |
|---|---|---|
| 1 | pass (code) | eraser filters whole strokes by isPointInStroke; remember() before each stroke and erase, per page, 50 steps. Touch not driven here (Play/Craft) |
| 2 | pass (code) | onion only when mode is draw and not playing (src.html:723); print builds from strokes only |
| 3 | pass | shot t1: "12 drawings, 12 frames, 1.0 seconds"; twos "24 frames, 2.0 seconds"; Blink "4 drawings, 11 frames, 0.9 seconds" (11/12 = 0.917) |
| 4 | pass | centers recomputed: Real (150,204) (220,380) (290,632 squashed, bottom 660, width 104 = 1.3 x 80) (360,380); Even (150,300) (220,460) (290,620) (360,460). Chart bunched vs even: `audit-r1/state-bounce-time-1366x768.png`, `teaching/frames/t8-even-time.png` |
| 5 | pass | strokes identical after two hold changes, a preset and 24 fps (t1); 24 fps, 10 loops of 0.5 s: loop starts 510 to 5010 ms, at most 1 ms off ideal (t2) |
| 6 | pass (audit) | audit clean rows for every size and mode; keep-region leads only inside modal dialogs |
| 7 | pass | hold set to 6 on the drawing on screen while looping: next drawing came 517 ms later (500 expected) (t3); stop cancels the frame loop at once |
| 8 | pass | Real bounce on twos prints 24 numbered cards on 3 sheets; dashed cut borders, STAPLE margin, plain white, no paper texture |
| 9 | pass | Blink with hold edit survived a fresh tab (t5, t6: holds 8,3,1,1); setItem throwing shows the footer warning with the exact line (t4) |
| 10 | pass (audit) | page, strip and Play in view at every size |
| 11 | left to Craft | voice counts are the Craft lens's check |

Numbers recomputed: Ease the ends 3+2+8x1+2+3 = 18 frames, 1.5 s; 48 drawings held 6 = 288 frames = 48.0 s at 6,
12.0 s at 24, 36 sheets; Blink opener 8 + 47 x 6 = 290 frames, 37 sheets (notes.md matches). |cos| bounce vs a true
parabola: 204 vs 193.3, 380 vs 353.3 (within 27, as the spec says).

## Other checks
- Giveaways: no predict, quiz or hidden-information mode; nothing to give away.
- Facts: 24 frames per second as a common film rate, ones and twos, slow in and slow out, timing and spacing match the
  spec's Sources (Williams 2001; Thomas and Johnston 1981, ch. 3). Both Animation Mentor links in notes.md exist (the
  site refuses automated fetches; found by search).
- Guardrails: grade 6-8, students drive; no hard history, health or cultural content. Nothing for the sensitivity
  agent. Rule 8: the media arts standards here cover no sensitive topic.
- Language: plain and right for grade 6-8, apart from items 7 and 9.

## Audit pilot
- Leads wrong: "count and word disagree: 1 seconds" at every size is the substring of "0.1 seconds" (1 frame / 12 =
  0.083, shown as 0.1). Not a bug. The starter-library and timing-help keep-region leads come from modal dialogs the
  states open on purpose (their `keep` is [] yet the audit still checked the global list).
- Leads confirmed: the film strip scrolls sideways in bounce-time, delete-pauses-book and page-limit; that is the
  spec's own design (one row that scrolls), not a teaching problem.
- Missed (outside its reach): items 1 to 9 above, chiefly the ones/twos rate mismatch and the untaught planning
  standard.
