# Teaching lens: fake-or-fact-lab (Refine round 1)

Cold read of spec.md, src.html, notes.md, handoff.md, art/prompts.json, voice/lines.json and kit/fact-check.js; bundled
with `CURIO_DRAFT=1` (570 KB); `audit_tool.py` run first (port 9960); my own drives on port 9962 through `__tool`
(frames in my scratch folder `lens-fof-teaching/f1` to `f5`). Sources checked online: Wineburg and McGrew (2019)
summaries (Stanford repository, Digital Inquiry Group), NPS Denali "Amphibians", and name searches for the invented
brands.

Counts: blockers 1 (general 0, family 1), should fix 8 (general 3, family 5), polish 8, nit 3.

## What holds up

- **The lateral-reading claim is right.** The Report card ("professional fact-checkers left an unfamiliar site quickly
  ... judged sites more accurately than historians and college students who read the site closely") matches the study:
  10 fact-checkers, 10 historians, 25 Stanford undergraduates; fact-checkers left the site and opened new tabs, the
  others stayed on the page and were taken in by logos and domain names. The three questions match Digital Inquiry
  Group's Civic Online Reasoning. S1's `.example.org` address is a neat echo of the study's ".org" trap.
- **Expert verdicts and reasons** for S1, S3, S4 and S5 hold up against what the outside read finds. Every reason is
  word for word the spec's. Report counts recomputed by hand from the calls (inside 2 of 6, outside 6 of 6 for my test
  set) match the screen.
- **Done when**, as far as Teaching reaches: 1 pass (locks, padlock label, locked line; same-site links on S1, S2, S4);
  2 pass for the spec's terms (chips and typed); 3 pass (S1 and S5 Trace highlight the passage, S2 image search lists
  the 2019 collage first, S1 and S4 lookups); 4 pass (Lock disabled until a verdict, seconds and tabs recorded, reveal
  shows verdict and why); 5 pass (counts, the table survives a reload); 6 fails in spirit (see the blocker); 7 and 8
  belong to Play and Craft (see the Audit pilot note on 375 wide).
- **Nonpartisan, classroom-safe**: study apps, a shark hoax, library hours, a four-day week, games, wood frogs. Every
  address passes `fc.safeDomain`.
- **Sensitivity agent: not needed.** Nothing cultural, Native or hard history (rule 5) and no people in any picture.
  The S2 shark photo is not a sensitivity question and is already settled: Cory took the recommendation on w1-51
  ("Keep it") on 2026-10-27, so the spec's open question is stale.

## Blocker

1. **Two invented names belong to real brands, and both are cast as bad actors.** (src.html:292 and 385 "Daily Ledger
   Now"; src.html:329, 429, 511 "BrightPath Apps")
   - *What:* "The Daily Ledger" is a real daily newspaper (Canton, Illinois, USA Today Co.). Here "Daily Ledger Now" is
     the fake news site with a hidden owner. "BrightPath" is a real children's brand (BrightPath Kids / BrightPath
     Early Learning, a large child-care chain with a parent app). Here "BrightPath Apps" secretly funds a fake research
     group. Done when 6 says "no real site, brand or person appears", and the family rule says "no real brands". A
     reserved domain doesn't help when the display name is a real brand's.
   - *Fix:* rename both to names with no real match (search each before use), and carry the new names through the
     index terms, chips, notebook text, answer key in handoff.md and the spec. Engine lesson: the family doc should
     ask builders to search every invented display name, not only to check domains.
   - *Seen:* web search for both names; frame `f2/t14-s4-inside.png`.
   - Tag: **family:fact-check**.

## Should fix

