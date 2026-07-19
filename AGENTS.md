# Repository Guidelines

## Project Structure & Module Organization

This repository is a dependency-free, six-page portfolio built with HTML5 and inline CSS.

- `index.html` is the landing page.
- `work.html` lists the featured projects.
- `about.html` contains the biography and background.
- `project-*.html` files are individual case studies.
- `images/` stores local JPEG and PNG assets referenced with relative URLs.
- `README.md` documents the visual system, local setup, and known unfinished areas.

Keep each page self-contained. Navigation and shared visual patterns are duplicated intentionally because there is no template or build layer.

## Build, Test, and Development Commands

No installation or build step is required. Preview through a local HTTP server so relative links behave consistently:

```bash
python3 -m http.server 8000
# Open http://localhost:8000
```

Alternatively, run `npx serve .` if Node.js is available. Before submitting changes, inspect the working tree with `git diff --check` when working from a Git clone; this catches whitespace errors.

## Coding Style & Naming Conventions

Use semantic HTML5 elements (`nav`, `section`, `article`, and `figure`) and preserve the existing two-space indentation for nested markup. Keep global resets in the page-level `<style>` block and page-specific presentation inline unless introducing shared CSS is explicitly part of the change. Follow existing lowercase, hyphenated filenames such as `project-kith.html`; use descriptive lowercase image names such as `concrete-runways-cover.jpg`.

Maintain the established palette and typography described in `README.md`. Include useful `alt` text when adding actual `<img>` elements, and keep every page's `<title>`, language, charset, and viewport metadata accurate.

## Testing Guidelines

There is no automated test framework or coverage requirement. Manually verify changed pages at desktop and mobile widths. Check navigation links, image loading, text overflow, keyboard focus, and browser-console errors. If shared navigation or repeated styles change, review all six pages, not only the edited file.

## Commit & Pull Request Guidelines

This checkout does not include Git history, so no repository-specific commit convention can be inferred. Use short, imperative subjects such as `Fix project navigation links` and keep unrelated edits separate. Pull requests should summarize the user-visible change, list pages tested, note remaining placeholders or limitations, and include before/after screenshots for layout or visual updates. Link an issue when one exists.
