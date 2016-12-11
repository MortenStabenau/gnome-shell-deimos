#!/usr/bin/python
# Display a notification with two buttons. Used this to test what notifications
# look like
from gi.repository import Notify

def f():
    pass

Notify.init("App Name")
n = Notify.Notification.new("Notification Text")
n.set_urgency(2)
n.add_action("action_click", "Button Text 1", f)
n.add_action("action_click2", "Button Text 2", f)
n.show()
