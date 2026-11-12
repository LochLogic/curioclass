# Approach-to-teaching sources: access audit

Audit date: 2026-11-11. Purpose: confirm that every source the Curio Class "approach to teaching" document would cite can actually be obtained and read.

## How this was tested

- Every URL below was requested live (curl with a browser user agent) and the HTTP status and content type recorded. Nothing here relies on memory for reachability.
- HTML pages were then read with WebFetch to confirm real content came back.
- **Every PDF tested returns binary through WebFetch** (12 of 12 tried, plus one over the 10 MB WebFetch size cap). This is a tool limit, not a problem with the files. Each PDF was then streamed into PyMuPDF in memory to confirm a real text layer; page and word counts are given. Local tools that work on this PC: `pdftotext` (Git Bash, file input only, not stdin) and Python `pymupdf` / `pypdf`.
- Side effect to know about: WebFetch saves a copy of each binary PDF it fetches into the session `tool-results` folder, so those copies can be text-extracted directly.
- Sites that refuse automated clients: Sage Journals and Taylor and Francis (403 to curl and WebFetch), web.archive.org (429 to curl, refused by WebFetch), NCTM and the EEF toolkit page (WebFetch refused, curl fine), PMC (bot check for WebFetch).

Access codes used in the tables:

- **HTML full**: full text read as HTML through WebFetch.
- **HTML part**: page read, but only part of the source is on it.
- **PDF, extracts**: reachable; WebFetch gives binary; text layer confirmed (pages / words). Needs local download and text extraction to read.
- **PDF, scan**: reachable but image only, needs OCR.
- **Landing only**, **Blocked**, **Paywalled**, **Not found**: as named.

## 1. Shared core (learning science and instruction)

