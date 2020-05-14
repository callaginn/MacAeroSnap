#!/usr/bin/env python3

# MacAeroSnap
# This script adds aerosnap-like window-snapping to macOS Mojave using
# python3, tkinter, bash, and applescript.

import sys, threading, window, desktop, mouse, snap

# Print Debugging Info if a (-v) flag is passed
debug = False

if len(sys.argv) > 1 and sys.argv[1] == "-v":
	debug = True

def main():
	threading.Timer(0.1, main).start() # called every tenth of a second

	hitsize = 10
	cursor = mouse.position()

	# Grab New Top Window Bounds
	position.current = window.position()

	if debug:
		print({
			"current": vars(position.current),
			"old": vars(position.old)
		})

	# If window moves, check to see if cursor hit a boundary
	if position.current.left != position.old.left or position.current.top != position.old.top:
		if debug: print("window moved")

		if cursor.left <= hitsize:
			mouse.release()
			snap.left()

		if cursor.left >= int(screen.width) - int(hitsize):
			mouse.release()
			snap.right()

		if cursor.top <= int(23) + int(hitsize):
			mouse.release()
			snap.top()

		if cursor.top >= int(screen.height) - int(hitsize):
			mouse.release()
			snap.bottom()

	# Save old position of top app window
	position.old = position.current

# Grab Desktop and Initial Top Window Bounds
screen = desktop.position()
position = window.init()

# Start Main Loop
main()
