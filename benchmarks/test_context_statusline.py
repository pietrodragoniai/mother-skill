import importlib.util
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location('context_statusline', Path(__file__).resolve().parents[1] / 'mother-skill/scripts/context_statusline.py')
monitor = importlib.util.module_from_spec(spec)
spec.loader.exec_module(monitor)

class ContextBudgetTests(unittest.TestCase):
    def test_normal(self):
        self.assertIn('OK', monitor.render({'context_window':{'used_percentage': 59}}))
    def test_preparation(self):
        self.assertIn('Prepara handoff', monitor.render({'context_window':{'used_percentage': 60}}))
    def test_near_threshold_display(self):
        self.assertIn('69.9% · Prepara', monitor.render({'context_window':{'used_percentage':69.9}}))
    def test_handoff(self):
        self.assertIn('NEW SESSION', monitor.render({'context_window':{'used_percentage': 70}}))
    def test_missing(self):
        self.assertIn('non disponibile', monitor.render({'context_window':{'used_percentage':None}}))
    def test_no_confusion_with_rate_limit(self):
        self.assertIn('non disponibile', monitor.render({'rate_limits':{'five_hour':{'used_percentage':99}}}))

if __name__ == '__main__':
    unittest.main()
