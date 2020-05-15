#!/usr/bin/env xcrun swift

// returns title of active window

import Foundation
import Cocoa

class activeApp: NSObject {
    override init() {
    super.init()
    NSWorkspace.shared.notificationCenter.addObserver(self,
        selector: #selector(printMe(notification:)),
        name: NSWorkspace.didActivateApplicationNotification,
        object:nil)
    }
    @objc func printMe(notification: NSNotification) {
        let app = notification.userInfo!["NSWorkspaceApplicationKey"] as! NSRunningApplication
		print(app)
        print(app.localizedName!)
    }
}

let runme = activeApp()
RunLoop.main.run()
