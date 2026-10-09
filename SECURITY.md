# Sicurezza · Mother Skill

Mother Skill è una **beta di workflow**. Non è un sandbox e non dà accesso autonomo ai sistemi: le azioni avvengono coi permessi reali di Claude Code, del terminale e degli account collegati.

- Non condividere segreti, token, `.env` o dati personali nelle issue.
- Prima di testare usa un progetto nuovo e non sensibile, senza servizi a pagamento.
- Gli installer installano solo la skill e mantengono backup delle versioni precedenti dello **stesso nome**; non reinstallano Claude Code.
- Push, PR, migrazioni distruttive, staging e rilascio dipendono dalle autorizzazioni esplicite previste dal flusso.
- Se trovi un problema di sicurezza, evita di pubblicare exploit o dati: contatta privatamente il manutentore del repository quando il canale sarà disponibile.

La CLI Windows non è ancora verificata nativamente in questa release.
