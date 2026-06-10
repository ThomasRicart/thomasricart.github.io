@echo off
setlocal enabledelayedexpansion

echo --- Nettoyage des fichiers LaTeX et temporaires ---
del /S /Q *.aux *.pytxcode *.thm *.log *.out *.toc *.lof *.lot *.nav *.snm *.synctex.gz *.bbl *.blg *.fls *.aux *.xsim *.fdb_latexmk >nul 2>&1

:: Recherche récursive des dossiers "pythontex-files*"
for /d /r %%D in (pythontex-files*) do (
    echo Suppression du dossier : "%%D"
    rd /s /q "%%D"
)
echo Nettoyage termine.
echo.

:: Demande du message de commit
set /p message="Entrez votre message de commit (ex: Mise a jour doc) : "

echo --- Debut du processus complet ---

:: 1. Sauvegarde du code source sur GitHub (branche main)
echo [1/3] Sauvegarde du code source (Markdown et Python)...
git add -A

:: Astuce pour eviter que le script plante si aucun fichier n'a change
git diff-index --quiet HEAD --
if %ERRORLEVEL% NEQ 0 (
    git commit -m "%message%"
    git push origin main
    if !ERRORLEVEL! NEQ 0 (
        echo [ERREUR] Impossible de pousser les sources sur GitHub. Verification necessaire.
        pause
        exit /b
    )
) else (
    echo Aucun changement detecte dans les sources. Passage au deploiement.
)

:: 2. Generation et deploiement du site (GitHub Pages)
echo [2/3] Deploiement MkDocs en cours (avec nettoyage du cache)...
call mkdocs gh-deploy --clean --force
if %ERRORLEVEL% NEQ 0 (
    echo [ERREUR] Le deploiement MkDocs a echoue.
    pause
    exit /b
)

:: 3. Nettoyage du dossier local "site"
echo [3/3] Nettoyage du dossier local 'site'...
if exist site (
    rd /s /q site
    echo Dossier 'site' supprime.
)

echo --- Termine ! Tout est a jour ---
pause