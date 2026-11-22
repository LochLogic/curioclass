import type { ShipHullId } from '../sim/narrative.ts';

/**
 * High-detail procedural 3D mesh generator for all 4 unlockable Farlight explorer crafts.
 * Uses smooth lofted fuselages, rounded teardrop canopies, swept airfoil wings,
 * cylindrical thruster nacelles, wingtip navigation lights, and glowing exhaust plumes.
 * Interleaved vertex layout: pos(3), normal(3), color(3), material(roughness, emissive) = 11 floats.
 */

export interface ProceduralMesh {
  vertices: Float32Array<ArrayBuffer>;
  indices: Uint16Array<ArrayBuffer>;
}

class SculptBuilder {
  private verts: number[] = [];
  private idx: number[] = [];

  /** Smooth lofted fuselage / nacelle / canopy along Z using elliptical cross-sections */
  addLoft(
    rings: ReadonlyArray<{ z: number; rx: number; ry: number; cy?: number }>,
    cx: number,
    sides: number,
    color: [number, number, number],
    roughness: number,
    emissive = 0,
  ): void {
    const startBase = this.verts.length / 11;
    const ringCount = rings.length;

    for (let r = 0; r < ringCount; r++) {
      const cur = rings[r]!;
      const prev = rings[Math.max(0, r - 1)]!;
      const next = rings[Math.min(ringCount - 1, r + 1)]!;
      const cy = cur.cy ?? 0;
      const dr = ((next.rx + next.ry) - (prev.rx + prev.ry)) * 0.5;
      const dz = Math.max(0.01, Math.abs(next.z - prev.z));
      const slopeZ = -dr / dz;

      for (let i = 0; i < sides; i++) {
        const a = (i / sides) * Math.PI * 2;
        const ca = Math.cos(a);
        const sa = Math.sin(a);
        const px = cx + ca * cur.rx;
        const py = cy + sa * cur.ry;
        let nx = ca / Math.max(0.05, cur.rx);
        let ny = sa / Math.max(0.05, cur.ry);
        let nz = slopeZ;
        const nLen = Math.hypot(nx, ny, nz) || 1;
        nx /= nLen; ny /= nLen; nz /= nLen;

        this.verts.push(px, py, cur.z, nx, ny, nz, color[0], color[1], color[2], roughness, emissive);
      }
    }

    for (let r = 0; r < ringCount - 1; r++) {
      const r0 = startBase + r * sides;
      const r1 = startBase + (r + 1) * sides;
      for (let i = 0; i < sides; i++) {
        const ni = (i + 1) % sides;
        this.idx.push(r0 + i, r0 + ni, r1 + ni, r0 + i, r1 + ni, r1 + i);
      }
    }
  }

  /** Swept airfoil wing (mirrored cleanly when side = -1 or +1) */
  addSweptWing(
    side: -1 | 1,
    rootX: number, rootY: number, rootZ: number, rootChord: number, rootThick: number,
    tipX: number, tipY: number, tipZ: number, tipChord: number, tipThick: number,
    color: [number, number, number],
    roughness: number,
    emissive = 0,
  ): void {
    const rx = rootX * side;
    const tx = tipX * side;
    // 4-point diamond airfoil profile at root and tip
    const profile = (x: number, y: number, z: number, ch: number, th: number): [number, number, number][] => [
      [x, y, z - ch * 0.52],         // leading edge
      [x, y + th * 0.62, z - ch * 0.1], // top ridge
      [x, y, z + ch * 0.48],         // trailing edge
      [x, y - th * 0.38, z - ch * 0.05], // bottom ridge
    ];
    const rp = profile(rx, rootY, rootZ, rootChord, rootThick);
    const tp = profile(tx, tipY, tipZ, tipChord, tipThick);

    const addQuad = (a: [number, number, number], b: [number, number, number], c: [number, number, number], d: [number, number, number]) => {
      const ux = b[0] - a[0], uy = b[1] - a[1], uz = b[2] - a[2];
      const vx = d[0] - a[0], vy = d[1] - a[1], vz = d[2] - a[2];
      let nx = uy * vz - uz * vy;
      let ny = uz * vx - ux * vz;
      let nz = ux * vy - uy * vx;
      const l = Math.hypot(nx, ny, nz) || 1;
      nx /= l; ny /= l; nz /= l;
      const base = this.verts.length / 11;
      for (const p of [a, b, c, d]) {
        this.verts.push(p[0], p[1], p[2], nx, ny, nz, color[0], color[1], color[2], roughness, emissive);
      }
      this.idx.push(base, base + 1, base + 2, base, base + 2, base + 3);
    };

    for (let i = 0; i < 4; i++) {
      const ni = (i + 1) % 4;
      if (side === 1) {
        addQuad(rp[i]!, tp[i]!, tp[ni]!, rp[ni]!);
      } else {
        addQuad(rp[ni]!, tp[ni]!, tp[i]!, rp[i]!);
      }
    }
    // Cap wingtip
    if (side === 1) {
      addQuad(tp[0]!, tp[1]!, tp[2]!, tp[3]!);
    } else {
      addQuad(tp[3]!, tp[2]!, tp[1]!, tp[0]!);
    }
  }

