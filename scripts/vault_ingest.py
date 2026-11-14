#!/usr/bin/env python3
"""Portable multimodal importer for the blog asset vault."""
from __future__ import annotations
import argparse, hashlib, html, json, os, re, shutil, subprocess, sys
from urllib.parse import urlsplit
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
        return f"https://github.com/{parts[0]}/{parts[1].removesuffix('.git')}"
    if host in {'twitter.com','www.twitter.com','x.com','www.x.com'} and len(parts)>=3 and parts[1].lower()=='status':
        return f"https://x.com/{parts[0]}/status/{parts[2]}"
    path='/' + '/'.join(parts) if parts else ''
    return f"https://{host}{path}"

def url_import(args, data):
    canonical = canonical_url(args.url)
    parsed = urlsplit(canonical)
    label = args.title or parsed.netloc + parsed.path
    source_id = slugify(label)
    existing = next((x for x in data.get("sources", []) if x.get("source_uri") == canonical or x.get("canonical_url") == canonical), None)
    if not args.no_vault_write:
        COLLECTED.mkdir(parents=True, exist_ok=True); note = COLLECTED / f"{source_id}.md"
        body = f"# {label}\n\n{args.text or 'Saved source for the asset vault.'}\n\n- link: {canonical}\n- 形態: {args.kind}\n\n## 实际に使ったメモ\n_待使用。_\n"
        if note.exists():
            previous = note.read_text(encoding="utf-8")
            if canonical not in previous:
                note.write_text(previous.rstrip() + f"\n\n## Additional source\n- link: {canonical}\n- 形態: {args.kind}\n", encoding="utf-8")
        else:
            note.write_text(body, encoding="utf-8")
        update_collected_readme(title=label, canonical=canonical, kind=args.kind, note=note)
    if not existing: data.setdefault("sources", []).append({"source_id": source_id, "name": label, "source_uri": canonical, "canonical_url": canonical, "form": "url", "kind": args.kind, "design_integration": "pending catalog sync" if args.text else "not requested", "learning_state": "not_recorded", "core_usage": args.text or "Saved via vault_ingest.py", "reference_links": [canonical]})
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

def source_prose(value: str) -> str:
    value = re.sub(r"<br\s*/?>", "\n", value, flags=re.I)
    value = re.sub(r"!\[[^]]*\]\([^)]*\)", "", value)
    value = re.sub(r"\[([^]]+)\]\([^)]*\)", r"\1", value)
    value = re.sub(r"</?(?:a|div|p|span|img|h[1-6]|strong|em|code|pre|ul|ol|li)\b[^>]*>", "", value, flags=re.I)
    return html.unescape(value.replace("`", "").replace("**", "").replace(r"\|", "|")).strip()


def source_links(text: str) -> list[str]:
    links = []
    text = re.sub(r"!\[[^]]*\]\([^)]*\)", "", text)
    for match in re.findall(r"https?://[^\s<>\"'`]+", html.unescape(text)):
        url = match.rstrip(").,;:!?]}")
        try:
            host = (urlsplit(url).hostname or "").lower()
        except ValueError:
            continue
        if not host or host in {"localhost", "127.0.0.1", "::1", "shields.io"} or host.endswith((".localhost", ".shields.io")):
            continue
        if url not in links:
            links.append(url)
    return links


def source_table_rows(text: str) -> dict[str, dict]:
    """Read only the two authoritative top-level routing/state tables."""
    rows = {}
    headers = []
    state = table = ""
    for number, line in enumerate(text.splitlines(), 1):
        if line.startswith("## "):
            headers = []
            heading = re.search(r"(Table [12]).*learning_state\s*=\s*(learned|queued)", line)
            table, state = heading.groups() if heading else ("", "")
        if not state or not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in re.split(r"(?<!\\)\|", line.strip().strip("|"))]
        if any("(`source_id`)" in cell for cell in cells):
            headers = [re.search(r"`([^`]+)`", cell).group(1) if "`" in cell else cell for cell in cells]
        elif headers and len(cells) == len(headers) and not re.fullmatch(r"[-: ]+", cells[0]):
            row = dict(zip(headers, cells))
            source_id = source_prose(row["source_id"])
            if source_id in rows:
                raise SystemExit(f"duplicate source table entry: {source_id}")
            rows[source_id] = {**row, "learning_state": state, "table": table, "line": number}
    if not rows:
        raise SystemExit("no collected-tools routing/state table rows found")
    return rows


