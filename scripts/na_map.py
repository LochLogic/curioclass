"""Build a North America map (countries and culture regions) as projected SVG paths for tools to inline.

    python scripts/na_map.py <countries-50m.json> <out.json>

Input: world-atlas 2.0.2 countries-50m.json (Natural Earth, public domain; https://cdn.jsdelivr.net/npm/world-atlas@2.0.2/).
Output JSON: {"view": [w, h], "countries": [{"id", "name", "d"}], "regions": {key: d}, "centers": {key: [x, y]}}
Projection: Albers equal-area conic, standard parallels 25 and 60, centered on 100 W. Culture regions are drawn
by hand in longitude and latitude (their borders are approximate on purpose) and clipped to the land.
Bundle it with the token "json:<name>" in a tool's src.html (scripts/bundle_tool.py).
"""
import json, math, sys
from shapely.geometry import Polygon, MultiPolygon, box, mapping, shape
from shapely.ops import unary_union, transform

KEEP = {'United States of America', 'Canada', 'Mexico', 'Greenland', 'Guatemala', 'Belize', 'Honduras', 'El Salvador',
        'Nicaragua', 'Costa Rica', 'Panama', 'Cuba', 'Haiti', 'Dominican Rep.', 'Jamaica', 'Bahamas', 'Puerto Rico'}

# approximate culture areas (longitude, latitude), clipped to land later
REGIONS = {
    'arctic': [(-170, 76), (-10, 86), (-10, 58), (-60, 58), (-64, 60), (-78, 61), (-94, 61), (-115, 67), (-140, 69), (-158, 66), (-163, 60), (-157, 57), (-158, 54), (-179.9, 50), (-179.9, 62)],
    'subarctic': [(-163, 60), (-158, 66), (-140, 69), (-115, 67), (-94, 61), (-78, 61), (-64, 60), (-52, 54), (-52, 46.5), (-60, 47.5), (-67, 49), (-76, 47), (-86, 48), (-95, 50), (-110, 53),
                  (-118, 55), (-125.2, 53.5), (-128, 57), (-138, 59), (-152, 59), (-160, 58)],
    'northwest': [(-152, 59), (-138, 59), (-128, 57), (-124, 52), (-121.5, 49), (-121.5, 45.5), (-122.5, 42), (-124, 40), (-128, 45), (-133, 52), (-142, 58)],
    'plateau': [(-121.5, 49), (-124, 52), (-125.2, 53.5), (-118, 55), (-114, 51), (-113, 47), (-114, 44.5), (-117.5, 43.5), (-121.5, 44.5), (-121.5, 45.5)],
    'basin': [(-121.5, 44.5), (-117.5, 43.5), (-114, 44.5), (-110.5, 42.5), (-107.5, 40), (-109, 37.5), (-113, 36.5), (-117, 35.3), (-119.5, 38), (-120.5, 40.5)],
    'california': [(-124, 40), (-122.5, 42), (-120.5, 42), (-120.5, 40.5), (-119.5, 38), (-117, 35.3), (-115, 32.5), (-117.2, 32.5), (-121, 34.5), (-124.5, 38)],
    'southwest': [(-117, 35.3), (-113, 36.5), (-109, 37.5), (-104.5, 38), (-102.5, 35), (-103.5, 29.5), (-106, 28), (-110, 27), (-113, 29), (-115, 32.5)],
    'plains': [(-118, 55), (-110, 53), (-95, 50), (-93.5, 46), (-91.5, 39.5), (-94, 36), (-95, 34), (-97.5, 28), (-103.5, 29.5), (-102.5, 35), (-104.5, 38), (-109, 37.5), (-107.5, 40),
               (-110.5, 42.5), (-114, 44.5), (-113, 47), (-114, 51)],
    'northeast': [(-95, 50), (-86, 48), (-76, 47), (-67, 49), (-60, 47.5), (-60, 45), (-66, 43.5), (-70, 41), (-75, 38.5), (-81.5, 37.5), (-88, 37), (-91.5, 39.5), (-93.5, 46)],
    'southeast': [(-95, 34), (-94, 36), (-91.5, 39.5), (-88, 37), (-81.5, 37.5), (-75, 38.5), (-75.5, 35), (-81, 31), (-79.5, 25), (-82, 26), (-85, 29.8), (-89.5, 29), (-94, 29.5), (-97.5, 28)],
}

