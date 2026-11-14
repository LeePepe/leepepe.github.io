# Vault importer

`scripts/vault_ingest.py` updates the committed `vault/manifest.json`, invokes the installed `design_catalog.py` by default, and rebuilds the site unless `--no-build` is supplied. `--no-vault-write` is the explicit opt-out for design-studio writes (useful for isolated tests).

## Runtime dependencies

- Python 3.10+ and Pillow (`python3 -m pip install Pillow`) for image decoding, thumbnail generation, and the deterministic RGB fallback palette.
- macOS Vision OCR uses the system `swift` tool and Vision/AppKit; OCR gracefully returns empty text when unavailable.
- The default catalog sync requires the installed `~/.copilot/skills/design-studio/scripts/design_catalog.py`. Set `DESIGN_CATALOG` or `DESIGN_STUDIO_VAULT_DIR` for another installation or isolated vault.
- No network access or arbitrary URL execution is performed. URL imports write a structured note under `COLLECTED_TOOLS_DIR` (default `~/Development/Personal/collected-tools`) and deduplicate by canonical scheme/host/path.

Examples:

```sh
python3 scripts/vault_ingest.py --image ./shot.png --title "New shot" --measure-palette --archetype-ref VS-005
python3 scripts/vault_ingest.py --url https://github.com/owner/repo --kind tool
python3 scripts/vault_ingest.py --text "Undoable confirmation" --kind pattern
python3 scripts/vault_ingest.py --image ./fixture.png --measure-palette --no-vault-write --no-build
```

`--kind pattern` routes text through `design_catalog.py ingest`; `vault` and `inspiration` use `vault-ingest`. Unsupported kind values are rejected by argparse. `--commit` and `--push` are opt-in; push targets only the current branch.
