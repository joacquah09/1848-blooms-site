# 1848 Blooms & Designs — site v3

Static site (HTML, CSS, vanilla JS). No build step needed to view: open `index.html`.

- `build.py` regenerates the pages (`python3 build.py`, needs Pillow).
- Fonts: Gilda Display (headings, free stand-in for Cammron Light), Questrial, Pinyon Script, Cormorant — embedded in `assets/site.css`.
- Placeholder copy is highlighted yellow (`.ph`). Replace designer name/story, contact details, social links (currently `#`), prices, FAQ and testimonials.
- Forms: set `FORM_ENDPOINT` in `assets/site.js` (e.g. Formspree). Empty = preview mode.
- Hosting: GitHub Pages → Settings → Pages → deploy from `main`, root.
