#!/usr/bin/env python

# Get the current mouse position.

import logging
import sys
import Tkinter
import threading
import subprocess

def windowposition():
    script = '''
        tell application "System Events" to set frontApp to name of first application process whose frontmost is true
        tell application frontApp to get the bounds of the front window
    '''

    xy = subprocess.check_output(['osascript', '-e', script]).replace('\n','').replace(' ','').split(",")
    return xy

def mouseposition():
    # Returns the current position of the mouse as a dictionary object
    p = Tkinter.Tk()
    x, y = p.winfo_pointerxy()
    cursor = {'x': x, 'y': y}
    return cursor

def snap(direction):
    switcher = {
        "left":
            '''
            --- get Dock height
            tell application "System Events" to tell process "Dock"
                set dock_dimensions to size in list 1
                set dock_height to item 2 of dock_dimensions
            end tell
            --- get the new width and height for the window
            tell application "Finder"
                set desktop_dimensions to bounds of window of desktop
                set new_width to (item 3 of desktop_dimensions) / 2
                set new_height to (item 4 of desktop_dimensions) - dock_height
            end tell
            --- get active window
            tell application "System Events"
                set frontApp to name of first application process whose frontmost is true
            end tell
            --- resize window
            tell application frontApp
                activate
                set bounds of window 1 to {0, 0, new_width, new_height}
            end tell
            '''
        ,
        "right":
            '''
            --- get Dock height
            tell application "System Events" to tell process "Dock"
                set dock_dimensions to size in list 1
                set dock_height to item 2 of dock_dimensions
            end tell
            --- get the new width and height for the window
            tell application "Finder"
                set desktop_dimensions to bounds of window of desktop
                set new_width to (item 3 of desktop_dimensions) / 2
                set new_height to (item 4 of desktop_dimensions) - dock_height
            end tell
            --- get active window
            tell application "System Events"
                set frontApp to name of first application process whose frontmost is true
            end tell
            --- resize window
            tell application frontApp
                activate
                set bounds of window 1 to {new_width, 0, new_width * 2 + 4, new_height}
            end tell
            '''
        ,
        "top":
            '''
            --- get Dock height
            tell application "System Events" to tell process "Dock"
            	set dock_dimensions to size in list 1
            	set dock_height to item 2 of dock_dimensions
            end tell
            --- get the new width and height for the window
            tell application "Finder"
            	set desktop_dimensions to bounds of window of desktop
            	set new_width to (item 3 of desktop_dimensions)
                set new_height to ((item 4 of desktop_dimensions) - dock_height) / 2
            end tell
            --- get active window
            tell application "System Events"
            	set frontApp to name of first application process whose frontmost is true
            end tell
            --- resize window
            tell application frontApp
            	activate
            	set bounds of window 1 to {0, 0, new_width, new_height}
            end tell
            '''
        ,
        "bottom":
            '''
            --- get Dock height
            tell application "System Events" to tell process "Dock"
            	set dock_dimensions to size in list 1
            	set dock_height to item 2 of dock_dimensions
            end tell
            --- get the new width and height for the window
            tell application "Finder"
            	set desktop_dimensions to bounds of window of desktop
            	set new_width to (item 3 of desktop_dimensions)
            	set new_height to ((item 4 of desktop_dimensions) - dock_height) / 2
            end tell
            --- get active window
            tell application "System Events"
            	set frontApp to name of first application process whose frontmost is true
            end tell
            --- resize window
            tell application frontApp
            	activate
            	set bounds of window 1 to {0, new_height, new_width, new_height * 2}
            end tell
            '''
        ,
    }

    subprocess.check_output('MouseTools -releaseMouse', shell=True)
    script = switcher.get(direction)
    subprocess.check_output(['osascript', '-e', script])


def main():
    threading.Timer(0.25, main).start() # called every half second

    hitsize = 10
    cursor = mouseposition()
    mouse_x = cursor["x"]
    mouse_y = cursor["y"]

    # Get position of top app window
    xy = windowposition()
    x = xy[0]
    y = xy[1]

    # If I'm correct, values should be sometimes different:
    global old_x
    global old_y
    print "WINDOW POSITION"
    print "OLD: " + old_x + ',' + old_y
    print "NEW: " + x + ',' + y
    print "---------------"

    # See if window position has changed
    if x != old_x or y != old_y:
        print "window moved."

        # Check to see if cursor hits left, right, top, or bottom borders
        if mouse_x <= hitsize:
            snap("left")

        if mouse_x >= int(screen_width) - int(hitsize):
            snap("right")

        if mouse_y <= int(23) + int(hitsize):
            snap("top")

        if mouse_y >= int(screen_height) - int(hitsize):
            snap("bottom")

    # Save old position of top app window
    old_x = x
    old_y = y

# Grab Desktop Size and Position of Top App Window
script = 'tell application "Finder" to get bounds of window of desktop'
dimensions = subprocess.check_output(['osascript', '-e', script]).replace('\n','').replace(' ','').split(",")
screen_width = dimensions[2]
screen_height = dimensions[3]

# Grab initial position of top window
xy = windowposition()
x = xy[0]
y = xy[1]
old_x = x
old_y = y

# Start main loop
main()
