NOT YET

# Sensitivity review: worry-size-sorter

Fresh agent, blind to codex-report.md and codex-review.md. Read as a child-safety and early-childhood counsellor would.
Read: spec.md, src.html (all), worry-data.json, voice/lines.json (every line), notes.md, tool.draft.json, art/prompts.json.
Looked at every .webp (13 card vignettes on a contact sheet, the five kid poses side by side, the door card and the kid's
hair at full size). Drove the bundle in headless Chrome (port 9841): b1 dropped in Small at 1366x768, b3 dropped in Medium
at 1280x600, Body clues with Tummy open, Tools with m3 at step 1, Talk back on m3.

Scope note: the brief called it K-2, but spec, tool.draft.json and the page all say Grades 3-5. I judged it for ages 8 to 11.

## Findings

1. **where:** art/ws-card-door.webp, shown on card b1 "A grown-up asked me to keep a secret, and it feels wrong." (Sort,
   basket thumbnail).
   **what:** the picture is a child's bedroom at night (quilted bed, stuffed bunny, lamp on) with the closed bedroom door
   and hallway light coming in under it. Paired with an adult's secret that feels wrong, this is the classic picture of
   night-time abuse in the child's own room. For a child living that, met alone at home (rule 4), it is a trigger with no
   adult present; for every other child it plants a frightening, specific scene the text never says. It also narrows "a
   grown-up's secret" to home and bedroom, when grooming happens in many settings.
   **how seen:** full-size view of the webp, and the big-b1 frame (card on top of the stack beside the Big panel).
   **fix:** redraw with no bedroom and no night: for example a small wrapped box or a closed notebook with a "shh" sticker
   on a hallway bench or school cubby, daylight. Keep "No people."
   **level:** blocker. **tag:** general.

2. **where:** worry-data.json b3 reason (also voice/lines.json): "You won't be in trouble for telling."
   **what:** a promise the tool cannot keep. Some adults do react badly (take the device, scold); a child who sent a photo
   and then is punished learns not to tell next time. It also misses the core message for this card: it is not the child's
   fault. NetSmartz-style guidance leads with blame-free framing, not a guarantee about consequences.
   **how seen:** read the data; the big-b3-short frame shows it as the first line under "This one is Big."
   **fix:** "Tell a trusted adult right away, even if you already sent something. It's not your fault. The person who
   asked did something wrong." Re-record the voice line to match.
   **level:** should fix. **tag:** general.

3. **where:** worry-data.json b1 reason: "A secret that feels wrong, or that you're told to keep from your family, is always
   one to tell."
   **what:** good flag, but it reads as if the family is always the safe place to take it, and it does not say the grown-up
   may be someone the child knows and loves, which is the usual case. A child whose secret-keeper is a family adult needs
   to hear that it still counts. (The adult chips below do give non-family routes; the reason should match.)
   **how seen:** big-b1 frame, read alongside the chips.
   **fix:** add one sentence: "That's true even if it's a grown-up you know, or one in your family." Keep the rest.
   **level:** should fix. **tag:** general.

4. **where:** art/ws-kid-stand, ws-kid-fists, ws-kid-shoulders, ws-kid-loose (the hair top).
   **what:** green chroma-key fringe left in the curls (12+ clearly green pixels on stand; visible as a green halo at full
   size and on the Body clues stage at 560 px). It is the only child in the tool, and a green rim on textured hair reads
   as careless handling of a Black or brown child's hair.
   **how seen:** zoomed crop of ws-kid-stand head; five-pose contact sheet shows it on four poses (ws-kid-toes is clean).
   **fix:** re-despill or hand-clean the hair edge on the four poses.
   **level:** should fix. **tag:** general.

5. **where:** notes.md, "Sensitive content and disclosures".
   **what:** online exploitation is one of the five Big cards, but notes give the teacher no US route for it. School
   reporting procedure covers abuse; an online photo request from a stranger also belongs with NCMEC.
   **how seen:** read notes.md against the b3 card.
   **fix:** add one line: "For an online photo request or a shared image of a child, report to NCMEC's CyberTipline
   (report.cybertip.org, 1-800-843-5678) as well as through your school; Take It Down (takeitdown.ncmec.org) helps remove
   images." Adult-facing only, so it does not conflict with the no-hotline-on-screen call.
   **level:** should fix. **tag:** general.

