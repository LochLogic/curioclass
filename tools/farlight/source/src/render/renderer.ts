import spaceWgsl from './shaders/space.wgsl';
import planetWgsl from './shaders/planet.wgsl';
import worldPropsWgsl from './shaders/world-props.wgsl';
import shipWgsl from './shaders/ship.wgsl';
import postWgsl from './shaders/post.wgsl';
import type { GpuContext, QualityTier } from './gpu-context.ts';
import type { StarKind, StarSystem } from '../sim/galaxy.ts';
import type { ShipState } from '../sim/flight.ts';
import { BIOME_INDEX, type PlanetFlightState } from '../sim/planet-flight.ts';
import { buildExplorerShipMesh, type ProceduralMesh } from '../proc/ship-gen.ts';
import { buildSlalomRingMesh, buildStationMesh } from '../proc/station-gen.ts';
import type { OrbitalActivityState } from '../sim/slalom.ts';
import type { ShipHullId } from '../sim/narrative.ts';
import type { CampRecord } from '../sim/journey.ts';
import {
  buildCampMesh,
  buildCityTowerMesh,
  buildCritterMesh,
  buildFishMesh,
  buildFlierMesh,
  buildGrassMesh,
  buildLanternMesh,
  buildRoverMesh,
  buildRuinMesh,
  buildSpireMesh,
  buildTreeMesh,
  spawnSurfaceInstances,
  type WorldInstanceSet,
} from '../proc/world-gen.ts';
import { quatRotateVec, v3Norm, v3Sub, vec3 } from '../sim/math.ts';

const STAR_KIND_INDEX: Record<StarKind, number> = {
  'warm-sun': 0,
  'amber-dwarf': 1,
  'sky-giant': 2,
  pulsar: 3,
  'black-hole': 4,
};

const QUALITY_INDEX: Record<QualityTier, number> = {
  performance: 0,
  high: 1,
  ultra: 2,
};

function perspectiveMatrix(fovRad: number, aspect: number, near: number, far: number): Float32Array {
  const f = 1.0 / Math.tan(fovRad * 0.5);
  const nf = 1.0 / (near - far);
  return new Float32Array([
    f / aspect, 0, 0, 0,
    0, f, 0, 0,
    0, 0, far * nf, -1,
    0, 0, far * near * nf, 0,
  ]);
}

function mulMat4(a: Float32Array, b: Float32Array): Float32Array {
  const out = new Float32Array(16);
  for (let c = 0; c < 4; c++) {
    for (let r = 0; r < 4; r++) {
      out[c * 4 + r] =
        a[0 * 4 + r]! * b[c * 4 + 0]! +
        a[1 * 4 + r]! * b[c * 4 + 1]! +
        a[2 * 4 + r]! * b[c * 4 + 2]! +
        a[3 * 4 + r]! * b[c * 4 + 3]!;
    }
  }
  return out;
}

function modelMatrix(tx: number, ty: number, tz: number, pitch: number, roll: number, scale = 1): Float32Array {
  const cp = Math.cos(pitch), sp = Math.sin(pitch);
  const cr = Math.cos(roll), sr = Math.sin(roll);
  // Scale + Rotate Z (roll) then X (pitch) + translate
  return new Float32Array([
    cr * scale, sr * cp * scale, -sr * sp * scale, 0,
    -sr * scale, cr * cp * scale, -cr * sp * scale, 0,
    0, sp * scale, cp * scale, 0,
    tx, ty, tz, 1,
  ]);
}

function viewMatrixFromBasis(
  right: { x: number; y: number; z: number },
  up: { x: number; y: number; z: number },
  forward: { x: number; y: number; z: number },
): Float32Array {
  // Column-major view rotation mapping camera-relative world pos into view space (-Z forward)
  return new Float32Array([
    right.x, up.x, -forward.x, 0,
    right.y, up.y, -forward.y, 0,
    right.z, up.z, -forward.z, 0,
    0, 0, 0, 1,
  ]);
}

interface GpuMesh {
  vertexBuf: GPUBuffer;
  indexBuf: GPUBuffer;
  indexCount: number;
}

export class FarlightRenderer {
  private gpu: GpuContext;
  private spacePipeline: GPURenderPipeline;
  private planetPipeline: GPURenderPipeline;
  private worldPropsPipeline: GPURenderPipeline;
  private shipPipeline: GPURenderPipeline;
  private postPipeline: GPURenderPipeline;

  private spaceUniformBuf: GPUBuffer;
  private spaceUniformData: Float32Array<ArrayBuffer>;
  private spaceBindGroup: GPUBindGroup;

  private planetUniformBuf: GPUBuffer;
  private planetUniformData: Float32Array<ArrayBuffer>;
  private planetBindGroup: GPUBindGroup;

  private worldPropsUniformBuf: GPUBuffer;
  private worldPropsUniformData: Float32Array<ArrayBuffer>;
  private worldPropsBindGroup: GPUBindGroup;