  /** Vertical tail stabilizer fin */
  addTailFin(
    cx: number, baseY: number, zFront: number, zBack: number, height: number, thick: number,
    color: [number, number, number],
    roughness: number,
    emissive = 0,
  ): void {
    const ht = thick * 0.5;
    const p: [number, number, number][] = [
      [cx - ht, baseY, zFront],
      [cx + ht, baseY, zFront],
      [cx + ht, baseY, zBack],
      [cx - ht, baseY, zBack],
      [cx - ht * 0.4, baseY + height, zFront + (zBack - zFront) * 0.58],
      [cx + ht * 0.4, baseY + height, zFront + (zBack - zFront) * 0.58],
      [cx + ht * 0.4, baseY + height, zBack + 0.14],
      [cx - ht * 0.4, baseY + height, zBack + 0.14],
    ];
    const faces: [number, number, number, number][] = [
      [0, 3, 7, 4], // left
      [2, 1, 5, 6], // right
      [1, 0, 4, 5], // leading edge
      [3, 2, 6, 7], // trailing edge
      [4, 7, 6, 5], // top
    ];
    for (const [ia, ib, ic, id] of faces) {
      const a = p[ia]!, b = p[ib]!, c = p[ic]!, d = p[id]!;
      const ux = b[0] - a[0], uy = b[1] - a[1], uz = b[2] - a[2];
      const vx = d[0] - a[0], vy = d[1] - a[1], vz = d[2] - a[2];
      let nx = uy * vz - uz * vy;
      let ny = uz * vx - ux * vz;
      let nz = ux * vy - uy * vx;
      const l = Math.hypot(nx, ny, nz) || 1;
      nx /= l; ny /= l; nz /= l;
      const base = this.verts.length / 11;
      for (const pt of [a, b, c, d]) {
        this.verts.push(pt[0], pt[1], pt[2], nx, ny, nz, color[0], color[1], color[2], roughness, emissive);
      }
      this.idx.push(base, base + 1, base + 2, base, base + 2, base + 3);
    }
  }

  /** Glowing engine thruster nacelle + luminous tapered exhaust plume */
  addThruster(
    cx: number, cy: number, zStart: number, radius: number,
    housingCol: [number, number, number],
    glowCol: [number, number, number],
  ): void {
    this.addLoft(
      [
        { z: zStart - 0.35, rx: radius * 0.72, ry: radius * 0.72, cy },
        { z: zStart, rx: radius, ry: radius, cy },
        { z: zStart + 0.38, rx: radius * 0.92, ry: radius * 0.92, cy },
      ],
      cx,
      10,
      housingCol,
      0.38,
      0,
    );
    // Glowing core + tapered thruster plume (emissive > 1.2 triggers dynamic boost pulse in ship.wgsl!)
    this.addLoft(
      [
        { z: zStart + 0.32, rx: radius * 0.68, ry: radius * 0.68, cy },
        { z: zStart + 0.56, rx: radius * 0.48, ry: radius * 0.48, cy },
        { z: zStart + 1.05, rx: 0.02, ry: 0.02, cy },
      ],
      cx,
      8,
      glowCol,
      0.1,
      1.65,
    );
  }

