# Sensitivity read: US History I, section 5.2 (days 78 to 82), 2026-11-15

Reader: a fresh sensitivity agent that did not see the work written. Community: Black Americans, for slavery,
emancipation, Black military service and the memory of the war. Brief: docs/pipeline/briefs/sensitivity-read.md.

## What I read

- AGENTS.md; the brief.
- docs/courses/us-history-i/s05.md (unit plan: frame, error register, assessment, sensitive topics, sensitivity study,
  days table) and docs/courses/us-history-i/u05-2.md (section plan, all fields).
- courses/us-history-i/u05-2/: opener.md, family.md, d078.md to d082.md, sources-78.md, sources-79.md,
  sources-80.md, sources-82.md.
- data/plans/us-history-i/sources.csv (rows 78A to 82F, 89-W1, 89-W2, P2-DUB) and items.csv (every s05 item for
  days 78 to 82, and s05-EM).

## What I studied

1. Association for the Study of African American Life and History, https://asalh.org/ (and its Journal of African
   American History reviews). The community's own scholarly body, founded by Carter G. Woodson. Taught me where
   current Black scholarship on the war sits: Edda L. Fields-Black's *Combee* (2024) on the Combahee raid and Hillary
   N. Green's *Unforgettable Sacrifice* on how Black communities remembered the war.
2. National Park Service, "We Called Ourselves Combee", https://www.nps.gov/articles/000/we-called-ourselves-combee.htm.
   The people of the Combahee called themselves "Combee" (Gullah); Tubman worked as nurse, scout and spy, built an
   informant network and recruited; about 300 men of the 2nd South Carolina Volunteers (later the 34th USCT) went up
   the river; more than 750 people were freed and more than 150 then enlisted. Taught me to show the raid as Black
   people's own action, not as freedom given.
3. W. E. B. Du Bois, *Black Reconstruction in America* (1935), chapter 4, "The General Strike", and chapter 17, "The
   Propaganda of History" (known to me; the unit already lists the book as P2-DUB, paraphrase only). The foundational
   Black argument that enslaved people's flight and labor withdrawal drove emancipation, and that later history was
   written to erase it.
4. Benjamin Quarles, *The Negro in the Civil War* (1953) (known to me). The first full account of Black wartime
   service by a Black historian; source of the agency framing for USCT service, unequal pay and the Combahee raid.
5. National Archives, "Black Soldiers in the Civil War" (educator article),
   https://www.archives.gov/education/lessons/blacks-civil-war/article.html. About 185,000 compiled USCT service
   records (including white officers); the Bureau of Colored Troops, May 22, 1863; named soldiers (Samuel Cabble,
   Louis Martin, Garland White) with their own records. Taught me that Black soldiers' own words and names are
   readily available in public-domain federal records.
