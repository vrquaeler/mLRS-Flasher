#!/usr/bin/env python3
#*******************************************************
# Copyright (c) MLRS project
# GPL3
# https://www.gnu.org/licenses/gpl-3.0.de.html
#*******************************************************
# Win Launcher
# 6. Apr. 2025
#********************************************************

import subprocess
import os, time


def setup_virtualenv():
    print('------------------------------------------------------------')
    print("Setting up mLRS-Flasher.")
    print("Note: This can take a moment, please be patient a just wait.")
    print("This does not affect your system in any way.")
    print("You always can undo by deleting the folder 'venv'.")
    print('------------------------------------------------------------')
    
    # Create virtual environment
    print("1. Setting up the virtual environment")
    print("...")
    subprocess.run(["python", "-m", "venv", "venv"], check=True)
    print("virtual environment created")
    
    print('------------------------------------------------------------')
    
    # Upgrade pip
    print("2. Upgrade pip")
    subprocess.run(["venv\\Scripts\\python", "-m", "pip", "install", "--upgrade", "pip"], check=True)
    print("pip upgraded")
    
    print('------------------------------------------------------------')
    
    # Install required modules
    print("3. Install required modules into virtual environment")
    subprocess.run(["venv\\Scripts\\python", "-m", "pip", "install", "pillow", "requests", "pyserial", "customtkinter", "tk"], check=True)
    print("required modules installed")
    
    print('------------------------------------------------------------')
    print('### DONE ###')
    print('')


if __name__ == "__main__":
    # Check if venv folder exists before running mLRS_Flasher
    if not os.path.isdir("venv"):
        setup_virtualenv()
        time.sleep(1)
        
    print('------------------------------------------------------------')
    print("Start mLRS-Flasher")
    print('------------------------------------------------------------')
        
    #subprocess.run(["venv\\Scripts\\pythonw.exe", "mLRS_Flasher.py"], check=True)        
    subprocess.Popen(["venv\\Scripts\\pythonw.exe", "mLRS_Flasher.py", "-frozen"])        

    time.sleep(0.5)
    