  build(): ProceduralMesh {
    return {
      vertices: new Float32Array(this.verts),
      indices: new Uint16Array(this.idx),
    };
  }
}

export function buildExplorerShipMesh(hull: ShipHullId = 'starhopper'): ProceduralMesh {
  const b = new SculptBuilder();
  const glass: [number, number, number] = [0.22, 0.74, 0.96];
  const slate: [number, number, number] = [0.22, 0.28, 0.38];
  const navGreen: [number, number, number] = [0.35, 1.0, 0.62];
  const navCoral: [number, number, number] = [1.0, 0.42, 0.35];

  if (hull === 'sunskipper') {
    const ivory: [number, number, number] = [0.97, 0.95, 0.89];
    const gold: [number, number, number] = [0.98, 0.76, 0.28];
    const glow: [number, number, number] = [1.0, 0.82, 0.32];

    b.addLoft(
      [
        { z: -1.65, rx: 0.04, ry: 0.04, cy: -0.02 },
        { z: -1.15, rx: 0.30, ry: 0.22, cy: 0.0 },
        { z: -0.25, rx: 0.46, ry: 0.30, cy: 0.02 },
        { z: 0.65, rx: 0.42, ry: 0.26, cy: 0.02 },
        { z: 1.20, rx: 0.22, ry: 0.16, cy: 0.0 },
      ],
      0, 12, ivory, 0.28, 0,
    );
    b.addLoft(
      [
        { z: -0.95, rx: 0.05, ry: 0.04, cy: 0.16 },
        { z: -0.45, rx: 0.30, ry: 0.22, cy: 0.26 },
        { z: 0.25, rx: 0.24, ry: 0.16, cy: 0.22 },
        { z: 0.55, rx: 0.04, ry: 0.03, cy: 0.16 },
      ],
      0, 10, glass, 0.06, 0.12,
    );
    for (const side of [-1, 1] as const) {
      b.addSweptWing(side, 0.35, 0.0, 0.05, 0.95, 0.12, 2.35, 0.08, 0.22, 0.55, 0.06, gold, 0.22, 0.08);
      b.addThruster(side * 1.08, -0.02, 0.78, 0.20, slate, glow);
      b.addTailFin(side * 1.08, 0.08, 0.25, 1.05, 0.42, 0.07, ivory, 0.3, 0);
    }
    return b.build();
  }

  if (hull === 'cloudwhale') {
    const cream: [number, number, number] = [0.95, 0.96, 0.93];
    const mint: [number, number, number] = [0.42, 0.88, 0.78];
    const glow: [number, number, number] = [0.42, 1.0, 0.84];

    b.addLoft(
      [
        { z: -1.65, rx: 0.08, ry: 0.07, cy: 0.0 },
        { z: -1.15, rx: 0.62, ry: 0.40, cy: 0.02 },
        { z: -0.15, rx: 0.82, ry: 0.48, cy: 0.04 },
        { z: 0.85, rx: 0.72, ry: 0.42, cy: 0.02 },
        { z: 1.38, rx: 0.46, ry: 0.28, cy: 0.0 },
      ],
      0, 14, cream, 0.32, 0,
    );
    b.addLoft(
      [
        { z: -1.05, rx: 0.08, ry: 0.06, cy: 0.26 },
        { z: -0.45, rx: 0.50, ry: 0.30, cy: 0.40 },
        { z: 0.25, rx: 0.42, ry: 0.26, cy: 0.38 },
        { z: 0.65, rx: 0.08, ry: 0.05, cy: 0.26 },
      ],
      0, 12, glass, 0.06, 0.14,
    );
    for (const side of [-1, 1] as const) {
      b.addSweptWing(side, 0.68, -0.04, 0.2, 1.25, 0.22, 1.85, -0.02, 0.48, 0.62, 0.10, mint, 0.3, 0);
      b.addThruster(side * 0.58, -0.04, 1.15, 0.26, slate, glow);
    }
    b.addTailFin(0, 0.32, 0.55, 1.28, 0.46, 0.12, mint, 0.32, 0);
    return b.build();
  }

  if (hull === 'comet-dart') {
    const cobalt: [number, number, number] = [0.22, 0.48, 0.96];
    const gold: [number, number, number] = [1.0, 0.80, 0.28];
    const glow: [number, number, number] = [0.48, 0.94, 1.0];

    b.addLoft(
      [
        { z: -1.95, rx: 0.03, ry: 0.03, cy: -0.02 },
        { z: -1.25, rx: 0.28, ry: 0.18, cy: 0.0 },
        { z: -0.25, rx: 0.46, ry: 0.25, cy: 0.0 },
        { z: 0.85, rx: 0.44, ry: 0.24, cy: 0.0 },
        { z: 1.25, rx: 0.32, ry: 0.18, cy: 0.0 },
      ],
      0, 12, cobalt, 0.22, 0,
    );
    b.addLoft(
      [
        { z: -1.05, rx: 0.04, ry: 0.03, cy: 0.14 },
        { z: -0.45, rx: 0.28, ry: 0.18, cy: 0.22 },
        { z: 0.25, rx: 0.22, ry: 0.14, cy: 0.18 },
        { z: 0.58, rx: 0.04, ry: 0.02, cy: 0.12 },
      ],
      0, 10, glass, 0.05, 0.16,
    );
    for (const side of [-1, 1] as const) {
      b.addSweptWing(side, 0.32, -0.02, 0.18, 1.45, 0.13, 2.05, 0.02, 0.78, 0.42, 0.06, cobalt, 0.24, 0);
      b.addTailFin(side * 1.98, 0.02, 0.58, 1.02, 0.46, 0.07, gold, 0.22, 0.12);
    }
    b.addThruster(0, -0.01, 1.08, 0.28, slate, glow);
    return b.build();
  }

  // Default: Sculpted Starhopper (rounded cream aerospace hull, coral wingtips, twin nacelles + plumes)
  const cream: [number, number, number] = [0.96, 0.93, 0.87];
  const coral: [number, number, number] = [0.98, 0.44, 0.32];
  const glow: [number, number, number] = [0.35, 0.95, 1.0];

  b.addLoft(
    [
      { z: -1.62, rx: 0.04, ry: 0.04, cy: -0.03 },
      { z: -1.18, rx: 0.34, ry: 0.24, cy: -0.01 },
      { z: -0.35, rx: 0.52, ry: 0.32, cy: 0.02 },
      { z: 0.55, rx: 0.50, ry: 0.30, cy: 0.02 },
      { z: 1.12, rx: 0.36, ry: 0.22, cy: 0.0 },
    ],
    0, 14, cream, 0.3, 0,
  );

  // Glossy teardrop bubble canopy
  b.addLoft(
    [
      { z: -0.96, rx: 0.05, ry: 0.04, cy: 0.18 },
      { z: -0.42, rx: 0.34, ry: 0.23, cy: 0.30 },
      { z: 0.24, rx: 0.28, ry: 0.18, cy: 0.26 },
      { z: 0.62, rx: 0.05, ry: 0.03, cy: 0.18 },
    ],
    0, 12, glass, 0.06, 0.12,
  );

  // Swept airfoil wings + coral wingtip winglets + subtle nav lights
  for (const side of [-1, 1] as const) {
    b.addSweptWing(side, 0.42, -0.04, 0.15, 1.05, 0.15, 1.82, 0.0, 0.45, 0.52, 0.07, cream, 0.32, 0);
    b.addTailFin(side * 1.78, 0.0, 0.22, 0.68, 0.34, 0.07, coral, 0.28, 0.05);
    // Tiny glowing wingtip nav beacon
    b.addLoft(
      [
        { z: 0.28, rx: 0.04, ry: 0.04, cy: 0.34 },
        { z: 0.42, rx: 0.06, ry: 0.06, cy: 0.34 },
        { z: 0.56, rx: 0.03, ry: 0.03, cy: 0.34 },
      ],
      side * 1.78, 6, side === 1 ? navGreen : navCoral, 0.1, 1.4,
    );
    b.addThruster(side * 0.42, -0.02, 0.96, 0.20, slate, glow);
  }

  // Center dorsal coral tail fin
  b.addTailFin(0, 0.24, 0.35, 1.08, 0.50, 0.08, coral, 0.28, 0);

  return b.build();
}
