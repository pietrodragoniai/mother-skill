#!/usr/bin/env python3
"""Project progress tracker. NEVER a security or permission enforcement boundary."""
from __future__ import annotations
import argparse
import json
import os
import tempfile
from datetime import datetime, timezone
from pathlib import Path

PHASES = ('DISCOVER','CHALLENGE','BLUEPRINT','SETUP','PREVIEW','BUILD','VERIFY_SHIP','EVOLVE')
RELEASES = ('NOT_STARTED','PR_OPEN','CI_GREEN','CI_APPROVED','STAGING','STAGING_APPROVED','PRODUCTION')
GATES = ('plan','ci','staging','production')

def file_for(root):
    return Path(root).expanduser().resolve()/'.claude'/'mother-skill'/'STATE.json'

def load(root):
    p=file_for(root)
    with p.open(encoding='utf-8') as f:
        state=json.load(f)
    if state.get('schema_version')!=1 or state.get('phase') not in PHASES or state.get('release',{}).get('status') not in RELEASES:
        raise ValueError('STATE.json non valido o schema non supportato')
    return state

def save(root,state):
    p=file_for(root)
    state['updated_at']=datetime.now(timezone.utc).isoformat()
    temp=None
    try:
        with tempfile.NamedTemporaryFile('w',encoding='utf-8',dir=p.parent,prefix='.state-',suffix='.tmp',delete=False) as f:
            temp=f.name
            json.dump(state,f,indent=2,ensure_ascii=False)
            f.write('\n')
            f.flush()
            os.fsync(f.fileno())
        os.replace(temp,p)
    finally:
        if temp and Path(temp).exists(): Path(temp).unlink()

def set_phase(state,to):
    if to not in PHASES:
        raise ValueError('Fase sconosciuta')
    cur=state['phase']
    i=PHASES.index(cur)
    nxt=PHASES[i+1:i+2]
    allowed = set(nxt)
    if cur=='SETUP': allowed.add('BUILD')  # no visual preview needed
    if to not in allowed:
        raise ValueError(f'Transizione non ammessa: {cur} → {to}')
    if cur=='BLUEPRINT' and to=='SETUP' and not state['gates'].get('plan'):
        raise ValueError('Manca un OK umano al piano (registrare solo dopo conferma reale)')
    state['phase']=to
    return state

def set_gate(state,gate,reason):
    if gate not in GATES: raise ValueError('Gate sconosciuto')
    if not reason or not reason.strip(): raise ValueError('Serve riferimento testuale a un OK espresso dall’utente')
    state['gates'][gate]={'recorded_at':datetime.now(timezone.utc).isoformat(),'evidence':reason.strip()}
    return state

def set_release(state,to,evidence):
    if to not in RELEASES: raise ValueError('Stato release sconosciuto')
    previous=state['release']['status']
    if state['phase'] != 'VERIFY_SHIP':
        raise ValueError('La release si traccia nella fase VERIFY_SHIP')
    if RELEASES.index(to) != RELEASES.index(previous)+1:
        raise ValueError(f'Non saltare step di release: {previous} → {to}')
    if not evidence or not evidence.strip():
        raise ValueError('Servono evidenze concrete (URL PR, SHA, CI, staging/live)')
    needed={'CI_APPROVED':'ci','STAGING_APPROVED':'staging','PRODUCTION':'production'}
    if to in needed and not state['gates'].get(needed[to]):
        raise ValueError(f'Manca conferma utente: {needed[to]}')
    state['release']={'status':to,'evidence':evidence.strip()}
    return state

def main():
    pa=argparse.ArgumentParser(description=__doc__)
    pa.add_argument('--root',required=True,type=Path)
    sub=pa.add_subparsers(dest='command',required=True)
    sub.add_parser('status')
    ph=sub.add_parser('phase');ph.add_argument('--to',required=True)
    ga=sub.add_parser('gate');ga.add_argument('--name',required=True);ga.add_argument('--evidence',required=True)
    rel=sub.add_parser('release');rel.add_argument('--to',required=True);rel.add_argument('--evidence',required=True)
    ar=pa.parse_args()
    state=load(ar.root)
    if ar.command=='phase': set_phase(state,ar.to)
    elif ar.command=='gate': set_gate(state,ar.name,ar.evidence)
    elif ar.command=='release': set_release(state,ar.to,ar.evidence)
    if ar.command!='status': save(ar.root,state)
    print(json.dumps(state,indent=2,ensure_ascii=False))

if __name__=='__main__':main()
