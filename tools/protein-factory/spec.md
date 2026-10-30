# Protein Factory

## One idea
Work the line in a protein factory: copy a real gene's DNA into messenger RNA, read it three letters at a time on
the codon wheel to chain amino acids, then take ten work orders that change the gene on purpose (one letter that
makes sickle hemoglobin, one that changes nothing, one that stops the line, one extra letter that scrambles
everything after it, three missing letters that remove one amino acid) and see that a protein's shape and job come
straight from its DNA sequence.

## Not like
- gene-pool (grade 8, genetics family): breeding made-up creatures to see traits pass on. Here no breeding; the
  path from one real gene to one real protein, letter by letter.
- punnett-predictor (same group, genetics family): chances of inheriting versions of genes. Here what a version of a
  gene is, at the level of letters.
- membrane-gatekeeper (same group): shows the F508del CFTR protein missing from the membrane. Here the same change
  from the DNA side (three letters deleted); the two tools cite each other.
- equation-balancer (sci 10, puzzle): balancing atoms. Here the puzzle is reading frames and codons.
- Any cipher or code tool: the genetic code is not a secret code; the tool says it is read by a machine (the
  ribosome) the same way in nearly all living things.

## Who and how
Grade 9, science (Life Science module DNA and Protein Synthesis: "From genes to proteins"). Driver: students on
laptops, alone or in pairs. 20 to 40 minutes; levels are short so it fits a part period. Standards: HS-LS1-1 (the
structure of DNA determines the structure of proteins, which carry out the functions of life), HS-LS3-1 (DNA and
chromosomes code the instructions for traits passed from parents to offspring).
Topic line: DNA, RNA and protein synthesis.
9-12 dark theme. Header: title, `.seg` modes **Work orders**, **Free lab**, kit buttons `motion`, `sound`, `read`.

## Screens and modes
Layout: stage left at about 65 percent of the width, panel right. The stage sits on the painted cytoplasm backdrop
(pf-cytoplasm, dimmed to 35 percent so every letter keeps its contrast). Stage, top to bottom, like a factory line: the **DNA** (two strands, coding strand on top with codon brackets and
codon numbers, template strand below), the **mRNA** strip, the **ribosome** (a rounded body that slides along
the mRNA one codon at a time: the painted pf-ribosome cutout), and the **protein chain** (beads, one per amino acid, three-letter code on each,
colored by property with a key: water-avoiding, water-loving, charged plus, charged minus, special; the key also
uses bead shapes). Panel: the **work order** card (goal, tools allowed, **Check order**; the text is code, laid over
the painted blank pf-order-board), the **codon wheel** (the standard table drawn as a wheel in code, at most 220 px
across: first letter inner ring, second middle, third outer; clicking a slice names the amino acid), `hint`, `tip`.
Focus (both modes): the line, and on it the codon under the ribosome and the bead it makes. The line is the biggest,
central thing at every size; the card and wheel sit beside it, never above it.
Editing tools (buttons and keys): **Change a letter** (select a base, then A, C, G or T), **Insert a letter**
(select a gap between bases), **Delete a letter**, **Undo**. After every edit the mRNA, ribosome reading and chain
redraw; changed bases and changed beads get an accent outline; a **Compare** strip shows the original chain above
the new one with differences marked.

**Work orders** (opens first). Ten orders, all open from the start (a checklist marks done ones):
1. Transcribe: build the mRNA for the first 7 codons of the HBB gene by choosing the base that pairs with each
   template base (A pairs with U in RNA). The mRNA strip shows 21 empty boxes; click a box (or arrow to it), then
   press **A**, **C**, **G** or **U** (buttons under the strip, or keys). Check: the mRNA matches.
2. Translate: for each of those 7 codons pick its amino acid from the codon wheel. The chain shows 7 empty bead
   slots; click a slot (or the codon above it), then click a wheel slice to place that amino acid in the slot. (The
   wheel never edits the gene.) Check: M V H L T P E.
