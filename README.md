# Vanessa Rubel — Portfolio (source export)

A 6-page personal portfolio site: plain static HTML with inline CSS. No build step, no framework, no dependencies.

## What's here

```
index.html                        Homepage (hero, name, 3 featured project tiles)
work.html                          "Selected work" index (alternating image/text rows)
about.html                         About page
project-tiffany-wendel.html        Project detail — Tiffany Wendel
project-kith.html                  Project detail — Kith
project-concrete-runways.html      Project detail — Concrete Runways
tiffany-methodology.html           Tiffany performance visual methodology
images/                            Photos used on the site
```

## 1. Framework / technology

Plain HTML5 + inline CSS. No React, no JS framework, no build tool, no npm package is required to view or edit it — every style is written directly on each element via the `style="..."` attribute. This is intentional: it's the simplest possible thing to open in Codex, edit, and reload.

## 2. Install dependencies

None. There is no `package.json` — nothing to install.

## 3. Run it locally

Serve the folder so relative links and browser behavior match the deployed site:

```
npx serve .
```
or
```
python3 -m http.server 8000
```
then visit `http://localhost:8000` (or the port `serve` prints).

## Fonts

- Body/headline font: system sans stack (`'Helvetica Neue', Helvetica, Arial, sans-serif`) — no download needed, uses whatever's installed on the viewing device.
- Serif "reflection" quotes use **Newsreader** (Google Fonts), loaded via a `<link>` tag in each page's `<head>`. Requires an internet connection to fetch from `fonts.googleapis.com`; if you need it fully offline, download the Newsreader italic 400/500 weights and self-host with an `@font-face` rule instead of the Google Fonts `<link>`.

## Design system reference

- Sand background: `#F3F3E9`
- Cobalt (headlines, links, accent blocks): `#0212EE`
- Cherry (tags, accents, tilted highlight boxes): `#D20001`
- Soft pink (accent block, contrast text on cobalt): `#FEC6E9`
- Body text: `#1a1a1a`
- Corners: ~8px radius on image/accent blocks
- Tilts: small rotations (-2.5° to 2.5°) on images and color blocks
- Nav: `Work · Index · Info`, with a tilted "VR ✦" pill top-left

## Current site notes

- Each page has a title, viewport metadata, and the shared `favicon.svg`.
- Pages use fluid sizing with page-specific responsive rules where needed, including the Tiffany case-study result carousel.
- The Tiffany methodology is available as `tiffany-methodology.html`; its source data, generated summaries, and visual-generation script remain in `data/tiffany/`, `images/tiffany-data/`, and `scripts/`.

## Editing notes

Every visual property lives inline on the element it affects — there are no shared CSS classes to hunt through. To change a color, font size, or spacing value, find the element in the relevant `.html` file and edit its `style="..."` attribute directly. This keeps every page fully self-contained, at the cost of some repetition between pages (e.g. the nav bar markup is duplicated across all six files rather than shared via a template/include, since there's no build step to assemble includes).
