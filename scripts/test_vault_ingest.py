import copy, json, shutil, subprocess, tempfile, unittest
from pathlib import Path
from unittest.mock import patch
from PIL import Image
import sys
from types import SimpleNamespace
sys.path.insert(0, str(Path(__file__).parent))
import vault_ingest

class VaultIngestTests(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix='vault-test-', dir=Path.cwd()))
        self.manifest = self.tmp/'manifest.json'; self.shots = self.tmp/'shots'; self.collected = self.tmp/'collected'
        self.manifest.write_text(json.dumps({'schema_version':1,'screenshots':[],'cards':[],'patterns':[],'tools':[],'toolchains':[]}))
        self.patches = [patch.object(vault_ingest, 'MANIFEST', self.manifest), patch.object(vault_ingest, 'SHOTS', self.shots), patch.object(vault_ingest, 'COLLECTED', self.collected), patch.object(vault_ingest, 'sync_design_catalog')]
        for p in self.patches: p.start()
    def tearDown(self):
        for p in self.patches: p.stop()
        shutil.rmtree(self.tmp, ignore_errors=True)
    def test_image_creates_full_thumb_palette_and_ocr_gracefully(self):
        source=self.tmp/'source.png'; Image.new('RGB',(1400,1000),(20,40,80)).save(source)
        args=type('Args',(),{'image':str(source),'title':'Sample Shot','measure_palette':True,'archetype_ref':'VS-005','platform':'desktop','text':'note'})()
        data=vault_ingest.load()
        with patch.object(vault_ingest, 'ocr_result', return_value={'text':'','status':'empty_text','error':''}):
            result=vault_ingest.image_import(args, data)
        self.assertEqual(result['mode'],'image'); self.assertEqual(len(data['screenshots']),1)
        shot=data['screenshots'][0]; self.assertTrue((self.shots / Path(shot['image']).name).exists()); self.assertTrue((self.shots / Path(shot['thumbnail']).name).exists()); self.assertLessEqual(len(shot['measured_palette']),6)
    def test_url_dedupes_canonical_source_and_writes_note(self):
        args=type('Args',(),{'url':'https://github.com/acme/demo/tree/main/docs?x=1','title':'Demo','text':'use it','kind':'tool','no_vault_write':False})()
        data=vault_ingest.load(); vault_ingest.url_import(args,data); vault_ingest.url_import(args,data)
        self.assertEqual(len(data['sources']),1); self.assertEqual(data['sources'][0]['source_uri'],'https://github.com/acme/demo'); self.assertTrue(list(self.collected.glob('*.md'))); self.assertIn('https://github.com/acme/demo', (self.collected/'README.md').read_text())
        self.assertEqual(vault_ingest.canonical_url('https://twitter.com/name/status/123?x=1'),'https://x.com/name/status/123')
        self.assertNotEqual(vault_ingest.canonical_url('https://example.com/a'),vault_ingest.canonical_url('https://example.com/b'))
    def test_url_without_title_uses_canonical_label_and_preserves_notes(self):
        data = vault_ingest.load()
        for raw, canonical in [
            ('https://github.com/acme/demo.git/tree/main/docs?ref=1', 'https://github.com/acme/demo'),
            ('https://twitter.com/designer/status/123/photo/1?ref=1', 'https://x.com/designer/status/123'),
            ('https://example.com/design/reference?ref=1', 'https://example.com/design/reference'),
        ]:
            with self.subTest(raw=raw):
                label = canonical.removeprefix('https://')
                note = self.collected / (vault_ingest.slugify(label) + '.md')
                self.collected.mkdir(exist_ok=True)
                note.write_text('# Owner notes\n\nKeep this original wording.\n')
                args = SimpleNamespace(url=raw, title=None, text=None, kind='tool', no_vault_write=False)
                first = vault_ingest.url_import(args, data)
                preserved = note.read_text()
                second = vault_ingest.url_import(args, data)
                self.assertFalse(first['deduped']); self.assertTrue(second['deduped'])
                self.assertEqual(second['url'], canonical)
                self.assertEqual(note.read_text(), preserved)
                self.assertIn('Keep this original wording.', preserved)
                self.assertIn(canonical, preserved)
                source = next(s for s in data['sources'] if s['source_uri'] == canonical)
                self.assertEqual(source['name'], label)
                self.assertEqual(source['source_id'], note.stem)
        self.assertEqual(len(data['sources']), 3)

    def git(self, *args):
        return subprocess.check_output(['git', *args], cwd=self.tmp, text=True, stderr=subprocess.STDOUT).strip()

    def prepare_git_fixture(self):
        self.git('init', '-b', 'master')
        self.git('config', 'user.name', 'Vault Test'); self.git('config', 'user.email', 'vault-test@example.invalid')
        paths = ['index.html', 'vault/index.html', 'vault/manifest.json', 'assets/vault/shots/sample.png', 'unrelated.txt']
        for name in paths:
            path = self.tmp / name; path.parent.mkdir(parents=True, exist_ok=True); path.write_text('before\n')
        self.git('add', '--', *paths); self.git('commit', '-qm', 'fixture')
        for name in paths:
            (self.tmp / name).write_text('after\n')
        (self.tmp / 'unrelated-untracked.txt').write_text('not importer output\n')
        return patch.multiple(vault_ingest, ROOT=self.tmp, SHOTS=self.tmp / 'assets/vault/shots')

    def test_commit_stages_root_vault_and_assets_but_not_unrelated_changes(self):
        with self.prepare_git_fixture():
            vault_ingest.commit_changes()
            self.assertEqual(set(self.git('show', '--pretty=', '--name-only', 'HEAD').splitlines()),
                             {'index.html', 'vault/index.html', 'vault/manifest.json', 'assets/vault/shots/sample.png'})
            self.assertIn('Co-authored-by: Copilot', self.git('log', '-1', '--pretty=%B'))
            self.assertEqual(self.git('diff', '--cached', '--name-only'), '')
            self.assertEqual(self.git('diff', '--name-only'), 'unrelated.txt')
            self.assertIn('unrelated-untracked.txt', self.git('ls-files', '--others', '--exclude-standard'))
            self.assertEqual(vault_ingest.publishing_branch(), 'master')
            for checkout in [('checkout', '-qb', 'feat/test'), ('checkout', '-q', '--detach', 'master')]:
                self.git(*checkout)
                with self.assertRaisesRegex(SystemExit, 'publishing master'):
                    vault_ingest.publishing_branch()

    def test_commit_refuses_unrelated_staged_change_before_staging_outputs(self):
        with self.prepare_git_fixture():
            self.git('add', '--', 'unrelated.txt')
            head = self.git('rev-parse', 'HEAD')
            with self.assertRaisesRegex(SystemExit, 'unrelated staged paths'):
                vault_ingest.commit_changes()
            self.assertEqual(self.git('diff', '--cached', '--name-only'), 'unrelated.txt')
            self.assertEqual(self.git('rev-parse', 'HEAD'), head)

    def test_source_snapshot_uses_only_top_level_table_and_note_authority(self):
        self.collected.mkdir()
        (self.collected / 'README.md').write_text('''# Index
## Table 1 — learning_state = learned
| # | 来源实体 (`source_id`) | `source_uri` | `local_path` | `design_integration` | `coverage_refs` | 对账结论 |
|---|---|---|---|---|---|---|
| 1 | `hallmark` | `https://github.com/Nutlope/hallmark` | [hallmark.md](hallmark.md) + `repos/hallmark` | `web.json` (`T-021`/`IP-007`) + `DC-009` | [private](../knowledge-vault/must-not-read.md) | 已完成反 AI 模板感 3 步解剖设计与多视口门禁沉淀 |
## Table 2 — learning_state = queued
| # | 来源实体 (`source_id`) | `topic_key` | `source_uri` | `local_path` | `design_routing_ref` | `coverage_refs` | 具体问题 (`question`) 与 (`why_now`) |
|---|---|---|---|---|---|---|---|
| 1 | `bama` | `agent-cli` | `https://github.com/daveebbelaar/bama` | `repos/bama` | `verify_design_cases.py` (`allowed_native.bama_macos_only`) + `design_catalog.py` (`measure.swift`) | `[]` | **问题**：BAMA 怎样验证用户故事？<br>**证据**：`repos/bama/README.md:42-65`（仅摄取测色板） |

| [tenfold-design-skill.md](tenfold-design-skill.md) | design skill | divergent mobile directions |
''')
        (self.collected / 'hallmark.md').write_text('''# Hallmark

A real-browser design workflow.

- link: https://www.usehallmark.com/`)
- 形態: skill / plugin / real-browser linter

## 核心 3 ステップワークフロー (3-Step)

1. Choose three themes, then anatomy and browser audit.

## 实际に使ったメモ

已集成。
''')
        xlinks = [f'https://x.com/adrian_partain/status/{n}' for n in range(101, 106)]
        (self.collected / 'tenfold-design-skill.md').write_text('''# Tenfold

Explore genuinely different mobile directions before selecting one; keep `handoff/<goal>/r<N>/` offline.

- リポジトリ: https://github.com/adrianpartain59/tenfold
- 形態: Claude Code plugin / design skill
- 本地适配: `my-designer` Mode A or Mode B; freeze `AppTheme` + `design.md`.
- 外部 workflow: pick + notes, then ten more.

## 参考链接

''' + '\n'.join(f'{i}. {url}\"]' for i, url in enumerate(xlinks, 1)) + '''
https://img.shields.io/badge/not-a-reference
![badge](https://badges.example/anything.svg)
http://localhost:4545/<project>

## 实际に使ったメモ

_(まだ未使用。試したらここに追記)_
''')
        allowed = {self.collected / name for name in ('README.md', 'hallmark.md', 'tenfold-design-skill.md')}
        read_text = Path.read_text
        def guarded_read(path, *args, **kwargs):
            self.assertIn(path, allowed, 'snapshot must not read repo README or knowledge-vault')
            return read_text(path, *args, **kwargs)
        data = {'cards': [{'id': 'CL-001'}], 'sources': []}
        with patch.object(Path, 'read_text', guarded_read):
            vault_ingest.refresh_source_snapshot(data, self.collected)
            before = copy.deepcopy(data)
            vault_ingest.refresh_source_snapshot(data, self.collected)
        self.assertEqual(data, before)
        sources = {s['source_id']: s for s in data['sources']}
        self.assertEqual(data['cards'], [{'id': 'CL-001'}])
        self.assertEqual(sources['bama']['design_routing_ref'], 'verify_design_cases.py (allowed_native.bama_macos_only) + design_catalog.py (measure.swift)')
        self.assertEqual(sources['bama']['question'], 'BAMA 怎样验证用户故事？')
        self.assertEqual(sources['bama']['core_usage'], sources['bama']['question'])
        self.assertEqual(sources['bama']['why_now'], 'repos/bama/README.md:42-65（仅摄取测色板）')
        self.assertEqual(sources['bama']['learning_state'], 'queued')
        self.assertEqual(sources['hallmark']['core_usage'], '已完成反 AI 模板感 3 步解剖设计与多视口门禁沉淀')
        self.assertEqual(sources['hallmark']['learning_state'], 'learned')
        self.assertIn('https://www.usehallmark.com/', sources['hallmark']['reference_links'])
        self.assertEqual(sources['tenfold']['learning_state'], 'not_recorded')
        self.assertIn('my-designer Mode A or Mode B', sources['tenfold']['design_integration'])
        self.assertIn('handoff/<goal>/r<N>/', sources['tenfold']['core_usage'])
        self.assertEqual(sources['tenfold']['reference_links'], ['https://github.com/adrianpartain59/tenfold', *xlinks])
        self.assertIn('まだ未使用。', sources['tenfold']['usage_state'])
        self.assertEqual(data['source_inventory_count'], 3)
        self.assertEqual(len(data['source_snapshot']['inputs']), 3)

    def test_source_rendering_counts_entities_without_duplicate_catalog_section(self):
        sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
        import build_site
        root = self.tmp / 'site'; (root / 'vault').mkdir(parents=True)
        data = {'cards': [], 'screenshots': [], 'patterns': [], 'tools': [{'id': 'T-001'}, {'id': 'T-002'}],
                'toolchains': [{'id': 'T-001', 'name': 'Only toolchain'}],
                'sources': [{'source_id': 'bama', 'source_uri': 'https://github.com/daveebbelaar/bama', 'learning_state': 'queued',
                             'core_usage': '怎样验证用户故事？', 'question': '怎样验证用户故事？', 'why_now': 'README.md:42',
                             'design_routing_ref': 'measure.swift'}]}
        (root / 'vault/manifest.json').write_text(json.dumps(data))
        with patch.object(build_site, 'REPO_ROOT', root):
            build_site.build_vault_page()
        rendered = (root / 'vault/index.html').read_text()
        self.assertNotIn('id="vault-tools"', rendered); self.assertNotIn('data-type="tool"', rendered)
        self.assertEqual(rendered.count('data-type="source"'), 1)
        self.assertEqual(rendered.count('data-type="toolchain"'), 1)
        self.assertIn('<span>外部工具与参考库</span><strong>1</strong>', rendered)
        self.assertIn('待探索问题：</strong>怎样验证用户故事？', rendered)
        self.assertIn('来源定位：</strong>README.md:42', rendered)
        self.assertIn('设计路由：</strong>measure.swift', rendered)

    def test_text_import_is_structured(self):
        args=type('Args',(),{'text':'undoable interaction','title':'Undo','kind':'pattern'})()
        self.patches[-1].stop()
        with patch.object(vault_ingest, 'sync_design_catalog', return_value=SimpleNamespace(stdout='{"created_cards":[{"id":"IP-999","name":"Undo","source_prompt_zh":"undoable interaction","state_machine":"idle -> commit -> settle"}]}')):
            data=vault_ingest.load(); result=vault_ingest.text_import(args,data)
        self.assertEqual(result['mode'],'text'); self.assertEqual(data['patterns'][0]['source_prompt_zh'],'undoable interaction'); self.assertEqual(data['patterns'][0]['state_machine'],'idle -> commit -> settle')

    def test_rejects_non_png_jpeg_and_non_publishing_push(self):
        bad=self.tmp/'bad.gif'; bad.write_bytes(b'GIF89a')
        args=type('Args',(),{'image':str(bad),'title':'bad','measure_palette':True,'archetype_ref':None,'platform':'','text':'','no_vault_write':True})()
        with self.assertRaises(SystemExit): vault_ingest.image_import(args, vault_ingest.load())
        with patch.object(vault_ingest.subprocess, 'check_output', return_value='feat/blog-asset-vault\n'):
            with self.assertRaises(SystemExit): vault_ingest.publishing_branch()

    def test_ocr_empty_is_distinct_from_runtime_failure(self):
        if sys.platform != 'darwin': self.skipTest('Vision is macOS-only')
        ok=SimpleNamespace(returncode=0,stdout='',stderr='')
        with patch.object(vault_ingest.subprocess,'run',return_value=ok):
            self.assertEqual(vault_ingest.ocr_result(self.tmp/'x.png')['status'],'empty_text')
        fail=SimpleNamespace(returncode=2,stdout='',stderr='bad image')
        with patch.object(vault_ingest.subprocess,'run',return_value=fail):
            with self.assertRaises(SystemExit): vault_ingest.ocr_result(self.tmp/'x.png')

    def test_catalog_command_routes_image_text_and_pattern(self):
        fake=SimpleNamespace(stdout='{}')
        self.patches[-1].stop()
        with patch.object(vault_ingest.subprocess, 'run', return_value=fake) as run:
            vault_ingest.sync_design_catalog(type('Args',(),{'no_vault_write':False,'archetype_ref':'VS-005','kind':'inspiration'})(), image=self.tmp/'x.png')
            image_command=run.call_args[0][0]; self.assertIn('vault-ingest', image_command); self.assertIn('--measure-palette', image_command)
            vault_ingest.sync_design_catalog(type('Args',(),{'no_vault_write':False,'archetype_ref':None,'kind':'pattern'})(), text='pattern')
            pattern_command=run.call_args[0][0]; self.assertIn('ingest', pattern_command); self.assertIn('--text', pattern_command)

    def test_build_hook_is_default_and_skippable(self):
        with patch.object(vault_ingest.subprocess, 'run') as run:
            vault_ingest.maybe_build(type('Args',(),{'no_build':False})())
            run.assert_called_once()
        with patch.object(vault_ingest.subprocess, 'run') as run:
            vault_ingest.maybe_build(type('Args',(),{'no_build':True})())
            run.assert_not_called()

if __name__ == '__main__': unittest.main()
