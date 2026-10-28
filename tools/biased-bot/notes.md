## A 5-minute start

1. Read the opening story. Predict how many right lunches each room will get, then press **Run the lunch line**. A full run takes about 27 seconds; **Skip to results** finishes immediately.
2. Compare the three room bars. Room 12 and Room 3 get 10 right lunches. Room 9 gets 6. Its four students who wrote a flagged 1 receive tacos instead of pasta.
3. Tap the **Room 9 jar**. Compare its 1 with Room 12's 1. All rooms are fictional. The handwriting style is a difference, not a mistake by the writer.
4. Raise Room 12 to 30 cards, press **Train Bitsy**, and run again. Does Room 9 improve? Then return Room 12 to 15 and add Room 9 cards: try 3, then 6, retraining and running each time.
5. Ask students to explain the change using the bars and the jar cards, then try their own writing.

## The two modes

- **Lunch Line:** Fewer and More change a jar by three cards, one each of 1, 4 and 7. Jar changes need Train Bitsy before a new run. Tap a jar to inspect its actual training examples, grouped by digit. The same 30 lunch cards are tested every run. Stop keeps partial results labeled stopped. Old results remain labeled after a training change.
- **Try Your Writing:** draw a 1, 4 or 7. Bitsy compares the drawing's normalized 8 by 8 grid of ink with the training cards and uses the labels of the three nearest examples. Read shows the guess and those examples. Teach with the number you intended. A single added example may not change a three-neighbor vote; try another example, then read again. Wrong labels can teach Bitsy wrong.

## Talk about it

- What changed between your prediction and the results? Who received the wrong food, and what would that feel like?
- Did adding Room 12 cards fix Room 9? Did adding Room 3 cards? What evidence distinguishes the number of examples from whose examples they are?
- Room 3 writes big, wobbly numbers, yet its score starts at 10. Why is "messy writing" an incomplete explanation?
- Why is one example of each Room 9 digit insufficient here, while two of each work? Look at the three look-alikes in the writing mode.
- After all rooms reach 10, train only on Room 9. Whose lunch is wrong now? How could students from every room help improve the next version?
- A perfect score on these cards measures only these fictional test examples. What other handwriting might you ask for before using a robot throughout a school?

## Good to know

The rows below are computed with the shared Curio Class ml-lab engine, the exact seeds and stroke rules in the spec. Scores are right lunches out of 10, in Room 12, Room 3, Room 9 order.

| Jar cards: Room 12 / Room 9 / Room 3 | Room 12 | Room 3 | Room 9 |
|---|---|---|---|
| 15 / 0 / 0 | 10 | 10 | 6 |
| 30 / 0 / 0 | 10 | 10 | 6 |
| 15 / 0 / 30 | 10 | 10 | 6 |
| 15 / 3 / 0 | 10 | 10 | 6 |
| 15 / 6 / 0 | 10 | 10 | 10 |
| 15 / 15 / 15 | 10 | 10 | 10 |
| 0 / 15 / 0 | 6 | 6 | 10 |
| 3 / 0 / 0 | 10 | 10 | 5 |

- For the first four rows, Room 9's four 1s are read as 4. With only Room 9 training, four 1s in each other room are read as 7. In the final row, Room 9 loses two 1s to 4 and three 4s to 1.
- Bitsy receives only 64 ink values. Room badges identify the source for students; they are never classifier features. Ink is centered and scaled, so location or overall writing size is not a separate clue.
- These fixed, labeled examples form a nearest-neighbor classifier, not a generative chatbot. The particular need for two examples of each style is specific to this dataset and the three-neighbor vote.
- Nothing is collected or sent. The drawing and My cards exist only in memory on the current device and disappear when the page closes. Start over empties My cards too. Only the kit's shared Motion preference can persist.
- Keyboard: Tab reaches modes, header, panel controls, then the drawing pad. Enter or Space activates buttons. On the pad, arrows move a pen and Space lowers or lifts it. A seventh stroke clears the six previous strokes first. Escape closes the card viewer and returns focus to its jar.
- Motion off removes the sliding and gear movement. Training still takes 0.6 seconds and lunch cards still finish at 0.9 seconds each.
- Compact previews keep the main controls visible and let the results panel scroll. The queue shows ten cards at a time and advances to the next ten during a run. On phones, controls precede the scene; the writing scene contains the full-sized pad and ink grid.

## Standards and student actions

- **E4-ALG-ML-02:** change the sources of training examples, retrain, and compare the same lunch tests. Explain why more examples of an already represented style did not solve a missing-style problem.
- **E4-SOC-HU-18:** identify whose lunch is wrong from disaggregated results, inspect that room's examples, and improve the model by including its handwriting. Training on Room 9 alone lets a solo student see harm move to others.
- **E4-DAT-IM-11:** compare outcomes by data source, test whether the examples represent the users, and connect missing data with the effect on those users. The drawing mode lets students contribute their own perspective while keeping it private.
- **E3-ALG-ML-02:** label a personal drawing, retrain, and see the changed nearest examples and later guesses. Experience learning from examples rather than writing a digit-recognition rule.
- CSTA 2017 crosswalk: **1B-DA-07**, propose cause and effect and predict results using data; **1B-IC-19**, improve technology for diverse user needs; **1B-IC-20**, seek diverse perspectives to improve computational artifacts. AI4K12 Big Ideas 3 and 5.

## Sensitive context and sources

The fictional room activity addresses unfair outcomes and whose data is included. Do not treat a handwriting difference as a deficit or ask a child to represent an entire real group. The on-screen activity and narration name no real place or population.

For teacher background only: Buolamwini and Gebru's **Gender Shades** (2018) examined commercial gender classification systems and found the highest error rates for darker-skinned women. The parallel is to assess performance across groups rather than relying only on an overall average. This is sensitive context about skin tone and gender, and the tested task was binary gender classification, not a test of every form of face recognition. The paper is not introduced in the student scene or narration.

- [Regional handwriting variation, Arabic numerals](https://en.wikipedia.org/wiki/Regional_handwriting_variation), the spec's source for numeral-style variation.
- [AI4K12](https://ai4k12.org), Big Idea 3, Learning, and Big Idea 5, Societal Impact.
- Buolamwini and Gebru, *Gender Shades: Intersectional Accuracy Disparities in Commercial Gender Classification*, Proceedings of Machine Learning Research 81, 2018. Teacher background only, as specified.
- [CSTA K-12 Computer Science Standards](https://csteachers.org/k12standards/), 2017 crosswalk named above.
- Rooms, cards and numerical results are made up for this tool. Results are computed rather than claims about real students or schools.
