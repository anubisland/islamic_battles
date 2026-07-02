@echo off
echo ========================================
echo   Deploying Islamic Battles Atlas v5
echo ========================================

cd /d "C:\Users\melwa\OneDrive\Documents\GitHub\islamic_battles"

echo.
echo [1] Copying downloaded index.html...
if exist "%USERPROFILE%\Downloads\index.html" (
    copy /Y "%USERPROFILE%\Downloads\index.html" "index.html"
    echo     Done - copied from Downloads
) else (
    echo     WARNING: No index.html found in Downloads folder
    echo     Will use existing index.html in repo folder
)

echo.
echo [2] Current file size:
for %%A in (index.html) do echo     %%~zA bytes

echo.
echo [3] Git status:
git status --short

echo.
echo [4] Staging...
git add index.html

echo.
echo [5] Committing...
git commit -m "feat: atlas v5 - language picker AR/EN + 5 voices + lessons EN translation"

echo.
echo [6] Pushing to GitHub...
git push origin main

echo.
echo ========================================
if %ERRORLEVEL% EQU 0 (
    echo   SUCCESS! Site will update in ~1 minute
    echo   URL: https://anubisland.github.io/islamic_battles/
) else (
    echo   ERROR: Push failed - check output above
)
echo ========================================
pause
