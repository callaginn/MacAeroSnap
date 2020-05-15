#!/usr/bin/env xcrun swift

import Foundation
import Cocoa

// Gets screen dimensions, mouse position, and releases mouse
let desktop = NSScreen.screens[0].frame
var mouse = NSEvent.mouseLocation
mouse.y = NSHeight(desktop) - mouse.y

let mouseUp = CGEvent.init(mouseEventSource:nil, mouseType:.leftMouseUp, mouseCursorPosition:mouse, mouseButton:.left)!

mouseUp.post(tap:.cghidEventTap)
