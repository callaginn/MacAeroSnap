#!/usr/bin/env xcrun swift

import Cocoa
import Foundation

func printInfo(_ value: Any) {
    let t = type(of: value)
    print("'\(value)' of type '\(t)'")
}

var frame = NSScreen.screens[0].frame

var screen = [
	"width": String(format: "%.0f", frame.width),
	"height": String(format: "%.0f", frame.height)
]

print(screen)
print(screen["width"]!, screen["height"]!)
