#!/usr/bin/env python3
"""Generates the v2 static pages for 1848 Blooms & Designs into /home/claude/v3/site."""
import os, html
from PIL import Image

OUT = os.path.dirname(os.path.abspath(__file__))
IMG = OUT + '/assets/img'
SITE = '1848 Blooms & Designs'
WED_ATTR = 'href="wedding.html" data-wm-open'
EMAIL = 'ireneacquah@1848bloomsanddesigns.com'
AREA = 'Delaware, Pennsylvania &amp; Beyond'
_d = {}


def dims(n):
    if n not in _d:
        with Image.open(f'{IMG}/{n}.jpg') as i:
            _d[n] = i.size
    return _d[n]


def im(n, alt, cls='', eager=False, extra=''):
    w, h = dims(n)
    load = 'fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
    c = f' class="{cls}"' if cls else ''
    return f'<img{c} src="assets/img/{n}.jpg" width="{w}" height="{h}" alt="{html.escape(alt)}" {load} {extra}>'


def ratio(n):
    w, h = dims(n)
    return round(w / h, 3)



NAV = [('index.html','Home'),('about.html','About'),('services.html','Services'),('floral-bar.html','Floral Bar'),
       ('portfolio.html','Portfolio'),('experiences.html','Experiences'),('contact.html','Contact')]
MNAV = [('index.html','Home'),('about.html','About'),('designer.html','Meet the designer'),('services.html','Services'),('floral-bar.html','Floral Bar'),('portfolio.html','Portfolio'),('experiences.html','Experiences'),('reserve.html','Reserve your spot'),('contact.html','Contact')]
LOGO = '<a class="brand" href="index.html" aria-label="1848 Blooms &amp; Designs, home"><img src="assets/logo.png" width="86" height="76" alt="1848 Blooms &amp; Designs"></a>'
SOC = ('<span class="social">'
              '<a href="https://www.instagram.com/1848BloomsandDesigns" target="_blank" rel="noopener" aria-label="Instagram"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><rect x="3.500" y="3.500" width="17" height="17" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.200" cy="6.800" r=".6" fill="currentColor"/></svg></a>'
       '<a href="https://www.facebook.com/1848BloomsandDesigns" target="_blank" rel="noopener" aria-label="Facebook"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M13.500 21v-7.500h2.500l.4-3h-2.900V8.600c0-.9.3-1.500 1.500-1.500h1.500V4.400c-.3 0-1.200-.1-2.200-.1-2.200 0-3.700 1.300-3.700 3.800v2.400H7.800v3h2.800V21h2.900z"/></svg></a>'
       '<a href="https://www.tiktok.com/@1848bloomsanddesigns" target="_blank" rel="noopener" aria-label="TikTok"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12.53.02c1.31-.02 2.61-.01 3.91-.02.08 1.53.63 3.09 1.75 4.17 1.12 1.11 2.7 1.62 4.24 1.79v4.03c-1.44-.05-2.89-.35-4.2-.97-.57-.26-1.1-.59-1.62-.93-.01 2.92.01 5.84-.02 8.75-.08 1.4-.54 2.79-1.35 3.94-1.31 1.92-3.58 3.17-5.91 3.21-1.43.08-2.86-.31-4.08-1.03-2.02-1.19-3.44-3.37-3.65-5.71-.02-.5-.03-1-.01-1.49.18-1.9 1.12-3.72 2.58-4.96 1.66-1.44 3.98-2.13 6.15-1.72.02 1.48-.04 2.96-.04 4.44-.99-.32-2.15-.23-3.02.37-.63.41-1.11 1.04-1.36 1.75-.21.51-.15 1.07-.14 1.61.24 1.64 1.82 3.02 3.5 2.87 1.12-.01 2.19-.66 2.77-1.61.19-.33.4-.67.41-1.06.1-1.79.06-3.57.07-5.36.01-4.03-.01-8.05.02-12.07z"/></svg></a>'
       '<a href="https://www.linkedin.com/company/1848-blooms-and-designs/" target="_blank" rel="noopener" aria-label="LinkedIn"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20.45 20.45h-3.56v-5.57c0-1.33-.02-3.04-1.85-3.04-1.85 0-2.14 1.45-2.14 2.94v5.67H9.35V9h3.41v1.56h.05c.48-.9 1.64-1.85 3.37-1.85 3.6 0 4.27 2.37 4.27 5.46v6.28zM5.34 7.43a2.06 2.06 0 1 1 0-4.13 2.06 2.06 0 0 1 0 4.13zM7.12 20.45H3.56V9h3.56v11.45z"/></svg></a>'
       '</span>')


def header(cur):
    links = ''.join(f'<a href="{h}"' + (' aria-current="page"' if h == cur else '') + f'>{t}</a>' for h, t in NAV)
    m = ''.join(f'<li><a href="{h}">{t}</a></li>' for h, t in MNAV)
    return f'''<a class="skip" href="#main">Skip to content</a>
<header class="hd"><div class="hd__top">
  <p class="flank hd__tag">{AREA}<br>Florist</p>
  {LOGO}
  <div class="hd__right">{SOC}<a class="contact-link" href="contact.html">Contact</a>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="mnav"><i aria-hidden="true"></i><span>Menu</span></button></div>
</div></header>
<nav class="primary" aria-label="Main">{links}</nav>
<nav class="mnav" id="mnav" aria-label="Menu">
  <ul>{m}</ul>
  <div class="foot-line"><span>Serving {AREA}</span><span>Now booking 2027</span></div>
</nav>'''


def footer():
    thumbs = ''.join(im(n, a) for n, a in [('arch-willow','A wooden arch with white flowers'),('pastel-table-a','A pastel table with a tall arrangement'),('bouquet-ribbon','A pastel bouquet with a rust ribbon'),('bridesmaids','Bridesmaids holding bouquets'),('ladder-daisies','Daisies in a woven basket')])
    return f'''<footer class="site-footer">
  <div class="f-top">{LOGO}<div class="hd__right">{SOC}<a class="contact-link" href="contact.html">Contact</a></div></div>
  <div class="f-mid">
    <ul><li><a href="index.html">Home</a></li><li><a href="about.html">About</a></li><li><a href="designer.html">Meet the designer</a></li><li><a href="portfolio.html">Portfolio</a></li></ul>
    <ul><li><a href="services.html">Services</a></li><li><a href="floral-bar.html">Floral Bar</a></li><li><a href="experiences.html">Experiences</a></li><li><a href="reserve.html">Reserve your spot</a></li></ul>
    <div class="f-btns"><a class="btn" href="reserve.html">Reserve your spot</a><a class="btn" {WED_ATTR}>Wedding inquiry</a></div>
  </div>
  <div class="f-thumbs">{thumbs}</div>
  <div class="legal"><span>&copy; <span data-year>2026</span> 1848 Blooms &amp; Designs</span><span>Serving {AREA} &middot; Now booking 2027</span></div>
</footer>'''


def page(fname, title, desc, body, noindex=False, og='home-banner'):
    robots = '<meta name="robots" content="noindex">' if noindex else ''
    t = SITE if fname == 'index.html' else f'{title} | {SITE}'
    open(f'{OUT}/{fname}', 'w').write(f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(t)}</title>
