// Curio Class Worker: everything is static assets, except the pictures, which live in the R2 bucket curioclass-media
// (the 20,000-file limit on static assets, docs/ROADMAP.md). URLs stay the same; the R2 key is the path under dist/.
// scripts/sync_media.py uploads new pictures before a deploy; build_site.py writes dist/.assetsignore so they skip the asset upload.
const MEDIA = /^\/((?:library\/[^/]+\/art\/[^/]+\.jpg)|(?:modules\/[^/]+\/words\/art\/[^/]+\.webp))$/;

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    let path;
    try { path = decodeURIComponent(url.pathname); } catch { path = url.pathname; }
    if (path === '/api/message') return message(request, env);
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

// Messages from the home page banner. Stored: the message, its kind, who they are (optional), an email (optional) and
// the date. Never the IP address or device details. The rate limit key is used to count and is not stored.
const KINDS = ['broken', 'feedback', 'idea', 'hello'];
const ROLES = ['', 'teacher', 'parent', 'student', 'other'];
const DAILY_CAP = 500;

function reply(status, body) {
  return new Response(JSON.stringify(body), {
    status,
    headers: { 'content-type': 'application/json', 'cache-control': 'no-store' },
  });
}

async function message(request, env) {
  if (request.method !== 'POST') return reply(405, { ok: false, error: 'Send with POST.' });
  if (new URL(request.url).origin !== request.headers.get('origin')) return reply(403, { ok: false, error: 'Wrong origin.' });
  const who = request.headers.get('cf-connecting-ip') || 'unknown';
  const { success } = await env.MSG_LIMIT.limit({ key: who });
  if (!success) return reply(429, { ok: false, error: 'That is a lot of messages at once. Please wait a minute.' });
  let d;
  try { d = await request.json(); } catch { return reply(400, { ok: false, error: 'That did not arrive in one piece.' }); }
  if (d.website) return reply(200, { ok: true });  // the hidden trap field: only robots fill it in
  const text = String(d.message || '').trim();
  const kind = KINDS.includes(d.kind) ? d.kind : 'feedback';
  const role = ROLES.includes(d.role) ? d.role : '';
  const email = String(d.email || '').trim();
  const page = String(d.page || '').slice(0, 200);
  if (text.length < 2) return reply(400, { ok: false, error: 'Write a message first.' });
  if (text.length > 2000) return reply(400, { ok: false, error: 'Please keep it under 2,000 characters.' });
  if (email && (email.length > 200 || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)))
    return reply(400, { ok: false, error: 'That email does not look right. You can leave it empty.' });
  const today = new Date().toISOString().slice(0, 10);
  const row = await env.MSG.prepare('SELECT COUNT(*) AS n FROM messages WHERE created >= ?').bind(today).first();
  if (row && row.n >= DAILY_CAP) return reply(503, { ok: false, error: 'The mailbox is full for today. Please try tomorrow.' });
  await env.MSG.prepare('INSERT INTO messages (created, kind, role, message, email, page) VALUES (?, ?, ?, ?, ?, ?)')
    .bind(new Date().toISOString(), kind, role, text, email, page).run();
  return reply(200, { ok: true });
}
