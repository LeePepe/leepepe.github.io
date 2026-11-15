#!/usr/bin/env python3
"""Focused catalog and persisted observation regressions (stdlib + Node.js)."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import build_site


class DemoTests(unittest.TestCase):
    def test_scans_active_gallery_metadata_not_helpers_or_nested_rounds(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            sources = {
                'new-goal/index.html': '<title>A &amp; B</title><article data-variant="v01" data-category="pulse">macOS</article>',
                'another/index.html': '<script id="gallery-config" type="application/json">' + json.dumps({'cards': [{'category': 'voice', 'id': 'v02', 'platform': 'mobile', 'round': 3}]}) + '</script>',
                '_helper/index.html': '<article data-category="x" data-variant="v01"></article>',
                'retired/index.html': '<script id="gallery-config">{"active":false,"cards":[{"category":"old","id":"v01"}]}</script>',
                'new-goal/round/index.html': '<article data-category="x" data-variant="v01"></article>',
                '_sync_notes.html': '<title>Extraction helper</title>',
            }
            for name, text in sources.items():
                target = root / 'demos' / name
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(text)
            with patch.object(build_site, 'REPO_ROOT', root):
                projects = build_site.scan_demo_projects()
            self.assertEqual([p['goal'] for p in projects], ['another', 'new-goal'])
            self.assertEqual(projects[0]['platforms'], ['mobile'])
            self.assertEqual(projects[1]['title'], 'A & B')
            self.assertEqual(projects[1]['categories'], ['pulse'])
            self.assertEqual(projects[1]['platforms'], ['macos'])

    def test_group_id_fallback_malformed_config_and_round_deduplication(self):
        cases = {
            'broken': '<script id="gallery-config">{invalid</script>',
            'empty': '<script id="gallery-config">{"cards":[]}</script>',
            'nonobject': '<script id="gallery-config">null</script>',
            'unusable': '<script id="gallery-config">{"cards":[null,{"id":"x"},{"category":"pulse","id":"v02","round":[]},{"category":"","id":"v03"}]}</script>',
        }
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for goal, prefix in cases.items():
                target = root / 'demos' / goal / 'index.html'
                target.parent.mkdir(parents=True)
                target.write_text(prefix + '<article data-group="pulse" data-id="v01" data-round="5"></article>' * 2 + '<article data-group="pulse" data-id="v01" data-round="4"></article><article data-group="pulse" data-id="current"></article>')
            target = root / 'demos' / 'config' / 'index.html'
            target.parent.mkdir(parents=True)
            target.write_text('<script id="gallery-config">{"cards":[{"group":"roi","variant":"v02","round":5,"platform":"macos"},{"group":"roi","variant":"v02","round":5},{"group":"roi","variant":"current","reference":true}]}</script>')
            with patch.object(build_site, 'REPO_ROOT', root):
                projects = {p['goal']: p for p in build_site.scan_demo_projects()}
            for goal in cases:
                self.assertEqual([(c['category'], c['id'], c['round']) for c in projects[goal]['cards']], [('pulse', 'v01', '5'), ('pulse', 'v01', '4')])
            self.assertEqual(len(projects['config']['cards']), 1)
            self.assertEqual(projects['config']['cards'][0]['id'], 'v02')

    def test_legacy_hyphenated_state_and_throwing_storage_are_read_only(self):
        javascript = build_site.DEMOS_SCRIPT + r'''
const value = JSON.stringify({a:{category:'pulse',id:'v01',selected:true,notes:'完整\\n笔记'}});
const storage = {getItem:key => key === 'design-gallery-legacy' ? value : null};
const denied = {getItem:() => {throw new Error('denied')}, get length(){throw new Error('denied')}};
console.log(JSON.stringify({legacy:module.exports.readEntries({goal:'legacy'},storage), denied:module.exports.readEntries({goal:'aidash-cards-redesign'},denied)}));
'''
        result = json.loads(subprocess.check_output(['node', '-e', javascript], text=True))
        self.assertTrue(result['legacy'][0]['selected'])
        self.assertEqual(result['legacy'][0]['notes'], '完整\\n笔记')
        self.assertEqual(result['denied'], [])

    def test_reimported_markdown_titles_and_unsafe_palette_render_safely(self):
        manifest = json.loads((build_site.REPO_ROOT / 'vault/manifest.json').read_text())
        for collection in ('cards', 'patterns'):
            for item in manifest[collection]:
                if item['id'] in ('IP-006', 'IP-007', 'MP-007', 'TC-001', 'LN-001', 'MI-007'):
                    item['name'] = '**说法**：CRON <script>bad</script>'
        next(card for card in manifest['cards'] if card['id'] == 'VS-005')['semantic_palette'] = [{'hex':'red;\" onmouseover=\"alert(1)', 'role':'unsafe'}]
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'vault').mkdir()
            (root / 'vault/manifest.json').write_text(json.dumps(manifest))
            with patch.object(build_site, 'REPO_ROOT', root):
                build_site.build_vault_page()
            source = (root / 'vault/index.html').read_text()
            self.assertNotIn('<h3>**说法**', source)
            self.assertIn('<h3>零术语人话表达 (Plain-Language Microcopy)</h3>', source)
            self.assertNotIn('style="--swatch:red;', source)
            self.assertNotIn('id="vault-shots"', source)

    def test_reads_both_storage_formats_and_keeps_every_full_note(self):
        saved = {
            'aidash-cards-r2:selection:select-scheduled-pulse': 'v02',
            'aidash-cards-r2:star:skills-context-roi:v03': '1',
            'aidash-cards-r2:star:skills-context-roi:v04': '0',
            'aidash-cards-r2:note:skills-context-roi:v04': 'First line\n完整观察 <script> stays text',
            'aidash-cards-r2:note:scheduled-pulse:v01': '   ',
            'design-gallery:voxpocket-holistic-redesign': json.dumps({
                '["voice",2,"v01"]': {'category': 'voice', 'round': 2, 'id': 'v01', 'selected': True, 'notes': 'Round 2\n全文'},
                '["voice",3,"v01"]': {'category': 'voice', 'round': 3, 'id': 'v01', 'starred': True, 'notes': 'Round 3 notes'},
                'broken': None,
            }),
            'design-gallery:broken': '{invalid',
        }
        javascript = build_site.DEMOS_SCRIPT + '\n' + r'''
const values = SAVED;
const keys = Object.keys(values), storage = {length: keys.length, key: i => keys[i], getItem: key => values[key] || null};
const projects = [{goal:'aidash-cards-redesign',categories:['scheduled-pulse','skills-context-roi']}, {goal:'voxpocket-holistic-redesign',categories:['voice']}];
console.log(JSON.stringify({summaries: projects.map(p => module.exports.summarize(p,module.exports.readEntries(p, storage))), broken: module.exports.readEntries({goal:'broken'}, storage), denied: module.exports.readEntries(projects[0], null), unchanged: JSON.stringify(values) === JSON.stringify(SAVED)}));
'''.replace('SAVED', json.dumps(saved))
        result = json.loads(subprocess.check_output(['node', '-e', javascript], text=True))
        aidash, voice = result['summaries']
        self.assertEqual(aidash['counts'], {'notes': 1, 'starred': 1, 'selected': 1})
        self.assertIn('选择：v02', aidash['text'])
        self.assertIn('收藏：v03', aidash['text'])
        self.assertIn(saved['aidash-cards-r2:note:skills-context-roi:v04'], aidash['text'])
        self.assertEqual(voice['counts'], {'notes': 2, 'starred': 1, 'selected': 1})
        self.assertIn('r2/v01', voice['text'])
        self.assertIn('r3/v01', voice['text'])
        self.assertIn('Round 2\n全文', voice['text'])
        self.assertEqual(result['broken'], [])
        self.assertEqual(result['denied'], [])
        self.assertTrue(result['unchanged'])


if __name__ == '__main__':
    unittest.main()