<meta name="description" content="{html.escape(desc)}">
{robots}
<meta property="og:title" content="{html.escape(t)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:type" content="website">
<meta property="og:image" content="assets/img/{og}.jpg">
<meta name="theme-color" content="#C5A193">
<link rel="icon" type="image/png" href="assets/favicon.png">
<link rel="stylesheet" href="assets/site.css?v=21">
</head>
<body>
{header(fname)}
<main id="main">
{body}
</main>
{footer()}
{wedding_modal()}
<script src="assets/site.js?v=6"></script>
</body>
</html>
''')


# ---------- components ----------
# ---------- wedding & event inquiry pop-up (one copy on every page) ----------
def _opts(name, items, kind='radio', cls=''):
    return ''.join(f'<label class="{cls}"><input type="{kind}" name="{name}" value="{html.escape(o)}"><span>{html.escape(o)}</span></label>' for o in items)

def _step(n, kicker, title, desc, inner):
    return f"""<section class="wm__step" data-step="{n}"{' hidden' if n > 1 else ''}>
      <p class="wm__kicker">{kicker}</p>
      <h2 class="wm__title" tabindex="-1">{title}</h2>
      <p class="wm__desc">{desc}</p>
      <div class="wm__fields">{inner}</div>
    </section>"""

def wedding_modal():
    steps = [
        _step(1, 'Let&rsquo;s start with you', 'Welcome', 'We&rsquo;re honored you&rsquo;re considering 1848 Blooms &amp; Designs. We design refined, nature-inspired floral experiences for weddings and events. A few details so we know how to reach you.', """
        <div class="field"><label for="wm-name">Full name</label><input id="wm-name" name="name" autocomplete="name" required><p class="err">Enter your full name.</p></div>
        <div class="field"><label for="wm-email">Email address</label><input id="wm-email" name="email" type="email" autocomplete="email" required><p class="err">Enter a valid email address.</p></div>
        <div class="field"><label for="wm-phone">Phone number</label><input id="wm-phone" name="phone" type="tel" autocomplete="tel" required><p class="err">Enter your phone number.</p></div>"""),
        _step(2, 'Tell us about your event', 'Your event', 'This is where your vision begins to take shape.', f"""
        <fieldset class="field"><legend>Event type</legend><div class="wm-chips">{_opts('event_type', ['Wedding', 'Bridal Shower', 'Baby Shower', 'Dinner Party', 'Corporate Event', 'Other'])}</div><p class="err">Choose your event type.</p></fieldset>
        <div class="field"><label for="wm-date">Event date</label><input id="wm-date" name="event_date" type="date" required><p class="err">Choose your event date.</p></div>
        <div class="field"><label for="wm-venue">Event location (venue and city)</label><input id="wm-venue" name="event_location" placeholder="The Barn at Spring Brook, Kennett Square" required><p class="err">Enter the venue and city.</p></div>"""),
        _step(3, 'Your vision &amp; aesthetic', 'Your vision', 'Tell us how you picture the day.', """
        <div class="field"><label for="wm-words">Describe your event in a few words</label><textarea id="wm-words" name="event_description" rows="3" placeholder="Elegant, modern, romantic, minimal" required></textarea><p class="err">Give us a few words.</p></div>
        <div class="field"><label for="wm-colors">Color palette</label><input id="wm-colors" name="color_palette" placeholder="Blush, ivory and sage" required><p class="err">Share your color palette.</p></div>
        <div class="field" data-insp><label for="wm-link">Inspiration photos or Pinterest link</label><input id="wm-link" name="pinterest_link" type="url" inputmode="url" placeholder="Paste a Pinterest board or link">
          <label class="wm-file"><input type="file" name="attachment" accept="image/*" multiple><span>Or upload photos</span><em data-files>JPG or PNG, up to 5 MB each</em></label>
          <p class="err">Add a Pinterest link or upload at least one photo.</p></div>"""),
        _step(4, 'Floral elements', 'What are you dreaming of?', 'Select the floral elements you&rsquo;re interested in. Choose as many as you like.', f"""
        <fieldset class="field"><legend class="sr">Which floral elements are you considering?</legend><div class="wm-cards">{_opts('floral_elements', ['Bridal Bouquet', 'Centerpieces', 'Ceremony Florals', 'Floral Installations', 'Floral Bar Experience', 'Weekly / Corporate Florals'], 'checkbox')}</div><p class="err">Choose at least one.</p></fieldset>"""),
        _step(5, 'Your investment', 'Estimated floral budget', 'Understanding your investment range allows us to design intentionally and align with your vision.', f"""
        <fieldset class="field"><legend class="sr">Estimated floral budget</legend><div class="wm-cards wm-cards--2">{_opts('floral_budget', ['$500 to $1,000', '$1,000 to $2,500', '$2,500 to $5,000', '$5,000+'])}</div><p class="err">Choose a budget range.</p></fieldset>"""),
        _step(6, 'One final detail', 'The feeling', 'A final note to help us understand your vision more deeply.', """
        <div class="field"><label for="wm-feel">What feeling or experience do you want your florals to create?</label><textarea id="wm-feel" name="desired_feeling" rows="5" required></textarea><p class="err">Tell us a little about the feeling you want.</p></div>"""),
    ]
    return f"""<dialog class="wm" id="wm" aria-labelledby="wm-head">
  <div class="wm__panel">
    <div class="wm__art" aria-hidden="true">{im('bouquet-white-b', '', 'wm__img')}<p class="wm__quote">Refined, nature-inspired florals for weddings and events.</p></div>
    <form class="wm__form" data-wm novalidate>
      <div class="wm__top">
        <p class="wm__brand" id="wm-head">Wedding &amp; event inquiry</p>
        <button type="button" class="wm__x" data-wm-close aria-label="Close">&times;</button>
        <div class="wm__bar" role="progressbar" aria-valuemin="1" aria-valuemax="6" aria-valuenow="1"><i></i></div>
        <p class="wm__count" aria-live="polite">Step <b data-wm-n>1</b> of 6</p>
      </div>
      <div class="wm__body">
        {''.join(steps)}
        <section class="wm__step wm__done" data-step="done" hidden>
          <img src="assets/logo.png" width="86" height="76" alt="">
          <h2 class="wm__title" tabindex="-1">Thank you<span data-wm-who></span></h2>
          <p class="wm__desc">We received your inquiry. Irene will reply by email within 24 hours to set up a time to talk about your florals.</p>
          <button type="button" class="btn" data-wm-close>Close</button>
        </section>
      </div>
      <div class="hp" aria-hidden="true"><label>Leave this empty<input name="website" tabindex="-1" autocomplete="off"></label></div>
      <div class="wm__nav">
        <div class="notice" role="status"></div>
        <button type="button" class="wm__back" data-wm-back hidden>Back</button>
        <button type="submit" class="btn" data-wm-next>Next</button>
      </div>
    </form>
  </div>
</dialog>"""

def tbar(title, left, right, tag='h2', cls='dsp'):
    return f'<div class="tbar"><{tag} class="{cls}">{title}</{tag}></div>'


def phero(img, alt, title, left, right, lede, btn=None, plain=False):
    b = f'<div class="btn-row">{btn}</div>' if btn else ''
    bg = '' if plain else im(img, alt, 'phero__img', eager=True)
    cls = 'phero phero--plain' if plain else 'phero'
    eb = f'<span class="eyebrow">{left.replace("<br>", " ")} &middot; {right.replace("<br>", " ")}</span>'
    return f'''<section class="{cls}">
  {bg}
  <div class="phero__mid">{eb}{tbar(title, left, right, 'h1')}</div>
  <div class="phero__foot"><p>{lede}</p>{b}</div>
