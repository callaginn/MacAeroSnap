# MacAeroSnap
This script adds AeroSnap functionality to macOS Sierra using python, bash, and applescripts. Unlike most AeroSnap bash scripts, this script uses the mouse to dock windows to the left, right, top, or bottom of the screen.

At the moment, this script must be launched manually.

### How it Works
- It grabs the desktop size and frontmost Finder window position by passing AppleScript into python.
- Every 0.1 seconds, it records the Finder window position and checks it against the last recorded position. If it's different on a pass, it assumes the window is being dragged.
- If the window is being dragged, it calls Tkinter for the mouse position and checks to see if the mouse has entered the left or right side of the screen. If it has hit a boundary, it fires the appropriate AppleScript, which docks the frontmost Finder window to that side of the screen.

### Installation
1. Paste the following into your Terminal:<br>
`git clone https://github.com/callaginn/MacAeroSnap ~/bin/MacAeroSnap; ln -sf $_/macsnap ~/bin;`
2. Run the `install.sh` bash script. This will check, verify, and download the [MouseTools](http://hamsoftengineering.com) dependency and extract it automatically. This script is required for "releasing" the mouse.
3. Add the destination folder to your $PATH:<br>
`echo 'PATH="$PATH:$HOME/bin"' >> ~/.bash_profile; . ~/.bash_profile;`

### Start and Stop
Type `mouse.py` into the macOS Terminal and press enter. For debugging info, pass an additional verbose flag to the script: `mouse.py -v`. You can stop this script at any time by closing the Terminal.
