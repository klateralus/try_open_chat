@ECHO off

SETLOCAL EnableDelayedExpansion

SET "EXEC_DIR=%~dp0"
SET "PACKAGES_DIR=!EXEC_DIR!packages

ECHO "Installing non built-in packages: PySide2, keyring, openai to !PACKAGES_DIR! ..."
python -m pip install PySide2 keyring openai --target !PACKAGES_DIR! --no-user
ECHO "Packages are installed!"

ECHO "Running AI Assistant..."
python ___.py
ECHO "AI Assistant is shutdown..."

ECHO "Removing non built-in packages: PySide2, keyring, openai from !PACKAGES_DIR! ..."
rmdir /s /q !PACKAGES_DIR!
ECHO "Folders are cleaned"

ECHO "Thank you for trying, have a great day!"