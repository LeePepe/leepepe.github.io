import json, tempfile, unittest
from pathlib import Path
from unittest.mock import patch
from PIL import Image
import sys
sys.path.insert(0, str(Path(__file__).parent))
import vault_ingest

class VaultIngestTests(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix='vault-test-', dir=Path.cwd()))
        self.manifest = self.tmp/'manifest.json'; self.shots = self.tmp/'shots'; self.collected = self.tmp/'collected'
        self.manifest.write_text(json.dumps({'schema_version':1,'screenshots':[],'cards':[],'patterns':[],'tools':[],'toolchains':[]}))
        self.patches = [patch.object(vault_ingest, 'MANIFEST', self.manifest), patch.object(vault_ingest, 'SHOTS', self.shots), patch.object(vault_ingest, 'COLLECTED', self.collected)]
        for p in self.patches: p.start()
    def tearDown(self):
        for p in self.patches: p.stop()
    def test_image_creates_full_thumb_palette_and_ocr_gracefully(self):
        source=self.tmp/'source.png'; Image.new('RGB',(1400,1000),(20,40,80)).save(source)
        args=type('Args',(),{'image':str(source),'title':'Sample Shot','measure_palette':True,'archetype_ref':'VS-005','platform':'desktop','text':'note'})()
        data=vault_ingest.load()
        with patch.object(vault_ingest, 'ocr', return_value=''):
            result=vault_ingest.image_import(args, data)
        self.assertEqual(result['mode'],'image'); self.assertEqual(len(data['screenshots']),1)
        shot=data['screenshots'][0]; self.assertTrue((self.shots / Path(shot['image']).name).exists()); self.assertTrue((self.shots / Path(shot['thumbnail']).name).exists()); self.assertLessEqual(len(shot['measured_palette']),6)
    def test_url_dedupes_canonical_source_and_writes_note(self):
        args=type('Args',(),{'url':'https://github.com/acme/demo/','title':'Demo','text':'use it','kind':'tool','no_vault_write':False})()
        data=vault_ingest.load(); vault_ingest.url_import(args,data); vault_ingest.url_import(args,data)
        self.assertEqual(len(data['tools']),1); self.assertTrue(list(self.collected.glob('*.md')))
    def test_text_import_is_structured(self):
        args=type('Args',(),{'text':'undoable interaction','title':'Undo','kind':'pattern'})()
        data=vault_ingest.load(); result=vault_ingest.text_import(args,data)
        self.assertEqual(result['mode'],'text'); self.assertEqual(data['patterns'][0]['source_prompt_zh'],'undoable interaction')

    def test_build_hook_is_default_and_skippable(self):
        with patch.object(vault_ingest.subprocess, 'run') as run:
            vault_ingest.maybe_build(type('Args',(),{'no_build':False})())
            run.assert_called_once()
        with patch.object(vault_ingest.subprocess, 'run') as run:
            vault_ingest.maybe_build(type('Args',(),{'no_build':True})())
            run.assert_not_called()

if __name__ == '__main__': unittest.main()