PHI1, PHI2, PHI0, LAM0 = map(math.radians, (25, 60, 45, -100))
N = (math.sin(PHI1) + math.sin(PHI2)) / 2
C = math.cos(PHI1) ** 2 + 2 * N * math.sin(PHI1)
RHO0 = math.sqrt(C - 2 * N * math.sin(PHI0)) / N


def albers(lon, lat):
    rho = math.sqrt(C - 2 * N * math.sin(math.radians(lat))) / N
    th = N * (math.radians(lon) - LAM0)
    return rho * math.sin(th), RHO0 - rho * math.cos(th)


def decode(topo, name):
    sx, sy = topo['transform']['scale']; tx, ty = topo['transform']['translate']
    arcs = []
    for arc in topo['arcs']:
        x = y = 0; pts = []
        for dx, dy in arc:
            x += dx; y += dy
            pts.append((x * sx + tx, y * sy + ty))
        arcs.append(pts)

    def ring(ids):
        out = []
        for i in ids:
            pts = arcs[i] if i >= 0 else arcs[~i][::-1]
            out.extend(pts if not out else pts[1:])
        return out

    feats = []
    for g in topo['objects'][name]['geometries']:
        polys = [g['arcs']] if g['type'] == 'Polygon' else g.get('arcs', [])
        shp = [Polygon(ring(p[0]), [ring(h) for h in p[1:]]) for p in polys]
        feats.append((g.get('properties', {}).get('name'), g.get('id'), MultiPolygon([s for s in shp if s.is_valid or True])))
    return feats


def path(geom, k, ox, oy):
    geoms = geom.geoms if hasattr(geom, 'geoms') else [geom]
    out = []
    for p in geoms:
        if p.is_empty or p.geom_type != 'Polygon':
            continue
        for r in [p.exterior, *p.interiors]:
            c = list(r.coords)
            out.append('M' + 'L'.join(f'{(x - ox) * k:.1f},{(oy - y) * k:.1f}' for x, y in c) + 'Z')
    return ''.join(out)


def main():
    topo = json.load(open(sys.argv[1], encoding='utf-8'))
    area = box(-179.9, 6, -10, 84)
    feats = []
    for name, fid, mp in decode(topo, 'countries'):
        if name not in KEEP:
            continue
        g = mp.buffer(0).intersection(area)
        # leave out Hawaii and the far western Aleutians so the map stays compact
        g = unary_union([p for p in getattr(g, 'geoms', [g]) if not (p.centroid.y < 30 and p.centroid.x < -140) and p.centroid.x > -178])
        feats.append((name, fid, g))
    land = unary_union([g for _, _, g in feats])
    proj = lambda g: transform(lambda x, y, z=None: albers(x, y), g.segmentize(0.5) if hasattr(g, 'segmentize') else g)
    pf = [(n, i, proj(g).simplify(0.0012, preserve_topology=True)) for n, i, g in feats]
    minx, miny, maxx, maxy = unary_union([g for *_, g in pf]).bounds
    W = 1000; k = W / (maxx - minx); H = round((maxy - miny) * k)
    out = {'view': [W, H], 'countries': [], 'regions': {}, 'centers': {}}
    for n, i, g in pf:
        out['countries'].append({'id': i, 'name': n, 'd': path(g, k, minx, maxy)})
    for key, ring in REGIONS.items():
        r = Polygon(ring).segmentize(0.5).intersection(land)
        r = proj(r).simplify(0.0012, preserve_topology=True)
        out['regions'][key] = path(r, k, minx, maxy)
        c = r.representative_point()
        out['centers'][key] = [round((c.x - minx) * k), round((maxy - c.y) * k)]
    json.dump(out, open(sys.argv[2], 'w'), separators=(',', ':'))
    print(f'{W}x{H}, {len(out["countries"])} countries, {sum(len(c["d"]) for c in out["countries"]) // 1024} KB of country paths')


if __name__ == '__main__':
    main()
