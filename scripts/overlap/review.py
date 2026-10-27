"""Sort the overlap decisions into review tiers and apply Cory's two rules to the suggested fixes (2026-10-27).

    python scripts/overlap/review.py      -> docs/agents/overlap/review.json

Tiers (how much of Cory's attention a fix needs now):
  A  decide now: wave 1 tools (specs come next), clashes with live tools, trademarks
  B  accept in bulk with a skim: clashes between planned tools in the same subject, and any clash in K-5
     (one teacher teaches every subject there)
  C  leave the concept alone; the suggested fix becomes a note for the spec agent: cross-subject clashes in 6-12,
     and changes below the clash rule's bar (title echoes, repeated settings)
  N  no change: keeps, spec notes and the add-standard call

Rule 2, topic words: a new title keeps the word teachers search for, or the tool page carries it in a topic line.
Rule 3, families: a fix keeps the tool in its family, or says outright that it leaves and why.
The rule edits live in TITLE, CONCEPT, LINE and FAMILY below; decisions.json is left as the pass wrote it.
"""
import csv, json, os, re, sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(__file__))
from common import ROOT, OUT  # noqa: E402

TRADEMARK = {'mad-libs-machine', 'food-web-jenga', 'battleship-grid', 'rube-goldberg-workshop', 'lemonade-monopoly'}

