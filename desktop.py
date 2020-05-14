#!/usr/bin/env python3

import subprocess
from types import SimpleNamespace

def position():
	script = 'tell application "Finder" to get bounds of window of desktop'
	output = subprocess.check_output(['osascript', '-e', script]).decode()
	dimensions = output.replace('\n','').replace(' ','').split(",")

	return SimpleNamespace(**{
		"left": dimensions[0],
		"top": dimensions[1],
		"width": dimensions[2],
		"height": dimensions[3]
	})