</section>'''


def closer(title='Let\u2019s design something unforgettable.', btn='Inquire now', href='contact.html', band='band-petal'):
    ext = ' target="_blank" rel="noopener"' if href.startswith('http') else ''
    return f'''<section class="section {band}"><div class="wrap closer">
  <h2 class="dsp">{title}</h2><div class="btn-row"><a class="btn btn--arrow" href="{html.escape(href)}"{ext}>{btn}</a></div>
</div></section>'''


# ================================================================== HOME
rail_imgs = ['table-window','bridesmaids','bouquet-bright','couple-window','pastel-table-a','arch-pampas','bouquet-chair','installation-hanging','tablescape-citrus','bouquet-ribbon']
rail_alt = {n:a for n,c,a in []}
RAIL = ''.join(f'<figure style="--ar:{round(dims(n)[0]/dims(n)[1],3)}">{im(n, n.replace("-"," ").capitalize()+" by 1848 Blooms & Designs")}</figure>' for n in rail_imgs)

home = f'''
<section class="hero">
  {im('home-banner', 'A long white table set with candles, glassware and a low arrangement of yellow, peach and white flowers beside a window', 'hero__img', eager=True)}
  <div class="hero__body">
    <span class="eyebrow">{AREA} &middot; Now booking 2027</span>
    <h1>Nature inspired garden style florals</h1>
    <div class="btn-row">
      <a class="btn btn--arrow" href="services.html">Weddings + events</a>
      <a class="btn btn--arrow" href="floral-bar.html">Floral Bar</a>
      <a class="btn btn--arrow" href="experiences.html">Experiences</a>
    </div>
  </div>
  <span class="scroll-cue" aria-hidden="true">Scroll to begin</span>
</section>

<section class="intro">
  <div class="wrap">
    <h2 class="dsp">Thoughtful design. Intentional details. Unforgettable moments.</h2>
    <span class="rule"></span>
    <p>We design florals for weddings, private events and hands-on gatherings. Each one starts with the room, the season and the people who will fill it, then gets built stem by stem.</p>
    <div class="btn-row"><a class="btn" href="services.html">Explore offerings</a></div>
  </div>
</section>

<section class="rail-wrap" aria-label="Recent work">
  <div class="rail" data-rail>{RAIL}</div>
  <div class="rail-ctl"><button type="button" class="prev" data-prev><i></i>Previous</button><button type="button" class="next" data-next>Next<i></i></button></div>
</section>

<section class="bio">
  <div class="bio__img">{im('designer-smile', 'The designer smiling in a beige apron, holding a bouquet of white, yellow and orange flowers')}</div>
  <div class="bio__card">
    <span class="eyebrow">Meet the designer</span>
    <h2 class="dsp">Irene Acquah</h2>
    <span class="rule"></span>
    <p>I am so glad you’re here. I’m Irene, lead designer of 1848 Blooms and Designs, where I pour my heart into creating beautiful nature inspired florals and arrangements.</p>
    <a class="arrow-link" href="designer.html">Learn more</a>
  </div>
</section>

<section class="feature">
  {im('table-long-pastel', 'A long white table set with pastel centerpieces and wishbone chairs in a bright room')}
  <div class="feature__card">
    <h2 class="dsp">Weddings + events</h2>
    <p>We take on a limited number of weddings and events each season so every client gets our full creative focus. Our full-service design covers every touchpoint, from personal flowers to installations, and we deliver and set up everything.</p>
    <a class="btn" href="services.html">View the details</a>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <h2 class="dsp" style="text-align:center">Floral experiences</h2>
    <p class="sec-intro">From hands-on workshops to private gatherings and the Floral Bar, our experiences are designed to inspire creativity, connection and a deeper appreciation for the beauty in everyday moments.</p>
    <div class="cards">
      <figure><a href="experiences.html"><div class="ph-img">{im('designing-table', 'A florist arranging yellow and white flowers at a table in a bright room', '', extra='style="object-position:70% 50%"')}</div><h3>Workshops</h3></a><figcaption><p>Learn a designer’s techniques in a small class and leave with your own arrangement.</p></figcaption></figure>
      <figure><a href="experiences.html"><div class="ph-img">{im('designer-making', 'A designer arranging flowers in white bowls at a wooden table', '', extra='style="object-position:30% 50%"')}</div><h3>Private gatherings</h3></a><figcaption><p>Bring the workshop to your group for a shower, a birthday or a team day.</p></figcaption></figure>
      <figure><a href="floral-bar.html"><div class="ph-img">{im('ladder-daisies', 'Daisies and cosmos in a woven basket at the foot of a wooden ladder')}</div><h3>The Floral Bar</h3></a><figcaption><p>A self-serve flower station for your event. Pick, arrange, take home.</p></figcaption></figure>
    </div>
    <div class="btn-row btn-row--center" style="margin-top:clamp(2.2rem,4vw,3.6rem)"><a class="btn" href="reserve.html">Reserve your spot</a></div>
  </div>
</section>

<section class="section band-paper2">
  <div class="wrap">
    <h2 class="dsp" style="text-align:center;margin-bottom:clamp(2rem,4vw,3.5rem)">Kind words</h2>
    <div class="rev">
      <figure class="rc"><span class="src">Google &middot; <span class="stars" aria-label="5 out of 5 stars">★★★★★</span></span><blockquote>Irene was fabulous to work with! She took my vision and made it come to life for our wedding day! She is willing to go above and beyond for ideas. My lavender, eucalyptus, and sage came together beautifully. I cannot express enough how amazing she was to work with. Thank you for taking my ideas and making them as beautiful as I could imagine.</blockquote><button type="button" class="more" hidden aria-expanded="false">Read more</button><cite>Danielle F.</cite></figure>
      <figure class="rc"><span class="src">Google &middot; <span class="stars" aria-label="5 out of 5 stars">★★★★★</span></span><blockquote>I was very happy with the flower arrangement. Blooms and Design was very professional and polite on the phone. Irene gets 5 Stars!</blockquote><button type="button" class="more" hidden aria-expanded="false">Read more</button><cite>Bill B.</cite></figure>
      <figure class="rc"><span class="src">Google &middot; <span class="stars" aria-label="5 out of 5 stars">★★★★★</span></span><blockquote>I used 1848 Blooms and design for my event and she awesome. Avery professional and on time.</blockquote><button type="button" class="more" hidden aria-expanded="false">Read more</button><cite>Emmbra N.</cite></figure>
      <figure class="rc"><span class="src">Google &middot; <span class="stars" aria-label="5 out of 5 stars">★★★★★</span></span><blockquote>Their service provided was impeccable. It’s the best place to get your flower arrangements.</blockquote><button type="button" class="more" hidden aria-expanded="false">Read more</button><cite>Ally F.</cite></figure>
      <figure class="rc"><span class="src">Google &middot; <span class="stars" aria-label="5 out of 5 stars">★★★★★</span></span><blockquote>Hands down my go to place to get the freshest bouquets! Top notch quality.</blockquote><button type="button" class="more" hidden aria-expanded="false">Read more</button><cite>Gina H.</cite></figure>
    </div>
    <div class="btn-row btn-row--center" style="margin-top:clamp(2rem,4vw,3rem)"><a class="btn" href="https://www.google.com/maps?cid=16409749098243940665" target="_blank" rel="noopener">Read all reviews on Google</a></div>
  </div>