# rule 2: the pass's new title drops the word teachers type, so it comes back into the title
TITLE = {
    'bee-bot-garden': 'Robot Mouse Mail',
    'input-output-machine': 'Input or Output?',
    'compound-interest-garden': 'Compound Interest Head Start',
    'roller-coaster-physics': 'Zipline Energy',
    'elevator-hundred': 'Hundred Bead Slider',
    'text-feature-safari': 'Text Feature Makeover',
    'network-detective': 'Network Help Desk',
    'shape-courtroom': 'Shape Sieve',
    'ph-detective': 'pH Mystery Liquids',
    'chain-reaction': 'Cause and Effect Rewind',
    'story-map-treasure': 'Story Map Quilt',
    'pizza-shop-assembly-line': 'Paper Plane Assembly Line',
    'dance-floor-moves': 'Transformation Dock',
    'transformation-golf': 'Rigid Motion Twins',
    'blueprint-builder': 'Same Facts, New Structure',
    'cone-slicer': 'Conic Focus Finder',
    'ten-frame-factory': 'Ten Frame Spillover',
    'recipe-scaler': 'Recipe Scaler',   # rule 3 below keeps the original
    'pizza-party': 'Pizza Party',
}
# rules 2 and 3 change the concept itself
CONCEPT = {
    'compound-interest-garden': 'Two savers put in the same $50 a month, one from age 16 and one from 26; a stacked bar splits '
        'each year into deposits, interest and interest on interest. Change the rate or how often it compounds, then find '
        'the rule of 72. A plain savings account at a fixed rate, so no market returns (market-time-machine) and no '
        'doubling-penny sequences (savings-plan).',
    'recipe-scaler': 'Scale a family recipe up for the whole class party: multiply each fraction of a cup by the number of '
        'batches and watch the measuring cups fill. No shop to run and no customers, so it no longer sits beside '
        'grocery-run and the pizza shop.',
    'pizza-party': '',   # '' = the original concept stands
}
# rule 2: the topic line on the tool page (what teachers type), for every tool whose title changes
LINE = {
    'festival-passport': 'cultures and celebrations around the world',
    'bee-bot-garden': 'coding a path with arrow commands',
    'input-output-machine': 'computer inputs and outputs',
    'local-changemaker-planner': 'civic action and who makes the decision',
    'power-grid-tycoon': 'energy sources, cost, reliability and emissions',
    'boundaries-builder': 'healthy relationships and boundaries',
    'compound-interest-garden': 'saving and compound interest',
    'roller-coaster-physics': 'conservation of energy with friction, roller coaster physics',
    'move-like-me': 'locomotor and nonlocomotor movement',
    'two-sides-theater': 'point of view in stories',
    'elevator-hundred': 'adding tens and ones within 100',
    'text-feature-safari': 'nonfiction text features',
    'book-detectives': 'author, illustrator and main topic',
    'bundle-bakery': 'tens and ones, place value',
    'pattern-block-pond': 'composing shapes with pattern blocks',
    'shape-spy': '3D shapes and position words',
    'retell-puppets': 'retelling a story with sentence frames',
    'class-snack-vote': 'how computers collect and count data',
    'pattern-finder': 'what AI is and how it learns patterns',
    'debate-prep-desk': 'argument writing with claims and reasons',
    'town-hall-debate': 'argument, counterclaims and rebuttal',
    'fruit-sorter-ai': 'train and test a classifier',
    'fossil-dig': 'fossils and changing environments',
    'evidence-locker': 'supporting reasons with text evidence',
    'polynomial-garden': 'adding and multiplying polynomials',
    'fair-use-court': 'copyright, fair use and Creative Commons',
    'robber-baron-or-captain': 'the Gilded Age, robber barons or captains of industry',
    'pattern-detective': 'multiplication table patterns, two-step problems',
    'network-detective': 'wired and wireless networks, logging in',
    'shape-courtroom': 'classifying quadrilaterals by their properties',
    'ph-detective': 'acids, bases and pH',
    'mad-libs-machine': 'parts of speech (nouns, verbs and adjectives)',
    'food-web-jenga': 'food webs',
    'battleship-grid': 'the coordinate plane, first quadrant',
    'rube-goldberg-workshop': 'energy conversion devices',
    'lemonade-monopoly': 'competition and monopoly',
    'chain-reaction': 'cause and effect words (because, so, as a result)',
    'treasure-map-steps': 'two-step word problems',
    'story-map-treasure': 'story elements (problem, solution, lesson)',
    'pizza-shop-assembly-line': 'specialization and productivity',
    'keyword-kitchen': 'choosing search keywords',
    'pizza-physics': 'circle area and circumference',
    'ice-cream-shop': 'volume of cylinders, cones and spheres',
    'dance-floor-moves': 'transformations (slides, flips, turns and dilations)',
    'transformation-golf': 'rigid motions and congruence',
    'space-cargo': "Newton's second law, F = ma",
    'inquiry-planner': 'writing a research question',
    'island-economy': 'resources and sustainability',
    'build-a-government': 'forms of government',
    'argument-frames-pro': 'academic argument language',
    'scam-shield': 'insurance, deductibles and scam texts',
    'flowchart-factory': 'flowcharts and pseudocode',
    'essay-architect': 'organizing an essay with transitions',
    'blueprint-builder': 'text structures',
    'snack-scale': 'more, fewer, the same',
    'skate-park-energy': 'kinetic and potential energy',
    'cone-slicer': 'conic sections',
    'meal-and-move-planner': 'nutrition and fitness planning',
    'depth-detective': 'perspective and space in art',
    'root-detective-cards': 'Greek and Latin roots',
    'screen-time-detective': 'digital wellness and screen time',
    'data-detective': 'scatter plots and lines of fit',
    'unit-detective': 'units and dimensional analysis',
    'watershed-detective': 'watershed pollution and solutions',
    'word-zoo': 'nouns, verbs and adjectives',
    'story-dress-up': 'pretend play and acting out a story',
    'particle-zoom': 'matter is made of particles',
    'summary-scaffold': 'summarizing and citing',
    'ten-frame-factory': 'teen numbers as ten and some more',
}
# rule 3: tools that leave their family, and why (everything else in a family stays in it)
LEAVES = {
    'class-snack-vote': 'Leaves class-poll on purpose: the class vote is the clash itself, and K-2 has one teacher for both tools.',
    'polynomial-garden': 'Leaves algebra-tiles on purpose: its grade 9 sibling Algebra Tile Studio owns the area model.',
    'snack-scale': 'Leaves balance on purpose: a seesaw tipped by how many snacks mixes up count and weight.',
}
RESTORED = {
    'pizza-party': 'Back in fraction-food: the pass moved it out of food for load relief only (no clash), so it stays Pizza Party.',
    'recipe-scaler': 'Back in fraction-food: Fraction Kitchen one grade up is the family spiral working as meant. The bakery goes, the recipe stays.',
    'compound-interest-garden': 'Stays in money, and compound interest is back at the core (the pass had moved it to emergency funds).',
}

# my lean on the open calls where it differs from, or adds to, the pass's recommendation
LEAN = {
    'counterclaim-ping-pong': 'Lean: rename to Counterclaim Rally, for the same reason Jenga and Mad Libs get renamed.',
    'retell-puppets': 'Lean: Bedtime Retell over the merge, since a merge makes one tool serve two modules.',
}


