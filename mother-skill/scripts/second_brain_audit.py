#!/usr/bin/env python3
"""Audita la dimensione dei documenti second-brain: NON modifica file."""
import argparse
from pathlib import Path

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('root', nargs='?', default='.')
    a=p.parse_args(); root=Path(a.root).resolve()
    candidates=[root/'CLAUDE.md',root/'CHANGELOG.md',root/'docs/wiki/INDEX.md']
    candidates += list((root/'.claude/mother-skill').glob('*.md'))
    candidates += list((root/'docs/wiki').rglob('*.md')) if (root/'docs/wiki').exists() else []
    seen=set()
    for f in candidates:
        if f in seen or not f.is_file(): continue
        seen.add(f)
        content=f.read_text(errors='replace'); lines=content.count('\n')+1
        label=' REVIEW_LENGTH' if lines>250 else ''
        print(f'{f.relative_to(root)}: {lines} lines; {len(content.encode())} bytes{label}')
    print('Audit only: nothing modified, no token count inferred.')
if __name__=='__main__': main()
