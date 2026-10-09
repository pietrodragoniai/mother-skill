"""Structural and safety checks for the public Mother Skill beta."""
from pathlib import Path
import json
import os
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]
SKILL = ROOT / 'mother-skill'


class MotherReleaseTests(unittest.TestCase):
    def test_public_name_and_command(self):
        skill = (SKILL / 'SKILL.md').read_text(encoding='utf-8')
        self.assertTrue(skill.startswith('---\nname: mother-skill\n'))
        self.assertIn('effort: high', skill)
        self.assertIn('disable-model-invocation: true', skill)
        for name in ('README.md', '01-APRI-QUI.html', 'START-QUI.md', 'GITHUB-PUBLISH.md'):
            self.assertIn('/mother-skill', (ROOT / name).read_text(encoding='utf-8'))

    def test_marketplace_and_plugin_metadata_match(self):
        marketplace = json.loads((ROOT / '.claude-plugin/marketplace.json').read_text(encoding='utf-8'))
        plugin = json.loads((SKILL / '.claude-plugin/plugin.json').read_text(encoding='utf-8'))
        self.assertEqual(plugin['name'], 'mother-skill')
        self.assertEqual(plugin['version'], '1.0.0')
        self.assertEqual(marketplace['plugins'][0]['name'], plugin['name'])
        self.assertEqual(marketplace['plugins'][0]['source'], './mother-skill')
        self.assertTrue((SKILL / 'SKILL.md').is_file())

    def test_manifesto_qualifies_benchmark(self):
        body = (ROOT / 'PERCHE-MOTHER-SKILL.md').read_text(encoding='utf-8')
        self.assertIn('75%', body)
        self.assertIn('non una cifra dimostrata', body)
        self.assertIn('60%', body)
        self.assertIn('70%', body)

    def test_html_offline_browser_first(self):
        html = (ROOT / '01-APRI-QUI.html').read_text(encoding='utf-8')
        self.assertIn('<!DOCTYPE html>', html)
        self.assertIn('Mother Skill', html)
        self.assertIn('INSTALLA-MAC.command', html)
        self.assertIn('INSTALLA-WINDOWS.cmd', html)
        self.assertNotIn('<script src=', html)

    def test_installer_preserves_legacy(self):
        with tempfile.TemporaryDirectory() as tmp:
            home = Path(tmp)
            legacy = home / '.claude' / 'skills' / 'opus-inline-studio'
            legacy.mkdir(parents=True)
            (legacy / 'SKILL.md').write_text('keep me', encoding='utf-8')
            env = dict(os.environ, HOME=str(home))
            run = subprocess.run(['bash', str(ROOT / 'INSTALLA-MAC.command')], input='\n', text=True,
                                 capture_output=True, env=env, timeout=20)
            self.assertEqual(run.returncode, 0, run.stdout + run.stderr)
            self.assertEqual((legacy / 'SKILL.md').read_text(encoding='utf-8'), 'keep me')
            self.assertTrue((home / '.claude/skills/mother-skill/SKILL.md').exists())

    def test_installer_backup_on_upgrade(self):
        with tempfile.TemporaryDirectory() as tmp:
            home = Path(tmp)
            previous = home / '.claude/skills/mother-skill'
            previous.mkdir(parents=True)
            (previous / 'SKILL.md').write_text('previous-mother', encoding='utf-8')
            env = dict(os.environ, HOME=str(home))
            run = subprocess.run(['bash', str(ROOT / 'INSTALLA-MAC.command')], input='\n', text=True,
                                 capture_output=True, env=env, timeout=20)
            self.assertEqual(run.returncode, 0, run.stdout + run.stderr)
            backups = sorted(previous.parent.glob('mother-skill-backup-*/SKILL.md'))
            self.assertEqual(len(backups), 1)
            self.assertEqual(backups[0].read_text(encoding='utf-8'), 'previous-mother')
            self.assertIn('name: mother-skill', (previous / 'SKILL.md').read_text(encoding='utf-8'))


if __name__ == '__main__':
    unittest.main()
