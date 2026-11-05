// Check every Worksheet Generator (site/assets/gen/<id>.js, listed in data/closet/generators.json).
//   node scripts/check_generators.mjs            all generators
//   node scripts/check_generators.mjs fractions  one or more by id
// For each generator it makes many sheets (every option of every setting, plus random mixes of settings, each with many
// sheet codes) and checks that: the sheet has its parts; nothing prints undefined, NaN, Infinity or an em dash; every
// answer blank has an answer; no question repeats on a sheet; the same code makes the same sheet; different codes make
// different sheets; and the generator's own verify() re-works every answer without finding a mismatch.
// The vocabulary and puzzle generators read the Word Wall list from the built site, so build with --closet first
// (CURIO_DIST picks another build folder).
import fs from 'node:fs';
import path from 'node:path';
import vm from 'node:vm';
import { fileURLToPath } from 'node:url';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const reg = JSON.parse(fs.readFileSync(path.join(ROOT, 'data/closet/generators.json'), 'utf8'));
const want = process.argv.slice(2);
const ids = reg.generators.map(g => g.id).filter(id => !want.length || want.includes(id));
const ctx = vm.createContext({ console, Math, JSON, Set, Map, Array, Object, String, Number, Date });
const load = f => vm.runInContext(fs.readFileSync(f, 'utf8'), ctx, { filename: f });
load(path.join(ROOT, 'site/assets/gen/engine.js'));
const Gen = ctx.Gen;
const dist = process.env.CURIO_DIST || path.join(ROOT, 'dist');
const data = {};
const SEEDS = +(process.env.GEN_SEEDS || 25);
let bad = 0;

for (const id of ids) {
  const file = path.join(ROOT, 'site/assets/gen', id + '.js');
  const out = [];
  if (!fs.existsSync(file)) { console.log(`${id}: MISSING ${file}`); bad++; continue; }
  const pre = path.join(ROOT, 'site/assets/gen', id + '-data.js');   // an optional word or fact bank, loaded first
  try { if (fs.existsSync(pre)) load(pre); load(file); } catch (e) { console.log(`${id}: does not load: ${e.message}`); bad++; continue; }
  const def = Gen.defs[id];
  if (!def) { console.log(`${id}: the file does not call Gen.add('${id}', ...)`); bad++; continue; }
  let d = null;
  if (def.data) {
    const f = path.join(dist, 'closet/worksheets/make', def.data + '.json');
    if (!fs.existsSync(f)) { console.log(`${id}: needs ${f}; build with --closet first`); bad++; continue; }
    d = data[def.data] ||= JSON.parse(fs.readFileSync(f, 'utf8'));
  }
  // settings to try: defaults, each option of each select/check on its own, then random mixes
  const combos = [Gen.values(def, {}, d)];
  const base = combos[0];
  for (const f of def.fields) {
    if (f.type === 'select') for (const [val] of Gen.opts(f, base, d).slice(0, 40)) combos.push(Gen.values(def, { ...base, [f.id]: val }, d));
    if (f.type === 'check') combos.push(Gen.values(def, { ...base, [f.id]: !base[f.id] }, d));
    if (f.type === 'number') for (const val of [f.min, f.max]) if (val != null) combos.push(Gen.values(def, { ...base, [f.id]: val }, d));
    if (f.type === 'text') combos.push(Gen.values(def, { ...base, [f.id]: 'Plants & "animals" <of> the desert' }, d));
  }
  const rr = Gen.rng('combos:' + id);
  for (let i = 0; i < 120; i++) {
    let v = {};
    for (const f of def.fields) {   // pick in field order, so options that depend on earlier fields are right
      v = Gen.values(def, v, d);
      if (f.type === 'select') { const o = Gen.opts(f, v, d); if (o.length) v[f.id] = rr.pick(o)[0]; }
      if (f.type === 'check') v[f.id] = rr.chance(.5);
      if (f.type === 'number') v[f.id] = rr.int(f.min ?? 1, f.max ?? 20);
    }
    combos.push(Gen.values(def, v, d));
  }
  let made = 0;
  const say = (v, seed, msg) => { if (out.length < 12) out.push(`  ${msg}   [settings ${JSON.stringify(v)} sheet ${seed}]`); else if (out.length === 12) out.push('  ...'); };
  for (const v of combos) {
    const htmls = new Set();
    for (let k = 0; k < SEEDS; k++) {
      const seed = 'T' + k.toString(36).toUpperCase().padStart(4, 'A');
      let s, html;
      try { s = Gen.make(id, v, seed, d); html = Gen.render(id, s); }
      catch (e) { say(v, seed, `crashed: ${e.stack.split('\n').slice(0, 2).join(' ')}`); continue; }
      made++;
      htmls.add(html.split(seed).join(''));   // the sheet code prints in the footer: ignore it when counting different sheets
      for (const k2 of ['title', 'directions']) if (!s[k2]) say(v, seed, `no ${k2}`);
      if (!Array.isArray(s.parts) || !s.parts.length) say(v, seed, 'no parts');
      if (!Array.isArray(s.items)) say(v, seed, 'no items list');
      if (!def.noKey && !(s.items || []).length) say(v, seed, 'no items');
      const m = html.match(/\bundefined\b|\bNaN\b|Infinity|\[object |\bnull\b(?! hypothesis)/);
      if (m) say(v, seed, `prints "${m[0]}" near: ${html.slice(Math.max(0, m.index - 80), m.index + 40).replace(/<[^>]+>/g, ' ')}`);
      if (/—/.test(html)) say(v, seed, 'has an em dash');
      if (/<span class="ws-ans">\s*<\/span>/.test(html)) say(v, seed, 'an answer blank with no answer');
      const qs = (s.items || []).map(x => String(x.q));
      const dup = qs.find((q, i) => qs.indexOf(q) !== i);
      if (dup) say(v, seed, `question repeats: ${dup.slice(0, 80)}`);
      for (const it of s.items || []) if (it.a == null || String(it.a) === '' || /NaN|undefined/.test(String(it.a))) { say(v, seed, `item with no answer: ${String(it.q).slice(0, 60)}`); break; }
      if (Gen.render(id, Gen.make(id, v, seed, d)) !== html) say(v, seed, 'the same sheet code made a different sheet');
      if (def.verify) for (const p of def.verify(s, v, d) || []) say(v, seed, `verify: ${p}`);
    }
    if (!def.fixed && htmls.size < Math.min(SEEDS, 5)) say(v, '*', `only ${htmls.size} different sheets from ${SEEDS} codes`);
  }
  console.log(`${id}: ${combos.length} settings, ${made} sheets, ${out.length ? out.length + ' problems' : 'ok'}`);
  if (out.length) { console.log(out.join('\n')); bad++; }
}
console.log(bad ? `${bad} generator(s) with problems` : `all ${ids.length} generators ok`);
process.exit(bad ? 1 : 0);
