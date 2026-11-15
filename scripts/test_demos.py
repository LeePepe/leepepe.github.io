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
