# Answer-key read: english-language-arts-grade-4 unit 4, days 120 to 156

Date: 2026-11-27. Brief: docs/pipeline/briefs/sensitivity-read.md sections 1 and 2, kind answer-key. Packet: build/sections/packets/english-language-arts-grade-4-u04.md.

I solved every item cold from the packet before I opened any plan, key or prep note. I read the texts first, and I opened a shared piece, text or day block only for an item that needed it. I then compared my answers with the keys, checked rule 4 against the ledger, traced each fact to a sources.csv row and synced field 3 to items.csv.

## Items read

142 packet items (exits and end items). The file holds 160 s04 rows and 174 s04 wrongs rows, with 44 handback rows naming s04 items. No item was split, added or removed, so these counts are unchanged.

## Faults

| Item | Kind | What was wrong | Fix | Stage |
|---|---|---|---|---|
| s04-X125-pronoun | ambiguous | The exit prints the reserved ending, and the ending already holds a relative-pronoun sentence about Maya. A child could copy it and be marked right. | Stem: "Write a new sentence about Maya using a relative pronoun." Key: "Maya, who checks each name, slows down at her desk." Steps add "A sentence copied from the ending is not yet." Sample wrong and u04-2 Ask, Key and print row match. | section plan |
| s04-X125-adverb | ambiguous | Same fault: the ending prints "At the desk where her notes lay," ready to copy. | Stem: "Write a new sentence about the desk using a relative adverb." Key: "Maya slows down at the desk where she checks each name." u04-2 matches. | section plan |
| s04-X131-adverb | ambiguous | The installment prints "the shelf where she had found the envelope," ready to copy. | Stem: "Write a new sentence about the shelf using a relative adverb." Key: "Maya checks the label on the shelf where the envelope was. Accept another new sentence with a relative adverb that fits." u04-3 matches. | section plan |
| s04-D3-whose | key | The key, "Maya, whose notes her brother reads, owns the notes," restates the joined fact as its own main clause, so it says nothing. | Key: "Maya is the one whose notes her brother reads." The wrongs row now uses the same frame with "whom." The u04-4 D3 cold solution matches. s04.md line 346 still prints the old key (refine plan point). | unit plan |
| s04-C1-support | needs-info | The key relied on 36 being three-fourths of the states. The account never gives the number of states, so the child cannot do that step. | The key no longer needs the number: it says three-fourths had to agree, Tennessee supplied the thirty-sixth ratification, and certification on August 26 shows the requirement was met. Steps and samples match. The item stays held for text-owner replacement. | unit plan |
| s04-X149-support | ambiguous | The card gives two facts that support sharing the display, and the key credited only one. | Key adds "Also accept that it labels the garden report, so visitors can check the source." Steps, samples and the u04-6 Key line match. | section plan |
| s04-P134-spell-1, s04-P134-parts-1 | rule4 | "reconstruct" is not cold: the unit 3 P119 probe used "reconstruction", and unit 3 texts print "reconstructed". | Word changed to "abrupt" (meaning stated in the stem), key "ab + rupt." Wrongs rows: abrubt (X), abr + upt (R). The u04-3 probe table matches. | section plan |
| s04-P135-spell-2, s04-P135-parts-2 | rule4 | "retractable" is not cold: the unit 2 u02-1 word probe used "retraction". | Word changed to "adjustable" (meaning stated in the stem), key "adjust + able." Wrongs rows: adjustabel (X), adjus + table (R). The u04-3 probe table matches. | section plan |
| u04-2, u04-3, u04-4, u04-6 field 3 | field3 | After the data fixes above, the Ask lines, Keys and print override rows no longer matched items.csv. | All synced word for word. The stem-sync check now prints no differences. | data |

Left as holds, not changed by this job: C1, X127, X138, X148, X149, X150 and X154 wait for registered fixed selections from the text owners. C1 has a second issue: archive C on day 120 already teaches its procedure. Both are plan points in the refine report.

## Checks

- Rule 4: I ran `ledger.py show ela --before english-language-arts-grade-4 --term` on each idiom, simile, probe word and case word. The lower grades have no rows for "safe than sorry", "look before", "onion" or "opened the door". "eager" is in a grade 2 feelings word bank, which is a term, not a case. "fog" is a kindergarten weather word, a different use from X133's figure. I rejected telegraph, inaudible and restructure as replacement probe words because they are already used. abrupt and adjustable have no rows at grade 4 or below, and they do not appear in the unit 2 or unit 3 probes or texts. The ledger note for the 134 and 135 probes now names the new pairs.
- Facts traced to sources.csv rows (rows read, no URLs opened): the ratification count, three-fourths and August 26 to s04-src-amendment; Burn's reason and his mother's letter to s04-src-burn-statement and s04-src-burn-context; the composting site, newsletter and outreach to s04-src-youth-projects. s04-src-reading-06 holds the garden opening until day 154, and the plan keeps it closed until X155.
- No key on a child page: the probe keys and recording sheets are teacher pieces, and no shared piece prints an exit key.
- Stems: after the fixes, no stem prints its answer or a copyable sentence, each stem asks one thing, and no stem sentence is over 15 words. Spelling stems state the meaning of the word wanted.
- Cold recheck against the final files: X125-pronoun, X125-adverb, X131-adverb, D3-whose, C1-support, X149-support and the four probe items. My answers now match the keys or fall inside their accept clauses.
- Gate: `gate.py --course english-language-arts-grade-4` shows 194 failing lines, the same as the baseline, and 0 new.

## My own errors

- The packet header showed the keys of X120 to X127 before I had solved them. My answers for those items are not fully cold. I solved X125 and its parts from the text, and I found the copy fault in X125 from the text, not from the key.
- Cold misread: I thought X155's reserved paragraph 1 was opened on day 143. The plan and sources.csv do reserve it. Only the g4-u4-06 text frontmatter is stale, which is a refine plan point, not an item fault.
- At first I marked X122-pause, A4-delivery, A4-stress, A5-opposite and D2-idiom as unanswerable. The packet did not include their delivery spec or strip. I opened those pieces and could then answer each one, so they have no fault.

## Changed for the next unit

- When an exit prints its reserved passage, check that no key can be copied from that passage. Ask for a "new" sentence and mark a copied one "not yet".
- Check dictation and probe words against this course's earlier units' probes and texts as well as the lower-grade ledger.
- A relative-clause key must not restate the joined fact as its own main clause.
- A procedural key must not depend on a number the text leaves out.
- When a card gives two facts that answer the stem, accept both.
