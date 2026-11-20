# Arts pre-work: cold read, 2026-11-19

Read as the curriculum expert (docs/agents/EXPERT.md). I did not write these drafts. Nothing was edited but this file.
No outside source was opened. Anything resting on my memory is marked "from memory". Ratings: Firm (the repo's own
text shows it), Likely (one source or strong reasoning), Judgment call (reasonable reviewers differ).

## What I read

AGENTS.md; docs/agents/EXPERT.md; docs/agents/lenses/arts.md; docs/ADOPTION-BAR-SUBJECTS.md (pass rule, C1 to C16,
part 2, the arts row of "Before a scope and sequence"); docs/courses/arts/STANDARD.md and APPROACH.md; docs/APPROACH.md;
docs/courses/UNIT-PLAN.md; docs/reviews/arts-open-material-2026-11-16.md and arts-hs-music-and-levels-2026-11-16.md;
data/standards/ncas-performance-standards.txt (header read, all 1,202 ids counted by discipline and grade);
docs/reviews/prework-physical-education-read-2026-11-19.md (format). Also, to check stale notes only: the NCAS line of
scripts/standards.py, scripts/progression.py (grep for arts), docs/courses/CALENDAR.md (first 60 lines), data/courses.csv,
the 2026-11-16 entries in docs/agents/decisions/DESK-ANSWERS.md, and the "Our words" line of docs/courses/health/STANDARD.md.

## Verdict

The standard file is sound as a list: the 1,202 ids add up per discipline to the header's figures, no duplicates, no
malformed ids, and the band-year rule for K to 8 is clear and right. It is not yet usable by a planner, because no id
has any wording (a planner cannot tell what `TH:Cr2.1.5a` asks), no table says how many ids each course-year owns, and
the notes about the script and about pacing have gone stale. The approach page covers the bar's nine arts criteria in
outline but leaves out most shared-core approach rows (model fading, how a day opens, English learners, access,
safety, critique, cultural respect, room, cost, sources, evidence), so as drafted it would pass roughly four of the
nine arts criteria cleanly and would fail C7, C10, C11 and C14 (a door criterion), which together exceed the pass
rule's three part passes. The one change that matters most is adding the missing slots to APPROACH.md (findings 4 to
12) before asking for Cory's yes; the own-words id file (finding 1) matters most for the planners who come next.

## Findings, most serious first

### 1. No id has wording, so a planner cannot say what any of the 1,114 taught ids asks (Firm)

- **Where:** data/standards/ncas-performance-standards.txt; STANDARD.md sections 1 and 2; UNIT-PLAN.md rule 15 and
  section field 1.
