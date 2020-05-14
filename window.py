#!/usr/bin/env python3

import subprocess
from types import SimpleNamespace

def position():
	script = '''
	    tell application "System Events" to set frontApp to name of first application process whose frontmost is true
	    tell application frontApp to get the bounds of the front window
	'''

	output = subprocess.check_output(['osascript', '-e', script]).decode()
	bounds = output.replace('\n','').replace(' ','').split(",")

	return SimpleNamespace(**{
		"left": bounds[0],
		"top": bounds[1],
		"width": bounds[2],
		"height": bounds[3]
	})

def init():
	return SimpleNamespace(**{
		"current": position(),
		"old": position()
	})