2. **Nothing on the Lab screen says the pages are made up.** (Lab mode, every specimen; notes.md says it, the screen
   doesn't)
   - *What:* A solo student (rule 4) who reads S4 in Pass 1 sees "BREAKING: Every school will switch to a four-day week
     next fall" with no sign it is invented. Only Wayfind's home ("Search the made-up web"), Openpedia's strapline and
     CheckPoint Desk's tagline say so, and only in Pass 2. The reveal never says it either, and "Fact-checkers:" reads as
     a real ruling.
   - *Fix:* one plain line that is always visible in the Lab (under the tray or in the browser chrome): "Every page in
     this lab is made up for practice." Label the reveal "Our fact-check" or "What a fact-checker would find".
   - *Seen:* `grep "made-up"` in src.html and the engine; frames `t01`, `t14`, `t20`.
   - Tag: **family:fact-check** (the engine could draw the line in its browser frame for all three siblings).

3. **The three verdicts are never defined, so S2 and S5 are a guess about the scale, not about the source.** (panel
   verdicts; src.html:302 S2 why)
   - *What:* S2's own reason starts "The flood was real." A careful student who finds the real flood and the fake shark
     can fairly pick "Partly true, stretched" and is marked "✗ no match". S5 is the mirror case ("Scientists PROVE ...
     smarter" could fairly be "Don't trust it"). With the exact-match rule, the student cannot know where the line is.
   - *Fix:* a one-line meaning for each verdict that a student can read before the call (a small "What the calls mean"
     under "Your call", or in the hint): for example Trust it = the main claim holds and the source is who it says;
     Partly true, stretched = there's a real fact under it, but the claim goes further than the evidence; Don't trust it
     = the main claim is false or the source hides who's behind it. Then S2's reason can say why: "The flood was real,
     but the post's news is the shark, and that photo is a 2019 art collage."
   - *Seen:* reveal frames; spec Content.
   - Tag: **family:fact-check** (fact-check-desk and ad-agency share the scale).

4. **S6's "the author is who she says she is" has nothing to check against.** (src.html:421 S6 page; src.html:487
   staff table; spec S6)
   - *What:* the pond page is signed only "Ms. Park". It never says she teaches, or where. The outside find is a staff
     page at a different school site listing "Ms. Park, Science teacher", matched by surname alone. That teaches a weak
     move (a name match is not proof of identity), and it contradicts the reason given.
   - *Fix:* give the page a checkable claim, for example an "About me" line: "I teach science at Willow Creek Middle
     School" (under the renamed school, item 6). The staff page then confirms what she said. Keep the hit counter and the
     clip art.
   - *Seen:* frame `f2/t17-s6-inside.png`, `t17b-s6-staff`, `t27` notes.
   - Tag: **general**.

5. **S1's Trace works in Pass 1, so an outside card is earned on the inside read.** (src.html:336 cite link; Pass 1
   locks at src.html:677)
   - *What:* "our 2025 family survey" is a same-site link, so in Pass 1 it opens the survey page with "412 StudyStar
     customers" highlighted and adds a **What's the evidence?** card. The spec lists Trace as a Pass 2 tool. The inside
     column of the lab table then mixes in an outside move.
   - *Fix:* treat `cite` links as part of the `leave`/Trace lock in Pass 1 (shown with the Pass 2 padlock, like the other
     locked controls), or, if the spec prefers that a careful inside reader can open the site's own survey page, open it
     without the highlight and tag that card **Inside**. Either way say which in the spec.
   - *Seen:* drive `f3/t22-s1-pass1-survey` (url `/survey`, mark "412 StudyStar customers", evidence card, pass 1).
   - Tag: **family:fact-check**.

6. **Other invented names that match real places.** (src.html:483 to 488)
   - *What:* "Willow Creek Middle School" is a real school name (Huntertown, Indiana; Rochester, Minnesota; Willowcreek
     in Lehi, Utah and Portage, Indiana), and the page lists named staff ("Ms. Park", "Mr. Okafor", "Ms. Reyes"). That
     edges toward naming real private people at a real school. "Port Alder", "Lakeshore Tribune", "Openpedia", "Wayfind"
     and "CheckPoint Desk" turned up no real match in my searches.
   - *Fix:* an invented school name with no real match.
   - *Seen:* web search.
   - Tag: **general**.

7. **The outside call can be locked with no outside reading, and Retest after the reveal rewrites the data.**
   (src.html:703 `lockCall`; src.html:723 `retest`)
   - *What:* the lesson is "see in your own data how the outside read did". But Pass 2 locks with zero tabs and zero
     findings (drive `t08`: pass 2 recorded 0 s, 0 tabs), and those rows still count as "Outside read matched". Retest,
     offered right after the expert verdict, replaces the row, so a student can turn every miss into two matches
     (drive `t09`: after Retest the counts are 1 of 1 inside and 1 of 1 outside). The report's comparison then measures
     memory, not the read.
   - *Fix:* (a) Lock my call in Pass 2 needs at least one outside card (the hint says so while it waits, and Lock
     stays visible but off), and (b) a retested row is marked "retest" in the table and left out of the two counts, or
     the first try is kept. Both change spec interactions, so the integrator may send them to the spec's open questions
     instead.
   - *Seen:* drives `f2/t08`, `f2/t09`.
   - Tag: **family:fact-check** (fact-check-desk will have the same holes).