  private treeMesh: GpuMesh;
  private lanternMesh: GpuMesh;
  private spireMesh: GpuMesh;
  private critterMesh: GpuMesh;
  private flierMesh: GpuMesh;
  private grassMesh: GpuMesh;
  private fishMesh: GpuMesh;
  private ruinMesh: GpuMesh;
  private cityMesh: GpuMesh;
  private campMesh: GpuMesh;
  private roverMesh: GpuMesh;
  private stationMesh: GpuMesh;
  private slalomRingMesh: GpuMesh;

  private treeInstBuf: GPUBuffer | null = null;
  private lanternInstBuf: GPUBuffer | null = null;
  private spireInstBuf: GPUBuffer | null = null;
  private critterInstBuf: GPUBuffer | null = null;
  private flierInstBuf: GPUBuffer | null = null;
  private grassInstBuf: GPUBuffer | null = null;
  private fishInstBuf: GPUBuffer | null = null;
  private ruinInstBuf: GPUBuffer | null = null;
  private cityInstBuf: GPUBuffer | null = null;
  private parkedShipInstBuf: GPUBuffer;
  private parkedShipData = new Float32Array(8);
  private campInstBuf: GPUBuffer;
  private campInstData = new Float32Array(8);
  private stationInstBuf: GPUBuffer;
  private stationInstData = new Float32Array(8);
  private slalomInstBuf: GPUBuffer;
  private slalomInstData = new Float32Array(6 * 8);
  private cachedInstSeed = -1;
  private cachedInstances: WorldInstanceSet | null = null;

  private shipUniformBuf: GPUBuffer;
  private shipUniformData: Float32Array<ArrayBuffer>;
  private shipBindGroup: GPUBindGroup;
  private shipVertexBuf: GPUBuffer;
  private shipIndexBuf: GPUBuffer;
  private shipIndexCount: number;

  private postSampler: GPUSampler;
  private postBindGroup!: GPUBindGroup;

