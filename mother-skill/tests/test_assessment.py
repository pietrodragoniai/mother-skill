"""Run: python3 -m unittest discover -s tests -v (from skill directory)."""
from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'scripts' / 'assess_quiz.py'
spec = importlib.util.spec_from_file_location('assess_quiz', SCRIPT)
quiz = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(quiz)


class AssessmentTests(unittest.TestCase):
    def test_bank_invariants(self):
        bank = quiz.get_bank()
        self.assertEqual(len(bank['core']), 6)
        self.assertEqual(set(bank['tracks']), {'web', 'data', 'motion', 'general'})
        for focus in bank['tracks']:
            questions = quiz.selected_questions(bank, focus)
            self.assertEqual(len(questions), 8)
            self.assertEqual(len({q['id'] for q in questions}), 8)

    def test_scoring_extremes_and_domains(self):
        bank = quiz.get_bank()
        qs = quiz.selected_questions(bank, 'web')
        perfect = quiz.assess(qs, [q['answer'] for q in qs], 'web', bank['version'])
        self.assertEqual((perfect['score'], perfect['level'], perfect['max_score']), (8, 'Fluent', 8))
        self.assertEqual(perfect['domains_to_explain'], [])
        unknown = quiz.assess(qs, ['E'] * 8, 'web', bank['version'])
        self.assertEqual((unknown['score'], unknown['level']), (0, 'Starter'))
        self.assertEqual(len(unknown['domains_to_explain']), 8)

    def test_mid_scores(self):
        qs = quiz.selected_questions(quiz.get_bank(), 'general')
        for n, expected in [(2, 'Starter'), (3, 'Explorer'), (5, 'Explorer'), (6, 'Builder'), (7, 'Builder')]:
            answers = [q['answer'] if i < n else 'E' for i, q in enumerate(qs)]
            self.assertEqual(quiz.assess(qs, answers, 'general', 1)['level'], expected)

    def test_invalid_answers(self):
        qs = quiz.selected_questions(quiz.get_bank(), 'general')
        for answers in (['E'] * 7, ['E'] * 9, ['E'] * 7 + ['F'], ['E'] * 7 + ['AB']):
            with self.assertRaises(ValueError):
                quiz.assess(qs, answers, 'general', 1)

    def test_cli_writes_only_when_requested(self):
        with tempfile.TemporaryDirectory() as folder:
            target = Path(folder) / 'profile.json'
            args = [sys.executable, str(SCRIPT), '--focus', 'motion', '--answers', 'E,E,E,E,E,E,E,E', '--profile-path', str(target), '--format', 'json']
            result = subprocess.run(args, check=True, capture_output=True, text=True)
            self.assertEqual(json.loads(result.stdout)['score'], 0)
            self.assertFalse(target.exists())
            result = subprocess.run(args + ['--save'], check=True, capture_output=True, text=True)
            saved = json.loads(target.read_text(encoding='utf-8'))
            self.assertEqual(saved['level'], 'Starter')
            self.assertEqual(saved['track'], 'motion')
            self.assertNotIn('answers', saved)
            self.assertIn('domains_to_explain', saved)
            self.assertNotIn('name', saved)
            self.assertNotIn('email', saved)

    def test_cli_rejects_overwrite_of_unknown_schema(self):
        with tempfile.TemporaryDirectory() as folder:
            target = Path(folder) / 'profile.json'
            target.write_text('{"schema_version":99}', encoding='utf-8')
            before = target.read_bytes()
            p = subprocess.run([sys.executable, str(SCRIPT), '--answers', 'E,E,E,E,E,E,E,E', '--profile-path', str(target), '--save'], capture_output=True, text=True)
            self.assertEqual(p.returncode, 2)
            self.assertEqual(target.read_bytes(), before)


if __name__ == '__main__':
    unittest.main()
