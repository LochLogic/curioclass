# Phase 0: Plan, Name, Verbiage, Structure

Status: DRAFT for Cory's review, 2026-10-22.
Scope: Phase 0 only. Phases 1-3 are listed at the end so the structure is built to receive them.

---

## 1. What the two concept pieces tell us (the house style)

| | State Quest | The Elements Inspector V2 |
|---|---|---|
| Subject / grade | Social studies (geography), roughly 3-8 | Science (chemistry), roughly 6-12 |
| Form | Game with modes (Practice, Challenge with 3 lives) | Explorer / reference with a 3D model, search, spectra |
| Size | 127 KB | 792 KB (bundles Three.js r128, MIT) |
| Network | None. Fully offline | None. Fully offline |
| Accessibility | Focus rings, 44px targets, keyboard | Skip link, aria labels, keyboard, sr-only text |
| Docs | Roadmap comment in the file, data source cited (US Census, public domain) | License notice for bundled library |

These already set a strong standard. Make it the rule for every item:

1. **One file, works offline.** A teacher can download it, put it on a USB stick, run it on a locked-down school Chromebook, or project it with no internet.
2. **No accounts, no tracking, no ads, no data leaves the page.** This is also what makes it safe under student privacy laws (COPPA, FERPA, state laws) with zero paperwork for the school.
3. **Accessible by default** (WCAG 2.2 AA target): keyboard, screen reader labels, color is never the only signal, 44px tap targets.
4. **Sourced and licensed.** Every data source cited, every bundled library's license kept.
5. **Two modes where it fits:** a no-pressure Practice mode and a Challenge mode.

---

## 2. Name

The brand does not do the SEO work; page titles do ("Periodic Table Explorer, Free Interactive, Grades 6-12"). So the name should be short, memorable, friendly to teachers, and say "free + hands-on".

Shortlist (domains NOT checked yet, that is the next step):

| Name | Why | Risk |
|---|---|---|
| **Open Bench** (recommended) | A lab bench, a workbench: hands-on things you pick up and use. "Open" says free and open. Works for K and for AP Chem. | Generic word pair, may need openbench.education / .org |
| Free Range Class | Playful, says free, says roam around | Slightly jokey for a district IT approval list |
| Chalk & Spark | Classroom + spark of interest | Longer, ampersand is awkward in URLs |
| Pocket Lab | Small, portable, one-file tools | Existing commercial "PocketLab" sensor company, avoid |
| Kit Shelf | Shelf of ready kits | Less distinctive |

Superseded 2026-10-22: Cory wants a fun name. Finalists: **Hall Pass** (Cory leaning), **Free Period**, **Snow Day**.

Cursory availability (2026-10-22, registry lookups only, not a trademark search):
- Hall Pass: hallpass.com/.org/.app/.school taken; hallpasstools.com free. "Hall pass" is an established school-software category (Securly e-hallpass, Infinite Campus Hall Pass, Navigate360 Hall Pass), so search and trademark collisions are likely in our exact market.
- Free Period: .com/.org/.app taken; no edtech product found using the name.
- Snow Day: .com/.org taken; snowdaylearning.com free; name is crowded by snow-day predictor apps.
- .education lookups did not resolve (likely available, unconfirmed).

**Chosen 2026-10-22: Curio Class (curioclass.org).** Deeper check:
- curioclass.org: not registered (registry returns "Object not found", no DNS). Cory to buy it.
- curioclass.com: registered since 2021 (GoDaddy nameservers, renews 2027-03), no live site. curioclass.net / .education appear free (DNS only).
- Same name in use, other fields: CurioClass Jewellery (curioclass.cc), Curio Class UK corporate cohort training (curioclass.co.uk, site currently down).
- Many "Curio" kids/learning apps exist (CurioKids AI, Curio XR, CurioHeads, Jovia "Curio" finance app, EU CURIO toolkit). None named Curio Class.
- Trademarks (via aggregators, unverified on USPTO TSDR): CURIO 98619827 pending, class 41, VR/AR education instruction; CURIOXR pending class 41; CURIOTECH class 41; CURIO CABINET 87584802 educational web content (status unknown); CURIO class 28 toys registered. No found "CURIO CLASS" mark.
- Risk read (not legal advice): "Curio" alone is crowded in education; the full "Curio Class" is not. Always brand as the two-word name, never "Curio" alone.

## 2b. Design direction (agreed 2026-10-22)

