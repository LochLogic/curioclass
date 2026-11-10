# Who Gets to Vote?

## One idea
A long gallery wall runs from 1776 to 1870, and on it hang real voices about who should vote: a New Jersey widow who could vote under the 1776 constitution until the 1807 law took it away; a New York delegate in 1821 arguing to drop the property rule for white men while raising it to $250 for Black men; a Rhode Island worker in the Dorr Rebellion of 1841-42; Elizabeth Cady Stanton and Frederick Douglass at Seneca Falls in 1848; Frances Ellen Watkins Harper in 1866 on being both Black and a woman; William Apess, a Pequot minister, in 1833 on the rights his people were denied; and the 1869 split between women's groups over the 15th Amendment; the child reads each voice, tags who they spoke for and against, then slides a "who can vote" bar across the decades for each group (white men without property, Black men, women, Native Americans) and explains in their own words how and why views changed and who was left out, so an eighth grader learns how and why perspectives changed over time and to weigh many perspectives rather than one.

## Not like
- voices-of-freedom (8, spec): voices on slavery. Here voices on voting.
- reconstruction-amendments (8, spec): the 15th Amendment as law. Here the long argument before it.
- two-parties (8, spec): the 1790s party fights. Here who could join the vote at all.
- state-quest (3-8, live): state facts on a map. Here one right across states and time.

