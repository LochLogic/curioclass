# Open social studies material for Curio Class: is there a base text we may adapt?

Read 2026-11-13 (pre-work P2). Research notes, not legal advice. Every licence below was read on the publisher's own
page on that date unless marked "search only" (seen in a search summary, page not opened) or "not read, blocked".
Nothing in the repo was changed except this file. The bar is BASE-TEXTS.md: CC BY 4.0, CC BY 3.0, or public domain
(US federal work) is a base; NC, SA, ND or unclear is reference only.

## The short answer

- **No social studies program clears the bar end to end.** There is no Illustrative Mathematics or OpenSciEd for
  social studies: every complete K-12 program found (Core Knowledge, Michigan Open Book, New Visions, New York
  toolkit and C3 inquiries, OER Project, iCivics) is NonCommercial, ShareAlike or all rights reserved.
- **OpenStax's live social studies books are all CC BY-NC-SA 4.0** (U.S. History, American Government 4e, World
  History 1 and 2, Economics 3e, Macro 3e, Micro 3e, Principles of Finance 1e and 2e, Psychology 2e, Sociology 3e).
  American Government 3e, which the task named, is now **retired** and is CC BY 4.0. So are Economics 1e and 2e,
  Macro and Micro 1e and 2e (and their AP editions), Psychology 1e and Sociology 1e and 2e. The official PDFs of the
  retired CC BY books are still on OpenStax's servers.
- **Every OpenStax preface read, including the CC BY retired ones, carries an AI clause:** "This book may not be used
  in the training of large language models" and may not "otherwise be ingested into large language models or
  generative AI offerings without OpenStax's prior written permission". The same prefaces say OpenStax-made images,
  activities and assessments are CC BY-NC-SA, and the site footer on the CC BY books still prints CC BY-NC-SA. Curio
  Class builds with AI agents, so this is a person's call before any agent reads these books (see Traps).
- **Real CC BY or public domain pieces exist, but each covers part of one course:** Washington's Since Time
  Immemorial units (CC BY 4.0), the ETSU open text World History Since 1500 (CC BY 4.0, college), CFPB financial
  education activities (public domain), DocsTeach activities (CC0) and National Archives documents, NPS Teaching with
  Historic Places (public domain), and Oak National Academy's history and geography (Open Government Licence v3.0,
  attribution-only, but not one of the three licences BASE-TEXTS.md names).
- **Subject order:** social studies has no base text, so by the plan **science goes second**.

## Candidates

Course ids are from data/courses.csv: ss-k5, world-geo-6, world-hist-7, us-hist-8 (Civics, grade 8), world-hist-hs
(World History I, grade 9), world-hist-2 (grade 10), us-hist-1 (grade 11), us-hist-hs (US History II, grade 12),
government, economics, psychology.

### OpenStax (Rice University)

Licence per book from the OpenStax catalogue data (books API, read 2026-11-13); prefaces opened for American
Government 3e, U.S. History, Psychology 1e and Principles of Economics 2e.

