(function () {
  var r = document.getElementById('reader');
  if (!r) return;
  var text = r.querySelector('.story-text'), pager = r.querySelector('.pager'), at = r.querySelector('.pager-at');
  var KEY = 'curio-reader', prefs = { size: 20, font: 'serif', theme: 'paper', view: 'scroll' }, page = 0;
  try { Object.assign(prefs, JSON.parse(localStorage.getItem(KEY)) || {}); } catch (e) {}

  function save() { try { localStorage.setItem(KEY, JSON.stringify(prefs)); } catch (e) {} }

  // Pages view: wrap the text's blocks into pages of about a screenful, sized to the current font.
  function paginate() {
    var kids = Array.prototype.slice.call(text.querySelectorAll(':scope > .r-page > *, :scope > *:not(.r-page)'));
    text.innerHTML = '';
    var budget = Math.round(2600 / prefs.size * 10), cur = null, words = 0;
    kids.forEach(function (el) {
      var w = (el.textContent.match(/\S+/g) || []).length + (el.tagName === 'IMG' || el.querySelector('img') ? 60 : 0);
      if (!cur || (words + w > budget && words > 0) || (el.tagName === 'H2' && words > 0) || el.tagName === 'HR') {
        cur = document.createElement('div');
        cur.className = 'r-page';
        text.appendChild(cur);
        words = 0;
        if (el.tagName === 'HR') return;
      }
      cur.appendChild(el);
      words += w;
    });
    page = Math.min(page, text.children.length - 1);
    show();
  }

  function show() {
    var pages = text.children;
    for (var i = 0; i < pages.length; i++) pages[i].classList.toggle('on', i === page);
    at.textContent = 'Page ' + (page + 1) + ' of ' + pages.length;
    r.querySelector('[data-act="prev"]').disabled = page === 0;
    r.querySelector('[data-act="next"]').disabled = page >= pages.length - 1;
  }

  function apply() {
    r.style.setProperty('--size', prefs.size + 'px');
    r.dataset.font = prefs.font;
    r.dataset.theme = prefs.theme;
    r.dataset.view = prefs.view;
    r.querySelectorAll('[data-set]').forEach(function (b) {
      b.setAttribute('aria-pressed', String(prefs[b.dataset.set] === b.dataset.val));
    });
    pager.hidden = prefs.view !== 'pages';
    paginate();
  }

  function turn(d) {
    var n = Math.max(0, Math.min(text.children.length - 1, page + d));
    if (n === page) return;
    page = n;
    show();
    r.scrollIntoView({ block: 'start', behavior: 'smooth' });
  }

  r.addEventListener('click', function (e) {
    var b = e.target.closest('button');
    if (!b) return;
    if (b.classList.contains('gloss')) {
      var open = b.querySelector('.gloss-pop');
      r.querySelectorAll('.gloss-pop').forEach(function (p) { p.parentNode.setAttribute('aria-expanded', 'false'); p.remove(); });
      if (!open) {
        var pop = document.createElement('span');
        pop.className = 'gloss-pop';
        pop.setAttribute('role', 'tooltip');
        pop.textContent = b.dataset.gloss;
        b.appendChild(pop);
        b.setAttribute('aria-expanded', 'true');
      }
      return;
    }
    if (b.dataset.set) { prefs[b.dataset.set] = b.dataset.val; save(); apply(); return; }
    var act = b.dataset.act;
    if (act === 'bigger' || act === 'smaller') { prefs.size = Math.max(14, Math.min(40, prefs.size + (act === 'bigger' ? 2 : -2))); save(); apply(); }
    if (act === 'print') window.print();
    if (act === 'prev') turn(-1);
    if (act === 'next') turn(1);
  });
  document.addEventListener('keydown', function (e) {
    if (prefs.view !== 'pages' || /INPUT|TEXTAREA|SELECT/.test(e.target.tagName)) return;
    if (e.key === 'ArrowRight') turn(1);
    if (e.key === 'ArrowLeft') turn(-1);
  });
  r.querySelectorAll('.gloss').forEach(function (g) { g.setAttribute('aria-expanded', 'false'); });
  apply();
})();
