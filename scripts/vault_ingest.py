#!/usr/bin/env python3
"""Portable multimodal importer for the blog asset vault."""
from __future__ import annotations
import argparse, json, os, re, shutil, subprocess, sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
try:
    from PIL import Image
except ImportError:
    Image = None

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "vault" / "manifest.json"
SHOTS = ROOT / "assets" / "vault" / "shots"
COLLECTED = Path(os.environ.get("COLLECTED_TOOLS_DIR", str(Path.home() / "Development/Personal/collected-tools")))
DESIGN_CATALOG = Path(os.environ.get("DESIGN_CATALOG", str(Path.home() / ".copilot/skills/design-studio/scripts/design_catalog.py")))
DESIGN_VAULT_DIR = os.environ.get("DESIGN_STUDIO_VAULT_DIR")

def slugify(value: str) -> str:
    value = re.sub(r"[^\w\-]+", "-", value.lower(), flags=re.UNICODE).strip("-")
    return value or "asset"

def palette(path: Path):
    if Image is None: return []
    with Image.open(path) as source:
        image = source.convert("RGB"); image.thumbnail((300, 300))
        quantized = image.quantize(colors=6, method=Image.Quantize.MEDIANCUT)
        colors = quantized.getcolors(image.width * image.height) or []
        raw = quantized.getpalette(); total = sum(n for n, _ in colors) or 1
        return [{"hex": "#%02X%02X%02X" % tuple(raw[i * 3:i * 3 + 3]), "pct": round(n / total * 100, 1)} for n, i in sorted(colors, reverse=True)[:6]]

def ocr(path: Path) -> str:
    """Use Vision when available; empty text is a valid result for visual-only shots."""
    if sys.platform != "darwin": return ""
    swift = '''import Vision, AppKit
let u=URL(fileURLWithPath:CommandLine.arguments[1]); guard let image=NSImage(contentsOf:u) else { exit(0) }
var r=CGRect.zero; guard let rep=image.representations.first, let c=rep.cgImage(forProposedRect:&r, context:nil, hints:nil) else { exit(0) }
let req=VNRecognizeTextRequest { req, _ in print((req.results as? [VNRecognizedTextObservation] ?? []).compactMap{$0.topCandidates(1).first?.string}.joined(separator:" ")) }; req.recognitionLevel = .fast
try? VNImageRequestHandler(cgImage:c, options:[:]).perform([req])'''
    try:
        result = subprocess.run(["swift", "-e", swift, str(path)], capture_output=True, text=True, timeout=20)
        return result.stdout.strip()
    except (OSError, subprocess.SubprocessError):
        return ""

def load():
    return json.loads(MANIFEST.read_text(encoding="utf-8")) if MANIFEST.exists() else {"schema_version":1,"screenshots":[],"cards":[],"patterns":[],"tools":[],"toolchains":[]}

def save(data):
    MANIFEST.parent.mkdir(parents=True, exist_ok=True); MANIFEST.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

def sync_design_catalog(args, *, image=None, text=None):
    if getattr(args, "no_vault_write", False):
        return None
    if not DESIGN_CATALOG.is_file():
        raise SystemExit(f"design catalog not found: {DESIGN_CATALOG}; use --no-vault-write to opt out")
    is_pattern = getattr(args, "kind", None) == "pattern" and not image
    command = [sys.executable, str(DESIGN_CATALOG), "ingest" if is_pattern else "vault-ingest", "--no-jev"]
    if DESIGN_VAULT_DIR and not is_pattern:
        command += ["--vault-dir", DESIGN_VAULT_DIR]
    if image:
        command += ["--image", str(image), "--measure-palette"]
        if getattr(args, "archetype_ref", None): command += ["--archetype-ref", args.archetype_ref]
    else:
        command += ["--text", text or ""]
    return subprocess.run(command, cwd=ROOT, check=True, capture_output=True, text=True)

def maybe_build(args):
    if not args.no_build:
        subprocess.run([sys.executable, str(ROOT / "build_site.py")], cwd=ROOT, check=True)

def image_import(args, data):
    source = Path(args.image).expanduser().resolve()
    if not source.is_file(): raise SystemExit(f"image not found: {source}")
    if Image is None: raise SystemExit("Pillow is required for image import")
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    stem = f"{stamp}-{slugify(args.title or source.stem)}"; ext = source.suffix.lower() if source.suffix.lower() in {".png", ".jpg", ".jpeg"} else ".png"
    SHOTS.mkdir(parents=True, exist_ok=True); dest = SHOTS / (stem + ext); thumb = SHOTS / (stem + "-thumb" + ext)
    with Image.open(source) as image:
        image.convert("RGBA" if ext == ".png" else "RGB").save(dest)
        small = image.copy(); small.thumbnail((960, 960), Image.Resampling.LANCZOS); small.convert("RGBA" if ext == ".png" else "RGB").save(thumb)
        width, height = image.size
    sync_design_catalog(args, image=dest)
    data["screenshots"].append({"id": stem, "title": args.title or source.stem, "image": f"/assets/vault/shots/{dest.name}", "thumbnail": f"/assets/vault/shots/{thumb.name}", "width": width, "height": height, "measured_palette": palette(dest) if args.measure_palette else [], "ocr_text": ocr(dest), "archetype_ref": args.archetype_ref, "platform": args.platform.split(",") if args.platform else [], "notes": args.text or "Imported by vault_ingest.py."})
    return {"mode":"image", "id":stem}

