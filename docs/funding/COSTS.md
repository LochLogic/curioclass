# Cost sheet: finishing Curio Class

Drafted 2026-10-28 for funding asks. Prices are list prices found online on 2026-10-28 or rough ranges; check each
before quoting it to a funder. Lines marked **(Cory)** need Cory's real numbers.

## The work left

| | Count |
|---|---|
| Tool concepts in the catalog | 797 |
| Live | 76 |
| Still to build | 721 (198 already specced) |
| Also planned | Reading Room (about 700 public domain stories), Supply Closet (diagrams, charts per module, module kit, the Map), Spanish review, ASL collection |

## Why the AI bill is bigger than "tokens per tool"

The measured pipeline cost is about 0.7M to 1M tokens a tool (build, three Refine lenses, polish, exit checks, lesson
plan). For 721 tools that is roughly 500M to 720M tokens on its own. The real total is larger, because the work that
makes the tools good sits outside any one tool:

- **Engines and the kit:** each tool family (number line, data desk, robot, stage, music studio...) gets a shared
  engine built once and tuned across its siblings.
- **Study and iteration:** catalog audits, overlap passes, standards gap checks, pilots (the Codex builder pilot),
  tuning the audit tools, wave post-mortems that change the briefs.
- **Second rounds:** about 1 in 3 tools needs a second Refine round.
- **The rest of the site:** Supply Closet, Reading Room enrichment and verification, art prompts, voice scripts.

A fair planning figure is **1 to 1.5 billion tokens over the next year**. Bought as pay-as-you-go API calls this would
cost many times more than subscriptions, so subscriptions at the top tier are the cheap way to do it, and the top
tier is what lets the work run without hitting usage limits mid-wave.

## Year-one budget

| Line | What it buys | Estimate |
|---|---|---|
| **AI compute** | | |
| Claude Max 20x | the main builder and integrator, uninterrupted | $200/mo x 12 = $2,400 |
| ChatGPT Pro | the Codex builder (second, parallel builder) and gpt-image art | $200/mo x 12 = $2,400 |
| Overflow credits | API and image credits for rush waves and art redos | $1,200 |
| *Subtotal* | | *$6,000* |
| **Hardware** | | |
| Memory upgrade | 32 GB to 96-128 GB, so local FLUX art, voice and builds can run together | $400 to $900 |
| GPU for the voice and art worker | a 24 to 32 GB card, so voice and art run at full speed alongside builds | $1,800 to $3,000 |
| Storage | 4 TB working drive plus a 4 TB backup drive (art, voice, and story assets grow fast) | $500 to $800 |
| *Subtotal* | | *$2,700 to $4,700* |
| **People and testing** | | |
| Spanish native-speaker review | every Word Wall card, chart and game card is in Spanish | $1,500 to $3,000 |
| Teacher pilots | thank-you stipends for about 10 classroom teachers who run tools and report back | $1,000 |
| Print testing | paper, ink, and poster prints to test every print format on real printers | $300 |
| *Subtotal* | | *$2,800 to $4,300* |
| **Outreach** | | |
| Teacher conferences and handouts | state teacher conference registrations, printed one-pagers and cards | $1,500 |
| **Running costs** | | |
| Domain, email, hosting | hosting is free on Cloudflare | about $100 |
| Fiscal sponsor fee | if a grant goes through a sponsor, 7 to 10 percent | on top |
| **Direct total** | | **about $13,000 to $16,600**, plus any sponsor fee |

## Cory's time (in-kind)

About 15 hours a week (10 to 20) for review, direction and outreach: about 750 hours a year. Valued at $60 an hour
that is **$45,000 of in-kind work**, a strong match to show any funder. An optional stipend line can sit on top: for
example $15,000 buys back 250 of those hours so the work goes faster.

## Ask levels

| Ask | What it does |
|---|---|
| $5,000 | A full year of uninterrupted AI compute (Claude and Codex at the top tier) |
| $10,000 | Compute plus the hardware: the catalog gets finished on the fastest path |
| $16,000 | The whole year-one budget: compute, hardware, Spanish review, teacher pilots, outreach |
| $30,000 | The above plus a stipend for Cory's time |

## Today's actual costs (Cory)

| Line | Per month |
|---|---|
| Claude plan | (Cory) |
| ChatGPT plan | (Cory) |
| Other AI (Gemini, credits) | (Cory) |
| Domain and email | (Cory) |
| Power for overnight GPU runs | (Cory) |

## Sources for prices

- Claude Max ($100 and $200 tiers) and ChatGPT Pro ($200): third-party pricing guides found 2026-10-28, for example
  https://dupple.com/learn/claude-pro-vs-max and https://www.morphllm.com/chatgpt-vs-claude. Confirm on the vendors'
  own pricing pages.
- Fiscal sponsor fees: HCB help center (7 percent, teen-led only, so not for us), Open Source Collective docs
  (10 percent), general 5 to 15 percent range from sponsor guides.
- Hardware: ranges only; RAM and GPU prices move fast, so price them on the day.