- Simple static backend; the look comes from a design system, not the stack.
- Site shell is grown-up and clean (museum/editorial feel) so high schoolers take it seriously.
- The fun lives in the moment a tool opens: a short reveal animation and optional bell sound (off by default).
- Grade-band skins inside tools, same layout and controls:
  - K-2: **teacher led.** Designed for the teacher driving on a projector or smartboard while kids watch and call out answers. Very large visuals, bright colors, celebrations visible from the back of the room, read-aloud, controls sized for an adult at the board, nothing a child must read alone to proceed.
  - 3-5: colorful, more text, light game elements, students may drive.
  - 6-8: cleaner, scores and streaks.
  - 9-12: sleek "pro instrument" feel (like Elements Inspector).
- One shared starter template carries the opening animation, skins, accessibility, and Practice/Challenge modes.

---

## 3. Verbiage (our words for our things)

Pick one word per concept and never drift. Teachers search for "interactive", "activity", "game", "simulation", so those stay in titles and descriptions even though our internal unit name is different.

| Concept | Our word | Definition | Example |
|---|---|---|---|
| One interactive file | **Tool** | A single self-contained, offline interactive | State Quest, Elements Inspector |
| Kind of tool | **Tool type** | Game, Explorer, Simulator, Builder, Quiz, Visualizer, Timeline, Lab | State Quest = Game; Elements = Explorer |
| Topic a tool teaches | **Module** | A unit of curriculum within a subject and grade (Phase 1 builds this list) | "US states and regions", "Periodic table" |
| Broad area | **Subject** | Math, ELA, Science, Social Studies, Arts, Health/PE, Computer Science, World Languages, CTE | |
| Grade | **Grade** / **Grade band** | K, 1...12; bands K-2, 3-5, 6-8, 9-12 | |
| Play setting inside a tool | **Mode** | Practice (no pressure) and Challenge (scored) | State Quest's two modes |
| Standard alignment | **Standards** | Codes the tool supports (CCSS, NGSS, C3, state) | NGSS HS-PS1-1 |
| Page for a tool | **Tool page** | Landing page: play button, download, teacher notes, standards | |
| Teacher-facing guide | **Teacher notes** | 1 page: objective, 5-min intro, 3 discussion questions, extension | |
| Release maturity | **Status** | Concept, Beta, Ready, Retired | Both current pieces = Beta |

Voice rules for site copy:
- Plain, warm, short. Write for a tired teacher at 9pm planning tomorrow.
- Lead with what the student does ("Click a state, name it"), not features.
- "Free" means free: no "freemium", no "sign up to unlock". Say it once on each page, plainly.
- No em dashes (house rule).

Core copy (draft):
- Hero: **"Hands-on lessons for every grade. Free forever, no sign-up."**
- Sub: "Interactive tools you can project, share, or download. They work offline and never collect student data."
- Promise strip: "No accounts. No ads. No tracking. Works offline. Yours to use, share, and adapt."

---

## 4. License

- Tools and site content: **CC BY 4.0** (anyone can use, share, adapt, even sell copies; must credit). Teachers and districts trust CC.
- Code inside tools: **MIT**, so others can fork and improve.
- Alternative if you do not want others reselling: CC BY-NC-SA 4.0. Tradeoff: NC limits some districts and nonprofits. Recommend CC BY.

---

## 5. Site outline (information architecture)

```
/                          Home: hero, search, browse by grade, browse by subject, newest tools
/grades/                   K | 1 | 2 ... 12, and grade bands
/grades/5/                 All grade 5 tools, grouped by subject
/subjects/                 Subject list
/subjects/science/         Subject landing, grouped by grade band then module
/subjects/science/grade-8/ Modules for that subject + grade
/tools/                    Full catalog with filters (grade, subject, tool type, standard)
/tools/state-quest/        Tool page (see template below)
/tools/state-quest/play/   Full-screen tool (the actual HTML file)
/standards/                Browse by standard code (big SEO surface)
/standards/ngss/hs-ps1-1/  Tools that support this standard
/teachers/                 How to use: projecting, Chromebooks, offline/USB, LMS embedding
/about/                    Mission, why free, who makes it, how it is funded (or not)
/privacy/                  Short and literal: we collect nothing from students
/accessibility/            Our standard and how to report problems
/license/                  CC BY 4.0 / MIT explained in plain words
/request/                  Teachers request a tool or report a bug (simple form, no account)
/sitemap.xml, /feed.xml
```