def update_collected_readme(*, title, canonical, kind, note):
    readme = COLLECTED / "README.md"
    if not readme.exists():
        readme.write_text("# Collected Tools\n\n| file | 种別 | one-line summary |\n|---|---|---|\n", encoding="utf-8")
    text = readme.read_text(encoding="utf-8")
    row = f"| [{note.name}]({note.name}) | {kind} | {canonical} |"
    if canonical not in text:
        readme.write_text(text.rstrip() + "\n" + row + "\n", encoding="utf-8")

def url_import(args, data):
    url = args.url.strip(); match = re.match(r"^https?://([^/]+)(/[^?#]*)?", url, re.I)
    if not match: raise SystemExit("--url must be an http(s) URL")
    host, path = match.group(1).lower(), re.sub(r"/\.git$", "", (match.group(2) or "").rstrip("/"))
    canonical = f"https://{host}{path}"
    existing = next((x for x in data.get("tools", []) if x.get("url") == canonical or x.get("canonical_url") == canonical), None)
    if not args.no_vault_write:
        COLLECTED.mkdir(parents=True, exist_ok=True); note = COLLECTED / f"{slugify(args.title or host + path)}.md"
        body = f"# {args.title or host}\n\n{args.text or 'Saved source for the asset vault.'}\n\n- link: {canonical}\n- 形態: {args.kind}\n\n## 实际に使ったメモ\n_待使用。_\n"
        if note.exists():
            previous = note.read_text(encoding="utf-8")
            if canonical not in previous:
                note.write_text(previous.rstrip() + f"\n\n## Additional source\n- link: {canonical}\n- 形態: {args.kind}\n", encoding="utf-8")
        else:
            note.write_text(body, encoding="utf-8")
        update_collected_readme(title=args.title or host, canonical=canonical, kind=args.kind, note=note)
    if not existing: data.setdefault("tools", []).append({"id": f"URL-{len(data.get('tools', []))+1:03d}", "name": args.title or host, "category": args.kind, "platforms": ["web"], "canonical_url": canonical, "track": args.text or "Saved via vault_ingest.py"})
    if args.text:
        sync_design_catalog(args, text=args.text)
    return {"mode":"url", "url":canonical, "deduped": bool(existing)}

def text_import(args, data):
    sync_design_catalog(args, text=args.text)
    entry = {"id": f"TEXT-{datetime.now(timezone.utc).strftime('%Y%m%d%H%M%S')}", "name": args.title or args.text[:60], "category": args.kind, "source_prompt_zh": args.text, "created_at": datetime.now(timezone.utc).isoformat()}
    target = "patterns" if args.kind == "pattern" else "cards"; data.setdefault(target, []).append(entry)
    return {"mode":"text", "id":entry["id"]}

def main():
    p=argparse.ArgumentParser(); group=p.add_mutually_exclusive_group(); group.add_argument("--image"); group.add_argument("--url")
    p.add_argument("--title"); p.add_argument("--text", dest="text", default=None); p.add_argument("--kind", choices=["tool","inspiration","vault","pattern"], default="inspiration"); p.add_argument("--archetype-ref"); p.add_argument("--platform", default=""); p.add_argument("--measure-palette", action="store_true"); p.add_argument("--no-vault-write", action="store_true"); p.add_argument("--no-build", action="store_true"); p.add_argument("--commit", action="store_true"); p.add_argument("--push", action="store_true")
    args=p.parse_args()
    if not args.image and not args.url and not args.text: p.error("one of --image, --url, or --text is required")
    data=load(); result=image_import(args,data) if args.image else url_import(args,data) if args.url else text_import(args,data)
    data["updated_at"] = datetime.now(timezone.utc).isoformat(); save(data); maybe_build(args)
    if args.commit:
        subprocess.run(["git","add","vault","assets/vault/shots","vault/index.html"], cwd=ROOT, check=True); subprocess.run(["git","commit","-m","chore: ingest asset vault item"], cwd=ROOT, check=True)
    if args.push:
        branch=subprocess.check_output(["git","branch","--show-current"], cwd=ROOT, text=True).strip(); subprocess.run(["git","push","origin",branch], cwd=ROOT, check=True)
    print(json.dumps(result, ensure_ascii=False))
if __name__ == "__main__": main()
