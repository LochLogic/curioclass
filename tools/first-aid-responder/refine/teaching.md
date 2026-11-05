# Teaching lens: first-aid-responder (round 1)

Counts: blockers 1, should fix 7, polish 5, nit 3

Read: spec.md, src.html, notes.md, tool.draft.json, voice/lines.json, the module row (data/modules.csv:
health-pe-9-12-first-aid-and-cpr, NHES.S7 only), BUILD.md wave lessons, the shared audit (audit-r1/audit.md) and its
frames. Own runs (drive.py, port 9731, profile in my scratch folder): scratch `teaching/f1` (CPR and scene checks),
`f2` (pause-pattern round), `f3` (ghost and Timer Off). Fact check against AHA 2025 Adult BLS, AHA/ARC 2024 First Aid,
Red Cross CPR Steps and Learn First Aid, CDC heat and seizure first aid, from the spec's Sources and the guidance as
published; pages were not re-fetched in this run.

## Blocker

**B1. The CPR score rewards stopping.** general (Honest numbers lesson)
- Where: CPR rhythm, `compress()` and `endRound()` in src.html (in-band = the 5-interval median rate, per compression).
- What: a compression counts "on target" whenever the median of the last 5 intervals is 100 to 120, so one long pause
  per 5 intervals never moves the median. A round of 5 compressions at 110, then a 5 s stop, repeated for 2 minutes,
  scores **98.8% in target band**, is spoken as "Round over. 99 percent of your compressions were on target.", and is
  saved as **New best. Ghost best: 98.8%.** The real compression rate in that round is 42.5 a minute (shown above it as
  Average rate, but the headline, the spoken line and the ghost all use the in-band percent). Python, same rule:
  10 on / 4 s off gives 99.3% at 69 a minute; 3 on / 3 s off gives 98.9% at 45 a minute.
