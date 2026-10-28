PASS
Counts: blockers 1 (general 0, family 1), should fix 17 (general 11, family 6), polish accepted 11

# fake-or-fact-lab: Refine

Lens files: refine/teaching.md (T), refine/play.md (P), refine/craft.md (C). Read them for frames, lines and detail.
Teaching checked the Stanford card (Wineburg and McGrew 2019), the three questions, the S1, S3, S4, S5 verdicts and the
report counts: all hold. No rule-5 content and no people pictures, so no sensitivity agent. The shark photo is settled
(Cory, w1-51, "Keep it", 2026-10-27); the spec's open question about it is stale and can be closed.

## Blockers
1. **Real names cast as bad actors** (T-1, T-6; family:fact-check). "Daily Ledger Now" echoes The Daily Ledger (a real
   Canton, Illinois paper); "BrightPath Apps" matches the real BrightPath Kids; "Willow Creek Middle School" is a real
   school name in three states and the page lists named staff. Done when 6 says no real brand. Rename every
   organization, outlet, school and app to names that are plainly invented, check each with a web search before using
   it (say the searches in handoff.md), and keep every web address on a reserved domain.

## Should fix
2. **Nothing on the Lab screen says the specimens are made up** (T-2; general). A solo student can leave believing the
   four-day-week claim, and the reveal reads as real fact-checker rulings. One plain line on the Lab screen and in the
   reveal ("Every page here is made up for practice").
3. **The three verdicts are never defined** (T-3; family:fact-check). S2's reason says "the flood was real", so
   "Partly true, stretched" is marked no match; S5 is the mirror. Define each verdict on screen (one line each) and
   make S2 and S5 agree with those definitions.
4. **S6's identity check rests on a surname match** (T-4; general). Give the page the evidence the reason claims (she
   teaches, and where), or change the reason.
5. **The Pass 1 trace works for S1** (T-5, P-5; family:fact-check). "our 2025 family survey" goes to a page on the same
   site, so the trace highlights and adds a What's-the-evidence card during the inside read. Inside reads stay inside:
   the citation opens nothing (or says "Save this for the outside read") until Pass 2.
6. **Retest and the outside call can be gamed** (T-7, P-1; general). Integrator call (BASELINE: the data must be the
   student's real first try): Retest keeps the first try in the report and marks the row "retested"; after the reveal
   Next specimen is the main button and Retest secondary; Pass 2 can't be locked until at least one outside move (a
   tab opened). Update the spec's Interactions sentences to match.
7. **Jar labels track the answer** (T-8; family:fact-check). The trusted Gazette is "article", the untrusted look-alike
   "site". Label by what the student can see (or the same word for both).
8. **Search is thin** (T-9, C-4; family:fact-check). `FC.pure.words` drops only 's, so plain plurals and singulars miss
   ("puzzle game", "video game smarter", S5's key route, "study app", "sharks", "libraries sunday", "Ms Parks",
   "4-day week"). Match simple plurals, punctuation and number words, and make sure each specimen's key route is found
   by the plain searches a grade 7 student would type, not only by the chips.
9. **375 wide: Lock my call below the fold** (P-2, C-3; general, BR1 lesson). The page slot is 137 px and the header
   wraps to three rows. Compact header at 375 and a page slot that leaves the verdicts and Lock in view (Done when 7).
10. **The locked hint names no control** (P-3; general). "Make your inside call first." becomes "Pick a verdict, then
    press Lock my call."
11. **Report with specimens still untested doesn't say to press Lab** (P-4; general).
12. **The Lab welcome names Lock my call while it is off** (T polish, builder flag; general, BR1 lesson: no line names
    a disabled control). Reword so the steps are in order without naming a disabled control as the next action.
13. **Focus drops to the page body** (P-6, C-1; general, BR1 lesson). After Lock (both passes), Retest (it focuses the
    disabled Lock, src.html:838) and Clear lab > Yes (src.html:843). Land on the next sensible control.
14. **Enter locks the wrong verdict** (C-2; general). Pick one verdict, Tab to another, press Enter: the first gets
    locked (src.html:868).
15. **Tap notes and citation links under 44 px** (P-7, C-5; family:fact-check). Inline links 20 to 24 px tall, the
    followers note 16 px; `.fc-tap` min-height does nothing on inline elements. Use padding or inline-block.
16. **Engine and doc disagree** (C-6; family:fact-check). `block()` ignores style and cls on img and post and drops a
    post note; tooMany always says "Eight tabs"; this tool's violet is hard-coded in the engine (move it to a CSS
    variable); document the `.fc-newtab`, `.fc-lookup`, `.fc-imgbtn` hooks.
17. **The outside line plays after the student pressed +** (C-7; general). Valid only while just the specimen tab is
    open.
18. **The expert event line is lost at a 2 s pace** (C-8; general). 0 of 2 at 2 s, 5 of 5 at 3.6 s. An event line
    must survive the next Pass 2 how line (how lines give way to it, or it plays before them).