| Source | Publisher, year | Best URL | Access result | Licence or reuse terms as stated | Use |
|---|---|---|---|---|---|
| Rosenshine, Principles of Instruction (article) | American Educator (AFT), Spring 2012 | https://www.aft.org/sites/default/files/Rosenshine.pdf (landing: https://www.aft.org/ae/spring2012/rosenshine) | PDF, extracts (9 pp / 7,205 words). Landing page is header only. | AFT site: all rights reserved, text not to be used without AFT permission. Article says adapted with permission from the IAE booklet. | Core citation for worked examples, small steps, guided practice, review. |
| Rosenshine, Principles of Instruction (booklet, Educational Practices Series 21) | International Academy of Education / UNESCO IBE, 2010 | http://www.iaoed.org/downloads/EdPractices_21.pdf (plain http only; https and the bare site fail) | PDF, extracts (32 pp / 8,291 words). All IBE-hosted URLs tried return 404; unesdoc is a JavaScript shell. | No reuse statement matched in the text search; check the inside cover on extraction. | Longer version with the research notes behind each principle. |
| Deans for Impact, The Science of Learning | Deans for Impact, 2015 | https://www.deansforimpact.org/files/assets/thescienceoflearning.pdf | PDF, extracts (18 pp / 9,328 words). Note: the file now at this URL is marked "Second Edition"; confirm its date on extraction before citing as 2015. | No licence statement matched in the text. | Six-question summary of cognitive science for teaching; plain-language anchor. |
| Pashler et al., Organizing Instruction and Study to Improve Student Learning | IES (NCER 2007-2004), 2007 | https://ies.ed.gov/ncee/wwc/Docs/PracticeGuide/20072004.pdf | PDF, extracts (63 pp / 28,013 words) | "This report is in the public domain." | Spacing, interleaved worked examples, quizzing, graphics with words, deep questions. |
| Dunlosky, Strengthening the Student Toolbox | American Educator (AFT), Fall 2013 | https://www.aft.org/ae/fall2013/dunlosky (PDF: https://www.aft.org/sites/default/files/dunlosky_0.pdf; the old dunlosky.pdf is 404) | HTML full (whole article and endnotes on the page). PDF also extracts (10 pp / 7,917 words). | AFT: all rights reserved, permission needed for reuse. | Practice testing and distributed practice as the strongest techniques. |
| Dunlosky et al., Improving Students' Learning With Effective Learning Techniques | Psychological Science in the Public Interest (Sage), 2013 | https://journals.sagepub.com/doi/10.1177/1529100612453266 | Blocked (403 to automated clients). Could not confirm free access from here; open it in a browser. | Not seen. | The full monograph behind the summary above. Substitute: the American Educator article. |
| How People Learn, expanded edition | National Academies Press, 2000 | https://www.nationalacademies.org/read/9853/chapter/1 (nap.nationalacademies.org/catalog/9853 redirects here) | HTML full, chapter by chapter (chapter/3 read as text, about 100k characters per chapter). Free PDF needs a guest email sign-up. | "Copyright 2000 by the National Academy of Sciences. All rights reserved." Terms of Use page not read. | Prior knowledge, understanding over facts, metacognition. |
| How People Learn II | National Academies Press, 2018 | https://www.nationalacademies.org/read/24783/chapter/1 | HTML full, chapter by chapter (chapter/3 read as text). Free PDF needs guest sign-up. | NAS all rights reserved (site footer); no open licence stated. | Culture, motivation, context; updates the 2000 volume. |
| Kirschner, Sweller, Clark, Why Minimal Guidance During Instruction Does Not Work | Educational Psychologist (Taylor and Francis), 2006 | https://www.tandfonline.com/doi/abs/10.1207/s15326985ep4102_1 | Blocked (403). An unofficial course-hosted copy is reachable and extracts (12 pp / 10,489 words): https://www.davidlewisphd.com/courses/EDD8121/readings/2006-Kirschner_et_al.pdf | "Copyright 2006, Lawrence Erlbaum Associates." The course copy is not an authorised host. | The case for explicit guidance for novices. |
| Clark, Kirschner, Sweller, Putting Students on the Path to Learning | American Educator (AFT), Spring 2012 | https://www.aft.org/sites/default/files/Clark.pdf | PDF, extracts (6 pp / 5,616 words) | AFT: all rights reserved. | Legitimate free version of the Kirschner argument; cite this one. |
| Hmelo-Silver, Duncan, Chinn, Scaffolding and Achievement in Problem-Based and Inquiry Learning | Educational Psychologist, 2007 | https://www.tandfonline.com/doi/abs/10.1080/00461520701263368 | Blocked / paywalled. No legitimate free copy verified (old USC host is dead, ResearchGate 403). | Not seen. | The counterpoint: inquiry with heavy scaffolding is not "minimal guidance". |
| Sinha and Kapur, When Problem Solving Followed by Instruction Works | Review of Educational Research (Sage), 2021 | https://doi.org/10.3102/00346543211019105 | Blocked (403). Could not confirm open access from here. | Not seen. | Productive failure meta-analysis; balanced counterpoint. |
| Black and Wiliam, Inside the Black Box | Phi Delta Kappan, October 1998 | https://kappanonline.org/inside-the-black-box-raising-standards-through-classroom-assessment/ | HTML full (through "Are We Serious About Raising Standards?" and references) | "(c) 1998 Phi Delta Kappa International. All rights reserved." | Formative assessment evidence base. |
| Leahy, Lyon, Thompson, Wiliam, Classroom Assessment: Minute by Minute, Day by Day | ASCD Educational Leadership, November 2005 | https://www.ascd.org/el/articles/classroom-assessment-minute-by-minute-day-by-day | HTML full (labelled "Premium Resource" but the full text came back) | ASCD all rights reserved. | Wiliam's five formative assessment strategies in short form. |
| EEF Teaching and Learning Toolkit | Education Endowment Foundation, living resource | https://educationendowmentfoundation.org.uk/education-evidence/teaching-learning-toolkit | Reachable (curl 200); WebFetch refused (403). Read it in a browser or via curl. | Copyright EEF in page metadata; reuse terms not seen. | Impact, cost and evidence ratings by strand; one-to-one tuition strand at .../teaching-learning-toolkit/one-to-one-tuition (200). |
| EEF, Metacognition and Self-Regulated Learning guidance report | EEF, v2.4.0 | https://d2tic4wvo1iusb.cloudfront.net/production/eef-guidance-reports/metacognition/metacognition-and-self-regulated-learning_guidance-report.v.2.4.0.pdf | PDF, extracts (50 pp / 11,161 words) | No licence line matched in the text. | Seven recommendations on teaching metacognition. |
| EEF, Teacher Feedback to Improve Pupil Learning | EEF, 2021 | https://d2tic4wvo1iusb.cloudfront.net/production/eef-guidance-reports/feedback/Teacher_Feedback_to_Improve_Pupil_Learning.pdf | PDF, extracts (55 pp / 20,921 words). 11.5 MB, over the WebFetch cap. | No licence line matched. | Feedback principles; relevant to automated feedback in tools. |
| CAST UDL Guidelines 3.0 | CAST, 2024 (released 2024-07-30) | https://udlguidelines.cast.org/ | HTML full (three principles, nine guidelines, citation). Downloads page at /more/downloads/ (200). | "(c) CAST, Inc." Terms of Use page not read; cast.org permissions page 404. | Access and representation design. Citation: CAST (2024), UDL Guidelines version 3.0. |
| WIDA English Language Development Standards Framework, 2020 Edition | WIDA, University of Wisconsin, 2020 | https://wida.wisc.edu/sites/default/files/resource/WIDA-ELD-Standards-Framework-2020.pdf | PDF, extracts (392 pp / 136,976 words) | "(c) 2020 Board of Regents of the University of Wisconsin System"; suggested citation in the file. | Language expectations and key language uses by grade cluster. |
| ELSF Guidelines for Improving Math Materials for English Learners | English Learners Success Forum | https://cdn.prod.website-files.com/681105d2cd8d422bfde21cb3/681105d2cd8d422bfde223ad_elsf-math-guidelines.pdf | PDF, extracts (14 pp / 4,531 words). The landing page puts a contact form in front, but this direct link works. | "Creative Commons Attribution 4.0 International License" (in the file). | Five focus areas for multilingual learner supports in math. |
| ELSF Guidelines for Improving ELA Materials for English Learners | English Learners Success Forum | https://cdn.prod.website-files.com/681105d2cd8d422bfde21cb3/681105d2cd8d422bfde223ae_elsf-ela-guidelines.pdf | PDF, extracts (16 pp / 5,369 words) | CC BY 4.0 (in the file). | Same, for the later ELA page. |
| WWC, Teaching Academic Content and Literacy to English Learners in Elementary and Middle School | IES (NCEE 2014-4012), 2014 | https://ies.ed.gov/ncee/wwc/Docs/PracticeGuide/english_learners_pg_040114.pdf | PDF, extracts (115 pp / 45,517 words) | Public domain. | Four recommendations on academic vocabulary and language in content teaching. |
| EdReports MLL Supports Evidence Guide v2.0, Math K-8 | EdReports, updated 07/2025 | https://cdn.edreports.org/media/2026/06/MLL-Math%20K-8%20Evidence%20Guide_2.0.pdf | PDF, extracts (94 pp / 32,874 words) | "(c) EdReports, All Rights Reserved" | What reviewers look for in multilingual learner supports. |
| EdReports MLL Review Criteria v2.0, Math K-12 | EdReports, updated 07/2025 | https://cdn.edreports.org/media/2026/06/MLL-Math%20K-12%20Review%20Criteria_2.0.pdf | PDF, extracts (6 pp / 1,409 words) | All rights reserved. | Short criteria list. |
| EdReports MLL Evidence Guides v2.0, other subjects | EdReports, 07/2025 | ELA 3-5: https://cdn.edreports.org/media/2026/06/MLL-ELA%203-5%20Evidence%20Guide_2.0.pdf ; Science 6-8: https://cdn.edreports.org/media/2026/06/MLL-Science%206-8%20Evidence%20Guide_2.0.pdf | PDF, extracts (113 pp and 48 pp). ELA K-2, math HS and science HS guides exist on the same CDN (not individually tested). Index: https://edreports.org/process/review-tools | All rights reserved. | Later pages. |
| Mayer, principles of multimedia learning | Mayer; Cambridge University Press (book) | Free one-page list: https://ugc.futurelearn.com/uploads/files/7d/d6/7dd6188d-c343-4311-b064-ac98d2c95abc/Multimedia_Principles._R._E._Mayer__2020.pdf | PDF, extracts (1 p / 342 words): a list only, third-party handout. No authoritative free summary by Mayer verified; his review articles are paywalled. | Not stated. | Coherence, signalling, redundancy, contiguity, segmenting for tool screens. |
| PhET research on interactive simulations | University of Colorado Boulder | https://phet.colorado.edu/en/research ; sample paper: https://phet.colorado.edu/publications/PhET_Interviews_I.pdf (Adams et al. 2008, Part I) | HTML full (publication list with links). Sample PDF extracts (33 pp / 9,462 words). | Footer: "University of Colorado. Some rights reserved"; specific licence not seen. | Implicit scaffolding and engaged exploration in simulation design. |
| Moyer-Packenham and Westenskow, virtual manipulatives meta-analysis | IJVPLE 2013; follow-up chapter IGI Global 2016 | https://digitalcommons.usu.edu/teal_facpub/2399/ | Landing only: record says full text "not available here", publisher DOI only. A third-party copy of the 2013 paper did not resolve. | Publisher copyright. | Effect of virtual manipulatives on achievement. |
| Bloom, The 2 Sigma Problem | Educational Researcher, 1984 | https://gwern.net/doc/psychology/1984-bloom.pdf (text layer); https://web.mit.edu/5.95/readings/bloom-two-sigma.pdf (scan) | gwern copy: PDF, extracts (14 pp / 10,420 words). MIT copy: PDF, scan (15 pp, no text layer). Publisher page is restricted. | AERA / Sage copyright; both free copies are unofficial hosts. | One-to-one tutoring and mastery learning. |
| Nickow, Oreopoulos, Quan, The Impressive Effects of Tutoring on PreK-12 Learning (added) | NBER Working Paper 27476, 2020 | https://www.nber.org/system/files/working_papers/w27476/w27476.pdf | PDF, extracts (84 pp / 25,618 words) | (c) authors; short quotations up to two paragraphs allowed with credit. | Modern, stronger evidence for one-to-one instruction than Bloom alone. |

## 2. Mathematics

