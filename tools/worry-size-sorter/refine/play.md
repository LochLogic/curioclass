# Play lens: worry-size-sorter (round 1)

Played twice: as a grade 4 student alone at home (Sort through all 13 cards, each tool, a week goal, the
reflection) and as a teacher projecting Sort and Body clues. Not a Curiosity (lesson tool, grades 3-5 Health).
My frames: `S:/CurioClass-codex-scratch/worry-size-sorter/play/shots/` (shots s1.json, s2.json, drive.py, port 9853).
Shared audit frames cited from `S:/CurioClass-codex-scratch/worry-size-sorter/audit-r1/`.

The defaults work for a solo student: the first screen says what to do (hint plus the card caption "Tap or drag to
pick up"), every waiting moment I walked names the next action and the control in the hint, Calm keeps the
breathing and squeeze timing, and nothing overlaps or clips at any audited size. The findings below are about
feel and words matching the state.

## Findings

1. **Sort, Big card dropped in Small or Medium (src.html:576-583)**: the card slides toward Big, then snaps back to
   the top of the stack at full size, captioned "Sorted. Look at the help beside it." The animation has no
   `fill`, so the one moment the tool exists to show (a Big worry always ends up in Big) is undone on screen; only a
   23 px thumbnail lands in the basket. A student who misses the 0.6 s slide sees the card still sitting on top.
   Better: the card stays in (or shrinks into) the Big basket and the stack shows the next card back or an empty
   slot. Seen: `play/shots/big-drop-after.png` (1.2 s after the drop, card back on top), and `big-drop-mid.png`.
   **should fix**, general.

2. **Sort, every drop (src.html:483-486, 572)**: for Small and Medium drops the card never moves either; it stays on
   the stack (scaled .94) while the basket bounces and a tiny thumbnail appears. With drag, the ghost vanishes on
   drop and the card reappears at the top. The core action of the tool lands flat. Better: the card visibly drops
   into the basket it was given (same fix as 1). Seen: `audit-r1/state-sorted-card-1366x768.png`,
   `play/shots/small-drag.png`. **polish**, general.

3. **My week, "Because" from a meter result (src.html:1027-1031, 1101)**: any result is used, whichever way it went.
   After Talk back rated 2 then 4, the goal reads "Because my meter went from 2 to 4 when I tried it," and the body
   clue choices are hidden, so the student cannot pick a better reason. Words do not match the intent of a reason.
   Better: use the meter line only when after < before; otherwise show the clue choices. Seen: drive shot
   `play/shots/because-up.png` (panel text "Because my meter went from 2 to 4 when I tried it."). **should fix**,
   general.

4. **Keyboard, number keys on the meter (src.html:1247-1250)**: the meter steps are drawn as big numbers 1 to 5,
   but the keys 1 to 4 switch modes everywhere. A keyboard student pressing 4 for "A lot" lands in My week and
   loses the tool run; 1 goes to Sort, 2 to Body clues. Better: while focus is in the meter (or in Tools step 1/3),
   1 to 5 rate; or move mode keys off bare digits there. Seen: `play/shots/meter-key4.png` (focus on meter2, key
   "4", mode became "week"). **should fix**, general.

5. **Sort result wording (src.html:529)**: a Small card put in Medium says "You put it in Medium." then "One way to
   size it: Small." To a grade 3 student alone that reads as "you were wrong," against the panel's own "Small and
   Medium can feel different to different people." The spec's "Many kids say Small" is softer. Better: "Many kids
   put this in Small. Medium is fine too." Seen: `play/shots/small-in-medium.png`. **polish**, general.

6. **My week, body clue reason for any tool (src.html:1096, 1102)**: all four clues are offered for every tool, so
   "I will do Worry box ... Because it can help with fast heart" is allowed, while Body clues ties fast heart to Box
   breathing only, and the label says "Pick the body clue this tool helps" as if one is right. Better: offer the
   clues Body clues names for that tool (or mark them "Body clues says"). Seen: code, and
   `audit-r1/state-week-chart-1366x768.png` (goal sentence built from a clue pick). **polish**, general.

7. **Body clues, Head ring on the face (src.html:94, 232)**: ring 1 sits over the kid's nose and mouth at every size;
   at 680x425 it covers the whole face. Better: put it on the forehead or hair, beside the head. Also tapping a ring
   changes nothing on the kid (no pulse at the chest, no shake at the hands), a flat moment a small code effect
   could lift. Seen: `audit-r1/state-body-clue-1366x768.png`, `state-body-clue-680x425.png`. **polish**, general.

8. **Worry box fold (src.html:131)**: "Fold it" just shrinks and tilts the slip into a thin strip with about 9 px text
   far above the box; it does not read as folding, and the slip is not lined up with the slot it then drops into.
   Better: a two-step fold (halves then quarters) over the slot. Seen: `play/shots/box-folded.png`. **polish**,
   general.

9. **Tools at 680x425 (src.html:205)**: tile names hide, leaving four glyphs where □ (Box breathing) and ▣ (Worry box)
   look nearly alike. Per spec, but a preview viewer cannot tell them apart. Better: keep a one-word label
   ("Breathe", "Talk", "Squeeze", "Box"). Seen: `audit-r1/state-mode-tools-680x425.png`. **nit**, general.

10. **Big panel button vs hint (src.html:518, 524)**: for up to 4 s the button reads "Listening..." while the hint
    says "Tap Next worry when you are ready." Small mismatch of words and state. Seen:
    `play/shots/big-drop-mid.png`. **nit**, general.

Checked and fine: Big panel fits at 1366x768 and 1280x720 with Next worry visible (`big-1280.png`); at 680x425 Next
worry is moved to the top and visible (`big-680.png`), the 911 line needs a panel scroll there (preview size only);
end of sort counts match the placements (`end-sort.png`); breathing count and phase (`breath-mid.png`), Calm
breathing keeps time (`breath-calm`: phase advanced on schedule, dot holds its corner); squeeze poses and timer
(`squeeze-mid.png`, `squeeze-let.png`); Talk back m3 shows its "gets bigger if" note (`talk-m3.png`); no console
errors in any of my shots. The cheap ways: putting all 13 in Big is accepted with the "never wrong" end note; Big
cards cannot be left outside Big; Facts, Plan and Brave all work. Nothing to give away (no quiz mode).

Content (abuse, online exploitation, family illness on the Big cards) is for the sensitivity review
(`refine/sensitivity.md`); I did not judge it.

Counts: blocker 0, should fix 3, polish 5, nit 2.

## Audit pilot

- Leads confirmed: none to confirm as faults. The "welcome not heard" rows for #worryCard and the baskets are by
  design (spec: the first card tap makes only its own sound; BASELINE 16); the premise stays on screen
  ("Every worry is real...") and in Read.
- Leads wrong: none.
- Missed: no audit state reaches a Big card (sorted-card always uses the first card, which is Small), so the Big
  panel and the snap-back (finding 1) were never shot; the card not moving on any drop (2); the meter-result
  reason (3); the digit-key clash (4, a key path, not a click); wording and placement items 5 to 10.
