# Mother Skill 🐣

**Your mom, but for coding.**  
**She raised you to ship.**

Non sai cos’è un repository? Non sai collegare una cartella a Claude Code? Oppure lavori già con Git, PR e CI/CD ma vuoi meno giri inutili?

## 🚀 Install Mother Skill

Already using Claude Code? No ZIP needed.

Paste these commands into your Claude Code session, one at a time:

**1. Add the marketplace**
```text
/plugin marketplace add pietrodragoniai/mother-skill
```

**2. Install Mother Skill**
```text
/plugin install mother-skill@mother-skill-marketplace
```

**3. Start Mother Skill**

Restart Claude Code or reload your plugins, then type:
```text
/mother-skill:mother-skill
```

**Your mom, but for coding. She raised you to ship. 🇮🇹**

**Mother Skill è la skill da installare per prima.** Ti accompagna dall’idea al primo prodotto funzionante, imparando quanto sai già e adattando il linguaggio. Non è un modello, un IDE o un servizio di hosting: è un workflow guidato per **Claude Code**.

> Ti insegna a camminare fra terminale e GitHub. Ti fa rifare i compiti quando servono. Ma non ti fa girare a vuoto per tre giorni.  
> *P.S. Non ti prepara la merenda. Ti prepara la pull request.*

**Release:** 1.0.0 · **Stato:** beta pubblica da collaudare · **Lingua:** italiano · **Esecutore previsto:** Claude Opus 5.5 High, inline.

## 🚀 La prima cosa da aprire

1. Scarica ed **estrai completamente** il pacchetto.
2. Apri con doppio clic **[`01-APRI-QUI.html`](01-APRI-QUI.html)**. È una guida interattiva offline nel browser: **niente lettori `.md`**.
3. Indica **Mac/Windows** e se Claude Code è già pronto, ha bisogno di login o manca.
4. Esegui l'installer della skill, poi l'avviatore; apri o crea una **cartella dedicata**.
5. In Claude Code digita **`/mother-skill Ho un'idea`**.

Se Claude Code funziona già, **non viene reinstallato né riconfigurato**. Gli avviatori rilevano la situazione e preservano account, impostazioni e progetti. L'installer copia la skill; non scarica applicazioni da Internet.

## Cosa fa mamma

| Tappa | Cosa ricevi |
|---|---|
| **Mother Knows Best** | Smart Setup + quiz iniziale: niente termini dati per scontati |
| **Grill Me** | Soft / Medium / Hard / Extreme + idee, obiezioni, alternative |
| **Growing Up** | MVP e piano a task, scelte tecnologiche spiegate |
| **Show Me Three** | A/B/C o prototipi solo quando serve davvero scegliere |
| **Do Your Homework** | Implementazione *inline* con Opus, screenshot utili, test mirati |
| **Clean Your Room** | Wiki/Second Brain snello, stato e handoff, contesto sotto controllo |
| **No Red CI Tonight** | Commit, push, PR, CI, staging e produzione con controlli reali |
| **Leave the Nest** | Changelog, versione, ripresa e manutenzione |

### Regole che ci distinguono

- **Un solo agente sviluppa:** niente dispatch a Sonnet/Haiku/altre istanze per scrivere, integrare o revisionare lo stesso task. CLI, test runner, CI e browser restano strumenti utilizzabili.
- **Context first:** se la percentuale è *osservabile*, prepara handoff al **60%** e prima di iniziare nuovi task lunghi al **70%** passa a una sessione pulita. Non inventa telemetria e non cancella nulla per fare spazio.
- **Niente loop infiniti:** due tentativi di correzione falliti per la stessa causa → diagnosi alternativa e confronto con l'utente prima del terzo.
- **Review unica a fine progetto/release**, ma **test e verifiche mirate a ogni task**. Una nuova review globale solo se il lavoro successivo invalida la precedente.
- **Sicurezza prima della velocità:** permessi reali, protezione segreti, backup, conferme per costi, migrazioni distruttive e produzione. Nessuna modalità “autopilot” li supera.

**«Fino al 75% di token in meno» è un obiettivo sperimentale, NON un risultato misurato.** Per pubblicare un numero attendibile servono misure su task comparabili. Leggi il [manifesto](PERCHE-MOTHER-SKILL.md) e il [protocollo benchmark](benchmarks/README.md).

## Installazione per chi è già pratico

```bash
# Copia la cartella mother-skill/ (non lo ZIP) in ~/.claude/skills/
# Poi apri Claude Code nel progetto:
claude
# Nella chat di Claude Code:
/mother-skill
```

L'installazione manuale è un'alternativa ai file `INSTALLA-MAC.command` e `INSTALLA-WINDOWS.cmd`. Per la distribuzione GitHub puoi anche usare il [marketplace locale/versionato](GITHUB-PUBLISH.md): la sintassi diventa `/mother-skill:mother-skill` per una skill installata come plugin. Non installare due copie della stessa skill se non necessario.

## Documentazione

- [Inizia nel browser](01-APRI-QUI.html) · [Guida testuale](START-QUI.md)
- [Manifesto della mamma](PERCHE-MOTHER-SKILL.md) · [FAQ](FAQ.md)
- [Istruzioni della skill](mother-skill/SKILL.md) · [Protocollo di contesto](mother-skill/references/context-budget.md)
- [Pubblicazione GitHub](GITHUB-PUBLISH.md) · [Kit social](KIT-LANCIO.md)
- [Test e benchmark](benchmarks/README.md) · [Contribuire](CONTRIBUTING.md) · [Sicurezza](SECURITY.md)

## Limiti reali

Questa release non è stata verificata end-to-end su ogni installazione Claude Code e lo starter Windows richiede ancora un test nativo. Il modello Opus 5.5 High dipende dall'account/configurazione disponibile; l'impostazione nel frontmatter vale per il turno di invocazione, non è un blocco permanente della sessione. La skill non può creare permessi o verificare CI/deploy senza strumenti/autorizzazioni. Non promette supervisione in background.

**Licenza:** da scegliere prima della pubblicazione open-source; vedi [LICENZA-DA-SCEGLIERE.md](LICENZA-DA-SCEGLIERE.md).