| Source | Publisher, year | Best URL | Access result | Licence or reuse terms as stated | Use |
|---|---|---|---|---|---|
| Progressions for the Common Core State Standards for Mathematics, compiled edition | Common Core Standards Writing Team, 2023 | https://mathematicalmusings.org/wp-content/uploads/2023/05/Progressions.pdf (linked from the home page; an earlier 2023/02 build of 332 pp is also live) | PDF, extracts (333 pp / 188,385 words). 11.5 MB, over the WebFetch cap, so local download is the only route. | "Creative Commons Attribution (CC BY) license", CC BY 4.0, (c) Common Core Standards Writing Team. | The content backbone: how each domain develops across grades. |
| K-8 Publishers' Criteria for the CCSS for Mathematics | CCSS lead writers, Spring 2013 (04/09/2013) | https://achievethecore.org/content/upload/Math_Publishers_Criteria_K-8_Spring_2013_FINAL.pdf | PDF, extracts (22 pp / 10,550 words) | No licence line matched. | Focus, coherence, rigor criteria that adoption rubrics descend from. |
| Common Core State Standards for Mathematics, including the Standards for Mathematical Practice | NGA Center and CCSSO, 2010 | https://corestandards.org/wp-content/uploads/2023/09/Math_Standards1.pdf (ADA version also linked from https://corestandards.org/) | PDF, extracts (93 pp / 39,574 words). The old HTML practice page is gone (corestandards.org/Math/Practice 404; thecorestandards.org returns 511). | No licence line matched in the PDF; the public licence page is 404 on the current site. | Exact Standards for Mathematical Practice text. |
| SAP Focus by Grade Level (K-8, and one per grade) | Student Achievement Partners, 2014 | https://achievethecore.org/page/634/focus-in-mathematics ; K-8 file: https://achievethecore.org/content/upload/SAP%20Focus%20Math%20K%E2%80%938%2011.12.14.pdf ; per grade: https://achievethecore.org/content/upload/SAP_Focus_Math_4.pdf (swap the digit) | PDF, extracts (K-8: 10 pp / 5,303 words; grade 4: 2 pp / 1,168 words) | No licence line matched. See the provenance note below. | Major, supporting, additional clusters per grade. |
| SAP Coherence Map | Student Achievement Partners | https://tools.achievethecore.org/coherence-map/ | Landing only for text tools: it is a JavaScript application (10 KB shell), so content must be used in a browser. | Not seen. | Standard-to-standard connections. |
| SAP rigor and shifts documents | Student Achievement Partners | https://achievethecore.org/page/1090/rigor ; shifts list: https://achievethecore.org/category/1147/shifts-in-mathematics | HTML part. The linked "rigor" PDF is a one-page graphic (14 words). The older /page/900/the-shifts URL now returns a soft 404. | Not seen. | Three aspects of rigor wording. The Publishers' Criteria covers this better. |
| WWC, Developing Effective Fractions Instruction for K-8 | IES (NCEE 2010-4039), 2010 | https://ies.ed.gov/ncee/wwc/Docs/PracticeGuide/fractions_pg_093010.pdf | PDF, extracts (90 pp / 39,652 words) | Public domain. | Fractions as numbers, number lines, sharing. |
| WWC, Improving Mathematical Problem Solving in Grades 4 Through 8 | IES, 2012 | https://ies.ed.gov/ncee/wwc/Docs/PracticeGuide/MPS_PG_043012.pdf | PDF, extracts (92 pp / 40,699 words) | Public domain. | Problem-solving instruction, visual representations, multiple strategies. |
| WWC, Assisting Students Struggling with Mathematics: Intervention in the Elementary Grades | IES (WWC 2021006), 2021 | https://ies.ed.gov/ncee/wwc/Docs/PracticeGuide/WWC2021006-Math-PG.pdf | PDF, extracts (165 pp / 62,778 words) | Public domain. | Systematic instruction, mathematical language, representations, number lines, word problems, timed activities. |
| WWC, Teaching Math to Young Children | IES, 2013 | https://ies.ed.gov/ncee/wwc/Docs/PracticeGuide/early_math_pg_111313.pdf | PDF, extracts (165 pp / 83,293 words) | Public domain. | Early number and operations progressions. |
| WWC, Teaching Strategies for Improving Algebra Knowledge | IES, 2015 | https://ies.ed.gov/ncee/wwc/Docs/PracticeGuide/wwc_algebra_040715.pdf | PDF, extracts (71 pp / 31,791 words) | Public domain. | Solved problems, structure, multiple strategies. |
| National Mathematics Advisory Panel, Foundations for Success | US Department of Education, 2008 | https://files.eric.ed.gov/fulltext/ED500486.pdf | PDF, extracts (120 pp / 34,223 words). The ed.gov original is 404. | "This report is in the public domain. Authorization to reproduce it in whole or in part is granted." | Conceptual understanding, fluency and problem solving as mutually reinforcing. |
| Adding It Up | National Research Council / NAP, 2001 | https://www.nationalacademies.org/read/9822/chapter/1 | HTML full, chapter by chapter (chapter/6 = "The Strands of Mathematical Proficiency", 163k characters). Free PDF needs guest sign-up. | NAS copyright; no open licence stated. | Five strands of mathematical proficiency. |
| NCTM, Principles to Actions executive summary (includes the eight effective mathematics teaching practices) | NCTM, 2014 | https://www.nctm.org/uploadedFiles/Standards_and_Positions/PtAExecutiveSummary.pdf | PDF, extracts (6 pp / 2,982 words). WebFetch gets HTTP 402 from NCTM; curl gets the file. The full book is paid. | No licence line matched; NCTM copyright. | The eight teaching practices, quotable source. |
| Illustrative Mathematics K-5, Design Principles | Illustrative Mathematics / Kendall Hunt, 2021 | https://im.kendallhunt.com/k5/teachers/teacher-guide/design-principles.html (curriculum.illustrativemathematics.org redirects here); also .../teacher-guide/how-to-use-the-materials.html and about-these-materials.html | HTML full (11 principle headings including the 5 Practices, task complexity, purposeful representations) | "Licensed under the Creative Commons Attribution 4.0 license. (c) 2021 Illustrative Mathematics." Name and logo excluded from the licence. | Model of how a top-rated curriculum states its approach. |
| Illustrative Mathematics 6-8, Design Principles | Open Up Resources / Illustrative Mathematics, 2017-2019 | https://im.kendallhunt.com/MS/teachers/design_principles.html | HTML full | CC BY 4.0; (c) 2017-2019 Open Up Resources, adaptations (c) 2019 Illustrative Mathematics. | Same, middle grades. |
| Eureka Math, A Story of Units: A Curriculum Overview for Grades P-5 | Great Minds, 2015 | https://greatminds.org/hubfs/knowledge/resources/math/EM_Basic_Curriculum_Files/Curriculum_Overview/EM_GPK5_CurriculumOverview.pdf ; map: .../Curriculum%20Map/EM_GPK5_CurriculumMap.pdf | PDF, extracts (66 pp / 24,068 words). The landing page shows a form gate but the direct file link works. engageny.org now redirects to an NYSED page whose math files sit in a SharePoint folder (not tested). | "(c) 2015 Great Minds." No Creative Commons statement in this file. The 2013 EngageNY edition carried a CC licence, but no live official copy of it was found. | Coherence story, module sequence, rationale. Read only; do not reuse text. |
| Smith and Stein, 5 Practices | NCTM / Corwin, 2011 | Free one-page list: https://stemtc.scimathmn.org/sites/default/files/downloads/5_practices_for_orchestrating_productive_math_discussions.pdf | PDF, extracts (1 p / 181 words). Book is paid. | Not stated. | Anticipate, monitor, select, sequence, connect. Better free source: the "Using the 5 Practices" section of the IM K-5 Design Principles (CC BY 4.0). |
| Concrete-representational-abstract research | Various | No free synthesis verified. Bouck et al. 2018 and the 2025 meta-analysis are paywalled; Fyfe et al. 2014 author page had no file link. | Not found (free). | n/a | Substitutes that are free and confirmed reachable: WWC 2021 intervention guide and the EEF maths guidance report (both above and below); check on extraction which recommendations cover representations and manipulatives. |
| EEF, Improving Mathematics in Key Stages 2 and 3 | EEF, 2022 update | https://d2tic4wvo1iusb.cloudfront.net/production/eef-guidance-reports/maths-ks-2-3/EEF-Improving-Mathematics-in-Key-Stages-2-and-3-2022-Update.pdf | PDF, extracts (38 pp / 12,094 words) | No licence line matched. | Manipulatives and representations, misconceptions, problem solving. |
| EdReports Core Content Evidence Guide v2.0, Mathematics K-8 | EdReports, updated 07/2025 | https://cdn.edreports.org/media/2026/06/Math%20K-8%20Evidence%20Guide_2.0.pdf (same file is linked from https://edreports.org/process/review-tools/math); criteria: https://cdn.edreports.org/media/2026/06/Math%20K-8%20Review%20Criteria_2.0.pdf | PDF, extracts (112 pp / 30,804 words); read locally for the summary below. | "(c) EdReports, All Rights Reserved" | The indicator the approach document must satisfy. |
| NYSED mathematics briefs, Brief 1: The Research Base for Mathematics Teaching and Learning (added) | New York State Education Department | https://www.nysed.gov/sites/default/files/programs/standards-instruction/nysed-brief-1-the-research-base-for-mathematics-teaching-and-learning.pdf (briefs 2, 3, 5 alongside) | PDF, extracts (4 pp / 2,182 words) | No licence line matched. | A state agency's own short research statement; useful model for tone and length. |