- **What is wrong:** The file is ids only (right: the performance standards are all rights reserved). Nothing in the
  repo says what `VA:Cr2.3.4a` or `MU:Pr5.1.6b` means. Each progression, scope and unit writer will reopen the coalition's
  PDFs or paraphrase from memory, and three writers will paraphrase one id three ways. Health and PE got a one-line
  own-words file on 2026-11-19 (health STANDARD.md line 33); arts did not. UNIT-PLAN rule 15 ("the standard's verb is
  quoted exactly") cannot be followed here: the performance standards' wording may not be copied, and a unit plan field 2
  must list each standard "with its parts listed by verb".
- **Reuse terms check (header of the id file, STANDARD.md section 2):** the file header and section 2 both say
  paraphrase with citation is allowed, only the eleven anchors and the blank matrix are free, and a quote is limited to
  250 words. So an own-words file is within the stated terms; the terms themselves I did not reopen. Two cautions.
  The repo is public (memory file: curioclass public since 2026-10-28), so keep each line short and about what the
  student does, not a re-sentence of the standard's own phrasing; and the anchors (Cr1 to Cn11) may be used in their
  real wording (free and unlimited), which gives writers the verbs at the anchor level for nothing.
- **Fix:** Add `data/standards/ncas-performance-standards-words.txt`: `id<TAB>one line, at most 14 words, what the student
  does, in Curio Class's words`, one line for each of the 1,114 non-PK ids and each of the 63 music strand ids when they
  load; written by one agent and read by a second; header:
  "Our own one-line paraphrases for planning. Not the coalition's wording. National Core Arts Standards, 2014. Citation
  line as in STANDARD.md section 2." Add to STANDARD.md section 2: "A plan names a performance standard by id and states
  its action in the one-line words of ncas-performance-standards-words.txt. It never quotes the performance standards.
  The eleven anchors may be quoted." Add to UNIT-PLAN rule 15 one clause: "Arts: the performance standard's verb is
  not quoted (all rights reserved); the unit plan states each part in the one-line words and cites the id; the anchor's
  wording may be quoted."

### 2. No table says how many ids each course-year owns, or which course a grade code belongs to (Firm)

- **Where:** STANDARD.md section 3.1 and 3.2; the id file header ("performance standards per grade: DA 11, MA 11, MU 15,
  TH 12, VA 15").
- **What is wrong:** The rule names the mapping in words, but a planner cannot count. The header's "per grade" figures
  are unlettered standards (DA 11) while the file's ids are lettered statements (DA 21 per grade), and the header does
  not say which a course claims. STANDARD.md says "each id is taught" so the unit is the lettered id, but this is never
  stated. Music has uneven counts (K 19, grades 1 and 2 20, grades 3 to 8 21) and theater K has 17 where grade 1 has 24;
  a writer who assumes an even spread will miscount. The user's brief says "20 band courses plus the high school music
  course": high school music is one of the twenty, not an extra course.
- **Fix:** Paste this table into STANDARD.md after section 3.2 (counts made from the file on 2026-11-19; pre-K excluded):

| Discipline | K to 2 (K, 1, 2) | 3 to 5 | 6 to 8 | 9 to 12 per level (`.Ia`, `.IIa`, `.IIIa`; Level 4 repeats `.IIIa`) |
|---|---|---|---|---|
| Visual arts (VA) | 15 + 15 + 15 = 45 | 45 | 45 | 15 |
| Music (MU) | 19 + 20 + 20 = 59 | 63 | 63 | 21 each, strand `.C`, 63 in all, not yet loaded |
| Theater (TH) | 17 + 24 + 24 = 65 | 72 | 72 | 24 |
| Dance (DA) | 21 + 21 + 21 = 63 | 63 | 63 | 21 |
| Media arts (MA) | 18 + 18 + 18 = 54 | 54 | 54 | 18 |

  Add: "An id is one lettered statement (`DA:Cr1.1.2a`). A year's scope and sequence claims every id of its grade in its
  discipline, counted in this table. The file holds 1,202 ids: 1,114 taught (K to 8 and high school levels), 88 pre-
  kindergarten, not taught. Totals check: VA 180, MU 185, TH 281, DA 252, MA 216 taught." Add one line: "High school
  music is one of the 20 courses; its 63 ids are not in the file yet."

### 3. Two stale notes about the script and the music strand ids (Firm)

- **Where:** STANDARD.md section 1 (last bullets) and 3.3 (last bullet); ADOPTION-BAR-SUBJECTS.md arts row.
- **What is wrong:** STANDARD.md 3.3 says "scripts/standards.py does not yet accept the strand letter; its pattern changes
  before loading." The NCAS pattern in scripts/standards.py (line 107) already allows `(?:[CEHT]\.)?` before the level,
  and the bar's arts row says "music strand ids now pass scripts/standards.py". The three texts disagree. Separately,
  STANDARD.md 1 says the script does not check grade or letter and "a reader checks grade and letter against the file":
  with 1,114 ids that check cannot be left to a reader.
- **Fix:** Replace the 3.3 sentence with: "Ids: 21 per level, 63 in all, format `MU:Cr1.1.C.Ia`. scripts/standards.py accepts
  the strand letter (2026-11-19 read). They load into the id file by hand, ids only, when the high school music frame is
  written." In section 1 replace the last two sentences of the script bullet with: "It does not check that an id exists in
  the file. A plan's ids are checked by the standards gate against the file's lines (a worker's job, owed); until it
  exists, each scope and sequence states its id count against the table in section 3 and a reader spot-checks ten."
  Confidence on the gate itself is a judgment call; the stale note is firm.

### 4. Pacing is called "waits on Cory" but Cory settled it (Firm)

- **Where:** STANDARD.md header table (row "A written rule...") and 3.4 (title "waits on Cory"); APPROACH.md "Pacing".
- **What is wrong:** DESK-ANSWERS 2026-11-16 says "pacing as picked (K to 8 arts 64 sessions with a 32-session path,
  high school arts 160 days)" and the bar's arts row says pacing was settled. Both arts pages still say it waits. 3.4
  also says it "changes the arts course's day count from the 160 in docs/GLOSSARY.md": the glossary and CALENDAR.md set 160
  as the school year, not a course's days (science 3 to 5 runs 120 course days on 30 weeks), so nothing in the glossary
  changes. What is missing is the session length, which the bar's C2 needs ("minutes per lesson") and which no arts page
  states.
- **Fix:** Retitle 3.4 "Pacing (settled 2026-11-16)" and replace its body with: "A K to 8 arts year is 64 course days (two
  sessions a week over 32 weeks, CALENDAR.md). Session length: 40 minutes (ours, untested); every section plan states the
  set-up and clean-up minutes inside it. A school that meets once a week keeps every unit and every standard on 32 days by
  merging the days each unit marks. High school levels are 160 course days." In APPROACH.md "Pacing" replace the text with
  "See STANDARD.md 3.4." The 40-minute figure is a judgment call; the stale wording is firm.

### 5. Nobody holds the model and no day withdraws it (C7) (Firm)

- **Where:** APPROACH.md throughout; docs/APPROACH.md principle 3; UNIT-PLAN rule 12 and section field 5.
- **What is wrong:** C7 fails if "no day is named for withdrawing the model". The approach says technique is "shown and
  named in steps" but never says who holds the model on a given day or when it goes. Unit field 2 says "what is carried",
  and rule 12 requires "what happens to it" in the subject's verb (math: tied and withdrawn; science: revised; ELA: read and
  returned to). The arts page names no verb. A writer cannot fill section field 5.
- **Fix:** Add to APPROACH.md after "What the arts carry": "**What happens to what is carried.** The technique is shown by
  the teacher in named steps (the teacher holds it), tried together with a step card (the class holds it with the card), then
  made alone with the card in hand, then made with the card withdrawn. Each section plan names the day the step card goes
  and the day a student uses the steps from memory. A model work or demonstration is copied as a step, never as the end,
  and the card goes before the check. A technique is never first met in independent work." Add the verb to the arts
  slot of UNIT-PLAN rule 12: "arts: shown, carried with a step card, withdrawn."