  constructor(gpu: GpuContext) {
    this.gpu = gpu;
    const { device, format } = gpu;

    // 1. Space HDR pipeline
    const spaceMod = device.createShaderModule({ code: spaceWgsl });
    this.spacePipeline = device.createRenderPipeline({
      layout: 'auto',
      vertex: { module: spaceMod, entryPoint: 'vsMain' },
      fragment: {
        module: spaceMod,
        entryPoint: 'fsMain',
        targets: [{ format: 'rgba16float' }],
      },
      primitive: { topology: 'triangle-list' },
    });

    // 8 vec4s + 6 * 6 vec4s = 44 vec4s = 176 floats = 704 bytes
    this.spaceUniformData = new Float32Array(176);
    this.spaceUniformBuf = device.createBuffer({
      size: this.spaceUniformData.byteLength,
      usage: GPUBufferUsage.UNIFORM | GPUBufferUsage.COPY_DST,
    });
    this.spaceBindGroup = device.createBindGroup({
      layout: this.spacePipeline.getBindGroupLayout(0),
      entries: [{ binding: 0, resource: { buffer: this.spaceUniformBuf } }],
    });

    // 1b. Planetary Surface HDR pipeline (writes exact frag_depth for 3D flora/critter occlusion)
    const planetMod = device.createShaderModule({ code: planetWgsl });
    this.planetPipeline = device.createRenderPipeline({
      layout: 'auto',
      vertex: { module: planetMod, entryPoint: 'vsMain' },
      fragment: {
        module: planetMod,
        entryPoint: 'fsMain',
        targets: [{ format: 'rgba16float' }],
      },
      primitive: { topology: 'triangle-list' },
      depthStencil: {
        format: 'depth24plus',
        depthWriteEnabled: true,
        depthCompare: 'always',
      },
    });

    // 9 vec4s = 36 floats = 144 bytes
    this.planetUniformData = new Float32Array(36);
    this.planetUniformBuf = device.createBuffer({
      size: this.planetUniformData.byteLength,
      usage: GPUBufferUsage.UNIFORM | GPUBufferUsage.COPY_DST,
    });
    this.planetBindGroup = device.createBindGroup({
      layout: this.planetPipeline.getBindGroupLayout(0),
      entries: [{ binding: 0, resource: { buffer: this.planetUniformBuf } }],
    });

    // 1c. GPU-Instanced 3D World Props (Trees, Lantern Fungi, Crystal Spires, Critters, Parked Ship)
    const propsMod = device.createShaderModule({ code: worldPropsWgsl });
    this.worldPropsPipeline = device.createRenderPipeline({
      layout: 'auto',
      vertex: {
        module: propsMod,
        entryPoint: 'vsMain',
        buffers: [
          {
            arrayStride: 11 * 4,
            stepMode: 'vertex',
            attributes: [
              { shaderLocation: 0, offset: 0, format: 'float32x3' },
              { shaderLocation: 1, offset: 12, format: 'float32x3' },
              { shaderLocation: 2, offset: 24, format: 'float32x3' },
              { shaderLocation: 3, offset: 36, format: 'float32x2' },
            ],
          },
          {
            arrayStride: 8 * 4,
            stepMode: 'instance',
            attributes: [
              { shaderLocation: 4, offset: 0, format: 'float32x4' },
              { shaderLocation: 5, offset: 16, format: 'float32x4' },
            ],
          },
        ],
      },
      fragment: {
        module: propsMod,
        entryPoint: 'fsMain',
        targets: [{ format: 'rgba16float' }],
      },
      primitive: { topology: 'triangle-list', cullMode: 'back' },
      depthStencil: {
        format: 'depth24plus',
        depthWriteEnabled: true,
        depthCompare: 'less',
      },
    });

    // mat4(16) + 6*vec4(24) = 40 floats = 160 bytes
    this.worldPropsUniformData = new Float32Array(40);
    this.worldPropsUniformBuf = device.createBuffer({
      size: this.worldPropsUniformData.byteLength,
      usage: GPUBufferUsage.UNIFORM | GPUBufferUsage.COPY_DST,
    });
    this.worldPropsBindGroup = device.createBindGroup({
      layout: this.worldPropsPipeline.getBindGroupLayout(0),
      entries: [{ binding: 0, resource: { buffer: this.worldPropsUniformBuf } }],
    });

    const padU16 = (src: Uint16Array<ArrayBuffer>): Uint16Array<ArrayBuffer> => {
      if ((src.byteLength & 3) === 0) return src;
      const padded = new Uint16Array(src.length + 1);
      padded.set(src);
      return padded;
    };

    const uploadMesh = (mesh: ProceduralMesh): GpuMesh => {
      const vertexBuf = device.createBuffer({
        size: (mesh.vertices.byteLength + 3) & ~3,
        usage: GPUBufferUsage.VERTEX | GPUBufferUsage.COPY_DST,
      });
      device.queue.writeBuffer(vertexBuf, 0, mesh.vertices);
      const idxData = padU16(mesh.indices);
      const indexBuf = device.createBuffer({
        size: idxData.byteLength,
        usage: GPUBufferUsage.INDEX | GPUBufferUsage.COPY_DST,
      });
      device.queue.writeBuffer(indexBuf, 0, idxData);
      return { vertexBuf, indexBuf, indexCount: mesh.indices.length };
    };

    this.treeMesh = uploadMesh(buildTreeMesh());
    this.lanternMesh = uploadMesh(buildLanternMesh());
    this.spireMesh = uploadMesh(buildSpireMesh());
    this.critterMesh = uploadMesh(buildCritterMesh());
    this.flierMesh = uploadMesh(buildFlierMesh());
    this.grassMesh = uploadMesh(buildGrassMesh());
    this.fishMesh = uploadMesh(buildFishMesh());
    this.ruinMesh = uploadMesh(buildRuinMesh());
    this.cityMesh = uploadMesh(buildCityTowerMesh());
    this.campMesh = uploadMesh(buildCampMesh());
    this.roverMesh = uploadMesh(buildRoverMesh());
    this.stationMesh = uploadMesh(buildStationMesh());
    this.slalomRingMesh = uploadMesh(buildSlalomRingMesh());
    this.parkedShipInstBuf = device.createBuffer({
      size: 8 * 4,
      usage: GPUBufferUsage.VERTEX | GPUBufferUsage.COPY_DST,
    });
    this.campInstBuf = device.createBuffer({
      size: 8 * 4,
      usage: GPUBufferUsage.VERTEX | GPUBufferUsage.COPY_DST,
    });
    this.stationInstBuf = device.createBuffer({
      size: 8 * 4,
      usage: GPUBufferUsage.VERTEX | GPUBufferUsage.COPY_DST,
    });
    this.slalomInstBuf = device.createBuffer({
      size: 6 * 8 * 4,
      usage: GPUBufferUsage.VERTEX | GPUBufferUsage.COPY_DST,
    });

    // 2. 3D Procedural Ship HDR pipeline
    const shipMod = device.createShaderModule({ code: shipWgsl });
    this.shipPipeline = device.createRenderPipeline({
      layout: 'auto',
      vertex: {
        module: shipMod,
        entryPoint: 'vsMain',
        buffers: [{
          arrayStride: 11 * 4,
          attributes: [
            { shaderLocation: 0, offset: 0, format: 'float32x3' },
            { shaderLocation: 1, offset: 12, format: 'float32x3' },
            { shaderLocation: 2, offset: 24, format: 'float32x3' },
            { shaderLocation: 3, offset: 36, format: 'float32x2' },
          ],
        }],
      },
      fragment: {
        module: shipMod,
        entryPoint: 'fsMain',
        targets: [{ format: 'rgba16float' }],
      },
      primitive: { topology: 'triangle-list', cullMode: 'back' },
      depthStencil: {
        format: 'depth24plus',
        depthWriteEnabled: true,
        depthCompare: 'less',
      },
    });

    const shipMesh = buildExplorerShipMesh();
    this.shipIndexCount = shipMesh.indices.length;
    this.shipVertexBuf = device.createBuffer({
      size: shipMesh.vertices.byteLength,
      usage: GPUBufferUsage.VERTEX | GPUBufferUsage.COPY_DST,
    });
    device.queue.writeBuffer(this.shipVertexBuf, 0, shipMesh.vertices);

    const shipIdx = padU16(shipMesh.indices);
    this.shipIndexBuf = device.createBuffer({
      size: shipIdx.byteLength,
      usage: GPUBufferUsage.INDEX | GPUBufferUsage.COPY_DST,
    });
    device.queue.writeBuffer(this.shipIndexBuf, 0, shipIdx);

    // 2 mat4 (32 floats) + 3 vec4 (12 floats) = 44 floats = 176 bytes
    this.shipUniformData = new Float32Array(44);
    this.shipUniformBuf = device.createBuffer({
      size: this.shipUniformData.byteLength,
      usage: GPUBufferUsage.UNIFORM | GPUBufferUsage.COPY_DST,
    });
    this.shipBindGroup = device.createBindGroup({
      layout: this.shipPipeline.getBindGroupLayout(0),
      entries: [{ binding: 0, resource: { buffer: this.shipUniformBuf } }],
    });

    // 3. AgX + Bloom Post-Processing pipeline
    const postMod = device.createShaderModule({ code: postWgsl });
    this.postPipeline = device.createRenderPipeline({
      layout: 'auto',
      vertex: { module: postMod, entryPoint: 'vsMain' },
      fragment: {
        module: postMod,
        entryPoint: 'fsMain',
        targets: [{ format }],
      },
      primitive: { topology: 'triangle-list' },
    });

    this.postSampler = device.createSampler({ magFilter: 'linear', minFilter: 'linear' });
    this.rebuildPostBindGroup();
  }

