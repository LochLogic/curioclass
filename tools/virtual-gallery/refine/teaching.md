# Teaching lens: virtual-gallery (round 1)

Cold Teaching lens, 2026-11-05. Read spec.md, src.html, notes.md, tool.draft.json, the shared audit
(`S:/CurioClass-codex-scratch/virtual-gallery/audit-r1/audit.md`). Not a Curiosity (lesson norms apply). Own checks
ran through `scripts/drive.py` on the built bundle (port 9801), scripts and frames in
`S:/CurioClass-codex-scratch/virtual-gallery/teaching/` (`t1.js`, `t2.js`, `t3.js`, `f/*.png`).

Second sources, read for this lens: the Smithsonian Guidelines for Accessible Exhibition Design PDF (text extracted
locally) and the NCAS Visual Arts "at a glance" PDF (2021 rev., text extracted locally) for the HS performance
standards under VA:Pr4, Pr5, Pr6.

## Findings

### 1. VA:Pr6 is mentioned, not taught at the high school level (should fix, general)
- Where: module `arts-9-12-portfolio-and-curation` (VA:Pr4;VA:Pr5;VA:Pr6), notes.md "Standards and sources"; this is
  the only tool on the module (`data/tools-concepts.csv:207`), so nothing else covers the code.
- What: the HS performance standards under Pr6 are all about the exhibition's effect on viewers: Pr6.1.Ia "Analyze
  and describe the impact that an exhibition or collection has on personal awareness of social, cultural, or political
  beliefs and understandings", IIa "Make, explain, and justify connections between artists or artwork and social,
  cultural, and political history", IIIa "Curate a collection ... to impact the viewer's understanding of social,
  cultural, and/or political experiences". The tool's Pr6 activities are a tag-based Flow check and a statement whose
  meaning is never looked at ("Format checked; review the meaning yourself"). Nothing asks what a visitor will come
  away understanding, and the Walk never compares the visitor's experience with the curator's intent beyond the
  First seen work. The notes' claim ("VA:Pr6 is practiced through arranging a visitor sequence, writing a statement,
  and revising the show after walking it") describes the anchor wording, not the 9-12 standard.
- How seen: NCAS at-a-glance PDF text; src.html `checks()` (lines 810 to 816); cheap-pass run below.
- Better: a real activity, not a thin one (BASELINE rule 2): before Walk, the curator writes one line "A visitor
  should leave understanding ..." (Where I'm From is a natural fit: a neighborhood, a family routine, a community);
  the walk ends on that line beside the order strip and asks which stops carried it and which jump broke it, and the
  printed sheet keeps it. Otherwise move Pr6 off the module to a tool that teaches exhibition impact (gallery-critique
  or the art-museum family) and say so.

### 2. Selection (VA:Pr4) reduces to matching lime tags; nothing asks the student to justify a choice (should fix, family:none / general)
- Where: Select mode, `tagsHTML()` (src.html:663, `.tag.match` lime highlight), Theme check (src.html:789).
- What: HS Pr4 asks students to "analyze, select, and critique" (IIa) and "critique, justify, and present choices"
  (IIIa). The tool pre-tags every work and highlights the tag that matches the brief, and the Theme check counts those
  tags, so a student passes Theme by picking lime chips without looking at a single picture. The key skill "Choose
  works for a theme and explain the exceptions" (notes.md) has no place to explain anything: a work without the tag
  joins silently, and the Water brief, which needs one such work, never asks why.
- How seen: t1.js cheap run (6 home-tagged works, nothing read) passes Theme; `tagsHTML()`.
- Better: hide the tags until the student has chosen (or let the student tag works, then compare with Jordan's
  tags), and give every chosen work without the theme tag a one-line "why it belongs" box that the Theme check needs
  before it ticks; print those lines on the sheet. That is the "justify" in the standard.

