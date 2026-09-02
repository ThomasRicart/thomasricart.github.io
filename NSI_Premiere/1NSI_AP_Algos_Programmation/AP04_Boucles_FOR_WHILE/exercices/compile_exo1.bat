@echo off
set FILENAME=AP04_EXO1

echo ======================================================
echo   COMPILATION : PDFLATEX + PYTHONTEX + PDFLATEX
echo ======================================================

:: --- VERSION SUJET ---
echo [1/2] Generation du SUJET...
:: Passe 1 : Crée les fichiers .pytxcode
pdflatex -interaction=batchmode -jobname=%FILENAME%_Sujet "\def\visibleornot{invisible} \input{%FILENAME%.tex}"
:: Passe PythonTeX : Exécute le code contenu dans le document
pythontex %FILENAME%_Sujet
:: Passe 2 : Intègre les résultats et stabilise la pagination (\pageref{LastPage})
pdflatex -jobname=%FILENAME%_Sujet "\def\visibleornot{invisible} \input{%FILENAME%.tex}"


:: --- VERSION CORRECTION ---
echo [2/2] Generation de la CORRECTION...
:: Passe 1
pdflatex -interaction=batchmode -jobname=%FILENAME%_Correction "\def\visibleornot{visible} \input{%FILENAME%.tex}"
:: Passe PythonTeX
pythontex %FILENAME%_Correction
:: Passe 2
pdflatex -jobname=%FILENAME%_Correction "\def\visibleornot{visible} \input{%FILENAME%.tex}"

:: --- NETTOYAGE ---
echo Nettoyage des fichiers temporaires...
:: On garde les dossiers pythontex-files-xxx si tu en as besoin pour le debug, 
:: sinon tu peux ajouter des lignes pour les supprimer.
del /q %FILENAME%_Sujet.aux %FILENAME%_Sujet.log %FILENAME%_Sujet.out %FILENAME%_Sujet.pytxcode >nul 2>&1
del /q %FILENAME%_Correction.aux %FILENAME%_Correction.log %FILENAME%_Correction.out %FILENAME%_Correction.pytxcode >nul 2>&1

echo.
echo ✅ Termine ! Verifiez %FILENAME%_Sujet.pdf et %FILENAME%_Correction.pdf
pause