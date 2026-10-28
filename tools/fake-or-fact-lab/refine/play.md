# fake-or-fact-lab: Play lens (Refine round 1)

Cold play, twice: as a grade 6 student alone at home (Sound on, no teacher), and as a teacher projecting it at
1920x1080 and 1366x768. Bundle: `CURIO_DRAFT=1 python scripts/bundle_tool.py fake-or-fact-lab` (570 KB, clean).
Frames in my scratch folder (lens-fof-play/f1 to f5, audit/): default, Pass 1 with notes and a verdict, Pass 2 on
Wayfind results, Pass 2 site lookup, the reveal, the reveal hidden, a six-row report, an empty report, Clear lab
confirm, the notebook pop-up, eight tabs, no results, every specimen's Pass 1, S2 image search, S5 Trace, at
680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x1000 and 375x812 (`drive.py --host`). Held clicks
(0.12 s) at 2 to 5 s gaps and at 0.25 s for the voice runs. Console clean in every shot.

Counts: blockers 0, should fix 7, polish 6, nits 4.

## Should fix

1. **Retest after the reveal makes the lab table meaningless, and it is the biggest button on screen.** (reveal,
   panel; src.html:757-763, 723-730) After the expert check the panel's big violet button is **Retest**, where Lock
   my call was; Next specimen is a smaller button inside the reveal. A solo student presses the big button, which
   wipes the row and starts Pass 1 again already knowing the expert verdict. Doing that for each specimen gives
   "Inside read matched the experts on 6 of 6", the opposite of what the report is there to show. Seen: frames
   reveal-1366x768, reveal-680x425, h375-reveal; drive run v-retest (row count 0 after Retest). Better: Next specimen
   (or See the report) is the panel's big button; Retest is a small secondary control, and a retested row is marked
   "retest" (or the first try is kept for the counts). **general**
2. **Lock my call is below the fold at 375x812.** (stack layout, relayout() src.html:885-892) Lock spans 808 to 868 in
   an 812 tall iframe; the browser's `Math.max(300, left)` floor pushes it down, and the header takes three rows
   (Read wraps alone). Done when 7 and the BR1 sizes lesson. Seen: h375-default, h375-p1 (`drive.py --host`). The
   page area at that size also shows only the site banner (see polish 5). **general**
3. **The locked hint names no control.** (L.locked, src.html:596, 633) Tapping a padlocked control sets the hint and
   speaks "That's for the outside read. Make your inside call first." A student who can't read the screen is not told
   how to make a call. Better: "That's for the outside read. First pick a verdict and press Lock my call." The hint
   then stays on this line until the next redraw. Seen: v-first-locked, v-locked5. **general** (STANDARDS, Say how to
   act)
4. **Report's hint names no next step while specimens are untested.** (drawPanel src.html:757, L.wReport) With one
   of six tested, the hint and the spoken welcome are "This is your lab table. Compare your inside reads with your
   outside reads." Nothing says to go back. Better, when fewer than six are tested: add "Press Lab to test the next
   specimen." Seen: v-report-partial. **general**
5. **Pass 1 can follow S1's citation to its own survey, and the card is tagged "What's the evidence?" during the
   inside read.** (WORLD S1 `/survey`, same host; fact-check.js noteOn and page notes) The survey sits on
   smartstudycenter.example.org, so the "leave" lock does not apply. In Pass 1 a tap on "our 2025 family survey"
   opens it with the passage highlighted (the Trace) and adds the evidence card "412 StudyStar customers...", the
   S1 answer, before the inside call. The notes say things a page says about itself are tagged Inside. Seen: drive
   run v-s1-pass1-cite (url /survey, notes ["evidence: The survey behind the 40%..."]). Better: in Pass 1 the survey
   note is tagged Inside (the site describing its own survey), or the cite link counts as a Pass 2 Trace and is
   locked. **family:fact-check**
6. **Focus drops to the page body after Lock my call (Pass 2) and after Retest.** (lockCall, retest handler
   src.html:703-730, 838) Lock is hidden after the second call and Retest focuses the disabled Lock button, so focus
   goes to `<body>`. A keyboard student then tabs through the header, panel, tray and browser to reach Next
   specimen. Seen: v-retest (focus BODY), v-solo2 (focus body after the S3 lock). Better: focus Next specimen when
   the reveal opens, and the first verdict after Retest, with `preventScroll`. **general** (BR1 focus lesson)
7. **The citation links are 24 px tall targets.** ("our 2025 family survey", "A new study") The audit's lead,
   confirmed: 164x24 to 175x25 at every size. These are the Trace controls for S1 and S5. Better: pad the cite
   links to 44 px tall (inline-block with padding) as the tap blocks already are. **family:fact-check**

## Polish