</section>

<section class="closing">
  {im('centerpiece-wide-b', 'A wide table with a lush centerpiece of roses, pampas and greenery')}
  <div><span class="script">Let’s design florals they’ll remember.</span><a class="btn btn--arrow" href="contact.html">Inquire now</a></div>
</section>
'''
page('index.html', 'Florals for weddings, events and experiences',
     'Floral design for weddings and meaningful gatherings in Delaware, Pennsylvania and beyond, plus hands-on floral experiences and the Floral Bar.', home)

# ================================================================== ABOUT
about = f'''
{phero('table-long-pastel', 'A long white table set with pastel centerpieces and wishbone chairs in a bright room', 'About 1848', 'Delaware, Pennsylvania<br>&amp; Beyond', 'Floral<br>design studio',
       '1848 Blooms &amp; Designs creates florals for weddings and events, and teaches hands-on floral experiences.')}

<section class="section band-sand">
  <div class="wrap">
    {tbar('How we design', 'Our approach', 'In three parts')}
    <div class="principles" style="margin-top:clamp(2.5rem,5vw,4.5rem)">
      <div><h3>Thoughtful design</h3><p>Inspired by the beauty of a garden, we embrace the way flowers naturally grow and bloom. Layers of color, texture, movement and contrast come together to create arrangements that feel organic, romantic and effortlessly beautiful.</p></div>
      <div><h3>Intentional details</h3><p>Every stem has its place. From varying heights and delicate blooms to unexpected textures and subtle color transitions, each detail is thoughtfully considered to create balance, depth and a natural sense of movement.</p></div>
      <div><h3>Unforgettable moments</h3><p>Flowers have a way of transforming a space and how it makes us feel. We create floral designs that invite you to pause, take in the beauty and remember the moments that matter most.</p></div>
    </div>
  </div>
</section>

<section class="full-img">{im('table-window', 'A bright table by a window set with glassware and a centerpiece of yellow and orange flowers', extra='style="object-position:50% 70%"')}</section>

<section class="panels">
  <div class="panel panel--img">{im('designer-smile', 'Irene Acquah smiling in a beige apron, holding a bouquet of white, yellow and orange flowers', extra='style="object-position:50% 8%"')}</div>
  <div class="panel panel--petal panel--center"><div>
    <h2 class="dsp">Meet the lead designer behind 1848</h2>
    <div class="btn-row"><a class="btn" href="designer.html">Meet the designer</a></div>
  </div></div>
</section>

{closer('Tell us about your event.', 'Inquire now', band='band-paper2')}
'''
page('about.html', 'About', 'About 1848 Blooms & Designs, a floral design studio serving Delaware, Pennsylvania and beyond for weddings, events and hands-on experiences.', about)

# ================================================================== DESIGNER
designer = f'''
{phero('designer-couch', 'The designer relaxing on a cream sofa with a laptop, a bouquet of orange and yellow flowers beside her', 'Meet the designer', 'Lead<br>designer', '1848 Blooms<br>&amp; Designs',
       'Irene Acquah, lead designer of 1848 Blooms &amp; Designs.')}

<section class="panels">
  <div class="panel panel--img" style="min-height:640px">{im('designer-doorway', 'The designer standing in a sunlit doorway wearing a beige apron')}</div>
  <div class="panel panel--petal panel--center"><div>
    <h2 class="dsp">Why flowers</h2>
    <p>1848 Blooms &amp; Designs was founded on a love for timeless beauty, thoughtful details and meaningful experiences.</p>
    <p>What began as a passion for floral design has grown into a studio dedicated to creating elevated, intentional moments, whether through weddings, curated events or interactive floral experiences.</p>
    <p>Each design reflects a commitment to simplicity, elegance and the quiet beauty found in nature.</p>
    <div class="btn-row"><a class="btn" href="contact.html">Work with her</a><a class="btn btn--ghost" href="experiences.html">Join an experience</a></div>
  </div></div>
</section>

<section class="section band-paper2">
  <div class="wrap">
    {tbar('In the studio', 'Making', 'Gathering')}
    <div class="strip" style="margin-top:clamp(2rem,4vw,3.5rem)">
      <figure style="--r:{ratio('designer-window')}">{im('designer-window', 'The designer in an orange shirt and apron holding a bouquet by a window')}</figure>
      <figure style="--r:{ratio('designer-making')}">{im('designer-making', 'A designer arranging flowers in white bowls at a wooden table by a window')}</figure>
      <figure style="--r:{ratio('designer-stool')}">{im('designer-stool', 'The designer laughing on a stool, holding a bouquet and a single stem')}</figure>
    </div>
  </div>
</section>

{closer('Let’s make something together.', 'Inquire now')}
'''
page('designer.html', 'Meet the designer', 'Meet Irene Acquah, lead designer of 1848 Blooms & Designs.', designer)

# ================================================================== SERVICES
services = f'''
{phero('centerpiece-wide-a', 'A low arrangement of yellow, peach and white garden flowers on a white table set with glassware', 'Services', 'Weddings', 'Events',
       'Full-service florals, from a single bouquet to a ceremony and reception, designed around life’s most meaningful moments our clients cherish.',
       '<a class="btn" href="contact.html#general">Start an inquiry</a>')}

<section id="weddings" class="panels">
  <div class="panel panel--img" style="min-height:680px">{im('kiss-arch', 'A couple kissing under a wooden arch draped in white fabric and white flowers')}</div>
  <div class="panel panel--petal panel--center"><div>
    <h2 class="dsp">Weddings</h2>
    <p>Your florals should feel like you and fit the occasion. We understand and design the whole story so the ceremony, the reception and the people in them all feel connected.</p>
    <ul class="tick">
      <li><strong>Personal flowers</strong><span>Bouquets, boutonnieres, corsages and flowers for your wedding party.</span></li>
      <li><strong>Ceremony flowers</strong><span>Floral arches, aisle arrangements and statement pieces for your ceremony.</span></li>
      <li><strong>Reception flowers</strong><span>Centerpieces, installations and floral details that bring your reception space together.</span></li>
    </ul>
    <p><em>Custom wedding florals tailored to your celebration.</em></p>
    <p class="small">Wedding florals start at $2,500.00</p>
    <div class="btn-row"><a class="btn" {WED_ATTR}>Inquire about your wedding</a></div>
  </div></div>
</section>

<section id="events" class="panels">
  <div class="panel panel--sage panel--center"><div>
    <h2 class="dsp">Events</h2>
    <p>Some gatherings call for more than a beautiful table. They call for flowers that make people stop and look.</p>
    <p>From intimate dinners and bridal showers to birthdays and corporate events, we bring the beauty of a garden into the spaces where people come together.</p>
    <ul class="tick">
      <li><strong>Flowers that make the table feel like part of the occasion, not just a place to sit.</strong></li>
      <li><strong>A little height. An unexpected color. A mix of blooms and textures that makes the whole room come alive.</strong></li>
      <li><strong>From a single arrangement to a room full of flowers, every celebration deserves its own look.</strong></li>
    </ul>
    <p><em>Every event is different. Let’s talk about yours.</em></p>
    <p class="small">Event florals start at $750.00</p>
    <div class="btn-row"><a class="btn" href="contact.html">Inquire about your event</a></div>
  </div></div>
  <div class="panel panel--img" style="min-height:680px">{im('pastel-table-a', 'A pastel table with a tall arrangement of pink and white flowers, a taper candle and pink napkins')}</div>
