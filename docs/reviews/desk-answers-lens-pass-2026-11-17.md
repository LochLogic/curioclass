# Desk answers applied: lens pass calls (q-lens-pass-1), 2026-11-17

Cory answered six calls on the Desk card q-lens-pass-1. Each is applied below. Gates: `unitplan.py check` passes for
us-history-i, social-studies-grade-3, science-grade-1 and english-language-arts-grade-11 (every unit PASS);
`plan.py check` gives 0 failures for each of the four courses. Decision log line added to
docs/agents/decisions/DESK-ANSWERS.md.

## 1. US History I unit 8: students choose the organization

Changed: field 2 Limits now says the teacher models organization research on the 1869 National Woman Suffrage
Association (the worked example) and each student researches one organization chosen from the listed topics: the
American Woman Suffrage Association, the Woman's Christian Temperance Union or the National Association of Colored
Women (survey pages carry the ones not chosen). Field 5 item 4 asks for "the organization you chose" and its answer
names tactics generically; the "set by the teacher" sentence in the scoring paragraph is replaced; the item 4 meets
sample now uses the American Woman Suffrage Association; exit E130 uses a statement from the chosen organization.
days.csv day 130 note says students choose after the teacher's worked example; the plan's day list note matches.

Item-level choice (mine): the National Association of Colored Women was added as a third choice so students have more
than two options; the standard's own list of topics is not in data/standards (it reads only "choosing one of the
listed topics"). The printed collection now needs a short source set for each listed organization.

Files: docs/courses/us-history-i/s08.md; data/plans/us-history-i/days.csv. Sources opened: none needed.
Left: item 2 still names "the class topic, the 1906 law" for the T7.2 policy research; that is the policy study, not
this call, and is unchanged.

## 2. Social studies grade 3 unit 2: Menominee kept on day 43

The plan already limited the Menominee Indian Tribe of Wisconsin to the constitution comparison, with homeland,
treaty and oral history in unit 4. Added "kept on day 43" to that line. The field 6 background line now says the news
search of the last 24 months is to be run before this unit's days are written (not yet run). The search was not run.

Files: docs/courses/social-studies-grade-3/s02.md. Sources opened: none.

## 3. Science grade 1 unit 1: daytime stars, weighted lightly

Kept the step and error D. Scoring now: for item T the description point rests on the core pattern alone (stars seen
on clear dark nights, not in the day). The idea that stars are still present by day, hidden by the bright sky, is
noted on the sheet and a disappearance claim (D) gets day 8 feedback, but it never costs a point the core pattern
earned. The item T row and the does-not sample were changed to match. Item-level choice (mine): "lightly" is done as
a noted, unscored element rather than a fractional point, since the record sheet uses 0 and 1 cells.

Source: the NASA page already in field 10, "Why Can You See the Moon During the Day? We Asked a NASA Scientist:
Episode 19" (https://www.nasa.gov/solar-system/why-can-you-see-the-moon-during-the-day-we-asked-a-nasa-scientist-episode-19/),
reread today: the transcript says the stars are still up there during the day but the sky is too bright to see them.
Field 10 now names this; error D's source cell points to it.

Files: docs/courses/science-grade-1/s01.md.

## 4. ELA grade 11 unit 6: Occom

No 18th-century printing of the Narrative exists to confirm: written 1768, it was first printed in 1982 (the
existing ela-texts.csv note). So the swap went to another Occom text that could be confirmed: A Sermon at the
Execution of Moses Paul. Edition used: archive.org, sermonatexecutio01occo (John Carter Brown Library copy); title
page: New Haven, printed 1788; London, reprinted 1788. Bounds read on the page images today:

- page 13: "This must be the unavoidable portion" through "the wages of sin is death" (the sentence putting
  "Negroes, Indians, English" under one judgment);
