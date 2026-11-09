# Teaching lens: moon-base-drama (round 1)

Cold read of spec.md, src.html, notes.md, voice/lines.json, audit-states.json and the shared audit
(S:/CurioClass-codex-scratch/moon-base-drama/audit-r1). My own frames and logs are in
S:/CurioClass-codex-scratch/moon-base-drama/teaching/out (driven with scripts/drive.py, held clicks, port 9887).
Standard text was checked against the NCAS theatre performance standards (New York's adopted set, K, 1 and 2).

## Findings

### 1. Rewinding twice skips choices, and the meter then contradicts the story map (blocker, general)
- Where: src.html:585-595 (rewind buttons), :651 (`button.disabled = n > state.visited`), :709-725 (`goBeat` with
  `rewound`).
- What: after a full run, Rewind to Batteries moves every choice to `oldChoices`, but `state.visited` stays at 8, so
  Water and Warmth stay enabled in the map. Rewind again to Warmth jumps straight to beat 6 with no Batteries or Water
  choice made. The story map still shows the sun-battery and ice icons on those nodes, not faded (they are before the
  current beat), so the class sees "we chose batteries and ice", while the meter reads Light 1, Water 1. Choosing the
  blanket and going on gives "The long night is here, and the plants are droopy" on a path whose map shows all three
  good choices. The tool tells K-2 children their right science choices failed. A meter that misleads is a blocker
  (REFINE, Rounds). Done when 3 also fails: the rewind does not restore a consistent story.
- How seen: drive shots rw-b-skip (after Rewind to Batteries: `dis:[false,false,false]`, old `{3:0,4:0,6:0}`),
  rw-c-jump6 (beat 6, meter 1,1,1, Batteries and Water nodes carry old icons, not `future`), rw-d-jump6-end
  (meter 1,1,3, `endLow`), frame out/rw-d-jump6-end.png.
- Better: a rewind sets `visited` back to the rewound beat (only reached choices can be rewound to), or the skipped
  nodes show as faded old story and the map buttons after the current choice stay disabled until reached again.

### 2. A child alone never hears the question the science choice answers (should fix, general; may be a spec question)
- Where: spec "Ada's card, not spoken", Done when 4; src.html:396, :401, :408 (`ada:` lines), the welcome
  "Teacher, you are Commander Ada."
- What: the choice questions ("How do we keep the plant lamps on all night?", "Where can we get water?", "How do we
  keep the plants warm?") live only on Ada's card, which is never spoken, and the choice labels are not spoken
  either. With a teacher this is the design and it works. A pre-reader alone at home (BASELINE rule 4) hears a fact
  and then sees two buttons with no question, so TH:Cn11 (apply the moon fact to a choice) does not happen. The K-2
  teacher-led guardrail softens this, so the merge may route it to the spec's open questions. A small fix inside the
  spec: Read on a choice beat could speak the choice labels ("Fill the batteries now, or wait until dark?") as
  Mission Control asking the crew, keeping Ada's card unspoken.
- How seen: src.html read; voice log v-slow shows only Mission Control lines at beats 3 and 4.

### 3. TH:Cr3 at grade 2 is thin: the crew never adapts dialogue (polish, general)
- Where: the choice beats (spec "Mission", notes "Say the crew's line before tapping its choice").
- What: NCAS TH:Cr3.1.2a is "Contribute to the adaptation of dialogue"; grade 1 is adaptation of the plot. Rewind
  teaches plot revision well (K: answering Ada's questions also covers Cr3.1.K a). For grade 2 the crew only picks
  between two fixed lines. Better: on a rewind, Ada's card adds "Say it your own way" (for example "Rewinding to the
  batteries" card: "Say the new line in your own words. What will you tell me?"), so the class rewrites the line, not
  only switches buttons. Cheap and inside the spec.
- How seen: standard text vs. src.html:395-410.

### 4. TH:Re9 is described by its effect, not by what the code asks (polish, general)
- Where: spec "Who and how", notes "Good to know" ("TH:Re9 (explain its effect)").
- What: TH:Re9 K-2 is evaluate dramatic play, select or use props, and discuss or describe how characters respond to
  challenges. The tool does all three (job props, the ending question, the crew meeting each moon problem), but the
  notes don't say so, so a teacher can't see the match. Better: notes name the real asks: "choose a prop for your
  job (Re9 b), say how the crew met each moon problem and which choice mattered most (Re9 a, c)". Talk about it
  could add "How did the crew act when the doors opened?" for Re9 c.
- How seen: NCAS text vs. notes.md.

### 5. The Warmth wrong choice doesn't answer the warmth question (polish, general)
- Where: src.html:407-410, beat 6.
- What: Ada asks "How do we keep the plants warm?" and option B is "Open the doors for air", which answers a
  different question, so it reads as a joke rather than a misconception the fact corrects. Option A, "Wrap it in a
  blanket", has no antecedent for "it" (Ada said "the plants"). Better: A "Wrap the greenhouse in a blanket"; B a
  warmth idea the two facts on that radio line refute, for example "Open the doors to let warm air in" (result:
  outside is colder than a freezer and has no air).
- How seen: src.html; frames state-water-result, my v-five log.

### 6. The ending picture barely shows what the meter says (polish, general)
- Where: src.html:113-115, :657-663 (night, lamps, leaf droop).
- What: Re9 hinges on "which choice made the biggest difference", but the full and droopy endings look nearly the
  same: the painted greenhouse plants behind stay lush and lit, and only the small foreground tray is squashed
  (scaleY .55), which reads as shorter, not wilted. Light 1 still shows a big lit lamp, and droop ignores Light, so
  "no batteries" ends with upright plants. Better: droop and dim also follow Light, and the background plants darken
  more when a meter is low, so children can point at what changed.
- How seen: audit frame state-night-1366x768.png (all full) beside my out/rw-d-jump6-end.png (1,1,3, droopy); path
  walk `100 ... lamps=1 droopy=false`.

### 7. The full-success ending opens with an instruction (nit, general)
- Where: src.html:458, guided `reflect_endFull`.
- What: the first ending heard says "Tell Ada which choice helped. Tap Rewind." before "Great work, crew!", so the
  payoff lands after a how-to. Put the how-to after the ending line, or let the hint carry it.
- How seen: audit frame state-night-1366x768.png caption; voice log v-five last line.

## Checks that passed
- Done when 2: all 8 paths (path walk in the tool, `paths` shot): meter 1,1,1 at beat 2; A gives +2, B gives 0, 1, 0;
  AAA ends full, any single B ends two full, two or three B end low. Every ending is reachable and matches the meter.
  Recomputed by hand: matches the spec's check.
- Done when 3 (single rewind): Rewind to Water from the end restores Light 3, Water 1, Warm 1 and fades later nodes
  (rw-e). Fails only in the double-rewind case above.
- Done when 4, 5, 7: voice logs v-slow, v-fast, v-five: no Ada line is ever spoken; each Mission Control line plays
  when its beat opens; Radio again replays the result; fast taps cut lines with no stale line after; how-to lines once.
- Done when 1, 6, 8, 9: audit rows clean at every size and state; Next is disabled on an open choice beat and the
  choose line does not name it (state-batteries-680x425.png).
- Facts, spot-checked against a second source: lunar night near the equator -208 F (-133 C) (NASA Weather on the
  Moon), so "colder than a home freezer" holds; gravity one sixth (NASA Moon Facts); exosphere, not breathable air
  (NASA Moon Facts); ice in permanently shadowed polar regions (NASA Moon Facts); 29.5 / 2 = 14.75 days ("about two
  weeks"); 1.62 / 9.81 = 0.165 ("about one sixth"). Water B line ("found ice late, tank still low") matches Water +1.
- Notes: What it teaches, Key skills and Support at home are true of this tool, and the home ideas are doable tonight.
  No sensitive topics, no hard history, nothing cultural or Native: no sensitivity review needed.
- Guardrails: teacher-led K-2, no score; the check on a job badge is stated as not a score.

## Audit pilot
- Leads confirmed: none of its 16 voice leads bear on teaching (the "welcome not heard" after a first badge tap is by
  design: the badge line carries the premise; Craft owns it).
- Leads wrong: none checked.
- What it missed: the double-rewind skip (finding 1). Its rewind-open state opens the map once from beat 3 and never
  rewinds twice, so a contradiction between map and meter could not show. The weak ending contrast (finding 6) is a
  "what one look means" item it can't judge.
