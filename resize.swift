#!/usr/bin/env xcrun swift

// This script resizes a Terminal Window

import Cocoa
import Foundation

let type = CGWindowListOption.optionOnScreenOnly
let windowList = CGWindowListCopyWindowInfo(type, kCGNullWindowID) as NSArray? as? [[String: AnyObject]]

print(windowList!)

for entry in windowList! {
	let owner = entry[kCGWindowOwnerName as String] as! String
	var bounds = entry[kCGWindowBounds as String] as? [String: Int]
	let pid = entry[kCGWindowOwnerPID as String] as? Int32

	if owner == "Terminal" {
		let appRef = AXUIElementCreateApplication(pid!);  //TopLevel Accessability Object of PID

		var value: AnyObject?
		let result = AXUIElementCopyAttributeValue(appRef, kAXWindowsAttribute as CFString, &value)

		if let windowList = value as? [AXUIElement] {
			print ("windowList #\(windowList)")

			if let window = windowList.first {
				var position : CFTypeRef
				var size : CFTypeRef
				var  newPoint = CGPoint(x: 0, y: 0)
				var newSize = CGSize(width: 800, height: 800)

				position = AXValueCreate(AXValueType(rawValue: kAXValueCGPointType)!,&newPoint)!;
				AXUIElementSetAttributeValue(windowList.first!, kAXPositionAttribute as CFString, position);

				size = AXValueCreate(AXValueType(rawValue: kAXValueCGSizeType)!,&newSize)!;
				AXUIElementSetAttributeValue(windowList.first!, kAXSizeAttribute as CFString, size);
			}
		}
	}
}
