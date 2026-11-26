# Fake or Fact Lab: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Refine

<!-- part: refine.md -->

PASS
Counts: blockers 1 (general 0, family 1), should fix 17 (general 11, family 6), polish accepted 11

### fake-or-fact-lab: Refine

Lens files: refine/teaching.md (T), refine/play.md (P), refine/craft.md (C). Read them for frames, lines and detail.
Teaching checked the Stanford card (Wineburg and McGrew 2019), the three questions, the S1, S3, S4, S5 verdicts and the
report counts: all hold. No rule-5 content and no people pictures, so no sensitivity agent. The shark photo is settled
(Cory, w1-51, "Keep it", 2026-10-27); the spec's open question about it is stale and can be closed.

#### Blockers
1. **Real names cast as bad actors** (T-1, T-6; family:fact-check). "Daily Ledger Now" echoes The Daily Ledger (a real
   Canton, Illinois paper); "BrightPath Apps" matches the real BrightPath Kids; "Willow Creek Middle School" is a real
   school name in three states and the page lists named staff. Done when 6 says no real brand. Rename every
   organization, outlet, school and app to names that are plainly invented, check each with a web search before using
   it (say the searches in handoff.md), and keep every web address on a reserved domain.

#### Should fix
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

#### Polish accepted
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

#### Settled calls
- The shark photo stays (w1-51).
- Item 6 is decided by the integrator under BASELINE; the spec sentences change with it.


#### Exit check, round 1

