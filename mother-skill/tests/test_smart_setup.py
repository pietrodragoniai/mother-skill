"""Test di preflight Mac simulato. Windows CMD richiede un collaudo nativo."""
import os
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LAUNCHER = ROOT / 'AVVIA-MAC.command'


class SmartSetupTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.base = Path(self.tmp.name)
        self.home = self.base / 'home'
        self.home.mkdir()
        self.bindir = self.base / 'bin'
        self.bindir.mkdir()
        self.launchlog = self.base / 'launched.txt'
        self.env = os.environ.copy()
        self.env.update(HOME=str(self.home), MOCK_LOG=str(self.launchlog), PATH=f'{self.bindir}:' + os.environ.get('PATH', ''))
        self.skill = self.home / '.claude' / 'skills' / 'mother-skill' / 'SKILL.md'
        self.skill.parent.mkdir(parents=True)
        self.skill.write_text('test skill', encoding='utf-8')
        self.project = self.home / 'Documents' / 'Project Existing'
        self.project.mkdir(parents=True)
        (self.project / 'valuable.txt').write_text('DO NOT CHANGE', encoding='utf-8')
        (self.home / '.claude' / 'settings.json').write_text('{"default": "custom"}', encoding='utf-8')

    def fake_cli(self):
        cmd = self.bindir / 'claude'
        cmd.write_text('''#!/bin/bash
case "$1" in
  --version) if [[ "${MOCK_VERSION:-ok}" == bad ]]; then exit 1; fi; echo '2.1.299 (Claude Code)'; exit 0;;
  auth) if [[ "$2" == status ]]; then [[ "${MOCK_AUTH:-ok}" == ok ]]; exit $?; fi;;
esac
printf 'args:%s\\ncwd:%s\\n' "$*" "$PWD" > "$MOCK_LOG"
''', encoding='utf-8')
        cmd.chmod(0o755)

    def run_launcher(self, stdin='\n\n', **extra):
        env = dict(self.env, **extra)
        return subprocess.run(['bash', str(LAUNCHER)], input=stdin, text=True, capture_output=True, env=env, timeout=12)

    def test_ready_existing_project_preserves_configuration(self):
        self.fake_cli()
        out = self.run_launcher(f'{self.project}\nN\n', MOCK_AUTH='ok')
        self.assertEqual(out.returncode, 0, out.stderr + out.stdout)
        self.assertIn('Login gia configurato', out.stdout)
        self.assertIn('args:\n', self.launchlog.read_text())
        self.assertIn(f'cwd:{self.project}\n', self.launchlog.read_text())
        self.assertEqual((self.project / 'valuable.txt').read_text(), 'DO NOT CHANGE')
        self.assertEqual((self.home / '.claude' / 'settings.json').read_text(), '{"default": "custom"}')

    def test_ready_opt_in_opus_only_for_session(self):
        self.fake_cli()
        out = self.run_launcher(f'{self.project}\ns\n')
        self.assertEqual(out.returncode, 0, out.stderr + out.stdout)
        self.assertIn('args:--model claude-opus-5-5 --effort high', self.launchlog.read_text())

    def test_unconfirmed_auth_does_not_trigger_reinstall(self):
        self.fake_cli()
        out = self.run_launcher(f'{self.project}\n', MOCK_AUTH='missing')
        self.assertEqual(out.returncode, 0, out.stderr + out.stdout)
        self.assertIn('login non confermato', out.stdout)
        self.assertIn('args:\n', self.launchlog.read_text())
        self.assertNotIn('--model', self.launchlog.read_text())

    def test_broken_cli_diagnoses_instead_of_launching(self):
        self.fake_cli()
        out = self.run_launcher('\n', MOCK_VERSION='bad')
        self.assertEqual(out.returncode, 1)
        self.assertIn('claude doctor', out.stdout)
        self.assertFalse(self.launchlog.exists())

    def test_missing_skill_does_not_launch(self):
        self.fake_cli()
        self.skill.unlink()
        out = self.run_launcher('\n')
        self.assertEqual(out.returncode, 1)
        self.assertIn('INSTALLA-MAC.command', out.stdout)
        self.assertFalse(self.launchlog.exists())

    def test_missing_cli_without_login_or_install(self):
        out = self.run_launcher('\n')
        self.assertEqual(out.returncode, 1)
        self.assertIn('Desktop', out.stdout)
        self.assertFalse(self.launchlog.exists())

    def test_rejects_home_as_project(self):
        self.fake_cli()
        out = self.run_launcher(f'{self.home}\n')
        self.assertEqual(out.returncode, 1)
        self.assertIn('SOTTOCARTELLA', out.stdout)
        self.assertFalse(self.launchlog.exists())


if __name__ == '__main__':
    unittest.main()
