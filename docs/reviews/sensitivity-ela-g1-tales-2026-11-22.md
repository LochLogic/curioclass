# Sensitivity read: ELA grade 1 tales g1-u2-03 and g1-u2-04 (2026-11-22)

Read: both texts, their sources.csv rows, and the day files that read them (d035 to d046).

## g1-u2-03, Why the Sun and the Moon Live in the Sky (Efik and Ibibio)

Culture and tense: correct. "the Efik and Ibibio people of southern Nigeria" and "a story the Efik and Ibibio people ... tell" are present tense (texts/g1-u2-03.md:19; d035.md:25). It is framed as a tale throughout.
Content: no stereotype, no sacred or ceremonial content, no mocking names. The Sun and Moon are a married pair and the Water is a person with "people", as in the collected tale. Keeping "Water" masculine matches the source.
Core: recognizable. Friends, the visits, "build a huge compound", the repeated "is it safe", the roof, the sky all match Dayrell's tale XVI. The retelling adds only "They did not know what would happen" (line 47) and "I warn you" (line 27); both are harmless.

Must-fix: none.

Should-fix:
- texts/g1-u2-03.md:12 says Dayrell's colonial-era limits "are named on the teacher page". The credit lines in d035.md:103 and d035.md:8 do not name them, and grep of the course found no "colonial" in the day files. Fix: add one plain sentence to the d035 teacher notes, or drop the claim from line 12.
- texts/g1-u2-03.md:14 still says "The required tradition-specific sensitivity read has not been done". Fix: update after this read.
- texts/g1-u2-03.md:28 and :34, picture notes: say "Sun and Moon drawn as friendly figures, no skin color or costume tied to any real people." Fix: add that line so artists do not draw the figures as caricatured Africans.

Fine: credit line (d035.md:103) is right: names the people, the collector and the year, and says "Changed by Curio Class". Source row names a solid source. The Project Gutenberg URL in sources.csv is a real page. I opened the pglaf mirror of ebook 34655, which Project Gutenberg hosts, and confirmed the events above.

## g1-u2-04, The Weaver Girl and the Cowherd (Chinese)

Culture and tense: correct. "a story people in China still tell" (texts/g1-u2-04.md:18) and d041.md:23 ("they still tell it") are present tense. It is a tale, not fact.
Content: no stereotype, no exotic framing, no costume or accent acting (teacher note forbids it). The names are the real names. No religion is retold; the Queen Mother is only a grandmother figure.
Core: recognizable. Sky weaver, cowherd, the river of stars, the magpie bridge, the yearly meeting, the stars Vega and Altair all match the traditional tale. Omitting the marriage without permission, the two children and the clothes-taking is disclosed (line 60) and fine for age six.

Must-fix:
- texts/g1-u2-04.md:58 cites Wikipedia "via search summary" as a source. Fix: delete that bullet; the project rule bars it.
- data/plans/english-language-arts-grade-1/sources.csv, row g1-u2-04: the URL column is empty, so the row names no solid source. Fix: put the Shanghai page below in the URL column; the row should also name a second source (see below), since I found only one.

Should-fix:
- texts/g1-u2-04.md:30 "Queen Mother of the Sky". The usual figure is the Queen Mother of the West (Xi Wangmu), and the Shanghai page names the Jade Emperor's family instead. I did not confirm the "of the West" naming in a source I opened. Fix: write "her grandmother, the Queen Mother" or "her grandmother, who ruled the sky" so the name is not invented.
- texts/g1-u2-04.md:57 and :13 give the Shanghai city government "Learn Chinese" page as the source. It is an official Chinese institution, but it is a language-learning page, not a folklore collection. Fix: add a university, museum or library folklore source when one is found.

Fine: festival facts. Qixi is the seventh day of the seventh month in the Chinese calendar, the magpie bridge is on that day, and Vega and Altair are the weaver and cowherd stars; the Shanghai page confirms all of these. "on the seventh night" (line 46) is consistent. The pronunciation hints in d041.md:25 are fine. The credit in d041.md:8 is right.

## Sources opened

- https://gutenberg.pglaf.org/3/4/6/5/34655/34655-h/34655-h.htm, Project Gutenberg mirror, Dayrell, Folk Stories from Southern Nigeria (1910), tale XVI: the Sun and the Water are friends who lived on earth; the Water asks for a very large compound; the Sun's wife is the Moon; the Water enters with fish and water animals, asks "is it safe" repeatedly; the Sun and Moon say yes; they end on the roof and then go into the sky. Matches the retelling. Public domain.
- https://english.shanghai.gov.cn/en-LearnChinese/20240806/edd565989b6d4b6589efe6ec09ffd161.html, Shanghai Municipal People's Government, "Learn Chinese: Qixi Festival": Qixi is the 7th day of the 7th lunar month; Zhinu (of the Jade Emperor's family) and the cowherd Niulang are parted by the Milky Way; magpies make a bridge once a year; Vega is the Weaver Girl star and Altair the Cowherd star. It also says they had two children, and it does not name a grandmother.

## Fixes applied (2026-11-22)

- g1-u2-04 line 58 Wikipedia bullet: removed; replaced with the Musselman Library (Gettysburg College) Special Collections page, opened and checked 2026-11-22.
- sources.csv row g1-u2-04: url now holds the library page and the Shanghai page; status "checked: 2026-11-22" with what each page states. The USC folklore archive page could not be opened (certificate error), so it is not cited.
- "Queen Mother of the Sky" is now "her grandmother, the Queen Mother" (page 4) and "her grandmother" (page 5); the choices note was reworded; d044 only says "the Queen Mother" and was left.
- g1-u2-03 line 12: the colonial-era sentence was added to d035's Credit teacher note; line 14 status updated; the three picture notes now say the figures carry no skin color or costume tied to real people. Same line added to g1-u2-04's sensitivity status note.