### 3. All nine checks tick with no writing beyond one character (should fix, general)
- Where: Labels check (src.html:806 to 809), Statement check (src.html:810), Anchor check (src.html:792).
- What: the REFINE cheap-way test. Choose the six home works, Hang on wall six times, Auto space, light each, star
  whatever Walk names First seen, type "x" as the statement: 9 of 9 met, "Every measured check is ticked" plays.
  Labels passes with every note blank and every title untouched (Jordan's titles are pre-filled), so the key skill
  "Write concise labels ... for an audience" is never exercised; the 25-word limit only ever bites a student who
  chose to write. The statement check accepts "x". The anchor can be starred after Walk has named the first-seen
  work, so it is never a prediction (the notes' key skill "Predict what a visitor notices first" has no predict step).
- How seen: t1.js `cheap` = all nine `true`; `untouchedLabels: true`; `stX: true`. The checklist and allTicked line
  are honest that meaning is not checked, which keeps this from being a blocker.
- Better: Labels needs at least one written note per work (the brief can still allow short ones); the statement
  needs a minimum (for example 2 sentences or 20 words) before Format can tick; lock the star once Walk has been
  entered with a hung show, or record "starred before the walk" vs "after" in the Anchor line so the prediction is
  visible.

### 4. The 145 cm default center line has no source, and the cited source says something different (should fix, general)
- Where: `fresh()` src.html:632 (`lines` default 145), shown on every wall ("145 cm · 57.1 in"), Line check
  (src.html:796) and its Why.
- What: STANDARDS "Facts": every number on screen has a source in the spec. The spec gives only the slider range
  (120 to 170); 145 cm appears nowhere in Sources. The one cited source, Smithsonian section II.A, says "Mount small
  items (to center line) at no higher than 1015 mm (40 in.)", and most of Jordan's works are small. The Line check
  then passes at any height (all walls at 120 cm pass, t1.js `lineAt120: true`), so the slider teaches only "make the
  walls match", not where a center line belongs for seated and standing visitors, which is the Pr5.1.IIa idea
  ("methods ... appropriate to display artwork in a specific place").
- How seen: t1.js; Smithsonian PDF text (section II.A, and section III wall labels).
- Better: source the default (the common 57 to 60 in / 145 to 152 cm gallery practice needs a named source in the
  spec), say in the Line Why that it is a standing-eye practice and that the guide sets small items lower for seated
  visitors, and let the seated band matter: a short note when a wall's line leaves every frame above the band.

### 5. Seated eye level is a wheelchair-user average, shown as all seated visitors (nit, general)
- Where: Hang panel muted line ("Faint wall band: seated eye level, 109 to 130 cm"), spec Rules.
- What: the guide gives 1090 to 1295 mm (43 to 51 in) as the average eye level of "A male adult who uses a
  wheelchair". The tool's numbers match (130 is 129.5 rounded); notes "Teaching with care" already says it is a design
  reference. On screen, "wheelchair user's eye level" would be more exact.

## Done when (spec), tested

| # | Result | How |
|---|---|---|
| 1 | Pass. Counts home 6, water 5, city 5, growing 4, night 2. Hint shows the themeShort text for growing and night only. Voice log shows growing as `themeShort` (silent, "early", n 2); the night line did not get its own log entry, so whether night is ever heard is a lead for Craft | t1.js `tags`, t2.js |
| 2 | Not mine (Play/Craft); place() pushes frames apart and keeps them off corners in my runs | t1.js |
| 3 | Pass on three layouts: back wall full (creek, centered), back wall empty (tomatoes, the side-wall frame nearest the back corner), anchor on a side wall only wins once the back wall is empty or its works sit at the corners, as the spec rule implies | t1.js `fs*` |
| 4 | Pass: spacing 14.29% pass, 16.54% fail, 29 cm gaps fail; 25-word note pass, 26 fail; 100-word statement pass, 101 fail; 26-word sentence fail; blank title fails | t1.js |
| 5 | Pass: tray order, label large and readable at the stop, word count and 137 cm shown | `f/walk-stop3.png` |
| 6 | Timing readout 3 s per stop (7 stops, 21 s), matches the 24 s for 8 | `f/walk-stop3.png` |
| 7 to 12 | Play/Craft; not re-checked | |

## Facts spot-checked against a second source

Smithsonian PDF (extracted text): labels 1220 to 1675 mm / 48 to 67 in, centerline 1370 mm / 54 in, seated
1090 to 1295 mm / 43 to 51 in, sentences no more than 25 words, labels 75 to 100 words: all match screen and notes
(notes correctly explain 168 cm is 66.1 in). Room arithmetic (340 cm each side of the door), frame size +16 cm,
spacing percentages, tag counts and the 3 s per stop all recomputed and correct. NCAS anchor wording for 4, 5, 6
matches the spec's glosses; the HS performance standards are what finding 1 and 2 are judged against.

## Grade fit, notes and guardrails

Language is right for 9-12. "Support at home" ideas are doable tonight. "Talk about it" questions are good and
tool-specific. "Teaching with care" names the personal side of Where I'm From and that nobody needs to upload
family photos (rule 8 met). No points, timers or hard history.

**For the sensitivity agent:** nothing cultural, Native or hard-history. Where I'm From invites personal and family
stories (handled in notes); no review needed in my view, flagged only so the integrator can decide.

## Audit pilot

- Confirmed: Checklist "choices cut short by a scroll panel" at 1366x768: only Selection, Theme, Anchor and half of
  Line show; five of nine checks and their Show me buttons are below the fold of an inner scroll panel
  (`audit-r1/state-mode-04checklist-1366x768.png`). For teaching this matters: the student reads a third of the
  juror's list. (Play/Craft own the fix.)
- Not checked by me: the label-open / statement-open / clear-confirm "#hint covered" rows (a modal over the footer is
  expected) and the `#add-work` "welcome not heard" row (Play/Craft).
- Missed by the audit (it cannot see these): the cheap all-ticks path (finding 3), the tag giveaway in Select
  (finding 2), the unsourced 145 cm default (finding 4), Pr6 coverage (finding 1). Also seen on my own frame: in Walk
  the large visitor-label inset sits over the right half of the wall label it is quoting (`f/walk-stop3.png`), a Play
  item.
