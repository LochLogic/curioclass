## What it teaches

Students read a confusion matrix and trace predictions to a nearest-neighbor model's training examples. They test how class imbalance, missing night data and incorrect labels change which animals are misclassified.

## Key skills

- Read a row as the real animal and a column as the model's prediction.
- Compare overall accuracy with day, night and individual animal results.
- Use nearby training examples as evidence for a diagnosis.
- Change training counts, labels, neighbors or clues and test the same held-out photos again.
- Explain why a repair helps one group and may hurt another.

## Support at home

- Sort familiar objects into groups. Ask how a group with only one example might be harder to recognize.
- Describe an object in dim light and daylight. Talk about which clues still work.
- Give one item a wrong label, then compare a decision based on one example with a vote from five.

## Five-minute start

Open Garage. Read the three scores, then tap the Raccoon row, Fox column. Inspect the test photo and its nearest training examples. Change k from 5 to 1 and run the fixed test again. Compare the new matrix with the original 39 of 40.

## Modes

Garage is free exploration with 160 balanced training photos. Students can break and repair the model without a win condition.

Work Orders gives three ranger complaints. Each repair must meet both live goals. A completed order reveals its explanation and enables the next order. Edits remain when switching to Garage and back. Reset restores the current order, not the whole sequence. Nothing is saved on reload.

## Talk questions

- Where did the eight missing fox predictions go?
- Why can a model look strong overall and fail at night?
- What evidence distinguishes a mislabeled example from too few examples?
- Does adding more data always help? What kind of data matters?
- Why does changing k help with wrong labels but not with completely missing night examples?

## Good to know

The species and camera-trap context follow the sources in spec.md. Infrared night images are monochrome, but the exact Mask reduction is a teaching assumption, not a claim that all real raccoon masks disappear. Cedar Hollow and all numerical features are made up. This is a four-feature nearest-neighbor model, not a real image recognition system. The paintings change size, but Legs, Tail and Mask values appear as bars rather than altering the paintings.

Rows are truth and columns are predictions. Tabs filter existing results without retraining; goals always use the specified full set or night subset. Counts of two and one in the first work order rise to seven and six with the first +5 steps. At zero or forty the controls clamp. With no clues the model has no useful distance information and votes by its stable training order.

Possible repairs: WO1 add five day and five night fox photos (40/40), use k=1 (39/40), or reduce raccoons to 5/5 (39/40). WO2 add ten night examples of each type (37/40, Night 22/25), or remove Mask (36/40, Night 22/25). WO3 use k=5 (39/40), or repair the eight incorrect deer labels (37/40). The inspector reveals nearest training photos, including correctly painted deer with an Empty label.

To inspect all eight incorrect labels, temporarily use only Size with k=9. Open the relevant matrix squares and inspect their training matches. After repairing the labels, restore all four clues and k=1 before comparing with the 37/40 reference result. The full eight-label path was checked through the tool's UI handlers.

Garage returns to its working starting model when you leave it. Work Orders retain their current edits across Garage visits. On a phone, Run and the work-order advance button stay in the header; scroll for the work order card, training controls and evidence. Short landscape previews keep the hint and Run visible while their toolbox scrolls.

At zero training photos the model has no answer. Its matrix adds a No answer column and an unused zero row because the shared engine draws square matrices. Adding training photos restores the four-class matrix. If other animals are manually relabeled as a class, that label can still be predicted even when that animal's two training steppers are zero.

The training pool is seeded 601, the forty test items 602. Features use Euclidean distance, stable tie ordering and majority votes. All seventeen reference results were recomputed with kit/ml-lab.js before building.

Standards: MS-ALG-ML-06, MS-ALG-ML-07, MS-ALG-ML-08, MS-DAT-IM-29. Students refine a model with generated evidence and compare errors by class and time. CSTA crosswalk: 2-DA-08, 2-DA-09, 2-IC-21. The night work order makes unequal impact visible through students' own repairs.

The 2-IC-21 crosswalk covers the bias part here. Its accessibility-design discussion is not a student activity in this tool, so this is not full coverage of that entire CSTA standard.

Sound and Read use browser speech because recording is outside this build. Motion off removes animation without changing the data. Letters and wrong-answer X marks supplement colors. All data stay in memory; no network requests and no saved student work.

## Review notes

The matrix labels explicitly name rows and columns. After a model edit, photos and scores describe the last test until Run the test is pressed. The finished repair note now reports errors corrected, new errors and remaining errors from that student run.

The work-order goals measure model results. Because the specification accepts trying different k values and clue sets, a student can find a numerical repair by trial and error without diagnosing it. Completion alone does not demonstrate the diagnosis standard; ask students to explain the relevant error cell and training matches. Closing that loophole in solo use needs a specification change.
