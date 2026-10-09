# MOTHER SKILL
## La madre di tutte le skill. Letteralmente. (Beh, quasi.)

**Your mom, but for coding.**  
**She raised you to ship.**

Non sai programmare? Non hai mai aperto un terminale? Non sai neanche come aprire una cazzo di cartella in Claude Code?

Tranquillo. **C'è mamma.**

Mother Skill non nasce per farti sentire stupido. Nasce per portarti dal «non so da dove iniziare» al «questo l'ho costruito io». Senza spiegarti ogni giorno cos'è un commit quando lo sai già.

## Come una vera madre

- **Ti insegna a camminare.** Cartella, terminale, repository, commit e push. Uno alla volta, nel momento in cui servono.
- **Ti fa le domande scomode.** Il Grill Me prende la tua idea e cerca gli errori prima che diventino settimane buttate.
- **Ti fa scegliere.** Tre proposte quando hanno senso; niente tre mockup per correggere una virgola nel database.
- **Ti fa mettere in ordine la stanza.** Second Brain, wiki, handoff e piani: puliti, piccoli e recuperabili.
- **Non chiama gli zii per farti i compiti.** Opus lavora inline. Niente deleghe che moltiplicano briefing, riletture e revisioni della stessa attività.
- **Non ti lascia uscire con la CI rossa.** Test, correzioni, PR e preview prima di metterci la faccia in produzione.
- **Sa quando è ora di andare a dormire.** Quando il contesto cresce, prepara un handoff e ricomincia pulito.
- **E quando diventi bravo, smette di spiegarti le tabelline.** Le spiegazioni cambiano con te, non con l'umore del giorno.

## La filosofia: Context First

Il contesto è la risorsa più preziosa. Una sessione non migliora solo perché continua a rileggere gli stessi file. Per questo Mother Skill lavora in modo incrementale: stato breve, file mirati e un unico esecutore.

**60%:** se l'utilizzo del contesto è effettivamente noto, inizia a preparare l'handoff.  
**70%:** una volta messo in sicurezza il task, evita nuovi lavori lunghi, salva lo stato e proponi una nuova sessione nella stessa cartella.  
**Nuova sessione:** leggi `STATE.json`, handoff, stato Git e documenti pertinenti. Non riaprire l'intera wiki o il repository senza motivo.

Queste soglie sono una **policy operativa**, non un limite tecnico garantito. Se Claude Code non espone il dato, non inventiamo percentuali; si usa il giudizio per cambiare sessione dopo milestone o conversazioni molto lunghe.

## Revisione: una volta bene, non dieci volte a caso

Durante ogni task si fanno test mirati, controlli di sicurezza e verifiche del cambiamento. **La review globale, trasversale a tutto il progetto, si fa quando è pronto un candidato release.** Se emergono modifiche sostanziali, la review può essere ripetuta su quanto invalidato: non si sacrifica la qualità per uno slogan.

Dopo due correzioni fallite della stessa causa, niente terzo giro cieco: Mother Skill si ferma, propone una diagnosi alternativa, ne discute con te e procede solo con una nuova strategia.

## 75% di token risparmiati?

**È un obiettivo da validare, non una cifra dimostrata.** Il target del **-75%** rispetto ai workflow multi-passaggio più ridondanti richiede benchmark riproducibili, misurando token, costo, tempo e difetti fino a PR/CI/deploy equivalenti. La skill non può garantire questo risultato e non è corretto dichiarare «75% in meno» senza prove. Vedi `benchmarks/README.md`.

## Per chi è

Per chi non sa aprire una cartella, per il creativo con un'idea, per un professionista con poco tempo e per chi scrive codice già da anni ma vuole un percorso più lineare.

**Mother Skill non è magicamente superiore a ogni altro workflow.** Ha una tesi precisa — meno passaggi ripetuti, più continuità e più controllo — che puoi provare, criticare e misurare.

### Mother Skill. She raised you to ship.

*P.S. Non ti prepara la merenda. Ti prepara la pull request.*