### EdReports Math K-8 v2.0: where the instructional approach and research base are judged (own-words summary)

- **Indicator 3e** (Gateway 3 Teacher and Student Supports, Criterion 3.1 Teacher Supports) is the one. It asks whether the materials explain the program's instructional approaches, identify the research-based strategies used, and explain the role of the standards.
- Scoring is 0, 1 or 2. Full credit needs all three parts present. One or two of the three earns 1. None earns 0.
- Reviewers are told to look for: a clear overview of the approaches and how they steer teaching and learning; a description of how those approaches show up in actual lessons and activities; explicit references to research, with citations to studies; the reasoning for choosing each strategy; and a clear account of how the program lines up with the standards.
- Criterion 3.1 is worth 10 points in total (9 to 10 meets, 5 to 8 partially meets). Its other indicators: 3a teacher guidance for enacting the materials (2 points), 3b adult-level explanations of the mathematics and how it connects across grades (2 points), 3c year-long scope and sequence with standards correlation, 3d communication to students and caregivers (narrative evidence only), 3f supply list, 3g assessment system and guidance for next steps (2 points), 3h not assessed in mathematics.
- Related narrative-only indicators later in Gateway 3 (3r to 3u) cover how digital technology is integrated and the teacher guidance for it; relevant because Curio Class is tool-first.
- Oddity to be aware of: the guide's cover lists indicators 1a to 1g and 2a to 2i, but the body runs 1a to 1h and 2a to 2l. Cite indicator numbers from the body pages.

## 3. For later pages (science and ELA)