3. Sickle hemoglobin: change one letter so amino acid 7 becomes valine.
4. Hemoglobin C: change one letter so amino acid 7 becomes lysine.
5. Silent change: change one letter in codons 1 to 21 so the protein does not change at all.
6. Stop early: change one letter so the chain stops after 8 amino acids.
7. Frameshift and fix: insert one letter in codon 3 (before its first, second or third letter; every such
   insertion scrambles the chain and stops it after 6 amino acids), then delete one other letter within codons 3 to 6
   so there is no early stop. A deletion that gives back the original DNA exactly is refused: "That undoes the
   order. Delete a different letter." Check reports how many amino acids differ from the original and the fewest
   possible for the letter you inserted (the tool tries every allowed deletion; it is 1 for 10 of the 12 insertions
   and 0 for 2, where the fix lands on a silent codon).
8. CFTR F508del: on the CFTR gene's codons 505 to 511, delete three letters (one at a time, anywhere) so
   phenylalanine 508 is removed and every other amino acid stays the same.
9. Write a gene: write the shortest DNA that makes M-A-G-I-C and then stops. Check: valid, and the card says "Yours
   is one of 288 genes that make this protein."
10. Your own order: make any change, then classify it yourself (silent, changes one amino acid, early stop, frame
    shift, removes or adds whole amino acids); Check compares your label with the tool's.
