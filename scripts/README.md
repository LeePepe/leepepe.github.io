# Vault importer

## Live vault and Demos regression gates

`python3 build_site.py` generates the vault and Demos hub and idempotently adapts only the two root gallery shells. Candidate content and nested gallery pages remain upstream-owned. The eight CL maps explicitly assign light/dark semantic roles; contrast-safe accent shades retain each source hue. Palette bars use an intentional UI-area allocation (50% canvas, 20% surface, 15% accents, 15% text/border), not a measured screenshot distribution. Theme and CTA state are local to each specimen; gallery telemetry on the hub is read-only.

Run `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s scripts -p 'test_*.py'` for importer, metadata fallback/deduplication, title normalization and storage regressions. Run `node scripts/test_vault_browser.mjs --output /absolute/handoff/receipts/browser` for actual drag/touch/cancel, reaction, sorting, context, ring, disclosure, anchor, clipboard, contrast and portal-storage tests, plus viewport/stage PNGs and containment-aware geometry. Evidence paths must stay outside this published repository. The runner owns an ephemeral loopback server and closes it and the browser in `finally`.

Run `node scripts/test_vault_webkit.mjs --output /absolute/handoff/receipts/webkit` for real WebKit slide/drop, optical fallback, dual appearances and 44px geometry checks. This catches native macOS select controls that ignore a minimum height unless their custom control appearance is explicit. Both runners are bounded (300s Chromium, 120s WebKit).

The existing Playwright runtime defaults to `/tmp/tia-pw/node_modules/playwright/index.mjs`; override `PLAYWRIGHT_MODULE` only if that runtime is unavailable. `DEMO_BASELINE` defaults to `origin/master`: browser tests compare complete current remote summary markup, iframe sources and candidate metadata, not historical candidate counts. No dependency files or test screenshots are published. Reduced motion disables autoplay; all stages retain keyboard/click alternatives, and checkbox labels supply real 44px hit regions. Geometry records only active hits and their real containing DOM boxes; deliberately overlapping, noninteractive visual layers are separately recorded in `noninteractiveVisuals`. Section PNGs capture an additional 8px of the actual surrounding page gutter, not added pixels, so panel borders are not mistaken for cropped content. Vault filters remain in normal document flow instead of occluding the interactive stage beneath a tall sticky toolbar.

`scripts/vault_ingest.py` updates the committed `vault/manifest.json`, invokes the installed `design_catalog.py` by default, and rebuilds the site unless `--no-build` is supplied. `--no-vault-write` is the explicit opt-out for design-studio writes (useful for isolated tests).

## Runtime dependencies

- Python 3.10+ and Pillow (`python3 -m pip install Pillow`) for image decoding, thumbnail generation, and the deterministic RGB fallback palette.
- macOS Vision OCR uses the system `swift` tool and Vision/AppKit; a successful no-text recognition is recorded as `empty_text`, while a Vision/runtime failure exits nonzero with stderr.
- Image palette measurement is enabled by default, tries BAMA `measure.swift palette` first, and falls back to validated Pillow median-cut RGB for PNG/JPEG (including RGBA PNG). Use `--no-measure-palette` only when intentionally skipping measurement.
- The default catalog sync requires the installed `~/.copilot/skills/design-studio/scripts/design_catalog.py`. Set `DESIGN_CATALOG`, `DESIGN_STUDIO_VAULT_DIR`, or `DESIGN_CATALOG_PATH` for another installation or isolated vault/catalog.
- No network access or arbitrary URL execution is performed. URL imports write a structured note under `COLLECTED_TOOLS_DIR` (default `~/Development/Personal/collected-tools`) and deduplicate by canonical scheme/host/path. Without `--title`, the canonical host/path supplies the label and note slug; GitHub subpaths collapse to owner/repo and X/Twitter links collapse to the status, without overwriting existing notes.
- `--refresh-sources` deterministically refreshes the committed source snapshot from the top-level `README.md` learned/queued routing tables plus `hallmark.md` and `tenfold-design-skill.md`. It preserves table questions/reconciliation wording, routing references, note usage records, and clean reference links, with input hashes and line citations. It does not read repo READMEs or follow knowledge-vault references, write external sources, or invoke the design catalog. Tenfold remains `not_recorded` unless classified in a state table. Normal site rendering consumes only this offline snapshot for vault sources; rerunning the refresh with unchanged inputs leaves it unchanged.

Examples:

```sh
python3 scripts/vault_ingest.py --image ./shot.png --title "New shot" --measure-palette --archetype-ref VS-005
python3 scripts/vault_ingest.py --url https://github.com/owner/repo --kind tool
python3 scripts/vault_ingest.py --text "Undoable confirmation" --kind pattern
python3 scripts/vault_ingest.py --image ./fixture.png --measure-palette --no-vault-write --no-build
python3 scripts/vault_ingest.py --refresh-sources --no-build
```

`--kind pattern` routes text through `design_catalog.py ingest`; `vault` and `inspiration` use `vault-ingest`. Unsupported kind values are rejected by argparse. `--commit` and `--push` are opt-in. Commit stages only changed, existing importer/build files, the manifest, root `index.html`, `vault/index.html`, and vault shots; it refuses unrelated staged changes and does not stage unrelated unstaged/untracked files. Push targets `origin master` and refuses feature branches and detached HEADs; it never pushes from a temporary worktree branch. The permanent Personal wrapper is `~/Development/Personal/collected-tools/vault_ingest.py`; it defaults to `/Users/lee/Development/leepepe.github.io` and accepts `BLOG_ASSET_VAULT_ROOT` for a worktree or clone. Reinstall it reproducibly after cloning with `python3 scripts/install_vault_wrapper.py`; it is intentionally outside Git history.
