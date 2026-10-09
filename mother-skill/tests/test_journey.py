import tempfile
import unittest
from pathlib import Path
from scripts.init_workspace import create_workspace
from scripts.journey import load, set_phase, set_gate, set_release, save

class JourneyTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name) / 'mia-app'
        self.root.mkdir()
        create_workspace(self.root)
        self.s = load(self.root)
    def tearDown(self): self.tmp.cleanup()
    def test_initial_phase(self): self.assertEqual(self.s['phase'], 'DISCOVER')
    def test_preserves_existing_files(self):
        p = self.root / '.claude/mother-skill/PLAN.md'
        p.write_text('MIO LAVORO', encoding='utf-8')
        create_workspace(self.root)
        self.assertEqual(p.read_text(encoding='utf-8'), 'MIO LAVORO')
    def test_no_jump(self):
        with self.assertRaises(ValueError): set_phase(self.s, 'BUILD')
    def test_plan_gate_before_setup(self):
        for phase in ('CHALLENGE', 'BLUEPRINT'): set_phase(self.s, phase)
        with self.assertRaises(ValueError): set_phase(self.s, 'SETUP')
        set_gate(self.s, 'plan', 'OK esplicito nel dialogo')
        set_phase(self.s, 'SETUP')
        set_phase(self.s, 'BUILD')
        self.assertEqual(self.s['phase'], 'BUILD')
    def test_release_gates_and_evidence(self):
        self.s['phase'] = 'VERIFY_SHIP'
        with self.assertRaises(ValueError): set_release(self.s, 'CI_GREEN', '')
        set_release(self.s, 'PR_OPEN', 'https://github.com/org/repo/pull/1')
        set_release(self.s, 'CI_GREEN', 'CI run 123 success')
        with self.assertRaises(ValueError): set_release(self.s, 'CI_APPROVED', 'user said yes')
        set_gate(self.s, 'ci', 'utente: approvo la CI')
        set_release(self.s, 'CI_APPROVED', 'CI run 123 user acknowledged')
        set_release(self.s, 'STAGING', 'https://preview.example.test')
        with self.assertRaises(ValueError): set_release(self.s, 'STAGING_APPROVED', 'ok')
        set_gate(self.s, 'staging', 'utente ha testato e approvato')
        set_release(self.s, 'STAGING_APPROVED', 'feedback approvato')
        with self.assertRaises(ValueError): set_release(self.s, 'PRODUCTION', 'https://example.test')
        set_gate(self.s, 'production', 'utente: pubblica in produzione')
        set_release(self.s, 'PRODUCTION', 'https://example.test build 123')
        save(self.root, self.s)
        self.assertEqual(load(self.root)['release']['status'], 'PRODUCTION')
    def test_fails_on_home(self):
        with self.assertRaises(ValueError): create_workspace(Path.home())
    def test_does_not_overwrite_existing_claude_md(self):
        p = self.root / 'CLAUDE.md'
        p.write_text('ESISTENTE', encoding='utf-8')
        create_workspace(self.root, with_claude_md=True)
        self.assertEqual(p.read_text(encoding='utf-8'), 'ESISTENTE')

if __name__ == '__main__': unittest.main()