</section>

<section class="panels">
  <div class="panel panel--img" style="min-height:460px">{im('installation-hanging', 'A long hanging floral installation of pink, magenta and white flowers with trailing greenery')}</div>
  <div class="panel panel--petal-2 panel--paper2 panel--center"><div>
    <h2 class="dsp">Want guests to make their own?</h2>
    <p>Add a Floral Bar to your event, or book a hands-on experience for your group.</p>
    <div class="btn-row"><a class="btn" href="floral-bar.html">See the Floral Bar</a><a class="btn btn--ghost" href="experiences.html">See experiences</a></div>
  </div></div>
</section>

<section class="section">
  <div class="wrap split split--top split--57">
    <h2 class="dsp" style="font-size:clamp(2rem,.9rem + 3.4vw,4rem)">Questions we hear a lot</h2>
    <div class="faq">
      <details><summary>How far in advance should I book?</summary><div><p>For weddings, we recommend reaching out 6–12 months ahead, especially for popular dates. For smaller events, 4–8 weeks is a good starting point. Have something coming up sooner? Reach out and we’ll see what we can do.</p></div></details>
      <details><summary>How much do wedding and event flowers cost?</summary><div><p>Every event is different, so pricing depends on the flowers, arrangements and overall design. Share a few details about your celebration and we’ll put together a proposal based on what you need.</p></div></details>
      <details><summary>Can I choose my flowers and colors?</summary><div><p>Absolutely. We love hearing what you have in mind. We’ll work with your preferred colors and flowers, while recommending seasonal blooms and combinations that work beautifully together. Specific varieties depend on availability.</p></div></details>
      <details><summary>Do you deliver and set up?</summary><div><p>Delivery and on-site setup can be included depending on your event and floral needs. We’ll confirm the arrangements, location and any associated fees in your proposal.</p></div></details>
      <details><summary>Where do you provide floral services?</summary><div><p>We serve Delaware, Pennsylvania and beyond, including Philadelphia, New Hope, Lumberville, Doylestown and Kennett Square. Planning something farther away? We’d love to hear about it.</p></div></details>
      <details><summary>What happens after I submit an inquiry?</summary><div><p>We’ll review your event details, learn more about what you’re looking for and discuss the next steps. Once the scope and pricing are agreed upon, we’ll explain the booking and payment process.</p></div></details>
    </div>
  </div>
</section>

{closer('Ready to talk florals?', 'Inquire now', 'contact.html#general', 'band-petal')}
'''
page('services.html', 'Services', 'Wedding and event floral design in Delaware, Pennsylvania and beyond: bouquets, ceremony florals, reception florals and installations.', services)

# ================================================================== FLORAL BAR
bar = f'''
{phero('', '', 'The Floral Bar', 'Pick<br>and arrange', 'Take it<br>home',
       'A self-serve flower station for your event. Guests choose their own blooms, build a bouquet or arrangement, and leave with something they made.',
       '<a class="btn" href="contact.html">Inquire about a Floral Bar</a>', plain=True)}

<section class="panels">
  <div class="panel panel--img" style="min-height:640px">{im('home-floralbar', 'A woven basket filled with white and hot pink roses')}</div>
  <div class="panel panel--sage panel--center"><div>
    <h2 class="dsp">Pick your stems. Arrange them. Take them home.</h2>
    <p>The Floral Bar turns flowers into the activity. We set up the bar with seasonal stems, greenery and containers in your palette, and a designer shows guests how to build something beautiful.</p>
    <div class="btn-row"><a class="btn" href="contact.html">Inquire about a Floral Bar</a></div>
  </div></div>
</section>

<section class="section">
  <div class="wrap">
    {tbar('How it works', 'Three steps', 'For every guest')}
    <ol class="steps steps--three" style="margin-top:clamp(2.5rem,5vw,4.5rem)">
      <li><h3>Pick</h3><p>We set up the bar with seasonal stems, greenery and containers in your palette. Guests choose what they love.</p></li>
      <li><h3>Arrange</h3><p>A designer is on hand to show guests how to build a bouquet or arrangement, whatever their experience.</p></li>
      <li><h3>Take</h3><p>Everyone leaves with their own piece, wrapped and ready to carry home. It doubles as a favor.</p></li>
    </ol>
  </div>
</section>

<section class="panels">
  <div class="panel panel--petal panel--center"><div>
    <h2 class="dsp">Where it works best</h2>
    <ul class="tick">
      <li><strong>Bridal showers and bachelorette parties</strong></li>
      <li><strong>Weddings and rehearsal dinners</strong><span>Part of the reception, or a favor guests make.</span></li>
      <li><strong>Birthdays and baby showers</strong></li>
      <li><strong>Corporate and team events</strong></li>
    </ul>
    <p class="small">Floral Bar packages start at $850.00</p>
    <div class="btn-row"><a class="btn" href="contact.html">Inquire about a Floral Bar</a></div>
  </div></div>
  <div class="panel panel--img" style="min-height:640px">{im('ladder-daisies', 'Daisies and cosmos in a woven basket at the foot of a wooden ladder')}</div>
</section>

