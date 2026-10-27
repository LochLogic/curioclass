# Punnett Predictor

## One idea
A Punnett square is a shortcut for meiosis: set up a cross, open the square to watch the chromosomes that made each
row and column separate, breed 1, 10, 100 and 1,000 offspring to see the real ratio wander and then settle on the
prediction, test Mendel's own pea counts with chi-square, and then meet two fruit fly genes on the same chromosome
that break the square, where only crossing over makes the rare combinations.

## Not like
- gene-pool (grade 8, genetics family): breeding made-up creatures, mutations and selection over many generations.
  Here one cross at a time with real organisms (peas and flies), the probability behind it and a statistical test.
- protein-factory (same group, genetics family): what a version of a gene is, letter by letter. Here how versions
  are passed on and shuffled.
- mitosis-mixer (same group): mitosis makes two identical cells. Here meiosis makes four different sex cells; the
  meiosis view says so.
- carnival-odds, game-show-strategist and medical-test-paradox (math): probability as the subject. Here probability
  is the tool and the subject is inheritance; the chance model is meiosis itself.
- sample-machine (math): sampling variation in general. Here the sample is a brood of offspring and the test is
  chi-square against a genetic prediction.

## Who and how
Grade 9, science (Life Science module Genetics and Inheritance: "Mendelian genetics and meiosis"). Driver: students
on laptops; the teacher can project the 1,000-offspring run. 20 to 40 minutes. Standards: HS-LS3-2 (new genetic
combinations through meiosis, plus errors and mutations: independent assortment and crossing over here, with
mutation pointed to protein-factory), HS-LS3-3 (statistics and probability to explain the variation and
distribution of expressed traits in a population).
Topic line: inheritance, meiosis and probability.
9-12 dark theme. Header: title, `.seg` modes **Cross**, **Mendel's data**, **Linked genes**, kit buttons `motion`,
`sound`, `read`.

## Screens and modes
**Cross** (opens first). Pea skin. Panel: **Genes** `.seg` **One gene** / **Two genes**; **Trait** pickers (seed
shape R/r round or wrinkled, seed color Y/y yellow or green; with Two genes both); **Parent 1** and **Parent 2**
genotype pickers (for each gene: RR, Rr, rr), each parent drawn as a pea in code with its genotype under it.
Stage left: the **Punnett square** (2 by 2 for one gene, 4 by 4 for two), gamete headers on top and left, each
box showing the genotype and a small pea, plus the prediction summary ("3 round : 1 wrinkled", "9 : 3 : 3 : 1").
**Open the square** (button, or click any gamete header): the meiosis view slides in for that parent: one cell
with its chromosome pairs (one pair per gene, genes on different chromosomes), copying, pairing, line-up (for two
genes the two pairs can line up two ways: shown side by side), first split, second split, four sex cells, with each
sex cell linking back to the header it explains. Stage right: **Breed** buttons **1**, **10**, **100**, **1,000**
(adds that many offspring), **Clear**, a tally table (phenotype, count, fraction, predicted), a peas grid (up to 100
drawn, then counts only) and a **Converge** chart (graphing.js): fraction with the dominant look against number bred
(log x axis), with the predicted line. **Seed** field (default 1) so a class can share runs. After 10 or more
offspring, a **Test the fit** card computes chi-square (see Content).

**Mendel's data**. A table of Mendel's seven F2 traits (real counts), each row with ratio and chi-square, and a bar
pair per row (observed, expected). Click a row to see the cross that made it (Yy x Yy and so on) in a small square.
A second card: the two-gene F2 (round yellow 315, wrinkled yellow 101, round green 108, wrinkled green 32) against
9:3:3:1. Prompts: "Are Mendel's ratios exactly 3 to 1? Are they close enough?" / "Simulate a cross with the same
total in Cross. How far from 3 to 1 do your runs land?" (a **Try this total** button sets Cross to Yy x Yy and breeds
the row's total).