def refresh_source_snapshot(data, directory: Path):
    names = ("README.md", "hallmark.md", "tenfold-design-skill.md")
    inputs = {name: (directory / name).read_text(encoding="utf-8") for name in names}
    rows = source_table_rows(inputs["README.md"])
    sources = {source["source_id"]: source for source in data.get("sources", [])}
    for source_id, row in rows.items():
        route_key = "design_integration" if row["learning_state"] == "learned" else "design_routing_ref"
        source = {
            "source_id": source_id,
            "source_uri": canonical_url(source_prose(row["source_uri"])),
            "local_path": source_prose(row["local_path"]),
            "form": "repo",
            "design_integration": source_prose(row[route_key]),
            "learning_state": row["learning_state"],
            "learning_evidence": f"README.md:{row['line']} · {row['table']} · learning_state = {row['learning_state']}",
        }
        if row["learning_state"] == "queued":
            question, _, why_now = row["question"].partition("<br>")
            source.update(design_routing_ref=source["design_integration"], topic_key=source_prose(row["topic_key"]),
                          question=re.sub(r"^问题[：:]\s*", "", source_prose(question)),
                          why_now=re.sub(r"^证据[：:]\s*", "", source_prose(why_now)))
            source["core_usage"] = source["question"]
        else:
            source["reconciliation"] = source_prose(row["对账结论"])
            source["core_usage"] = source["reconciliation"]
        source["reference_links"] = [source["source_uri"]]
        sources[source_id] = source

    def note_field(text, label):
        match = re.search(rf"^- {re.escape(label)}[:：]\s*(.+)$", text, re.M)
        return source_prose(match.group(1)) if match else ""

    for source_id, name in (("hallmark", "hallmark.md"), ("tenfold", "tenfold-design-skill.md")):
        text = inputs[name]
        if source_id == "tenfold" and source_id not in rows:
            if name not in inputs["README.md"]:
                raise SystemExit("Tenfold note is not registered in collected-tools/README.md")
            paragraphs = text.split("\n\n")
            summary = next(p for p in paragraphs if p.strip() and not p.startswith("#"))
            repo = canonical_url(note_field(text, "リポジトリ"))
            sources[source_id] = {
                "source_id": source_id, "source_uri": repo,
                "local_path": name + (" + repos/tenfold" if (directory / "repos/tenfold").is_dir() else ""),
                "learning_state": "not_recorded",
                "learning_evidence": "README.md registers the note but neither learning_state table classifies tenfold.",
                "design_integration": note_field(text, "本地适配"),
                "core_usage": source_prose(summary),
                "usage_notes": note_field(text, "外部 workflow"),
            }
        source = sources[source_id]
        source["form"] = note_field(text, "形態")
        source["reference_links"] = source_links(source["source_uri"] + "\n" + text)
        source["note_path"] = name
        if "## 实际に使ったメモ" in text:
            source["usage_state"] = source_prose(text.split("## 实际に使ったメモ", 1)[1]).strip("_").strip()
        if source_id == "hallmark":
            workflow = text.split("## 核心 3 ステップワークフロー", 1)[1].split("\n## ", 1)[0]
            source["usage_notes"] = source_prose(workflow.split("\n", 1)[1])
    data["sources"] = [sources[key] for key in sorted(sources)]
    data["source_inventory_count"] = len(data["sources"])
    data["source_snapshot"] = {"inputs": [{"path": f"Personal/collected-tools/{name}", "sha256": hashlib.sha256(text.encode()).hexdigest()} for name, text in inputs.items()],
                               "boundary": "Top-level tables and Hallmark/Tenfold notes only; no repo README scraping or knowledge-vault reads."}
    return {"mode": "refresh-sources", "source_count": len(data["sources"])}


def commit_changes():
    allowed = {"scripts/vault_ingest.py", "scripts/README.md", "build_site.py", "index.html", "vault/manifest.json", "vault/index.html"}
    allowed.update(str(path.relative_to(ROOT)) for path in SHOTS.glob("*") if path.is_file())
    staged = subprocess.check_output(["git", "diff", "--cached", "--name-only", "-z"], cwd=ROOT, text=True).split("\0")
    if set(filter(None, staged)) - allowed:
        raise SystemExit("refusing --commit: unrelated staged paths exist")
    changed = subprocess.check_output(["git", "diff", "HEAD", "--name-only", "-z"], cwd=ROOT, text=True).split("\0")
    untracked = subprocess.check_output(["git", "ls-files", "--others", "--exclude-standard", "-z"], cwd=ROOT, text=True).split("\0")
    paths = sorted(path for path in allowed & set(changed + untracked) if (ROOT / path).is_file())
    if not paths:
        raise SystemExit("no importer/build changes to commit")
    subprocess.run(["git", "add", "--", *paths], cwd=ROOT, check=True)
    subprocess.run(["git", "commit", "-m", "chore: ingest asset vault item", "-m", "Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>"], cwd=ROOT, check=True)


def main():
    p=argparse.ArgumentParser(); group=p.add_mutually_exclusive_group(); group.add_argument("--image"); group.add_argument("--url"); group.add_argument("--refresh-sources", action="store_true", help="refresh the offline source snapshot from top-level collected-tools tables/notes (read-only)")
    p.add_argument("--title"); p.add_argument("--text", dest="text", default=None); p.add_argument("--kind", choices=["tool","inspiration","vault","pattern"], default="inspiration"); p.add_argument("--archetype-ref"); p.add_argument("--platform", default=""); p.add_argument("--measure-palette", dest="measure_palette", action="store_true", default=True); p.add_argument("--no-measure-palette", dest="measure_palette", action="store_false"); p.add_argument("--no-vault-write", action="store_true"); p.add_argument("--no-build", action="store_true"); p.add_argument("--commit", action="store_true"); p.add_argument("--push", action="store_true")
    args=p.parse_args()
    if not args.image and not args.url and not args.text and not args.refresh_sources: p.error("one of --image, --url, --text, or --refresh-sources is required")
    if args.refresh_sources and args.text: p.error("--refresh-sources cannot be combined with --text")
    data=load()
    result=refresh_source_snapshot(data, COLLECTED) if args.refresh_sources else image_import(args,data) if args.image else url_import(args,data) if args.url else text_import(args,data)
    if not args.refresh_sources:
        data["updated_at"] = datetime.now(timezone.utc).isoformat()
    save(data); maybe_build(args)
    if args.commit:
        commit_changes()
    if args.push:
        publishing_branch(); subprocess.run(["git","push","origin","master"], cwd=ROOT, check=True)
    print(json.dumps(result, ensure_ascii=False))
if __name__ == "__main__": main()
