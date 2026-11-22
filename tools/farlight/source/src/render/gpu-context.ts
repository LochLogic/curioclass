export type QualityTier = 'performance' | 'high' | 'ultra';

export interface GpuContext {
  adapter: GPUAdapter;
  device: GPUDevice;
  canvas: HTMLCanvasElement;
  context: GPUCanvasContext;
  format: GPUTextureFormat;
  hdrTexture: GPUTexture;
  depthTexture: GPUTexture;
  width: number;
  height: number;
  quality: QualityTier;
  resize(quality?: QualityTier): void;
}

const QUALITY_SCALE: Record<QualityTier, number> = {
  performance: 0.75,
  high: 1.0,
  ultra: Math.min(window.devicePixelRatio || 1, 2.0),
};

export async function initWebGpu(canvas: HTMLCanvasElement): Promise<GpuContext> {
  if (!navigator.gpu) {
    throw new Error('This browser does not have WebGPU, which Farlight needs to draw the galaxy. A recent browser on most computers has it; try another browser or device.');
  }
  const adapter = await navigator.gpu.requestAdapter({ powerPreference: 'high-performance' });
  if (!adapter) {
    throw new Error('Could not find a compatible WebGPU graphics adapter.');
  }
  const device = await adapter.requestDevice();
  const context = canvas.getContext('webgpu');
  if (!context) {
    throw new Error('Could not initialize WebGPU canvas context.');
  }

  const format = navigator.gpu.getPreferredCanvasFormat();
  context.configure({ device, format, alphaMode: 'opaque' });

  let quality: QualityTier = 'high';
  let width = 1;
  let height = 1;
  let hdrTexture!: GPUTexture;
  let depthTexture!: GPUTexture;

  const createTargets = () => {
    const scale = QUALITY_SCALE[quality];
    width = Math.max(1, Math.floor(window.innerWidth * scale));
    height = Math.max(1, Math.floor(window.innerHeight * scale));
    canvas.width = width;
    canvas.height = height;

    hdrTexture?.destroy();
    depthTexture?.destroy();

    hdrTexture = device.createTexture({
      size: { width, height },
      format: 'rgba16float',
      usage: GPUTextureUsage.RENDER_ATTACHMENT | GPUTextureUsage.TEXTURE_BINDING,
    });
    depthTexture = device.createTexture({
      size: { width, height },
      format: 'depth24plus',
      usage: GPUTextureUsage.RENDER_ATTACHMENT,
    });
  };

  createTargets();

  const ctx: GpuContext = {
    adapter,
    device,
    canvas,
    context,
    format,
    get hdrTexture() { return hdrTexture; },
    get depthTexture() { return depthTexture; },
    get width() { return width; },
    get height() { return height; },
    get quality() { return quality; },
    set quality(q: QualityTier) { quality = q; },
    resize(nextQuality?: QualityTier) {
      if (nextQuality) quality = nextQuality;
      createTargets();
    },
  };

  return ctx;
}
