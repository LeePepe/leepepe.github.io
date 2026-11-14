import json, shutil, tempfile, unittest
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
