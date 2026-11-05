## What it teaches
Students use the columns of a matrix to predict where a picture moves. They compare matrix products, connect the determinant to area and orientation, and use inverses to recover positions and colors.

## Key skills
- Match the two columns to the transformed right and up arrows.
- Predict how a matrix changes area and orientation.
- Compare two transformation orders and explain when their products differ.
- Test an inverse by multiplying back to the identity.
- Solve a pixel position or color system and explain why flattening loses information.

## Support at home
- Draw a large letter F on scrap paper. Turn or flip the paper and describe what changed and what stayed the same.
- Use a tiled floor or a hand-drawn grid to describe where one step right and one step up would land after a stretch.
- Mix two imaginary color amounts by averaging them. Discuss why knowing only one average does not tell you both starting amounts.

## A 5-minute start
1. Open Studio and press Shear. Find the two arrow destinations in the matrix columns.
2. Press Stretch x2, then Reflect. Compare area and orientation.
3. Press Identity, tap a pixel, then drag an arrow. Explain why the pin follows the same matrix as every other pixel.
4. Open Order matters. Compare the default turn and shear before pressing Swap.

## The modes
- **Studio:** change four entries, their sliders, the presets, or the arrow tips. Probe a pixel and animate the entries from identity.
- **Order matters:** edit A and B, compare BA with AB, swap the cards, and optionally compare A + B.
- **Undo it:** recover an inverse for four moves, recover the origin of a moved pixel, or recover RGB through a three-channel filter. Two misses reveal Show me. A correct result retains the student's actual equation on screen. A correct Blend answer restores the original picture colors and the ringed sample.

## Talk about it
- Why does the first column describe the right arrow's destination?
- Why do Shear and Reflect both preserve the area, although their determinants differ?
- Which two transformations commute? Find a pair that does and a pair that does not.
- Why can an invertible matrix recover every pixel, while a flattened picture cannot be separated again?
- Why does the Blend filter have an inverse when the Gray filter does not?

## Good to know
- Entries accept decimals or simple fractions and clamp to -10 through 10. Studio sliders run from -3 through 3.
- Arrow tips are keyboard focusable. Arrow keys change a coordinate by 0.1; Shift changes it by 1.
- Wrong pixel-origin answers draw a cross at the attempted destination and a dashed line to the target ring.
- RGB answers use whole numbers from 0 through 255. The ringed tile is a controlled sample used in the color equation, rather than a sample taken from the painted asset.
- The fixed axes cover -6 through 6. Large transformations leave the stage and are clipped, including Move 3's pixel at (5, 11).
- Animate linearly interpolates matrix entries with an eased time parameter. It is not a constant-speed rotation. Any edit cancels it immediately.
- Work lasts only for the current session; it stays on this device. Nothing is saved. All interactions and supplied art work offline. Sound and Motion use the shared Curio Class kit; Read speaks the current hint.
- The spec's gray example (270, 0, 0) is algebraically valid but outside the RGB input range. The screen instead permutes the active sample's channels to show two valid colors giving the same active gray value.

## Standards and sources
Studio practices N-VM.C.12 and C.7. Order matters practices N-VM.C.8 and C.9, including multiplication and addition. Undo it practices N-VM.C.10 and A-REI.C.9 with two-dimensional inverses and a technology-computed three-dimensional filter inverse. AP Precalculus Unit 4 topics 4.10 through 4.14 connect the representation to transformations.

- OpenStax, Precalculus 2e, 9.5 Matrices and Matrix Operations and [9.7 Solving Systems with Inverses](https://openstax.org/books/precalculus-2e/pages/9-7-solving-systems-with-inverses).
- College Board, [AP Precalculus](https://apcentral.collegeboard.org/courses/ap-precalculus), Course and Exam Description, 2023.
- Common Core State Standards, [N-VM.C](https://www.thecorestandards.org/Math/Content/HSN/VM/) and A-REI.C.9.
- All numerical examples come from spec.md and are independently recomputed in Scratch.