**Linked genes**. Fly skin (fruit flies drawn in code: gray or black body, normal or vestigial wings). A testcross:
a female heterozygous for both genes (gray body and normal wings from one parent, black and vestigial from the
other) with a black vestigial male. The 4 by 4 square, assuming the genes assort independently, predicts 1:1:1:1.
**Show real data**: Morgan-style counts 965 : 944 : 206 : 185, far from 1:1:1:1 (chi-square 1002.6). **Chromosome
view**: both genes on one chromosome; the meiosis view shows the female's two chromosomes, and a **Crossing over**
slider (0 to 50 map units, default 17) sets how often a crossover falls between the genes. Breed buttons as in
Cross. The prediction updates: parental types (50 - d/2) percent each, recombinants d/2 percent each. Readout
"recombinants 391 of 2,300 = 17 percent: the genes are about 17 map units apart". At 50 the result matches 1:1:1:1;
at 0 only the parent types appear.

## Content
Mendel's F2 counts (dominant : recessive, total, ratio, chi-square against 3:1, all df 1):
| Trait | Dominant | Recessive | Total | Ratio | Chi-square |
|---|---|---|---|---|---|
| Seed shape (round, wrinkled) | 5,474 | 1,850 | 7,324 | 2.96 | 0.26 |
| Seed color (yellow, green) | 6,022 | 2,001 | 8,023 | 3.01 | 0.01 |
| Flower color (violet, white; scored on seed coat) | 705 | 224 | 929 | 3.15 | 0.39 |
| Pod shape (inflated, constricted) | 882 | 299 | 1,181 | 2.95 | 0.06 |
| Pod color (green, yellow) | 428 | 152 | 580 | 2.82 | 0.45 |
| Flower position (along stem, at tip) | 651 | 207 | 858 | 3.14 | 0.35 |
| Stem length (long, short) | 787 | 277 | 1,064 | 2.84 | 0.61 |
Two genes: 315 : 108 : 101 : 32 (total 556) against 312.75 : 104.25 : 104.25 : 34.75: chi-square 0.470, df 3.
Fly testcross: 965 gray normal, 944 black vestigial, 206 gray vestigial, 185 black normal (total 2,300);
recombinants 391 / 2,300 = 0.17; chi-square against 1:1:1:1 = 1002.6, df 3.
Critical values (5 percent): df 1, 3.84; df 3, 7.81. Plain words on the card: under the critical value, "A
difference this size happens by chance often (more than 1 time in 20). The data fit the prediction." Over it, "A
difference this size would be rare by chance alone (less than 1 time in 20). Something other than chance, or a
different rule, is at work."
Breeding: each offspring gets one random gamete from each parent, gametes drawn by the meiosis model (probability.js
`Rand(seed)`): unlinked genes independent; linked genes recombine with probability d/100 (d up to 50).
Expected spread (computed): for Rr x Rr after 1,000 offspring the dominant share has standard deviation
sqrt(0.75 x 0.25 / 1,000) = 0.0137, so nearly every run lands between 0.70 and 0.80.
Hints: Cross "<b>Cross.</b> Pick the parents, then open the square to see where each row comes from. Breed 1,000 and
watch the ratio settle." / Mendel "<b>Mendel's data.</b> Click a row. Is it exactly 3 to 1? Is it close enough?" /
Linked "<b>Linked genes.</b> Show the real data, then open the chromosome view and set the crossing over."
Tips: "Each box in the square is a chance, not a promise: one in four, every time." / "Big samples land close to
the prediction; small ones wander." / "Genes on different chromosomes sort independently. Genes close together on
one chromosome tend to travel together." / "Crossing over swaps pieces between partner chromosomes."
Model limits line: "Real traits often depend on many genes and on the environment. Real crossing over can happen
more than once between distant genes; this model counts one."

## Interactions in detail
- Genotype pickers are `.seg` groups; changing a parent clears the brood (with "Brood cleared: new parents" in the
  status line).