1. **The lab welcome says "Pick a specimen" while S1 is already open, and never says to tap lines.** (L.wLab) A
   solo student hears "Pick a specimen" and looks for something to pick; the notebook (the inside half of the
   evidence) is only explained in its small empty-state text. Better: "Read this page. Tap lines to save them in your
   notebook. Then pick a verdict and press Lock my call. Tap a jar for another specimen." **general**
2. **The Pass 2 hint does not move on.** (L.h2) With Wayfind open and results showing, the hint still says "Press
   the plus for a new tab." Better: once a new tab is open, "Tap a suggestion or a result to read it. Then pick a
   verdict." **general**
3. **Pass 2 can be locked with no outside move at all.** A student can pick a verdict and lock straight away (0 s,
   no new tab), so the outside call is just the inside call again and the counts compare nothing. Better: the first
   time Lock is pressed in Pass 2 with no new tab, lookup or Trace, a one-time hint "You haven't left the page yet.
   Press the plus first, or press Lock my call again to lock anyway." **family:fact-check**
4. **The reveal is the flattest moment.** It gives the verdict and two lines of why, but the student's notebook,
   which they built for a whole pass, plays no part. Better: list the two or three findings that decided it, each
   with its question tag, marked "you found this" when it is in the notebook. (Inside the spec's "two or three lines
   of why"; the integrator may send it to open questions.) **family:fact-check**
5. **At 680x425 and 375 wide the browser chrome eats the page.** The tab strip, the bar (Who runs this site? on its
   own row) and the site masthead leave the headline below the page area's fold; at 375 only the banner shows. The
   tool is playable by scrolling the page, but the specimen is what a student came to read. Better: at those sizes
   a slimmer masthead and the lookup button as an icon in the bar. Seen: default-680x425, h375-p1. **family:fact-check**
6. **Projected, the type is small.** At 1920x1080 the page text and reveal are 16 px, tray labels 12.5 px and
   "Tested"/"New" states 12.5 px bold; from the back of a room the jar states and the reveal table are hard to read.
   Better: scale the page and reveal type with the stage above about 1600 px wide. Seen: reveal-1920x1080. **general**

## Nits

1. "blog" loses its descender in the tray jars at compact sizes (line box clips the g). default-680x425. **general**
2. Jar state "Inside done" truncates to "Inside d..." at 680 and 375. **general**
3. Clear lab's Yes/No step leaves the hint on the lab table line. clear-confirm. **general**
4. The report's "Tabs opened" column is the outside pass only, while the reveal shows tabs for both. Say "Tabs
   (outside)". **general**

## Voice (play-side counts, Sound on, held clicks)

| line | kind | expected | spoken |
|---|---|---|---|
| wLab | welcome | once, on the first tap | once (first tap on jar or page); Read and first tap correct |
| locked | how | once | once in five locked taps (the rest silent or dropped newer); the hint changes at once |
| outside, tools | how | once, on the first lock | once each; dropped stale when the student locks Pass 2 first, correct |
| image | how | once, when a Search this image button is on screen | dropped stale after the student tapped it; spoken later on S3, whose photo has the button (true to the screen) |
| expert | event | every reveal | every reveal; dropped by hush on a mode switch |
| wReport | welcome | once, with rows | once |

The welcome is about 7 s long, so a locked tap in the first seconds waits behind it; the hint shows the line at once.
No stale line at a 0.25 s tap pace (v-fast).

## Teacher projecting

Starts on S1 with the specimen and the three verdicts in view at 1366x768 and 1920x1080; keys 1 to 3 and Enter work.
The class vote works as the teacher's pick. Apart from Should fix 1 (Retest) and Polish 6 (type size), it runs well
from the front.

## Audit pilot

- **Confirmed:** the 24 px cite links (Should fix 7); the tray running off screen at 375 (by design, it scrolls
  sideways, and S3 is cut at the edge as a cue); clipped tab titles and address (ellipsis, expected).
- **Wrong:** every 375 "overlap" (page blocks scrolled inside `.fc-page` counted as overlapping the panel; the
  frames show none) and the 680x425 "below the fold" page blocks (inside the page's own scroll).
- **Missed:** Lock my call below the fold at 375x812 (Should fix 2); hints that name no control (3, 4); Retest
  gaming (1) and the Pass 1 Trace (5), which are past one click; focus lost after the second lock and Retest (6), a
  two-click sequence; the Pass 2 hint that doesn't move on; all feel and projection items.

## Against the Teaching lens (read after the above was written)

Agree on the Pass 1 Trace (their 5, my 5), Retest rewriting the data (their 7b, my 1), "Tabs opened" and the audit's
false 375 overlaps; they rate a Pass 2 lock with no outside move as should fix where I put it at polish 3 (their
grade is the stronger case), and they caught the jar kind labels tracking the answer (both "site" jars are Don't
trust it), which I read as neutral and missed.
