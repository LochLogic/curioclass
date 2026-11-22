import type { ProceduralMesh } from './ship-gen.ts';

/**
 * Procedural 3D meshes for Discovery Space Stations and Orbital Slalom Rings.
 * Interleaved vertex layout: pos(3), normal(3), color(3), material(roughness, emissive) = 11 floats.
 */

class RingMeshBuilder {
  private verts: number[] = [];
  private idx: number[] = [];

  addTorus(
    majorR: number,
    minorR: number,
    majorSegs: number,
    minorSegs: number,
    color: [number, number, number],
    roughness: number,
    emissive: number,
    axis: 'y' | 'z' = 'z',
  ): void {
    const base = this.verts.length / 11;
    for (let i = 0; i < majorSegs; i++) {
      const u = (i / majorSegs) * Math.PI * 2;
      const cu = Math.cos(u), su = Math.sin(u);
      for (let j = 0; j < minorSegs; j++) {
        const v = (j / minorSegs) * Math.PI * 2;
        const cv = Math.cos(v), sv = Math.sin(v);
        const r = majorR + minorR * cv;
        let px: number, py: number, pz: number;
        let nx: number, ny: number, nz: number;
        if (axis === 'z') {
          px = r * cu; py = r * su; pz = minorR * sv;
          nx = cv * cu; ny = cv * su; nz = sv;
        } else {
          px = r * cu; py = minorR * sv; pz = r * su;
          nx = cv * cu; ny = sv; nz = cv * su;
        }
        this.verts.push(px, py, pz, nx, ny, nz, color[0], color[1], color[2], roughness, emissive);
      }
    }
    for (let i = 0; i < majorSegs; i++) {
      const ni = (i + 1) % majorSegs;
      for (let j = 0; j < minorSegs; j++) {
        const nj = (j + 1) % minorSegs;
        const a = base + i * minorSegs + j;
        const b = base + ni * minorSegs + j;
        const c = base + ni * minorSegs + nj;
        const d = base + i * minorSegs + nj;
        this.idx.push(a, b, c, a, c, d);
      }
    }
  }

  addCylinder(
    cx: number, cy: number, cz: number,
    rxBot: number, rxTop: number, height: number,
    sides: number,
    color: [number, number, number],
    roughness: number,
    emissive = 0,
  ): void {
    const y0 = cy - height * 0.5;
    const y1 = cy + height * 0.5;
    for (let i = 0; i < sides; i++) {
      const a0 = (i / sides) * Math.PI * 2;
      const a1 = ((i + 1) / sides) * Math.PI * 2;
      const am = (a0 + a1) * 0.5;
      const nx = Math.cos(am), nz = Math.sin(am);
      const base = this.verts.length / 11;
      const pts: [number, number, number][] = [
        [cx + Math.cos(a0) * rxBot, y0, cz + Math.sin(a0) * rxBot],
        [cx + Math.cos(a1) * rxBot, y0, cz + Math.sin(a1) * rxBot],
        [cx + Math.cos(a1) * rxTop, y1, cz + Math.sin(a1) * rxTop],
        [cx + Math.cos(a0) * rxTop, y1, cz + Math.sin(a0) * rxTop],
      ];
      for (const p of pts) {
        this.verts.push(p[0], p[1], p[2], nx, 0, nz, color[0], color[1], color[2], roughness, emissive);
      }
      this.idx.push(base, base + 1, base + 2, base, base + 2, base + 3);
    }
  }

  build(): ProceduralMesh {
    return {
      vertices: new Float32Array(this.verts),
      indices: new Uint16Array(this.idx),
    };
  }
}

/** Cozy glowing Discovery Space Station (rotating habitat ring + central spire + docking halo) */
export function buildStationMesh(): ProceduralMesh {
  const b = new RingMeshBuilder();
  const hull: [number, number, number] = [0.92, 0.94, 0.97];
  const coral: [number, number, number] = [0.98, 0.52, 0.36];
  const gold: [number, number, number] = [1.0, 0.84, 0.42];
  const cyan: [number, number, number] = [0.36, 0.95, 1.0];

  // Central tower & observation cupola
  b.addCylinder(0, 0, 0, 3.2, 2.8, 18.0, 12, hull, 0.32, 0);
  b.addCylinder(0, 10.5, 0, 2.2, 0.4, 4.5, 10, coral, 0.28, 0.1);
  b.addCylinder(0, -10.5, 0, 0.4, 2.2, 4.5, 10, coral, 0.28, 0.1);
  // Glowing observation ring around hub
  b.addTorus(3.4, 0.45, 16, 6, gold, 0.15, 1.2, 'y');
  // Wide rotating habitat wheel + glowing inner window strip
  b.addTorus(14.0, 1.85, 24, 8, hull, 0.35, 0, 'y');
  b.addTorus(12.2, 0.52, 24, 6, cyan, 0.12, 1.35, 'y');
  // Four radial spokes
  for (let i = 0; i < 4; i++) {
    const a = (i / 4) * Math.PI * 2;
    b.addCylinder(Math.cos(a) * 7.5, 0, Math.sin(a) * 7.5, 1.1, 1.1, 1.4, 6, coral, 0.4, 0);
  }
  return b.build();
}

/** Glowing Holographic Orbital Slalom Ring (fly through to score!) */
export function buildSlalomRingMesh(): ProceduralMesh {
  const b = new RingMeshBuilder();
  const cyan: [number, number, number] = [0.32, 0.96, 1.0];
  const gold: [number, number, number] = [1.0, 0.82, 0.34];
  b.addTorus(18.0, 0.95, 24, 8, cyan, 0.12, 1.55, 'z');
  b.addTorus(20.0, 0.35, 24, 6, gold, 0.15, 1.1, 'z');
  return b.build();
}
