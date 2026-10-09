# Context Budget Protocol — limite operativo 70%

**Obiettivo:** non lasciare che il contesto saturo causi riletture ridondanti o perdita di coerenza. Preferisci *nuova conversazione con handoff* anziché delegare un compito a nuovi agenti solo per ottenere memoria fresca.

## Misurazione effettiva (mai inventare numeri)

1. Claude Code espone `/context` all'utente. Se è visibile la percentuale, utilizzala; altrimenti **non affermare di conoscerla**.
2. Se l'utente attiva volontariamente la status line, può usare `scripts/context_statusline.py`, che legge `context_window.used_percentage` dall'input JSON fornito da Claude Code e stampa un avviso a 60% e 70%. Non modifica settings, non ferma la sessione e non notifica automaticamente il modello: l'utente può riferire l'avviso.
3. Se la percentuale manca, passa a handoff quando la conversazione diventa lunga/ripetitiva, termina una milestone o l'utente chiede di ripartire. Non usare una stima spacciandola per telemetria.


## Visualizzazione opzionale (solo con consenso)

Questa è un'opzione avanzata: **non necessaria per cominciare**. Puoi chiedere a Claude Code di configurare la status line tramite `/statusline`, oppure, dopo aver verificato che Python 3 è disponibile, aggiungere manualmente `statusLine` nelle tue impostazioni esistenti. **Non sostituire l'intero `settings.json`**, perché potresti perdere la configurazione personale.

Esempio per Mac/Linux, sostituendo il percorso con quello reale dove hai installato la skill:

```json
{
  "statusLine": {
    "type": "command",
    "command": "python3 /PERCORSO/mother-skill/scripts/context_statusline.py"
  }
}
```

Su Windows la stringa `command` deve usare un eseguibile Python funzionante (es. `py -3`) e un percorso valido per Windows, quotato se contiene spazi. Prima verifica di non avere già una status line personalizzata: l'esempio la **sostituisce** e non va applicato automaticamente.

La status line legge dati di uso contesto **dell'ultima risposta API**, può essere momentaneamente non disponibile e non obbliga Claude a fermarsi. Mostra avvisi solo all'utente; riferisci l'avviso a Claude o avvia volontariamente l'handoff, perché il modello non ha necessariamente accesso al dato mostrato. La preferenza del 70% non è una garanzia tecnica che ogni singola chiamata rimanga sotto soglia.

## Soglie

- **0–59%:** lavoro normale, letture solo su richiesta del task, review puntuali.
- **60–69%:** prepara l'handoff mentre termini l'unità minima sicura: verifica test, salva decisioni, stato e lavori non committati senza cancellarli. Non interrompere modifiche a metà che potrebbero rompere il progetto.
- **>=70% (osservato):** non avviare nuovo task lungo, consolidare handoff entro breve, proporre `/clear` o nuova sessione nello stesso workspace. **Non fare `git commit` o `git push` automaticamente** per liberare contesto. Se ci sono operazioni critiche già in corso, finisci o metti in sicurezza prima del cambio.
- **Sessione nuova:** carica soltanto `CLAUDE.md` essenziale, `STATE.json`, `HANDOFF.md`, `git status --short`/branch, e i file pertinenti. Controlla sempre se i test dichiarati nel handoff corrispondono agli strumenti/progetto correnti. Per approfondire usa percorsi specifici dalla wiki, *non la wiki intera*.

## Handoff compatto obbligatorio

Max ~400–700 parole, preferibilmente meno, con: scopo e task ID, fase, ultimo esito verificato, cosa resta, percorsi dei file, branch e SHA **se esistono**, modifiche non committate, test passati/falliti con comandi, decisioni e vincoli, problema bloccante e unica prossima azione. In `STATE.json` tenere lo stato strutturato evitando duplicazioni in dieci MD. Non copiare log completi, output enormi o screenshot serializzati.

## Quale strumento scegliere

- `/context`: visualizza uso del contesto (comando dell'utente).
- `/clear`: nuova conversazione nel workspace corrente, dopo aver verificato l'handoff.
- `/compact`: abbrevia la conversazione corrente; **non equivale a nuova sessione** e non risponde al requisito di ripartenza pulita quando il 70% è stato raggiunto.
- `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=70`: quando supportato, anticipa la **compattazione**, non il cambio conversazione, quindi NON implementa questa regola. Non modificare variabili/setting globali per conto dell'utente.

## Non delegare per recuperare contesto

Nessun agente secondario deve ricostruire la storia leggendo tutto il repository. Il nuovo turno Opus inline riparte dal handoff selettivo e dalla verifica Git. Usa browser, test runner e compilatori come strumenti, non come agenti di implementazione delegati.

## Verifica finale distinta da verifiche di task

Ogni task: lint/test mirati e controlli sui cambiamenti. Solo quando i task sono integrati: **una review finale trasversale** (architettura, sicurezza, regressioni, flussi utente, costi) prima di PR finale o release, in base alla pipeline. Correggere ciò che la review trova e testare di nuovo; ripetere review totale solo se un cambiamento sostanziale invalida la precedente.

Riferimenti ufficiali:
- https://code.claude.com/docs/en/commands
- https://code.claude.com/docs/en/statusline
- https://code.claude.com/docs/en/env-vars