### 6. How a day opens is not stated (section field 6) (Firm)

- **Where:** APPROACH.md "Kinds of day"; docs/APPROACH.md principle 4; UNIT-PLAN section field 6.
- **What is wrong:** Field 6 asks "how it opens and for how long" and rule 13 makes teaching first the default, with an
  opening task allowed only where students can attempt it. The arts page is silent, and its own unit shape (understanding
  first) does not say what a fluency, application or respond day opens with. A writer will invent openings per section.
- **Fix:** Add: "**How a day opens.** Every day opens in the first five minutes with one of three things, named in the day
  row: a warm-up from earlier technique (a rhythm, a warm-up, a sketch drill), a look or listen at a work with no prior
  knowledge asked (taught on the same day), or the set-up routine. A making day opens with the demonstration of the step,
  never with a free choice. In grades 2 to 5, teaching first is the default for anything new; no opening task asks for a
  technique not yet taught. A timer may be used for a set-up and clean-up cue (classroom management, rule 14)."

### 7. Unit field 2 asks for standards, parts and limits; the approach gives three carried things only (Firm)

- **Where:** APPROACH.md "What the arts carry (unit field 2)"; UNIT-PLAN unit field 2 and rule 5, 15, 19.
- **What is wrong:** Unit field 2 asks for each standard with its parts by verb and the limits, then what is carried. The
  arts page lists only the carried things (technique, works, showing). It does not say how a performance standard's
  parts are listed, which is the heart of C1 and of rule 5 (every part has an end-of-unit item). With no wording in the
  file (finding 1), the parts have no home. The word "works studied: two to four works" is also carried as if the
  works are the standard.
- **Fix:** Add one bullet to the top of that section: "**The standards and their parts.** The unit lists each performance
  standard by id with its parts in the one-line words of the words file, one part per action, and the limit (for example,
  'with a given pattern, not an invented one'). Every part has an end-of-unit item. The three carried things sit under this."

### 8. English learners, access for disabilities, reading load and extension are missing (C10, C11) (Firm)

- **Where:** APPROACH.md "Supports (field 9)"; UNIT-PLAN section field 9; bar C10, C11.
- **What is wrong:** "Supports" gives choice of material or role, a way to perform without performing alone, and a free
  option. It has nothing for an English learner (the discipline's words in depth, frames, telling a language gap from a
  skill gap), nothing for a student who cannot see, hear, move or tolerate sound, touch or crowds, no reading load line, no
  extension on the same standard. C10 and C11 "fail if" the supports are a general list not tied to the lesson, have no
  frames, and nothing separates a language gap from a content gap. Critique talk is where language demands rise.
- **Fix:** Add to "Supports":
  - "**English learners.** Each unit teaches three to five discipline words in depth, with a picture, a movement or a
    sound and a frame ('I see ___ because ___.' 'The rhythm goes ___.' 'My character wants ___.'). A student may show or
    perform the word instead of saying it. The unit's check marks what the student made, shown or performed separately from
    what they said, so a language gap is not marked as a skill gap."
  - "**Access.** Each section names what changes for a student who cannot see (describe the work aloud, touch models, large
    print step cards), cannot hear (a visual beat, a floor vibration, a written cue), cannot move freely (seated or
    one-limb versions, a role such as director or sound lead), or is sensitive to noise, touch, light or crowds (hearing
    protection, gloves, brush grips, a quiet corner, no forced contact, no strobe)."
  - "**Reading load.** Step cards are picture-led with the words read aloud on the card for grades K to 2. A student reads
    at most one short card alone in grades 3 to 5."
  - "**Extension, same standard.** A harder pattern, a second voice or layer, a tighter constraint, or teaching the step to a
    partner. Never the next grade's standard."

### 9. Safety content has no home; the page only says it is "listed in each section" (Firm)

- **Where:** APPROACH.md "Supports" (third bullet); lens "unsafe use of space"; bar part 2 criterion 9.
- **What is wrong:** The approach asks each section to list equipment and safe use of space but says nothing about what is
  safe. Dance, theater, visual arts, music and media arts each have different hazards; the lens names them and the approach
  does not. A section writer from nothing will write nothing, or invent. Safety facts also need sources or the mark "from
  memory" (UNIT-PLAN rule 16).
- **Fix:** Add a "Safe use" block: "Each section lists the clear space, the surface, the equipment and the hazard. Rules for
  every course: dance, a floor with room to move arms out, soft-soled or bare feet on a clean floor, no lifts, no jumping from
  heights, partner contact only by agreement and never required; theater, no real weapons, no contact stage fights, props
  checked, falls not rehearsed; visual arts, blades only by adult, no heat sources for children below grade 6, powdered clay
  and dyes with ventilation, wash hands, materials labelled non-toxic, no sharing of face-contact items; music, volume limits
  for headphones and drums, no loud sound in a student's ear, hearing and voice rest, no forced singing alone; media arts,
  no filming a student without the family's yes, no flashing lights, screen breaks. A safety statement without a source is
  marked 'from memory'." (Safety specifics are from memory; a named reader should check them. The health expert agent's
  pattern does not exist for arts.)

### 10. No critique routine, though the bar and lens ask for one (Firm)