**Check order** gives a plain result: "Order complete" (no fanfare) or what is still off ("Amino acid 7 is still
glutamic acid"). Orders 3, 4 and 8 then open their calm health card with its painted picture.

**Free lab**. Pick a gene: **HBB (first 21 codons)**, **CFTR (codons 505 to 511)**, or **Blank** (type DNA, up to
60 letters). All editing tools, the classifier readout ("This change: changes one amino acid, Glu to Val") and a
**Show reading frames** toggle that shows the three possible frames under the strip.

## Content
HBB coding sequence, start (NCBI RefSeq NM_000518.5), codons 1 to 21:
ATG GTG CAT CTG ACT CCT GAG GAG AAG TCT GCC GTT ACT GCC CTG TGG GGC AAG GTG AAC GTG
Protein: M V H L T P E E K S A V T A L W G K V N V (matches UniProt P68871 start).
Numbering note shown on screen: "We count the start methionine as 1. Doctors and many books call the sickle change
'position 6' because the finished protein loses that first methionine."
Checked answers (Python, Curio Class 2026-10-27, standard code):
- Order 3: codon 7 GAG to GTG, Glu to Val (chain M V H L T P V E K ...). The only one-letter change that gives Val at
  7 (GTG); GAG cannot reach the other Val codons in one step.
- Order 4: codon 7 GAG to AAG, Glu to Lys.
- Order 5: many answers, for example codon 7 GAG to GAA (still Glu).
- Order 6: codon 9 AAG to TAG (Lys to stop): chain stops after 8. Other answers (for example codon 8 GAG to TAG
  stops after 7) do not meet "after 8"; only codon 9 with a first-letter change to T works (AAG to TAG).
- Order 5: 47 one-letter changes in codons 1 to 21 are silent; all are accepted.
- Order 7: all 12 insertions inside codon 3 (3 places x 4 letters) stop the chain after 6 amino acids. Insert G after
  the first letter of codon 3 (CAT becomes CGA...): chain M V R S D S stop. Then deleting any one other letter from
  the start of codon 3 to the end of codon 6 removes the stop; the number of changed amino acids runs from 1 to 4.
  Fewest possible per insertion: 1 for 10 of the 12; 0 for C or T inserted before the third letter of codon 3 (a
  later deletion leaves CAC or CAT, both His), so the card computes it rather than printing a fixed 1 (the old
  "fewest possible: 1" was wrong for those two). For example deleting the A just after the inserted G gives M V R L T P E E K ... (only H
  became R); deleting the first letter of the shifted codon 5 gives M V R S T P ... (2 differ). (Crick et al. 1961
  used this plus-one, minus-one trick to show the code is read in threes.)
- Order 8: CFTR codons 505 to 511 AAT ATC ATC TTT GGT GTT TCC (NM_000492.4), protein N I I F G V S. Deleting CTT (the
  last letter of codon 507 and the first two of 508) gives AAT ATC ATT GGT GTT TCC: N I I G V S. Codon 507 changes
  ATC to ATT but stays isoleucine. Three runs of three letters in a row give N I I G V S (TCT, CTT and TTT), and
  seven picks of any three letters do (positions 7 to 11 of the 21, in the combinations checked); they make only two
  different genes: ...ATC ATT GGT... (codon 507 ATT) and ...ATC ATC GGT... (deleting TTT; codon 507 stays ATC). All
  are accepted, and the card says the real F508del deletes CTT.
- Order 9: the shortest answer is 18 letters (5 codons plus a stop); codons for M 1, A 4, G 4, I 3, C 2, stop 3: 1 x 4 x 4 x 3 x 2 x 3 = 288 genes.
Health cards (calm, factual, shown after orders 3, 4 and 8):
- Sickle: "Two copies of this version cause sickle cell disease: the hemoglobin sticks together when oxygen is low
  and red blood cells bend into a sickle shape. One copy is called sickle cell trait. Valine is water-avoiding where
  glutamic acid was charged: one letter changed the protein's surface."
- HbC: "Hemoglobin C is another version at the same spot. It is usually mild."
- F508del: "This is the most common change behind cystic fibrosis. The protein folds wrong and does not reach the cell
  surface (see Membrane Gatekeeper)."
Bead properties (OpenStax Biology 2e 3.4 grouping, simplified): water-avoiding A V L I M F W, water-loving S T N Q Y,
charged plus K R H, charged minus D E, special G P C; the key lists them.
Hints: Work orders "<b>Work orders.</b> Read the order, edit the DNA, then press Check order." / Free lab "<b>Free
lab.</b> Change, insert or delete letters and watch the chain."
Tips: "Three letters, one amino acid: a codon." / "Most amino acids have more than one codon, so some changes are
silent." / "One extra letter shifts every codon after it." / "A missing set of three removes one amino acid and keeps
the rest in frame."
Model limits line: "Real genes have parts that are cut out (introns) and switches that control them. Here only the
part that codes protein, and only a short stretch."

## Interactions in detail
- Bases are focusable buttons; arrow keys move, letters A C G T change, Insert key or I inserts a gap letter,
  Delete removes. Screen readers hear "Codon 7, base 2, A".
- After each edit the ribosome slides from the first changed codon to the end, one codon per 250 ms (at most 21
  codons, about 5 s; Motion off: instant chain). The chain, compare strip and classifier update at once; only the
  ribosome and the bead pop-in are animated, so nothing waits on the slide.
- Every control stays live while the ribosome slides: a new edit stops the slide, redraws at once and starts a new
  slide from its own first changed codon; Undo does the same; Check order checks the current gene at once (it never
  waits for the slide); a mode switch or Reset order stops the slide.
- The codon wheel highlights the codon under the ribosome; clicking slices only reads (it never edits the gene),
  except in order 2, where a selected bead slot takes the clicked amino acid.
- Orders reset their gene when opened; Undo works up to 50 steps.
- Check order uses `Code.classify` and the order's test; it never reveals the answer, only what is off.
- Mode change: `V.hush()`; each order keeps its edits until Reset order.

## Look
Accent `--brand #e0ff1a` (hi-vis safety yellow-green, a factory floor), `--brand-ink #10161f`. Stage `#10151c`
under the painted cytoplasm backdrop (dimmed so the stage reads no lighter than `#1a2028`). Base colors with
letters always shown: A `#7dd87d`, T and U `#ff8a8a`, G `#ffd166`, C `#7cb8ff`. Bead colors: water-avoiding
`#d9c9a3`, water-loving `#8fe3d2`, charged plus `#8fb5ff`, charged minus `#ff9d8f`, special `#d0a8ff`, each with a
shape (round, rounded square, plus-notch, minus-notch, diamond). The painted ribosome is warm violet-gray, so it
never matches a base or bead color.
Contrast (computed): brand on --panel 15.24:1, on --sec-bg 14.44:1; brand-ink on brand 15.99:1. Nearest 9-12
accent #b6f23a (dE 17); in this group punnett-predictor's #a3ffaf (dE 60).

## Art
Local FLUX (`scripts/localart.py`), no people. 6 images. House style for all: a clean painted science
illustration, soft light, muted deep colors, blank surfaces with no lettering.
- pf-cytoplasm: an even full-frame texture of the inside of a cell, deep blue-violet watery gel with faint soft
  shapes of tiny round particles and threadlike fibers, dark and low in contrast; 16:9; cutout no; people no; the
  stage backdrop behind the line, dimmed to 35 percent.
- pf-ribosome: a single ribosome, a rounded two-part molecular machine, a larger lumpy upper body sitting on a
  smaller lower body with a narrow groove between them, warm violet-gray, soft lit, on a plain green background;
  4:3; cutout yes; people no; slides along the mRNA strip, the groove over the codon being read.
- pf-order-board: a blank cream paper work order clipped to a dented steel clipboard, top view, shop-floor light;
  3:4; cutout yes; people no; behind the work order card text (text in code).
- pf-sickle-cells: red blood cells seen under a microscope, several smooth round disk-shaped cells beside several
  long curved crescent-shaped cells, pale background; 4:3; cutout no; people no; the sickle health card.
- pf-round-cells: red blood cells seen under a microscope, many smooth round disk-shaped cells with a soft paler
  center, pale background; 4:3; cutout no; people no; the hemoglobin C card.
- pf-airway: a close-up painted cutaway of the lining of a small airway, a row of tall cells with fine hairlike
  cilia on top under a thick layer of sticky glistening mucus; 4:3; cutout no; people no; the F508del card.
Drawn in code: DNA and mRNA strips, bases, codon brackets, beads, compare strip, codon wheel, key, card text,
preview.svg.

## Voice
Bank `upbeat-guide` (a factory floor lead on a tour): brisk, friendly, never cheering. Uses `Curio.voice`,
scope = mode. No neighbor in this batch or in `neighbors.py` uses it.
- welcomeOrders (how; Work orders entered; stale once any order is opened or edited): "Welcome to Protein Factory.
  Pick a work order from the list, then follow it and press Check order."
- transcribeHow (how; order 1 opened; stale once a box is filled): "Click an empty mRNA box, then press the base
  that pairs with the template letter below it."
- translateHow (how; order 2 opened; stale once a slot is filled): "Click an empty bead slot, then click its amino
  acid on the codon wheel."
- editHow (how; the first of orders 3 to 10 opened; stale after the first edit): "Click a letter in the DNA, then
  press Change, Insert or Delete. Press Check order when you think it's done."
- welcomeFree (how; Free lab entered; stale after the first edit): "Free lab. Pick a gene, then change, insert or
  delete letters and watch the chain."
- wheel (how; first codon wheel click; stale once the next codon is read): "Read the codon from the middle out:
  first letter, second, then third."
- frameshift (how; first frame shift in a session; stale on the next edit): "One extra letter, and every codon after
  it is read differently."
- orderDone (event; each completed order; stale on the next edit or order switch): "Order complete. Check the
  compare strip to see what changed."
- notYet (event; each Check that fails; stale on the next edit): "Not yet. The card says what's still off."
- sickleCard (event; order 3 done; stale when the card closes): "One letter changed, and the protein's surface
  changed with it."
- undone (event; each refused deletion in order 7; stale on the next edit): "That undoes the order. Delete a
  different letter."

## Family engine
**genetics** family. The engine is described in full in punnett-predictor's spec (`kit/genetics.js`). This tool
feeds: `Code` (standard codon table, `transcribe`, `translate`, `mutate` with change, insert and delete,
`classify` into silent, missense, nonsense, frameshift, in-frame deletion or insertion), `Strand` (two-strand
DNA and mRNA view with codon brackets and focusable bases), `Chain` (property-colored, shaped beads with a compare
strip), and the codon wheel drawing. Gene data: HBB codons 1 to 21 and CFTR codons 505 to 511.

## Sources
- HBB coding sequence: NCBI RefSeq NM_000518.5 (Homo sapiens hemoglobin subunit beta), https://www.ncbi.nlm.nih.gov/nuccore/NM_000518.5
  (checked 2026-10-27); protein UniProt P68871.
- CFTR coding sequence codons 505 to 511: NCBI RefSeq NM_000492.4, https://www.ncbi.nlm.nih.gov/nuccore/NM_000492.4
  (checked 2026-10-27).
- Standard genetic code: NCBI, "The Genetic Codes", table 1, https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi
- Sickle cell disease and trait, the Glu to Val change: NIH MedlinePlus Genetics, "HBB gene" and "Sickle cell
  disease" (https://medlineplus.gov/genetics/gene/hbb/); NIH NHLBI, "Sickle Cell Disease".
- Hemoglobin C: NIH MedlinePlus Genetics, "HBB gene" (variants section).
- F508del in CFTR, misfolding: NIH MedlinePlus Genetics, "CFTR gene", https://medlineplus.gov/genetics/gene/cftr/
- Reading frame shown by insertions and deletions: Crick, F. H. C., Barnett, L., Brenner, S. and Watts-Tobin, R. J.
  (1961), "General nature of the genetic code for proteins", Nature 192:1227-1232.
- Transcription, translation, mutations and amino acid properties: OpenStax Biology 2e, chapter 15 "Genes and
  Proteins" and section 3.4 (CC BY 4.0), https://openstax.org/books/biology-2e/pages/15-introduction
- Checks run in Python against the standard table (Curio Class, 2026-10-29, re-running the 2026-10-27 answers):
  HBB 1 to 21 translates to M V H L T P E E K S A V T A L W G K V N V. Every one-letter change tried: order 3 has
  exactly one answer (codon 7 GAG to GTG), order 4 one (GAG to AAG), order 6 one (codon 9 AAG to TAG), order 5 has
  47 silent answers. Order 7: all 12 insertions inside codon 3 stop after 6 amino acids; every later deletion in
  codons 3 to 6 tried; fewest changed is 1 for 10 insertions and 0 for 2 (fixed the old fixed "1"). Order 8: every
  set of three deletions tried; 7 give N I I G V S, making 2 distinct genes (fixed the old "exactly three" and the
  claim that codon 507 always reads ATT). Order 9: 1 x 4 x 4 x 3 x 2 x 3 = 288. Ribosome slide: 21 codons x 250 ms
  = 5.25 s.

## Done when
1. Order 1 fills by clicking a box and pressing a base; order 2 completes only with M V H L T P E placed from the
   wheel into the slots.
2. Order 3 completes with codon 7 GAG to GTG; the chain reads Val at 7 and the calm sickle card shows with its
   painted cells.
3. Order 6 completes only with codon 9 AAG to TAG (chain of 8).
4. Order 7: inserting G in codon 3 shows an early stop after 6 amino acids; deleting the A after it completes the
   order with 1 amino acid changed (H to R) and "fewest possible: 1"; inserting C before CAT's last letter reports
   "fewest possible: 0"; deleting the inserted G itself is refused with "That undoes the order".
5. Order 8 accepts deleting CTT (codon 507 reads ATT), TCT, or TTT (codon 507 reads ATC), and any other three single
   deletions that give N I I G V S.
6. Order 9 accepts any 18-letter gene for M A G I C plus a stop and says "one of 288".
7. Focus: at 1366x768 and 680x425 the line (DNA, mRNA, ribosome, chain) is the largest thing on screen and the
   wheel is no wider than 220 px.
8. A tap while the ribosome slides: an edit made mid-slide redraws the chain in the same frame and restarts the
   slide; Check order mid-slide answers at once.
9. Every base can be changed, inserted or deleted by keyboard; screen readers hear codon and base positions.
10. Main controls visible at 1366x768 and 680x425; strands scroll inside their frame at 375 wide.
11. Each how-to line speaks once in five repeated actions and never names a control that is not on screen;
    orderDone speaks each completed order.
12. All 6 images load and none shows a person; letters stay readable on the cytoplasm backdrop; no network, no em
    dashes; health cards are calm and cite NIH.

## Open questions
- [protein-factory] Orders 3, 4 and 8 name sickle cell disease, hemoglobin C and cystic fibrosis with short calm
  cards. Keep the disease names, or describe the changes without them?
