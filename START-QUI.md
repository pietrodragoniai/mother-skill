# Preferisci non aprire un Markdown?

**Per iniziare fai doppio clic su `01-APRI-QUI.html`: si apre nel tuo browser, anche senza un programma per i file `.md`.** Questa pagina è la guida tecnica alternativa.

---

# INIZIA QUI — MOTHER SKILL v1.0: SMART SETUP

Benvenuto! Puoi partire da zero **oppure usare il Claude Code che hai già configurato**. Non è necessario reinstallarlo.

## 1. Prima domanda: come usi Claude oggi?

### A — Ho già Claude Code nel terminale e funziona

1. **Salta completamente l'installazione di Claude Code.** Non toccare le impostazioni, gli account o i progetti già esistenti.
2. Estrai lo ZIP ed esegui soltanto `INSTALLA-MAC.command` o `INSTALLA-WINDOWS.cmd` per aggiungere la skill (se era già presente, viene effettuato un backup della skill precedente).
3. Hai già un progetto aperto? Apri una **nuova sessione** di Claude Code nella sua cartella e digita `/mother-skill`. Oppure utilizza `AVVIA-MAC.command` / `AVVIA-WINDOWS.cmd` per scegliere una cartella.
4. Se vuoi il workflow originale, puoi scegliere **Opus 5.5 High soltanto per la sessione**. La disponibilità dipende dal tuo accesso; il programma non cambia le impostazioni globali.

### B — Ho Claude Code installato ma non ho completato il login

1. **Non reinstallarlo.** Il launcher riconosce la presenza del comando e ti comunica se il login non è verificato.
2. Esegui l'installer della **skill**, poi l'avviatore. Se Claude chiede accesso, completa il login **nell'interfaccia ufficiale**.
3. Se lavori tramite un provider aziendale o una configurazione personalizzata, non resettare nulla: verifica con il tuo amministratore o con la guida Anthropic.

### C — Uso già l'app Claude Desktop, scheda Code

1. Non sei obbligato a installare la CLI del terminale per usare **Claude Desktop Code**.
2. Installa la skill con l'installer per il tuo sistema, poi apri **Claude Desktop > Code > nuova sessione locale** e seleziona una cartella dedicata. Se necessario, riavvia la sessione per rilevare la skill.
3. Digita `/mother-skill` se compare fra le skill disponibili. Se non compare, consulta la guida all'integrazione delle skill o prova il percorso CLI (non presumere che la chat Claude ordinaria abbia accesso alla cartella).

### D — Non ho mai installato Claude Code

1. Puoi scegliere l'app grafica **Claude Desktop, scheda Code**, oppure l'installazione CLI dalla guida ufficiale: https://code.claude.com/docs/en/quickstart . È richiesto un piano/account compatibile con Claude Code.
2. Per la CLI, su **Mac** apri Terminale ed esegui `curl -fsSL https://claude.ai/install.sh | bash`; su **Windows** apri PowerShell ed esegui `irm https://claude.ai/install.ps1 | iex`. Gli script scaricano software ufficiale; sono disponibili alternative come Homebrew/WinGet.
3. Riapri il terminale e prova `claude --version`, poi avvia `claude` e completa l'accesso nell'interfaccia ufficiale. Non inviare mai password o chiavi API in chat.
4. Installa la skill con `INSTALLA-*.command` o `INSTALLA-WINDOWS.cmd`, poi avviala dalla cartella del progetto.

### E — Ho installato qualcosa, ma non so se funziona

Su Mac usa Terminale, su Windows PowerShell. Verifica:

```text
claude --version
claude auth status
```

Il primo comando verifica che il programma sia disponibile; il secondo verifica lo stato dell'autenticazione (senza mostrare credenziali nella nostra skill). Se `claude` non viene trovato, **non significa necessariamente che Claude Desktop non sia installato**. Se la versione non risponde, prova `claude doctor` e consulta https://code.claude.com/docs/en/setup . Non reinstallare a tentativi.

## 2. Che cosa fanno i file dello ZIP?

- `INSTALLA-MAC.command` o `INSTALLA-WINDOWS.cmd` **copiano solo questa skill**, non Claude Code. Se esiste una versione precedente della skill, ne fanno un backup.
- `AVVIA-MAC.command` o `AVVIA-WINDOWS.cmd` **rilevano** se la CLI esiste, se risponde e se il login è verificato. Poi ti aiutano a scegliere una cartella e ad aprire Claude. Non cambiano le impostazioni globali.
- Se Claude Code è già aperto nella cartella giusta e hai installato la skill, basta avviare una nuova sessione e richiamare `/mother-skill`.

**Scegli una cartella dedicata.** Puoi lasciare vuoto il percorso nell'avviatore per crearne una in Documenti; se hai già un progetto, indica la sua cartella esistente. Evita la home, l'intera cartella Documenti o cartelle di sistema.

## 3. Quando Claude Code si apre

Digita:

```text
/mother-skill Ho un'idea
```

La skill propone un quiz adattivo, Grill Me e un percorso guidato dall'idea al prodotto. GitHub, commit, push, Node.js, SQL, deploy e altri strumenti verranno spiegati quando necessari.

## 4. Mini glossario

- **CLI/terminale**: interfaccia in cui impartisci comandi scritti.
- **Cartella di progetto**: spazio del computer che contiene i file della tua app.
- **Repository**: progetto con cronologia delle modifiche gestita da Git.
- **Commit**: salvataggio di modifiche nella cronologia locale; **push**: invio al remoto, per esempio GitHub.
- **Deploy**: pubblicazione del prodotto online; non coincide con push.

## Sicurezza e limiti

Gli avviatori non eseguono installazioni da Internet, non fanno logout, non modificano le impostazioni di Claude, non toccano il tuo repository e non richiedono privilegi da amministratore. `claude auth status` può non essere disponibile in installazioni obsolete: in quel caso il login risulta semplicemente **non verificato**, non necessariamente assente. L'accesso specifico al modello Opus 5.5 High va verificato nella tua sessione; non viene forzata una sostituzione silenziosa.

Guide ufficiali:
- https://code.claude.com/docs/en/quickstart
- https://code.claude.com/docs/en/setup
- https://code.claude.com/docs/en/desktop
- https://code.claude.com/docs/en/cli-reference

## Perché questo metodo?

Leggi `PERCHE-MOTHER-SKILL.md` per capire la strategia inline, il controllo del contesto al 70% e il perché delle revisioni finali non ripetitive. Il risparmio del 75% è un **target non ancora dimostrato**, non una garanzia.
