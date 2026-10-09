# Quality & Release Engine

Prima di scrivere: check baseline, file esistenti, segreti esclusi dal Git (`.env`, chiavi), licenze, privacy, eventuali dati personali e spese cloud. Verifica responsive, accessibilità, error handling, performance e ripristino secondo impatto reale. Dipendenze: niente installazione indiscriminata.

## Flusso Git e CI corretto
1. Lavoro locale verificato → ottenere consenso al **commit**; il commit è la versione locale, NON un rilascio.
2. Ottenere consenso al **push** → invia branch remoto; controlla remote/upstream e accesso.
3. PR sul branch → link reale, descrizione di comportamento, test, screenshot pertinenti, rischi e migrazioni.
4. Leggi run CI reale tramite permessi concessi; se non accessibile, NON segnare verde. Se rossa: diagnosi con log, fix inline, test locale, commit/push fix autorizzati, nuova CI. Due fix consecutivi falliti stessa causa → stop, nuove ipotesi e confronto umano. NON saltare check, branch protection, review o `--dangerously-skip-permissions`.
5. Su CI verde richiedi **OK CI** esplicito, a prescindere dall'autonomia.
6. Staging/preview: configura SOLO ambiente reale e consentito. A seconda della piattaforma la preview può crearsi già dopo la PR; distingui in tal caso fra URL disponibile e autorizzazione a promuovere. Fai smoke test; utente prova e dà **OK staging**.
7. Produzione: prepara versione/changelog PRIMA del build/tag/deploy secondo policy, controlla migrazioni, backup, rollback, approvazioni e domande su costi. Richiedi **OK produzione** distinto dall'OK staging. Poi merge/promozione/deploy consentiti. Verifica URL live, versione/hash e health; registra realmente ciò che è successo.
8. Se non è possibile pubblicare, lascia stato BLOCKED/PENDING, offri istruzioni ma non simulare deploy o test utente.

## No permessi magici
Una skill non può «accendere i permessi» di Github, CI o provider automaticamente. Chiedi all'utente di autorizzare i tool nella UI di Claude Code / credenziali OAuth del provider; mai chiedere token/password in chat. Gli script di stato sono ausili di tracciamento, non barriere di sicurezza. Non scaricare comandi shell non verificati; nessun deploy incontrollato.

## No monitoraggio fittizio
Controlla la CI finché gli strumenti/sessione lo consentono. Non promettere azioni asincrone dopo uscita se non esistono pipeline/notifiche reali configurate con consenso.