6. National Park Service search on the United States Colored Troops (Appomattox and Chickamauga park pages, via
   search, https://home.nps.gov/apco/learn/historyculture/united-states-colored-troops-at-appomattox.htm). About
   179,000 in the army and about 19,000 in the navy; the round "about 180,000" is fair.
7. American Historical Association, statement on Confederate monuments (2017),
   https://www.historians.org/news/aha-statement-on-confederate-monuments. Most monuments went up from the late 1800s
   into the 1910s and again in the civil rights era, tied to "Redemption" and the end of Black voting; Black citizens
   had no voice in placing them. Taught me why Confederate symbols belong only inside sources.
8. Frederick Douglass, Decoration Day address at Arlington, May 30, 1871 (reprints found via search, among them the
   Frederick Douglass Papers Project item 18357). Confirmed the line the day 82 placeholder points at (finding 8).
9. Jefferson Davis, *The Rise and Fall of the Confederate Government*, vol. 1, part 1, chapter 10 (Project Gutenberg
   19831, found via search). The chapter's topic heading does include "Slavery not the Cause, but an Incident", and
   the quoted clause is Davis's.
10. National Archives, Pacific Railway Act transcript, https://www.archives.gov/milestone-documents/pacific-railway-act.
    Section 2's sentence continues past where the day 79 sheet stops (finding 6).

Two of these are the community's own voice (ASALH; Du Bois and Quarles as Black scholars); the federal pages carry
the Combee people's own name. Where members of the community differ: how much credit Tubman gets as leader
of the raid against Montgomery (Fields-Black argues for Tubman and the Combee people at the center); and how far
Lincoln deserves credit against self-emancipation (Du Bois and later Black historians put the weight on enslaved
people; others, Quarles among them, give Lincoln a larger share). Neither disagreement needs settling for this
section; the days should not present either side as the only account.

Note on the brief's list of five days: I read all five. Day 81 (essay revision) raises nothing; its line that "a
defensible counterclaim is not an invitation to balance a Lost Cause assertion" is right.

## Verdict

Pass with fixes. The section's handling of the unit's hard rules is sound: the Lost Cause is tested and the opener
says plainly that it fails; Stephens is framed with care; no battle role play; Confederate symbols appear only as
sources; no graphic dead; every quotation I could check is accurate except one truncated law, and no figure looks
invented. The fixes are about voice and agency: no Black historian is drawn on anywhere in the five days, Black
soldiers never speak for themselves on day 80, the unequal treatment and violence they faced are never named, and
the people at Fortress Monroe and the Combahee are left nameless or passive.

## Findings, most serious first

### 1. No Black scholarship anywhere in days 78 to 82. LAYER: unit

- **Where.** Every day's teacher page and the opener's "What the teacher needs to know". The unit's own rule (s05,
  days.csv notes for 75, 82 and 85: "Black scholarship on the Lost Cause") and this read's brief require it. The only
  Black voice is Douglass, a primary source, not scholarship. Du Bois appears in the unit only for essay 2 (P2-DUB,
  days 87 to 92). s05 "Sensitivity study" lists Du Bois and the EJI report but nothing on the war, USCT service or
  the Lost Cause.
- **Why it matters.** The days repeat Black scholars' arguments (flight "pressed" policy, "who was left out of the
  reunion story") without crediting the people who made them, which is the erasure day 82 teaches against. A teacher
  with no background has nowhere to go.
