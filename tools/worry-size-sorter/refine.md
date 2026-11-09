OPEN (round 1, Claude Refine 2026-11-06; Codex fixes next)
Counts: blockers 1 (general 1, family 0), should fix 12 (general 12, family 0), polish accepted 18
Traced to spec: blockers 1, should fix 8

# Refine: worry-size-sorter

Lenses: refine/teaching.md, refine/play.md, refine/craft.md, refine/sensitivity.md (fresh agent; grades 3 to 5).
Shared audit: S:/CurioClass-codex-scratch/worry-size-sorter/audit-r1/. Integrator spot-checks: viewed
art/ws-card-door.webp at full size (bedroom at night, bed, lamp, stuffed bunny, light under the door: confirmed);
read src.html:574-583 (Big slide animation has no fill, card returns), 1027-1031 (because() uses any meter result),
1228-1250 (digits 1 to 4 switch mode from anywhere except SELECT and a held Sort card: confirmed).
"(spec)" = the cause is in spec.md; "(build)" = the spec was right and the build missed it.

## Blocker
1. **Card b1 picture shows a child's bedroom at night.** art/ws-card-door.webp, Sort card b1 "A grown-up asked me to
   keep a secret, and it feels wrong." The picture is a child's bedroom (bed, quilt, stuffed bunny, lamp on) with the
   bedroom door closed and hallway light under it. Paired with a grown-up's secret that feels wrong, it is the classic
   scene of night-time abuse in the child's own room: a trigger for a child living it, met alone at home, and a
   frightening specific scene for every other child; it also narrows the secret to home. Seen: sensitivity full-size
   view and its big-b1 frame; integrator viewed the webp. Fixed: redraw with no bedroom, no bed, no night, no people,
   for example a small wrapped box or a closed notebook with a blank "shh" sticker on a school cubby or hallway bench in
   daylight. Update the ws-card-door entry in spec art list and art/prompts.json to match (keep the token name or
   rename it consistently). No person, so no contact sheet entry. (general) (spec: the spec prompt asked for "a closed
   wooden bedroom door with a soft hallway light underneath")

## Should fix
1. **The goal's "Because" can argue against the goal.** src.html:1027-1031 because(), My week builder (1096-1102).
   Any meter result is used, so a rising meter gives "I will do Squeeze ... Because my meter went from 2 to 4 when I
   tried it", and the clue choices are hidden so the student cannot pick a better reason; "from 3 to 3" too. NHES 6.5.1
   asks how the goal supports well-being. Seen: teaching t2-week-because-up.png, t2b-week-goal-up.png; play
   because-up.png. Fixed: use the meter line only when after < before; calm 1 to 1 reads "Because I practiced it when
   I was calm."; otherwise show the clue choices (Should fix 2). (general) (spec: spec.md My week says "if the chosen
   tool has a meter result this load, the line is built from it" with no direction rule)
2. **"Pick the body clue this tool helps" accepts wrong pairings and leaves out tummy.** src.html:325, 1096-1102.
   Every clue is offered for every tool, so "Box breathing ... Because it can help with busy thoughts" is accepted while
   Body clues teaches busy thoughts go with Worry box and Talk back; the label reads as a fact question. Four clues
   here, five in Body clues (no tummy). Seen: teaching t3-week-because-mismatch.png; play cites
   audit-r1/state-week-chart-1366x768.png. Fixed: offer only the clues whose Body clues "Try" line names the chosen
   tool (from the clue data), label "Pick the body clue it helps (from Body clues)", and add tummy / butterflies with
   the tools Body clues names for it. If a tool has one clue only, preselect it. (general) (spec: the spec's four-clue
   list and "the body clue it helps" with no tie to the Body clues data)
3. **Box breathing teaches two rounds; the sources say three to four.** src.html:769 ("Two rounds, then check your
   meter."), 898. Cleveland Clinic and WebMD, and the spec's own Sources row, give 3 to 4 rounds. Seen: teaching read
   code and fetched page; audit-r1/state-breathing-stopped-1366x768.png. Fixed: default 3 rounds ("Three rounds, then
   check your meter."; 48 s at count 4, 36 s at count 3), One more round still up to 4; update voice line and Read text
   that says two. (general) (spec: spec Box breathing says "Two rounds play" against its own Sources row)
4. **Number keys pull a keyboard student out of a running tool.** src.html:1247-1250. Digits 1 to 4 switch mode
   from anywhere; the meter is drawn 1 to 5, so pressing 4 for "A lot" opens My week, 1 jumps to Sort and stops a
   breathing run. Seen: play meter-key4.png (focus on meter2, mode became week); craft digit-in-meter (mode sort,
   running false). Fixed: while focus is inside the stage or panel, digits do not switch mode; on the meter (Tools
   step 1 and step 3) 1 to 5 rate the step. Header buttons keep keys 1 to 4. (general) (spec: spec gives "keys 1 to
   4" globally and a 1 to 5 meter with no rule for focus inside a tool)
5. **A Big card dropped in Small or Medium snaps back to the stack.** src.html:576-583. The 0.6 s slide has no fill,
   so the card returns to the top at full size with "Sorted. Look at the help beside it."; only a 23 px thumbnail lands
   in Big. The one moment the tool exists to show is undone on screen. Seen: play big-drop-after.png (1.2 s after),
   big-drop-mid.png; integrator read the code. Fixed: the card ends in Big (shrinks into the Big basket and stays
   hidden from the stack), and the stack shows an empty slot or the next card back until Next worry; Motion off jumps
   there. Same settle for Small and Medium drops (Polish 6). (general) (build: spec says it "slides into Big")
6. **Saving My helpers gives no privacy line where it saves.** src.html:848-852, 1006-1008. "This one helps me"
   writes wss-week to localStorage, but the line about storage only shows in My week. BASELINE rule 7 (privacy stated
   where anything is stored). Seen: craft helps-privacy.png and its storage dump. Fixed: one small line under the step
   3 result buttons, "Saved on this device only." (plus "This browser won't save it." when storage is blocked).
   (general) (spec: spec puts the privacy line only in My week though Tools saves helpers)
7. **Read speaks hint strings that are not in the voice lines.** src.html:389-401. About 16 hints ("Tap a numbered
   ring to open a body clue.", "Tap Try a tool on it, or tap Next worry.", the My week builder hints and others) are
   not in voice/lines.json, so with recorded clips Read switches to the browser voice partway. STANDARDS "Bands".
   Seen: craft read logs. Fixed: put every hint string in L (and lines.json) and have Read speak keyed lines; regenerate
   lines.json so allLines() and the file match. (general) (build)
8. **Body clue rings sit on the face and off the body parts.** src.html:94-95, 232-233. Ring 1 (Head) covers the kid's
   nose and mouth at every size; ring 4 (Tummy) sits at the hem and waistband; at 680x425 ring 5 floats off the body
   with its leader at the thigh; ring 2 (Chest, fast heart) is on the viewer's left, the heart is on the viewer's right.
   Seen: audit-r1/state-body-clue-1366x768.png, state-body-clue-680x425.png (craft, play, sensitivity). Fixed: Head ring
   at the side of the hair or forehead edge, Tummy on the hoodie pocket, ring 5 led to the hand, and swap rings 2 and 3
   so the heart clue sits on the viewer's right; check 1366x768, 680x425 and 375 wide. (general) (build)
9. **Card b3 promises "You won't be in trouble for telling."** worry-data.json b3 reason and its voice line. The tool
   cannot keep that promise, and it misses the core message that it is not the child's fault. Seen: sensitivity
   big-b3-short frame. Fixed: "Tell a trusted adult right away, even if you already sent something. It's not your
   fault. The person who asked did something wrong." Update lines.json and the spec Content row. (general) (spec: the
   spec wrote this reason)
10. **Card b1's reason does not say the grown-up may be one you know or love.** worry-data.json b1. Fixed: keep the
    reason and add "That's true even if it's a grown-up you know, or one in your family." Update lines.json. Seen:
    sensitivity big-b1 frame. (general) (spec: the spec wrote this reason)
11. **Green chroma-key fringe in the kid's hair.** art/ws-kid-stand, ws-kid-fists, ws-kid-shoulders, ws-kid-loose
    (ws-kid-toes is clean). A green halo on the curls, visible on the Body clues stage at 560 px; on the only child in
    the tool, on textured hair, it reads as careless. Seen: sensitivity zoomed crop and five-pose contact sheet. Fixed:
    re-despill or hand-clean the hair edge on the four poses. If any pose is redrawn rather than edge-cleaned, it goes
    on Cory's contact sheet. (general) (build)
12. **Teacher notes have no route for online exploitation.** notes.md "Sensitive content and disclosures". Card b3 is
    an online photo request; notes give no US route beyond school procedure. Fixed: add one adult-facing line: "For an
    online photo request or a shared image of a child, report to NCMEC's CyberTipline (report.cybertip.org,
    1-800-843-5678) as well as through your school; Take It Down (takeitdown.ncmec.org) helps remove images." Not on
    screen (keeps the no-hotline-on-screen call). (general) (spec: the spec's Disclosure paragraph sets the notes
    content and leaves this out)

## Polish accepted
1. **Tools step 1 note.** Replace "Picture it's really happening." with "Think about this worry for a moment." for
   every card (sensitivity 6: an imaginal-exposure prompt on m3, home arguing, alone). When Box breathing or Squeeze is
   opened from the header with no card, hide the bare worry line and the note; ask only "How worried does your body feel
   right now?" (teaching 4, t1b-tools-header.png). (general)
2. **Body clues "Try:" names become buttons** that open Tools on that tile (teaching 5). (general)
3. **Medium result names the "talk it over" half.** For a Medium-sized card add "Who could you talk this over with?"
   (one line, no new chips) (teaching 6, t4-sort-medium-into-small.png). (general)
4. **b5 reason says what help is.** "...is a sign to get help. Tell a grown-up you trust; a school counselor or doctor
   can help with worry." Update lines.json (teaching 7). (general)
5. **Reflection: "I forgot" leads somewhere.** Add **Change who helps me remember** to Next week I will; when "I
   forgot" is picked, mark it as suggested (teaching 8, audit-r1/state-reflection-1366x768.png). (general)
6. **Small and Medium drops settle into the basket** instead of the card staying on the stack (play 2,
   audit-r1/state-sorted-card-1366x768.png, play small-drag.png). Do it with Should fix 5. (general)
7. **Softer sizing line.** Small card in Medium: "Many kids put this in Small. Medium is fine too." (and the mirror
   for Medium in Small) in place of "One way to size it: Small." (play 5, small-in-medium.png). (general)
8. **Worry box fold reads as folding**: a two-step fold (halves, then quarters) lined up over the slot it drops into
   (play 8, box-folded.png). Motion off jumps to folded. (general)
9. **Tool tile icons in one style**: four small inline SVG icons in the brand color, not two text glyphs and two color
   emoji (craft 5; spec says tile icons are drawn in code). Make Box breathing and Worry box clearly different. (general)
10. **Read in the Big panel**: join the adult chips as one sentence ("A parent or caregiver, a grandparent, a teacher,
    a school counselor, a coach or a doctor.") and drop the second "Tell one grown-up you trust" (craft 6). (general)
11. **b4 and b2 reasons add "not your fault".** b4 add "It's not your fault." b2 add "It's not your fault, and it's not
    your job to fix it." Update lines.json (sensitivity 7). (general)
12. **Notes for home and the disclosure steps** (sensitivity 9): add the home line (listen calmly, thank your child,
    contact the school counselor or doctor; for abuse, Childhelp National Child Abuse Hotline 1-800-422-4453), and add to
    the teacher steps "listen, don't question for details or investigate, write down the child's own words, tell them
    who you will tell next." Adult-facing only. (general)
13. **meterOther and the a > b result say "talk to a grown-up you trust"** in place of "talk to someone" (sensitivity
    10). Update lines.json. (general)
14. (nit) **End panel count**: "In Big: N. The 5 Big worries always go to a trusted adult." (teaching 9,
    t5-sort-end-allbig.png). (general)
15. (nit) **notes.md sources**: list the same sources as spec and tool.draft.json (add WebMD, Michigan Medicine,
    eSafety, Advocates for Youth, US Attorney tip sheet; add NHS Every Mind Matters to tool.draft.json), one YoungMinds
    URL, cite YoungMinds for the no-bedtime timing, and drop "browser voice fallback in this Build-only version"
    (teaching 10). (general)
16. (nit) **Big panel wait**: while the button reads "Listening...", the hint does not name Next worry; switch the hint
    when the button enables (play 10). (general)
17. (nit) **Count toggle**: a fixed label "Shorter count (3)" with aria-pressed, not a flipping label (craft 7). (general)
18. (nit) **Sorted card label**: "Sorted" in its aria-label after a drop, not "Pick up worry card" (craft 8). (general)

## Settled calls
- Should fix 2 (clue pairing): teaching said should fix, play said polish. Kept as should fix: the tool confirms a
  pairing its own Body clues mode contradicts, and the missing tummy clue is a gap in what S1 taught.
- Should fix 8 (rings): craft said should fix, play and sensitivity polish. Kept as should fix: a ring over the child's
  face and a heart clue on the wrong side are seen by every student in Body clues.
- Should fix 4 (digit keys): spec "keys 1 to 4" stays for the header; the fix only stops digits switching mode while
  focus is inside the stage or panel. Settled here, not routed.
- Welcome not heard after a first tap on the card or a basket: allowed (BASELINE 16, spec On load); all lenses agree.
  Do not change.
- "Danger right now? Call 911." stays (Cory, 2026-11-05: no hotline on screen); sensitivity 11 only noted. The NCMEC
  and Childhelp lines go in notes.md only, never on screen.
- No score, timer challenge or streak; all-Big is accepted with the "never wrong" note. Do not add a quiz or right
  answer to Sort.
- The door redraw has no people; do not add a person or an adult figure to any card vignette.

## To the spec's open questions
- Spec authors: update spec.md text to match Blocker 1 and Should fix 1, 2, 3, 9, 10, 12 (art prompt, Because rule,
  clue list, rounds, b1 and b3 reasons, notes Disclosure paragraph). Codex fixes the tool; the spec text update is for
  the spec owner.

## Not taken
- Play 7 second half (a pulse or shake on the kid when a ring is tapped): new animation beyond the spec, not needed.
- Play 9 (one-word tile labels at 680x425): spec hides names there; distinct icons (Polish 9) solve it.
- Sensitivity 11 (911 is US-only): Cory's 2026-11-05 call stands.
