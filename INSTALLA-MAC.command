#!/bin/bash
set -euo pipefail
HERE="$(cd -- "$(dirname -- "$0")" && pwd -P)"
SRC="$HERE/mother-skill"
BASE="$HOME/.claude/skills"
DST="$BASE/mother-skill"
# If an old Opus Inline Studio copy exists, do not silently remove it.
LEGACY="$BASE/opus-inline-studio"
if [[ -e "$LEGACY" || -L "$LEGACY" ]]; then
  echo 'Vedo anche la vecchia skill Opus Inline Studio. Non la modifico.'
  echo 'Se vuoi evitare due comandi nel menu, puoi archiviarla manualmente in seguito.'
fi
if [[ ! -f "$SRC/SKILL.md" ]]; then
  echo 'ERRORE: pacchetto incompleto. Estrai tutto lo ZIP prima.'; read -r -p 'Invio per chiudere...' _; exit 1
fi
mkdir -p "$BASE"
if [[ -e "$DST" || -L "$DST" ]]; then
  BACKUP="$BASE/mother-skill-backup-$(date +%Y%m%d-%H%M%S)-$$"
  echo "Versione precedente rilevata: la salvo in $BACKUP"
  mv "$DST" "$BACKUP"
fi
if ! cp -R "$SRC" "$DST"; then
  echo 'Copia non riuscita. Tento il ripristino del backup.'
  rm -rf "$DST"
  if [[ -n "${BACKUP:-}" && -e "$BACKUP" ]]; then mv "$BACKUP" "$DST"; fi
  read -r -p 'Invio per chiudere...' _; exit 1
fi
echo
printf 'SKILL INSTALLATA! File: %s\n' "$DST/SKILL.md"
echo 'Ora usa AVVIA-MAC.command: rileva Claude Code e riutilizza la tua configurazione.'
read -r -p 'Invio per chiudere...' _