- Breed adds offspring to the brood (cumulative) up to 10,000; peas grid draws the first 100; tallies count all.
  Breed 1,000 animates the tally over 1 s (instant with Motion off).
- Opening the square: Esc or **Close** returns; each meiosis step has Back and Next and can autoplay (3 s per step,
  off with Motion off).
- Test the fit appears only with 10 or more offspring and every expected count at least 5 (otherwise "Breed more
  for a fair test: every expected count should be 5 or more").
- Linked genes: the slider changes the prediction at once and clears the brood.
- Every square cell, header and button is focusable; square cells read "Rr, round, 1 in 2".
- Mode change: `V.hush()`; each mode keeps its brood.

## Look
Accent `--brand #a3ffaf` (garden pea green), `--brand-ink #10161f`. Stage `#10161a`. Peas drawn yellow
`#ffd84d` or green `#7fcf5a`, round or wrinkled outline (shape is always the second cue); flies gray `#a9b0b8` or
black `#2a2d31` with a light outline `#cfd6dd`, wings full or crumpled. Chromosomes: from parent 1 `#7cb8ff`,
parent 2 `#ff9db0`, each with a letter label.
Contrast (computed): brand on --panel 14.41:1, on --sec-bg 13.65:1; brand-ink on brand 15.11:1. Nearest 9-12
accent #7ddc72 (dE 19); in this group tree-of-life's #b8ead3 (dE 33).

## Art
none: drawn in code (peas, flies, chromosomes, square, charts).

## Voice
Bank `friendly-dad` (a patient parent who gardens and likes odds): warm, plain, a little wry. Uses `Curio.voice`,
scope = mode.
- welcomeCross (how): "Welcome to Punnett Predictor. Pick the parents, then open the square to see where each row
  comes from."
- welcomeMendel (how): "Mendel's data. Click a row and see how close he got to three to one."
- welcomeLinked (how): "Linked genes. Show the real data, then open the chromosome view."
- openSquare (how, first open): "Each row and column is one sex cell. Step through meiosis to see how it was made."
- settle (event, first time a brood reaches 1,000; stale on Clear): "A thousand peas. See how close the ratio sits to
  the prediction now."
- fitYes (event, each fit test under the critical value; stale on the next breed): "Close enough. Chance alone
  explains a gap this size."
- fitNo (event, each fit test over it; stale on the next breed): "That gap is too big for chance alone. Something
  else is going on."
- crossing (how, first slider move): "More crossing over, more of the rare combinations."

## Family engine
**genetics** family. This spec describes the shared engine in full for the unspecced sibling gene-pool (grade 8)
and for protein-factory (this group).
`kit/genetics.js` (depends on `kit/probability.js` from medical-test-paradox: `Rand`, `Frac`, `Tally`,
`Converge`):
- `Code`: the standard codon table; `transcribe(dna)`, `translate(rna, {frame})`, `mutate(dna, {change | insert |
  delete})`, `classify(before, after)` into silent, missense, nonsense, frameshift, in-frame deletion or insertion.
- `Strand(el, seq)` and `Chain(el, protein)`: two-strand DNA and mRNA view with codon brackets and focusable bases;
  amino acid beads by property with shapes, and a compare strip.
- `Gene({id, name, alleles, dominance, chromosome, cM})`: alleles with symbols and trait words; dominance is
  `complete`, `incomplete` or `co`; `chromosome` and `cM` place it for linkage.
- `Genotype(genes, pairs)`: phased pairs (which allele sits on which partner chromosome).
- `gametes(genotype)`: exact gamete probabilities from meiosis (independent assortment between chromosomes,
  recombination d/100 between linked genes, capped at 0.5); `gamete(genotype, rand)` draws one.
- `cross(p1, p2)`: exact offspring distribution as `Frac`s; `breed(p1, p2, n, rand)`: a `Tally` of n offspring;
  `phenotype(genotype)`.
- `chiSquare(observed, expected)`: statistic, df, 5 percent critical value (table for df 1 to 5) and the plain
  verdict words above.
- `Punnett(el, p1, p2)`: the square with focusable cells and gamete headers that open the meiosis view.
- `Meiosis(el, genotype, {crossover})`: the step-through animation (copy, pair, cross over, first split, second
  split, four cells).
- `Skins`: `pea` (Mendel's seven traits), `fly` (body color, wing shape, eye color), `creature` (made-up animals for
  gene-pool: color, horns, tail, size), each drawing a phenotype in code.
What each tool feeds: punnett-predictor feeds the pea and fly skins, Punnett, Meiosis, breed with Converge and
chiSquare. protein-factory feeds Code, Strand and Chain. gene-pool feeds the creature skin, `mutate` at the allele
level (a small chance per gamete that an allele changes), sexual versus asexual reproduction (asexual copies the
parent's genotype), breeding pairs chosen by the student, and selection over generations (artificial selection by
picking parents).

## Sources
- Mendel's F2 counts: Mendel, G. (1866), "Versuche über Pflanzen-Hybriden", English translation by Druery and
  Bateson (1901), "Experiments in Plant Hybridization", MendelWeb, http://www.mendelweb.org/Mendel.html (checked
  2026-10-27). Chi-square values computed in Python (Curio Class, 2026-10-27).
