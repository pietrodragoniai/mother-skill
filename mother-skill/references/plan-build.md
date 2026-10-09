# Writing Plans, task e implementazione inline

1. Non iniziare la modifica senza aver capito l'esito atteso. Crea `PLAN.md` con MVP, cosa non fare, criteri di successo, rischi, dipendenze, strategia test e TASK-001… ; usa writing plans in modo persistente. Se la modalità Plan non concede scrittura, prepara il piano in chat e persisti quando autorizzato.
2. Ottieni un OK al piano e alla scelta A/B/C quando significativa. Identifica file già modificati da altri e non sovrascriverli.
3. Per ogni task: preflight Git/status, modifica circoscritta **inline con Opus**, verifica locale, screenshot/anteprime quando supportati, niente attese non necessarie.
4. Bug: formula ipotesi falsificabile e osservazione prima di correggere; se un test fallisce due volte dopo correzioni sulla stessa causa, stop prima del terzo tentativo e confronto su alternative. Reset del contatore solo a causa distinta esplicitata, mai per aggirare il blocco.
5. Fine task: riepiloga obiettivo, file, test eseguiti e loro esito, rischi, decisioni, prossimo task, `HANDOFF.md` compatto. Domanda: «Vuoi continuare, fare commit (salvataggio locale), push (invio GitHub) o fermarti?» Commit e push sono due permessi separati; non forzare remote.
6. Aggiorna `STATE.json` e `PLAN.md` senza duplicare paragrafi lunghi. Se cambia ambito, torna alla decisione e richiedi OK.

Se non ci sono strumenti di esecuzione, produci istruzioni verificabili e dichiara esplicitamente che non hai testato. Non considerare un task DONE per la sola compilazione: prova il caso d'uso e almeno una regressione quando applicabile.

## Revisioni e contesto

Non revisionare l'intera applicazione dopo ogni task: fai test locali mirati e una **review finale di progetto** soltanto quando il candidato release è integrato. Usa `context-budget.md` per terminare la sessione con handoff a 70% osservato. Un errore di test o CI richiede una correzione mirata, non tre revisioni globali ripetute.
