#!/bin/bash
set -euo pipefail

echo '=== MOTHER SKILL — SMART SETUP ==='
echo 'Controllo soltanto Claude Code. Nessuna reinstallazione o modifica ai tuoi account.'

# CLI missing does NOT prove Claude Desktop is missing.
if ! command -v claude >/dev/null 2>&1; then
  echo
  echo '[NUOVO / DESKTOP] Non trovo Claude Code nel terminale.'
  echo 'Se usi gia Claude Desktop > Code, apri una sessione locale nella cartella'
  echo 'del progetto e digita: /mother-skill'
  echo 'Altrimenti, segui la guida ufficiale: https://code.claude.com/docs/en/quickstart'
  read -r -p 'Premi Invio per chiudere...' _ || true
  exit 1
fi

if ! claude --version >/dev/null 2>&1; then
  echo
  echo '[DA VERIFICARE] Il comando claude esiste ma non risponde correttamente.'
  echo 'Non reinstallo nulla. Controlla con: claude doctor'
  echo 'Guida: https://code.claude.com/docs/en/setup'
  read -r -p 'Premi Invio per chiudere...' _ || true
  exit 1
fi

echo '[OK] Claude Code risulta installato.'
if claude auth status >/dev/null 2>&1; then
  AUTH_READY=1
  echo '[OK] Login gia configurato: nessun nuovo accesso richiesto.'
else
  AUTH_READY=0
  echo '[ACCESSO DA VERIFICARE] Installazione presente, login non confermato.'
  echo 'Continuando, Claude ti mostrera eventualmente il login ufficiale.'
  echo 'Se usi un account aziendale/provider esterno, conserva la sua configurazione.'
fi

SKILL="$HOME/.claude/skills/mother-skill/SKILL.md"
if [[ ! -f "$SKILL" ]]; then
  echo
  echo '[SKILL MANCANTE] Esegui INSTALLA-MAC.command una sola volta.'
  echo 'Non e necessario reinstallare Claude Code.'
  read -r -p 'Premi Invio per chiudere...' _ || true
  exit 1
fi

echo '[OK] La skill e installata.'
DEFAULT="$HOME/Documents/Progetti-Mother/primo-progetto"
echo
echo 'Se hai GIA un progetto, inserisci il percorso della sua cartella.'
echo "Se parti da zero, premi Invio: useremo $DEFAULT"
read -r -p 'Percorso completo della cartella del progetto: ' PROJECT || true
PROJECT="${PROJECT:-$DEFAULT}"
if [[ "$PROJECT" == '"'*'"' && ${#PROJECT} -ge 2 ]]; then PROJECT="${PROJECT:1:${#PROJECT}-2}"; fi
if [[ "$PROJECT" != /* ]]; then
  echo 'Inserisci un percorso assoluto, che inizi con /.'
  read -r -p 'Invio per chiudere...' _ || true
  exit 1
fi
# Check sensitive roots before creating anything.
case "${PROJECT%/}" in /|"$HOME"|"$HOME/Documents"|"$HOME/Downloads"|"$HOME/Desktop")
  echo 'Scegli una SOTTOCARTELLA dedicata: non home, Documenti, Download o Scrivania.'
  read -r -p 'Invio per chiudere...' _ || true
  exit 1;;
esac
mkdir -p -- "$PROJECT"
PROJECT="$(cd -- "$PROJECT" && pwd -P)"
case "$PROJECT" in /|"$HOME"|"$HOME/Documents"|"$HOME/Downloads"|"$HOME/Desktop")
  echo 'Cartella non sicura; avvio annullato.'
  exit 1;;
esac

echo "[OK] Cartella selezionata: $PROJECT"
echo 'Non elimino ne modifico file esistenti.'
echo 'Dentro Claude scrivi: /mother-skill Ho un idea'
cd -- "$PROJECT"

if [[ "$AUTH_READY" == 1 ]]; then
  echo
  echo 'Claude e gia configurato. Per rispettare le tue impostazioni, non cambio modello senza consenso.'
  read -r -p 'Solo per questa sessione: avvio con Opus 5.5 High? [s/N] ' USE_OPUS || true
  case "${USE_OPUS:-}" in
    s|S|si|SI|Si) exec claude --model claude-opus-5-5 --effort high;;
  esac
fi
exec claude