{closer('Bring the Floral Bar to your event.', 'Start an inquiry', band='band-paper2')}
'''
page('floral-bar.html', 'Floral Bar', 'The Floral Bar by 1848 Blooms & Designs: a self-serve flower station where guests pick stems, arrange them and take them home.', bar)

# ================================================================== EXPERIENCES
# Edit upcoming workshops and passes here, then run `python3 build.py`.
# `book`: a payment or booking link (Square, Stripe, Eventbrite...). Leave it
# empty and the button opens the reservation form with the workshop filled in.
WORKSHOPS = [
    dict(slug='winter-garden', title='Winter Garden Arrangement', date='Sat, Jan 17, 2027', time='2:00 – 4:00 PM',
         place='Location TBD', price=175, seats=12, booked=0, img='bouquet-white-b',
         alt='A white bouquet of roses and wildflowers with greenery',
         blurb='A seasonal arrangement with textured blooms and winter greenery.', book='https://book.stripe.com/00weVdfAD5rq4ag9sp1kA09'),
    dict(slug='romantic-roses', title='Romantic Garden Roses', date='Sat, Feb 14, 2027', time='2:00 – 4:00 PM',
         place='Location TBD', price=175, seats=12, booked=0, img='pastel-closeup',
         alt='Pink garden roses and blue glassware on a pastel table',
         blurb='Create a lush, garden-inspired arrangement featuring romantic roses and seasonal blooms.', book='https://book.stripe.com/6oUfZh0FJ3ji2288ol1kA0a'),
    dict(slug='spring-bloom', title='Spring in Bloom', date='Sat, Mar 14, 2027', time='2:00 – 4:00 PM',
         place='Location TBD', price=175, seats=12, booked=0, img='ranunculus-jar',
         alt='White ranunculus in a clear glass jar',
         blurb='A fresh spring arrangement that celebrates the season’s first blooms.', book='https://book.stripe.com/cNi14n1JN4nmeOU4851kA0b'),
]
# Live seat counts from Stripe (written hourly by scripts/stripe_sync.py).
# A workshop's capacity is the payment limit on its Stripe Payment Link.
_seats_file = 'data/workshop-seats.json'
if os.path.exists(_seats_file):
    import json
    _live = json.load(open(_seats_file))
    for _w in WORKSHOPS:
        _w.update({k: v for k, v in _live.get(_w['slug'], {}).items() if k in ('seats', 'booked', 'closed')})

PASSES = [
    dict(slug='pass-4', title='Four-workshop pass', price=660, save=40, book='https://buy.stripe.com/14A6oH3RV8DC6ioawt1kA0c'),
    dict(slug='pass-6', title='Six-workshop pass', price=960, save=90, book='https://buy.stripe.com/28E00j3RV9HGfSYeMJ1kA0d'),
]

ICONS = {
 'flower': '<svg viewBox="0 0 32 32" aria-hidden="true"><circle cx="16" cy="16" r="3.2"/><path d="M16 12.8c-2.6-3.6-2.6-7 0-9 2.6 2 2.6 5.4 0 9zM16 19.2c2.6 3.6 2.6 7 0 9-2.6-2-2.6-5.4 0-9zM12.8 16c-3.6 2.6-7 2.6-9 0 2-2.6 5.4-2.6 9 0zM19.2 16c3.6-2.6 7-2.6 9 0-2 2.6-5.4 2.6-9 0z"/></svg>',
 'scissors': '<svg viewBox="0 0 32 32" aria-hidden="true"><circle cx="9" cy="24" r="3.5"/><circle cx="23" cy="24" r="3.5"/><path d="M11.5 21.5 24 4M20.5 21.5 8 4"/></svg>',
 'people': '<svg viewBox="0 0 32 32" aria-hidden="true"><circle cx="16" cy="10" r="4"/><path d="M8 26c0-5 3.6-8 8-8s8 3 8 8"/><circle cx="7.5" cy="13" r="3"/><path d="M2.5 25c0-3.6 2.2-6 5.5-6"/><circle cx="24.5" cy="13" r="3"/><path d="M29.5 25c0-3.6-2.2-6-5.5-6"/></svg>',
 'vase': '<svg viewBox="0 0 32 32" aria-hidden="true"><path d="M12 4h8M13 4v5c-4 2-6 6-6 10 0 5 4 9 9 9s9-4 9-9c0-4-2-8-6-10V4"/></svg>',
}

def book_href(item, kind):
    if item['book']:
        return f'href="{html.escape(item["book"])}"'
    return f'href="reserve.html?experience={kind}&amp;item={item["slug"]}"'

def ws_row(w):
    left = 0 if w.get('closed') else max(0, w['seats'] - w['booked'])
    pct = round(100 * w['booked'] / w['seats'])
    plural = 's' if left != 1 else ''
    tag = ('Sold out' if left <= 0 else f'Only {left} spot{plural} left' if left <= 4
           else f'{left} spots available' if w['booked'] == 0 else f'{left} spots left')
    btn = (f'<a class="btn" {book_href(w, "workshop")}>Book now</a>' if left > 0
           else '<span class="btn btn--off" aria-disabled="true">Sold out</span>')
    return f'''<article class="ws">
  <div class="ws__img">{im(w['img'], w['alt'])}</div>
  <div class="ws__body">
    <h3>{w['title']}</h3>
    <p class="ws__meta"><span>{w['date']}</span><span>{w['time']}</span><span>{w['place']}</span></p>
    <p>{w['blurb']}</p>
  </div>
  <div class="ws__price"><strong>${w['price']}</strong><span>per person</span></div>
  <div class="ws__cta">
    <span class="ws__tag">{tag}</span>
    <div class="ws__bar" role="img" aria-label="{w['booked']} of {w['seats']} spots booked"><i style="width:{pct}%"></i></div>
    {btn}
  </div>
</article>'''

benefits = ''.join(f'<li>{ICONS[i]}<span>{t}</span></li>' for i, t in [
    ('flower', 'Fresh, seasonal flowers'), ('scissors', 'Step-by-step guidance'),
    ('people', 'Small, intimate classes'), ('vase', 'An arrangement to take home')])
passes = ''.join(f'''<div class="pass"><h3>{p_['title']}</h3><strong>${p_['price']}</strong><span>Save ${p_['save']}</span><a class="btn" {book_href(p_, "pass")}>Choose pass</a></div>''' for p_ in PASSES)

exp = f'''
<section class="ex-hero">
  <div class="ex-hero__img">{im('designing-table', 'Irene arranging yellow and white flowers at a table in a bright room', eager=True, extra='style="object-position:70% 50%"')}</div>
  <div class="ex-hero__copy">
    <span class="eyebrow">Experiences</span>
    <h1 class="dsp">A year of floral workshops</h1>
    <p>Hands-on workshops, seasonal design experiences and private gatherings. No experience needed, just come ready to create.</p>
    <div class="btn-row"><a class="btn" href="#workshops">View workshops</a><a class="btn btn--ghost" href="#passes">Get a workshop pass</a></div>
  </div>
</section>

<ul class="ex-benefits">{benefits}</ul>

<section class="section" id="workshops">
  <div class="wrap">
    <h2 class="dsp ex-h2">Upcoming workshops</h2>
    <div class="ws-list">
      {''.join(ws_row(w) for w in WORKSHOPS)}
    </div>
    <p class="ws-note">All sales are final. Can&rsquo;t make it? Pass your spot to a friend. Just email us their name so we can update our list.</p>
  </div>
</section>

<section class="section section--tight" id="passes">
  <div class="wrap">
    <div class="passes">
      <div class="passes__intro"><h2 class="dsp ex-h2">Workshop passes</h2><p>Enjoy a year of floral experiences and save.</p></div>
      {passes}
    </div>
  </div>
</section>

<section class="section" id="private">
  <div class="wrap ex-private">
    <figure>{im('pastel-table-c', 'A pastel table with a tall arrangement of pink and white flowers and pink napkins')}</figure>
    <div>
      <span class="eyebrow">Private experiences</span>
      <h2 class="dsp ex-h2">Gather, create, celebrate</h2>
      <p>A floral workshop for your group, perfect for birthdays, bridal showers, team gatherings and more. We bring the flowers, the tools and the know-how.</p>
      <div class="btn-row"><a class="btn" href="reserve.html?experience=private">Plan a private experience</a></div>
    </div>
  </div>
