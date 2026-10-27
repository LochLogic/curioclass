"""Shared loader for the overlap scripts. Not run directly; imported by rule.py, stats.py, standards.py, build_decisions.py.

tags.csv in docs/agents/overlap is the master tag file: edit it there, then rerun the scripts.
"""
import csv, os, io, json, collections, itertools, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
OUT = os.path.join(ROOT, 'docs', 'agents', 'overlap')
sys.path.insert(0, os.path.dirname(__file__))

GENERIC = {'generic', 'plain', 'real', 'school', 'cards', 'game'}
# raw setting group -> coarse group (used for new tags written in decisions_src.py)
GMAP = {'shop': 'shop-food', 'food-service': 'shop-food', 'bakery': 'shop-food',
        'kitchen': 'kitchen-food', 'food': 'kitchen-food', 'garden': 'garden-farm', 'farm': 'garden-farm',
        'zoo': 'animals', 'safari': 'animals', 'pond': 'nature', 'robot': 'robot-machine', 'machine': 'robot-machine',
        'council': 'council-debate', 'debate': 'council-debate', 'film': 'film-media', 'camera': 'film-media',
        'recording': 'film-media', 'radio': 'film-media', 'poster': 'newsroom', 'ocean': 'water', 'river': 'water',
        'travel': 'travel-map', 'trail': 'travel-map', 'train': 'vehicle', 'race': 'vehicle', 'casino': 'game-show',
        'vault': 'treasure', 'maze': 'fantasy', 'fortress': 'fantasy', 'body': 'body-medical', 'hospital': 'body-medical',
        'playground': 'town', 'music-studio': 'music', 'repair-shop': 'construction', 'business': 'business-money',
        'bank': 'business-money', 'dig': 'nature', 'security': 'cyber', 'network': 'cyber', 'code': 'cyber'}
BANDS = ['K-2', '3-5', '6-8', '9-12']


def coarse(g):
    g = GMAP.get(g, g)
    return 'generic' if g in GENERIC else g


def bands(label):
    if label == 'K-12': return list(BANDS)
    if label == '6-12': return ['6-8', '9-12']
    return [label]


def load(after=False):
    """Rows from tags.csv joined to tools-concepts.csv. after=True applies the new tags and titles in decisions_src.py."""
    concepts = {r['tool_id']: r for r in csv.DictReader(io.open(os.path.join(ROOT, 'data', 'tools-concepts.csv'), encoding='utf-8'))}
    rows = []
    for r in csv.DictReader(io.open(os.path.join(OUT, 'tags.csv'), encoding='utf-8')):
        r = dict(r)
        r['bands'] = bands(r['band'])
        r['grade'] = concepts[r['tool_id']]['grade']
        r['module_id'] = concepts[r['tool_id']]['module_id']
        r['concept'] = concepts[r['tool_id']]['concept']
        r['setting_group'] = coarse(r['setting_group'])
        r['changed'] = False
        rows.append(r)
    if after:
        from decisions_src import D
        by = {r['tool_id']: r for r in rows}
        renamed = json.load(io.open(os.path.join(OUT, 'renamed.json'), encoding='utf-8'))  # decisions keep pre-rename ids
        for d in D:
            r = by[renamed.get(d['id'], d['id'])]
            if os.path.exists(os.path.join(ROOT, 'tools', r['tool_id'], 'spec.md')):
                continue  # a spec is newer than the decision: tags.csv already carries its tags

            if d.get('title'): r['title'] = d['title']; r['changed'] = True
            if d.get('concept'): r['concept'] = d['concept']; r['changed'] = True
            a = d.get('after')
            if a:
                r['action'] = a['action']; r['setting_group'] = coarse(a['group']); r['skill_key'] = a['skill']
    return rows


def match(a, b):
    m = []
    if a['skill_key'] == b['skill_key']: m.append('skill')
    if a['action'] == b['action']: m.append('action')
    if a['setting_group'] == b['setting_group'] and a['setting_group'] != 'generic': m.append('setting')
    return m


def pairs(rows):
    """The clash rule: same band and 2 or more of skill, action, non-generic setting group. Cross-band pairs need all 3."""
    out = []
    for a, b in itertools.combinations(rows, 2):
        common = [x for x in BANDS if x in a['bands'] and x in b['bands']]
        m = match(a, b)
        if common and len(m) >= 2:
            out.append(('/'.join(common), a, b, m))
        elif not common and len(m) == 3:
            out.append(('cross-band', a, b, m))
    return out
