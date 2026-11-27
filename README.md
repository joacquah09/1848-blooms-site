# 1848 Blooms & Designs — site v3

Static site (HTML, CSS, vanilla JS). No build step needed to view: open `index.html`.

- `build.py` regenerates the pages (`python3 build.py`, needs Pillow).
- Fonts: Gilda Display (headings, free stand-in for Cammron Light), Questrial, Pinyon Script, Cormorant — embedded in `assets/site.css`.
- Placeholder copy is highlighted yellow (`.ph`). Replace designer name/story, contact details, social links (currently `#`), prices, FAQ and testimonials.
- Forms: the contact and reserve forms send through FormSubmit (`FORM_ENDPOINT` and `FORM_CC` in `assets/site.js`) to ireneacquah@ with a copy to jonasacquah@. The first submission sends an activation email to ireneacquah@ that must be confirmed once. Empty endpoint = preview mode.
- Hosting: GitHub Pages → Settings → Pages → deploy from `main`, root.

## Workshop seats (automatic)

Every hour, `.github/workflows/stripe-seats.yml` runs `scripts/stripe_sync.py`, which reads each workshop's Stripe Payment Link: the link's payment limit is the capacity and its completed payments are the seats booked. It writes `data/workshop-seats.json`, rebuilds the site and commits if anything changed.

- Change a workshop's capacity: in Stripe, edit the Payment Link and change "Limit the number of payments". The site follows within the hour.
- Needs the repository secret `STRIPE_READ_KEY`: a Stripe restricted key with **Payment Links: Read** only.
- Run it now: GitHub > Actions > "Update workshop seats from Stripe" > Run workflow.

## SEO

- Business details used by search engines (phones, emails, Google Business Profile link, social links, target towns) live at the top of `build.py`. Google structured data (Florist, Service, Breadcrumb JSON-LD), canonical links and Open Graph tags are generated from them.
- `wedding-florist.html` is the wedding landing page for "wedding florist" searches in Delaware, Greenville, Philadelphia and New Hope. `wedding.html` stays the inquiry form page.
- `build.py` also writes `sitemap.xml`, `robots.txt` and `404.html` (which forwards old Shopify links like `/pages/contact` to the matching page), plus 800px copies of photos in `assets/img/sm/` for phones. These copies are made once and committed; delete one to regenerate it.
