# The Map: research on teaching order (Phase F, Q5)

Researched 2026-10-27 for `data/sequence.csv`. Q5 asked us to look at published progressions and pacing guides, and
their licenses, before drafting a teaching order. This is what we found and what we recommend.

## The short answer

- **A teaching order is our own arrangement of our own modules.** We copy no text, unit names or lesson content from
  anyone. Published sequences are references that tell us what usually comes first. Even so, we lean only on sources
  whose license would allow reuse, cite them on the Map's about page, and use NonCommercial sources only to cross-check.
- **Math has the best open evidence.** Two sources are CC BY 4.0. Draft math first.
- **Science grades 6 to 8 have a published model** (NGSS Appendix K). K-5 and high school are a judgment call.
- **ELA, social studies and the electives have no open year-long order worth following closely.** Draft those from the
  frameworks and a few simple rules (below), then have Cory spot-check.
- **`builds_on` can mostly be computed** from the standards codes already in `modules.csv`. Hand-edit only the rest.

## Sources by subject

Licenses were checked on 2026-10-27. Rows marked *unconfirmed* had conflicting or missing statements. Treat those as
cross-check only until someone reads the publisher's own license page.

| Subject | Source | What it gives us | License | How we use it |
|---|---|---|---|---|
| Math | Progressions for the CCSS in Mathematics (Common Core Standards Writing Team, Univ. of Arizona IME, May 2023 edition) | How each domain grows across grades (fractions 3 to 5, ratios 6 to 7, and so on) | CC BY 4.0 (stated on the 2023 edition; older drafts carry a plain copyright) | Primary basis for `builds_on` and for order within a grade |
| Math | Illustrative Mathematics K-12, first edition | A tested unit order for each grade | CC BY 4.0 (first edition only; the newer v.360 is CC BY-NC 4.0) | Primary cross-check for order within a grade. Cite the first edition only |
| Math | Eureka Math / EngageNY | A second unit order per grade | Said to be CC BY-NC-SA (*unconfirmed*, only seen on a mirror) | Cross-check only |
| Math | Achieve the Core Coherence Map | Standard-to-standard links K-8 | Free to use; terms page not read (*unconfirmed*); includes some third-party content | Cross-check for `builds_on` only. Do not copy its link data |
| Science | NGSS Appendix K, Model Course Mapping | Course Map Model 1: Conceptual Progressions for grades 6 to 8 (which performance expectations go in which year), plus three high school models | NGSS copyright is held by the National Academies Press; schools and non-profit education groups may copy and adapt. The NGSS name is a WestEd trademark | Basis for which middle school modules come early or late. Say "based on NGSS", never call our map "the NGSS" |
| Science | OpenSciEd unit sequence (6-8, high school) | A tested order of units | *Conflicting*: New Jersey's framework says CC BY 4.0; OpenSciEd's own license description (v2.0) says CC BY-NC 4.0 for classroom materials | Cross-check only, until its license page is read |
| ELA | EL Education K-8 | Four topic modules a year, each pairing reading and writing | Not confirmed in this search (*unconfirmed*) | Pattern only: pair a reading module with the writing module that uses it |
| ELA, social studies K-5 | Core Knowledge Sequence | Topic order by grade | CC BY-NC-SA (4.0 for the 2023 editions, 3.0 for older ones). No resale, and a "does not endorse" line is required | Cross-check only |
| Social studies | C3 Framework (NCSS) | The Inquiry Arc. It deliberately gives no content order | Copyrighted by NCSS | Not a sequence source |
| Computer science | CSTA K-12 CS Standards (2017) | Standards by band, no year order | CC BY-NC-SA 4.0. Claiming "aligned to CSTA" requires approval from CSTA's review team | Order within a band only. **Flag:** the site should not say "CSTA-aligned" anywhere without that review |
| All | State pacing guides (Utah UEN and others) | District-style calendars | Varies by state and is often unstated. Utah's 2026 SB 119 would require open licenses, but it has not passed | Do not use as a basis, too varied and unclear |

