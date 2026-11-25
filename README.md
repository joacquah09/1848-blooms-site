# 1848 Blooms & Designs — site v3

Static site (HTML, CSS, vanilla JS). No build step needed to view: open `index.html`.

- `build.py` regenerates the pages (`python3 build.py`, needs Pillow).
- Fonts: Gilda Display (headings, free stand-in for Cammron Light), Questrial, Pinyon Script, Cormorant — embedded in `assets/site.css`.
- Placeholder copy is highlighted yellow (`.ph`). Replace designer name/story, contact details, social links (currently `#`), prices, FAQ and testimonials.
- Forms: the contact and reserve forms send through FormSubmit (`FORM_ENDPOINT` and `FORM_CC` in `assets/site.js`) to ireneacquah@ with a copy to jonasacquah@. The first submission sends an activation email to ireneacquah@ that must be confirmed once. Empty endpoint = preview mode.
- Hosting: GitHub Pages → Settings → Pages → deploy from `main`, root.