- pages 16 to 17: "My poor unhappy brother MOSES" through "at the hands of a holy God" (includes "You are an Indian,
  a despised creature" and "Whatever partiality, injustice and error there may be among the judges of the earth").

Fit: day 109 (~RL.11-12.9, eighteenth-century treatments of faith and unequal treatment) pairs it with Wheatley's
On Being Brought from Africa to America: both claim spiritual equality across nations; Wheatley rebukes the
scornful, Occom names contempt and turns his listener to self-examination. The day 109 exit, the comparison
paragraph, the day 115 meets sample, field 8 and field 10 were rewritten; the Narrative fallback lines are gone.
The address to Native listeners on drunkenness (pages 21 to 23) is not printed. A 1772 first printing is marked
"from memory" (the catalogue record could not be opened: the Evans/TCP page refused, the Oxford host was down).

Files: docs/courses/english-language-arts-grade-11/s06.md; data/plans/english-language-arts-grade-11/days.csv (day
109 note); data/plans/ela-texts.csv (new row g11-u6-03; note on g11-u3-11); scope-and-sequence.md (record row
g11-u6-03, g11-u3-11 no longer says "compare 109", unit 6 summary line).

Left for the lead: unit 3 day 43 (s03.md and days.csv) still reads the 1768 Narrative whole, with its rights
unresolved. Day 109 now reads the sermon fresh rather than rereading, so unit 3 is not required for it, but the same
rights question stands there.

## 5. ELA grade 11 unit 1: day 14 cold story

Chopin's The Story of an Hour stays on day 139 (unit 9, unchanged). Day 14's cold story is now Poe's The Oval
Portrait, 1845 Broadway Journal text (Text-03b), read on the Edgar Allan Poe Society transcription
(https://www.eapoe.org/works/tales/ovlprtb.htm), about 1,250 words, so it still fits eight reading minutes. It suits
day 14's purpose (literary uncertainty, where to end, older diction): a frame narrator in "incipient delirium" reads an
unnamed writer's account that ends abruptly on the wife's death, with two readings (life drawn into the portrait, or
weeks of confinement and neglect) and nothing proved. Items A1 to A8 and day 15's B1 were rewritten on it with quotes
checked against the transcription: vignette (context), perceive / perception / imperceptibly (word forms), ardor
(1828 entry), pined (verify), the first sentence (syntax). The 1828 ardor entry was read at
https://webstersdictionary1828.com/Dictionary/ardor (stress on the first syllable, noun, sense 2 "warmth ... eagerness"),
and field 10's dictionary link now points there.

Item-level choice (mine): Poe is also the day 9 to 12 author (Usher). The story is still unseen, and its nested text
and unstable narrator test the unit's own skills; a different author was weighed (Bierce's The Boarded Window,
Irving's The Adventure of the German Student) but both run near 2,000 words, too long for eight minutes.

days.csv day 14 does not name Chopin, so it is unchanged. Files: s01.md; ela-texts.csv (new row g11-u1-05);
scope-and-sequence.md (record row g11-u1-05).

## 6. ELA grade 11 unit 5: Jacobs chapter I kept

Chose to keep chapter I. Reason: no clearly better period text. Chapter I (opened today on Wikisource; imprint
Boston: published for the author, 1861, edited by L. Maria Child) has no sexual violence and no slur, adds a woman's
voice beside Douglass and Truth, is unseen, and fits day 93's ~RI.11-12.3 task (affection and a promise of freedom
undone by a will). It also ends on her mistress teaching her to read and spell, which ties straight to the unit
question about learning to read. A Douglass alternative (My Bondage and My Freedom) would retell events students have
just read, so it is not cold. Truth is already day 92. Other narratives (Brown, Bibb, Northup) offer no advantage
and none was checked.

Scope and sequence unit 5 now keeps the candidate in its smallest form (chapter I only, days 93 and 95, 0 added
days) and still drops the further chapters. Text record row g11-u5-04 added there and in ela-texts.csv.

Frame slur note corrected: checked on the Wikisource chapters today, the slur is in Narrative chapters 4 (one use), 6
(four, Hugh Auld's speech), 9 (one) and 10 (four); none in chapter 11, the Appendix, the preface or the letter. The
frame line (and its copy in s05.md field 10's frame block) now says every occurrence is omitted with a mark and
an editor's note, the packet is searched for the word before printing, and it is never spoken.

Files: docs/courses/english-language-arts-grade-11/frame.md, s05.md, scope-and-sequence.md; data/plans/ela-texts.csv.
days.csv needed no change (day 93 says only "unseen short nineteenth-century memoir passage").

## Not done

- The 24-month news check for social studies grade 3 unit 2 (by instruction).
- Unit 3 of ELA grade 11 still uses the 1768 Occom Narrative on day 43 (rights unresolved; see item 4).
- The Desk card itself was not edited.
