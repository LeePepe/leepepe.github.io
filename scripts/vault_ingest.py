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
DESIGN_CATALOG_PATH = os.environ.get("DESIGN_CATALOG_PATH", str(Path.home() / ".copilot/skills/design-studio/references/catalog.json"))
BAMA_MEASURE = Path(os.environ.get("BAMA_MEASURE", str(Path.home() / "Development/Personal/collected-tools/repos/bama/skills/design/design-from-app/scripts/measure.swift")))

def slugify(value: str) -> str:
    value = re.sub(r"[^\w\-]+", "-", value.lower(), flags=re.UNICODE).strip("-")
    return value or "asset"

def palette(path: Path):
    if sys.platform == "darwin" and BAMA_MEASURE.is_file():
        try:
            result = subprocess.run(["swift", str(BAMA_MEASURE), "palette", str(path)], capture_output=True, text=True, timeout=30, check=True)
            measured=[]
            for line in result.stdout.splitlines():
                match=re.match(r"(#[0-9A-Fa-f]{6})\s+([0-9.]+)%", line.strip())
                if match: measured.append({"hex":match.group(1).upper(),"pct":float(match.group(2))})
            if measured: return measured[:6]
        except (OSError, subprocess.SubprocessError):
            pass
    if Image is None: raise SystemExit("Pillow is required for validated RGB/RGBA PNG/JPEG palette fallback")
    try:
        with Image.open(path) as source:
            if source.format not in {"PNG", "JPEG"}: raise SystemExit("palette supports PNG and JPEG images only")
            image = source.convert("RGB"); image.thumbnail((300, 300))
            quantized = image.quantize(colors=6, method=Image.Quantize.MEDIANCUT)
            colors = quantized.getcolors(image.width * image.height) or []
            raw = quantized.getpalette(); total = sum(n for n, _ in colors) or 1
            return [{"hex": "#%02X%02X%02X" % tuple(raw[i * 3:i * 3 + 3]), "pct": round(n / total * 100, 1)} for n, i in sorted(colors, reverse=True)[:6]]
    except (OSError, ValueError) as exc:
        raise SystemExit(f"palette measurement failed for {path}: {exc}") from exc

def ocr_result(path: Path) -> dict[str, str]:
    """Return recognized, empty, or unavailable; runtime failures are surfaced."""
    if sys.platform != "darwin": return {"text":"", "status":"unavailable", "error":"Vision requires macOS"}
    swift = '''import Vision
import AppKit
let u = URL(fileURLWithPath: CommandLine.arguments[1])
guard let image = NSImage(contentsOf: u) else { fputs("cannot read image\\n", stderr); exit(2) }
var r = CGRect.zero
guard let rep = image.representations.first, let c = rep.cgImage(forProposedRect: &r, context: nil, hints: nil) else { fputs("cannot create CGImage\\n", stderr); exit(2) }
let req = VNRecognizeTextRequest { request, _ in
    print((request.results as? [VNRecognizedTextObservation] ?? []).compactMap { $0.topCandidates(1).first?.string }.joined(separator: " "))
}
req.recognitionLevel = .fast
do { try VNImageRequestHandler(cgImage: c, options: [:]).perform([req]) } catch { fputs("\\(error.localizedDescription)\\n", stderr); exit(3) }'''
    try:
        result = subprocess.run(["swift", "-e", swift, str(path)], capture_output=True, text=True, timeout=30)
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise SystemExit(f"Vision OCR failed for {path}: {exc}") from exc
    if result.returncode != 0:
        raise SystemExit(f"Vision OCR failed for {path}: {result.stderr.strip() or 'swift exited non-zero'}")
    text=result.stdout.strip()
    return {"text":text, "status":"recognized_text" if text else "empty_text", "error":""}

def ocr(path: Path) -> str:
    return ocr_result(path)["text"]

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
    if is_pattern:
        command += ["--catalog", DESIGN_CATALOG_PATH]
    if image:
        command += ["--image", str(image), "--measure-palette"]
        if getattr(args, "archetype_ref", None): command += ["--archetype-ref", args.archetype_ref]
    else:
        command += ["--text", text or ""]
    return subprocess.run(command, cwd=ROOT, check=True, capture_output=True, text=True)

def maybe_build(args):
    if not args.no_build:
        subprocess.run([sys.executable, str(ROOT / "build_site.py")], cwd=ROOT, check=True)

def publishing_branch():
    branch=subprocess.check_output(["git","branch","--show-current"], cwd=ROOT, text=True).strip()
    if branch != "master": raise SystemExit("refusing --push: only the publishing master branch is allowed")
    return branch

def image_import(args, data):
    source = Path(args.image).expanduser().resolve()
    if not source.is_file(): raise SystemExit(f"image not found: {source}")
    if Image is None: raise SystemExit("Pillow is required for image import")
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    stem = f"{stamp}-{slugify(args.title or source.stem)}"; ext = source.suffix.lower() if source.suffix.lower() in {".png", ".jpg", ".jpeg"} else ".png"
    SHOTS.mkdir(parents=True, exist_ok=True); dest = SHOTS / (stem + ext); thumb = SHOTS / (stem + "-thumb" + ext)
    try:
        with Image.open(source) as image:
            if image.format not in {"PNG", "JPEG"}: raise SystemExit("image import supports PNG and JPEG files only")
            image.convert("RGBA" if ext == ".png" else "RGB").save(dest)
            small = image.copy(); small.thumbnail((960, 960), Image.Resampling.LANCZOS); small.convert("RGBA" if ext == ".png" else "RGB").save(thumb)
            width, height = image.size
    except (OSError, ValueError) as exc:
        raise SystemExit(f"image import failed for {source}: {exc}") from exc
    sync_design_catalog(args, image=dest)
    ocr_data=ocr_result(dest)
    data["screenshots"].append({"id": stem, "title": args.title or source.stem, "image": f"/assets/vault/shots/{dest.name}", "thumbnail": f"/assets/vault/shots/{thumb.name}", "width": width, "height": height, "measured_palette": palette(dest) if getattr(args, "measure_palette", True) else [], "ocr_text": ocr_data["text"], "ocr_status": ocr_data["status"], "ocr_error": ocr_data["error"], "archetype_ref": args.archetype_ref, "platform": args.platform.split(",") if args.platform else [], "notes": args.text or "Imported by vault_ingest.py."})
    return {"mode":"image", "id":stem}

