# Teaching lens: worry-size-sorter (round 1)

Cold lens, blind to codex-report*.md and codex-review.md. Read: REFINE.md, STANDARDS.md, BASELINE.md, spec.md, src.html
(all), worry-data.json, voice/lines.json, notes.md, tool.draft.json, audit-states.json, refine/sensitivity.md (its
child-safety findings are not repeated here). Drove the bundle in headless Chrome (port 9850, no host server).
My frames: S:/CurioClass-codex-scratch/worry-size-sorter/teaching/frames/. Audit frames cited from audit-r1/.

Standards checked against the SHAPE America NHES 2024 page (indicator text fetched 2026-11-06). Facts spot-checked
against Cleveland Clinic (box breathing), HealthLinkBC (PMR timing), NHS Every Mind Matters and YoungMinds (worry time).

## Findings

1. **where:** src.html:1027-1031 `because()`, My week builder and goal sentence.
   **what:** the "Because" line is built from the tool's last meter result whatever its direction. A student whose meter
   went UP sets a goal that reads "I will do Squeeze and let go in the morning every day this week. A grown-up at home
   helps me remember. Because my meter went from 2 to 4 when I tried it." The goal's own reason argues against it.
   NHES 6.5.1 asks the student to explain how the goal supports well-being; this teaches the opposite. Same for an
   unchanged meter ("from 3 to 3").
   **how seen:** t2-week-because-up.png, t2b-week-goal-up.png (driven: Squeeze, rate 2, Stop, rate 4, then builder).
   **fix:** use the meter line only when after < before (or calm 1 to 1, worded "I practiced it when I was calm");
   otherwise show the body-clue pick.
   **level:** should fix. **tag:** general.

2. **where:** src.html:325, 1096-1102 (Because row), against worry-data.json clues.
   **what:** "Pick the body clue this tool helps" accepts any clue for any tool, so the goal says "I will do Box
   breathing ... Because it can help with busy thoughts", while the tool's own Body clues mode teaches busy thoughts
   (Head) go with Worry box and Talk back, and box breathing goes with heart, breathing and tummy. The prompt reads as
   a fact question and the tool confirms a wrong pairing. The list also has four clues where Body clues has five (no
   tummy / butterflies).
   **how seen:** t3-week-because-mismatch.png; goal sentence printed by the driver.
   **fix:** either mark the clues each tool answers (from D.clues "tools") and offer only those, or reword to "Pick the
   body clue you want help with" so it is the student's own reason. Add tummy.
   **level:** should fix. **tag:** general.

3. **where:** src.html:769 ("Two rounds, then check your meter."), 898; spec Sources row "Box breathing ... 3 to 4 rounds".
   **what:** both cited sources (Cleveland Clinic: repeat the cycle three to four times; WebMD) give 3 to 4 rounds, the
   spec's own Sources row says so, but the practice ends at 2 and the panel teaches "Two rounds". A student who
   follows the tool learns a shorter practice than the source.
   **how seen:** read code; Cleveland Clinic page fetched. Audit frame state-breathing-stopped-1366x768.png.
   **fix:** default to 3 rounds ("Three rounds, then check your meter"; 48 s at 4, 36 s at 3), still up to 4.
   **level:** should fix. **tag:** general.

4. **where:** Tools opened from the header, Box breathing and Squeeze (src.html:707, 760-764).
   **what:** step 1 says "Picture it's really happening." while the stage shows a bare "A spelling test tomorrow." with
   no "Your worry:" label, and for these two tools the student has no worry picker (only Talk back and Worry box get
   one). A student who came straight to Tools is asked to picture a worry they did not pick and cannot change.
   (Sensitivity finding 6 rewords the prompt; this is about the missing label and choice.)
   **how seen:** t1b-tools-header.png.
   **fix:** for Box breathing and Squeeze opened from the header, hide the worry line and ask "How worried does your
   body feel right now?" only, or offer the same picker.
   **level:** polish. **tag:** general.

5. **where:** Body clues panel "Try:" line (src.html:673).
   **what:** the link from a body clue (S1) to the tool that answers it (S7) is text only. The student reads "Try: Box
   breathing" and has to find Tools and the tile themselves. This is the moment the two standards meet.
   **how seen:** audit state-body-clue-1366x768.png; code.
   **fix:** make each named tool a button that opens Tools on that tile.
   **level:** polish. **tag:** general.