6. **where:** Tools step 1, src.html renderToolPanel: "Picture it's really happening. This is your own rating, not a test."
   **what:** asks a child working alone to imagine the worry vividly. Fine for a spelling test; for m3 ("My grown-ups were
   arguing") it is an imaginal-exposure prompt about home conflict with no adult present.
   **how seen:** tools-m3 frame (the m3 "gets bigger if" note shows under it, which helps but comes after).
   **fix:** "Think about this worry for a moment. How worried does your body feel right now?" for every card.
   **level:** polish. **tag:** general.

7. **where:** worry-data.json b4 and b2 reasons.
   **what:** b4 ("Being hurt is never okay...") and b2 ("too heavy to carry alone") are accurate and kind but miss the line
   children most need with each: being hurt is not your fault; a family member's illness is not your fault and not your
   job to fix.
   **how seen:** read data.
   **fix:** b4 add "It's not your fault." b2 add "It's not your fault, and it's not your job to fix it."
   **level:** polish. **tag:** general.

8. **where:** Body clues hotspots (src.html #clue0, #clue1, #clue3).
   **what:** ring 1 (Head) sits on the child's face, covering eyes and nose; ring 4 (Tummy) sits at the hoodie hem and
   waistband rather than the belly; ring 2 (Chest, the heartbeat clue) is on the child's right side, the heart is on the
   left (viewer's right).
   **how seen:** clues frame at 1366x768.
   **fix:** Head ring at the side of the hair or forehead, Tummy ring up on the hoodie pocket, swap rings 2 and 3 so the
   heart clue is on the viewer's right.
   **level:** polish. **tag:** general.

9. **where:** notes.md, "Support at home" and disclosure paragraph.
   **what:** the tool stands alone and many will meet it at home, but notes tell a parent nothing about what to do if a
   Big card turns into a real worry. The teacher disclosure steps also leave out "listen, don't question for details or
   investigate, write down the child's own words, tell them who you will tell next."
   **how seen:** read notes.md.
   **fix:** one line each: home ("If a Big card brings up something real, listen calmly, thank your child, and contact your
   child's school counselor or doctor; if it involves abuse, the Childhelp National Child Abuse Hotline is 1-800-422-4453"),
   and the teacher steps above.
   **level:** polish. **tag:** general.

10. **where:** Tools step 3, meterOther / meterResult when the after rating is 4 or 5.
    **what:** "Try a different tool, or talk to someone." is gentle but vague when a child rates the worry high after
    practising.
    **how seen:** read meterResult and L.meterOther.
    **fix:** "talk to a grown-up you trust" in place of "talk to someone".
    **level:** polish. **tag:** general.

11. **where:** Big panel, "Danger right now? Call 911."
    **what:** correct scope (only immediate danger, never for worry itself) and US-only, as notes say. On a public site a
    non-US child sees 911 with no country cue. Accepted under Cory's 2026-11-05 call; noted only.
    **level:** nit. **tag:** general.

## Checked and sound
- Class is never asked to disclose: "You never have to tell the class. Tell one grown-up you trust." on the Big panel and in
  Read; notes say keep talk on the written cards; no typing anywhere.
- A parent is one route of six (Parent or caregiver, Grandparent, Teacher, School counselor, Coach, Doctor); "If that
  grown-up doesn't help, keep telling until someone does" covers an adult who fails; week helper offers teacher, friend
  or self, not only home.
- m3 and m4 escalate correctly ("anyone gets hurt, or you feel unsafe at home"; "afraid someone will hurt you. Then it's
  Big.") and that note follows them into Tools. m3 talk-back "It isn't my job or my fault" is right.
- b5 and the "too big to carry" card match CDC/NIMH warning signs; nothing frames worry as a diagnosis.
- Nothing shames: Big cards slide to Big with "This one is Big", an over-cautious Big drop gets "Telling is never wrong",
  zero-day weeks get "That happens."
- Reporting duties in notes are accurate and appropriately hedged (state law and role; an internal report may not satisfy
  a duty to report to the agency).
- People art: one consistent 9-year-old across five poses, calm or smiling in every one, modest seated socks pose; the
  13 worry vignettes have no people, so no group is shown as the one who worries. No stereotype found beyond the hair
  fringe in finding 4.
- Other card art (bedside pills with blank labels, evening kitchen with two mugs, empty bus seat, tablet chat) is gentle
  and not frightening.

Counts: 1 blocker, 4 should fix, 5 polish, 1 nit.