Two Common Core cautions for the Map page itself. The CCSS license forbids edited or condensed versions of the
standards, so the Map shows codes and our own module titles, never paraphrased standard text. And nothing on the Map
should suggest an endorsement by NGA/CCSSO, NGSS/WestEd, IM or CSTA.

## How to draft `sequence.csv`

Columns, as planned, plus one more: `subject, grade, module_id, order, builds_on, basis`. `basis` records why a stop
sits where it does: `progressions`, `im-order`, `ngss-k`, `chronology`, `horizons`, `pair`, `framework` or `judgment`.
It lets Cory see which orders came from evidence and which are our call.

Rules by subject:

1. **Math.** Follow the IM first-edition unit order for the grade, placing each module where its standards land.
   `builds_on` is the same domain one grade back (3.NF leads to 4.NF), checked against the Progressions. High school
   follows the course order in `courses.csv`.
2. **Science.** Grades 6 to 8: modules whose performance expectations Appendix K puts early come first. K-5 and high
   school: order by dependency (matter before chemical change, cells before body systems), basis `judgment`.
3. **ELA.** Within a grade: foundational skills early, then reading modules, each followed by the writing or speaking
   module that uses it (basis `pair`). Language and vocabulary modules spread through the year, not bunched.
4. **Social studies.** K-3 expanding horizons: self, family, school, community, state (basis `horizons`). History
   grades: chronological (basis `chronology`). Economics, civics and inquiry-skill modules go next to the era or
   topic they serve.
5. **Electives** (arts, CS, health and PE, SEL, library, ELD, world languages, CTE): framework strand order, with
   "making" modules after the "learning about" modules they draw on. Basis `framework`.

## What this changes in the plan

- The Grade 3 pilot stays: math first (strongest evidence), then science, ELA and social studies.
- Draft math for all grades right after the pilot, since its basis is the most solid.
- A small checker (`scripts/check_sequence.py`) should confirm every module appears exactly once, `order` has no
  gaps within a region, every `builds_on` id exists and points to the same or an earlier grade, and `basis` is from
  the list.
- The `/map/` about section names the CC BY sources with attribution and links to their licenses.

## Still open

- Read OpenSciEd's and EL Education's own license pages before they move beyond cross-check.
- Read Achieve the Core's Terms of Use before using its Coherence Map for anything more than a sanity check.
- Confirm with Cory that Curio Class stays non-commercial. If it ever charges, NonCommercial sources must stay
  cross-check only (they already are under this plan).

## Sources

- Progressions documents: https://archive.math.arizona.edu/ime/progressions/ (2023 edition with the CC BY 4.0 notice:
  https://webnew.ped.state.nm.us/wp-content/uploads/2025/04/Progressions-for-the-Common-Core-State-Standards-Math_05.23-version.pdf)
- Illustrative Mathematics terms of use: https://www.illustrativemathematics.org/terms-of-use
- NGSS Appendix K: https://static.nsta.org/ngss/AppendixK-FINAL-6.5.13.pdf and https://www.nextgenscience.org/resources/ngss-appendices
- NGSS trademarks and copyright: https://www.nextgenscience.org/ngss-trademarks-and-copyright/ngss-trademarks-and-copyright
- CCSS commercial license: https://thecorestandards.org/commercial-license/
- OpenSciEd license (conflicting): https://www.nj.gov/education/standards/science/Sci6-8.shtml and
  https://issuu.com/openscied/docs/openscied_license_for_commercial_use_nc_
- CSTA standards: https://csteachers.org/k12standards/standards/
- Core Knowledge Sequence (2023): https://www.coreknowledge.org/wp-content/uploads/2023/03/CK_Sequence-2023_Preschool_W2.pdf
- Utah SB 119 (2026, introduced): https://le.utah.gov/Session/2026/bills/introduced/SB0119S03.pdf
