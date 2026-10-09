#!/usr/bin/env python3
"""Optional *display-only* Claude Code statusLine: never modifies settings."""
from __future__ import annotations
import json
import sys


def render(data):
    item = data.get('context_window') or {}
    pct = item.get('used_percentage')
    if not isinstance(pct, (int, float)) or isinstance(pct, bool) or pct < 0:
        return 'Mother Skill · Contesto non disponibile'
    if pct >= 70:
        return f'Mother Skill · CONTEXT {pct:g}% >= 70% · HANDOFF + NEW SESSION'
    if pct >= 60:
        return f'Mother Skill · CONTEXT {pct:g}% · Prepara handoff'
    return f'Mother Skill · CONTEXT {pct:g}% · OK'


if __name__ == '__main__':
    try:
        print(render(json.load(sys.stdin)))
    except (ValueError, TypeError, OSError):
        print('Mother Skill · Contesto non disponibile')