| Source | Publisher, year | Best URL | Access result | Licence or reuse terms as stated | Use |
|---|---|---|---|---|---|
| A Framework for K-12 Science Education | National Research Council / NAP, 2012 | https://www.nationalacademies.org/read/13165/chapter/1 | HTML full, chapter by chapter (chapter/7 = Dimension 1, practices). Free PDF needs guest sign-up. | NAS copyright; no open licence stated. | Three-dimensional learning. |
| NGSS Appendix A, Conceptual Shifts | NGSS Lead States, April 2013 | https://www.nextgenscience.org/sites/default/files/resource/files/Appendix%20A%20-%204.11.13%20Conceptual%20Shifts%20in%20the%20Next%20Generation%20Science%20Standards.pdf | PDF, extracts (5 pp) | NGSS public licence: states, districts, schools, teachers and non-profit education entities may copy and adapt; NGSS name is a trademark with its own rules (https://www.nextgenscience.org/ngss-trademarks-and-copyright/ngss-trademarks-and-copyright, read as HTML). | Shifts. |
| NGSS Appendix E, DCI Progressions | as above (file dated 061617) | https://www.nextgenscience.org/sites/default/files/resource/files/AppendixE-ProgressionswithinNGSS-061617.pdf | PDF, extracts (8 pp) | as above | Progressions. |
| NGSS Appendix F, Science and Engineering Practices | as above | https://www.nextgenscience.org/sites/default/files/resource/files/Appendix%20F%20%20Science%20and%20Engineering%20Practices%20in%20the%20NGSS%20-%20FINAL%20060513.pdf | PDF, extracts (33 pp) | as above | Practices by grade band. |
| NGSS Appendix G, Crosscutting Concepts | as above | https://www.nextgenscience.org/sites/default/files/resource/files/Appendix%20G%20-%20Crosscutting%20Concepts%20FINAL%20edited%204.10.13.pdf | PDF, extracts (17 pp) | as above | Crosscutting concepts. All appendices listed at https://www.nextgenscience.org/resources/ngss-appendices |
| 3-5-ETS1 evidence statements | NGSS, June 2015 | 3-5-ETS1-1: https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/3-5-ETS1-1%20Evidence%20Statements%20June%202015%20asterisks-4.pdf ; K-5 ETS bundle: https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/K-5%20ETS%20Evidence%20Statements%20June%202015%20asterisks.pdf | PDF, extracts (1 p and 6 pp). The same name without "-4" is 404. ETS1-2 and ETS1-3 are inside the bundle. | as above | Engineering design evidence. |
| EQuIP Rubric for Lessons and Units: Science, v3.0 | Achieve / NextGenScience, September 2016 | https://www.nextgenscience.org/sites/default/files/EQuIPRubricforSciencev3.pdf | PDF, extracts (14 pp / 6,200 words) | Creative Commons Attribution 3.0 Unported (in the file). | Unit quality criteria. |
| CCSS ELA Appendix A | NGA Center and CCSSO, 2010 | https://www.oregon.gov/ode/educator-resources/standards/ELA/Documents/ela-appendix-a.pdf (also on nysed.gov, 43 pp) | PDF, extracts (46 pp / 23,811 words). The corestandards.org original is 404; Wayback has a 2022 capture but refuses automated fetches. | No licence line matched. | Research behind text complexity, foundational skills, writing. |
| Supplement to Appendix A, New Research on Text Complexity | NGA Center and CCSSO, 2012 | https://achievethecore.org/content/upload/Appendix-A-New-Research-on-Text-Complexity-revised%20(1).pdf | PDF, extracts (10 pp / 4,796 words). The older E0813 URL is a soft 404. | No licence line matched. | Quantitative bands. |
| CCSS ELA Appendix B | NGA Center and CCSSO, 2010 | https://www.oregon.gov/ode/educator-resources/standards/ELA/Documents/ela-appendix-b.pdf (also achievethecore.org/content/upload/corestandards_appendix_b_text_exemplars_sample_performance_task.pdf, 183 pp) | PDF, extracts (254 pp / 116,195 words) | The file's own "Copyright and Permissions" section: exemplar excerpts used by permission or fair use; do not republish excerpts. | Text exemplars and sample tasks. |
| Writing Next | Carnegie Corporation of New York, 2007 | https://carnegie.org/wp-content/uploads/2026/01/ccny_report_2007_writing.pdf | PDF, extracts (77 pp / 26,772 words) | No reproduction without permission from Carnegie Corporation. | Eleven elements of adolescent writing instruction. |
| Reading Next | Carnegie Corporation of New York, 2004 | https://carnegie.org/wp-content/uploads/2026/01/ccny_report_2004_reading.pdf | PDF, extracts (59 pp / 20,466 words) | (c) 2004 Carnegie Corporation, all rights reserved. | Fifteen elements of adolescent literacy. |
| WWC, Foundational Skills to Support Reading for Understanding, K-3 | IES, 2016 | https://ies.ed.gov/ncee/wwc/Docs/PracticeGuide/wwc_foundationalreading_040717.pdf | PDF, extracts (123 pp / 58,873 words) | Public domain. | Foundational reading. |
| WWC, Teaching Elementary School Students to Be Effective Writers | IES, 2012 (revised 2018) | https://ies.ed.gov/ncee/wwc/Docs/PracticeGuide/WWC_Elem_Writing_PG_Dec182018.pdf | PDF, extracts (118 pp / 50,897 words) | Public domain. | Elementary writing. |
| WWC, Teaching Secondary Students to Write Effectively | IES, 2016 | https://ies.ed.gov/ncee/wwc/Docs/PracticeGuide/wwc_secondary_writing_110116.pdf | PDF, extracts (97 pp / 42,773 words) | Public domain. | Secondary writing. |
| WWC, Improving Reading Comprehension in K-3 (added) | IES, 2010 | https://ies.ed.gov/ncee/wwc/Docs/PracticeGuide/readingcomp_pg_092810.pdf | PDF, extracts (87 pp / 39,566 words) | Public domain. | Comprehension strategies. |
| WWC, Providing Reading Interventions for Students in Grades 4-9 (added) | IES, 2022 | https://ies.ed.gov/ncee/wwc/Docs/PracticeGuide/WWC-practice-guide-reading-intervention-full-text.pdf | PDF, extracts (204 pp / 74,440 words) | Public domain. | Upper-grade reading. |
| SAP text complexity materials | Student Achievement Partners | https://achievethecore.org/page/2725/text-complexity ; Why Text Complexity Matters: https://achievethecore.org/content/upload/Why_Text_Complexity_Matters.pdf | HTML part (page lists rubrics and tools); PDF extracts (10 pp / 3,589 words) | Not seen. | Qualitative rubrics, rationale. |
| SAP knowledge-building materials | Student Achievement Partners | Research Supporting Shift 3, Building Knowledge: https://achievethecore.org/content/upload/Research%20Supporting%20Shift%203%20-%20Building%20Knowledge%5B1%5D.pdf ; Research Supporting the ELA Standards and Shifts: https://achievethecore.org/content/upload/Research%20Supporting%20the%20ELA%20Standards%20and%20Shifts%20Final.pdf | PDF, extracts (3 pp and 17 pp) | Not seen. | Annotated bibliographies for knowledge building. Index of research pages: https://achievethecore.org/category/420/research-and-articles |
| Kamil and others, Improving Adolescent Literacy: Effective Classroom and Intervention Practices (added 2026-11-12) | IES practice guide, 2008 | https://ies.ed.gov/ncee/wwc/Docs/PracticeGuide/adlit_pg_082608.pdf | PDF, extracts (65 pp; word count not recorded). Opened by the curriculum expert on 2026-11-11 with curl and a browser user agent, text taken out with pymupdf. Not re-tested for this entry. Read in part: the checklist (PDF 15 to 16), the level-of-evidence paragraph of all five recommendations (PDF 17, 22, 27, 32, 37) and step 4 of recommendation 2 (PDF 24). | Public domain. | Grades 4 to 12. Vocabulary strong, comprehension strategies strong, discussion moderate, motivation moderate, specialist help strong. Its levels are strong, moderate and low. |
| National Reading Panel, Teaching Children to Read: Reports of the Subgroups (added 2026-11-12) | NICHD, 2000 | https://www.nichd.nih.gov/sites/default/files/publications/pubs/nrp/Documents/report.pdf | PDF, extracts (449 pp; word count not recorded). Opened by the expert the same way. Not re-tested for this entry. Read in part: PDF 192 (3-3) and PDF 216 (3-28) of the fluency chapter, and the paragraph on its search. | Public domain. | Chapter 3, fluency: guided oral rereading supported; independent silent reading not shown to help. |
| Hasbrouck and Tindal, An Update to Compiled ORF Norms, Technical Report 1702 (added 2026-11-12) | University of Oregon, 2017 | https://files.eric.ed.gov/fulltext/ED594994.pdf | PDF, extracts (20 pp; word count not recorded). Opened by the expert the same way. Not re-tested for this entry. Read in part: the grade 5 and 6 table, PDF 16 (printed page 13). | All rights reserved; read and cite the figures only. | Oral reading norms by grade and season. |

## Provenance note on achievethecore.org

The pages currently served at achievethecore.org and tools.achievethecore.org carry Internet Archive markers in their HTML ("FILE ARCHIVED ON ... RETRIEVED FROM THE INTERNET ARCHIVE") and developer comments about a "rebuild" from a Wayback capture. The site appears to be a restored copy, not the organisation's original deployment. The PDFs open and match their titles, but several old URLs now return a generic page with status 200 (soft 404; always 140,749 bytes). For anything load-bearing, cite the original author (for example the Common Core Standards Writing Team, or NGA Center and CCSSO) and prefer a state agency or the author's own host where one exists.

## List 1: fully readable now (HTML, no extraction needed)

- Dunlosky, Strengthening the Student Toolbox: https://www.aft.org/ae/fall2013/dunlosky
- How People Learn (2000): https://www.nationalacademies.org/read/9853/chapter/1 (step through chapters)
- How People Learn II (2018): https://www.nationalacademies.org/read/24783/chapter/1
- Adding It Up (2001): https://www.nationalacademies.org/read/9822/chapter/1
- A Framework for K-12 Science Education (2012): https://www.nationalacademies.org/read/13165/chapter/1
- Black and Wiliam, Inside the Black Box: https://kappanonline.org/inside-the-black-box-raising-standards-through-classroom-assessment/
- Leahy et al. (Wiliam), Classroom Assessment: Minute by Minute, Day by Day: https://www.ascd.org/el/articles/classroom-assessment-minute-by-minute-day-by-day
- CAST UDL Guidelines 3.0: https://udlguidelines.cast.org/
- Illustrative Mathematics K-5 Design Principles (CC BY 4.0): https://im.kendallhunt.com/k5/teachers/teacher-guide/design-principles.html
- Illustrative Mathematics 6-8 Design Principles (CC BY 4.0): https://im.kendallhunt.com/MS/teachers/design_principles.html
- PhET research index: https://phet.colorado.edu/en/research
- EdReports math review tools index: https://edreports.org/process/review-tools/math
- NGSS copyright and trademark terms: https://www.nextgenscience.org/ngss-trademarks-and-copyright/ngss-trademarks-and-copyright
- EEF Teaching and Learning Toolkit: readable in a browser or by curl, but WebFetch is refused (403): https://educationendowmentfoundation.org.uk/education-evidence/teaching-learning-toolkit

