// Curio Class Worker: everything is static assets, except the pictures, which live in the R2 bucket curioclass-media
// (the 20,000-file limit on static assets, docs/ROADMAP.md). URLs stay the same; the R2 key is the path under dist/.
// scripts/sync_media.py uploads new pictures before a deploy; build_site.py writes dist/.assetsignore so they skip the asset upload.
const MEDIA = /^\/((?:library\/[^/]+\/art\/[^/]+\.jpg)|(?:modules\/[^/]+\/words\/art\/[^/]+\.webp))$/;

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    let path;
    try { path = decodeURIComponent(url.pathname); } catch { path = url.pathname; }
    const m = MEDIA.exec(path);
    if (!m || !['GET', 'HEAD'].includes(request.method)) return env.ASSETS.fetch(request);

    const cache = caches.default;
    const key = new Request(url.origin + url.pathname, { method: 'GET' });
    let res = await cache.match(key);
    if (!res) {
      const obj = await env.MEDIA.get(m[1]);
      if (!obj) return env.ASSETS.fetch(request);  // not in R2: the asset 404 page
      const headers = new Headers();
      obj.writeHttpMetadata(headers);
      headers.set('etag', obj.httpEtag);
      headers.set('cache-control', 'public, max-age=604800');
      res = new Response(obj.body, { headers });
      ctx.waitUntil(cache.put(key, res.clone()));
    }
    if (request.headers.get('if-none-match') && request.headers.get('if-none-match') === res.headers.get('etag'))
      return new Response(null, { status: 304, headers: res.headers });
    return request.method === 'HEAD' ? new Response(null, { headers: res.headers }) : res;
  },
};
