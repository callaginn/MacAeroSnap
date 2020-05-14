#!/usr/bin/env python3

import tkinter, subprocess
from types import SimpleNamespace

# Get Mouse Coordinates Silently
def position():
	x, y = tkinter.Tk().winfo_pointerxy()

	return SimpleNamespace(**{
		"left": x,
		"top": y
	})

def release():
	subprocess.check_output('MouseTools -releaseMouse', shell=True)
