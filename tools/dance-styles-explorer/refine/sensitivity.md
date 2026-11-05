# Sensitivity review: dance-styles-explorer
PASS for cultural context, cast representation and the scoped repaired pose frames. See model limitations below.

## Scope
Fresh review of `data.json`, cultural context in `notes.md`, named phrase definitions in `src.html`, and the supplied spec. Did not read builder reports. No browser or physical-technique certification.

## Findings
- **Should fix, general, Irish style file:** "the Irish Dancing Commission set rules from 1930" conflicts with the Commission's own history: committee discussions in 1930, approval of Rules and Regulations in 1931, activity from 1932. The text repeats the spec. Suggested narrow correction: "the Irish Dancing Commission developed competition rules in the early 1930s." Leave the spec unchanged and record its conflict.
- **Should fix, family:dance, named movement rendering:** a generic capsule hand cannot demonstrate the difference between pataka and alapadma. The painted replacement needs distinct visible hand shapes, with grounded araimandi and ankle bells; labels alone do not teach these terms. This was already explicitly acknowledged in the notes. Parent is replacing the artwork.

## Respect and context
The files credit African American social dance in jazz and tap, Bronx hip hop and its practitioners in breaking, Gitano (Roma) communities in flamenco, and hereditary women dancers in Bharatanatyam before later institutional reshaping. They avoid presenting the 1930s as the invention of Bharatanatyam. No derogatory language, caricature, exoticizing comparison or ranking of traditions found.

These short phrases can support analysis, not expertise in performing a tradition. Retain the model-specific disclaimer and distinguish analysis conventions from claims about every dancer. A diverse cast should span the Western styles as well as the other traditions. Clothing and skin tone must not imply who is permitted to participate. Varied builds should remain anatomically credible in the moves shown.

## Phrase checks for the final artwork
Ballet first position has heels together and turnout; second-position wide feet must not be labeled first. Releve is rising; tendu keeps the pointed working toe in contact with the floor; arabesque extends a leg behind. Modern contraction and release must change torso shape. Jazz isolations keep the rest quieter; tap and Irish models must distinguish busy feet from quieter upper bodies. Breaking baby freeze requires supported low floor contact rather than an unsupported floating shape. Flamenco braceo and floreo must visibly differ from a generic raised arm. Bharatanatyam pataka has four straight fingers held together with the thumb bent, while alapadma opens and spreads the fingers like a lotus. Cast review will check visible cues, not certify a full dance technique.

## Sources checked
- [Martha Graham Dance Company history](https://marthagraham.org/history/): company founded 1926; contraction and release.
- [Ailey Revelations source sheet](https://pressroom.alvinailey.org/internal_redirect/cms.ipressroom.com.s3.amazonaws.com/292/files/20179/Revelations%20Info%20Sheet_FINAL.pdf): premiere 1960.
- [Library of Congress tap history](https://www.loc.gov/collections/songs-of-america/articles-and-essays/musical-styles/parlor-and-concert-stage/tap-dance/): African American and Irish interaction and William Henry Lane.
- [UNESCO Flamenco](https://ich.unesco.org/en/RL/flamenco-00363): 2010 inscription; cante, baile, toque; essential Gitano role.
- [Kalakshetra history](https://www.kalakshetra.in/college/history/): 6 January 1936 founding.
- [Riverdance original performance](https://riverdance.com/blog/2019/04/30/the-1994-eurovision-performance/): Eurovision 1994; Flatley and Butler.
- [CLRG history](https://www.clrg.ie/history-of-clrg/): 1930 discussions, 1931 rules, 1932 first activity.
- [CCRT Bharatanatyam publication](https://ccrtindia.gov.in/wp-content/uploads/2020/09/Pub_Dance_Bharatnatyam.pdf): pataka and alapadma in the tradition; hastas and expression.

## Painted set checked
Viewed `_scratch/dance-styles-explorer/painted-cast-contact.png` and final rendering frames `fixed-plie`, `fixed-fifth`, `fixed-freeze`, `fixed-pataka`, `fixed-lotus`, `fixed-irish`, and `fixed-trace` in `review-frames/`. The cast naturally varies skin tones, builds, apparent ages and presentation. Western traditions also have diverse performers. Rehearsal clothes avoid national-costume caricature. The supported freeze and distinct mudra hand paintings address the primary named-pose risks. There is no claim that a performer must have a given ethnicity to dance a tradition.

The Irish date has been corrected to "early 1930s" in data.json and is visible in `fixed-irish.png`.

## Rendered-pose corrections confirmed
- **Fixed blocker, family:dance, painted rig projection:** the original `fixed-irish.png` sliver head and `fixed-trace.png` flattened head/arm breakup are corrected in `repair-irish.png`, `repair-bow.png` and `repair-trace.png`. Heads remain intact, necks attach, and the painted body remains recognizable. Parent preserved head aspect and a minimum torso projection. These remain stylized articulated models, not expert technique footage.
- **Fixed should fix, general, mudra atlas crop:** floating colored strips above the wrists in `fixed-lotus.png` are absent from `repair-lotus.png`. The hand detail remains distinct and legible.
- **Polish, family:dance, plié crop:** `fixed-plie.png` has crossed-looking ankle/shin joints above the shoes. The first-position heels are now close, but smoother crop joins would improve the anatomy.

Scoped re-check also viewed `repair-compare.png`: the two painted performers, their trace markings, and badge shapes remain readable. No remaining cultural blocker or should-fix was found in the supplied cast or repaired frames. Model limitations remain: the front-view paintings are articulated and foreshortened rather than newly painted for every facing, hands are enlarged in a detail inset, and these phrases support observation rather than physical technique instruction. Retain the explicit educational-model language and do not imply a full authoritative performance. The plié seam item above is optional polish, not a cultural gate.
