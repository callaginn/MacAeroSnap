#!/usr/bin/env python3

# MacAeroSnap
# This script adds aerosnap-like window-snapping to macOS Mojave using
# python3, tkinter, bash, and applescript.
# Print Debugging Info if a (-v) flag is passed

import sys, threading, window, desktop, mouse, snap

hitsize = 20
debug = False

if len(sys.argv) > 1 and sys.argv[1] == "-v":
	debug = True

def main():
	# Repeat every tenth of a second
	threading.Timer(0.1, main).start()

	# Grab New Top Window Bounds
	position.current = window.position()

	# If window moves, check to see if cursor hit a boundary
	if position.current.left != position.old.left or position.current.top != position.old.top:
		cursor = mouse.position()

		if debug:
			print("window is moving")
			print(cursor.left)
			# print({"current": position.current.left, "old": position.old.left})

		if cursor.left <= int(hitsize):
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
