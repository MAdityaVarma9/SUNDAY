@echo off
REM Sunday Chatbot Launcher for Windows
REM This script launches the Sunday chatbot in your default browser

title Sunday - AI Assistant

REM Get the directory where this batch file is located
set "dir=%~dp0"

REM Launch the HTML file
start "" "%dir%sunday_chatbot.html"

REM Optional: Display welcome message
echo.
echo ========================================
echo    Sunday AI Assistant Launcher
echo ========================================
echo.
echo Launching Sunday in your default browser...
echo.
echo If Sunday doesn't open automatically:
echo 1. Make sure sunday_chatbot.html is in the same folder
echo 2. Try opening the HTML file directly in your browser
echo 3. Check that your browser can access local files
echo.
echo ========================================
pause