| Book | State | Licence (catalogue) | Courses it could serve | Verdict |
|---|---|---|---|---|
| U.S. History (2014) | live | CC BY-NC-SA 4.0. Preface: "Creative Commons Attribution-NonCommercial-ShareAlike License" | us-hist-1, us-hist-hs, ss-k5 grade 5 | Reference |
| World History Vol. 1 (2023) and Vol. 2 (2022) | live | CC BY-NC-SA 4.0 | world-geo-6, world-hist-7, world-hist-hs, world-hist-2 | Reference |
| American Government 4e (2025) | live | CC BY-NC-SA 4.0 | government, us-hist-8 | Reference |
| **American Government 3e (2021)** | **retired** | CC BY 4.0. Preface: "licensed under a Creative Commons Attribution 4.0 International (CC BY) license" | government, us-hist-8 | Partial base, text only, gated on the AI clause |
| American Government 1e, 2e | retired | CC BY 4.0 | as above | Older; use 3e if any |
| Principles of Economics 3e, Macro 3e, Micro 3e (2022) | live | CC BY-NC-SA 4.0 | economics | Reference |
| **Principles of Economics 2e (2017), Macro 2e, Micro 2e, Macro and Micro for AP 2e** | **retired** | CC BY 4.0. Preface: "This book uses the Creative Commons Attribution License" (the same paragraph then describes NC-SA terms; see Traps) | economics | Partial base, text only, gated on the AI clause |
| Principles of Finance 1e (deprecated), 2e (2026-06-24, live) | | CC BY-NC-SA 4.0 | economics (personal finance) | Reference; college corporate finance, poor fit anyway |
| Psychology 2e (2020) | live | CC BY-NC-SA 4.0 | psychology | Reference |
| **Psychology 1e (2014)** | **retired** | CC BY 4.0. Preface: "licensed under a Creative Commons Attribution 4.0 International (CC BY) license" | psychology | Partial base, text only, gated on the AI clause |
| Introduction to Sociology 1e, 2e | retired | CC BY 4.0 | none on our list | Not needed |
| Life, Liberty, and the Pursuit of Happiness (2020) | retired | CC BY 4.0 (catalogue) | us-hist-1, us-hist-hs (AP US History level) | Link only: no PDF in the catalogue, served only through OpenStax Tutor; not read |

No OpenStax personal finance text exists; no OpenStax geography text exists. The OpenStax K12 social studies page
(openstax.org/k12/social-studies) lists only the live NC-SA editions.

Level fit: all college or AP. Quality signals: widely adopted college texts; no K-12 review read.

### Other textbooks

| Candidate | Licence (as read) | Courses | Level | Verdict |
|---|---|---|---|---|
| The American Yawp (Stanford University Press, updated edition) and its Primary Source Reader | CC BY-SA 4.0: the home page shows a "Creative Commons BY-SA" badge linking to by-sa/4.0 | us-hist-1, us-hist-hs | College | Reference |
| World History Since 1500: An Open and Free Textbook (Rankin and Weise, East Tennessee State University, 2022, 15 chapters) | "This work is licensed under a Creative Commons Attribution 4.0 International License" (ETSU digital commons page) | world-hist-2; the 1500 to 1800 part of world-hist-hs | College survey | **Partial base**, text only; third-party images not checked |
| History in the Making: US to 1877 (University of North Georgia) | CC BY-SA (3.0 or 4.0, sources disagree) (search only) | us-hist-1 | College | Reference |
| World History: Cultures, States, and Societies to 1500 (UNG / LOUIS) | CC BY-SA 4.0 (search only) | world-hist-hs | College | Reference |
| World History to 500 CE (Rausch); Global Interconnections 1300 to present (CSU Ohio) | CC BY-NC 4.0; CC BY-NC-SA 4.0 (search only) | world-hist-7, world-hist-2 | College | Reference |
| Michigan Open Book Project (K, 1, 2, 3 Michigan, 4, 5, 7 Ancient World, 8 US, HS World History, HS US, HS Civics) | "licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License" (textbooks.wmisd.org/the-books.html) | ss-k5, world-hist-7, us-hist-8, high school | K-12 | Reference. Quality: 2015 press coverage was critical (search only) |
| Utah (UEN / USBE) open textbooks | Science, math, language only; no social studies title found. Utah HB 488 (2026) would commission open social studies material; status unknown (search only) | none yet | K-12 | Watch item |

### State and tribal curricula

