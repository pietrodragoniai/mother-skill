# Starter Zero + Smart Setup — prima ancora del quiz

## Il paradosso di avvio
La skill può guidare SOLO quando è caricata da Claude Code. Prima servono installazione dell'app/CLI, una cartella di lavoro e l'installazione della skill. La distribuzione include `01-APRI-QUI.html` (guida primaria per principianti, apribile con doppio clic in un browser), `START-QUI.md` (guida tecnica alternativa), installer locali e launcher. Non presentare come automatico un passaggio svolto manualmente.

## Prima regola: non reinstallare chi è già operativo

La skill gira **dentro** Claude Code e non può eseguire controlli prima del suo avvio. Il pacchetto esterno, invece, include launcher di preflight che distinguono: (1) CLI presente e login verificato, (2) CLI presente e login non verificato, (3) CLI non raggiungibile nel terminale, (4) CLI danneggiata/non avviabile. Desktop Code è un percorso indipendente: assenza di `claude` nel PATH non prova assenza di Desktop. Consulta anzitutto `01-APRI-QUI.html`; `START-QUI.md` resta una guida tecnica alternativa.

- Se Claude CLI e account sono già pronti: **mai proporre di reinstallare, ri-autenticare, resettare, aggiornare, sovrascrivere settings o inizializzare Git**. Verifica solo workspace e disponibilità della skill; salva le preferenze tecniche che l'utente vuole mantenere.
- Se manca solo il login: non reinstallare; chiedi login tramite schermata ufficiale di Claude o il flusso aziendale.
- Se manca la CLI ma l'utente usa Desktop Code: illustra nuova sessione Code locale e cartella progetto, senza imporre terminale.
- Se la CLI esiste ma il comando di verifica fallisce: `claude doctor` e diagnosi prima di qualsiasi reinstallazione.
- Se la versione è vecchia e `claude auth status` non funziona: stato **sconosciuto**, non inferire "logout".
- Usa `claude --version` e `claude auth status` solo se appropriato e in modalità non invasiva; non stampare output che può includere dettagli del profilo.
- Il modello Opus 5.5 High richiede accesso; per utenti già configurati non sovrascrivere silenziosamente modello/effort globali. Una selezione CLI per sessione va concordata.

## Percorso A — Desktop, per chi teme il terminale
1. Conferma che l'utente sia nell'app **Claude Desktop > Code**, non in una normale chat o sessione cloud senza filesystem locale.
2. Crea una cartella dedicata tramite Finder (Mac) / Esplora file (Windows) in Documenti, ad esempio `Progetti Opus/Mia App`. Non partire dalla cartella Documenti intera, da Download, dalla home o da una cartella contenente dati privati.
3. Nuova sessione Code locale e seleziona la cartella dedicata nell'interfaccia; controlla nome e percorso prima di consentire scrittura. Se il menu/plugin non mostra la skill personale, suggerisci il percorso terminale o distribuzione plugin quando disponibile, senza inventare integrazione.
4. Mostra come visualizzare la preview del progetto, distinguendola dall'app pubblicata.

## Percorso B — Terminale, con esempi copia/incolla
- Mac: Finder → Applicazioni → Utility → Terminale; Windows: Start → Terminale / PowerShell.
- `pwd` su Mac/Linux e `Get-Location` su PowerShell mostrano **dove ti trovi**; `cd` cambia cartella, `mkdir` crea una cartella.
- La cartella scelta è il workspace. Lancia `claude` **da dentro**: `cd ~/Documents/Progetti-Mother/mia-app && claude` su Mac, oppure `cd "$HOME\Documents\Progetti-Mother\mia-app"; claude` in PowerShell (solo con cartella esistente).
- Installer ufficiali aggiornati: https://code.claude.com/docs/en/quickstart . Per utenti assoluti suggerisci i launcher allegati alla skill, che fanno `cd` da soli. Verifica `claude --version` e login; non chiedere mai di incollare password o API key nella chat.

## Checklist preflight (read-only prima di qualsiasi installazione)
- sistema operativo e disponibilità di `claude --version`;
- eventuale login Claude completato; piano/accesso a Claude Code/Opus secondo disponibilità;
- percorso workspace e permessi locali;
- file preesistenti/monorepo: ispeziona, non sovrascrivere;
- Git disponibile? Non è indispensabile per parlare dell'idea; richiederlo solo quando serve;
- connettività e costi potenziali: non presupporre un piano gratuito illimitato.

## Primo messaggio adatto al beginner
«Benvenuto. Prima ti mostro dove lavoreremo: [cartella]. Claude legge e modifica file in questa cartella solo secondo i permessi concessi. Iniziamo dalla tua idea. Hai in mente un'app, un sito, un video o vuoi partire da una proposta semplice?»

Se bloccato: mostra **un solo passo per volta**, come copiare un comando, e chiedi cosa appare sullo schermo. Non eseguire istruzioni da siti sconosciuti o richiedere privilegi amministratore senza necessità. `claude doctor` è utile per diagnostica CLI se disponibile.