## List 2: reachable only as binary PDFs (download locally, then extract text)

All confirmed to have a real text layer unless marked.

Shared core
- https://www.aft.org/sites/default/files/Rosenshine.pdf
- http://www.iaoed.org/downloads/EdPractices_21.pdf (http only)
- https://www.deansforimpact.org/files/assets/thescienceoflearning.pdf
- https://ies.ed.gov/ncee/wwc/Docs/PracticeGuide/20072004.pdf
- https://www.aft.org/sites/default/files/dunlosky_0.pdf
- https://www.aft.org/sites/default/files/Clark.pdf
- https://d2tic4wvo1iusb.cloudfront.net/production/eef-guidance-reports/metacognition/metacognition-and-self-regulated-learning_guidance-report.v.2.4.0.pdf
- https://d2tic4wvo1iusb.cloudfront.net/production/eef-guidance-reports/feedback/Teacher_Feedback_to_Improve_Pupil_Learning.pdf (over 10 MB)
- https://wida.wisc.edu/sites/default/files/resource/WIDA-ELD-Standards-Framework-2020.pdf
- https://cdn.prod.website-files.com/681105d2cd8d422bfde21cb3/681105d2cd8d422bfde223ad_elsf-math-guidelines.pdf
- https://cdn.prod.website-files.com/681105d2cd8d422bfde21cb3/681105d2cd8d422bfde223ae_elsf-ela-guidelines.pdf
- https://ies.ed.gov/ncee/wwc/Docs/PracticeGuide/english_learners_pg_040114.pdf
- https://cdn.edreports.org/media/2026/06/MLL-Math%20K-8%20Evidence%20Guide_2.0.pdf
- https://cdn.edreports.org/media/2026/06/MLL-Math%20K-12%20Review%20Criteria_2.0.pdf
- https://cdn.edreports.org/media/2026/06/MLL-ELA%203-5%20Evidence%20Guide_2.0.pdf
- https://cdn.edreports.org/media/2026/06/MLL-Science%206-8%20Evidence%20Guide_2.0.pdf
- https://ugc.futurelearn.com/uploads/files/7d/d6/7dd6188d-c343-4311-b064-ac98d2c95abc/Multimedia_Principles._R._E._Mayer__2020.pdf
- https://phet.colorado.edu/publications/PhET_Interviews_I.pdf
- https://gwern.net/doc/psychology/1984-bloom.pdf (text layer; the MIT copy at https://web.mit.edu/5.95/readings/bloom-two-sigma.pdf is a scan and needs OCR)
- https://www.nber.org/system/files/working_papers/w27476/w27476.pdf

Mathematics
- https://mathematicalmusings.org/wp-content/uploads/2023/05/Progressions.pdf (over 10 MB)
- https://achievethecore.org/content/upload/Math_Publishers_Criteria_K-8_Spring_2013_FINAL.pdf
- https://corestandards.org/wp-content/uploads/2023/09/Math_Standards1.pdf
- https://achievethecore.org/content/upload/SAP%20Focus%20Math%20K%E2%80%938%2011.12.14.pdf
- https://achievethecore.org/content/upload/SAP_Focus_Math_4.pdf (and _K, _1 to _8)
- https://ies.ed.gov/ncee/wwc/Docs/PracticeGuide/fractions_pg_093010.pdf
- https://ies.ed.gov/ncee/wwc/Docs/PracticeGuide/MPS_PG_043012.pdf
- https://ies.ed.gov/ncee/wwc/Docs/PracticeGuide/WWC2021006-Math-PG.pdf
- https://ies.ed.gov/ncee/wwc/Docs/PracticeGuide/early_math_pg_111313.pdf
- https://ies.ed.gov/ncee/wwc/Docs/PracticeGuide/wwc_algebra_040715.pdf
- https://files.eric.ed.gov/fulltext/ED500486.pdf
- https://www.nctm.org/uploadedFiles/Standards_and_Positions/PtAExecutiveSummary.pdf (use curl; WebFetch gets 402)
- https://greatminds.org/hubfs/knowledge/resources/math/EM_Basic_Curriculum_Files/Curriculum_Overview/EM_GPK5_CurriculumOverview.pdf
- https://d2tic4wvo1iusb.cloudfront.net/production/eef-guidance-reports/maths-ks-2-3/EEF-Improving-Mathematics-in-Key-Stages-2-and-3-2022-Update.pdf
- https://cdn.edreports.org/media/2026/06/Math%20K-8%20Evidence%20Guide_2.0.pdf
- https://cdn.edreports.org/media/2026/06/Math%20K-8%20Review%20Criteria_2.0.pdf
- https://stemtc.scimathmn.org/sites/default/files/downloads/5_practices_for_orchestrating_productive_math_discussions.pdf
- https://www.nysed.gov/sites/default/files/programs/standards-instruction/nysed-brief-1-the-research-base-for-mathematics-teaching-and-learning.pdf

Later pages
- NGSS Appendices A, E, F, G and the two ETS1 evidence statement files (URLs in table 3)
- https://www.nextgenscience.org/sites/default/files/EQuIPRubricforSciencev3.pdf
- https://www.oregon.gov/ode/educator-resources/standards/ELA/Documents/ela-appendix-a.pdf
- https://achievethecore.org/content/upload/Appendix-A-New-Research-on-Text-Complexity-revised%20(1).pdf
- https://www.oregon.gov/ode/educator-resources/standards/ELA/Documents/ela-appendix-b.pdf
- https://carnegie.org/wp-content/uploads/2026/01/ccny_report_2007_writing.pdf
- https://carnegie.org/wp-content/uploads/2026/01/ccny_report_2004_reading.pdf
- https://ies.ed.gov/ncee/wwc/Docs/PracticeGuide/wwc_foundationalreading_040717.pdf
- https://ies.ed.gov/ncee/wwc/Docs/PracticeGuide/WWC_Elem_Writing_PG_Dec182018.pdf
- https://ies.ed.gov/ncee/wwc/Docs/PracticeGuide/wwc_secondary_writing_110116.pdf
- https://ies.ed.gov/ncee/wwc/Docs/PracticeGuide/readingcomp_pg_092810.pdf
- https://ies.ed.gov/ncee/wwc/Docs/PracticeGuide/WWC-practice-guide-reading-intervention-full-text.pdf
- https://achievethecore.org/content/upload/Why_Text_Complexity_Matters.pdf
- https://achievethecore.org/content/upload/Research%20Supporting%20Shift%203%20-%20Building%20Knowledge%5B1%5D.pdf
- https://achievethecore.org/content/upload/Research%20Supporting%20the%20ELA%20Standards%20and%20Shifts%20Final.pdf
- https://ies.ed.gov/ncee/wwc/Docs/PracticeGuide/adlit_pg_082608.pdf (added 2026-11-12)
- https://www.nichd.nih.gov/sites/default/files/publications/pubs/nrp/Documents/report.pdf (added 2026-11-12)
- https://files.eric.ed.gov/fulltext/ED594994.pdf (added 2026-11-12)