</section>
'''
page('experiences.html', 'Experiences', 'Book a hands-on floral workshop, a workshop pass or a private floral experience with 1848 Blooms & Designs in Delaware, Pennsylvania and beyond.', exp)

# ================================================================== PORTFOLIO
P = [
    ('kiss-arch', 'weddings', 'A couple kissing under a wooden arch draped in white fabric and flowers'),
    ('table-long-pastel', 'events', 'A long white table with pastel centerpieces and wishbone chairs'),
    ('bouquet-bright', 'bouquets weddings', 'A bright bouquet of yellow, coral and blush flowers held against a white dress'),
    ('bridesmaids', 'weddings', 'Bridesmaids in lavender dresses holding white bouquets on a brick patio'),
    ('place-setting', 'details events', 'A place setting with a blush menu card, a sprig of yellow flowers and gold flatware'),
    ('installation-hanging', 'events', 'A long hanging floral installation of pink, magenta and white flowers'),
    ('bouquet-chair', 'bouquets', 'A pink and blue bouquet with a pale blue ribbon resting on a wooden chair'),
    ('arch-pampas', 'weddings', 'A wooden triangle ceremony arch dressed with pampas grass and dried flowers'),
    ('flatlay-suite', 'details weddings', 'An invitation suite flat lay with a ring box and soft blooms'),
    ('pastel-table-a', 'events', 'A pink and cream table with a tall pastel arrangement and a taper candle'),
    ('couple-window', 'weddings', 'A bride and groom sharing a quiet moment at a window, her bouquet in hand'),
    ('tablescape-citrus', 'events details', 'A centerpiece of orange roses and yellow blooms on a linen-covered table'),
    ('bouquet-white-b', 'bouquets', 'A white bouquet of roses and wildflowers with greenery'),
    ('reception-lights', 'events weddings', 'A reception table beneath string lights with a pampas and rose centerpiece'),
    ('ladder-daisies', 'floral-bar', 'Daisies and cosmos in a woven basket beside a wooden ladder'),
    ('bouquet-ribbon', 'bouquets', 'A pastel and coral bouquet tied with a rust-colored ribbon'),
    ('flatlay-blue', 'details', 'Blush invitation cards with pale blue ribbon and delphinium'),
    ('arch-willow', 'weddings', 'A wooden ceremony pergola draped with white fabric and flowers beneath a willow tree'),
    ('bowl-window', 'details events', 'A white footed bowl of yellow, peach and pink flowers on a window ledge'),
    ('basket-walk', 'floral-bar', 'A woman in a white dress carrying a striped basket of wildflowers'),
    ('couple-bouquet', 'weddings', 'A bride seated with a white bouquet beside her groom'),
    ('bouquet-anthurium', 'bouquets', 'A bouquet with green anthurium, white roses and a cream ribbon'),
    ('tablescape-detail', 'details events', 'A closeup of a tablescape with roses, glassware and a place card'),
    ('installation-ladders', 'events', 'A hanging floral installation above two wooden ladders with small vases'),
    ('pastel-closeup', 'details events', 'A closeup of pink roses and blue glassware on a pastel table'),
    ('bouquet-marble', 'bouquets', 'A white bouquet tied with trailing ribbon on a marble stool'),
    ('invitations-pink', 'details', 'Blush wedding invitations with a ring box and yellow craspedia'),
    ('ladder-basket', 'floral-bar', 'A woven basket of wildflowers on a wooden ladder'),
]
shots = ''.join(f'<button type="button" class="shot" data-cat="{c}" aria-label="View larger: {html.escape(a)}">{im(n, a)}</button>' for n, c, a in P)
portfolio = f'''
{phero('', '', 'Portfolio', 'Weddings<br>and events', 'Bouquets<br>and details',
       'A look at recent weddings, events, bouquets and the details between them.', plain=True)}

<section class="section section--tight">
  <div class="wrap">
    <div class="filters" role="group" aria-label="Filter portfolio">
      <button type="button" data-filter="all" aria-pressed="true">All</button>
      <button type="button" data-filter="weddings" aria-pressed="false">Weddings</button>
      <button type="button" data-filter="events" aria-pressed="false">Events</button>
      <button type="button" data-filter="bouquets" aria-pressed="false">Bouquets</button>
      <button type="button" data-filter="details" aria-pressed="false">Details</button>
      <button type="button" data-filter="floral-bar" aria-pressed="false">Floral Bar</button>
    </div>
    <div class="gallery">{shots}</div>
  </div>
</section>

<dialog class="lb" id="lightbox" aria-label="Photo viewer">
  <div class="lb__in"><img src="" alt=""><p class="lb__cap"></p></div>
  <button type="button" class="x" aria-label="Close">&times;</button>
  <button type="button" class="pv" aria-label="Previous photo">&lsaquo;</button>
  <button type="button" class="nx" aria-label="Next photo">&rsaquo;</button>
</dialog>

{closer('Like what you see?', 'Inquire now', band='band-paper2')}
'''
page('portfolio.html', 'Portfolio', 'Weddings, events, bouquets and floral details by 1848 Blooms & Designs.', portfolio)

# ================================================================== CONTACT
contact = f'''
<section class="phero phero--plain">
  <div class="phero__mid"><span class="eyebrow">Inquiries &middot; Now booking 2027</span><div class="tbar"><h1 class="dsp">Get in touch</h1></div></div>
  <div class="phero__foot">
    <p>We are looking forward to hearing from you!</p>
    <p>For weddings, please visit our <a class="link" href="services.html#weddings">wedding page here</a> and complete our <a class="link" {WED_ATTR}>wedding inquiry form here</a>.<br>For general inquiries, send us a <a class="link" href="#general">message here</a>.</p>
  </div>
</section>

<section class="section" id="general">
  <div class="wrap form-grid form-grid--flip">
    <aside class="aside">
      {im('designer-stool', 'Irene Acquah, lead designer of 1848 Blooms & Designs, laughing on a stool and holding a bouquet', '', extra='style="object-position:50% 30%"')}
      <dl>
        <div><dt>Email</dt><dd><a class="link" href="mailto:{EMAIL}">{EMAIL}</a></dd></div>
        <div><dt>Service area</dt><dd>{AREA}</dd></div>
        <div><dt>Follow along</dt><dd><a class="link" href="https://www.instagram.com/1848BloomsandDesigns" target="_blank" rel="noopener">Instagram</a>, <a class="link" href="https://www.facebook.com/1848BloomsandDesigns" target="_blank" rel="noopener">Facebook</a>, <a class="link" href="https://www.tiktok.com/@1848bloomsanddesigns" target="_blank" rel="noopener">TikTok</a>, <a class="link" href="https://www.linkedin.com/company/1848-blooms-and-designs/" target="_blank" rel="noopener">LinkedIn</a></dd></div>
      </dl>
    </aside>
    <div class="gi">
      <h2 class="dsp">General inquiry</h2>
      <p>Whether you’re planning a wedding, a special event, a floral experience or simply have a question, we’re here to help bring your vision to life. Please type your message below or send me a direct email at <a class="link" href="mailto:{EMAIL}">{EMAIL}</a>.</p>
      <form class="form" data-form="inquiry" novalidate>
      <div class="field"><label for="name">Your name</label><input id="name" name="name" autocomplete="name" required><p class="err">Enter your name.</p></div>
      <div class="field"><label for="email">Email</label><input id="email" name="email" type="email" autocomplete="email" required><p class="err">Enter a valid email address.</p></div>
      <div class="field"><label for="phone">Phone</label><input id="phone" name="phone" type="tel" autocomplete="tel"></div>
      <div class="field"><label for="kind">What are you planning?</label>
        <select id="kind" name="event_type" required>
          <option value="">Choose one</option>
          <option>Wedding</option><option>Private event</option><option>Corporate event</option>
          <option>Floral Bar</option><option>Workshop or private gathering</option><option>Something else</option>
        </select><p class="err">Choose what you are planning.</p></div>
      <div class="field"><label for="date">Event date <span class="hint">(if you have one)</span></label><input id="date" name="event_date" type="date"></div>
      <div class="field"><label for="venue">Venue or city</label><input id="venue" name="venue" autocomplete="off"></div>
      <div class="field"><label for="guests">Guest count <span class="hint">(roughly)</span></label><input id="guests" name="guests" type="number" min="1" inputmode="numeric"></div>
      <div class="field"><label for="found">How did you find us?</label><input id="found" name="found_us"></div>
      <div class="field full"><label for="msg">Your message</label><textarea id="msg" name="message" placeholder="Colors, flowers you love, the feeling you want, or simply your question." required></textarea><p class="err">Tell us a little about your plans.</p></div>
      <div class="hp" aria-hidden="true"><label>Leave this empty<input name="website" tabindex="-1" autocomplete="off"></label></div>
      <div class="notice" role="status"></div>
      <button class="btn" type="submit">Send</button>
      </form>
    </div>
  </div>