6. **where:** Sort, Medium drop result (src.html:528-531).
   **what:** Medium means "A tool, and talk it over with someone." but the Medium result only offers "Try a tool on it";
   the "talk it over" half (and NHES 1.5.7, when to seek help) is never prompted for a Medium card.
   **how seen:** t4-sort-medium-into-small.png (panel text) and code.
   **fix:** for Medium-sized cards add one line, "Who could you talk this over with?" with the adult chips, or a "Ways to
   start" line.
   **level:** polish. **tag:** general.

7. **where:** worry-data.json b5 reason; NHES 1.5.7 ("Explain when and why it is important to seek health care").
   **what:** the one card that maps to seeking health care ends "is a sign to get help" without saying what help. The
   Doctor and School counselor chips are there, but nothing ties this card to them.
   **how seen:** read data against the fetched indicator text.
   **fix:** "...is a sign to get help. Tell a grown-up you trust; a school counselor or doctor can help with worry."
   **level:** polish. **tag:** general.

8. **where:** My week reflection (src.html:1187-1224).
   **what:** the barrier chips (6.5.4) lead nowhere: picking "I forgot" or "Someone interrupted" changes nothing, and
   the next-week choices are only Keep / Change the time / Try a different tool; there is no "Change who helps me",
   the obvious answer to "I forgot". Reflection (6.5.6) stops at naming the barrier.
   **how seen:** audit state-reflection-1366x768.png ("I forgot" picked, panel unchanged); code.
   **fix:** add "Change who helps me remember", and when "I forgot" is picked, mark it as the suggested choice.
   **level:** polish. **tag:** general.

9. **where:** Sort end panel (src.html:547-548).
   **what:** after an all-Big sort it reads "Big: 13. Every Big one goes to a trusted adult." directly above "You put 8 in
   Big that a tool could also help." The first line counts basket contents, the second admits 8 were not Big-sized.
   **how seen:** t5-sort-end-allbig.png.
   **fix:** "In Big: 13. The 5 Big worries always go to a trusted adult."
   **level:** nit. **tag:** general.

10. **where:** notes.md Sources and "Good to know".
    **what:** notes' source list drops five sources the spec and tool.draft.json cite (WebMD, Michigan Medicine, eSafety,
    Advocates for Youth, US Attorney tip sheet) and adds NHS Every Mind Matters, which tool.draft.json lacks; YoungMinds
    has two different URLs. NHS EMM, cited for worry-time length, actually suggests worry time "before bed"; the
    no-bedtime rule rests on YoungMinds ("Avoid using the box just before bedtime"), so cite that for timing.
    "Narration uses the kit's browser voice fallback in this Build-only version" will be false once voice is recorded.
    **how seen:** read notes.md against spec, tool.draft.json and the fetched pages.
    **level:** nit. **tag:** general.

## Checked and sound
- Codes: S1 (body clues, "too big to carry", Big cards), S6 (tool, time, helper, reason, 7-day chart, reflection) and
  S7 (four tools done with before/after rating) are each taught by something the student does. 6.5.2 (assistance) is
  the "Who helps me remember" row; 6.5.5 tracking is the chart. No code is only mentioned.
- Meter results: all 25 before/after pairs printed (t8-meter-all): down 10, up 10, same 4, calm start 1, as spec.
- Done when 3: Big cards dropped in Small/Medium go to Big with reason and panel; Small/Medium in Big accepted with
  "Telling is never wrong" (t5, audit sorted-card). Done when 7: day index by calendar date, future days refused,
  day 8 opens reflection (code 1001, 1038, 1173; audit week-chart and reflection frames).
- No giveaway problem: Sort is not a quiz; every option is accepted or corrected with a reason.
- Facts: box breathing 4-4-4-4 (Cleveland Clinic); PMR 5 s tense, 10 s relax within 4-10 s / 10-20 s (HealthLinkBC);
  worry time 10 min within NHS's 10 to 15; no bedtime per YoungMinds; body clues match the spec Sources rows.
- Language plain for grades 3-5; no score, timer challenge or streak; rule 8 note names abuse, online exploitation,
  family illness; Support at home ideas are doable tonight. Cultural / hard-history: nothing beyond what sensitivity.md
  already covers.

Counts: blockers 0, should fix 3, polish 5, nit 2.

## Audit pilot
- Leads confirmed: none were teaching leads. The "welcome not heard after a first tap on the card or a basket" rows are
  allowed by BASELINE 16; the premise is on the stage (principle line) and in Read, so nothing lost for teaching.
- Leads wrong: none.
- Missed (outside what it can see): the goal reason built from a rising meter (1), the clue-tool mismatch (2), the
  rounds below source (3), and the reflection chips leading nowhere (8).
