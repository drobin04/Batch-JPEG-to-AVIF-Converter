@echo off

rem Set python directory
set PYTHON=C:\Users\Douglas\anaconda3\python.exe
echo %PYTHON%
pause
rem Get the directory of the .bat file
for %%i in ("%~dp0.") do set BAT_DIR=%%~fi

rem Set the path to the Python script
set SCRIPT_PATH=%BAT_DIR%\context_menu_convertjpg_to_avif.py

rem Set the name of the context menu item
set MENU_ITEM_NAME=Convert JPEGs to AVIFs

rem Create the context menu item key for files
reg add "HKEY_CLASSES_ROOT\*\shell\%MENU_ITEM_NAME%" /ve /t REG_SZ /d "%MENU_ITEM_NAME%" /f
reg add "HKEY_CLASSES_ROOT\*\shell\%MENU_ITEM_NAME%\command" /ve /t REG_EXPAND_SZ /d "\"%PYTHON%\" \"%SCRIPT_PATH%\" \"%%1\"" /f

rem Create the context menu item key for folders
reg add "HKEY_CLASSES_ROOT\Directory\shell\%MENU_ITEM_NAME%" /ve /t REG_SZ /d "%MENU_ITEM_NAME%" /f
reg add "HKEY_CLASSES_ROOT\Directory\shell\%MENU_ITEM_NAME%\command" /ve /t REG_EXPAND_SZ /d "\"%PYTHON%\" \"%SCRIPT_PATH%\" \"%%1\"" /f

rem Create the context menu item key for the background of folders
reg add "HKEY_CLASSES_ROOT\Directory\Background\shell\%MENU_ITEM_NAME%" /ve /t REG_SZ /d "%MENU_ITEM_NAME%" /f
reg add "HKEY_CLASSES_ROOT\Directory\Background\shell\%MENU_ITEM_NAME%\command" /ve /t REG_EXPAND_SZ /d "\"%PYTHON%\" \"%SCRIPT_PATH%\" \"%%V\"" /f

echo Context menu item created successfully.
pause
