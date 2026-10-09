# Pubblicare Mother Skill su GitHub

**Stato:** repository ancora da pubblicare. Questa cartella è pronta per essere caricata, ma nessun repository remoto è stato creato automaticamente.

## Prima di tutto

1. Scegli la licenza: leggi `LICENZA-DA-SCEGLIERE.md` e aggiungi un file `LICENSE` autentico (MIT, Apache-2.0 o altra). **Senza licenza** non stai concedendo a terzi diritti generali di copia/modifica/distribuzione.
2. Sostituisci eventuali placeholder negli asset pubblici e scegli proprietario/nome del repository (consigliato `mother-skill`).
3. Rivedi gli script; prova l'avviatore Windows su macchina reale e il percorso Claude Code end-to-end prima di definire la release stabile.
4. Non committare credenziali, profili personali o cartelle `.claude` generate nei progetti di test.

## Da GitHub (metodo più semplice)

- GitHub → New repository → nome `mother-skill` → **vuoto**, senza README autogenerato.
- Estrai lo ZIP sul tuo computer e apri la cartella `mother-skill-v1.0`.
- Carica il contenuto del progetto nel repository oppure usa Git da terminale come sotto.
- Verifica nella scheda Actions che il workflow **Validation** sia verde; guarda i log se fallisce.
- Crea una release con tag `v1.0.0-beta.1` e allega il pacchetto ZIP di distribuzione.

## Con Git CLI

Esegui nella **radice estratta** (non dentro la cartella interna `mother-skill/`):

```bash
git init
git add .
git commit -m "feat: launch Mother Skill 1.0 beta"
git branch -M main
git remote add origin https://github.com/TUO-ACCOUNT/mother-skill.git
git push -u origin main
```

Il remote è un **esempio**; devi creare prima il repository e usare il tuo vero URL. `git push` richiede l'accesso al tuo account. Per il prossimo rilascio, aggiorna `CHANGELOG.md`, la versione del plugin, verifica CI e crea una GitHub Release.

## Usare Mother Skill dal marketplace GitHub

Il repository include `.claude-plugin/marketplace.json` e `mother-skill/.claude-plugin/plugin.json`.

```text
/plugin marketplace add https://github.com/TUO-ACCOUNT/mother-skill
/plugin install mother-skill@mother-skill-marketplace
```

Nelle installazioni plugin il comando è normalmente `/mother-skill:mother-skill`. In modalità *skill personale* (`~/.claude/skills/mother-skill`) il comando è `/mother-skill`. **Non installare entrambe le versioni per evitare comandi duplicati.** Verifica i comandi con `/help` o col menu `/` nella tua versione di Claude Code.

## Condivisione prima del GitHub pubblico

Manda lo ZIP e chiedi ai tester di estrarre tutto e aprire `01-APRI-QUI.html`. Non serve loro un programma per i file `.md`.

## Test tecnici

```bash
python -m compileall -q mother-skill/scripts
(cd mother-skill && python -m unittest discover -s tests -v)
python -m unittest discover -s benchmarks -v
```

`claude plugin validate .` e `claude plugin validate ./mother-skill` sono controlli aggiuntivi da eseguire **su un computer dove Claude Code è installato**; qui non sono stati verificati nella CLI reale.