## List 3: paywalled, blocked or not found, with the best free substitute

| Source | Problem | Best free substitute (confirmed reachable) |
|---|---|---|
| Kirschner, Sweller, Clark (2006) | Publisher blocks automated access; only an unofficial course copy is free | Clark, Kirschner, Sweller, American Educator 2012: https://www.aft.org/sites/default/files/Clark.pdf |
| Hmelo-Silver, Duncan, Chinn (2007) | Paywalled; no legitimate free copy verified | Cite from the abstract, and carry the balance with How People Learn II (motivation, context) and the IM Design Principles (problem-based with scaffolding). Or have a person fetch it through a library. |
| Sinha and Kapur (2021), productive failure | Sage returns 403 to automated clients; open access status not confirmed | Open the DOI in a browser: https://doi.org/10.3102/00346543211019105 . If it is not free, use How People Learn II. |
| Dunlosky et al. (2013) monograph | Sage returns 403 to automated clients | Dunlosky, American Educator 2013 (HTML, full) |
| Rosenshine IBE booklet at UNESCO IBE | IBE URLs 404, unesdoc needs JavaScript | The same booklet on the IAE host: http://www.iaoed.org/downloads/EdPractices_21.pdf |
| Wiliam book chapters (UCL repository copy) | 403 | Leahy et al. 2005 (ASCD, HTML full) and Black and Wiliam 1998 (HTML full) |
| Mayer, authoritative summary of multimedia principles | Review articles and book paywalled; only a third-party one-page list is free | Pashler et al. 2007 (public domain) covers combining graphics with verbal description; use the one-page list only as a checklist of principle names |
| Moyer-Packenham and Westenskow, virtual manipulatives | Repository holds the record only | PhET research papers (free), plus the EEF maths guidance report on manipulatives and representations |
| Concrete-representational-abstract synthesis | No free synthesis found | WWC 2021 intervention guide (public domain) and EEF maths guidance report |
| NCTM Principles to Actions (full book) | Paid | NCTM executive summary PDF (free, six pages, has the eight practices) |
| Smith and Stein, 5 Practices (book) | Paid | IM K-5 Design Principles section on the 5 Practices (CC BY 4.0), plus the one-page list |
| EngageNY original "A Story of Units" overview (2013, Creative Commons) | engageny.org retired; NYSED files moved to SharePoint (untested); Wayback refused | Great Minds 2015 edition of the same overview (direct PDF, all rights reserved, read only) |
| Standards for Mathematical Practice as an HTML page; CCSS public licence page | Old pages 404 or 511 | The practices are in the CCSSM PDF: https://corestandards.org/wp-content/uploads/2023/09/Math_Standards1.pdf . Licence terms not confirmed. |
| SAP Coherence Map | JavaScript application; no text for tools | Use in a browser; for prose on coherence use the Progressions (CC BY) |
| SAP rigor document | Only a one-page graphic | K-8 Publishers' Criteria |
| National Math Panel report on ed.gov | 404 | ERIC copy: https://files.eric.ed.gov/fulltext/ED500486.pdf |
| CCSS ELA Appendix A, B and supplement on corestandards.org | 404 | Oregon Department of Education copies (A and B) and the Achieve the Core copy (supplement), all listed above |
| Bloom (1984) at the publisher | Restricted | gwern.net copy with text layer; pair with Nickow et al. 2020 (NBER, free) |

## Sources an expert would likely ask for that were not on the list

Tested and included above: Clark, Kirschner, Sweller (2012); Leahy et al. (2005); Nickow, Oreopoulos, Quan (2020); the CCSSM document itself; NYSED mathematics research briefs; ELSF ELA guidelines; two further WWC reading guides.

Not tested in this pass (flag only, test before relying on them): Hattie and Timperley, The Power of Feedback (2007); a cognitive load theory summary such as the NSW CESE paper; Clements and Sarama on learning trajectories; Fyfe et al. (2014) on concreteness fading; the EdReports v2.0 FAQ; the adoption rubric of whichever state Curio Class targets first.

## Evidence notes (added 2026-11-11 with the second draft of the approach)

The study detail that docs/APPROACH.md and docs/APPROACH-MATH.md leave out to stay short. In our own words. Page
checks are in docs/reviews/approach-2026-11-11.md.

- **Sinha and Kapur 2021.** A meta-analysis of 53 studies, 166 comparisons of problem solving then instruction
  against instruction then problem solving. Understanding and transfer: Hedges' g about 0.36 in favour of problem
  first. Procedures: no difference (about -0.03). Grades 2 to 5 (25 of the 166 comparisons): about -0.09, in favour
  of instruction first, and different from the other grades. Grades 6 to 10: about 0.50. General skills such as
  controlling variables: about -0.17. The effect was larger when the teaching built on students' own attempts (0.56
  against 0.20). The abstract's larger bias-adjusted figure (0.87) is not used. Most studies were math and science.
  Read in part in a browser; the discussion section was not read.
- **Hmelo-Silver, Duncan and Chinn 2007.** Abstract only: argues that problem-based and inquiry teaching are heavily
  supported, not unguided. No number or study may be attributed to it.
- **Pashler et al. 2007.** Levels: spacing moderate (1); worked examples with problems moderate (2), stated for
  math and science problem solving; graphics with words moderate (3); concrete and abstract connected moderate (4),
  with the warning that concrete-only learning may not transfer, and a mention of fading the concrete; pre-questions
  low (5a); quizzing strong (5b); deep explanatory questions strong (7). This guide's lowest level is called Low.
- **National Mathematics Advisory Panel 2008.** Finding 11: automatic recall needs enough practice. Finding 23:
  neither all student-centered nor all teacher-directed teaching is supported. Finding 25: regular formative
  assessment helps in the elementary grades. Finding 26: real-world problem teaching helped on similar problems
  only, from a small number of studies. Finding 27: explicit teaching has consistently positive effects for
  students with math difficulties. Finding 28: practice and tutorial software has generally shown positive effects;
  a large national study found none under typical conditions. (11, 25 and 27 were checked by the expert review.)
- **Nickow, Oreopoulos and Quan 2020.** 96 randomized trials of one-to-one or small-group tutoring; pooled effect
  0.37 standard deviations; 11 of the 96 were parent tutoring, with smaller effects. A working paper.
- **Bloom 1984.** The "two sigma" claim rests on two doctoral studies of about three weeks. Not repeated as a rule.
  The copy read is on an unofficial host.
- **Adams et al. 2008.** Interviews with college undergraduates using simulations, not a controlled trial.
- **Black and Wiliam 1998.** Used without an effect size on purpose; later re-analyses found smaller effects (the
  expert names Kingston and Nash 2011, from memory, not read).
- **WWC 2021, recommendation 6.** Timed activities of one to five minutes, as one part of taught small-group
  intervention, on material already taught, with feedback. Not a whole-class finding.
- **EEF maths report 2022.** Written for ages 7 to 14.

