#!/usr/bin/env python3
"""Generates the v2 static pages for 1848 Blooms & Designs into /home/claude/v3/site."""
import os, html
from PIL import Image

OUT = os.path.dirname(os.path.abspath(__file__))
IMG = OUT + '/assets/img'
SITE = '1848 Blooms & Designs'
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
       '<a href="#" aria-label="Pinterest"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12.2 2C6.9 2 4.2 5.600 4.2 8.900c0 2 .8 3.800 2.400 4.400.3.100.5 0 .6-.3l.2-.9c.1-.3 0-.4-.2-.6-.5-.6-.8-1.300-.8-2.300 0-3 2.200-5.700 5.800-5.700 3.200 0 4.900 2 4.900 4.500 0 3.400-1.500 6.200-3.700 6.200-1.200 0-2.100-1-1.800-2.200.3-1.500 1-3.100 1-4.200 0-1-.5-1.800-1.600-1.800-1.300 0-2.300 1.300-2.300 3.100 0 1.100.4 1.900.4 1.900l-1.500 6.400c-.4 1.800-.1 4.200 0 4.400 0 .1.200.2.300.1.100-.2 1.800-2.200 2.300-4.200l.9-3.500c.5.900 1.800 1.600 3.200 1.600 4.200 0 7-3.800 7-8.900C20.200 5 17 2 12.200 2z"/></svg></a>'
       '<a href="#" aria-label="Instagram"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><rect x="3.500" y="3.500" width="17" height="17" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.200" cy="6.800" r=".6" fill="currentColor"/></svg></a>'
       '<a href="#" aria-label="Facebook"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M13.500 21v-7.500h2.500l.4-3h-2.900V8.600c0-.9.3-1.500 1.500-1.500h1.500V4.400c-.3 0-1.200-.1-2.200-.1-2.200 0-3.700 1.300-3.700 3.800v2.400H7.800v3h2.800V21h2.900z"/></svg></a>'
       '</span>')


def header(cur):
    links = ''.join(f'<a href="{h}"' + (' aria-current="page"' if h == cur else '') + f'>{t}</a>' for h, t in NAV)
    m = ''.join(f'<li><a href="{h}">{t}</a></li>' for h, t in MNAV)
    return f'''<a class="skip" href="#main">Skip to content</a>
<header class="hd"><div class="hd__top">
  <p class="flank hd__tag">Delaware + Philadelphia<br>floral designer</p>
  {LOGO}
  <div class="hd__right">{SOC}<a class="contact-link" href="contact.html">Contact</a>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="mnav"><i aria-hidden="true"></i><span>Menu</span></button></div>
</div></header>
<nav class="primary" aria-label="Main">{links}</nav>
<nav class="mnav" id="mnav" aria-label="Menu">
  <ul>{m}</ul>
  <div class="foot-line"><span>Serving Delaware and Philadelphia</span><span>Now booking 2026</span></div>
</nav>'''


def footer():
    thumbs = ''.join(im(n, a) for n, a in [('arch-willow','A wooden arch with white flowers'),('pastel-table-a','A pastel table with a tall arrangement'),('bouquet-ribbon','A pastel bouquet with a rust ribbon'),('bridesmaids','Bridesmaids holding bouquets'),('ladder-daisies','Daisies in a woven basket')])
    return f'''<footer class="site-footer">
  <div class="f-top">{LOGO}<div class="hd__right">{SOC}<a class="contact-link" href="contact.html">Contact</a></div></div>
  <div class="f-mid">
    <ul><li><a href="index.html">Home</a></li><li><a href="about.html">About</a></li><li><a href="designer.html">Meet the designer</a></li><li><a href="portfolio.html">Portfolio</a></li></ul>
    <ul><li><a href="services.html">Services</a></li><li><a href="floral-bar.html">Floral Bar</a></li><li><a href="experiences.html">Experiences</a></li><li><a href="reserve.html">Reserve your spot</a></li></ul>
    <div class="f-btns"><a class="btn" href="reserve.html">Reserve your spot</a><a class="btn" href="#"><span class="ph">Follow @yourhandle</span></a>
      <p class="f-note"><span class="ph">[hello@yourdomain.com]</span> &middot; <span class="ph">[Phone]</span></p></div>
  </div>
  <div class="f-thumbs">{thumbs}</div>
  <div class="legal"><span>&copy; <span data-year>2026</span> 1848 Blooms &amp; Designs</span><span>Serving Delaware and Philadelphia &middot; Now booking 2026</span></div>
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
<link rel="stylesheet" href="assets/site.css?v=3">
</head>
<body>
{header(fname)}
<main id="main">
{body}
</main>
{footer()}
<script src="assets/site.js"></script>
</body>
</html>
''')