| Candidate | Licence (as read) | Courses | Level | Verdict |
|---|---|---|---|---|
| Washington OSPI, John McCoy (lulilas) Since Time Immemorial: Tribal Sovereignty in Washington State | "Except where otherwise noted ... is licensed under a Creative Commons Attribution 4.0 International License"; "All logos are property of their respective owners"; third-party items marked next to the item. OSPI asks that adaptations avoid changing the content design or adding cultural bias. Endorsed by all 29 federally recognized tribes in Washington (search only). | K-3: three pathways (Our Place, Honoring the Salmon, Giving Thanks); grade 4: three Washington state units; grade 5 US history: three units (Encounter and Colonization; Revolution and Constitution in Indian Country; Elwha); middle school: one unit (Medicine Creek Treaty); high school: US History units 1 to 6 and Contemporary World Problems units 1 to 4. Serves ss-k5 (grades 4 and 5), us-hist-8, us-hist-1, us-hist-hs, government | K-12 | **Partial base** for tribal sovereignty strands. Washington-specific: grade 4 units are a state study. Needs a sensitivity review and a check of third-party marks per unit |
| Oregon Tribal History/Shared History (SB 13), Education Northwest for ODE | No licence line on the ODE page read (first 100k characters). OER Commons listing: not read, blocked (403) | ss-k5 (K-5), us-hist-8, high school | K-12 | Unclear, so reference only |
| Montana Indian Education for All (OPI) | No licence found (search only); some units are built on copyrighted trade books | ss-k5, middle, high | K-12 | Unclear, so reference only |
| New York K-12 Social Studies Toolkit / C3 Teachers inquiries (IDM) | Each toolkit inquiry prints CC BY-NC-SA 4.0 (already recorded in CurioClass-sources new-york-ss-toolkit NOTES.md, checked 2026-11-12/13). c3teachers.org timed out twice today: not read | IDM form for every course | K-12 | Reference (already in the store) |
| New Visions Global History I, II and US History (New York) | Own material "CC BY-NC-SA 4.0"; partner material under other licences (search only) | world-hist-hs, world-hist-2, us-hist-1 | High school | Reference |
| Core Knowledge History and Geography (K-8) | CC BY-NC-SA 4.0 on unit PDFs; names are trademarks (search only) | ss-k5, world-geo-6, world-hist-7 | K-8 | Reference |

### Nonprofit programs

| Candidate | Licence (as read) | Courses | Verdict |
|---|---|---|---|
| OER Project (World History Project, Big History) | Terms of use: course materials generally "Creative Commons Attribution Non-Commercial License (CC-BY-NC)"; bots barred from scraping | world-hist-hs, world-hist-2 | Reference |
| iCivics | Terms: no derivative works "unless you receive our permission in advance"; noncommercial only; no CC licence | us-hist-8, government | Link only |
| Digital Inquiry Group (Reading Like a Historian) | Free; FAQ names only a Stanford distribution agreement, no CC licence | us-hist-1, us-hist-hs, world history | Link only |
| **Oak National Academy (England), history and geography KS1 to KS4** | "Licensed on the Open Government Licence v3.0, except where otherwise stated" (Collection 2, the current curriculum). Collection 1 (legacy) is noncommercial only. Third-party items carry their own credit. Some content shared "only with users in the UK" behind sign-in. llms.txt invites adaptation and runs an MCP server for AI tools. | Primary history units include Stone Age, Ancient Egypt, Sumer, Indus and Shang, Ancient Greece, Rome, Early Islamic Baghdad, Benin or the Maya: a fit for world-geo-6 and world-hist-7. KS3 history and geography (not opened) likely fit world-hist-hs, world-hist-2 and geography strands | **Partial base if Cory accepts OGL v3.0** (attribution-only, treated by Oak as equivalent to CC BY 4.0, but not on the BASE-TEXTS.md list). British-centred framing; written for England |

### Federal and public domain sources