  setShipHull(hull: ShipHullId): void {
    const { device } = this.gpu;
    const mesh = buildExplorerShipMesh(hull);
    const idxData =
      (mesh.indices.byteLength & 3) === 0
        ? mesh.indices
        : (() => {
            const p = new Uint16Array(mesh.indices.length + 1);
            p.set(mesh.indices);
            return p;
          })();
    this.shipVertexBuf.destroy();
    this.shipIndexBuf.destroy();
    this.shipIndexCount = mesh.indices.length;
    this.shipVertexBuf = device.createBuffer({
      size: (mesh.vertices.byteLength + 3) & ~3,
      usage: GPUBufferUsage.VERTEX | GPUBufferUsage.COPY_DST,
    });
    device.queue.writeBuffer(this.shipVertexBuf, 0, mesh.vertices);
    this.shipIndexBuf = device.createBuffer({
      size: idxData.byteLength,
      usage: GPUBufferUsage.INDEX | GPUBufferUsage.COPY_DST,
    });
    device.queue.writeBuffer(this.shipIndexBuf, 0, idxData);
  }

  rebuildPostBindGroup(): void {
    this.postBindGroup = this.gpu.device.createBindGroup({
      layout: this.postPipeline.getBindGroupLayout(0),
      entries: [
        { binding: 0, resource: this.gpu.hdrTexture.createView() },
        { binding: 1, resource: this.postSampler },
      ],
    });
  }