- Fruit fly body color and wing testcross counts 965, 944, 206, 185 and 17 percent recombination: Urry et al.,
  Campbell Biology, 12th ed. (2020), Concept 15.3 (verify checks the four counts against the edition in hand).
- Meiosis, independent assortment, crossing over, linkage and map units: OpenStax Biology 2e, chapters 11 and 13
  (CC BY 4.0), https://openstax.org/books/biology-2e/pages/13-2-chromosomal-basis-of-inherited-disorders and
  https://openstax.org/books/biology-2e/pages/11-1-the-process-of-meiosis
- Chi-square critical values (0.05: df 1 3.84, df 3 7.81): NIST/SEMATECH e-Handbook of Statistical Methods,
  section 1.3.6.7.4, https://www.itl.nist.gov/div898/handbook/eda/section3/eda3674.htm
- Mendel's laws and Punnett squares: OpenStax Biology 2e, chapter 12, https://openstax.org/books/biology-2e/pages/12-introduction

## Done when
1. Rr x Rr shows a 2 by 2 square and predicts 3 : 1; RrYy x RrYy shows 4 by 4 and predicts 9 : 3 : 3 : 1.
2. Open the square shows four sex cells per parent, and each links back to its header.
3. Seed 1, Rr x Rr, Breed 1,000: the dominant share lands between 0.70 and 0.80; the Converge chart narrows toward
   0.75.
4. Mendel's data shows the seven rows with chi-square 0.26, 0.01, 0.39, 0.06, 0.45, 0.35, 0.61, all "fit"; the
   two-gene card shows 0.470.
5. Linked genes: Show real data gives chi-square 1002.6 ("too big for chance"); slider 17 predicts about 41.5 :
   41.5 : 8.5 : 8.5 percent; slider 50 predicts 25 percent each.
6. Test the fit refuses broods whose expected counts are under 5, with the reason.
7. Everything works by keyboard; main controls visible at 1366x768 and 680x425; the 4 by 4 square fits at 375 wide.
8. Each how-to line speaks once in five repeated actions; the fit lines speak each test.
9. No images, no network, no em dashes.

## Open questions
- [punnett-predictor] HS-LS3-2 also names errors in replication and mutations. This tool covers meiosis only and
  points to protein-factory for mutations. Enough, or add a nondisjunction step to the meiosis view?
- [punnett-predictor] The fly counts come from Campbell 12th ed. (Morgan-style data). If verify cannot check them in
  that edition, should the tool use Morgan's original 1911-1912 counts instead?