| Candidate | Terms (as read) | Courses | Verdict |
|---|---|---|---|
| CFPB youth financial education (135 classroom activities, K-1 through 11-12, earning, saving, protecting, spending, borrowing) | Site policy: "Information created by the CFPB is in the public domain"; logo and names are registered trademarks; outside copyrighted items may appear | economics (personal finance half), ss-k5 money strands | **Base for personal finance** (activities, not a full course). Check each activity for third-party items |
| Federal Reserve education (federalreserveeducation.org, absorbed St. Louis Fed Econ Lowdown) | "proprietary intellectual property of the Federal Reserve System and its regional banks"; whole-resource copies for noncommercial use only; no modifying, rebranding or adding to "any other database or compilation" | economics | Link only. Federal Reserve Banks are not federal agencies; not public domain |
| National Archives DocsTeach | "Teaching activities on this site have received the CC0 Public Domain Dedication"; documents labelled per item (In Copyright, Not Evaluated, No Known Copyright) (labels from search only) | every history and civics course | **Asset**: CC0 activities and public domain documents, item by item |
| Library of Congress (primary source sets) | loc.gov/legal: the Library "generally" does "not own the rights to materials in our collections". Teachers program page: not read, blocked (403) | every history course | Asset, item by item (rights statement on each item). Teacher guides' status unverified |
| NPS Teaching with Historic Places | NPS disclaimer: NPS-made material "is generally considered in the public domain"; Arrowhead is a trademark; third-party content excepted | us-hist-1, us-hist-hs, ss-k5, us-hist-8 | **Asset / partial base**: public domain lesson plans, one site at a time |
| US Courts educational resources (14 activities: amendments, Brown and Mendez re-enactments, financial literacy, civil discourse; landmark case podcasts) | No reuse line on the page; the website policies URL returned 404. Made by the Administrative Office of the US Courts, a federal body, so likely public domain (inference, unverified) | us-hist-8, government | Asset, probable; confirm before adapting |

Not checked this pass (open items): LibreTexts K12 social studies, Facing History (expected NC), Bill of Rights
Institute and Center for Civic Education (expected all rights reserved), Louisiana and other state social studies
units, OER Commons collections (OER Commons returned 403: not read, blocked).

## Course by course

| Course | Base (CC BY or public domain) | Partial base or assets | Reference only | Verdict |
|---|---|---|---|---|
| ss-k5 Elementary (K-5) | None | Since Time Immemorial K-3 pathways and grade 5 units (CC BY); CFPB K-5 activities; DocsTeach, NPS, LOC items; Oak primary geography (OGL) | Core Knowledge HG, Michigan Open Book, NY toolkit, Oregon SB 13 | **Our own** |
| world-geo-6 World Geography and Ancient Civilizations I | None | Oak primary history (Egypt, Sumer, Indus, Shang) and geography (OGL, if accepted) | OpenStax World History 1, Core Knowledge, Michigan grade 7 | **Our own** |
| world-hist-7 World Geography and Ancient Civilizations II | None | Oak primary history (Greece, Rome, Early Islamic civilisation, Benin, Maya) (OGL, if accepted) | OpenStax World History 1, OER Project | **Our own** |
| us-hist-8 Civics | None | OpenStax American Government 3e text (CC BY, college, AI clause); US Courts activities; DocsTeach; Since Time Immemorial middle school unit | American Government 4e, iCivics (link) | **Our own** |
| world-hist-hs World History I (500 to 1800) | None | ETSU World History Since 1500 chapters for 1500 to 1800 (CC BY, college) | OpenStax World History 1 and 2, OER Project, New Visions | **Our own** |
| world-hist-2 World History II (1800 on) | None complete | **ETSU World History Since 1500 (CC BY 4.0, college)**: the nearest thing to a base text found | OpenStax World History 2, OER Project, New Visions | Our own, adapting ETSU text where it helps |
| us-hist-1 US History I (1763 to WWI) | None | Since Time Immemorial HS US History units; DocsTeach; NPS Teaching with Historic Places | OpenStax U.S. History, American Yawp, New Visions | **Our own** |
| us-hist-hs US History II (1920s on) | None | Same assets as us-hist-1 | OpenStax U.S. History, American Yawp | **Our own** |
| government (half year) | None clean | OpenStax American Government 3e text (CC BY, college, AI clause); US Courts; Since Time Immemorial Contemporary World Problems | American Government 4e | Our own; American Government 3e as a partial base only if Cory clears the AI clause |
| economics (half year, with personal finance) | **CFPB activities (public domain) for the personal finance half** | OpenStax Economics 2e, Macro 2e, Micro 2e text (CC BY, college, AI clause) | Economics 3e, Principles of Finance, Federal Reserve education (link) | Our own economics; personal finance built on CFPB |
| psychology | None clean | OpenStax Psychology 1e text (CC BY, 2014, college, AI clause) | Psychology 2e | Our own; Psychology 1e only if Cory clears the AI clause |

## Traps