- **Where:** APPROACH.md "Kinds of day" (Respond), "Practices"; lens "Critique is a routine"; bar part 2 criterion 6.
- **What is wrong:** Criterion 6 asks that students "give and get feedback, and reflect to refine." The approach has only
  "revision after critique" on the Respond day. It gives no protocol (the lens names describe, ask, suggest), and it puts
  critique after the check, while UNIT-PLAN field 5 says scored work must have had written feedback and a chance to revise
  before it is scored. As drafted, a unit shape of "application, check, respond" scores before any feedback and revision.
- **Fix:** Add: "**Critique.** A critique follows one routine, always in this order: describe what you see or hear, ask a
  question about a choice, suggest one change tied to a look-for of the unit. Feedback names a look-for; praise alone is not
  feedback. Students revise and say in one line what they changed. Each unit has one critique before the check (inside the
  second application day) and the check scores work revised after it. The Respond day acts on the check as before."
  Change the unit shape line to "understanding, fluency, application, critique and revise, application, check, respond".
  The extra day is an item-level choice (see Settled by the expert).

### 11. Assessment of creative work: no scoring guide design, no samples, no plan for thirty performances (C8, C9) (Likely)

- **Where:** APPROACH.md "Kinds of day" (Check), "The daily evidence"; bar C8, C9; UNIT-PLAN fields 5 and 7.
- **What is wrong:** (a) The page says a showing is "scored with a guide that names the technique and the words" but says
  nothing about what the guide marks, so a writer will mark beauty, effort or neatness. (b) C9 fails an open task without
  a rubric and samples at two levels; Curio Class has no children, so samples of student work cannot exist, and the page
  does not say what a sample is. (c) A check day for a class of thirty performances in a 40 minute session cannot be done
  as drafted, and the page says the end-of-unit assessment is "always a check day". (d) Field 7's marking step ("students mark
  short items against the key... hands up sets the groups") does not fit teacher-judged performance; the social studies
  variant (groups from the record sheet by component, at most four groups) does. (e) The Check kind allows "a response to a
  work not studied in the unit", but the scout says dance and theater have no open recordings, so an unseen work cannot be
  shown there. (f) Daily evidence marks a rotating few students on a performing day, so each student has one observation per
  unit: that is one point, not growth. The portfolio is named but not defined.
- **Fix:** Add: "**Scoring creative work.** The guide has three to five look-fors, drawn from the unit's technique and words,
  each scored met, partly or not yet. It never marks talent, speed, neatness, effort, the maker's identity, or how the work
  compares with another student's. A student's choice of subject is never marked down. Students score their own work with the
  same guide first. **Samples.** A sample is a written description of a work or performance at each level, or a work the team
  made as an adult example; samples at two levels sit in the unit plan beside the look-fors. **The check day.** Performances
  are shown in small groups or recorded on the application days; the teacher scores from the live showing and the recording
  across the check day and the respond day, and the unit plan says how many students are scored on which day. **Response
  allocation.** Items are teacher-judged; groups for the respond day come from the record sheet, at most four, others work in
  pairs from the written move (the social studies form of unit field 7). **Unseen work.** In dance and theater, the unseen
  work is a short written description, a live demonstration by the teacher or a Curio Class original, never an embed.
  **Growth.** Each unit opens with a baseline look at the unit's main look-for (rotating groups, recorded met, partly or not
  yet) and ends with the same look at the check, so each student has two marks and the growth is the change. Kept work
  becomes a portfolio: one piece a unit, with its one-line reflection, kept in a folder (paper, a file or a photo)."

### 12. Cultural respect: nothing on whose work, living artists, sacred works, or performing another people's tradition (C12) (Firm)