8. **The jar labels hint at the answer.** (src.html:300 to 311 `kind`; tray)
   - *What:* S3 (the Gazette, Trust it) is labelled "article"; S4 (Daily Ledger Now, Don't trust it), which is the same
     kind of page, a news story on a news site, is labelled "site". Both "site" jars are Don't trust it. Small, but it is
     exactly the badge-reveals-the-answer case in the BR1 wave lessons.
   - *Fix:* label by what the page looks like, the same for look-alikes: S3 and S4 both "news story", S1 "site" (or
     "research site"), S2 "post", S5 and S6 "blog".
   - *Seen:* frames `t13`, `t14`; spec Content.
   - Tag: **general**.

9. **Not every part of W.7.8 and W.8.8 is taught well.** (module library-6-8-is-it-reliable; notes.md Standards taught)
   - *What:* the credibility-and-accuracy clause of W.6.8 to W.8.8 is taught well (two calls per source, evidence cards).
     Grades 7 and 8 also have "use search terms effectively". The suggestion chips choose the search terms for the
     student, and a typed query fails easily ("study app", "frog", "library closing" and "Willow Creek" all return
     nothing). Rule 2 wants the code really taught, so this is a should fix.
   - *Fix:* hold the chips back until the student has typed one search, or until a search returns nothing (the
     no-results line already names the three kinds of keywords). Then plain plural and singular should both match:
     `FC.pure.words` drops a trailing "'s" but not a plain "s", so "study app" misses the "apps" entry. The citation
     and paraphrase clauses aren't taught anywhere in this tool. Notes.md already limits the claim to the credibility
     clause; keep it that way, and the integrator can note in the module that citation is taught elsewhere.
   - *Seen:* query probe `q.json` (37 typed queries).
   - Tag: **family:fact-check** (stemming lives in the engine).

## Polish

10. **The Report doesn't react to the student's own data.** The conclusion card is the same whether the outside read
    beat the inside read or not, and a solo student gets no reflection prompt (the talk questions are in notes.md
    only). Better: one line built from the counts ("Your outside read matched 4 more times than your inside read."
    or "Your two reads tied. Which specimen fooled your inside read?"), and the rows where inside missed and outside
    matched picked out. Tag: general.
11. **Openpedia's wood frog says "comes back to life"** (src.html:515). The frog never dies; NPS says it is inanimate,
    with no breathing and no heartbeat, then thaws. Better: "In spring it thaws, and its heart starts beating again."
    "In the far north" (spec wording) is narrower than NPS, which says Alaskan frogs stay frozen longer than wood frogs
    elsewhere in North America. "In cold winters" is closer. Tag: general.
12. **The S2 shark fin is a smooth, even cone** (`art/ff-shark-street.webp`), with no curved trailing edge, so the
    "realistic fake" the spec and w1-51 wanted reads as fake at a glance and S2's inside read gets easy. Better: a
    redraw with a real dorsal fin shape (the sd prompt can say "a curved shark dorsal fin with a dark trailing edge").
    The flood photo (a different street, no shark) and the wood frog (brown, dark eye mask, frosty leaves) are right.
    Tag: general.
13. **The welcome names Lock my call while it is still off.** The builder flagged this against the BR1 lesson. As
    teaching, the line is fine: it orders the steps and Lock is the step after the verdict. If the integrator applies
    the lesson to the letter, a version that still says how to act: "Pick a specimen and read only the page itself.
    Then choose a verdict, and lock your call." The panel shows the control. Play and Craft own the final call. Tag:
    general.
14. **Report column "Tabs opened"** shows only Pass 2's tabs. "Tabs opened outside" says what it is. Tag: general.
15. **The reveal could name the source's purpose** (C3 D3.2 "intended use"): S1 "to sell study apps", S4 "to get
    shares". One clause in each reason would make the intended-use half of the code visible. Tag: general.
16. **"✗" means two things in the table**: the Don't trust it symbol and "✗ no match" sit side by side ("✗ Don't trust
    it ✓ match"). Better: words or a different mark for match ("Matches" / "Doesn't match"). Tag: family:fact-check.
17. **Teacher notes could name the .org lesson.** S1's `.example.org` address is one of the study's own traps ("official
    -looking logos and domain names"). One line under Good to know would help the class talk. Tag: general.

## Nit

18. The spec's Open question on the S2 photo is settled (w1-51, "Keep it"); remove it from the spec. Tag: general.
19. S3's photo shows autumn trees on an article dated February 12, 2026. A file photo is believable, but a winter or
    neutral season would avoid the question. Tag: general.
20. CheckPoint Desk's tagline "A made-up fact-check site" is the only site inside the fiction that calls itself made
    up. Once item 2 adds a lab-wide line, this tagline can go. Tag: general.

## Frames looked at

`f1/t01-default`, `f2/t02` (S1 inside taps), `t06b` (Openpedia), `t06c` (lookup), `t07`, `t08`, `t09`, `t10` (S2
inside), `t11` (image search), `t12b` (Gazette flood), `t12c` (collage page), `t13` to `t17b` (S3 to S6), `t18`
(Report, six rows), `t20` (reveal), `t21` (empty Report), `f3/t22` to `t27` (Pass 1 links and taps), `f5/t40`, `t41`
(S4 lookup, reload), audit `size-680x425`, `size-375x812 (iframe host)`.

## Audit pilot

- **Confirmed:** the 375-wide frame shows the browser squeezed to the site header with Lock my call at the very bottom
  edge (Done when 7 risk, for Play and Craft). The tiny `our 2025 family survey` link target (164x24) is real.
  Clicking a verdict or jar first speaks the welcome naming the disabled Lock my call, which matches the builder's
  flag. Motion off is clean. The voice repeats are clean.
- **Wrong or noise:** the 18 overlap leads at 375 wide pair page text inside the browser's scroll box with panel
  controls. That page text sits clipped out of view, so nothing visible overlaps. "Clipped" on the tab title and the
  long host are deliberate ellipses.
- **What it missed:** every finding above. It cannot see the real-brand names, the missing "made up" line, the
  undefined verdict scale, S6's name-only identity check, Trace working in Pass 1 (it clicked the link once and only
  logged "rebuilt"), outside calls with no outside reading, Retest rewriting the data, or jar labels that track the
  answer. All of these sit past the first click or in the content. A lens can leave sizes, Motion off and the 2 s
  voice pace to the script. It can't leave anything about content, flow or teaching.