## Polish accepted
19. The report reacts to the student's own data (one line on their inside vs outside matches) and the reveal mentions
    their notebook (T, P).
20. The encyclopedia's wood frog doesn't "come back to life": it survives being frozen and thaws (T).
21. The shark fin reads less like a smooth cone (T, placeholder-independent shape only).
22. "Tabs opened" column label in plainer words (T).
23. The reveal names each source's purpose; the teacher notes point out the .org trap (T).
24. The ✗ mark means one thing in the table (T).
25. The welcome doesn't say "Pick a specimen" while S1 is open, and says to tap lines into the notebook (P).
26. The Pass 2 hint moves on once Wayfind is open (P).
27. At 680x425 and 375 the specimen's headline is in view on arrival (P).
28. At 1920x1080, larger page text and jar labels for projection (P).
29. Craft's polish items that touch only what the student sees, as the builder judges (list them in handoff.md).

## Settled calls
- The shark photo stays (w1-51).
- Item 6 is decided by the integrator under BASELINE; the spec sentences change with it.


## Exit check, round 1

Cold exit check, 2026-10-28. Bundle `CURIO_DRAFT=1`: 587 KB (601,314 bytes), clean; only the SVG namespace and the
made-up `x.example` template in it; no console errors or warnings in any drive (the host page's favicon 404 only).
Frames and logs in the exit agent's scratch folder `exit-fof` (f1 flow and keys, f2 sizes, f3 375 host, f4 voice).

### Open

- **E1. voice/lines.json is missing the h1 hint** (should fix; general). `allLines()` returns 20 lines;
  voice/lines.json has 19. Missing: L.h1 "Read this page, and tap lines to save them. Then pick a verdict, and lock
  your call." It is the default screen's hint, so it is what Read speaks most often; once the voice is recorded it
  would have no clip (the bundler's "no recording" list skips it too). handoff.md says the two match. Done when
  voice/lines.json equals `allLines()` word for word.

### The merged list, re-checked

1. **Blocker 1, names: closed.** No old name is left in src, notes, spec, lines, prompts or tool.draft.json (only
   `site:'chirp'` as a field value in the spec's engine example). My own web searches: Gloverly, Quillbop,
   Gradewhistle, Tweedlebeak, Squallnook, Truthlamp, Glimmerlake, Zapline and "Zapline Now", Pixelpuddle,
   Puddlewick, Brambleskip, Quellmont, Dockfiddle, Port Alder (town and Gazette), Openpedia, Rhea Lind: no real
   organization, outlet, school, brand or artist (only loose echoes: Gloverall coats, Glimmerglass, Puddle Lane,
   Bramble Bank). The four names replaced unsearched (StudyStar, Chirp, Northwoods Nature Center, CheckPoint Desk)
   are gone, and their replacements (Gradewhistle, Tweedlebeak, Brambleskip, Truthlamp) have no match. Wayfind: one
   search summary named a small Melbourne consultancy "Wayfind" from a CB Insights listing, which two follow-up
   searches could not confirm; the only firm hits are Wayfinder products. Not a search brand, and it is cast as the
   neutral search tool, so not a blocker. Every address is reserved.
2. Made-up line: under the tray at every size (storage sentence drops when narrow) and in the reveal footer. Pass.
3. Verdict meanings show under each word at every size, including 375; the S2 and S5 whys fit them. Pass.
4. S6's About me card names Puddlewick Middle School; the staff page confirms it. Pass.
5. Pass 1 cite link: padlocked "Pass 2", 244x50; a click keeps the page, adds no card, sets the locked hint. Pass.
6. **Retest and the outside call: pass.** Retest after the reveal, then two "Trust it" calls on S1 (fact-checker:
   Don't trust it): the row and the counts keep the first try, tagged "retested", with "A retested row shows your
   first try."; a second Retest still keeps the first try. Pass 2 with a verdict picked and no outside move: Lock
   disabled, hint h2need; `lockCall()` and Enter from the body record nothing; an inside tap note does not unlock it;
   a Trace, a new tab or a lookup does. Notes are kept per specimen, so another specimen's outside find can't unlock
   it. Next specimen is the big button, Retest small with its line. spec.md Interactions match.
7. Jars: site, post, news story, news story, blog, blog ("news" when narrow). Pass.
8. **Search: pass.** 60 plain queries (10 per specimen) through the tool's own index: every key route is found by
   several plain queries a grade 7 student would type ("study apps", "who owns gloverly", "sharks", "is the shark
   photo real", "libraries sunday", "Marisol Vega", "4-day week", "J Carter education reporter", "video game
   smarter", "do video games make you smarter", "Ms Parks", "frozen frogs"). Misses, left as polish: "Port Alder
   library", "port alder town council", "school week next fall", "games and brains", "are video games good for
   kids".
9. 375x812 (`drive.py --host`): one-row header, verdicts and Lock in view, page slot 255 px with the headline in
   view, no small targets, no sideways scroll. 375x667: verdicts and Lock in view, page slot 110 px (the headline
   needs a scroll; known in handoff, polish). Pass.
10. to 12. Locked line and hint, Report "Press Lab to test the next specimen.", welcome wording: pass.
13. Focus (real input): inside lock to `+`, outside lock to Next specimen, Retest to Trust it, Clear lab > Yes to
    Lab. Pass.
14. Enter (real keys): pick Trust it, Tab to Partly, Enter picks Partly and records nothing; Enter again locks
    Partly. Pass.
15. Targets: every link and tap note in all six specimens, S2's profile, S4's author page, Wayfind home and results
    is 44 px or more; no target under 44 px at any size in four states. Pass.
16. fact-check.md against kit/fact-check.js: fold rules, the `trace` lock, `fc-tapi`, `--fc-note`, `maxTabs` in
    tooMany, `img` and `post` style, cls and note, the stable hooks: all match. Pass.
17. and 18. Voice: below. Pass.
19. to 29. Reveal "What decides it (your notebook has N of M)" with marks; the reacting report line; the wood frog
    thaws; "Tabs opened outside"; whys name purpose; "Matches" and "Doesn't match"; h2b; headline in view at
    680x425; `big` at 1920; compact words. Pass (two art prompts changed, images not yet redrawn, as expected).

### Regressions and giveaways

- Sizes 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080 and 760x1000 in Pass 1 S1, Pass 2 S2 after a
  search, the S4 reveal and a Report with a retest, plus the notebook pop-up at 680x425: no sideways scroll, hint
  never clipped, verdicts and Lock (or Next specimen) in view, no target under 44 px, Clear lab in view. At 375 the
  Report's Clear lab is below the fold under the table (not a main control).
- No cheap verdict: the three verdict buttons are the same size and text on every specimen; jar kinds don't track
  the answer; chip counts (2 or 3) don't either. One weak pattern, polish only: the site lookup has a record only
  for S1 and S4 (both Don't trust it); the others say "No lookup record". A record for the Gazette (an old
  registration to the paper) would make the lookup a real test both ways.
- Polish, not blocking: after a lookup the Pass 2 hint says "Tap a suggestion or a result to read it." while the
  lookup card shows (h2b is picked by tab count, not by Wayfind being open); a Trace-only outside pass shows 0 tabs
  in the table; the reveal footer says "Added to your lab table" on a retest, where the table keeps the first try.

### Voice check (browser voice, held clicks 0.12 s, Sound and Motion on)

Runs: five specimens at a 2 s pace (pick, lock, +, pick, lock, Next), five locked taps plus the locked lookup, five
Report and Lab switches, a 0.2 s fast run through lock, +, a jar, Report and Clear lab > Yes, first taps (stage,
Read, Sound off and on, Report with no rows, the Tab key, a jar, the locked +), and Read during the welcome with
Sound on and off.

| line | kind | expected | spoken |
|---|---|---|---|
| wLab | how (welcome) | 1 per load | 1 in every run |
| locked | how | 1 over 6 locked taps | 1, then silent or dropped (newer) |
| outside | how | 1, only while just the specimen tab is open | 1 (S2); on S1 dropped as newer when + came first; silent after |
| tools | how | 1 | 1 (S3); dropped as newer by the outside lock on S1 and S2 |
| image | how | only while a Search this image button shows | 0: dropped as stale each time (+ already pressed), right |
| expert | event | 5 over 5 reveals at 2 s | 5 of 5 |
| wReportMore | how (welcome) | 1 over 5 Report entries | 1 |
| read | read | each press | 3 of 3, hint only, also with Sound off |

- First taps: the stage, a jar and the Tab key get wLab within about 150 ms; Read speaks the hint only; Sound says
  nothing and Sound back on brings the skipped welcome once; Report with no rows says nothing (no rows, by design);
  the locked `+` gets only the locked line, then wLab after it.
- Stale lines and order: in the 0.2 s run every queued line was dropped (newer) once its moment passed; nothing
  played late; spoken lines follow the order of the actions.

### Gate

1. Done when 1 to 8: pass (8 holds with the browser voice; E1 matters once clips are recorded).
2. Codes: AASL Curate IV.B.3, Engage VI.A.3, C3 D3.2.6-8 and W.6.8 to W.8.8 (credibility clause) are taught by the
   two calls, the notebook and the outside tools; notes.md keeps the W.x.8 claim to the credibility clause. Pass.
3. Solo defaults: the made-up line, the verdict meanings, and every waiting moment names its control. Pass.
4. Sensitivity agent: not needed (no rule-5 content, no people pictures). Pass.
5. Open should-fix: E1. **Fails.**
6. Bundle clean, 587 KB, no console errors, no network requests. Pass.
7. Voice counts: right. Pass.

## Integrator fix (E1)
voice/lines.json gained the missing default Pass 1 hint (L.h1), so it now holds the same 20 lines as `allLines()`.
A one-line data fix, closed by the integrator without another look; handoff.md's claim that the two matched is now true.