# ---------- components ----------
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
    return f'''<section class="section {band}"><div class="wrap closer">
  <h2 class="dsp">{title}</h2><div class="btn-row"><a class="btn btn--arrow" href="{href}">{btn}</a></div>
</div></section>'''


# ================================================================== HOME
rail_imgs = ['table-window','bridesmaids','bouquet-bright','couple-window','pastel-table-a','arch-pampas','bouquet-chair','installation-hanging','tablescape-citrus','bouquet-ribbon']
rail_alt = {n:a for n,c,a in []}
RAIL = ''.join(f'<figure style="--ar:{round(dims(n)[0]/dims(n)[1],3)}">{im(n, n.replace("-"," ").capitalize()+" by 1848 Blooms & Designs")}</figure>' for n in rail_imgs)

home = f'''
<section class="hero">
  {im('home-banner', 'A long white table set with candles, glassware and a low arrangement of yellow, peach and white flowers beside a window', 'hero__img', eager=True)}
  <div class="hero__body">
    <span class="eyebrow">Delaware and Philadelphia &middot; Now booking 2026</span>
    <h1>Event floral design that leads with <span class="script">atmosphere.</span></h1>
    <div class="btn-row">
      <a class="btn btn--arrow" href="services.html">Weddings + events</a>
      <a class="btn btn--arrow" href="experiences.html">Experiences + Floral Bar</a>
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
    <h2 class="dsp"><span class="ph">[Designer name]</span></h2>
    <span class="rule"></span>
    <p class="ph">[Two or three lines in her voice: how long she has designed, what her process feels like, what clients say about working with her.]</p>
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
      <figure class="rc"><span class="src"><span class="ph">[Source]</span></span><blockquote class="ph">[Client quote about their wedding or event.]</blockquote><cite class="ph">[Client name]</cite></figure>
      <figure class="rc"><span class="src"><span class="ph">[Source]</span></span><blockquote class="ph">[Client quote about working with the designer.]</blockquote><cite class="ph">[Client name]</cite></figure>
      <figure class="rc"><span class="src"><span class="ph">[Source]</span></span><blockquote class="ph">[Client quote about a workshop or the Floral Bar.]</blockquote><cite class="ph">[Client name]</cite></figure>
    </div>
  </div>
</section>

<section class="closing">
  {im('centerpiece-wide-b', 'A wide table with a lush centerpiece of roses, pampas and greenery')}
  <div><span class="script">Let’s design florals they’ll remember.</span><a class="btn btn--cream btn--arrow" href="contact.html">Inquire now</a></div>
</section>
'''
page('index.html', 'Florals for weddings, events and experiences',
     'Floral design for weddings and meaningful gatherings in Delaware and Philadelphia, plus hands-on floral experiences and the Floral Bar.', home)