Cory, 2026-11-11: go forward without library access. The paywalled items below stay unread unless a free copy
turns up, and no page may rest on them.

**Not yet read, in order of value** (the first is the claim closest to what Curio Class builds):

1. A review of on-screen (virtual) manipulatives, such as Moyer-Packenham and Westenskow 2013.
2. Carbonneau, Marley and Selig 2013 (manipulatives meta-analysis) and Fyfe, McNeil, Son and Goldstone 2014
   (concreteness fading): the direct evidence for concrete, then pictures, then symbols.
3. Hattie and Timperley 2007 on feedback (the task and the next step, not the child).
4. The discussion section of Sinha and Kapur 2021; the full text of Hmelo-Silver et al. 2007 and Kirschner et al.
   2006 (library access).
5. Anything on parents teaching their own child a full course.
6. Learning trajectories (Clements and Sarama), when a K to 2 math course opens.

## Lesson-level sources found by the unit plan review (added 2026-11-11)

- EngageNY grade 4, full modules as PDFs with a text layer, CC BY-NC-SA 3.0 (stated in the files). Read only; the
  non-commercial, share-alike licence means nothing is copied. Module 1:
  https://unbounded-uploads.s3.amazonaws.com/attachments/2497/math-g4-m1-full-module.pdf ; module 3:
  https://unbounded-uploads.s3.amazonaws.com/attachments/2086/math-g4-m3-full-module.pdf ; module 5:
  https://unbounded-uploads.s3.amazonaws.com/attachments/2563/math-g4-m5-full-module.pdf . Lesson pages at
  lessons.unbounded.org link to the other modules. This is the live Creative Commons copy that List 3 says was
  not found.
- Illustrative Mathematics K-5 lesson pages open without sign-in:
  https://im.kendallhunt.com/k5/teachers/grade-4/unit-N/lesson-N/preparation.html and .../lesson.html ; scope and
  sequence at https://im.kendallhunt.com/k5/teachers/grade-4/course-guide/scope-and-sequence.html . Cool-downs and
  unit assessments need a free sign-in and have not been read.
- Fishtank Learning grade 4 unit pages are open (https://www.fishtanklearning.org/curriculum/math/4th-grade/);
  lesson pages show only the objective without a sign-in. Its terms give CC BY-NC-SA 4.0 for the free curriculum.
- Federal fractions practice guide (Siegler and others, 2010, public domain):
  https://ies.ed.gov/ncee/wwc/Docs/PracticeGuide/fractions_pg_093010.pdf . Roadblock 2.2 (PDF page 31) is the source
  for "numbers in a fraction read as separate whole numbers".

## ELA evidence notes and access notes (added 2026-11-12)

From the curriculum expert's cold reads of 2026-11-11: docs/reviews/approach-ela-2026-11-11.md,
docs/reviews/rights-ela-6-s2-2026-11-11.md and docs/reviews/rubric-ela-2026-11-11.md. In our own words. Each note
keeps the report's own statement of how much was read. Nothing here was re-opened when these notes were filed.

Evidence notes:

- **Kamil and others 2008 (Improving Adolescent Literacy).** Read in part: the checklist, the level-of-evidence
  paragraph of all five recommendations and step 4 of recommendation 2, of 65 pages. Recommendation 1, teaching
  words directly in regular lessons with repeated meetings in several settings: strong, for upper elementary,
  middle and high school; the effects are on word learning, and only some studies show a gain in comprehension.
  Recommendation 2, direct and explicit teaching of comprehension strategies, with the teacher thinking aloud
  and then guided practice: strong, on five randomized studies. Recommendation 3, extended discussion of what a
  text means: moderate, on four small studies and one large correlational one. Recommendation 5, intensive help
  from specialists for students who struggle: strong. Limits: it is the oldest guide of the set, its panel chose
  the studies and did not run a full search, and its lowest level is called "low", not "minimal".
- **National Reading Panel 2000.** Read in part: two pages of the fluency chapter (PDF 192 and 216) and the
  paragraph on its search, of 449 pages. It found only 14 studies that tried to raise the amount of independent
  silent reading, mostly with no gain. It concluded the evidence is not adequate to say that encouraging students
  to read more raises achievement, and that this does not show such programs cannot work. It notes that many
  correlational studies find the best readers read the most. It found clear evidence for guided repeated oral
  reading. It uses no strong, moderate or minimal scale. No later review was read.
- **Hasbrouck and Tindal 2017.** Read in part: the grade 5 and 6 table. In the fall of grade 6 the middle student
  reads about 132 words correct a minute and the 25th percentile about 112. The flag at 112 in the ELA pages is
  ours and untested.
- **Writing Next (Graham and Perin 2007).** Read in part: the sentence-combining section (PDF 26) and "A Note
  About Grammar Instruction" (PDF 29), of 77 pages. A meta-analysis of studies in grades 4 to 12, with the quality
  of writing as the outcome. Teaching parts of speech and sentence structure as a subject of its own had a small
  negative effect. Sentence combining had a moderate positive effect (0.50), mostly measured against that kind of
  grammar teaching. One study found grammar taught for use inside writing had a strong positive effect. Limits:
  the outcome is writing quality, not a test of conventions; it is a summary, and the studies were not read.
- **WWC 2022 (reading interventions, grades 4 to 9), recommendation 3, Part A.** Three to five minutes of
  background on the topic and three to five on its words before one passage, inside small-group help (PDF 28 to
  29). It is evidence for a short step before reading, not for a set of texts on one topic.
- **WWC elementary writing guide (2012, revised 2018).** Its studies run from kindergarten to grade 6 (PDF 14), so
  it covers grade 6.
- **WWC foundational skills guide (2016), recommendation 2.** Its studies were kindergarten and grade 1 (PDF 21).
  It says nothing to grades 3 to 5.
- **Supplement to Appendix A (2012), PDF page 8.** A person's judgment of a text may outweigh the computed
  measure, most of all for narrative fiction in the later grades. The same page says poetry, drama and
  kindergarten to grade 1 texts cannot be placed by a computed measure. The band table is on PDF page 4.

Access notes:

- **Publishers' Criteria, grades 3 to 12.** In the extracted text, words are split by odd spacing. Collapse runs
  of spaces before searching.
- **EdReports ELA criteria and evidence guides.** The four ELA files (grades 3 to 5 v2.1 and grades 6 to 12 v2.0,
  both updated 07/2025) now sit on a media host with hashed file names, not on the cdn.edreports.org addresses
  this page lists for the math and multilingual learner files. Plain curl works with no special header. The
  stable way in is the tools page: https://edreports.org/process/review-tools/ela . The four addresses, and how
  much of each was read, are in docs/RUBRIC-ELA.md. The tools page also links four multilingual learner files for
  ELA; their addresses are in docs/reviews/rubric-ela-2026-11-11.md. Those four were found, not opened.
- **Archive.org search.** The search endpoint (advancedsearch.php with output=json) answers without a block and
  gives publisher and year for old editions. Used to date Baldwin's Old Greek Stories (1895). The scan's title
  page was not opened.
- **LibriVox book pages.** Each lists every section with its reader and time in plain HTML tables. curl with a
  browser user agent works. Nobody listened to a recording.
- **Core Knowledge, Ancient Greece and Rome (grade 6 history reader).** The back cover (PDF page 154) prints
  "960L", a level stated by the publisher.