  render(
    system: StarSystem,
    ship: ShipState,
    timeSec: number,
    visualBank: number,
    visualPitch: number,
    jumpProgress = 0,
    scanPulse = 0,
    orbital: OrbitalActivityState | null = null,
  ): void {
    const { device, width, height } = this.gpu;
    const aspect = width / Math.max(1, height);
    const fovRad = (62 * Math.PI) / 180;
    const tanHalfFov = Math.tan(fovRad * 0.5);

    const right = quatRotateVec(ship.orientation, vec3(1, 0, 0));
    const up = quatRotateVec(ship.orientation, vec3(0, 1, 0));
    const forward = quatRotateVec(ship.orientation, vec3(0, 0, -1));

    // Floating-origin camera-relative star position (star sits at 0,0,0 in system coords)
    const starRel = vec3(-ship.position.x, -ship.position.y, -ship.position.z);

    const u = this.spaceUniformData;
    u.set([right.x, right.y, right.z, aspect], 0);
    u.set([up.x, up.y, up.z, tanHalfFov], 4);
    u.set([forward.x, forward.y, forward.z, timeSec], 8);
    u.set([starRel.x, starRel.y, starRel.z, system.starRadius], 12);
    u.set([system.starColor[0], system.starColor[1], system.starColor[2], STAR_KIND_INDEX[system.starKind]], 16);
    u.set([system.nebulaPrimary[0], system.nebulaPrimary[1], system.nebulaPrimary[2], QUALITY_INDEX[this.gpu.quality]], 20);
    u.set([system.nebulaSecondary[0], system.nebulaSecondary[1], system.nebulaSecondary[2], system.planets.length], 24);
    u.set([jumpProgress, scanPulse, 0, 0], 28);

    // Pack up to 6 planets (camera-relative positions)
    for (let i = 0; i < Math.min(6, system.planets.length); i++) {
      const p = system.planets[i]!;
      const rel = v3Sub(p.position, ship.position);
      const base = 32 + i * 24;
      u.set([rel.x, rel.y, rel.z, p.radius], base);
      u.set([p.colorA[0], p.colorA[1], p.colorA[2], p.biome === 'cloud-giant' ? 1 : 0], base + 4);
      u.set([p.colorB[0], p.colorB[1], p.colorB[2], p.hasRings ? 1 : 0], base + 8);
      u.set([p.atmosphereColor[0], p.atmosphereColor[1], p.atmosphereColor[2], p.ringTilt], base + 12);
      u.set([p.ringInner, p.ringOuter, p.id + 1, 0], base + 16);
      u.set([p.ringColor[0], p.ringColor[1], p.ringColor[2], 0], base + 20);
    }
    device.queue.writeBuffer(this.spaceUniformBuf, 0, u);

    // Pack 3D Explorer Ship uniforms (sleek, compact framing leaving wide unobstructed cosmic vista)
    const proj = perspectiveMatrix(fovRad, aspect, 0.2, 100);
    const bob = Math.sin(timeSec * 2.1) * 0.045;
    const model = modelMatrix(0, -1.62 + bob, -7.6 - ship.boostAmount * 0.65, visualPitch, visualBank, 0.78);
    const mvp = mulMat4(proj, model);

    // Transform star direction into camera/view space for accurate ship lighting
    const starDirWorld = v3Norm(starRel);
    const lx = starDirWorld.x * right.x + starDirWorld.y * right.y + starDirWorld.z * right.z;
    const ly = starDirWorld.x * up.x + starDirWorld.y * up.y + starDirWorld.z * up.z;
    const lz = -(starDirWorld.x * forward.x + starDirWorld.y * forward.y + starDirWorld.z * forward.z);

    const su = this.shipUniformData;
    su.set(mvp, 0);
    su.set(model, 16);
    su.set([lx, ly, lz, ship.boostAmount], 32);
    su.set([system.starColor[0], system.starColor[1], system.starColor[2], timeSec], 36);
    su.set([system.nebulaPrimary[0], system.nebulaPrimary[1], system.nebulaPrimary[2], 0], 40);
    device.queue.writeBuffer(this.shipUniformBuf, 0, su);

    // Record GPU commands
    const enc = device.createCommandEncoder();

    // Pass 1: HDR Procedural Space
    const spacePass = enc.beginRenderPass({
      colorAttachments: [{
        view: this.gpu.hdrTexture.createView(),
        loadOp: 'clear',
        storeOp: 'store',
        clearValue: { r: 0.01, g: 0.015, b: 0.03, a: 1 },
      }],
    });
    spacePass.setPipeline(this.spacePipeline);
    spacePass.setBindGroup(0, this.spaceBindGroup);
    spacePass.draw(3);
    spacePass.end();

    // Pass 1b: 3D Discovery Space Station & Glowing Orbital Slalom Rings (when not in warp tunnel)
    if (orbital && jumpProgress <= 0.001) {
      const spaceProj = perspectiveMatrix(fovRad, aspect, 1.0, 4000.0);
      const spaceView = viewMatrixFromBasis(right, up, forward);
      const spaceVP = mulMat4(spaceProj, spaceView);
      const wu = this.worldPropsUniformData;
      wu.set(spaceVP, 0);
      wu.set([ship.position.x, ship.position.y, ship.position.z, timeSec], 16);
      wu.set([starDirWorld.x, starDirWorld.y, starDirWorld.z, 0.0], 20); // 0 fog in space!
      wu.set([system.starColor[0], system.starColor[1], system.starColor[2], 1.0], 24);
      wu.set([system.nebulaPrimary[0], system.nebulaPrimary[1], system.nebulaPrimary[2], 0], 28);
      wu.set([1, 1, 1, 0], 32);
      wu.set([1, 1, 1, 0], 36);
      device.queue.writeBuffer(this.worldPropsUniformBuf, 0, wu);

      this.stationInstData.set([
        orbital.stationPos.x, orbital.stationPos.y, orbital.stationPos.z, 1.0,
        0, 8, 0, 0,
      ]);
      device.queue.writeBuffer(this.stationInstBuf, 0, this.stationInstData);

      let activeRings = 0;
      for (const r of orbital.rings) {
        if (r.passed) continue;
        this.slalomInstData.set([r.position.x, r.position.y, r.position.z, 1.0, r.yaw, 4, r.index, 0], activeRings * 8);
        activeRings++;
      }
      if (activeRings > 0) {
        device.queue.writeBuffer(this.slalomInstBuf, 0, this.slalomInstData.subarray(0, activeRings * 8));
      }

      const orbPass = enc.beginRenderPass({
        colorAttachments: [{
          view: this.gpu.hdrTexture.createView(),
          loadOp: 'load',
          storeOp: 'store',
        }],
        depthStencilAttachment: {
          view: this.gpu.depthTexture.createView(),
          depthLoadOp: 'clear',
          depthStoreOp: 'store',
          depthClearValue: 1.0,
        },
      });
      orbPass.setPipeline(this.worldPropsPipeline);
      orbPass.setBindGroup(0, this.worldPropsBindGroup);
      orbPass.setVertexBuffer(0, this.stationMesh.vertexBuf);
      orbPass.setVertexBuffer(1, this.stationInstBuf);
      orbPass.setIndexBuffer(this.stationMesh.indexBuf, 'uint16');
      orbPass.drawIndexed(this.stationMesh.indexCount, 1);

      if (activeRings > 0) {
        orbPass.setVertexBuffer(0, this.slalomRingMesh.vertexBuf);
        orbPass.setVertexBuffer(1, this.slalomInstBuf);
        orbPass.setIndexBuffer(this.slalomRingMesh.indexBuf, 'uint16');
        orbPass.drawIndexed(this.slalomRingMesh.indexCount, activeRings);
      }
      orbPass.end();
    }

    // Pass 2: 3D Procedural Explorer Ship onto HDR target
    const shipPass = enc.beginRenderPass({
      colorAttachments: [{
        view: this.gpu.hdrTexture.createView(),
        loadOp: 'load',
        storeOp: 'store',
      }],
      depthStencilAttachment: {
        view: this.gpu.depthTexture.createView(),
        depthLoadOp: 'clear',
        depthStoreOp: 'store',
        depthClearValue: 1.0,
      },
    });
    shipPass.setPipeline(this.shipPipeline);
    shipPass.setBindGroup(0, this.shipBindGroup);
    shipPass.setVertexBuffer(0, this.shipVertexBuf);
    shipPass.setIndexBuffer(this.shipIndexBuf, 'uint16');
    shipPass.drawIndexed(this.shipIndexCount);
    shipPass.end();

    // Pass 3: AgX Filmic Tone Mapping + HDR Bloom to swapchain
    const swapView = this.gpu.context.getCurrentTexture().createView();
    const postPass = enc.beginRenderPass({
      colorAttachments: [{
        view: swapView,
        loadOp: 'clear',
        storeOp: 'store',
        clearValue: { r: 0, g: 0, b: 0, a: 1 },
      }],
    });
    postPass.setPipeline(this.postPipeline);
    postPass.setBindGroup(0, this.postBindGroup);
    postPass.draw(3);
    postPass.end();

    device.queue.submit([enc.finish()]);
  }