# ================================================================== ABOUT
about = f'''
{phero('table-long-pastel', 'A long white table set with pastel centerpieces and wishbone chairs in a bright room', 'About 1848', 'Delaware<br>and Philadelphia', 'Floral<br>design studio',
       '1848 Blooms &amp; Designs creates florals for weddings and events, and teaches hands-on floral experiences.')}

<section class="section band-moss">
  <div class="wrap">
    {tbar('How we design', 'Our approach', 'In three parts')}
    <div class="principles" style="margin-top:clamp(2.5rem,5vw,4.5rem)">
      <div><h3>Thoughtful design</h3><p>We begin with questions about the space, the season and how you want people to feel. The flowers follow from the answers, never from a template.</p></div>
      <div><h3>Intentional details</h3><p>A ribbon color, a stem height, the way a bouquet sits in the hand. We decide each one on purpose, and we check them against each other.</p></div>
      <div><h3>Unforgettable moments</h3><p>Good florals do their work quietly. They become the thing guests mention afterward, without ever getting in the way of the day.</p></div>
    </div>
  </div>
</section>

<section class="full-img">{im('table-window', 'A bright table by a window set with glassware and a centerpiece of yellow and orange flowers', extra='style="object-position:50% 70%"')}</section>

<section class="section">
  <div class="wrap split split--top split--57">
    <div class="copy">
      <h2 class="dsp" style="font-size:clamp(2rem,.9rem + 3.6vw,4.2rem)">How an event comes together</h2>
      <p>Every project follows the same four steps, whether it is one bouquet or a full wedding. <span class="ph">[Confirm this process and add typical timelines.]</span></p>
    </div>
    <ol class="steps">
      <li><div><h3>Inquire</h3><p>Tell us the date, the place and what you are imagining. We reply with availability.</p></div></li>
      <li><div><h3>Consult</h3><p>We talk through the space, your palette and your priorities, and look at inspiration together.</p></div></li>
      <li><div><h3>Design</h3><p>You receive a proposal with florals, quantities and pricing. We refine it with you until it feels right.</p></div></li>
      <li><div><h3>Deliver and set up</h3><p>We prepare the flowers, bring them to your venue and install them, so you can focus on everything else.</p></div></li>
    </ol>
  </div>
</section>

<section class="panels">
  <div class="panel panel--img">{im('designer-smile', 'The designer smiling in a beige apron, holding a bouquet of white, yellow and orange flowers')}</div>
  <div class="panel panel--petal panel--center"><div>
    <h2 class="dsp">Meet the designer behind 1848</h2>
    <p>Every arrangement starts with one person’s eye. Read how she got started and what she cares about when she designs.</p>
    <div class="btn-row"><a class="btn" href="designer.html">Meet the designer</a></div>
  </div></div>
</section>

{closer('Tell us about your event.', 'Inquire now', band='band-paper2')}
'''
page('about.html', 'About', 'About 1848 Blooms & Designs, a floral design studio serving Delaware and Philadelphia for weddings, events and hands-on experiences.', about)

# ================================================================== DESIGNER
designer = f'''
{phero('designer-couch', 'The designer relaxing on a cream sofa with a laptop, a bouquet of orange and yellow flowers beside her', 'Meet the designer', 'Designer<br>and owner', '1848 Blooms<br>&amp; Designs',
       '<span class="ph">[Designer name]</span>, designer and owner of 1848 Blooms &amp; Designs.')}

<section class="panels">
  <div class="panel panel--img" style="min-height:640px">{im('designer-doorway', 'The designer standing in a sunlit doorway wearing a beige apron')}</div>
  <div class="panel panel--petal panel--center"><div>
    <h2 class="dsp">Why flowers</h2>
    <p class="ph">[Her story, in her own voice: how she started, what first drew her to flowers, and what the name 1848 means. Two or three short paragraphs is plenty.]</p>
    <p class="ph">I design with the season first. What is growing decides the palette, and the room decides the shape. [Edit or replace this line so it sounds like her.]</p>
    <p class="ph">[What she loves most about the work: the first walk-through of a venue, the moment a bouquet comes together, the room when guests arrive.]</p>
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
page('designer.html', 'Meet the designer', 'Meet the designer and owner of 1848 Blooms & Designs.', designer)

# ================================================================== SERVICES
services = f'''
{phero('arch-pampas', 'A wooden triangle ceremony arch dressed with pampas grass and dried flowers on a deck', 'Services', 'Weddings', 'Events',
       'Full-service florals, from a single bouquet to a ceremony and reception, designed around your venue and delivered by us.',
       '<a class="btn" href="contact.html">Start an inquiry</a>')}

<section id="weddings" class="panels">
  <div class="panel panel--img" style="min-height:680px">{im('kiss-arch', 'A couple kissing under a wooden arch draped in white fabric and white flowers')}</div>
  <div class="panel panel--petal panel--center"><div>
    <h2 class="dsp">Weddings</h2>
    <p>Your florals should feel like you and fit your venue. We design the whole picture so the ceremony, the reception and the people in them all feel connected.</p>
    <ul class="tick">
      <li><strong>Bridal and bridesmaid bouquets</strong><span>Plus boutonnieres, corsages and flowers for family.</span></li>
      <li><strong>Ceremony florals</strong><span>Arches, aisle pieces and welcome signage.</span></li>
      <li><strong>Reception florals</strong><span>Centerpieces, head table and tablescapes.</span></li>
      <li><strong>Installations</strong><span>Hanging and statement pieces for the moments guests will photograph.</span></li>
    </ul>
    <p class="small"><span class="ph">Wedding florals start at [$____].</span></p>
    <div class="btn-row"><a class="btn" href="contact.html">Inquire about your wedding</a></div>
  </div></div>
</section>