- **Where:** APPROACH.md "What the arts carry" (works studied); bar part 2 criterion 7, C12; lens "works from many times and places."
- **What is wrong:** The page says works come "from more than one time and culture across the year" and that each has its
  setting taught. It does not say whose work is chosen or recorded (C12 asks for "a record per unit of whose work and voices
  appear"), does not ask for living artists, does not name settings as when, where, by whom and for what, and does not say how
  a unit treats a work with a sacred or ceremonial use, or students performing, dressing in or imitating another people's
  dance, music, masks or story. Dance and theater are where this goes wrong first (costume, accent, casting, an invented
  "world dance"). The open-material scout adds a bias: museum open-access images and public domain recordings skew to older,
  European and American works, so "open where it exists" will make a one-tradition canon by default.
- **Fix:** Add: "**Works and their settings.** Each year's works include living makers and more than one region and period; a unit
  plan lists each work with its maker, place, date, purpose and rights line. No single tradition is the default; where the open
  copy of a work is thin, the unit uses a description and a link to the maker's or museum's own page, never a copy (not an
  excuse to drop the work). Where a work has a sacred or ceremonial use, the unit says what it is, studies it by looking and
  listening only, and does not have students perform or imitate it. Students learn a tradition's form from the community's
  own published teaching or a named practitioner's words, never by costume or invented imitation, and no student plays a
  character by an accent or a stereotype. The unit plan records the works' makers and places in one line each, and the
  fresh-agent sensitivity read covers them. **What a school may leave out.** A school may leave out a unit or a work for
  its community's reasons (for example, a unit that uses dance, masks or play-acting); each course page states which units
  stand alone."

### 13. Copyright of what is used in class goes beyond images (Likely)

- **Where:** APPROACH.md "What the arts carry" ("Images and recordings come from open or public domain sources where they
  exist"); docs/reviews/arts-open-material-2026-11-16.md.
- **What is wrong:** "Where they exist" lets a unit quietly use a non-open work. Music and theater classes also use scripts, songs,
  and dance, which are not images or recordings. Media arts invites remix of existing work. The scout's three rules (check on each
  item's own page; describe and link, do not embed; living artists link out) are not in the approach. Public performance, a family
  showing or posting is a different case from a class use (from memory: the US classroom exemption covers in-person teaching; a
  family evening and a recording that goes out do not). The approach gives no rule on student work.
- **Fix:** Add: "**Rights.** Every work a unit uses has a rights line in the unit plan, checked on the item's own page. A work that is
  not public domain or openly licensed is described in our own words and linked to the maker's or museum's page, never copied or
  embedded. Scripts, songs and dances students perform are public domain, openly licensed, original to Curio Class or written
  by the students. A showing for families uses only those. Media arts remix uses only public domain or openly licensed sources and
  names them. A student's work is the student's: it is shown outside the class only with the family's yes, and carries the
  student's choice of name."

### 14. Kept work and recordings of children: where do they live? (C15, FOUNDATION) (Likely)

- **Where:** APPROACH.md "The daily evidence" (a photo, a short recording, a saved file) and "A tool may ... keep work on the
  student's own device".
- **What is wrong:** A making day ends with a photo or recording; K to 2 speaks to a teacher or partner. The page does not say
  where a recording of a child's voice or face goes, who keeps it, or that none leaves the device (C15 fails any tool that stores
  data off the device). A home learner and a teacher with a class device are different cases. It also says nothing about the
  student who does not want to be recorded.
- **Fix:** Add: "**Kept work stays on the device or on paper.** A recording, photo or saved file stays on the student's, family's
  or school's device and goes nowhere else. A recording may be of hands, the work or the sound alone; a face or voice is never
  required. A student who does not want to be recorded is observed live and the teacher's mark stands as the evidence."

### 15. The ordinary-room answer is missing: minutes, class size, cost, teacher knowledge, two rooms (C14, a door criterion) (Firm)

- **Where:** APPROACH.md "Supports", "Pacing"; bar C14; UNIT-PLAN section fields 5 and 10.
- **What is wrong:** C14 fails if the course "needs space, kit, time or training most schools lack and gives no stand-in", states
  no cost, or has no paper path for a tool day. The approach lists no class size, no cost, no teacher training level, no stand-in
  list, and no "two rooms". The two rooms are not an extra: one child at home with a parent cannot "perform in an ensemble", cannot
  hold a critique with peers and has no class to show to, so the page's way to perform without performing alone ("ensemble, small group,
  recorded take") fails for the home room except the recorded take. Many K to 5 arts teachers are generalists (from memory); the
  page assumes a teacher who can hear technique.
- **Fix:** Add: "**The ordinary room.** A class of thirty needs a clear floor or tables, paper, pencils, found material and
  the voice; nothing is bought, and every unit lists a cheap stand-in. Set-up and clean-up are inside the session. The teacher
  needs no training in the discipline: each unit's teacher page says what to look and listen for, in plain words. **Two rooms.**
  One child at home: the parent is the audience and the critique partner; a showing is to the family or a recorded take; a
  duet or group piece has a solo or a doubled version. One projector or none: every day runs from a printed step card; the
  screen shows a work, a step or a playback only." The paper path for a tool day belongs here too: "a tool day has a printed
  version that does the same job."

### 16. No sources, no "not tried" statement, no logic model pointer, no family note (C13, C16) (Likely)

- **Where:** APPROACH.md whole page; docs/APPROACH.md "Sources" and its two honest notes; bar C13, C16.
- **What is wrong:** The arts page makes teaching claims (technique first, critique, kept work) with no source and no note on
  how much was read. The shared page covers general principles but its Sources table lists no arts source, and the bar's own
  rows for the arts instruments are the only support. The page does not say that nothing was tried with children and does not
  name the course's logic model. The shared page's introduction lists "math and ELA pages" and the science and social studies
  pages as promised but does not mention the arts draft.
- **Fix:** Add a short "Sources" table at the end: "Texas fine arts rubric 2025 (read in full by the bar's writer); California's
  five arts categories (read in full by the bar's writer); Oklahoma's fine arts rubric 2024 (read in full by the expert);
  National Core Arts Standards 2014 (ids and the free anchors; see STANDARD.md); NAfME descriptors for high school levels (read
  in full, 2026-11-16)." Add: "Nothing here has been tried with children, and Curio Class makes no claim that arts study raises
  any other result. Each course has a one-page logic model. Each finished unit has a family note, in English and Spanish."

### 17. High school levels: the 160-day year trips the bar's "daily period" and the 10 percent rule (Likely)

- **Where:** STANDARD.md 3.2 (160-day level; "Level 1's first unit assumes no earlier arts learning"); APPROACH.md "High school levels"
  (later levels "open with a short review unit"); bar part 2 "Fails if" ("a plan that needs a daily period") and C1.
- **What is wrong:** (a) A level of 160 daily sessions needs a daily period; high school arts often runs on rotation or block schedules
  (criterion 9). The K to 8 years get a short path; the high school levels get none. (b) Level 1 must teach a novice from nothing
  and reach Proficient in 160 days, which needs a bridge unit teaching grade 8 ids the high school ids do not list. C1 fails if more
  than 10 percent of teaching days go to content outside the course's standards; the same for the placement review at the top of each
  later level.
- **Fix:** Add to STANDARD.md 3.2: "A level's scope and sequence marks a short path of 80 course days (a semester or a rotation) that
  keeps every unit and every id by merging the marked days. Level 1 opens with a bridge unit of at most 12 days that teaches the
  discipline's grade 8 ids; Levels 2 and 3 open with a review unit of at most 6 days that doubles as placement. Bridge and review
  days are counted as inside the standards for the C1 limit and listed as bridge or review days in the frame." The numbers 12 and 6
  are ours, untested; the need for a short path follows from the bar. Confidence: Likely for the gap, Judgment call on the numbers.

### 18. The unit shape does not fit the 32-session path (Likely)

- **Where:** APPROACH.md "Kinds of day" (a unit runs roughly seven days); STANDARD.md 3.4 (merge to 32 days).
- **What is wrong:** A unit of seven days (eight with finding 10) becomes three or four days on a school that meets once a week.
  Every unit still needs a showing, a response to another artist's work and the check. The page does not say what a merged
  unit keeps. At about 24 ids a year in theater, roughly nine units a year, the path has about 3.5 days a unit.
- **Fix:** Add: "On the 32-session path each unit keeps four things, in this order and no fewer: the demonstration with a step
  card, one making or rehearsal day with a critique, the showing (the check), and one respond day; fluency days fold into the
  openers. The frame marks which days merge."

### 19. Colour-free and keyboard-free play: the tool examples fail C15 (Likely)

- **Where:** APPROACH.md "What a tool may and may not do" ("color mixing, shot types, stage directions, rhythm reading"); bar C15.
- **What is wrong:** C15 fails a tool that fails keyboard-only or colour-free play. A colour-mixing practice tool is a colour task;
  a rhythm tool is a sound task. The page does not say how a student who cannot see or hear the cue plays. The page also uses "tool"
  both for software (GLOSSARY: tool = Curio Class software) and for materials ("Tools that cost money are never required").
- **Fix:** In the tool paragraph add: "A tool for colour names every colour in words and in numbers and works with no colour
  judgment alone; a tool for sound shows the beat on screen and works with the sound off; every tool plays by keyboard." In "Supports"
  change the third bullet to "Materials and instruments that cost money are never required..."; keep "tool" for software only.

### 20. The "leans on" notes name courses that are not in the student's year, and no dance and PE split exists (Likely)

- **Where:** STANDARD.md section 6.
- **What is wrong:** (a) Media arts leans on computer science for privacy and copyright, but computer science is not core and a
  student may not take it that year; the arts unit "does not reteach the core skill" would leave the student with nothing.
  (b) A music unit on note values must "come after the fraction units in the same grade", but arts meets on its own two sessions a
  week with its own teacher; nothing says how a planner learns the math week (calendar.csv has weeks for math, so it is
  possible, but the rule does not say to look there). (c) "Dance units and PE dance units name each other and do not
  double-teach" has no split to follow; PE's own read found the same gap (docs/reviews/prework-physical-education-read-2026-11-19.md,
  its "what a progression writer still needs").
- **Fix:** (a) "Media arts teaches the one idea of privacy or copyright its unit needs, in a short step of the unit, and notes the
  computer science unit that goes deeper; it does not wait for it." (b) "A music unit on note values is placed after the math week
  that teaches fractions (data/plans/calendar.csv) or uses beat counts only." (c) "Dance in arts is the art: making, performing,
  responding to and connecting dance. Dance in physical education is movement skill, fitness and teamwork. Arts dance units do not
  teach the motor skill; PE dance units do not teach choreography, performing for an audience or response to dance. Each pair of
  units names the other in its connections line."

### 21. "Connect" is a named process with no place in a unit (Likely)

- **Where:** APPROACH.md "Practices", "Kinds of day"; bar part 2 criterion 1 and 7; lens "four processes, every course."
- **What is wrong:** The page names Cn10 and Cn11 by code in the practices slot but gives them no day. The kinds of day give
  creating, performing and responding places; connecting is nowhere. A year of creating, performing and responding passes the
  letter and not the standard.
- **Fix:** Add one sentence: "Connecting (Cn10, Cn11) lives in the understanding day that studies a work: the student names one tie
  to their own life (Cn10) and one tie to the work's time, place or purpose (Cn11), in the day's evidence sentence."

### 22. The unit shape and the day kinds may be read two ways on a "respond" day (Judgment call)

- **Where:** APPROACH.md "Kinds of day".
- **What is wrong:** The page splits "responding" (the artistic process, on an understanding day) from "respond" (the day kind) and
  says so, which is right and matches the glossary. But the daily evidence slot then says "a written or spoken response to a work" in the
  check kind, so a third use appears. A busy writer will put "respond" on a study day.
- **Fix:** Name the artistic process "responding to a work" in full everywhere on the page and keep "respond day" for the day kind.

### 23. Two sections restate the standard and the settled rules (Judgment call)

- **Where:** APPROACH.md "Pacing", "High school levels", "High school music"; STANDARD.md 3.2 to 3.4; the bar's arts row.
- **What is wrong:** AGENTS.md says each rule is stated once. The level table, the entry rule, the 160-day year, the placement rule and
  the music strand's no-instrument rule appear in STANDARD.md and again in APPROACH.md. The two will drift (they already did on pacing, finding 4).
- **Fix:** Keep the rules in STANDARD.md. In APPROACH.md cut both sections to what the plans fill: "Level 4 is one sustained project with
  checkpoints as check days and critique as respond days. High school music: composing and theory, practised by voice, body percussion and
  a free keyboard or Curio Class tool; a day may offer 'use your own instrument' as one way in. See STANDARD.md 3.2 and 3.3."

### 24. "Students who join mid-band" is ambiguous (Judgment call)

- **Where:** APPROACH.md "Supports", last bullet.
- **What is wrong:** "Start from the year's first unit openers" could mean a student who joins at the start of year 2 or 3 of a band, or
  one who joins mid-year. C4 asks what the band before taught. Each year's ids build on the earlier grade's, and nothing says what a
  student who skipped year 1 gets.
- **Fix:** "A student new to the band, or to the year, takes the year's first unit as written; each unit's opening retrieval or
  readiness task names the earlier-year technique it assumes and the ten-minute reteach (UNIT-PLAN field 4)."

## The bar and the approach, criterion by criterion

Pass = the line shows it and no fails-if is met. Part = something is there but a fails-if or a slot is open. Fail = not found or built in.

### Arts part (criteria 1 to 9)

| # | Verdict | The line, and what is lacking |
|---|---|---|
| 1 All four artistic processes in each course | Part | APPROACH "Practices": "Over a year every course touches all four processes." Connecting has no day (finding 21). |
| 2 Technique taught directly, in steps, gets harder | Part | "What the arts carry": "taught in steps that get harder"; "Practice that returns": "at a harder step." No fading and no model holder (finding 5). |
| 3 Discipline's words taught and used in making and responding | Pass | "A study day ends with a sentence that must use one of the day's words"; "words come back in every response." (EL depth is finding 8.) |
| 4 Students make, adapt or extend own work and show it, with choice | Pass | "Application: ... with some choice"; "Every unit has at least one showing"; "Choice grows by level." |
| 5 Taught to read, judge and respond to other artists' work | Pass | "Understanding ... a work is studied with the discipline's words"; "one response to another artist's work." |
| 6 Feedback given and received; reflect to refine | Fail | No critique protocol; revision only on a Respond day after the check (finding 10). |
| 7 Works from many times and cultures, with history and setting taught | Part | "From more than one time and culture across the year, each with its setting taught." No setting definition, no living artists, no sacred-work or imitation rule, no record (findings 12, 13). |
| 8 Assessment ranges: guide-scored work, self-assessment, work kept over time | Part | Guide, self-check, portfolio all named. Guide design, samples, check-day logistics, baseline and growth missing (finding 11). |
| 9 Pacing fits real schedules; equipment and safe use of space listed | Part | "Pacing" and "Equipment and safe use of space are listed" present. Stale pacing note (4); no safety content (9); no high school short path (17). |

### Fails-if list (part 2)

| Condition | Verdict | Line |
|---|---|---|
| Prompts to express with no technique taught | Pass | "A making day ... uses the technique"; Application follows understanding and fluency. |
| No performing or showing | Pass | "Every unit has at least one showing." |
| Response work without the discipline's words | Pass | Study-day evidence "must use one of the day's words". |
| One culture's canon | Part | Rule is stated; no guard against the open sources' bias (finding 12). |
| A plan that needs a daily period | Part | K to 8 clear; high school levels 160 daily sessions with no short path (finding 17). |

### Shared core rows that point at layer 3, read against this page

| Row | Verdict | Line or what is lacking |
|---|---|---|
| C1 Every standard named and taught in full; named edition loaded | Part | Edition named and loaded (STANDARD 1). Parts by verb impossible with no wording (1, 7); count table missing (2); music high school ids not loaded; no id-existence gate (3). |
| C2 Year plan with reasons, days, minutes, short path | Part | 64 days and 32-day path stated; minutes per session absent (4); high school short path absent (17). |
| C3 Nothing wrong, sold, authors plain | Part | No promotion on the page. Safety facts need sources (9); rights line per work (13); authorship is not stated on this page (16). |
| C4 Each idea rests on the last | Part | "Practice that returns" revisits earlier years. No readiness or retrieval line; mid-band note ambiguous (24); band before not stated. |
| C5 Unit overview prepares the teacher | Fail | The page says what a unit carries, not that a teacher page teaches the teacher (a non-specialist; finding 15). |
| C6 Lessons ready to teach | Not tested here | A scope and day layer criterion; the page names the day kinds and the evidence only. |
| C7 Taught, then faded, and returns | Fail | No holder, no withdrawal day (finding 5). |
| C8 Assessment system; students judge and track own work | Part | Self-check and portfolio present; before-teaching evidence, baseline and growth absent (11, 24). |
| C9 Teacher can score and act | Part | "Met, partly, not yet" and "next session's first minutes" present; rubric design, samples at two levels, record sheet use absent (11). |
| C10 Every learner works on the content | Fail | Choice and non-solo present; no disability access, no reading load, no extension on the same standard (8). |
| C11 English learners inside the lesson | Fail | No words, frames or gap-versus-skill note (8). |
| C12 People shown with care and range | Fail | No record, no living artists, no protocols (12). |
| C13 Approach explained; families told | Part | Subject page exists; no sources or "read" status; no family note slot (16). |
| C14 Ordinary room; cost, time, space, knowledge (door) | Fail | No cost, class size, minutes, paper path, teacher level or two rooms (15). |
| C15 Screens serve the learning | Part | Tool jobs and "keep work on the device" present; colour-free, keyboard and sound-off cases absent (14, 19). |
| C16 Honest about evidence | Part | The draft banner is honest; no "not tried" statement, no logic model (16). |

By the pass rule (the door is C1, C2, C3, C14), the page as written would stop at C14 and not be read further.
That is the main reason to fix findings 5 to 16 before Cory's yes.

## Pointers to what a progression writer would get wrong from these pages

- Count ids by grade wrongly (finding 2): header "per grade" figures are unlettered standards; music and theater K are uneven.
- Quote the performance standards' verbs (finding 1) or not know what an id asks.
- Put a high school level on a grade, or treat Level 4 as new ids (STANDARD 3.2 is clear, but nothing in a progression gate checks it; scripts/progression.py has no arts rule: arts has only grade ids, so a progression per technique has no automatic owner check).
- Teach a note-value unit before the math week, or reteach fractions (finding 20).
- Treat "respond" as the process on a respond day (finding 22).
- Assume 160 course days in arts K to 8 because of the old note (finding 4).

## Settled by the expert

| Choice | Reason | File it touches |
|---|---|---|
| The unit of count is the lettered id (`DA:Cr1.1.2a`); the course claims every id of its grade | The file lists lettered statements; the header's per-grade numbers are unlettered | STANDARD.md section 3 |
| One critique day before the check, inside the second application day (no extra day) | Keeps the 7-day shape; UNIT-PLAN field 5 requires feedback before scoring | APPROACH.md "Kinds of day" |
| Session length 40 minutes (ours, untested) | C2 needs minutes; the figure only has to be stated | STANDARD.md 3.4 |
| Bridge unit at most 12 days; review unit at most 6 days (ours, untested) | C1's 10 percent limit is 16 days of 160 | STANDARD.md 3.2 |
| Anchors may be quoted in real wording; performance standards never | STANDARD.md section 2 (anchors are free) | STANDARD.md section 2, UNIT-PLAN rule 15 |
| A one-line words file of at most 14 words per id | Matches health's file; short lines keep clear of the reuse limit | data/standards/ncas-performance-standards-words.txt (new) |
| "Tool" means software only on arts pages | GLOSSARY | APPROACH.md "Supports" |

## What is right and should not be touched

- The standard file itself: edition, header, per-discipline counts and the note that the high school music strand is a separate load.
- The K to 8 band-year rule (STANDARD 3.1): each year claims only its grade's ids and revisits earlier years as practice.
- The decision to claim composition and theory only for high school music and to leave ensemble, harmonizing instrument and technology strands out, with an ensemble companion page.
- The five kinds of day and the explicit split between the "responding" process and the "respond" day.
- The daily evidence forms (kept work plus a one-line self note; one sentence that uses a day's word; a performing-day self-check) and "met, partly, not yet, no mark."
- "A tool may ... may not": no judging of finished work, no standing in for performing, no generating the student's work.
- The revision watch (STANDARD 4) and the scout's verdict that every arts course is written fresh.

## For Cory

Each is a scope, money, people or audience call. My pick first.

1. **The own-words file for 1,114 NCAS ids is public.** The repo is public and the coalition's performance standards are all rights reserved. Recommended: write the one-line file now (STANDARD.md 2 says paraphrase with citation is allowed), keep lines short, and ask nobody for permission unless you want certainty; the alternative is a short email to the coalition's rights administrator before publishing the file. (Audience and legal risk, not a build call.)
2. **High school short path.** Recommended: yes, add an 80-day path to every high school level so a rotation or semester school can run it (finding 17). Alternative: leave levels as 160 daily sessions and accept the bar's "daily period" fail-if on those four years of five disciplines. This adds build scope to 15 courses of 160 days.
3. **A "what a school may leave out" statement per arts course.** Recommended: yes (finding 12): dance, theater, masks and play-acting units each stand alone, so a school or family that objects can omit one without breaking the course. This is the same stance Cory took for health's sensitive units.
4. **Approach yes.** Recommended: no yes until findings 4 to 16 are applied; then yes. It is a draft and not in force.

## Not checked

- Whether the 1,202 ids match the live coalition handouts (no outside source was opened). Only the file's internal counts were checked, against its own header.
- The 63 music strand ids: not in the file; their format and count rest on docs/reviews/arts-hs-music-and-levels-2026-11-16.md.
- The NCAS copyright terms themselves (STANDARD.md section 2 is the record); the exact citation form of the notice (I did not open the guidelines).
- Every claim about arts practice marked "from memory" above (safety specifics; school-schedule norms; the US classroom exemption; generalist teachers in K to 5).
- The statements of NAfME, California, Texas and other framework mappings in the high school review (read as the review's claims, not reopened).
- docs/courses/CALENDAR.md beyond its first 60 lines; scripts/course_status.py PER_GRADE; the arts lens beyond what the bar and approach rely on.
- The open-material scout's licence readings (search-only items are the scout's own marking).
- Whether any arts scope and sequence, unit plan or day exists; none was read. This read is of the pre-work only.