def concepts():
    rows = {}
    for f in sorted(os.listdir(os.path.join(ROOT, 'data', 'concepts'))):
        for line in open(os.path.join(ROOT, 'data', 'concepts', f), encoding='utf-8'):
            if line.startswith('#') or not line.strip():
                continue
            mod, title, fmt, fam, concept = line.rstrip('\n').split('|', 4)
            tid = re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')
            rows[tid] = dict(module=mod, title=title, family=fam, concept=concept, subject=f[:-4])
    return rows


def main():
    dec = json.load(open(os.path.join(OUT, 'decisions.json'), encoding='utf-8'))
    tags = {r['tool_id']: r for r in csv.DictReader(open(os.path.join(OUT, 'tags.csv'), encoding='utf-8'))}
    pairs = list(csv.DictReader(open(os.path.join(OUT, 'pairs.csv'), encoding='utf-8')))
    rows = concepts()
    fams = defaultdict(list)
    for r in rows.values():
        if r['family']:
            fams[r['family']].append(r['title'])
    out = []
    for x in dec:
        t, r = x['tool_id'], rows[x['tool_id']]
        ps = [p for p in pairs if t in (p['tool_a'], p['tool_b'])]
        other = lambda p: p['tool_b'] if p['tool_a'] == t else p['tool_a']
        live = [other(p) for p in ps if (p['live_b'] if p['tool_a'] == t else p['live_a']) == 'y']
        same = any(tags.get(other(p), {}).get('subject') == tags[t]['subject'] for p in ps)
        if x['fix'] in ('keep', 'spec-note', 'add-standard') and not ('Wave 1' in x['why']):
            tier, group = 'N', 'No change'
        elif 'Wave 1' in x['why'] or x['cluster'].startswith('W'):
            tier, group = 'A', 'Wave 1'
        elif t in TRADEMARK:
            tier, group = 'A', 'Trademark'
        elif live:
            tier, group = 'A', 'Clashes with a live tool'
        elif not ps:
            tier, group = 'C', 'Below the clash bar'
        elif same or x['band'] in ('K-2', '3-5'):
            tier, group = 'B', 'Same subject' if same else 'Crosses subjects in K-5'
        else:
            tier, group = 'C', 'Crosses subjects in 6-12'
        changes = x['fix'] in ('reshape', 'rename')
        new_title = TITLE.get(t, x['new_title']) if changes else ''
        new_concept = CONCEPT.get(t, x['new_concept']) if changes else ''
        rules = []
        if changes and t in TITLE and TITLE[t] != x['new_title']:
            rules.append(f"Title: {x['new_title'] or r['title']} becomes {TITLE[t]}, so the topic word stays in the title."
                         if TITLE[t] != r['title'] else f"Title: keeps {r['title']} (the pass had {x['new_title']}).")
        if changes and (new_title or r['title']) != r['title'] and t in LINE:
            rules.append(f"Topic line under the title on the tool page: \"{LINE[t]}\".")
        if r['family']:
            if t in LEAVES:
                rules.append('Family: ' + LEAVES[t])
            elif t in RESTORED:
                rules.append('Family: ' + RESTORED[t])
            elif changes:
                rules.append(f"Family: stays in {r['family']}.")
        if t in LEAN:
            rules.append(LEAN[t])
        out.append(dict(
            id=t, tier=tier, group=group, band=x['band'], subject=tags[t]['subject'], module=r['module'],
            family=r['family'], family_members=[m for m in fams.get(r['family'], []) if m != r['title']],
            cluster=x['cluster'], cluster_title=x['cluster_title'], fix=x['fix'],
            title=r['title'], concept=r['concept'],
            pass_title=x['new_title'], pass_concept=x['new_concept'],
            new_title=new_title if new_title and new_title != r['title'] else '',
            new_concept=new_concept, line=LINE.get(t, '') if changes and (new_title or r['title']) != r['title'] else '',
            rules=rules, why=x['why'], options=x['options'], live=live))
    order = {'A': 0, 'B': 1, 'C': 2, 'N': 3}
    out.sort(key=lambda o: (order[o['tier']], o['group'], ['K-2', '3-5', '6-8', '9-12'].index(o['band']), o['title']))
    json.dump(out, open(os.path.join(OUT, 'review.json'), 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
    count = defaultdict(int)
    for o in out:
        count[o['tier'] + ' ' + o['group']] += 1
    for k in sorted(count):
        print(f'{count[k]:3} {k}')
    print(len(out), 'items;', sum(bool(o['rules']) for o in out), 'with rule notes;',
          sum(1 for o in out if o['id'] in TITLE and o['fix'] in ('reshape', 'rename')), 'titles adjusted')


main()
