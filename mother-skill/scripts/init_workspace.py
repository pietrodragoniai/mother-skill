#!/usr/bin/env python3
"""Create the minimal Opus project memory without overwriting existing work."""
from __future__ import annotations
import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FILES = ["PLAN.md", "HANDOFF.md", "DECISIONS.md"]

def create_workspace(root: Path, project_name: str | None = None, with_claude_md: bool = False) -> list[Path]:
    root = root.expanduser().resolve()
    if not root.is_dir():
        raise ValueError("La cartella progetto deve esistere (non la creo silenziosamente).")
    if root == Path.home().resolve() or root == Path(root.anchor):
        raise ValueError("Scegli una cartella progetto dedicata, non home o radice del disco.")
    target = root / '.claude' / 'mother-skill'
    target.mkdir(parents=True, exist_ok=True)
    created = []
    for name in FILES:
        p = target / name
        if p.exists():
            continue
        txt = (ROOT / 'templates' / name).read_text(encoding='utf-8').replace('{{PROJECT}}', project_name or root.name)
        with p.open('x', encoding='utf-8') as fh:
            fh.write(txt)
        created.append(p)
    p = target / 'STATE.json'
    if not p.exists():
        initial = {
            'schema_version': 1,
            'project': project_name or root.name,
            'journey': 'idea-to-product',
            'phase': 'DISCOVER',
            'autonomy': 'guided',
            'grill': 'medium',
            'current_task': None,
            'correction_attempts': 0,
            'gates': {'plan': None, 'ci': None, 'staging': None, 'production': None},
            'release': {'status': 'NOT_STARTED', 'evidence': None},
            'updated_at': datetime.now(timezone.utc).isoformat()
        }
        with p.open('x', encoding='utf-8') as fh:
            json.dump(initial, fh, indent=2, ensure_ascii=False)
            fh.write('\n')
        created.append(p)
    if with_claude_md:
        p = root / 'CLAUDE.md'
        if not p.exists():
            with p.open('x', encoding='utf-8') as fh:
                fh.write((ROOT / 'templates' / 'CLAUDE.sample.md').read_text(encoding='utf-8'))
            created.append(p)
    return created

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, required=True)
    parser.add_argument('--name')
    parser.add_argument('--with-claude-md', action='store_true')
    args = parser.parse_args()
    created = create_workspace(args.root, args.name, args.with_claude_md)
    print(f'Creati {len(created)} file senza sovrascrivere gli esistenti:')
    for path in created:
        print(f' - {path}')
