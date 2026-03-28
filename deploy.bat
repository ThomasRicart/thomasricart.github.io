@echo off
echo.
echo ========================================
echo   Deploiement du site de cours
echo ========================================
echo.

cd /d "D:\--- LYCEE ---\ENSEIGNEMENT_G\"

:: Demande un message de commit
set /p COMMIT_MSG="Message de commit (ex: ajout chapitre 3) : "

echo.
echo [1/3] Ajout des fichiers...
git add .

echo [2/3] Commit et push sur GitHub...
git commit -m "%COMMIT_MSG%"
git push

echo [3/3] Deploiement sur GitHub Pages...
mkdocs gh-deploy

echo.
echo ========================================
echo   Site mis a jour avec succes !
echo   https://thomasricart.github.io
echo ========================================
echo.
pause
