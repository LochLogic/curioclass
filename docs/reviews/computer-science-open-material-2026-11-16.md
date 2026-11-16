# Open computer science material for Curio Class: is there a base text we may adapt?

Read 2026-11-16 (subject pre-work, the computer science counterpart of P2). Research notes, not legal advice. Each
licence was read on the publisher's own page that day unless marked "search only" (seen in a search summary, page
not opened) or "from memory". Nothing else in the repo was changed by this read. The bar is
docs/sources/BASE-TEXTS.md: CC BY 4.0, public domain or the UK Open Government Licence v3.0 is a base; NC, SA, ND or
unclear is reference only.

## The short answer

- **One strong partial base:** the Teach Computing Curriculum, made by the Raspberry Pi Foundation for England's
  National Centre for Computing Education, under the Open Government Licence v3.0 "unless expressly stated
  otherwise" (teachcomputing.org terms page). It runs from age 5 to 16: 14 units and 86 lessons in key stage 1,
  28 and 146 in key stage 2, 20 and 124 in key stage 3, 22 and 179 in key stage 4, each with lesson plans, slides,
  activity sheets, homework and assessments. England's year n is about US grade n minus 1, so it spans about
  kindergarten to grade 10.
- **Every US program is reference only:** Code.org (CC BY-NC-SA 4.0), Beauty and Joy of Computing and Mobile CSP
  (CC BY-NC-SA, search only), Bootstrap (a Creative Commons 4.0 licence with a written bar on running training,
  unclear, search only), Exploring Computer Science (copyright, no redistribution, search only).
- **No whole-course base for the Computing and Society, AI and data standards as CSTA 2026 writes them.** The English
  curriculum predates the 2026 standards, has no AI unit in key stage 3, and spends many units on creating media.
- **Verdict:** partial base for grades K to 8 from the Teach Computing Curriculum, unit by unit, after a check of
  each item for third-party material; the high school course and the SOC and AI strands are our own, with key stage
  4 as a partial base where a unit fits. Adopting it is Cory's call (APPROACH.md, "Questions in this draft").

## Candidates

| Candidate | Licence (as read) | Grades it could serve | Fit | Verdict |
|---|---|---|---|---|
| **Teach Computing Curriculum** (Raspberry Pi Foundation for the NCCE, funded by England's Department for Education) | "published under the Open Government License v 3.0 unless expressly stated otherwise" (terms page, opened); the key stage 1 teacher guide states OGL v3 (search only). Third-party works inside it are used under a UK teaching exemption, "non-commercial basis only": those items are excluded | K to 8 (key stages 1 to 3); grades 9 and 10 (key stage 4) | Strands per year: computing systems and networks, creating media, programming A and B, data and information (key stage 2, opened). Key stage 3 (opened): networks, Scratch then Python programming, spreadsheets, web, representation, data science, cybersecurity, physical computing. Gaps against CSTA 2026: AI and machine learning, much of SOC (bias, design values, law), US data and privacy context. Depends on named tools (Scratch, a microcontroller board, office and media apps), which our browser tools replace | **Partial base**, K to 8 first. Per-unit check for third-party images, text and tool screenshots |
| Oak National Academy computing | Oak releases its resources under the OGL (Computing at School write-up, search only); co-developed with the Raspberry Pi Foundation; key stage 3 and GCSE pathways; some year 9 lessons marked for removal by spring 2026 (search only) | 6 to 10 | Overlaps the Teach Computing Curriculum | Partial base, taken per unit, like Oak in social studies; check currency first |
| CS Unplugged (University of Canterbury) | "this website's content is shared under a Creative Commons Attribution-ShareAlike 4.0 International license" (site footer, opened) | K to 8 unplugged days | Excellent unplugged activities (binary, sorting networks, error detection) | Reference (ShareAlike). Ideas only; our unplugged tasks are our own |
| Computer Science Field Guide (same group) | CC BY-NC-SA (from memory) | 9 to 12 | Topic background | Reference |
| Code.org (CS Fundamentals, Discoveries, Principles) | CC BY-NC-SA 4.0 (its curriculum guides and commitment page, search only) | K to 12 | The most used US program | Reference |
| Beauty and Joy of Computing (UC Berkeley) | CC BY-NC-SA 4.0 (search only) | 9 to 12 | AP level | Reference |
| Mobile CSP (Trinity College) | CC BY-NC-SA 4.0 "unless otherwise noted" (Runestone site, search only) | 9 to 12 | App building | Reference |
| Bootstrap | "Creative Commons 4.0 Unported" with no NC or SA named, plus a written bar on running training with its materials (search only) | 6 to 12 | Algebra through programming | Unclear, so reference |
| Exploring Computer Science | Teacher copy for "individual classroom use", no redistribution without permission (v9 and v10 PDFs, search only) | 9 to 10 | | Reference |
| OpenStax Introduction to Computer Science (2024) | Preface (opened 2026-11-16): CC BY-NC-SA 4.0, with the AI clause. A 2024 listing called it CC BY 4.0 (search only), so an earlier printing may differ; not pursued | College | College level, poor fit | Reference |

## Traps

- "Unless expressly stated otherwise": each Teach Computing item is checked for its own licence line and for
  third-party images and text before any adaptation; those parts are dropped or replaced.
- England's terms and settings (key stage, year 7, GCSE, pounds) and named products are removed in adaptation; no
  product name reaches a student, teacher or family page. Names of the source appear only in the credit line.
- The English curriculum is written to England's national curriculum, not CSTA 2026. Every adapted unit is mapped to
  CSTA ids at the depth of the boundary statement; a lesson with no CSTA id is cut or kept only inside the 10 percent
  allowance of bar criterion C1.

## What was not done

No files were downloaded into S:\CurioClass-sources. Unit counts per lesson and the key stage 1 and key stage 4 unit
lists were not opened. If Cory says yes, the store folder is made the way the social studies partial bases were.
