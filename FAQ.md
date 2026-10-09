# FAQ · Mother Skill

### Non so cosa sia una cartella: posso iniziare?
Sì. Estrai lo ZIP, apri `01-APRI-QUI.html` nel browser e scegli il tuo percorso. Non serve aprire file Markdown.

### Ho già Claude Code installato: devo reinstallarlo?
No. Installa soltanto la skill. L'avviatore controlla la CLI e il login senza modificare l'account.

### Cosa significa «Mother Skill»?
È la skill che ti accompagna mentre impari: prima ti aiuta con le basi, poi ti lascia sempre più autonomo. Il tono scherzoso non cambia le protezioni tecniche.

### Lavora sempre con Opus 5.5 High?
È il modello/effort richiesto dalla skill, ma la disponibilità dipende dall'account e dalle policy. Il frontmatter può impostarlo per il solo turno; la sessione non è bloccata per sempre. Non c'è fallback silenzioso.

### Non usa mai agenti?
Non delega programmazione o review ad agenti paralleli. Può usare browser, test runner, compilatori, Git e CI come strumenti. Se la piattaforma non supporta un'operazione lo segnala.

### Ha davvero il 75% di token in meno?
Non ancora dimostrato. È un obiettivo di benchmark. Senza esperimenti comparabili non si può promettere il numero.

### Perché la soglia di contesto è al 70%?
È una scelta prudenziale per conservare margine e ridurre riletture inutili, non un limite imposto da Claude. La percentuale deve essere osservabile: altrimenti non viene inventata.

### Gli installer cancellano qualcosa?
Copiano i file della skill e fanno backup di una vecchia versione con lo stesso nome; non alterano la configurazione di Claude o i progetti. Prova comunque la beta su un progetto non importante.

### Perché ci sono file `.md`?
Sono documentazione per GitHub e per gli sviluppatori. L'utente principiante apre soltanto `01-APRI-QUI.html`.

### Posso usarla in aziende o su dati veri?
Richiede controlli sui permessi, segreti, privacy, backup e costi. Prima prova la beta in una cartella dedicata con dati non sensibili. Non è una certificazione di sicurezza.

### Cosa succede se la CI fallisce?
Opus tenta correzioni mirate, senza disabilitare i test per avere verde. Dopo due tentativi falliti sulla stessa causa riconsidera la diagnosi con te.

### Come contribuisco?
Apri una issue con versione, sistema operativo, percorso e passi per riprodurre. Non pubblicare segreti o log contenenti dati privati.
