#!/usr/bin/env python3

from applescript import AppleScript as applescript
from types import SimpleNamespace

def position():
	script = '''
	    tell application "System Events" to set frontApp to name of first application process whose frontmost is true
	    tell application frontApp to get the bounds of the front window
	'''

	bounds = applescript(script).run()

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
