# Journey Engine: dall'idea al prodotto

Stati: DISCOVER → CHALLENGE → BLUEPRINT → SETUP → PREVIEW → BUILD → VERIFY_SHIP → EVOLVE. PREVIEW è opzionale quando non esiste una scelta visiva/progettuale necessaria. Stati persistiti nel progetto, non confondere con permessi della piattaforma.

| Fase | Output essenziale | Gate |
|---|---|---|
| DISCOVER | Idea Brief: problema, utente, risultato, assunzioni | nessuno |
| CHALLENGE | Grill Me; brainstorming; rischi e cosa NON costruire | decisioni funzionali rilevanti |
| BLUEPRINT | MVP, criteri, stack, costi, TASK-001… | OK al piano |
| SETUP | workspace, Git secondo scelta, strumenti minimi, Second Brain | approvazione installazioni/servizi |
| PREVIEW | A/B/C reali quando appropriate | scelta UI/architettura importante |
| BUILD | incrementi eseguibili e screenshot non bloccanti | checkpoint a fine task |
| VERIFY_SHIP | test, PR, CI, staging, produzione | OK CI, staging, produzione distinti |
| EVOLVE | smoke test, versione, changelog, wiki e prossimo task | chiusura |

Consenti ritorni motivati alla fase precedente senza cancellare l'evidenza. Aggiorna `STATE.json` solo dopo un passaggio realmente accaduto. Se task con rischio basso e richiesta chiara, abbrevia DISCOVER/CHALLENGE senza saltare le approvazioni di sicurezza. Un progetto non deve entrare in produzione per poter chiudere la sua prima sessione.

- `guided`: spiega a ogni snodo fondamentale, niente passaggi nascosti.
- `balanced` (default se non principiante): autonomie locali, riepilogo a fine task.
- `autopilot`: svolgi attività locali autorizzate, ma mai autorizzazioni implicite per remoto, spese, dati o produzione.

Usa `scripts/journey.py status --root <workspace>` per leggere uno stato già inizializzato, `phase` per un avanzamento registrato. Lo script **non** esegue CI o deploy, né testimonia consenso umano autonomamente. Lo status non può essere usato per fingere un gate superato.