  private ensureSurfaceInstances(pf: PlanetFlightState, isEarth: boolean): void {
    const needRebuild =
      !this.cachedInstances ||
      this.cachedInstSeed !== pf.seed ||
      Math.hypot(pf.x - this.cachedInstances.centerX, pf.z - this.cachedInstances.centerZ) > 95;
    if (!needRebuild) return;

    const { device } = this.gpu;
    this.cachedInstSeed = pf.seed;
    const inst = spawnSurfaceInstances(pf.x, pf.z, pf.seed, pf.planet.biome, pf.seaLevel, isEarth);
    this.cachedInstances = inst;

    const makeInstBuf = (data: Float32Array<ArrayBuffer>, prev: GPUBuffer | null): GPUBuffer | null => {
      prev?.destroy();
      if (data.byteLength === 0) return null;
      const buf = device.createBuffer({
        size: data.byteLength,
        usage: GPUBufferUsage.VERTEX | GPUBufferUsage.COPY_DST,
      });
      device.queue.writeBuffer(buf, 0, data);
      return buf;
    };

    this.treeInstBuf = makeInstBuf(inst.treeData, this.treeInstBuf);
    this.lanternInstBuf = makeInstBuf(inst.lanternData, this.lanternInstBuf);
    this.spireInstBuf = makeInstBuf(inst.spireData, this.spireInstBuf);
    this.critterInstBuf = makeInstBuf(inst.critterData, this.critterInstBuf);
    this.flierInstBuf = makeInstBuf(inst.flierData, this.flierInstBuf);
    this.grassInstBuf = makeInstBuf(inst.grassData, this.grassInstBuf);
    this.fishInstBuf = makeInstBuf(inst.fishData, this.fishInstBuf);
    this.ruinInstBuf = makeInstBuf(inst.ruinData, this.ruinInstBuf);
    this.cityInstBuf = makeInstBuf(inst.cityData, this.cityInstBuf);
  }

