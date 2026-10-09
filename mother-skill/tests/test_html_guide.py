from pathlib import Path
from html.parser import HTMLParser
import unittest

ROOT=Path(__file__).resolve().parents[2]
GUIDE=ROOT/'01-APRI-QUI.html'

class CheckHTML(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids=set()
        self.js_external=[]
        self.os=set()
        self.states=set()
        self.copies=[]
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        if 'id' in a: self.ids.add(a['id'])
        if tag=='script' and 'src' in a: self.js_external.append(a['src'])
        if 'data-os' in a: self.os.add(a['data-os'])
        if 'data-state' in a: self.states.add(a['data-state'])
        if 'data-copy' in a: self.copies.append(a['data-copy'])

class GuideTests(unittest.TestCase):
    def test_openable_offline_html(self):
        html=GUIDE.read_text(encoding='utf-8')
        parser=CheckHTML();parser.feed(html);parser.close()
        self.assertIn('<!DOCTYPE html>',html)
        self.assertEqual(parser.js_external,[])
        self.assertIn('steps',parser.ids)
        self.assertEqual(parser.os,{'mac','win'})
        self.assertEqual(parser.states,{'ready','login','desktop','new','unknown'})
        self.assertIn('/mother-skill Ho un\'idea',parser.copies)
    def test_scripts_referenced_exist(self):
        html=GUIDE.read_text(encoding='utf-8')
        for name in ['INSTALLA-MAC.command','INSTALLA-WINDOWS.cmd','AVVIA-MAC.command','AVVIA-WINDOWS.cmd']:
            self.assertIn(name,html)
            self.assertTrue((ROOT/name).is_file())
    def test_readme_points_to_browser_guide(self):
        readme=(ROOT/'README.md').read_text(encoding='utf-8')
        self.assertIn('01-APRI-QUI.html', readme)
        self.assertIn('doppio clic', readme)
if __name__=='__main__': unittest.main()