**Tool page template** (every tool, same order):
1. Title + one-line "students will..." outcome
2. Big Play button, then Download (single .html), then Embed code (iframe)
3. Grades, subject, module, tool type, time needed (5 / 15 / 30 min)
4. Screenshot or short looping preview
5. Teacher notes (objective, intro script, discussion questions, extension)
6. Standards supported
7. Sources and credits, license
8. Related tools (same module, adjacent grades)

---

## 6. Being found (the "business" part)

- **SEO:** one page per tool, per module, per standard, per grade-subject pair. Titles match what teachers type: "free interactive periodic table for middle school". Schema.org `LearningResource` markup with `educationalLevel`, `teaches`, `educationalAlignment`, `isAccessibleForFree: true`.
- **Teacher channels:** OER Commons, PBS LearningMedia style directories, Merlot, state OER repositories, Teachers Pay Teachers free listings (pointing back to us), r/Teachers and subject subreddits, Facebook teacher groups, ed Twitter/Bluesky.
- **Distribution:** "Add to Google Classroom" link, embed code for Canvas/Schoology, downloadable zip per grade.
- **Trust signals:** no-tracking promise, accessibility statement, cited sources, teacher notes. These are what get a site onto a district's approved list.
- **Measurement without tracking students:** server-level request counts only (Cloudflare analytics, no cookies). No per-user analytics.

---

## 7. Tech structure (proposed)

- Static site on Cloudflare Pages (same pattern as Burn N Build). Zero server cost at this scale.
- Static site generator: **Eleventy** (small, single-purpose, just builds HTML from data). Lightweight-tools preference.
- Tools stay plain single HTML files. The site wraps them; it never changes them.
- Catalog driven by data files, so Phase 1 and 2 feed the site directly.

Repo / folder layout:
```
S:\CurioClass\
  docs\                           plans, voice guide, decisions log
  data\
    subjects.csv                  subject list
    grades.csv                    K-12 + bands
    modules.csv                   Phase 1: one row per module (grade x subject x topic)
    standards.csv                 Phase 1: standard codes
    tools.csv                     Phase 2/3: one row per tool, links to modules
  tools\
    state-quest\  state-quest.html, notes.md, meta.json, preview.png
    elements-inspector\ ...
  site\                           Eleventy source (templates, pages)
  templates\tool-starter.html     blank tool with house style, a11y, modes baked in
```

**Data schema (so Phase 1 has a target):**
- `modules.csv`: module_id, subject, grade, title, description, standards (codes, semicolon-separated), source
- `tools.csv`: tool_id, title, tool_type, module_ids, grades, status, file, size_kb, offline (y/n), license, sources

---

## 8. Phase 0 checklist

- [x] Review concept pieces, derive house style
- [x] Draft name shortlist, verbiage, voice, license, IA, SEO plan, tech structure
- [x] Name: Curio Class; license CC BY 4.0 (content) + MIT (code)
- [x] Domain and trademark check; Cory buying curioclass.org
- [x] Folder layout at S:\CurioClass, concepts moved into tools\
- [x] templates\tool-starter.html (band skins, opening reveal, bell, read-aloud, Practice/Challenge, a11y)
- [x] Seeded data\: grades, bands, subjects, tool-types, tools; modules.csv header only (Phase 1)
- [x] Private repo LochLogic/curioclass
- [ ] Teacher notes + meta for the two tools; cite Elements data sources
- [ ] Homepage + tool page mockup to judge the look (after Phase 1 scope; template PARKED 2026-10-22, Cory wants more design freedom)
- [ ] Eleventy skeleton (after mockup is approved)

## Later phases (for reference)
- Phase 1: modules.csv for K-12 across all subjects, aligned to CCSS / NGSS / C3 and a state baseline
- Phase 2: at least one tool concept per module (tools.csv rows with status = Concept)
- Phase 3: build, tune, publish
- Reading Room: public domain story library, plan in docs/LIBRARY-PLAN.md (draft 2026-10-25, awaiting Cory)
- Far back of the roadmap (parked 2026-10-25): instrument learning paths. One tool per instrument with about 10 to 12
  levels inside, beginner to early intermediate, on a shared engine (mic pitch detection, Web MIDI, Note Ninja staff).
  Recorder first, then keyboard, ukulele, guitar, voice; band instruments partly (a browser can't see the player's
  hands or hear how they shape the mouthpiece well enough to correct it). Own shelf under Arts and Music.
