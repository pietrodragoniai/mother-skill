@echo off
setlocal
set "HERE=%~dp0"
set "SRC=%HERE%mother-skill"
set "BASE=%USERPROFILE%\.claude\skills"
set "DST=%BASE%\mother-skill"
if exist "%BASE%\opus-inline-studio\SKILL.md" echo [INFO] Rilevata anche la vecchia Opus Inline Studio. Non la modifico.
if not exist "%SRC%\SKILL.md" goto source_missing
if not exist "%BASE%" mkdir "%BASE%"
if errorlevel 1 goto failed
if exist "%DST%" goto backup_existing
goto copy_new
:backup_existing
set "BACKUP=%BASE%\mother-skill-backup-%RANDOM%-%RANDOM%"
echo Creo backup della skill precedente: "%BACKUP%"
move "%DST%" "%BACKUP%" >nul
if errorlevel 1 goto failed
:copy_new
xcopy "%SRC%" "%DST%" /E /I /H /Q /Y >nul
if errorlevel 1 goto restore
if not exist "%DST%\SKILL.md" goto restore
echo.
echo SKILL INSTALLATA: "%DST%\SKILL.md"
echo Ora apri AVVIA-WINDOWS.cmd: riutilizza la configurazione Claude esistente.
pause
exit /b 0
:restore
echo Errore durante la copia. Ripristino la versione precedente se presente.
if exist "%DST%" rmdir /S /Q "%DST%"
if defined BACKUP move "%BACKUP%" "%DST%" >nul
goto failed
:source_missing
echo Pacchetto incompleto: estrai tutto lo ZIP prima di avviare.
goto failed
:failed
echo Installazione non riuscita. Nessun download eseguito.
pause
exit /b 1
