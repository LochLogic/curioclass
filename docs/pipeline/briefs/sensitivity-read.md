# Job: the agent reads that stand in for outside readers ({kind}, {target})

Added 2026-11-14. Cory, on the Desk: "We have no support for this, it's just us. Ensure that the sensitivity agent is
well educated, and we will make the best effort we can to teach with honesty and dignity at an age appropriate
level." And: "Our agents are our best hope for success." So no outside reader is planned. These reads take the
places FOUNDATION 7.3 once gave to people: a community reader, a health specialist, a science safety teacher, a math
content reviewer and an ELA teacher. Each runs as a fresh agent that has not seen the work written, and each studies
before it judges. A read that skips its study step fails, whatever it finds.

Slots: {kind} is one of `sensitivity`, `safety`, `answer-key`, `text`, `rights`, `spanish`; {target} is the file or unit read (a frame
unit, a unit plan, a day, a text); {community} names the people or topic for a sensitivity read; {date}.

## 1. Study first (every kind)
Before opening the target, build what a qualified reader would bring, and list it in the report under "What I
studied", each with a link or a file path and one line on what it taught you:
- **sensitivity:** the community's own published voice first: the nation's, people's or group's own sites, curricula,
  style and language pages, histories and statements (for a Native nation, the nation's own government and
  education pages and any tribally written curriculum, such as Since Time Immemorial in the source store); then
  scholarship by members of the community and by historians of it; then journalism and education style guides on
  that community or topic (for example a Native journalists' association guide, a disability language guide, a
  public health body's guidance for health topics). At least five sources, at least two of them the community's
  own. Note the community's own names and terms, what it asks outsiders not to do, the common stereotypes and
  errors, and where its members disagree.
- **safety:** published school science safety guidance (a national science teachers' association's safety
  advisories, a chemical society's secondary school chemical safety guide, the relevant manufacturer's safety data
  sheet for every chemical named), plus the materials list and room assumptions in docs/FOUNDATION.md section 5.
- **answer-key:** nothing outside; the study step is to solve. Solve every item cold, writing your own answer and
  method, before opening the key.
- **text:** the subject lens (docs/agents/lenses/ela.md), docs/RUBRIC-ELA.md, the standard's text-complexity
  guidance, and two published model texts of the same kind and grade.
- **rights** (added 2026-11-15; Cory 2026-11-14, answer 1: the second rights reader is an agent): the licence or
  public-domain basis of each outside text, image or base-text lesson, from its own source page (the licence text
  itself, the publication date and place, the edition), plus docs/FOUNDATION.md's rights rules. Credits stay light:
  one short credit per adapted day (Cory 2026-11-13).
- **spanish** (added 2026-11-15; the native Spanish reader is an agent): two published Spanish-language school texts of
  the same grade and kind, a style guide for neutral Latin American Spanish in schools, and the glossary of terms the
  course already uses in Spanish.

## 2. Read the target
- **sensitivity:** facts right and plain (BASELINE rule 5: don't soften history or science); the people shown as
  people with their own voices and agency, not only as victims or as a lesson for others; the community's own names
  and terms; no role play or simulation that puts a child in a victim's or perpetrator's place; images and
  activities that would not shame a child from that community sitting in the room; age-appropriate depth; the
  teacher note saying what may come up and how to handle it. Name each problem, quote the line, give the fix.
- **safety:** every hands-on step: the hazard, the control, the age, the supervision, the eye protection, the
  substitution if the room lacks something; the stop rule; allergies; heat, glass, chemicals, magnets, sharp
  edges, electricity. A step with no safe version in a typical classroom is cut or given a demonstration path.
- **answer-key:** compare your answers with the key; every mismatch is either the key's error, an ambiguous item
  (fix the item), or your error (say so). Check that each item tests the standard the plan says it tests.
- **text:** a qualified ELA teacher's read: complexity for the grade, the standard's work can be done on it,
  quality as writing, a fair picture of the people in it, and no line a child would be harmed by.
- **rights:** each outside item has a basis that allows our use (licence, public domain, or our own), the credit says
  it, the edition used is the one checked, and nothing comes from a login-gated or no-derivatives source. Funding-only
  items (rows marked "only if funded") are listed, not judged.
- **spanish:** a reader's read of the Spanish family and student copy: meaning kept, natural and age-appropriate,
  neutral across Spanish-speaking families, the course's terms used consistently, nothing a family would read as
  talking down.

## 3. Report
docs/reviews/{kind}-{target}-{date}.md: "What I studied" (the list from step 1); a verdict (pass, pass with fixes,
or fail) in two sentences; findings with the line quoted and the exact fix; "Could not settle" for anything the
sources did not answer (it goes to the lead, and to Cory only if it changes what a grade teaches). No em dashes;
"Curio Class" in full; no company names in any suggested student, teacher or family text. Edit nothing but the report.

## When these reads run
- Frames (step 2): the frames name which units need which read; no read runs on a frame alone.
- Units (step 4) and days (step 6): every unit gets the sensitivity read; units with hands-on work the safety read;
  every course's checks the answer-key read before the course is called finished; every original or replacement
  text the text read before it ships.