- **Fix.** Add interpretation rows to data/plans/us-history-i/sources.csv, use `background`, paraphrase only, status
  "paraphrase to check against the book":
  - `78-DUB`: Du Bois, *Black Reconstruction in America* (1935), chapter 4, "The General Strike"; days 78, 82.
  - `80-QUA`: Benjamin Quarles, *The Negro in the Civil War* (1953); day 80.
  - `80-FB`: Edda L. Fields-Black, *Combee: Harriet Tubman, the Combahee River Raid, and Black Freedom during the
    Civil War* (2024); day 80. Until the book is checked, the NPS "We Called Ourselves Combee" article (a federal work)
    can carry the facts.
  - `82-DUB`: Du Bois (1935), chapter 17, "The Propaganda of History"; day 82.
  - `82-GRE`: Hillary N. Green, *Unforgettable Sacrifice* (on Black communities' memory of the war); day 82.
  Then add one attributed sentence to each teacher page, written only after the check, in this shape:
  - Day 78, Teaching first, after the Fortress Monroe paragraph: "W. E. B. Du Bois argued in 1935 that enslaved
    people's flight to Union lines was a general strike that forced emancipation onto the Union's agenda."
  - Day 80, Pairs, after the Tubman sentence: "Historian Edda L. Fields-Black shows the raid as the work of the Combee
    people themselves, Tubman's scouts and the Black soldiers, many of whom had escaped slavery on those rivers."
  - Day 82, Debrief: "W. E. B. Du Bois called the later story 'the propaganda of history'; historians such as Hillary
    N. Green show Black communities kept their own memory of the war, through Emancipation Days and Decoration Days,
    as Douglass did at Arlington." (Quote Du Bois's chapter title only, which is a title, not prose.)
  Add the same names to s05 "Sensitivity study" and to the opener's teacher background. Per the unit's rule, modern
  historians are paraphrased, never quoted.

### 2. Day 80: Black soldiers never speak for themselves. LAYER: unit

- **Where.** sources-80.md. Source A is Douglass recruiting; C is a white-run Boston paper; D is a posed photograph
  with white officers in front; E is a white cartoonist's image of a Black veteran. Gooding (89-W1) and Taylor
  (89-W2) are reserved for the day 89 test.
- **Why it matters.** The brief asks for people shown "with their own voices and agency". The standard's own day on
  who served documents Black soldiers only through what others said, drew or photographed of them.
- **Fix.** Add a sources.csv row `80F`, a short wartime letter by a Black soldier, public domain, from the Freedmen
  and Southern Society Project's soldier letters or the National Archives' USCT records (for example Spotswood Rice
  to his children, September 1864, or a letter printed in the *Christian Recorder*), cut to about 100 words and
  checked against the transcription, never Gooding (reserved). Put it on the day 80 sheet as Source F and in the
  section plan's Day 80 source list; use it in the share (5 min), where pairs set it beside D: "D shows soldiers as a
  photographer posed them; F is a soldier in his own words." If the reading load is a concern, it replaces nothing:
  the share is where it is read aloud.

### 3. Day 80 and the opener: Black soldiers' unequal treatment and the violence against them are never named. LAYER: section

- **Where.** d080.md says only "Separate a call for service from proof men enlisted or received equal treatment."
  The opener says "about 180,000 served" and nothing more. The unit's rule is violence named plainly.
- **Why it matters.** A grade 11 reader leaves day 80 knowing that Black men served but not what they faced; the
  cartoon's question ("And not this man?") makes no sense without it, and day 89 item 5 asks why service "did not
  itself establish equal treatment".
- **Fix.** Add to the opener under "What the teacher needs to know", and read it in d080.md Pairs after "United
  States Colored Troops names Black Union regiments.", after checking each fact against National Archives and NPS
  pages and recording them in sources.csv: "Black soldiers were paid $10 a month, with $3 of it taken for clothing,
  while white privates were paid $13, until Congress made pay equal in June 1864; men of the 54th Massachusetts
  refused any pay rather than accept less. Their officers were almost all white. The Confederate government
  threatened captured Black soldiers with enslavement or death, and at Fort Pillow, Tennessee, in April 1864,
  Confederate troops killed Black soldiers who were trying to surrender." Under D's description on the sheet add:
  "The officers of the United States Colored Troops were almost all white."

### 4. Day 80 and the opener: Tubman and the Combee people are made passive or nameless. LAYER: section

- **Where.** sources-80.md Source C: the report says only "a Black woman". d080.md: "C reports Tubman guiding Black
  soldiers in the Combahee raid, freeing enslaved people." Opener: "Black Union soldiers freed some 750 people."
  Item s05-X80 sample: "a Black woman guided ... so Tubman led an armed raid", a jump the source does not support.
- **Why it matters.** The people on the rice plantations ran to the boats; the soldiers were mostly men who had
  escaped slavery in that same Lowcountry; Tubman scouted, gathered intelligence and recruited. Saying soldiers
  "freed" people repeats the gift-of-freedom story the section argues against on day 78. And students are told it
  was Tubman with no evidence on the page, on the day that teaches sourcing.
- **Fix.** Opener, replace the Tubman bullet with: "Harriet Tubman, who served the Union army as a scout, spy and
  nurse, guided the June 1863 Combahee River raid in South Carolina. About 300 men of the 2nd South Carolina
  Volunteers, most of whom had escaped slavery, went up the river; more than 750 people ran to the boats and to
  freedom, and more than 150 of the men then enlisted. The people of the Combahee called themselves Combee."
  (Figures from the NPS article; add it as a sources.csv background row.) In d080.md replace the Tubman sentence
  with: "C, written in Boston a month later, does not name the woman who guided the soldiers; later records, among
  them Tubman's own claim for army pay, show it was Harriet Tubman. More than 750 people ran to the boats." Add the
  step "how do we know who 'a Black woman' was?" to the share. Fix the s05-X80 sample to "a Black woman, whom other
  records show was Harriet Tubman, guided..." (items.csv, unit data).

### 5. Day 78: the people who escaped to Fortress Monroe are never named. LAYER: day

- **Where.** d078.md, Teaching first: "In May, enslaved people escaped to Fortress Monroe." The page rightly says
  Butler's letter "records his response, not the escapees' own voices" and rightly glosses contraband, but leaves the
  three men as a category.
- **Why it matters.** Their names are known and are the easiest way to show agency on a day otherwise told through
  Lincoln and Butler.
- **Fix.** Replace the sentence with: "On May 23, 1861, three enslaved men, Frank Baker, Shepard Mallory and James
  Townsend, rowed to Fortress Monroe. Within weeks hundreds more followed." Add the same names to the opener's
  second teacher-background bullet. (Names and date to be recorded in sources.csv from the National Park Service's
  Fort Monroe pages before printing.)

### 6. Day 79: the Pacific Railway Act quotation is cut mid-sentence and printed as if whole. LAYER: section

- **Where.** sources-79.md Source E ends "...to all lands falling under the operation of this act." The sentence
  continues "and required for the said right of way and grants hereinafter made." The opener quotes from it too.
- **Why it matters.** A quotation that drops its own limiting clause without a mark is an altered quotation; the
  unit's rule is that none is invented, and day 79 teaches students to read a law exactly.
- **Fix.** Print the whole sentence, ending "...falling under the operation of this act and required for the said
  right of way and grants hereinafter made.", and add to the gloss: "*right of way*, the strip the track runs on".
  Note in sources.csv 79E: "full sentence of section 2 printed".

### 7. Day 82: who reads Stephens aloud is left open. LAYER: day

- **Where.** d082.md Worked example: "Read A and B aloud with their source lines."
- **Why it matters.** The care around Stephens is good, but a teacher may hand B to a student to read. No child,
  and especially no Black child, should be asked to voice "the negro is not equal to the white man".
- **Fix.** Replace with: "You read A and B aloud yourself, with their source lines; never ask a student to read B
  aloud or copy its words into an answer. Students may refer to it as 'Stephens's 1861 claim'." Same line in At home:
  "The parent reads B."

### 8. Day 82: the Douglass placeholder points at a sentence he did not say in that form. LAYER: section

- **Where.** sources-82.md Source D: "his line that we must never forget the difference between those who struck at
  the nation's life and those who struck to save it". In the 1871 address Douglass objects to being asked "to
  remember with equal admiration those who struck at the nation's life, and those who struck to save it"; the
  "never forget" phrasing belongs to other sentences. The item s05-P82-2 already reads it correctly.
- **Why it matters.** A cutter following the placeholder may stitch a quotation that does not exist.
- **Fix.** Replace the placeholder with: "[to cut: about 60 words ending with his objection to being asked to
  remember 'with equal admiration' those who struck at the nation's life and those who struck to save it, those who
  fought for slavery and those who fought for liberty and justice; check against the Frederick Douglass Papers
  edition]".

