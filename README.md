# Aero Snap for Mac OS X
This python script adds AeroSnap functionality to macOS Sierra using python, bash, and applescripts. Unlike most macOS AeroSnap scripts, though, it uses the mouse when docking windows to the left, right, top, or bottom of the screen.

At the moment, MacAeroSnap must be launched manually.

### How it Works
- MacAeroSnap asks Applescript for the desktop size and foremost window position.
- Every 0.1 seconds, it records the Finder window position and checks it against the last recorded position. If it's different, it assumes the window is being dragged.
- If the window is being dragged, it calls Tkinter for the mouse position and checks to see if the mouse has crossed a border of the screen. If so, it fires AppleScript to dock the window to that side of the screen.

### Installation
1. Paste the following into your Terminal:<br>
`git clone https://github.com/callaginn/MacAeroSnap ~/bin/MacAeroSnap; ln -sf $_/macsnap.py ~/bin;`
2. Run the `install.sh` bash script. This will check, verify, and download the [MouseTools](http://hamsoftengineering.com) dependency and extract it automatically. This script is required for "releasing" the mouse.
3. Add the destination folder to your $PATH:<br>
`echo 'PATH="$PATH:$HOME/bin"' >> ~/.bash_profile; . ~/.bash_profile;`

### Start and Stop
Type `mouse.py` into the macOS Terminal and press enter. For debugging info, pass an additional verbose flag to the script: `mouse.py -v`. You can stop MacAeroSnap at any time by closing the Terminal.