Cold exit check, 2026-10-28. Bundle `CURIO_DRAFT=1`: 587 KB (601,314 bytes), clean; only the SVG namespace and the
made-up `x.example` template in it; no console errors or warnings in any drive (the host page's favicon 404 only).
Frames and logs in the exit agent's scratch folder `exit-fof` (f1 flow and keys, f2 sizes, f3 375 host, f4 voice).

##### Open

- **E1. voice/lines.json is missing the h1 hint** (should fix; general). `allLines()` returns 20 lines;
  voice/lines.json has 19. Missing: L.h1 "Read this page, and tap lines to save them. Then pick a verdict, and lock
  your call." It is the default screen's hint, so it is what Read speaks most often; once the voice is recorded it
  would have no clip (the bundler's "no recording" list skips it too). handoff.md says the two match. Done when
  voice/lines.json equals `allLines()` word for word.

##### The merged list, re-checked

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

##### Regressions and giveaways

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

##### Voice check (browser voice, held clicks 0.12 s, Sound and Motion on)

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

##### Gate

1. Done when 1 to 8: pass (8 holds with the browser voice; E1 matters once clips are recorded).
2. Codes: AASL Curate IV.B.3, Engage VI.A.3, C3 D3.2.6-8 and W.6.8 to W.8.8 (credibility clause) are taught by the
   two calls, the notebook and the outside tools; notes.md keeps the W.x.8 claim to the credibility clause. Pass.
3. Solo defaults: the made-up line, the verdict meanings, and every waiting moment names its control. Pass.
4. Sensitivity agent: not needed (no rule-5 content, no people pictures). Pass.
5. Open should-fix: E1. **Fails.**
6. Bundle clean, 587 KB, no console errors, no network requests. Pass.
7. Voice counts: right. Pass.

#### Integrator fix (E1)
voice/lines.json gained the missing default Pass 1 hint (L.h1), so it now holds the same 20 lines as `allLines()`.
A one-line data fix, closed by the integrator without another look; handoff.md's claim that the two matched is now true.

<!-- end part -->

<!-- part: refine/craft.md -->

### Craft lens: fake-or-fact-lab (Refine round 1)

Cold read of spec.md, src.html, notes.md, handoff.md, art/prompts.json, voice/lines.json, kit/fact-check.js and
docs/families/fact-check.md (line by line against the engine). Bundled with `CURIO_DRAFT=1` (570 KB, 585,781 bytes).
`audit_tool.py` run first (ports 9970-9971). My own drives on ports 9972, 9974 (my own iframe host served from my
scratch folder, so the tool folder was not touched) and 9976. Frames and logs in my scratch folder `lens-fof-craft`
(`audit/`, `f1` focus and keys, `f2` sizes in four states, `f3` voice, `f4` 375 host, `f5` targets). The engine's pure
part was also run in Node (`pure.js`: 40 searches, 16 reserved-name cases, the world check).

Counts: blockers 0, should fix 8, polish 6, nits 4.

#### Should fix

1. **Focus is dropped to the page body after the main actions.** (general) Seen with real held clicks and
   `document.activeElement` (`f1`, `f5`): after **Lock my call** in Pass 1 the button turns disabled and focus falls to
   `<body>` (lock1b); after Lock in Pass 2 the button is hidden and focus falls to `<body>` while the Expert check
   opens (lock2); **Retest** hides itself and then focuses `#lock`, which is disabled, so focus is lost (retest,
   src.html:838); **Clear lab > Yes** focuses `#clear`, which is now disabled (clear, src.html:843). A keyboard
   student has to Tab from the top of the page each time. BR1 lesson "focus is kept when controls rebuild".
   Better: after an inside lock focus the first verdict (or the `+` now unlocked), after an outside lock focus
   **Next specimen** in the reveal, after Retest the first verdict, after Clear the Lab mode button or the empty
   table's heading.
2. **Enter on a different verdict button locks the old verdict.** (general) src.html:868. Press 1 (Trust it), Tab to
   **Don't trust it**, press Enter: the keydown handler sees a verdict and a `.verdict` target, prevents the button's
   own click and locks **Trust it** (shot enter-change-verdict: `calls: ["trust1"]`, focus on v-dont). The student
   recorded a call they had just tried to change. Lock on Enter only when the focused verdict is the selected one (or
   let Enter on a verdict pick it, and lock only from `#lock` or the body).
3. **375 wide: the page is a 137 px slot and Lock my call is below the fold.** (general) Done when 7. `f4/h-p2-375`,
   `h-p1-375`, audit `size-375x812`: at 375x812 the header wraps to two rows (135 px), the tray, tab strip and the
   two-row address bar leave the page area at y 359 to 496, which shows only the site's own header band and a sliver
   of text; `#lock` is not in view (document 878 px tall); at 375x667 the verdicts are off screen too. The 3-line
   reserved hint also leaves an empty band. The spec asks for page, verdicts and Lock visible at every size and "375
   wide works". Better: icon-only Motion, Sound and Read in one header row under about 480 px (handoff already says
   so), the address bar on one row, a smaller tray (jars 80 px, kind and state on one line), so the page gets
   about 300 px and Lock sits on screen.
4. **Plain plurals and singulars miss in Wayfind.** (family:fact-check) `FC.pure.words` only drops a trailing 's,
   and `search` needs every term word exactly, so each tool must hand-list plural twins (this one did it for
   flood/floods, sunday/sundays, week/weeks, frog/frogs) and still missed some. Node run of `FC.pure.results` on this
   world: "puzzle game", "video game smarter" (S5's key evidence route), "study app", "sharks", "libraries sunday",
   "center for smart studies", "Ms Parks" and "4-day week" all give no results; case is handled ("CENTER FOR SMART
   STUDY" works). Better: fold a plain plural in the engine (drop a final "s" after a consonant other than s, on
   both the query words and the terms; "ies" to "y"), document it in fact-check.md, and drop the twin index entries.
   Siblings then get it for free.
5. **Tap targets and links inside pages are under 44 px.** (family:fact-check) `f5`, audit "small target": the inside
   tap notes on post parts are inline elements, so `.fc-tap{min-height:44px}` does nothing: "@StormWatchNow · 12,400
   followers" is 219x16 (S2's followers card). Inline links: "J. Carter" 58x20 (S4's only Pass 1 route to the author
   page), "A new study↗" 102x23 (S5's Trace), "our 2025 family survey↗" 164x24 (S1's Trace), "See all posts from
   @StormWatchNow" 266x23 (S2). The family doc says "Every target is at least 44 px". Better: in `noteOn`, make an
   inline tap part `display:inline-block` with padding to 44 px; give `.fc-a` in body text vertical padding (or a
   44 px hit area through a `::before`), keeping the text look.
6. **The family doc and the engine disagree in places.** (family:fact-check) BR1 lesson "the family doc matches the
   engine". (a) Doc: every block "may carry `note`, `style` and `cls`"; engine `block()` returns early for `img` and
   `post`, so `style` and `cls` are ignored on both and a block-level `note` on a `post` is silently dropped
   (fact-check.js:603-604). (b) Doc and engine: `maxTabs` is an option, but the default `tooMany` text says "Eight
   tabs is the most" whatever `maxTabs` is (fact-check.js:408). (c) The tap highlight, the "✓ Noted" pill and the
   Inside tag colour are hard-coded to this tool's violet `#6d28d9` (fact-check.js:334-338, 387), so fact-check-desk
   and ad-agency would carry fake-or-fact-lab's brand inside their pages and notebook; the doc says only the
   `--fc-*` chrome variables recolor. (d) Tools hang voice `needs` and CSS on `.fc-newtab`, `.fc-lookup`,
   `.fc-imgbtn`, `.fc-sbox`; only `.fc-sbox` is named in the doc. Better: apply style/cls/note in one place for every
   block, build the tooMany text from `maxTabs`, add `--fc-note` (default the tool's `--brand`) for the tap and
   Inside colours, and list the stable class hooks in the doc. Everything else in the doc checked out line by line
   (below).
7. **The "outside" how line plays after its moment at a 2 s pace.** (general) `f3` run v-2s (vlogs/v-2s.json): lock
   Pass 1, then press `+` 2 s later. "Now leave the page. Press the plus to open a new tab..." queued behind the Lab
   welcome and started at 9185 ms, after the student had already pressed `+` at 6436 ms and was in Wayfind. Its
   `valid` checks the specimen and pass only. Add "only the specimen tab is open" (`browser.tabs === 1`, or no new tab
   opened yet) to `valid`, so it drops once `+` is pressed (the tools and image lines then cover the next step).
8. **The Expert event line is lost at a 2 s pace.** (general) Same run, both specimens tried: the expert line ("Here
   is what the experts found...") queued behind the outside, tools and image how lines and was dropped as `newer` when
   Next specimen came 2.1 s after the Pass 2 lock. STANDARDS: no line is lost at a 2 s pace, and an event line is the
   result the student just earned. At the Pass 2 lock, drop the still-pending Pass 2 how lines (they no longer apply)
   or speak expert with `now`. At a 3.6 s pace it played 5 of 5 (voice table below).

#### Polish

1. **Reveal table cut at the preview size.** (general) `f2/reveal-680x425`: the Experts column is cut at the right
   ("Partly tr") and needs sideways scrolling; it repeats the verdict shown just above. In compact, drop the Experts
   column (or the third row) so the student's own two calls fit.
2. **Jar state "Inside done" truncates to "Inside ..." at 680x425, 800x500 and 375.** (general) `f2/p2-680x425`,
   `f4/h-p2-375`. The state word is the jar's signal. Use "Inside" (or two lines) in compact.
3. **"blog" reads "bloq" in the tray at compact sizes.** (general) audit `size-800x500`, `f2/p2-680x425`: the kind
   line's `overflow:hidden` with line-height 1.15 at 11.5 px clips the descender. Give `.jar span` a line-height of
   1.3 or padding-bottom 1px.
4. **The site's own address is clipped in Pass 1 at 760 to 1000 wide.** (family:fact-check) audit 800x500, 1000x625,
   760x900: "smartstudycenter.examp..." loses ".org"; the locked "Who runs this site? Pass 2" button takes the room.
   The host is a fact the student should read. Let the host win over the button label (icon plus "Pass 2" only when
   narrow).
5. **Reload loses the open pass's seconds and can double a tab.** (general) `save()` runs only on a lock or Clear,
   so a reload in Pass 2 restarts that pass's seconds and tabs from the last save; a specimen begun before another
   specimen's lock is saved with `tabs: 1`, and reopening it after a reload counts its tab again ("2 tabs" for an
   inside read). Save on `visibilitychange` (hidden) and when opening a specimen, and do not recount the specimen tab
   when the slot already has one.
6. **Single words find nothing.** (general) "Gazette", "Vega", "frog", "Bright Path" give no results while
   "Port Alder Gazette", "Marisol Vega", "wood frog", "BrightPath" work. A student who types one name gets the
   no-results line. Add single-word terms for the names ("gazette", "vega", "frog", "bright path").

#### Nits

1. The Lab screen says nothing about storage until the first reveal ("saved on this device only"); the inside lock
   already saves. A small line under Lock my call, or in the pass badge's first lock message, would cover rule 7 at
   once.
2. In the locked search form only the `<form>` gets `aria-disabled`; the input (read-only) and the Search button do
   not, so a screen reader hears a working search box. (family:fact-check)
3. At 760x900 the Report's Clear lab is below the fold under a six-row table (stack). It is not a main control.
4. drive.py has no digit keys in its key map, so verdict keys 1 to 3 had to be sent as page events (Enter was a real
   key). Not a tool problem.

#### Checked and fine

- **Contract:** one file, 570 KB with the four webp photos; no network requests (`performance` resource list empty;
  the only URLs in the bundle are the SVG namespace and the made-up `.example` templates); no console errors or
  warnings in any of my shots or the audit; kit used for voice, tones, motion (no re-implementation).
- **Engine against fact-check.md, line by line:** `FC.pure` hostOf (also `a@b.example`), isReserved (evil.com false,
  `brand.com.example` false, `example.com`, `a.example.org`, `sub.example.net`, `x.example.` true, `x.examples` and
  `xexample.com` false), parseUrl ("/" default, `+` and `%26` decoded), words (lowercase, `'s` and `’s` dropped, little
  words gone), search (all terms, most terms first, then index order), results (each address once), lab;
  `FC.create` opts `services` and `now`; `fc.report` `{bad: [], missing: []}` for this world; `safeDomain`; resolve
  for all service shapes; lock/unlock/locked/locks; note/notes/allNotes/group with `for`; begin/focus/pause/resume/
  setHidden/countTab/seconds/tabs/ms; call (replaces), callOf, calls, clear(g) and clear(), dump/restore; browser
  options `art, chips, noResults, maxTabs, lockLabel, texts` (all 13 keys exist), `onLocked, onNote(note, added,
  tapped), onOpen, onLink, home, focusSearch` and the handle; notebook `{empty, group}`, `refresh(fresh)`, `count`;
  every block type, rich parts, cite/Trace (highlight and "This source doesn't say that."), note tags and `on: 'tap'`
  defaults; one-shot notebook highlight. Exceptions are should-fix 6 above.
- **Report counts:** six tested rows with known calls (`f2/report-*`): "Inside read matched the experts on 1 of 6",
  "Outside read matched on 6 of 6", recomputed by hand from the calls; ✓/✗ marks right on every cell.
- **Saving:** calls survive a reload (persist-a, persist-b: tray reads Tested / Inside done after reload); Clear
  lab > Yes empties calls and storage (`{"calls":[],"notes":[],"T":{}}`) and sets the empty hint; No keeps it and
  returns focus to Clear lab; the try/catch wraps every storage call.
- **Focus kept where the engine rebuilds:** closing tab 3 by keyboard leaves focus on the next close button; selecting
  a tab keeps focus on it; `+` puts focus in Wayfind's box; Hide/Show keeps focus on the toggle; Next specimen
  focuses the new jar; a chip click leaves focus on the page container; nothing takes focus on load.
- **Keyboard paths:** tab order header, panel (verdicts, Lock), tray, browser chrome, page; Enter and Space take a tap
  note once; Enter on the locked `+` and in the locked search box give the locked hint and open nothing; key 2 then
  Enter locks "Partly true" from the body; Enter on a jar opens it and does not lock; the ninth tab shows the
  "Eight tabs" message and opens nothing.
- **Motion off:** audit clean (nothing runs forever); calm shot: the reveal is in place at once, no running
  animations.
- **Sizes:** at 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080 and 760x900, in Pass 1, Pass 2 with tabs,
  the reveal and the Report: no sideways page scroll, verdicts and Lock in view, the hint unclipped, the notebook
  chip and pop-up placed inside the window at 680x425. Only 375 fails (should fix 3).
- **Lines:** the 15 strings in `L` equal `voice/lines.json` word for word and in order; `allLines()` is `V.allLines`.
- **Art:** four `art:` tokens, all in prompts.json, no people. **Words:** no em dashes in src, notes, lines, prompts,
  tool.draft.json, the engine or the family doc; "Curio Class" never "Curio" alone; classroom-safe; storage stated
  in the Report panel and the reveal.

#### Voice check

Driven with `scripts/drive.py`, held clicks (`hold` 0.12), Sound on, Motion on, logs saved from `V.log` to
`f3/vlogs/*.json` (`as` = spoken, silent, dropped, read).

| line | kind | expected | spoken |
|---|---|---|---|
| welcome (Lab) | welcome | 1 | 1 |
| welcome (Report) | welcome | 1 over 5 Report entries | 1 (a pending Lab welcome dropped as stale on a tested specimen: right) |
| locked (tap the locked `+` or search, 6 taps) | how | 1, then silent | 1, then silent 5 |
| outside | how | 1 over 3 specimens | 1, then silent |
| tools | how | 1 over 3 specimens | 1, then silent |
| image | how | 1 where a photo exists | 1; dropped as stale on S1, S4, S5 (no photo; `needs: .fc-imgbtn`): right |
| expert | event | 5 over 5 Pass 2 locks | 5 at a 3.6 s pace; 0 of 2 at a 2 s pace (should fix 8) |
| Read | read | 5 | 5, hint only each time |
| verdict picks, tab opens, notes | none | silent | silent (tones only) |

- **Repeats:** how lines once then silent, the event line five times at a reading pace. Pass.
- **Stale lines:** fast taps (gap 0.2 s) through lock, `+`, Wayfind, then a jar change and Clear: the outside chain
  is dropped on the jar change and expert is dropped on the hush; no line played after its moment in those runs. The
  2 s pace run is the exception: should fix 7.
- **First tap:** the stage gets the welcome in about 130 ms; a jar and the Tab key get the welcome; a tap on the
  locked `+` gets only the locked line, then the welcome once it ends (welcomeAfter); Report with no rows says
  nothing; Read speaks the hint only; Sound says nothing; Sound off then on brings the skipped welcome once. Nothing
  speaks before the first tap. Pass.
- **Read:** cuts the welcome and speaks the hint, also with Sound off; nothing cut Read off; queued how lines are
  hushed and re-offered later; a mode change after Read starts the next line at once. Pass.
- **Order:** spoken lines follow the action order in every run; no older line after a newer one (expert is dropped,
  not played late).
- Every spoken line matched the screen at its time except "outside" in the 2 s run (should fix 7).

#### Audit pilot

`audit/audit.md`, 43 leads, run first on ports 9970-9971.

- **Confirmed:** the small inline link ("See all posts", should fix 5); the 375 problems (should fix 3; but it named
  overlaps, not the real cause, the 137 px page slot and Lock below the fold); the host clipped in the address bar at
  800, 1000 and 760 wide (polish 4); Motion off clean; no console errors; nothing focused on load.
- **Wrong:** "overlaps" at 375 were the page's own content scrolled inside `.fc-page`'s overflow clip; "below the
  fold" at 680x425 were controls inside the page's own scroll box, not the tool's controls; the "clipped" tab title is
  an ellipsis by design; jar text "past the edge" at 375 is the tray's sideways scroll, as the spec asks.
- **Missed:** focus lost after Lock, Retest and Clear (Lock is disabled on a fresh page, so its one held click never
  ran it); the Enter-on-another-verdict bug; plural search misses; the inline 16 px tap notes past the first screen;
  the stale outside line and the lost expert line (its five-click runs never chained lock, `+`, Next at a 2 s pace);
  the doc and engine mismatches; "bloq" and "Inside ..." truncation; the reveal table cut at 680x425; Lock below the
  fold at 375 (it saw only the first screen of the page box).
- **For later lenses:** the script can be trusted for first-screen targets, console errors, Motion and focus on load.
  It cannot yet replace multi-step flows (focus after rebuilds, chained voice), engine checks or reading a scroll box;
  its overlap and fold leads need a second look whenever a tool has its own scrolling pane.

<!-- end part -->

<!-- part: refine/play.md -->

### fake-or-fact-lab: Play lens (Refine round 1)

Cold play, twice: as a grade 6 student alone at home (Sound on, no teacher), and as a teacher projecting it at
1920x1080 and 1366x768. Bundle: `CURIO_DRAFT=1 python scripts/bundle_tool.py fake-or-fact-lab` (570 KB, clean).
Frames in my scratch folder (lens-fof-play/f1 to f5, audit/): default, Pass 1 with notes and a verdict, Pass 2 on
Wayfind results, Pass 2 site lookup, the reveal, the reveal hidden, a six-row report, an empty report, Clear lab
confirm, the notebook pop-up, eight tabs, no results, every specimen's Pass 1, S2 image search, S5 Trace, at
680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x1000 and 375x812 (`drive.py --host`). Held clicks
(0.12 s) at 2 to 5 s gaps and at 0.25 s for the voice runs. Console clean in every shot.

Counts: blockers 0, should fix 7, polish 6, nits 4.

#### Should fix

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

#### Polish

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

#### Nits

1. "blog" loses its descender in the tray jars at compact sizes (line box clips the g). default-680x425. **general**
2. Jar state "Inside done" truncates to "Inside d..." at 680 and 375. **general**
3. Clear lab's Yes/No step leaves the hint on the lab table line. clear-confirm. **general**
4. The report's "Tabs opened" column is the outside pass only, while the reveal shows tabs for both. Say "Tabs
   (outside)". **general**

#### Voice (play-side counts, Sound on, held clicks)

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

#### Teacher projecting

Starts on S1 with the specimen and the three verdicts in view at 1366x768 and 1920x1080; keys 1 to 3 and Enter work.
The class vote works as the teacher's pick. Apart from Should fix 1 (Retest) and Polish 6 (type size), it runs well
from the front.

#### Audit pilot

- **Confirmed:** the 24 px cite links (Should fix 7); the tray running off screen at 375 (by design, it scrolls
  sideways, and S3 is cut at the edge as a cue); clipped tab titles and address (ellipsis, expected).
- **Wrong:** every 375 "overlap" (page blocks scrolled inside `.fc-page` counted as overlapping the panel; the
  frames show none) and the 680x425 "below the fold" page blocks (inside the page's own scroll).
- **Missed:** Lock my call below the fold at 375x812 (Should fix 2); hints that name no control (3, 4); Retest
  gaming (1) and the Pass 1 Trace (5), which are past one click; focus lost after the second lock and Retest (6), a
  two-click sequence; the Pass 2 hint that doesn't move on; all feel and projection items.

#### Against the Teaching lens (read after the above was written)

Agree on the Pass 1 Trace (their 5, my 5), Retest rewriting the data (their 7b, my 1), "Tabs opened" and the audit's
false 375 overlaps; they rate a Pass 2 lock with no outside move as should fix where I put it at polish 3 (their
grade is the stronger case), and they caught the jar kind labels tracking the answer (both "site" jars are Don't
trust it), which I read as neutral and missed.

<!-- end part -->

<!-- part: refine/teaching.md -->

### Teaching lens: fake-or-fact-lab (Refine round 1)

Cold read of spec.md, src.html, notes.md, handoff.md, art/prompts.json, voice/lines.json and kit/fact-check.js; bundled
with `CURIO_DRAFT=1` (570 KB); `audit_tool.py` run first (port 9960); my own drives on port 9962 through `__tool`
(frames in my scratch folder `lens-fof-teaching/f1` to `f5`). Sources checked online: Wineburg and McGrew (2019)
summaries (Stanford repository, Digital Inquiry Group), NPS Denali "Amphibians", and name searches for the invented
brands.

Counts: blockers 1 (general 0, family 1), should fix 8 (general 3, family 5), polish 8, nit 3.

#### What holds up

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

#### Blocker

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

#### Should fix

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

#### Polish

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

#### Nit

18. The spec's Open question on the S2 photo is settled (w1-51, "Keep it"); remove it from the spec. Tag: general.
19. S3's photo shows autumn trees on an article dated February 12, 2026. A file photo is believable, but a winter or
    neutral season would avoid the question. Tag: general.
20. CheckPoint Desk's tagline "A made-up fact-check site" is the only site inside the fiction that calls itself made
    up. Once item 2 adds a lab-wide line, this tagline can go. Tag: general.

#### Frames looked at

`f1/t01-default`, `f2/t02` (S1 inside taps), `t06b` (Openpedia), `t06c` (lookup), `t07`, `t08`, `t09`, `t10` (S2
inside), `t11` (image search), `t12b` (Gazette flood), `t12c` (collage page), `t13` to `t17b` (S3 to S6), `t18`
(Report, six rows), `t20` (reveal), `t21` (empty Report), `f3/t22` to `t27` (Pass 1 links and taps), `f5/t40`, `t41`
(S4 lookup, reload), audit `size-680x425`, `size-375x812 (iframe host)`.

#### Audit pilot

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

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### fake-or-fact-lab: handoff (Refine round 1 fixes, draft)

#### What it is

- `src.html` on the kit starter with `kit:curio` and `kit:fact-check` (the family engine; API in
  docs/families/fact-check.md). Brand `#6d28d9`; `--inside` violet and `--outside` amber tint the two passes.
- Two modes: **Lab** (opens first) and **Report**. The panel is first in the DOM (hint, pass badge, notebook,
  verdicts, Lock my call, or after the reveal Next specimen with a small Retest; the Report's Clear lab).
- Draft: art is the 4 webp files in `art/` (bundled through `art:` tokens); voice is the browser voice
  (`voice/lines.json` matches `allLines()`, 19 lines, not recorded). The art prompts for ff-shark-street (curved fin
  with a dark trailing edge) and ff-library-front (green trees, not autumn) changed in `art/prompts.json`; the webp
  files were not regenerated.

#### Layout of src.html

1. CSS: palette, three layouts (`wide` w>=1000 and h>=650, `compact` w>=640 and w/h>=1.25, else `stack`) and the body
   classes `relayout()` sets: `c300` (panel 300 wide), `nbc` (notebook as a chip that opens `#nbPop`), `narrowb`
   (browser under 600: search box hidden, lookup icon-only, slim masthead), `tinyb` (under 390), `midb` (browser
   under 820: the locked lookup's label hides so the address fits), `tight` (short non-stack: jar drawings hide), `hx`
   (stack under 480: one-row header, emoji-only Motion, Sound, Read, small jars, two-line hint), `big` (wide and
   1600 or wider: larger page, jar and reveal type for projection). Narrow tables (under 560) turn into stacked rows.
2. HTML: header, `#panel`, `#stage` with `#lab` (`#tray` of jar buttons, `#madeup` line, `#bwrap` for the browser,
   `#reveal`) and `#report`.
3. Script: `D` (domains), `SPEC` (S1 to S6: kind, url, expert verdict, why, `key` deciding findings, chips), `WORLD`
   (sites, people, posts, images, Openpedia entries, the Wayfind index built with `ASK()`), `FIND` (note id to note),
   the line table `L`, then state, drawing, flow (`openSpec`, `pick`, `lockCall`, `retest`, `nextSpec`, `setMode`),
   report, keys, `relayout()`, and `window.__tool` (also `rowOf`, `FIND`).

#### The tricky parts

- **Sessions per specimen.** One browser; `state.sessions[S]` holds each specimen's tabs, swapped in with
  `browser.use()`. Retest throws the session away. The specimen's own tab counts once (not again on reopen).
- **First try.** `state.first[S]` keeps a retested specimen's first calls `{c1, c2}`; it is saved inside
  `fofl-table` as `first`. `rowOf(S)` returns the first try (with `retested: true`) when there is one, so the table and
  counts always use the first try. Clear lab empties it.
- **Locks.** Pass 1 locks `newTab, search, image, lookup, leave, trace`; other same-site links work. A locked tap sets
  the `locked` hint and speaks the `locked` how line once.
- **Outside move.** `outsideDone(S)`: a tab opened in Pass 2, or a note that is not an inside note. Lock stays
  disabled in Pass 2 until then (`h2need` hint).
- **Timers.** `fc.begin(S, pass)` on open, `fc.pause()` on Report and after the second call; `visibilitychange`
  pauses too and saves.
- **Voice.** `hint: false` with `read`. Welcomes: `wLab` (only in Pass 1; `welcomeAfter: true`), `wReport` or
  `wReportMore` (untested specimens left). `coachOutside()` queues outside (only while `browser.tabs === 1`, needs
  `.fc-newtab`), tools (needs `.fc-lookup`), image (needs `.fc-imgbtn`, so S2 only); `onOpen` re-runs it so the outside
  item drops once + is pressed. The outside lock calls `V.dropQueued()` before `expert`, so a fast Next specimen
  can't push the expert line out. `expert` is valid only while that specimen is open and tested.
- **Reveal.** Absolute over the bottom of the browser, capped at 85% in stack; Hide/Show. Its deciding-findings list
  comes from `SPEC[S].key` through `FIND`, marked by `fc.notes`. The Fact-checker column hides in compact.

#### Answer key (teacher copy; not in notes.md)

| Specimen | Fact-checker | Deciding findings |
|---|---|---|
| S1 Gloverly Study Institute (gloverlystudy.example.org) | Don't trust it | Openpedia: founded 2024 by Quillbop Apps (maker of Gradewhistle); Glimmerlake Tribune: funded by the app maker; Trace: the "survey" is 412 Gradewhistle customers (lookup: registered 2024 to Quillbop Apps, Inc.) |
| S2 @SquallnookAlerts on Tweedlebeak | Don't trust it | image search: "Street Shark" 2019 collage by Rhea Lind first; Truthlamp Fact Desk; the account names no source (Gazette flood story has no shark) |
| S3 Port Alder Gazette | Trust it | Marisol Vega's staff page (2020 to 2026); council minutes 4 to 1; Glimmerlake Tribune brief agrees (Openpedia: founded 1921) |
| S4 Zapline Now | Don't trust it | lookup 3 weeks ago, owner hidden; J. Carter has no other work; nobody else reports it |
| S5 Pixelpuddle Parent | Partly true, stretched | Trace: the Quellmont Journal study found a small link and says it cannot show cause; Glimmerlake Tribune says the same |
| S6 Ms. Park's Pond Notes | Trust it | Puddlewick Middle School staff page (science teacher, as her About me says); Brambleskip Nature Center; Openpedia wood frog |

#### Name searches (blocker 1)

Every organization, outlet, school, app, handle and site name was web-searched before use. "No match" means no real
organization, product or outlet with that name or a close one turned up.

| Name searched | Result | Decision |
|---|---|---|
| Daily Ledger Now | The Daily Ledger is a real Canton, Illinois paper (teaching lens) | replaced by Zapline Now |
| BrightPath Apps | real BrightPath Kids (teaching lens) | replaced by Quillbop Apps |
| Willow Creek Middle School | real school name in three states (teaching lens) | replaced by Puddlewick Middle School |
| Center for Smart Study | a real "Smart Study" app exists | replaced by Gloverly Study Institute |
| Quillbop | no match | used (Quillbop Apps) |
| Gradewhistle | no match | used (the app) |
| Gloverly | no match | used (Gloverly Study Institute) |
| Zapline Daily, Zapline Now | no match | used (Zapline Now) |
| Puddlewick Middle School | no match | used |
| Squawkle | close to the real Squawki | rejected |
| Tweedlebeak; "Tweedlebeak" app | no match (Tweedle apps are distinct) | used (social site, replaces Chirp) |
| @StormWatchNow | handle not found, but StormWatch is a real app and brand | replaced |
| Gustwhopper | echoes Ghost Whopper | rejected |
| Squallnook | no match | used (@SquallnookAlerts, Squallnook Alerts) |
| Pixel Parent | real Pixel Parents podcast | replaced |
| StudyStar, Chirp | not searched: common real product words, replaced on sight | replaced (Gradewhistle, Tweedlebeak) |
| Pixelpuddle; "Pixelpuddle Parent" | no match (the Pixel Parenting podcast is distinct) | used |
| Journal of Child Learning | close to a real journal | replaced |
| Quellmont | no match | used (Quellmont Journal of Child Learning) |
| Fernhollow Nature Center | real Fern Hollow | rejected |
| Northwoods Nature Center | not searched: a common place-name pattern, replaced on sight | replaced |
| Brambleskip; "Brambleskip Nature Center" | no match | used |
| CheckPoint Desk | not searched: Check Point is a real security company, replaced on sight | replaced |
| Truthlamp; "Truthlamp" fact check | no match (TruthLens is distinct) | used (Truthlamp Fact Desk) |
| Dockfiddle | no match | used (Dockfiddle Hardware ad) |
| Lakeshore Tribune | echoes real papers | replaced |
| Glimmerlake | no match | used (Glimmerlake Tribune) |
| Port Alder, Port Alder Gazette | no match | kept |
| Openpedia | no match | kept |
| Wayfind | only Wayfinder products | kept |
| Rhea Lind | no match | kept |

Every address is reserved (`.example` or `example.org`); `fc.report` and `safeDomain` pass.

#### Refine round 1: what changed, by item

1. Renamed every organization, outlet, school, app and handle (table above); the domains follow the names.
2. A line under the jars: "Every page in this lab is made up for practice. Your calls are saved on this device
   only." (second sentence hidden when narrow); the reveal footer says the same.
3. Each verdict button shows its one-line meaning. S2's why now says the post's news is the shark (so "Don't trust
   it" fits the definition); S5's says a fan blog cheering for games with a real study under it.
4. S6 has an "About me" card ("I teach science at Puddlewick Middle School"), checked by the school staff page; the
   why says so.
5. New engine lock `trace`: cite links (`.fc-citea`) are locked in Pass 1 even on the same site, with the padlock look.
6. Retest keeps the first try in the table and counts, tagged "retested"; Next specimen is the big button after the
   reveal, Retest a small one with "Your first try stays in the lab table."; Pass 2 can't lock before an outside move.
   spec.md Interactions updated.
7. Jar kinds: site, post, news story, news story, blog, blog ("news" when narrow): the Gazette and Zapline Now match.
8. `FC.pure.words` folds plurals ("-ies", final s), the numbers 0 to 12 and apostrophes; punctuation splits words.
   The index gained single-word name terms and plain routes (puzzle, spatial, game study, four day week, library
   Sunday, Ms Park teacher). A probe of plain grade 7 queries finds every key route.
9. 375 wide: one-row header (emoji-only Motion, Sound, Read, 44 px Lab/Report), smaller jars, two-line hint, short
   pass label, the page slot sized so verdicts and Lock are in view at 375x812.
10. Locked line and hint: "That's for the outside read. Pick a verdict, then press Lock my call."
11. Report with untested specimens: welcome and hint add "Press Lab to test the next specimen." (`wReportMore`).
12. Welcome: "Read this page. Tap lines to save them in your notebook. Then pick a verdict, and lock your call. Tap a
    jar for another specimen." (names no disabled control as the next step).
13. Focus: inside lock to `+`, outside lock to Next specimen, Retest to Trust it, Clear lab > Yes to Lab.
14. Enter locks only from the page body, Lock my call, or the verdict already picked.
15. Engine: inline tap notes get `fc-tapi` (inline-block, 44 px box); body links are 44 px inline-block boxes;
    result links 44 px.
16. Engine: `img` and `post` blocks take style, cls and note; tooMany uses `maxTabs`; the violet is `--fc-note`
    (default `--brand`); search button gets aria-disabled; hooks documented. Doc updated in the same change.
17. The outside line is queued only while just the specimen tab is open and is dropped once + is pressed.
18. The expert line survives a 2 s Next: queued how lines are dropped before it.
19. Reveal: "What decides it (your notebook has N of M)" with each key finding marked; the report adds a line that
    reacts to the student's own counts.
20. Wood frog: "In cold winters ... freezes solid. Its heart stops beating. In spring it thaws, and its heart starts
    beating again."
21. ff-shark-street prompt: a curved dorsal fin with a dark trailing edge (art not regenerated).
22. Report column "Tabs opened outside".
23. Each why names the source's purpose (to sell study apps, built to get shares, a fan blog, a paper that reports
    town news); notes.md has the `.org` question.
24. Match tags read "Matches" / "Doesn't match"; ✓ ~ ✗ belong to verdicts only.
25. Welcome no longer says "Pick a specimen" (see 12).
26. Pass 2 hint moves on once Wayfind is open (`h2b`: "Tap a suggestion or a result to read it. Then pick a
    verdict.").
27. Headline in view on arrival at 680x425 and 375x812 (slim masthead in narrow browsers).
28. `big` layout at 1600 and wider: larger page, jar, reveal and made-up line type.
29. Craft polish taken (student-visible only): reveal's Fact-checker column hidden in compact; "Inside" jar state;
   short "Notes: N" chip and "Pass 1: Inside" in compact; "Tested" pass label in compact; jar label line-height 1.3
   (no clipped descenders); the host label wins over the locked lookup label in narrow browsers; the table saves on
   specimen open, on hide and on pagehide; reopening a specimen does not recount its tab; a Clear lab confirm hint;
   the storage line in the Lab; the S3 caption "(file photo)".

#### Checks run (this round)

- Flow test through `__tool` (scratch flow.js): every key finding by chip and by typed plain queries, tags, notes once,
  Pass 1 cite link locked (stays on the page, locked hint), Trace, image search order, lookups, `fc.report`
  `{bad: [], missing: []}`, `safeDomain`.
- Node test of `FC.pure.words` folding ("4-day week", "Ms Parks", "libraries", "class", "bus").
- Size sweep at 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080 and 760x1000 in four states (Pass 1 S1,
  Pass 2 S2 after a search, S4 reveal, report with a retest): main controls in view, no target under 44 px, no
  truncation, no horizontal scroll.
- 375x812 and 375x667 through `drive.py --host` in the same states: all clean (no small targets, no hscroll).
- Voice at a 2 s pace with held clicks: cite link (locked spoken), lock (outside spoken), + then lock and Next
  (tools and image dropped as newer or chain, expert spoken), Report with untested specimens (wReportMore spoken);
  a second run with silent first taps speaks wLab once.
- Focus and Enter check (results in item 13 and 14). Console clean apart from the host's favicon 404.

#### Open

- At 375x667 the page slot is 110 px (verdicts and Lock in view; the headline needs a scroll). 375x812 is clean.
- The two changed art prompts need new images (the webp files still show the older fin and autumn trees).
- Voice is not recorded (draft).

<!-- end part -->

## Log

- 2026-11-25: refine.md folded in (last changed 2026-10-28)
- 2026-11-25: refine/craft.md folded in (last changed 2026-10-28)
- 2026-11-25: refine/play.md folded in (last changed 2026-10-28)
- 2026-11-25: refine/teaching.md folded in (last changed 2026-10-28)
- 2026-11-25: handoff.md folded in (last changed 2026-10-28)