### 9. Day 79: slavery leaves the room once the battles start. LAYER: unit

- **Where.** d079.md Teaching first has one line, "The Confederacy defended slavery." Lee's invasions are studied
  only as strategy.
- **Why it matters.** During the 1863 invasion of Pennsylvania, Confederate troops seized free Black people and
  sent them south into slavery; at Milliken's Bend, in the Vicksburg campaign (June 1863), newly raised Black
  regiments fought. Both tie the battles to what the war was about and lead into day 80, without battle detail.
- **Fix.** Add a sources.csv background row for each (NPS Gettysburg and Vicksburg park pages), then one sentence in
  Teaching first after "after Gettysburg, Lee never again invaded the North": "On that march Lee's army seized free
  Black Pennsylvanians and sent them south into slavery. In the Vicksburg campaign Black regiments, newly raised,
  fought at Milliken's Bend in June 1863." Not a role play, no casualty figure.

### 10. Opener and item s05-P79-1: Tennessee is called a "named exception". LAYER: unit

- **Where.** Opener: "named exceptions (Tennessee and parts of Louisiana and Virginia)"; items.csv s05-P79-1 answer,
  same words.
- **Why it matters.** Tennessee was left out of the Proclamation's list, not excepted by name; parts of Louisiana
  and Virginia (including the counties becoming West Virginia) were named. Small, but it is an answer key.
