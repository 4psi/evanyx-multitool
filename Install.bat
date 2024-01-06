@echo off
title Installing Modules...

rem Check if Python is installed
py --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Installing Python...
    REM Download and install Python
    curl -o python-installer.exe https://www.python.org/ftp/python/3.11.4/python-3.11.4-amd64.exe
    start /wait python-installer.exe /quiet PrependPath=1
    del python-installer.exe
)

rem If Python was not installed before, change the title to "Installing Modules..."
title Installing Modules...

rem Install required Python modules
echo Installing required modules...
python -m pip install -r requirements.txt

color b
cls
echo Downloaded All Modules!
PAUSE

rem Run the main Python script
python main.py