<section id="events" class="panels">
  <div class="panel panel--deep panel--center"><div>
    <h2 class="dsp">Events</h2>
    <p>Dinners, showers, birthdays and corporate gatherings. We style the table and the room so the occasion feels considered from the first glance.</p>
    <ul class="tick">
      <li><strong>Tablescapes and centerpieces</strong><span>Florals planned alongside your linens, candles and place settings.</span></li>
      <li><strong>Hanging and ladder installations</strong><span>Overhead pieces that turn a plain room into a place.</span></li>
      <li><strong>Arrangements and bouquets</strong><span>For hosts, guests of honor and gifting.</span></li>
    </ul>
    <p class="small" style="color:rgba(246,238,232,.85)"><span class="ph">Event florals start at [$____].</span></p>
    <div class="btn-row"><a class="btn btn--cream" href="contact.html">Inquire about your event</a></div>
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
      <details><summary>How far ahead should I book?</summary><div><p class="ph">[Answer: for example, how many months ahead for weddings and how many weeks for events.]</p></div></details>
      <details><summary>Do you deliver and set up?</summary><div><p class="ph">[Answer: delivery and setup details, and any fees.]</p></div></details>
      <details><summary>Do you travel outside Delaware and Philadelphia?</summary><div><p class="ph">[Answer: travel radius and travel fees.]</p></div></details>
      <details><summary>How do deposits and payments work?</summary><div><p class="ph">[Answer: deposit amount, payment schedule and accepted payment methods.]</p></div></details>
      <details><summary>Can I choose my own colors and flowers?</summary><div><p class="ph">[Answer: how much of the palette is the client’s call, and how seasonality affects it.]</p></div></details>
    </div>
  </div>
</section>

{closer('Ready to talk florals?', 'Inquire now', band='band-petal')}
'''
page('services.html', 'Services', 'Wedding and event floral design in Delaware and Philadelphia: bouquets, ceremony florals, reception florals and installations.', services)

# ================================================================== FLORAL BAR
bar = f'''
{phero('', '', 'The Floral Bar', 'Pick<br>and arrange', 'Take it<br>home',
       'A self-serve flower station for your event. Guests choose their own blooms, build a bouquet or arrangement, and leave with something they made.',
       '<a class="btn" href="contact.html">Inquire about a Floral Bar</a>', plain=True)}

<section class="panels">
  <div class="panel panel--img" style="min-height:640px">{im('home-floralbar', 'A woven basket filled with white and hot pink roses')}</div>
  <div class="panel panel--deep panel--center"><div>
    <h2 class="dsp">Pick your stems. Arrange them. Take them home.</h2>
    <p>The Floral Bar turns flowers into the activity. We set up the bar with seasonal stems, greenery and containers in your palette, and a designer shows guests how to build something beautiful.</p>
    <div class="btn-row"><a class="btn btn--cream" href="contact.html">Inquire about a Floral Bar</a></div>
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
    <p><span class="ph">[What is included: stems per guest, containers, a designer on site, setup and cleanup, and the guest counts you can serve.]</span></p>
    <p class="small"><span class="ph">Floral Bar packages start at [$____].</span></p>
    <div class="btn-row"><a class="btn" href="contact.html">Inquire about a Floral Bar</a></div>
  </div></div>
  <div class="panel panel--img" style="min-height:640px">{im('ladder-daisies', 'Daisies and cosmos in a woven basket at the foot of a wooden ladder')}</div>
</section>

{closer('Bring the Floral Bar to your event.', 'Start an inquiry', band='band-paper2')}
'''
page('floral-bar.html', 'Floral Bar', 'The Floral Bar by 1848 Blooms & Designs: a self-serve flower station where guests pick stems, arrange them and take them home.', bar)

# ================================================================== EXPERIENCES
exp = f'''
{phero('designing-table', 'A florist arranging yellow and white flowers at a table in a bright room', 'Experiences', 'Workshops', 'Private<br>gatherings',
       'Hands-on floral experiences that bring people together around flowers, designed to inspire creativity and connection.',
       '<a class="btn" href="reserve.html">Reserve your spot</a>')}

