#!/usr/bin/env python3
"""Install the stable Personal collected-tools entry point for this checkout."""
from pathlib import Path
import os
root = Path(__file__).resolve().parents[1]
out = Path(os.environ.get("COLLECTED_TOOLS_DIR", str(Path.home() / "Development/Personal/collected-tools"))) / "vault_ingest.py"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(f'''#!/usr/bin/env python3\nfrom pathlib import Path\nimport os, runpy, sys\nroot = Path(os.environ.get("BLOG_ASSET_VAULT_ROOT", {str(root)!r}))\nsys.path.insert(0, str(root / "scripts"))\nrunpy.run_path(str(root / "scripts" / "vault_ingest.py"), run_name="__main__")\n''', encoding="utf-8")
out.chmod(0o755)
print(out)