</section>
'''
page('contact.html', 'Contact', 'Inquire about wedding or event florals, the Floral Bar or a workshop with 1848 Blooms & Designs.', contact)

# ================================================================== RESERVE
reserve = f'''
{phero('', '', 'Reserve your spot', 'Workshops', 'Private<br>gatherings',
       'Choose a workshop, a pass or a private gathering, and we will confirm your spot and payment details by email.', plain=True)}

<section class="section">
  <div class="wrap form-grid">
    <form class="form" data-form="reservation" novalidate>
      <fieldset class="field full" style="border:0;padding:0;margin:0">
        <legend>Which experience?</legend>
        <div class="choice" style="margin-top:.6rem">
          <label><input type="radio" name="experience" value="workshop" required><span>Floral workshop</span></label>
          <label><input type="radio" name="experience" value="pass"><span>Workshop pass</span></label>
          <label><input type="radio" name="experience" value="private"><span>Private gathering</span></label>
        </div>
        <p class="err">Choose an experience.</p>
      </fieldset>
      <div class="field full" data-show="workshop"><label for="ritem">Which workshop?</label><select id="ritem" name="workshop"><option value="">Choose a date</option>{''.join(f'<option value="{w["slug"]}">{w["title"]}, {w["date"]}</option>' for w in WORKSHOPS)}</select></div>
      <div class="field full" data-show="pass" hidden><label for="rpass">Which pass?</label><select id="rpass" name="pass">{''.join(f'<option value="{p_["slug"]}">{p_["title"]}, ${p_["price"]}</option>' for p_ in PASSES)}</select></div>
      <div class="field" data-show="private" hidden><label for="rdate">Preferred date</label><input id="rdate" name="preferred_date" type="date"></div>
      <div class="field"><label for="rguests">Number of guests</label><input id="rguests" name="guests" type="number" min="1" value="1" inputmode="numeric" required><p class="err">Enter how many guests.</p></div>
      <div class="field"><label for="rname">Your name</label><input id="rname" name="name" autocomplete="name" required><p class="err">Enter your name.</p></div>
      <div class="field"><label for="remail">Email</label><input id="remail" name="email" type="email" autocomplete="email" required><p class="err">Enter a valid email address.</p></div>
      <div class="field"><label for="rphone">Phone</label><input id="rphone" name="phone" type="tel" autocomplete="tel"></div>
      <div class="field full"><label for="rnotes">Anything we should know?</label><textarea id="rnotes" name="notes" placeholder="The occasion, accessibility needs, or questions."></textarea></div>
      <div class="hp" aria-hidden="true"><label>Leave this empty<input name="website" tabindex="-1" autocomplete="off"></label></div>
      <div class="notice" role="status"></div>
      <button class="btn" type="submit">Reserve my spot</button>
    </form>
    <aside class="aside">
      {im('designer-making', 'A designer arranging flowers in white bowls at a wooden table', '', extra='style="aspect-ratio:3/2;object-position:30% 50%"')}
      <dl>
        <div><dt>What happens next</dt><dd>We email you to confirm your spot and send a link to pay.</dd></div>
        <div><dt>Cancellations</dt><dd>All workshop sales are final. Can&rsquo;t make it? You&rsquo;re welcome to pass your spot to someone else. Just email us their name so we can update our list.</dd></div>
        <div><dt>Questions</dt><dd><a class="link" href="contact.html">Send us a message</a></dd></div>
      </dl>
    </aside>
  </div>
</section>
'''
page('reserve.html', 'Reserve your spot', 'Reserve a spot in a floral workshop or private gathering with 1848 Blooms & Designs.', reserve)

# ================================================================== WEDDING INQUIRY (opens the pop-up)
wedding = f"""
{phero('', '', 'Wedding &amp; event inquiry', 'Weddings', 'Events',
       'We&rsquo;re honored you&rsquo;re considering 1848 Blooms &amp; Designs. Six short steps, about three minutes. We reply within 24 hours.', btn=None, plain=True)}
<section class="section section--tight"><div class="wrap" style="text-align:center"><a class="btn" {WED_ATTR} data-wm-auto>Start your inquiry</a></div></section>
"""
page('wedding.html', 'Wedding & event inquiry', 'Tell 1848 Blooms & Designs about your wedding or event: date, venue, vision, floral elements and budget.', wedding)

# ================================================================== THANK YOU
thanks = f'''
<div data-thanks>
<section class="phero phero--plain">
  <div class="phero__mid"><div class="tbar"><p class="flank">We received<br>your message</p><h1 class="dsp" data-ty-title>Thank you</h1><p class="flank">Talk<br>soon</p></div></div>
  <div class="phero__foot">
    <p data-ty="inquiry">We received your inquiry and will reply by email within 24 hours.</p>
    <p data-ty="wedding" hidden>We received your wedding and event inquiry. Irene will reply by email within 24 hours.</p>
    <p data-ty="booked" hidden>You&rsquo;re booked! Your receipt is on its way to your email. We&rsquo;ll send workshop details a few days before your date.</p>
    <p data-ty="pass" hidden>Your workshop pass is confirmed and your receipt is on its way to your email. We&rsquo;ll be in touch to help you choose your workshops.</p>
    <p data-ty="reservation" hidden>We received your reservation request. We will email you to confirm your spot within 24 hours.</p>
  </div>
</section>
<section class="section thanks-body">
  <div class="wrap split">
    <div>
      <ul class="tick">
        <li><strong>While you wait</strong><span>Browse recent work in the <a class="link" href="portfolio.html">portfolio</a>, or save ideas to share when we talk.</span></li>
        <li><strong>Need to add something?</strong><span>Reply to our email, or write to us at <a class="link" href="mailto:{EMAIL}">{EMAIL}</a>.</span></li>
      </ul>
      <div class="btn-row" style="margin-top:2rem"><a class="btn" href="index.html">Back to home</a><a class="btn btn--ghost" href="portfolio.html">See the portfolio</a></div>
    </div>
    <figure>{im('bouquet-ribbon', 'A pastel and coral bouquet tied with a rust-colored ribbon', '', extra='style="aspect-ratio:4/5;object-position:50% 40%"')}</figure>
  </div>
</section>
</div>
'''
page('thank-you.html', 'Thank you', 'Thank you from 1848 Blooms & Designs.', thanks, noindex=True)
print('built', len([f for f in os.listdir(OUT) if f.endswith('.html')]), 'pages')