- **Fix.** Opener: "areas it left out or excepted (Tennessee, which it did not list, and named parts of Louisiana and
  Virginia)". s05-P79-1 answer: "...or an area left out or excepted (Tennessee; named parts of Louisiana and
  Virginia)".

### 11. Day 82: the claim card has no source, on a day about sources. LAYER: section

- **Where.** sources-82.md: "A claim printed in many places long after the war".
- **Why it matters.** "In many places" is unsourced and unverifiable; a student cannot do the first sourcing step.
- **Fix.** "Our wording of a claim Jefferson Davis (Source A) and others made after the war, and later repeated on
  monuments and in some school books."  If "monuments and school books" cannot be sourced in sources.csv (the AHA
  statement covers monuments), cut that clause.

### 12. Day 82: Source F turns enslaved people into percentages only. LAYER: section

- **Where.** sources-82.md Source F.
- **Fix.** Under the table add: "Each share is people. In South Carolina in 1860, [checked count] people were held
  in slavery." Fill the count from the census volume when the table is checked; do not print it before.

### 13. Day 79: Grant's memoir date gap is given two ways. LAYER: section

- **Where.** sources-79.md Source C: "Written twenty years after the events"; sources.csv 79C: "remembered 22
  years later". 1863 to 1885 is 22.
- **Fix.** Sheet: "Written twenty-two years after the events".

### 14. Opener: no word guidance for "United States Colored Troops" or "contraband". LAYER: section

- **Fix.** Add to the opener's first sources bullet: "United States Colored Troops is the army's own name for its
  Black regiments; say it as a name, and in your own words say 'Black soldiers'. Contraband was Butler's word for
  people he treated as seized property; use it only when quoting him."

## Checks of quotations, dates and figures

Matched against what I know of the texts and the sources above: Lincoln to Greeley (wording right); Lee to Davis,
September 3, 1862; Stephens's Cornerstone passage; Lee's General Orders No. 9; Confederate Constitution, Article I,
section 9, clause 4, March 11, 1861; Davis's 1881 clause and chapter heading; Conkling letter date; Butler's
letter date; the Combahee report date (July 10, 1863, for a raid of June 1 to 2); "about 180,000" USCT; "some 750"
freed; every share in Source F agrees with the 1860 census totals to the nearest percent (still to be checked against
the volume, as the sheet says). Wrong: the Pacific Railway Act truncation (finding 6) and the Douglass placeholder
(finding 8).

## Could not settle

- s05-K79-1's "about 29,000 Confederate soldiers surrendered" at Vicksburg: I recall the paroled figure as nearer
  29,500. The day already forbids teaching it unchecked; check it against the Vicksburg park page.

## For Cory

- **Money and access.** Findings 1 and 4 need three books checked before their paraphrases can be printed
  (Quarles 1953, Fields-Black 2024, Green), and the project has no library access. Buy them (roughly $20 to $35
  each), or accept the federal NPS articles as the checkable stand-in for the facts and keep the historians' names
  as "read further" only?
