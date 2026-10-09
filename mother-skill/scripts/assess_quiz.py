#!/usr/bin/env python3
"""Deterministic, privacy-first adaptive onboarding assessment for Mother Skill.

Only Python standard library. Read-only unless --save is passed.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import sys

BANK = Path(__file__).resolve().parent.parent / 'data' / 'quiz_bank.json'
DEFAULT_PROFILE = Path.home() / '.claude' / 'mother-skill' / 'LEARNING_PROFILE.json'


def get_bank() -> dict:
    bank = json.loads(BANK.read_text(encoding='utf-8'))
    qs = bank['questions']
    ids = [q['id'] for q in qs]
    if len(ids) != len(set(ids)):
        raise ValueError('duplicate quiz ids')
    for q in qs:
        if sorted(q['options']) != list('ABCD') or q['answer'] not in q['options']:
            raise ValueError(f"invalid question {q['id']}")
    return bank


def selected_questions(bank: dict, focus: str) -> list[dict]:
    by_id = {q['id']: q for q in bank['questions']}
    return [by_id[qid] for qid in bank['core'] + bank['tracks'][focus]]


def assess(questions: list[dict], answers: list[str], focus: str, version: int) -> dict:
    if len(answers) != len(questions):
        raise ValueError(f'expected exactly {len(questions)} answers, got {len(answers)}')
    answers = [a.strip().upper() for a in answers]
    if any(a not in 'ABCDE' or len(a) != 1 for a in answers):
        raise ValueError('answers must be A, B, C, D, or E (Non so)')
    correct = [q['domain'] for q, a in zip(questions, answers) if a == q['answer']]
    explain = [q['domain'] for q, a in zip(questions, answers) if a != q['answer']]
    score = len(correct)
    level = 'Starter' if score <= 2 else 'Explorer' if score <= 5 else 'Builder' if score <= 7 else 'Fluent'
    return {
        'schema_version': 1,
        'assessment_version': version,
        'assessed_at': datetime.now(timezone.utc).isoformat(timespec='seconds'),
        'track': focus,
        'level': level,
        'score': score,
        'max_score': len(questions),
        'domains_demonstrated': sorted(set(correct)),
        'domains_to_explain': sorted(set(explain)),
        'preferences': {'explanations': 'adaptive', 'language': 'it'},
    }


def interactive(questions: list[dict]) -> list[str]:
    answers = []
    print('\nSkill Check — non è un esame. Rispondi A/B/C/D oppure E = Non so.\n')
    for i, q in enumerate(questions, 1):
        print(f"{i}/{len(questions)}  {q['question']}")
        for option, label in q['options'].items():
            print(f'  {option}. {label}')
        print('  E. Non so')
        while True:
            try:
                response = input('Risposta [A-E]: ').strip().upper()
            except (EOFError, KeyboardInterrupt):
                raise ValueError('quiz interrotto; nessun profilo salvato') from None
            if response in ('A', 'B', 'C', 'D', 'E'):
                answers.append(response)
                print()
                break
            print('Inserisci A, B, C, D o E.')
    return answers


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--focus', choices=['general', 'web', 'data', 'motion'], default='general')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--answers', help='Comma-separated 8 answers (A-E)')
    group.add_argument('--interactive', action='store_true', help='Interactive standalone terminal quiz')
    parser.add_argument('--save', action='store_true', help='Save privacy-minimal profile outside repository')
    parser.add_argument('--profile-path', type=Path, default=DEFAULT_PROFILE, help='Override personal profile path')
    parser.add_argument('--format', choices=['text', 'json'], default='text')
    args = parser.parse_args()
    try:
        bank = get_bank()
        questions = selected_questions(bank, args.focus)
        answers = interactive(questions) if args.interactive else args.answers.split(',')
        profile = assess(questions, answers, args.focus, bank['version'])
        if args.save:
            dst = args.profile_path.expanduser().resolve()
            dst.parent.mkdir(parents=True, exist_ok=True)
            # Never overwrite unrelated non-JSON content; protect the private learning profile.
            if dst.exists():
                previous = json.loads(dst.read_text(encoding='utf-8'))
                if previous.get('schema_version') != 1:
                    raise ValueError('existing profile has an incompatible schema; refusing overwrite')
            dst.write_text(json.dumps(profile, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
            try:
                dst.chmod(0o600)
            except OSError:
                pass
    except (ValueError, KeyError, OSError, json.JSONDecodeError) as exc:
        print(f'ERROR: {exc}', file=sys.stderr)
        return 2
    if args.format == 'json':
        print(json.dumps(profile, ensure_ascii=False, indent=2))
    else:
        print(f"Livello indicativo: {profile['level']} ({profile['score']}/{profile['max_score']})")
        print('Già dimostrati: ' + (', '.join(profile['domains_demonstrated']) or 'nessuno nel quiz'))
        print('Da spiegare in contesto: ' + (', '.join(profile['domains_to_explain']) or 'nessuno nel quiz'))
        if args.save:
            print('Profilo personale salvato in: ' + str(dst))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