1. **OpenStax AI clause on CC BY books.** The American Government 3e, Economics 2e and Psychology 1e prefaces say
   CC BY, then add "may not be used in the training of large language models" or ingested into "generative AI
   offerings" without written permission. A CC BY 4.0 grant cannot be narrowed by the licensor after the fact, but
   the clause states OpenStax's position, and Curio Class drafts with AI agents. A person should decide whether
   agents may read these books. The safe default is reference only, by a human, until Cory decides.
2. **Mixed licence wording on retired OpenStax pages.** The Economics 2e reuse paragraph says "Attribution License"
   then describes noncommercial and share-alike terms; the site footer on every book says CC BY-NC-SA; images,
   activities and assessments made by OpenStax are CC BY-NC-SA. If used: the text only, from the official retired
   PDF, saved with its copyright page and the catalogue record on the day taken. Never figures, questions or
   end-of-chapter material.
3. **Names and trademarks.** OpenStax and Rice names and covers, Since Time Immemorial logos ("property of their
   respective owners"), CFPB name and logo, the NPS Arrowhead, Oak branding: credit line only, no logos, no wording
   that implies endorsement.
4. **Tribal material needs care, not just a licence.** OSPI asks adapters not to change the content design or add
   cultural bias. The units are Washington-specific and tribally endorsed. Any Curio Class adaptation should keep
   tribal voices as written by the tribes and go through the fresh-agent sensitivity review (BASELINE rule).
5. **OGL is not on our list.** Oak's Open Government Licence v3.0 is attribution-only and Oak calls it equivalent
   to CC BY 4.0, but BASE-TEXTS.md names only CC BY 4.0, CC BY 3.0 and public domain. Adding OGL v3.0 is Cory's call.
   Collection 1 (legacy) Oak material is noncommercial and must not be mixed in; third-party items inside lessons
   keep their own terms.
6. **Federal does not mean public domain everywhere.** Federal Reserve Banks are private corporations: their
   education material is proprietary. Library of Congress and National Archives items are each labelled; many are
   in copyright or not evaluated. Check each item's rights line.
7. **College level.** Every CC BY textbook found (OpenStax retired editions, ETSU) is a college survey. Using them
   for grades 8 to 12 means rewriting for reading level anyway, which narrows the gain from adapting.
8. **Licences tightening again.** OpenStax moved its live social studies books to NC-SA; the CC BY editions now
   exist only as retired PDFs. If any is used, snapshot it now with its licence page and the date.

## Recommendation

- **No social studies course gets a full base text.** All eleven stay "our own", with the C3 skills and the
  Massachusetts 2018 anchor as BASE-TEXTS.md already says.
- **One clean partial base:** CFPB activities (public domain) for the personal finance half of economics.
- **Partial bases worth a decision by Cory:**
  1. ETSU World History Since 1500 (CC BY 4.0) for world-hist-2 and late world-hist-hs. Clean licence; college
     level. Recommended.
  2. Since Time Immemorial (CC BY 4.0) for the tribal sovereignty strand in grades 4, 5, 8 and 11 to 12, after a
     sensitivity review. Recommended as a strand, not a course.
  3. Oak National Academy (OGL v3.0) for ancient civilisations in world-geo-6 and world-hist-7, if Cory adds OGL
     v3.0 to the base-text bar.
  4. OpenStax American Government 3e, Economics 2e, Psychology 1e (CC BY, retired) for government, economics and
     psychology, only if Cory accepts the AI-clause risk; otherwise reference by a human only.
- **Assets for every course:** DocsTeach (CC0 activities), National Archives, Library of Congress and NPS items, US
  Courts activities, each checked item by item.
- **Subject order:** social studies has no base text, so by the plan **science goes second**. None of the partial
  bases is big enough to change that.

## Open items

- Cory: accept or reject OGL v3.0 as a base licence; decide on the OpenStax AI clause.
- Read the ETSU book's own copyright page and image credits before adapting (licence read on the repository page only).
- Open Oak KS3 history and geography unit lists and one lesson's licence footer.
- Confirm the US Courts reuse terms (website policies page returned 404).
- Retry c3teachers.org and the Library of Congress teachers pages later (timed out; 403).
- Check LibreTexts K12, Louisiana and other state social studies units, Facing History, Bill of Rights Institute.
- Watch Utah HB 488 (open social studies material for Utah).

## Sources (read 2026-11-13 unless marked)

- OpenStax catalogue data: https://openstax.org/apps/cms/api/v2/pages/?type=books.Book&fields=title,license_name,license_version,book_state,publish_date&limit=250
- OpenStax American Government 3e preface: https://openstax.org/books/american-government-3e/pages/preface
- OpenStax U.S. History preface: https://openstax.org/books/us-history/pages/preface
- OpenStax Psychology (1e) preface: https://openstax.org/books/psychology/pages/preface
- OpenStax Principles of Economics 2e preface: https://openstax.org/books/principles-economics-2e/pages/preface
- OpenStax K12 social studies: https://openstax.org/k12/social-studies
- Retired CC BY PDFs (from the catalogue, not downloaded): https://assets.openstax.org/oscms-prodcms/media/documents/AmericanGovernment3e-WEB.pdf ; https://assets.openstax.org/oscms-prodcms/media/documents/Economics2e-OP_s2jF42u.pdf ; https://assets.openstax.org/oscms-prodcms/media/documents/Psychology-OP.pdf
- The American Yawp: https://www.americanyawp.com/
- World History Since 1500 (ETSU): https://dc.etsu.edu/etsu-oer/13/
- History in the Making (search only): https://open.umn.edu/opentextbooks/textbooks/history-in-the-making-a-history-of-the-people-of-the-united-states-of-america-to-1877
- Since Time Immemorial: https://ospi.k12.wa.us/student-success/resources-subject-area/john-mccoy-lulilas-time-immemorial-tribal-sovereignty-washington-state ; elementary: https://ospi.k12.wa.us/student-success/resources-subject-area/time-immemorial-tribal-sovereignty-washington-state/elementary-curriculum
- Oregon SB 13: https://www.oregon.gov/ode/students-and-family/equity/NativeAmericanEducation/Pages/Senate-Bill-13-Tribal-HistoryShared-History.aspx ; OER Commons (blocked): https://oercommons.org/groups/oregon-office-of-indian-education/5067/10418/4443
- Montana IEFA (search only): https://opi.mt.gov/Educators/Teaching-Learning/Indian-Education-for-All/Indian-Education-Classroom-Resources
- Michigan Open Book Project: https://textbooks.wmisd.org/the-books.html
- C3 Teachers (timed out): https://c3teachers.org/ ; NY toolkit licence: S:\CurioClass-sources\reference-only-do-not-copy\new-york-ss-toolkit\NOTES.md
- New Visions licence (search only): https://www.newvisions.org/license-and-copyright-information
- Core Knowledge HG (search only): https://www.coreknowledge.org/history-geography/
- OER Project terms: https://www.oerproject.com/Terms-of-use
- iCivics terms: https://vision.icivics.org/terms-of-use
- Digital Inquiry Group FAQ: https://www.inquirygroup.org/faq
- Oak National Academy licensing: https://support.thenational.academy/a-guide-to-our-website-licensing ; llms.txt: https://www.thenational.academy/llms.txt ; primary history units: https://www.thenational.academy/teachers/curriculum/history-primary/units ; UK-only reversal (Tes): https://www.tes.com/magazine/news/general/oak-national-uk-restriction-u-turn-anger
- CFPB website policy: https://www.consumerfinance.gov/privacy/website-privacy-policy/ ; activities: https://www.consumerfinance.gov/consumer-tools/educator-tools/youth-financial-education/teach/activities/
- Federal Reserve education acceptable use: https://www.federalreserveeducation.org/support (redirected from https://www.stlouisfed.org/education/permitted-use)
- DocsTeach activities: https://docsteach.org/activities
- Library of Congress legal: https://www.loc.gov/legal/ ; teachers page (blocked): https://www.loc.gov/programs/teachers/about-this-program/
- NPS disclaimer: https://www.nps.gov/aboutus/disclaimer.htm ; Teaching with Historic Places: https://www.nps.gov/subjects/teachingwithhistoricplaces/index.htm
- US Courts educational resources: https://www.uscourts.gov/about-federal-courts/educational-resources
- Utah HB 488 (search only): https://le.utah.gov/Session/2026/bills/introduced/HB0488.pdf

## Follow-up: the open items, read 2026-11-13 (later, later.csv L9)

Read in Chrome; nothing downloaded.

| Item | What the source says | Verdict |
|---|---|---|
| C3 Teachers (c3teachers.org, loaded this time) | About page: the Inquiry Design Model "and related inquiry materials" are under CC BY-SA 4.0 (credit C3 Teachers, link the licence, share alike). Inquiry pages carry downloadable PDFs and Word files (one sampled: a Kentucky grade 11 Cold War inquiry, 2.0 MB). The New York toolkit copies we hold print CC BY-NC-SA. | Reference. CC BY-SA is not on the base-text bar (share-alike would bind the pages built from it), and some inquiries come from state partners with their own marks. The IDM form itself (question, supporting questions, tasks) is a method we already use, not text we copy. |
| Library of Congress teachers pages (loaded this time) | Primary source sets: "intended for classroom use. If your use will be beyond a single classroom, please review the copyright and fair use guidelines." No licence on the teacher guides. Items keep their own rights statements. | Assets item by item (each item's rights statement); teacher guides are reference only. |
| US Courts educational resources | No reuse terms on the educational resources page or the Privacy and Security Policy page (the old website policies page is gone). | Federal government works are public domain by statute (17 U.S.C. 105), so US Courts' own activities and scripts may be adapted with a credit line; photos and outside items inside them are checked one by one. Rests on the statute, not a stated policy. |
| LibreTexts K12 (social studies shelves) | Three books: Economics, Geography (eleven regional units) and United States Government, each "shared under a CK-12 license", built from El Paso ISD CK-12 FlexBooks. | Reference only: the CK-12 licence is noncommercial. |
| Louisiana (Bayou Bridges, K to 8) | Built by the Core Knowledge Foundation with the Louisiana Department of Education; Core Knowledge terms: free to adapt and share with attribution, selling prohibited (its Creative Commons licence is noncommercial); images in the PDFs may not be extracted. | Reference only, like Core Knowledge history and geography. |
| Since Time Immemorial unit files | They live on one OSPI page per unit (the main page links only standards). 17 unit pages: K to 3 pathways 1 to 3 (24 PDFs, 4.9 MB); grade 5 US history units 1 to 3 (42 files, 95.5 MB); middle school unit 1C, Medicine Creek Treaty (16 PDFs, 4.1 MB); high school US history units 1 to 6 (73 PDFs, 163 MB); Contemporary World Problems units 1 to 4 (39 PDFs, 125 MB). About 194 files, 392 MB, some in Spanish too. | Ready to load on Cory's yes (CC BY 4.0, read earlier). The grade 4 Washington state units are left out (a state study). |
| CFPB youth financial education | 135 activities across 14 listing pages, about three PDFs each (guide, worksheet, handout); three sampled are 84 to 156 KB. About 400 PDFs, roughly 50 MB. | Ready to load on Cory's yes (public domain). |
| Oak National Academy KS3 | History years 7 to 9: 40 units (medieval Islamic worlds, Mali, the Silk Road, conquest of the Americas, transatlantic slavery, the Mughal Empire, the Enlightenment, the French, Haitian, Industrial and Russian revolutions, both world wars, the Holocaust, decolonisation, and many British topics). Geography years 7 to 9: 20 units (weather and climate, population, biomes, India, China, globalisation, tectonic hazards, development, cities, the DRC, Nigeria, rivers, resources, the Middle East, glaciers, Russia, the Anthropocene). Lesson footer read (a KS3 geography lesson): "licensed on Open Government Licence version 3.0 ... except where otherwise stated". | Partial base for world history and geography units, unit by unit (OGL v3.0, accepted 2026-11-13). No bulk download; lessons are taken per unit when a course needs them. |

Not read: Facing History and the Bill of Rights Institute (expected noncommercial or all rights reserved; read only if a unit needs them).