- Why it is a blocker: the one habit hands-only CPR training most needs to break is pausing ("Don't stop", "minimize
  pauses", AHA 2025). The tool's own Don't card in Collapse in the gym says "Stop every few compressions to check them"
  is wrong, and then the CPR mode scores that exact habit at 99 percent and makes it the ghost to beat. REFINE: a meter
  that misleads when its assumption does not hold is a blocker.
- How seen: drive.py `f2/cpr-pause-pattern.png` (summary panel), `__tool.state.cpr.summary` = {average 42.5, percent
  98.8, longest 5.0}, vlog key `roundEnd99`.
- Better: score time, not taps. For example "on target" = share of the 2 minutes in which the current rate is 100 to
  120 and no gap is over 2 s (a pause zeroes the needle until compressions resume), or count a compression in band only
  when its own interval is also under 2 s and the median is in band; and let a round with any pause over 10 s never
  become the ghost. The spoken result should name pauses when there were any ("...on target, with 17 pauses").

## Should fix

**S1. Every Don't card gives itself away by its text.** general (No giveaways lesson)
- Where: Scenes, all six decks (the `dont` entries in `scenes`).
- What: on all 12 Don't cards the small body text repeats the bold title word for word ("Take off the soaked cloth and
  start over / Take off the soaked cloth and start over"). Of the 33 real steps, 32 have a short headline in "+"
  shorthand and a longer, different body. A student can skip the thinking and avoid the Don'ts by spotting the doubled
  line. Seen on `audit-r1/state-scene-open-1366x768.png` (wood shop deck: both Don'ts doubled) and
  `state-scene-error-1366x768.png`; tabulated from src.html.
- Better: give each Don't a short headline and a fuller body in the same style as the steps ("Wait before calling /
  Wait a minute to see if they wake up, then call"), and give "Call 911" in Heat at practice a body of its own.

**S2. Three step cards start with a lower-case word.** general
- Where: Deep cut ("send someone to call 911"), Burn ("gently take off rings or anything tight near the burn"),
  Seizure ("start timing the seizure"). These came from splitting the spec's "and 3." joined steps.
- What: the lower-case text shows on the card body (`state-scene-open-1366x768.png`, bottom right card), on the slot
  tooltip, and in the Read line for the focused card (voice/lines.json lines 37, 44, 60).
- Better: capitalize the three texts.

**S3. Deep cut: sending someone to call 911 is marked wrong until gloves are on.** general
- Where: Scene 3 ranks (gloves rank 2, "Send someone to call 911" rank 3).
- What: a student who taps "Send someone to call 911" right after "Make the scene safe" is told "Not yet: they protect
  you both" and loses 5 s. Red Cross life-threatening bleeding puts calling 911 before gloves, and sending a bystander
  to call costs the rescuer nothing. The tool teaches that help waits on gloves.
- Better: make "Send someone to call 911" share rank with gloves (or rank 2 with gloves, pressure rank 3), with a reason
  that says help can be sent the moment you see heavy bleeding.

**S4. Deep cut: the "add cloth on top" wording is an open source conflict, shipped as fact.** general
- Where: Scene 3 step "If blood soaks through, add more cloth on top and keep pressing" and the Don't "Take off the soaked
  cloth and start over / Add more on top instead".
- What: notes.md says twice (Oct 31 and Nov 3 source checks) that the current Red Cross page differs (keep the first
  dressing, one added pad, avoid stacking) and that it "needs a spec-owner decision before release". A fact the build
  itself marks unsettled cannot go to Cory as taught content.
- Better: settle it against the AHA/ARC 2024 First Aid text and the Red Cross page, word the step to match ("Don't
  lift it. If blood soaks through, put one more pad on top and press harder"), and remove the open note.

**S5. Seizure: "Call 911 only if longer than 5 minutes" is taught as the whole rule.** general
- Where: Scene 6 step "Call 911 if the seizure lasts longer than 5 minutes" and the Field guide "When to call 911" card.
- What: CDC also says call 911 when it is the person's first seizure, they have trouble breathing or waking afterward,
  another seizure follows, they are hurt, or it happens in water. In the scene the student does not know whether this
  classmate has a seizure history, so "only after 5 minutes" is the rule a student would carry away. notes.md knows
  ("the specified scene teaches only the duration trigger"). In a school the first move is also to get an adult or the
  nurse, which no step says.
- Better: card text "Call 911 if it lasts over 5 minutes, it's their first seizure, or they're hurt or have trouble
  breathing" (reason: "these are emergencies; if you don't know their history, call"), and the same clause on the
  Field guide card. Consider "Send someone for the nurse" sharing rank 2.

**S6. A perfect run never shows why the Don'ts are wrong.** general
- Where: finish card (`finishScene()`: "Why this order" lists only `state.placed`).
- What: a student who never taps a Don't card finishes without ever seeing "Ice can damage the skin more", "You can push
  the object deeper", "people can't swallow their tongue". The "avoid health risks" half of NHES.S7 is taught only to
  the students who get it wrong. Seen on `audit-r1/state-scene-finish-1366x768.png` (no Don'ts on the card).
- Better: add a short "Never do" block under Why this order with both Don'ts and their reasons, every run.

**S7. Heat at practice teaches the weaker cooling method for exertional heat stroke.** general
- Where: Scene 5 step "Cool them fast with cool, wet cloths or a cool bath".
- What: the scene is exertional heat stroke at football practice. AHA/ARC 2024 First Aid recommends whole-body (neck
  down) cold-water immersion as soon as possible for exertional heat stroke, with other active cooling only when
  immersion is not available. The CDC wording (general heat illness) is correct but not what athletic heat stroke
  calls for, and many schools keep an ice tub at practice for exactly this.
- Better: "Cool them fast: cold-water tub up to the neck if there is one, or cold wet towels and ice", reason "cooling
  in the first minutes is what saves lives". Add the 2024 First Aid guideline to the Sources line for this scene.

## Polish

**P1. Seizure briefing and first step disagree.** general. The briefing says "A student falls to the floor", then a
step is "Ease them to the floor and move hard or sharp things away". Better: "Move hard or sharp things away" as the
card (or a briefing where the student is starting to fall).

**P2. Burn: "Tell the teacher and school nurse" can only come last.** general. In a teaching kitchen the teacher is in
the room; ranking telling an adult after 10 minutes of cooling and dressing reads as "wait to tell an adult". Better:
let "Tell the teacher" share rank 2 with cooling and rings, and keep "a hand burn should be checked by a health care
provider" as the final step.

**P3. Heavy bleeding has no "if pressure doesn't stop it" step.** general. The scene is a forearm wound "bleeding a
lot"; AHA/ARC 2024 and Stop the Bleed (commonly taught in high school) add a tourniquet for life-threatening limb
bleeding that firm pressure does not control. A line in the reason or the Field guide "When to call 911" card ("an
adult trained with a tourniquet can use one on an arm or leg") would close it without a new step.

**P4. notes.md claims more than the tool does.** general. "What it teaches" says students "explain why each step belongs
there"; the tool shows the reasons, and students never explain. Better: "...and read why each step belongs there" or
add a Talk question that asks for it. The rest (Key skills, Support at home) is true of the tool and doable tonight.

**P5. Teacher notes need a content note.** general (rule 8). Collapse, choking and seizures may be hard for a student
who has seen one or lost someone. "Good to know" names the scope (no overdose, no graphic injuries) but not this.
Better: one line: "Some students may have witnessed an emergency or a death; let them choose Field guide or the rhythm
practice instead of a scene." Also note that spec open questions 1 (overdose scene) and 2 (Timer default) are still
open; not a teaching finding, but they belong to the integrator before Cory.

## Nit

- **N1.** Rate readout label "RATE / MIN · 5-INTERVAL MEDIAN" is jargon for grade 9. "RATE / MIN (last 5 presses)".
- **N2.** Field guide and the CPR note say "at least 2 inches"; AHA's adult range is 2 to 2.4 inches. Fine for
  hands-only messaging; optional "about 2 inches, not more than 2.4".
- **N3.** The "Not yet" line for a shared-rank step reads "Not yet: heavy bleeding needs pressure now and help on the way
  (either order). +5 s." The "(either order)" is the slot's label, not a reason; drop it from the reason text.

## Checks that passed

- Standards: NHES.S7 is the only code. It is taught by what a solo student does: choosing safe actions in order,
  getting each unsafe Don't corrected with a reason, and holding a rate (once B1 and S6 are fixed, both halves of
  "practice health-enhancing behaviors and avoid or reduce health risks" are taught). No move needed.
- Facts that match the sources: Collapse order (scene safe, shout-tap and breathing check of at most 10 s, gasping not
  normal, call 911 on speaker and get the AED, compressions 100 to 120 in the center of the chest, AED as soon as it
  arrives, keep going) matches Red Cross CPR Steps and AHA 2025 lay-rescuer sequence. Choking: consent question, have
  someone call, 5 back blows then 5 abdominal thrusts above the navel, repeat, CPR if unresponsive, no blind sweeps
  (AHA 2025 order). Burn: cool running water at least 10 minutes (inside the 2024 range), rings off, loose clean
  dressing, no ice, no popping, hand burns get care. Heat: signs, call 911, move, cool, no drink, never alone (CDC).
  Seizure: stay, time it, clear area, soft under head, on one side, never hold down, nothing in the mouth (CDC).
  Field guide Hands-only CPR card is accurate, including breaths for infants and young children. No red cross emblem.
- Gauge geometry: band arc endpoints (116.74, 26.85) and (203.26, 26.85) recomputed for 100 and 120 on the 60 to 160
  semicircle: correct.

## Done when (spec)

1. Pass. Slots 6, 5, 6, 5, 5, 6; decks 8, 7, 8, 7, 7, 8 (steps plus 2 Don'ts); "either order" on scenes 3, 4, 6 (f1).
2. Pass. Shared-rank steps placed in either order; an out-of-order tap gave "Not yet: ... +5 s"; a Don't went to Never
   with ✗, reason and +5 s; mistakes 2 (f1).
3. Pass. A timed run saved a best and the reopened scene showed the ghost; a Timer Off run and a run with Timer turned
   off mid-way both said "Untimed run. Nothing recorded." (f3). Clear by code (confirm-clear empties `far-best`).
4. Pass as written: steady 110 with up to 30 ms jitter, needle 102.8 to 115.4, 99.5% in band (first tap has no rate);
   90 reads coachFast; a 3 s gap counts one pause, longest 3.5 s (f1). But see B1: the check does not cover a student
   who pauses often, and that case fails.
5. Pass for scheduling: 220 clicks over 120 s, 545.5 ms apart (`testMetro`). Sound Off stops it by code
   (`Curio.onSound`); not heard in a muted Chrome.
6. Pass by code and the audit's held click on #chest ("ok"); `e.repeat` keys are ignored.
7, 9, 10, 11. Play and Craft own these; the audit frames show the rail and deck central at 1366x768 and the footer on
   all three modes. Not re-tested here.
8. Not re-tested here (Play and Craft); the audit's quick-tap rows are clean.

## Audit pilot

- Confirmed: the #chest / pad-label overlap at 680x425, 800x500 and 1000x625. On `state-mode-cpr-rhythm-800x500.png`
  "CENTER OF CHEST · PRESS SPACE" sits on the bottom edge of the chest pad; readable, cosmetic (Play/Craft).
- Wrong or benign: "welcome not heard" after a first tap on a scene card and on Clear best times. The scene card plays
  its briefing and the "order" how line instead, and the picker welcome ("Tap a scene card") no longer fits once a
  scene is open (`welcome()` returns null with a scene open). Not a teaching gap.
- Not checked by me: the 375x812 below-the-fold rows for Timer and Clear best times (Play/Craft).
- Missed (outside what it can see): the pause-pattern score (B1), the doubled-text Don't giveaway (S1), lower-case card
  text (S2), and every fact and order finding (S3 to S7, P1 to P3).
