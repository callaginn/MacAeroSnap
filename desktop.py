#!/usr/bin/env python3

from applescript import AppleScript as applescript
from types import SimpleNamespace

def position():
	script = 'tell application "Finder" to get bounds of window of desktop'
	dimensions = applescript(script).run()

	return SimpleNamespace(**{
		"left": dimensions[0],
		"top": dimensions[1],
		"width": dimensions[2],
		"height": dimensions[3]
	})

print(position())
