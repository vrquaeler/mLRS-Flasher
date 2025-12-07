<p align="left"><a href="https://raw.githubusercontent.com/olliw42/mLRS-docu/main/logos/mLRS_logo_long_w_slogan_1280x768.png"><img src="https://raw.githubusercontent.com/olliw42/mLRS-docu/main/logos/mLRS_logo_long_w_slogan_1280x768.png" align="center" height="153" width="256" ></a>

# mLRS Flasher Desktop App #

Link to the [mLRS project](https://github.com/olliw42/mLRS).


## Installation ##

### Windows ###

mLRS-Flasher is based on Python, and thus needs a full Python3 installation on your system. Not very Win-like, we know, and we appologize for this. 

- Install Python3 on your system, if you haven't done so already. Make sure that Python is added to the PATH (***this is crucial!***).
     - ***Note***: Most Python installers include a check box to add Python to the path during installation; don't miss it.
- You need some additional Python packages, namely "pillow", "requests", "pyserial", "customtkinter", "tk", "pymavlink". Run this command to install them: `pip install pillow requests pyserial customtkinter tk pymavlink`.
- Download the mLRS-Flasher GitHub repository, and make sure to extract (unpack) it if you downloaded it as a zip file.
- Run the mLRS_Flasher.py script.
    - ***Note***: mLRS_Flasher needs the rights to write to disk and modify files on disk.
- Depending on your Python distribution, you may need to install additional packages. To determine which ones are missing, run the mLRS_Flasher.py script in the Windows cmd console and check the error messages; they will indicate which package is required. Install the missing package, then run the script again, until success.

### MacOS ###

#### Run the Flasher ####

````
./run_mLRS_Flasher_mac.sh
````

### Linux ###

TBD


## Disclaimer ##

You of course use the app fully at your own risk.