<section class="section">
  <div class="wrap">
    <div class="xp">
      <figure>{im('designer-making', 'A designer arranging flowers in white bowls at a wooden table by a window')}</figure>
      <div>
        <h2 class="dsp">Floral workshops</h2>
        <p>Join a small class, learn the techniques behind a designer’s arrangements and leave with your own piece. No experience needed. <span class="ph">[Confirm format.]</span></p>
        <dl>
          <dt>Length</dt><dd><span class="ph">[Hours]</span></dd>
          <dt>Group size</dt><dd><span class="ph">[Number of guests]</span></dd>
          <dt>Price</dt><dd><span class="ph">[$ per person]</span></dd>
          <dt>Where</dt><dd><span class="ph">[Studio or venue and city]</span></dd>
        </dl>
        <div class="btn-row"><a class="btn" href="reserve.html?experience=workshop">Reserve your spot</a></div>
      </div>
    </div>
    <div class="xp">
      <figure>{im('table-window', 'A bright table by a window set with glassware and a centerpiece of yellow and orange flowers', '', extra='style="object-position:50% 75%"')}</figure>
      <div>
        <h2 class="dsp">Private gatherings</h2>
        <p>Bring a workshop to your group: bridal showers, birthdays, team outings or a day with friends. We shape the experience around the occasion. <span class="ph">[Confirm format.]</span></p>
        <dl>
          <dt>Length</dt><dd><span class="ph">[Hours]</span></dd>
          <dt>Group size</dt><dd><span class="ph">[Minimum and maximum]</span></dd>
          <dt>Price</dt><dd><span class="ph">[$ per person or per group]</span></dd>
          <dt>Where</dt><dd><span class="ph">[Your space or ours]</span></dd>
        </dl>
        <div class="btn-row"><a class="btn" href="reserve.html?experience=private">Reserve your spot</a></div>
      </div>
    </div>
  </div>
</section>

<section class="section band-paper2">
  <div class="wrap split split--top split--57">
    <div class="copy"><h2 class="dsp" style="font-size:clamp(2rem,.9rem + 3.4vw,4rem)">Upcoming dates</h2><p>Spots are limited so everyone gets time with the designer.</p></div>
    <table class="dates">
      <thead><tr><th scope="col">Date</th><th scope="col">Experience</th><th scope="col">Spots</th></tr></thead>
      <tbody>
        <tr><td><span class="ph">[Date and time]</span></td><td><span class="ph">[Workshop name]</span></td><td><a class="link" href="reserve.html?experience=workshop">Reserve</a></td></tr>
        <tr><td><span class="ph">[Date and time]</span></td><td><span class="ph">[Workshop name]</span></td><td><a class="link" href="reserve.html?experience=workshop">Reserve</a></td></tr>
        <tr><td><span class="ph">[Date and time]</span></td><td><span class="ph">[Workshop name]</span></td><td><a class="link" href="reserve.html?experience=workshop">Reserve</a></td></tr>
      </tbody>
    </table>
  </div>
</section>

{closer('Make something beautiful together.', 'Reserve your spot', 'reserve.html', 'band-petal')}
'''
page('experiences.html', 'Experiences', 'Hands-on floral workshops and private gatherings with 1848 Blooms & Designs in Delaware and Philadelphia.', exp)

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
{phero('', '', 'Contact', 'Inquiries', 'Now booking<br>2026',
       'Share the basics and we will reply with availability and next steps. <span class="ph">[Typical response time.]</span>', plain=True)}

<section class="section">
  <div class="wrap form-grid">
    <form class="form" data-form="inquiry" novalidate>
      <div class="field"><label for="name">Your name</label><input id="name" name="name" autocomplete="name" required><p class="err">Enter your name.</p></div>
      <div class="field"><label for="email">Email</label><input id="email" name="email" type="email" autocomplete="email" required><p class="err">Enter a valid email address.</p></div>
      <div class="field"><label for="phone">Phone <span class="hint">(optional)</span></label><input id="phone" name="phone" type="tel" autocomplete="tel"></div>
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
      <div class="field full"><label for="msg">What are you imagining?</label><textarea id="msg" name="message" placeholder="Colors, flowers you love, the feeling you want, anything that helps." required></textarea><p class="err">Tell us a little about your plans.</p></div>
      <div class="hp" aria-hidden="true"><label>Leave this empty<input name="website" tabindex="-1" autocomplete="off"></label></div>
      <div class="notice" role="status"></div>
      <button class="btn" type="submit">Send inquiry</button>
    </form>
    <aside class="aside">
      {im('pastel-table-c', 'A pastel table set with a tall arrangement of pink and white flowers, pink napkins and gold flatware')}
      <dl>
        <div><dt>Email</dt><dd><span class="ph">[hello@yourdomain.com]</span></dd></div>
        <div><dt>Phone</dt><dd><span class="ph">[Phone number]</span></dd></div>
        <div><dt>Service area</dt><dd>Delaware and Philadelphia</dd></div>
        <div><dt>Follow along</dt><dd><a class="link" href="#">Instagram</a>, <a class="link" href="#">Pinterest</a>, <a class="link" href="#">Facebook</a></dd></div>
      </dl>
    </aside>
  </div>
</section>
'''
page('contact.html', 'Contact', 'Inquire about wedding or event florals, the Floral Bar or a workshop with 1848 Blooms & Designs.', contact)

