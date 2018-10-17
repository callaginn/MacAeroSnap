# MacAeroSnap
This script adds AeroSnap functionality to macOS Sierra using only bash and applescripts. Unlike most AeroSnap bash scripts, this script uses the mouse to dock windows to the left, right, top, or bottom of the screen.

### How it Works

1. It grabs the desktop size and frontmost Finder window position by passing AppleScript into bash.
2. Every 0.1 seconds, it records the Finder window position and checks it against the last recorded position. If it's different on a pass, it assumes the window is being dragged.
3. If the window is being dragged, it calls MouseTools for the mouse position and checks to see if the mouse has entered the left or right side of the screen. And if it has hit a boundary, it fires the appropriate AppleScript, which docks the frontmost Finder window to that side of the screen.

### Installation
Paste the following into your Terminal:<br>
`git clone https://github.com/callaginn/MacAeroSnap ~/bin/MacAeroSnap; ln -sf $_/macsnap ~/bin;`

Make sure the destination folder has been added to your $PATH. If not, you can load it via this command:<br>
`echo 'PATH="$PATH:$HOME/bin"' >> ~/.bash_profile; . ~/.bash_profile;`

> *The only external tool this requires is [MouseTools](http://hamsoftengineering.com). Running macsnap for the first time will download it, verify the zip file's MD5 hash, and extract it automatically.*

### Start and Stop

This must be run manually by pasting `macsnap` into the Terminal. You can stop it at any time by closing the Terminal.
