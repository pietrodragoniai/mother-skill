@echo off
setlocal DisableDelayedExpansion
echo === MOTHER SKILL - SMART SETUP ===
echo Controllo Claude Code. Non modifico gli account o le impostazioni.

where claude >nul 2>nul
if errorlevel 1 goto missing_cli
claude --version >nul 2>nul
if errorlevel 1 goto broken_cli
echo [OK] Claude Code installato.

set "AUTH_READY=0"
claude auth status >nul 2>nul
if errorlevel 1 goto auth_unconfirmed
set "AUTH_READY=1"
echo [OK] Login esistente verificato. Nessun nuovo accesso necessario.
goto skill_check
:auth_unconfirmed
echo [ACCESSO DA VERIFICARE] Claude installato, login non confermato.
echo Se necessario, Claude mostrera la schermata di accesso ufficiale.
echo Non modifico l'eventuale configurazione aziendale.

:skill_check
if not exist "%USERPROFILE%\.claude\skills\mother-skill\SKILL.md" goto missing_skill
echo [OK] Skill presente.
set "DEFAULT=%USERPROFILE%\Documents\Progetti-Mother\primo-progetto"
echo Se hai un progetto esistente, inserisci il percorso completo.
echo Oppure premi Invio per creare: "%DEFAULT%"
set /p "PROJECT=Cartella del progetto: "
if not defined PROJECT set "PROJECT=%DEFAULT%"
set "PROJECT=%PROJECT:"=%"
if /I "%PROJECT%"=="%USERPROFILE%" goto unsafe
if /I "%PROJECT%"=="%USERPROFILE%\Documents" goto unsafe
if /I "%PROJECT%"=="%USERPROFILE%\Downloads" goto unsafe
if /I "%PROJECT%"=="%USERPROFILE%\Desktop" goto unsafe
if /I "%PROJECT%"=="%SystemRoot%" goto unsafe
if /I "%PROJECT%"=="%SystemDrive%\" goto unsafe
if not exist "%PROJECT%" mkdir "%PROJECT%"
if errorlevel 1 goto failed
pushd "%PROJECT%"
if errorlevel 1 goto failed
echo [OK] Cartella: "%CD%"
echo Non modifico file esistenti. In Claude digita: /mother-skill Ho un idea
if "%AUTH_READY%"=="1" goto choose_model
goto launch_default

:choose_model
echo Mantengo il tuo modello attuale, salvo tua scelta per questa sessione.
set "USE_OPUS="
set /p "USE_OPUS=Avviare questa sessione con Opus 5.5 High? [s/N]: "
if /I "%USE_OPUS%"=="s" goto launch_opus
if /I "%USE_OPUS%"=="si" goto launch_opus
goto launch_default
:launch_opus
claude --model claude-opus-5-5 --effort high
goto done
:launch_default
claude
goto done
:done
set "STATUS=%ERRORLEVEL%"
popd
if not "%STATUS%"=="0" goto failed
exit /b 0

:missing_cli
echo [NUOVO / DESKTOP] Non trovo Claude Code nel terminale.
echo Se usi gia Claude Desktop, apri la scheda Code, scegli una sessione locale
 echo e una cartella di progetto. Poi digita: /mother-skill
echo Altrimenti installa dalla guida: https://code.claude.com/docs/en/quickstart
pause
exit /b 1
:broken_cli
echo [DA VERIFICARE] Il comando claude esiste ma non funziona.
echo Non reinstallo nulla. Usa: claude doctor
echo Guida: https://code.claude.com/docs/en/setup
pause
exit /b 1
:missing_skill
echo Skill mancante. Usa INSTALLA-WINDOWS.cmd; non reinstallare Claude Code.
pause
exit /b 1
:unsafe
echo Scegli una sottocartella dedicata, non l'intera cartella utente o di sistema.
goto failed
:failed
echo Controlla il percorso o le impostazioni. Non ho toccato configurazioni di Claude.
pause
exit /b 1