# ================================================================== RESERVE
reserve = f'''
{phero('', '', 'Reserve your spot', 'Workshops', 'Private<br>gatherings',
       'Choose an experience and a date, and we will confirm your spot by email.', plain=True)}

<section class="section">
  <div class="wrap form-grid">
    <form class="form" data-form="reservation" novalidate>
      <fieldset class="field full" style="border:0;padding:0;margin:0">
        <legend>Which experience?</legend>
        <div class="choice" style="margin-top:.6rem">
          <label><input type="radio" name="experience" value="workshop" required><span>Floral workshop</span></label>
          <label><input type="radio" name="experience" value="private"><span>Private gathering</span></label>
        </div>
        <p class="err">Choose an experience.</p>
      </fieldset>
      <div class="field"><label for="rdate">Preferred date</label><input id="rdate" name="preferred_date" type="date" required><p class="err">Choose a date.</p></div>
      <div class="field"><label for="rguests">Number of guests</label><input id="rguests" name="guests" type="number" min="1" value="1" inputmode="numeric" required><p class="err">Enter how many guests.</p></div>
      <div class="field"><label for="rname">Your name</label><input id="rname" name="name" autocomplete="name" required><p class="err">Enter your name.</p></div>
      <div class="field"><label for="remail">Email</label><input id="remail" name="email" type="email" autocomplete="email" required><p class="err">Enter a valid email address.</p></div>
      <div class="field"><label for="rphone">Phone <span class="hint">(optional)</span></label><input id="rphone" name="phone" type="tel" autocomplete="tel"></div>
      <div class="field full"><label for="rnotes">Anything we should know?</label><textarea id="rnotes" name="notes" placeholder="The occasion, accessibility needs, or questions."></textarea></div>
      <div class="hp" aria-hidden="true"><label>Leave this empty<input name="website" tabindex="-1" autocomplete="off"></label></div>
      <div class="notice" role="status"></div>
      <button class="btn" type="submit">Reserve my spot</button>
    </form>
    <aside class="aside">
      {im('designer-making', 'A designer arranging flowers in white bowls at a wooden table', '', extra='style="aspect-ratio:3/2;object-position:30% 50%"')}
      <dl>
        <div><dt>What happens next</dt><dd>We email you to confirm your date and share details. <span class="ph">[Add payment steps.]</span></dd></div>
        <div><dt>Cancellations</dt><dd><span class="ph">[Cancellation and rescheduling policy.]</span></dd></div>
        <div><dt>Questions</dt><dd><a class="link" href="contact.html">Send us a message</a></dd></div>
      </dl>
    </aside>
  </div>
</section>
'''
page('reserve.html', 'Reserve your spot', 'Reserve a spot in a floral workshop or private gathering with 1848 Blooms & Designs.', reserve)

# ================================================================== THANK YOU
thanks = f'''
<div data-thanks>
<section class="phero phero--plain">
  <div class="phero__mid"><div class="tbar"><p class="flank">We received<br>your message</p><h1 class="dsp" data-ty-title>Thank you</h1><p class="flank">Talk<br>soon</p></div></div>
  <div class="phero__foot">
    <p data-ty="inquiry">We received your inquiry and will reply by email <span class="ph">[within X business days]</span>.</p>
    <p data-ty="reservation" hidden>We received your reservation request. We will email you to confirm your spot <span class="ph">[within X business days]</span>.</p>
  </div>
</section>
<section class="section thanks-body">
  <div class="wrap split">
    <div>
      <ul class="tick">
        <li><strong>While you wait</strong><span>Browse recent work in the <a class="link" href="portfolio.html">portfolio</a>, or save ideas to share when we talk.</span></li>
        <li><strong>Need to add something?</strong><span>Reply to our email, or write to us at <span class="ph">[hello@yourdomain.com]</span>.</span></li>
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