def update_collected_readme(*, title, canonical, kind, note):
    readme = COLLECTED / "README.md"
    if not readme.exists():
        readme.write_text("# Collected Tools\n\n| file | 种別 | one-line summary |\n|---|---|---|\n", encoding="utf-8")
    text = readme.read_text(encoding="utf-8")
    row = f"| [{note.name}]({note.name}) | {kind} | {canonical} |"
    if canonical not in text:
        readme.write_text(text.rstrip() + "\n" + row + "\n", encoding="utf-8")

def canonical_url(raw: str) -> str:
    match = re.match(r"^https?://([^/]+)(/[^?#]*)?", raw.strip(), re.I)
    if not match: raise SystemExit("--url must be an http(s) URL")
    host=match.group(1).lower(); parts=[p for p in (match.group(2) or '').split('/') if p]
    if host in {'github.com','www.github.com'} and len(parts)>=2:
        return f"https://github.com/{parts[0]}/{re.sub(r'\\.git$','',parts[1])}"
    if host in {'twitter.com','www.twitter.com','x.com','www.x.com'} and len(parts)>=3 and parts[1].lower()=='status':
        return f"https://x.com/{parts[0]}/status/{parts[2]}"
    path='/' + '/'.join(parts) if parts else ''
    return f"https://{host}{path}"

def url_import(args, data):
    canonical = canonical_url(args.url)
    existing = next((x for x in data.get("sources", []) if x.get("source_uri") == canonical or x.get("canonical_url") == canonical), None)
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
    if not existing: data.setdefault("sources", []).append({"source_id": slugify(args.title or host + path), "name": args.title or host, "source_uri": canonical, "canonical_url": canonical, "form": "url", "kind": args.kind, "design_integration": "pending catalog sync" if args.text else "not requested", "learning_state": "not_recorded", "core_usage": args.text or "Saved via vault_ingest.py", "reference_links": [canonical]})
    if args.text:
        sync_design_catalog(args, text=args.text)
    return {"mode":"url", "url":canonical, "deduped": bool(existing)}

def text_import(args, data):
    result=sync_design_catalog(args, text=args.text)
    payload={}
    if result and result.stdout:
        try: payload=json.loads(result.stdout)
        except json.JSONDecodeError as exc: raise SystemExit(f"design catalog returned invalid JSON: {exc}") from exc
    created=payload.get("created_cards", []) if payload else []
    if not created: raise SystemExit("design catalog returned no structured card; refusing TEXT stub")
    target = "patterns" if args.kind == "pattern" else "cards"
    for entry in created:
        entry["created_at"]=datetime.now(timezone.utc).isoformat(); data.setdefault(target, []).append(entry)
    return {"mode":"text", "id":created[0].get("id"), "created_count":len(created), "route_stage":payload.get("route_stage")}

def main():
    p=argparse.ArgumentParser(); group=p.add_mutually_exclusive_group(); group.add_argument("--image"); group.add_argument("--url")
    p.add_argument("--title"); p.add_argument("--text", dest="text", default=None); p.add_argument("--kind", choices=["tool","inspiration","vault","pattern"], default="inspiration"); p.add_argument("--archetype-ref"); p.add_argument("--platform", default=""); p.add_argument("--measure-palette", dest="measure_palette", action="store_true", default=True); p.add_argument("--no-measure-palette", dest="measure_palette", action="store_false"); p.add_argument("--no-vault-write", action="store_true"); p.add_argument("--no-build", action="store_true"); p.add_argument("--commit", action="store_true"); p.add_argument("--push", action="store_true")
    args=p.parse_args()
    if not args.image and not args.url and not args.text: p.error("one of --image, --url, or --text is required")
    data=load(); result=image_import(args,data) if args.image else url_import(args,data) if args.url else text_import(args,data)
    data["updated_at"] = datetime.now(timezone.utc).isoformat(); save(data); maybe_build(args)
    if args.commit:
        allowed={"scripts/vault_ingest.py","scripts/README.md","build_site.py","vault/manifest.json","vault/index.html"}
        allowed.update(str(p.relative_to(ROOT)) for p in SHOTS.glob("*") if p.is_file())
        staged=subprocess.check_output(["git","diff","--cached","--name-only"], cwd=ROOT, text=True).splitlines()
        if set(staged)-allowed: raise SystemExit("refusing --commit: unrelated staged paths exist")
        subprocess.run(["git","add","--",*sorted(allowed)], cwd=ROOT, check=True)
        subprocess.run(["git","commit","-m","chore: ingest asset vault item"], cwd=ROOT, check=True)
    if args.push:
        publishing_branch(); subprocess.run(["git","push","origin","master"], cwd=ROOT, check=True)
    print(json.dumps(result, ensure_ascii=False))
if __name__ == "__main__": main()
