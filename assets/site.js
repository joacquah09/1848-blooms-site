/* 1848 Blooms & Designs, v2 behaviour. No dependencies. */
(function () {
  'use strict';

  /* ---- Form delivery ------------------------------------------------------
     Set FORM_ENDPOINT to a form service URL (for example a Formspree endpoint
     like "https://formspree.io/f/xxxxxxx") and both forms will send their
     answers there as JSON. While it is empty, the forms run in preview mode:
     nothing is sent, and a notice tells the visitor so. */
  var FORM_ENDPOINT = 'https://formsubmit.co/ajax/ireneacquah@1848bloomsanddesigns.com';
  /* Copies of every submission also go to these addresses. */
  var FORM_TO = FORM_ENDPOINT.split('/').pop();
  var FORM_CC = 'jonasacquah@1848bloomsanddesigns.com';

  var doc = document, body = doc.body;
  var $ = function (s, c) { return (c || doc).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || doc).querySelectorAll(s)); };
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var clamp = function (v, a, b) { return Math.max(a, Math.min(b, v)); };

  /* ---- Header ---- */
  var header = $('.hd');
  function onHeader() { if (header) header.classList.toggle('is-scrolled', window.scrollY > 30); }

  /* ---- Full-screen menu ---- */
  var btn = $('.menu-btn'), mnav = $('.mnav');
  function setMenu(open) {
    body.classList.toggle('menu-open', open);
    btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    $('span', btn).textContent = open ? 'Close' : 'Menu';
    if (open) { mnav.querySelector('a').focus({ preventScroll: true }); }
  }
  window.addEventListener('resize', function () { if (window.innerWidth > 900 && body.classList.contains('menu-open')) setMenu(false); });
  if (btn && mnav) {
    btn.addEventListener('click', function () { setMenu(!body.classList.contains('menu-open')); });
    $$('a', mnav).forEach(function (a) { a.addEventListener('click', function () { setMenu(false); }); });
    doc.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && body.classList.contains('menu-open')) { setMenu(false); btn.focus(); }
    });
  }

  /* ---- Scroll-filled titles: letters fade in as the title crosses the screen ---- */
  var titles = $$('.rv');
  titles.forEach(function (el) {
    var text = el.textContent.replace(/\s+/g, ' ').trim();
    el.setAttribute('aria-label', text);
    el.textContent = '';
    text.split(' ').forEach(function (word, i, arr) {
      var w = doc.createElement('span');
      w.className = 'w'; w.setAttribute('aria-hidden', 'true');
      word.split('').forEach(function (c) {
        var s = doc.createElement('span'); s.className = 'ch'; s.textContent = c; w.appendChild(s);
      });
      el.appendChild(w);
      if (i < arr.length - 1) el.appendChild(doc.createTextNode(' '));
    });
    el._chars = $$('.ch', el);
  });
  function paintTitles() {
    var vh = window.innerHeight;
    titles.forEach(function (el) {
      var r = el.getBoundingClientRect();
      var p = reduce ? 1 : clamp((vh * 0.92 - r.top) / (vh * 0.5), 0, 1);
      var n = el._chars.length, k = p * (n + 10);
      el._chars.forEach(function (c, i) { c.style.opacity = (0.14 + 0.86 * clamp((k - i) / 10, 0, 1)).toFixed(3); });
    });
  }

  /* ---- Fan of photo prints ---- */
  var fans = $$('.fan');
  function paintFans() {
    var vh = window.innerHeight;
    fans.forEach(function (f) {
      var r = f.getBoundingClientRect();
      var p = reduce ? 1 : clamp((vh * 0.95 - r.top) / (vh * 0.55), 0, 1);
      f.style.setProperty('--p', (0.08 + 0.92 * p).toFixed(3));
    });
  }

  var ticking = false;
  function onScroll() {
    onHeader();
    if (ticking) return;
    ticking = true;
    requestAnimationFrame(function () { paintTitles(); paintFans(); ticking = false; });
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  window.addEventListener('resize', onScroll);
  onHeader(); paintTitles(); paintFans();

  /* ---- Photo rail: previous / next ---- */
  $$('[data-rail]').forEach(function (rail) {
    var wrap = rail.parentNode;
    var step = function (d) { var f = $('figure', rail); rail.scrollBy({ left: d * (f.getBoundingClientRect().width + 20), behavior: reduce ? 'auto' : 'smooth' }); };
    var pv = $('[data-prev]', wrap), nx = $('[data-next]', wrap);
    if (pv) pv.addEventListener('click', function () { step(-1); });
    if (nx) nx.addEventListener('click', function () { step(1); });
  });


  /* ---- ?debug overlay: shows which font the headings actually use ---- */
  if (/[?&]debug/.test(location.search)) {
    var h = $('h1') || $('h2'), cs = h && getComputedStyle(h);
    var box = doc.createElement('pre');
    box.style.cssText = 'position:fixed;z-index:999;left:8px;bottom:8px;right:8px;background:#fff;color:#000;font:12px/1.4 monospace;padding:10px;border:2px solid red;white-space:pre-wrap';
    var fs = []; doc.fonts.forEach(function (f) { fs.push(f.family + ' ' + f.weight + ' ' + f.style + ' ' + f.status); });
    box.textContent = 'h1 family: ' + (cs && cs.fontFamily) + '\nh1 weight: ' + (cs && cs.fontWeight) + '\nh1 size: ' + (cs && cs.fontSize) + '\nurl: ' + location.href + '\nfonts: ' + fs.join(' | ') + '\ncss rules: ' + (doc.styleSheets.length) + ' sheet(s)';
    body.appendChild(box);
    doc.fonts.ready.then(function () { var f2 = []; doc.fonts.forEach(function (f) { f2.push(f.family + ' ' + f.weight + ' ' + f.status); }); box.textContent = box.textContent.replace(/fonts: .*/, 'fonts: ' + f2.join(' | ')); });
  }

  /* ---- Year ---- */
  $$('[data-year]').forEach(function (n) { n.textContent = new Date().getFullYear(); });

  /* ---- Portfolio filters + lightbox ---- */
  var gallery = $('.gallery');
  if (gallery) {
    var shots = $$('.shot', gallery);
    var fbtns = $$('.filters button');
    fbtns.forEach(function (b) {
      b.addEventListener('click', function () {
        var f = b.getAttribute('data-filter');
        fbtns.forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
        shots.forEach(function (s) {
          s.hidden = !(f === 'all' || (s.getAttribute('data-cat') || '').split(' ').indexOf(f) > -1);
        });
        if (history.replaceState) history.replaceState(null, '', f === 'all' ? location.pathname : '#' + f);
      });
    });
    var hash = location.hash.replace('#', '');
    var start = fbtns.filter(function (b) { return b.getAttribute('data-filter') === hash; })[0];
    if (start) start.click();

    var lb = $('#lightbox');
    var lbImg = $('img', lb), lbCap = $('.lb__cap', lb);
    var idx = 0;
    var visible = function () { return shots.filter(function (s) { return !s.hidden; }); };
    var show = function (i) {
      var list = visible();
      if (!list.length) return;
      idx = (i + list.length) % list.length;
      var im = $('img', list[idx]);
      lbImg.src = im.getAttribute('data-full') || im.src;
      lbImg.alt = im.alt;
      lbCap.textContent = im.alt;
    };
    shots.forEach(function (s) {
      s.addEventListener('click', function () {
        show(visible().indexOf(s));
        if (typeof lb.showModal === 'function') lb.showModal(); else lb.setAttribute('open', '');
      });
    });
    $('.pv', lb).addEventListener('click', function () { show(idx - 1); });
    $('.nx', lb).addEventListener('click', function () { show(idx + 1); });
    $('.x', lb).addEventListener('click', function () { lb.close(); });
    lb.addEventListener('click', function (e) { if (e.target === lb || e.target.classList.contains('lb__in')) lb.close(); });
    lb.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowLeft') show(idx - 1);
      if (e.key === 'ArrowRight') show(idx + 1);
    });
  }

  /* ---- Forms ---- */
  var form = $('form[data-form]');
  if (form) {
    var type = form.getAttribute('data-form'); // inquiry | reservation
    var notice = $('.notice', form);

    var qs = new URLSearchParams(location.search);
    var pre = qs.get('experience');
    if (pre) {
      var radio = $('input[name="experience"][value="' + pre + '"]', form);
      if (radio) radio.checked = true;
    }

    /* reservation form: show the field that matches the chosen experience */
    var shows = $$('[data-show]', form);
    if (shows.length) {
      var sync = function () {
        var c = $('input[name="experience"]:checked', form);
        var v = c ? c.value : '';
        shows.forEach(function (f) {
          var on = f.getAttribute('data-show') === v;
          f.hidden = !on;
          var i = $('input,select', f);
          if (i) i.required = on;
        });
      };
      var item = qs.get('item');
      if (item) {
        shows.forEach(function (f) {
          var s = $('select', f);
          if (s && $('option[value="' + item + '"]', s)) s.value = item;
        });
      }
      $$('input[name="experience"]', form).forEach(function (r) { r.addEventListener('change', sync); });
      sync();
    }

    var validate = function () {
      var ok = true, first = null;
      $$('.field', form).forEach(function (f) {
        var inp = $('input,select,textarea', f);
        if (!inp || !inp.required) return;
        var bad;
        if (inp.type === 'radio' || inp.type === 'checkbox') {
          bad = !$$('input[name="' + inp.name + '"]', f).some(function (r) { return r.checked; });
        } else {
          bad = !inp.value.trim() || (inp.type === 'email' && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(inp.value));
        }
        f.classList.toggle('invalid', bad);
        if (bad) { ok = false; if (!first) first = inp; }
      });
      if (first) first.focus();
      return ok;
    };

    var go = function () {
      var name = (form.elements.name && form.elements.name.value || '').trim().split(' ')[0];
      var p = new URLSearchParams({ type: type });
      if (name) p.set('name', name);
      location.href = 'thank-you.html?' + p.toString();
    };

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (form.elements.website && form.elements.website.value) return; // honeypot
      if (!validate()) return;

      if (FORM_ENDPOINT) {
        var data = {};
        new FormData(form).forEach(function (v, k) { data[k] = (k in data) ? data[k] + ', ' + v : v; });
        delete data.website;
        data._subject = type === 'reservation' ? 'New reservation request from the website' : type === 'wedding' ? 'New wedding & event inquiry from the website' : 'New inquiry from the website';
        data._template = 'table';
        if (FORM_CC) data._cc = FORM_CC;
        if (data.email) data._replyto = data.email;
        var b = $('button[type=submit]', form);
        b.disabled = true; b.textContent = 'Sending';
        fetch(FORM_ENDPOINT, { method: 'POST', headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' }, body: JSON.stringify(data) })
          .then(function (r) { return r.json().catch(function () { return {}; }).then(function (j) { j = j || {}; j._ok = r.ok; return j; }); })
          .then(function (j) {
            if (j._ok && !(j.success === false || j.success === 'false')) { go(); return; }
            var err = new Error(j.message || 'send failed'); err.reply = j; throw err;
          })
          .catch(function (err) {
            if (window.console) console.warn('Form service reply:', err && err.reply ? err.reply : err);
            b.disabled = false; b.textContent = type === 'reservation' ? 'Reserve my spot' : type === 'wedding' ? 'Send my inquiry' : 'Send';
            var msg = String(err && err.message || '');
            var mail = '<a class="link" href="mailto:' + FORM_TO + '">' + FORM_TO + '</a>';
            notice.innerHTML = /activat/i.test(msg)
              ? 'Almost there: this form is still being switched on, so your message was not delivered yet. Please email us at ' + mail + ' in the meantime.'
              : 'Your message did not send. Please try again in a moment, or email us at ' + mail + '.';
            notice.classList.add('on');
          });
      } else {
        notice.innerHTML = 'Preview mode: this form is not connected to email yet, so nothing was sent. ';
        var c = doc.createElement('a');
        c.href = '#'; c.className = 'link'; c.textContent = 'Continue to the thank-you page';
        c.addEventListener('click', function (ev) { ev.preventDefault(); go(); });
        notice.appendChild(c);
        notice.classList.add('on');
        notice.scrollIntoView({ block: 'center', behavior: reduce ? 'auto' : 'smooth' });
      }
    });

    $$('input,select,textarea', form).forEach(function (i) {
      i.addEventListener('input', function () { var f = i.closest('.field'); if (f) f.classList.remove('invalid'); });
    });
  }

  /* ---- Thank-you page ---- */
  var ty = $('[data-thanks]');
  if (ty) {
    var q = new URLSearchParams(location.search);
    var nm = q.get('name');
    var t = ({ reservation: 1, wedding: 1 })[q.get('type')] ? q.get('type') : 'inquiry';
    var h = $('[data-ty-title]', ty);
    h.textContent = nm ? 'Thank you, ' + nm : 'Thank you';
    $$('[data-ty]', ty).forEach(function (n) { n.hidden = n.getAttribute('data-ty') !== t; });
  }
})();

/* review cards: show "Read more" only when the quote is clamped */
(function () {
  var cards = document.querySelectorAll('.rev .rc');
  if (!cards.length) return;
  function check() {
    cards.forEach(function (c) {
      var q = c.querySelector('blockquote'), b = c.querySelector('.more');
      if (!q || !b || c.classList.contains('is-open')) return;
      b.hidden = q.scrollHeight <= q.clientHeight + 2;
    });
  }
  cards.forEach(function (c) {
    var b = c.querySelector('.more');
    if (!b) return;
    b.addEventListener('click', function () {
      var open = c.classList.toggle('is-open');
      b.textContent = open ? 'Show less' : 'Read more';
      b.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  });
  check();
  window.addEventListener('resize', check);
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(check);
})();