  renderPlanet(
    system: StarSystem,
    pf: PlanetFlightState,
    timeSec: number,
    visualBank: number,
    visualPitch: number,
    boostAmount: number,
    camp: CampRecord | null = null,
  ): void {
    const { device, width, height } = this.gpu;
    const aspect = width / Math.max(1, height);
    const fovRad = (64 * Math.PI) / 180;
    const tanHalfFov = Math.tan(fovRad * 0.5);

    const isEarth = Boolean(system.ref.isHome && pf.planet.name === 'Earth');
    this.ensureSurfaceInstances(pf, isEarth);

    const cosY = Math.cos(pf.yaw), sinY = Math.sin(pf.yaw);
    const cosP = Math.cos(pf.pitch), sinP = Math.sin(pf.pitch);

    const forward = vec3(sinY * cosP, sinP, -cosY * cosP);
    const right = vec3(cosY, 0, sinY);
    const up = vec3(-sinY * sinP, cosP, cosY * sinP);

    const camY = (pf.onFoot || pf.inRover) ? pf.y + Math.sin(pf.walkBob) * (pf.inRover ? 0.08 : 0.14) : pf.y;
    const sunDir = v3Norm(vec3(Math.cos(pf.sunAngle), Math.sin(pf.sunAngle), -0.45));
    const seedOx = (pf.seed % 97) * 13.7;
    const seedOz = ((pf.seed >> 4) % 89) * 17.3;

    const pu = this.planetUniformData;
    pu.set([pf.x, camY, pf.z, timeSec], 0);
    pu.set([right.x, right.y, right.z, aspect], 4);
    pu.set([up.x, up.y, up.z, tanHalfFov], 8);
    pu.set([forward.x, forward.y, forward.z, pf.reentryHeat], 12);
    pu.set([sunDir.x, sunDir.y, sunDir.z, pf.seaLevel], 16);
    pu.set([
      pf.planet.atmosphereColor[0],
      pf.planet.atmosphereColor[1],
      pf.planet.atmosphereColor[2],
      BIOME_INDEX[pf.planet.biome],
    ], 20);
    pu.set([pf.planet.colorA[0], pf.planet.colorA[1], pf.planet.colorA[2], seedOx], 24);
    pu.set([pf.planet.colorB[0], pf.planet.colorB[1], pf.planet.colorB[2], seedOz], 28);
    pu.set([system.starColor[0], system.starColor[1], system.starColor[2], QUALITY_INDEX[this.gpu.quality]], 32);
    device.queue.writeBuffer(this.planetUniformBuf, 0, pu);

    // World props uniforms (exact near=0.5, far=2600.0 matching planet.wgsl frag_depth)
    const worldProj = perspectiveMatrix(fovRad, aspect, 0.5, 2600.0);
    const worldView = viewMatrixFromBasis(right, up, forward);
    const viewProj = mulMat4(worldProj, worldView);
    const dayFactor = Math.max(0, Math.min(1, (sunDir.y + 0.16) / 0.38));
    const fogDensity = pf.planet.biome === 'crater-moon' ? 0.00014 : 0.00052;

    const wu = this.worldPropsUniformData;
    wu.set(viewProj, 0);
    wu.set([pf.x, camY, pf.z, timeSec], 16);
    wu.set([sunDir.x, sunDir.y, sunDir.z, fogDensity], 20);
    wu.set([system.starColor[0], system.starColor[1], system.starColor[2], dayFactor], 24);
    wu.set([pf.planet.atmosphereColor[0], pf.planet.atmosphereColor[1], pf.planet.atmosphereColor[2], 0], 28);
    wu.set([pf.planet.colorA[0], pf.planet.colorA[1], pf.planet.colorA[2], 0], 32);
    wu.set([pf.planet.colorB[0], pf.planet.colorB[1], pf.planet.colorB[2], 0], 36);
    device.queue.writeBuffer(this.worldPropsUniformBuf, 0, wu);

    if (pf.onFoot || pf.inRover) {
      this.parkedShipData.set([
        pf.shipParkedX, pf.shipParkedY, pf.shipParkedZ, 1.85,
        -pf.shipParkedYaw, 4, 0, 0,
      ]);
      device.queue.writeBuffer(this.parkedShipInstBuf, 0, this.parkedShipData);
    }
    if (camp) {
      this.campInstData.set([camp.x, camp.y, camp.z, 1.0, 0.35, 4, 0, 0]);
      device.queue.writeBuffer(this.campInstBuf, 0, this.campInstData);
    }

    // 3D Explorer ship OR 6-Wheel Rover in view space (hidden while walking on foot)
    const proj = perspectiveMatrix(fovRad, aspect, 0.2, 100);
    const bob = pf.landed ? 0 : Math.sin(timeSec * 2.4) * 0.04;
    const model = pf.inRover
      ? modelMatrix(0, -1.78 + Math.sin(pf.walkBob) * 0.05, -5.6, 0.04, visualBank * 0.45, 0.72)
      : modelMatrix(0, (pf.landed ? -1.85 : -1.64) + bob, -7.6 - boostAmount * 0.55, visualPitch, visualBank, 0.78);
    const mvp = mulMat4(proj, model);

    const lx = sunDir.x * right.x + sunDir.y * right.y + sunDir.z * right.z;
    const ly = sunDir.x * up.x + sunDir.y * up.y + sunDir.z * up.z;
    const lz = -(sunDir.x * forward.x + sunDir.y * forward.y + sunDir.z * forward.z);

    const su = this.shipUniformData;
    su.set(mvp, 0);
    su.set(model, 16);
    su.set([lx, ly, lz, pf.landed ? 0 : boostAmount], 32);
    su.set([system.starColor[0], system.starColor[1], system.starColor[2], timeSec], 36);
    su.set([pf.planet.atmosphereColor[0], pf.planet.atmosphereColor[1], pf.planet.atmosphereColor[2], 0], 40);
    device.queue.writeBuffer(this.shipUniformBuf, 0, su);

    const enc = device.createCommandEncoder();

    // Pass 1: Raymarched Terrain, Sky, Clouds & Spectral Ocean + Depth Buffer
    const pPass = enc.beginRenderPass({
      colorAttachments: [{
        view: this.gpu.hdrTexture.createView(),
        loadOp: 'clear',
        storeOp: 'store',
        clearValue: { r: 0.05, g: 0.08, b: 0.16, a: 1 },
      }],
      depthStencilAttachment: {
        view: this.gpu.depthTexture.createView(),
        depthLoadOp: 'clear',
        depthStoreOp: 'store',
        depthClearValue: 1.0,
      },
    });
    pPass.setPipeline(this.planetPipeline);
    pPass.setBindGroup(0, this.planetBindGroup);
    pPass.draw(3);
    pPass.end();

    // Pass 2: GPU-Instanced 3D Flora, Lanterns, Spires, Hopping Critters & Parked Ship
    const inst = this.cachedInstances;
    if (inst) {
      const propsPass = enc.beginRenderPass({
        colorAttachments: [{
          view: this.gpu.hdrTexture.createView(),
          loadOp: 'load',
          storeOp: 'store',
        }],
        depthStencilAttachment: {
          view: this.gpu.depthTexture.createView(),
          depthLoadOp: 'load',
          depthStoreOp: 'store',
        },
      });
      propsPass.setPipeline(this.worldPropsPipeline);
      propsPass.setBindGroup(0, this.worldPropsBindGroup);

      const drawGroup = (mesh: GpuMesh, instBuf: GPUBuffer | null, count: number) => {
        if (!instBuf || count <= 0) return;
        propsPass.setVertexBuffer(0, mesh.vertexBuf);
        propsPass.setVertexBuffer(1, instBuf);
        propsPass.setIndexBuffer(mesh.indexBuf, 'uint16');
        propsPass.drawIndexed(mesh.indexCount, count);
      };

      drawGroup(this.treeMesh, this.treeInstBuf, inst.treeCount);
      drawGroup(this.lanternMesh, this.lanternInstBuf, inst.lanternCount);
      drawGroup(this.spireMesh, this.spireInstBuf, inst.spireCount);
      drawGroup(this.critterMesh, this.critterInstBuf, inst.critterCount);
      drawGroup(this.flierMesh, this.flierInstBuf, inst.flierCount);
      drawGroup(this.grassMesh, this.grassInstBuf, inst.grassCount);
      drawGroup(this.fishMesh, this.fishInstBuf, inst.fishCount);
      drawGroup(this.ruinMesh, this.ruinInstBuf, inst.ruinCount);
      drawGroup(this.cityMesh, this.cityInstBuf, inst.cityCount);

      if (pf.onFoot || pf.inRover) {
        propsPass.setVertexBuffer(0, this.shipVertexBuf);
        propsPass.setVertexBuffer(1, this.parkedShipInstBuf);
        propsPass.setIndexBuffer(this.shipIndexBuf, 'uint16');
        propsPass.drawIndexed(this.shipIndexCount, 1);
      }
      if (camp) {
        propsPass.setVertexBuffer(0, this.campMesh.vertexBuf);
        propsPass.setVertexBuffer(1, this.campInstBuf);
        propsPass.setIndexBuffer(this.campMesh.indexBuf, 'uint16');
        propsPass.drawIndexed(this.campMesh.indexCount, 1);
      }
      propsPass.end();
    }

    // Pass 3: View-space Starhopper (flying/landed) OR 6-Wheel Explorer Rover (driving)
    if (!pf.onFoot) {
      const shipPass = enc.beginRenderPass({
        colorAttachments: [{
          view: this.gpu.hdrTexture.createView(),
          loadOp: 'load',
          storeOp: 'store',
        }],
        depthStencilAttachment: {
          view: this.gpu.depthTexture.createView(),
          depthLoadOp: 'clear',
          depthStoreOp: 'store',
          depthClearValue: 1.0,
        },
      });
      shipPass.setPipeline(this.shipPipeline);
      shipPass.setBindGroup(0, this.shipBindGroup);
      if (pf.inRover) {
        shipPass.setVertexBuffer(0, this.roverMesh.vertexBuf);
        shipPass.setIndexBuffer(this.roverMesh.indexBuf, 'uint16');
        shipPass.drawIndexed(this.roverMesh.indexCount);
      } else {
        shipPass.setVertexBuffer(0, this.shipVertexBuf);
        shipPass.setIndexBuffer(this.shipIndexBuf, 'uint16');
        shipPass.drawIndexed(this.shipIndexCount);
      }
      shipPass.end();
    }

    // Pass 4: AgX Filmic Tone Mapping + HDR Bloom
    const swapView = this.gpu.context.getCurrentTexture().createView();
    const postPass = enc.beginRenderPass({
      colorAttachments: [{
        view: swapView,
        loadOp: 'clear',
        storeOp: 'store',
        clearValue: { r: 0, g: 0, b: 0, a: 1 },
      }],
    });
    postPass.setPipeline(this.postPipeline);
    postPass.setBindGroup(0, this.postBindGroup);
    postPass.draw(3);
    postPass.end();

    device.queue.submit([enc.finish()]);
  }
}
