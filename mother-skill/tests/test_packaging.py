import json
import unittest
from pathlib import Path
BASE = Path(__file__).resolve().parents[1]
class PackagingTests(unittest.TestCase):
    def test_skill_frontmatter(self):
        text = (BASE / 'SKILL.md').read_text(encoding='utf-8')
        self.assertTrue(text.startswith('---\n'))
        self.assertIn('model: claude-opus-5-5', text)
        self.assertIn('effort: high', text)
        self.assertIn('disable-model-invocation: true', text)
    def test_all_references_exist(self):
        import re
        skill = (BASE / 'SKILL.md').read_text(encoding='utf-8')
        for name in re.findall(r'`(references/[^`]+\.md)`', skill):
            self.assertTrue((BASE / name).is_file(), name)
    def test_quiz_bank_valid(self):
        obj = json.loads((BASE / 'data/quiz_bank.json').read_text(encoding='utf-8'))
        self.assertTrue(obj)
    def test_starter_scripts_exist(self):
        for name in ('01-APRI-QUI.html', 'START-QUI.md', 'INSTALLA-MAC.command', 'AVVIA-MAC.command', 'INSTALLA-WINDOWS.cmd', 'AVVIA-WINDOWS.cmd'):
            self.assertTrue((BASE.parent / name).is_file())
if __name__ == '__main__': unittest.main()
