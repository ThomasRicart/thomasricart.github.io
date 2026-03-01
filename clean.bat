del /S /Q *.aux *.pytxcode *.thm *.log *.out *.toc *.lof *.lot *.nav *.snm *.synctex.gz *.bbl *.blg *.fls *.aux *.xsim *.fdb_latexmk

@echo off
setlocal enabledelayedexpansion

:: Recherche récursive des dossiers "pythontex-files*"
for /d /r %%D in (pythontex-files*) do (
    echo Suppression du dossier : "%%D"
    rd /s /q "%%D"
)

echo Suppression terminée.
pause