## Who and how
- Grade 8, Social Studies (History), module "Reform and Rights". Standards: D2.His.5.6-8 (explain how and why perspectives of people have changed over time), AASL II.B.2 (evaluating a variety of perspectives during learning activities), AASL II.B.3 (representing diverse perspectives during learning activities).
- Format: gallery. Driver: one child alone (tool.json `driver: "student"`). `Read` reads every card. Controls 44 px or more.
- Nine voices on the wall, tags, four "who can vote" bars, the change card, the missing-voice card. Extra: Gallery talk (the child picks two voices that disagree and writes a short exchange in their own words). tool.json `modes: ["Gallery", "Gallery talk"]`, `minutes: "25-35"`, `grades_label: "Grade 8"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.His.5.6-8 | Slide each group's bar through the decades and write why the view changed | the four bars with labeled steps; the change card | 3, 4 |
| AASL II.B.2 | Tag each voice: who they spoke for, who they left out, and why | the voice cards with tags | 2 |
| AASL II.B.3 | Fill the missing-voice card for one group with few recorded words | the missing-voice card | 5 |

## Screens and modes
Header (kit): title "Who Gets to Vote?"; `Gallery`, `Gallery talk`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** A gallery wall with a timeline rail from 1776 to 1870, nine frames hung along it, and below the rail four empty bars labeled "White men without property," "Black men," "Women," "Native Americans." The welcome is queued (`welcomeAfter: true`): "In 1776 most Americans could not vote. By 1870 more could, but not everyone. These people argued about it. Tap the first frame." First hint: "Tap the 1776 frame."

**The voices (focus: the open frame).** At 1366x768 the frame opens at the center with tags at the side; at 680x425 the tags are a sheet. Each frame: a real portrait or document image, a short excerpt (under 15 words where quoted, credited), and a plain note.
1. 1776: New Jersey's constitution lets "all inhabitants" with enough property vote; some women and free Black residents do.
2. 1807: New Jersey's legislature limits voting to white male taxpayers.
3. 1821: New York's convention drops the property rule for white men but keeps a $250 property rule for Black men only.
4. 1833: William Apess, a Pequot minister, in "An Indian's Looking-Glass for the White Man," on the rights his people were denied.
5. 1841-42: the Dorr Rebellion in Rhode Island, where most men without land could not vote; a "People's Constitution" and a crisis.
6. 1848: Seneca Falls; the Declaration of Sentiments asks for the vote; Frederick Douglass speaks for it when others hesitate.
7. 1865: a Colored Convention petitions for the vote for Black men.
8. 1866: Frances Ellen Watkins Harper at the National Woman's Rights Convention, on being both Black and a woman.
9. 1869-1870: the women's movement splits over the 15th Amendment, which bars denying the vote by race but not by sex; the National Woman Suffrage Association opposes it and the American Woman Suffrage Association supports it.
- Excerpts are chosen with care; one 1869 frame notes that some white suffragists used racist arguments against the amendment, named plainly without quoting slurs.

**Tags (AASL II.B.2).** For each voice the child tags: who they spoke for, who they left out, and why (property, race, sex, nation, party). A note after each shows what the record says.

**The bars (the aha, D2.His.5.6-8).** For each group the child slides through the decades and the bar fills where the record says (property rules dropped for most white men by about the 1850s; Black men gain the vote by the 15th Amendment in 1870, though states soon blocked it; women in no state by 1870 except the territory of Wyoming in 1869; most Native Americans not citizens until 1924). At each step a change card asks "What changed people's minds here?" from tiles (new states in the West wanted settlers; the war and Black soldiers' service; reformers' petitions; party advantage) plus one line. Narrator: "Views changed, but slowly, and seldom for everyone at once."

**The missing voice (AASL II.B.3).** For one group with few recorded words (enslaved people, Native women, poor women), the child names what kind of source might hold their view and writes one line on why it is missing.

**The end.** The tagged frames, the four bars, the change card and the missing voice. `Print` prints them.

**Gallery talk (extra).** The child picks two voices who disagree and writes a short exchange in their own words, labeled "written by a student".

## Content
- Nine frames with portraits or documents, short excerpts, plain notes; tag tiles; four bars with dated steps; change tiles; the missing-voice card.
- All people, documents, dates and rules are real and sourced; excerpts are under 15 words and credited.
- The 1869 split is told with both sides' reasons and with the racism some used named plainly.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Frames open in any order; the bars open after six frames are tagged.
- A bar step can't be filled past what the record supports; a reason line explains.
- Keyboard: Tab to frames, tags, bars and cards; Enter to open and tag; arrows slide a bar.
- With Motion off frames open without zoom and bars fill without sliding.

## Look
- Accent `--brand` #0f6655 ballot green (header, frames, the rail); gold #f4c542 (the open frame, a filled bar step); paper #eef6f4; ink #03221b; muted #4a5a56.
- Contrast (WCAG 2.1, computed): white on brand 6.88:1; brand on paper 6.27:1; ink on paper 15.32:1; muted on paper 6.62:1; ink on gold 10.34:1.
- Never color alone: bar steps carry years and labels; tags carry words.
- Different from this batch (dusk violet, map slate, claret, prairie rust).

## Art
- Public domain portraits and documents (Library of Congress, National Portrait Gallery, ids checked at build): Frederick Douglass; Elizabeth Cady Stanton; Frances Ellen Watkins Harper (1898 portrait); William Apess (1830s engraving); Thomas Dorr; the 1776 New Jersey constitution; the Declaration of Sentiments; a Colored Convention proceedings page; the 15th Amendment print (1870). Each with credit.
- Real faces only.
- Drawn in code: the wall, rail, frames, bars, cards.
About 9 images.

## Voice
Two bank voices, each unique in this batch: `curious-librarian` as the narrator and hints; `big-sister` as the reader of excerpts, introduced each time as "from" the speaker, never playing them. `Curio.voice` with `scope: () => state.mode + ':' + state.frame + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- event, whole, each frame's plain note.
- event, whole, each excerpt.
- how `tag`: "Tag who this voice spoke for, and who they left out."
- how `bar`: "Slide this bar to the next change, then say why."
- how `missing`: "Name a voice the record is missing."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the gallery rail, frames, tags, four bars with dated steps, change and missing-voice cards.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Tags | Tag every voice as speaking for everyone | Each "left out" tag checks against the record (Seneca Falls asked for women, not Native nations). |
| Bars | Fill every bar to the end | Steps fill only as far as the record supports. |
| Change | Pick the same reason every time | Each step accepts only the reasons the record supports there. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). Plain note (whole), waits; excerpt (whole).
2. `tag`, for each frame.
3. `bar`, for each step.
4. `missing`; `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.His.5.6-8; AASL II.B.2 and II.B.3 | C3 Framework (NCSS, 2013, rev. 2017) and data/standards/c3-indicators.txt | AASL National School Library Standards (2018) and data/standards/aasl-2018.txt | yes |
| New Jersey women and free Black residents voted under the 1776 constitution until the 1807 law | Museum of the American Revolution, "When Women Lost the Vote" | Klinghoffer and Elkis, "The Petticoat Electors," Journal of the Early Republic (1992) | yes |
| New York 1821: property rule dropped for white men, $250 kept for Black men | New York State Archives, 1821 convention | Keyssar, "The Right to Vote" (Basic Books, 2000; rev. 2009) | yes |
| William Apess, "An Indian's Looking-Glass for the White Man" (1833) | O'Connell, ed., "On Our Own Ground" (UMass Press, 1992) | National Park Service, "William Apess" | yes |
| The Dorr Rebellion (1841-42) | Rhode Island State Archives | Keyssar (2000) | yes |
| Seneca Falls (1848), the Declaration of Sentiments, Douglass's support | National Park Service, Women's Rights National Historical Park | Library of Congress, "Seneca Falls" | yes |
| Harper's 1866 speech; the 1869 split (NWSA against, AWSA for the 15th Amendment) | National Park Service, "Frances Ellen Watkins Harper" | Library of Congress, "Women's Suffrage" collection essay | yes |
| Wyoming Territory 1869; most Native Americans not citizens until 1924 | National Archives, Indian Citizenship Act (1924) | Wyoming State Archives, "Woman suffrage 1869" | yes |
| Colored Conventions petitioned for the vote | Colored Conventions Project (University of Delaware) | Library of Congress | yes |
Backed twice: 9. Cut: 0.

Sensitivity note: race, sex and Native rights are central; excerpts are short and credited; the racist arguments some suffragists used in 1869 are named plainly without slurs; real faces only, and the excerpt voice never plays a real person. A fresh-agent read of the frames is needed before build.

Checks run (Python, scratchpad r16, 2026-11-09): frames in date order (1776, 1807, 1821, 1833, 1841, 1848, 1865, 1866, 1869); New Jersey women voted for 31 years (1776 to 1807); the 1924 Citizenship Act is 54 years after 1870; four bars, each with at least two dated steps; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 frame and tags; at 680x425 sheet.
2. Each voice is tagged for who it spoke for and left out, checked. (AASL II.B.2)
3. Four bars fill only as far as the record supports. (D2.His.5.6-8)
4. The change card names why views changed at each step. (D2.His.5.6-8)
5. The missing-voice card names a gap and a kind of source. (AASL II.B.3)
6. Gallery talk labels the exchange "written by a student".
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: no zoom or sliding; no network requests.

## Open questions
- Sensitivity flag: race, sex and Native rights in the fight over the vote, including racist arguments some suffragists used (default used: short credited excerpts, racism named without slurs, real faces only, fresh-agent read before build).
