# Aero Snap for Mac OS X
This python script adds AeroSnap functionality to macOS Mojave using python3, bash, applescript, and swift. Unlike most macOS AeroSnap scripts, though, it uses the mouse when docking windows to the left, right, top, or bottom of the screen.

At the moment, MacAeroSnap must be launched manually.

### How it Works
- MacAeroSnap asks Applescript for the desktop size and foremost window position.
- Every 0.1 seconds, it records the Finder window position and checks it against the last recorded position. If it's different, it assumes the window is being dragged.
- If the window is being dragged, it calls Tkinter for the mouse position and checks to see if the mouse has crossed a border of the screen. If so, it fires AppleScript to dock the window to that side of the screen.
- Once the window is snapped, the mouse is immediately released with a bit of Swift magic.

### Installation
1. Paste the following into your Terminal:<br>
`git clone https://github.com/callaginn/MacAeroSnap ~/bin/MacAeroSnap; ln -sf $_/macsnap.py ~/bin;`
2. Add the destination folder to your $PATH:<br>
`echo 'PATH="$PATH:$HOME/bin"' >> ~/.bash_profile; . ~/.bash_profile;`

### Start and Stop
Type `macsnap.py` into the macOS Terminal and press enter. For debugging info, pass an additional verbose flag to the script: `macsnap.py -v`. You can stop MacAeroSnap at any time by closing the Terminal.
