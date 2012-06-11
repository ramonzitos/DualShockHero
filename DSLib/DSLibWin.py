import sys
import threading

if not sys.platform.startswith("win"):
    raise Exception("I really think that you want to use another library compatible\
    with your system ;)")

try:
    import pyHook
    import pygame
except ImportError:
    raise Exception("Please, install the pywin32, pyHook and pygame modules.")

class KeyCollection():
    def __init__(self, *args):
        self.keys = []
        self.keys_pressed = {}
        self.args = args
        pygame.init()
        for i in args:
            self.keys.append(ord(i.key))
            self.keys_pressed[ord(i.key)] = False
        self.hm = pyHook.HookManager()

    def OnKeyDown(self, event):
        if event.Ascii in self.keys:
            self.keys_pressed[event.Ascii] = True
        print "Key Down"
        # Authorizating another applications for managing the keyboard events.
        return True
    
    def OnKeyUp(self, event):
        if event.Ascii in self.keys:
            self.keys_pressed[event.Ascii] = False
        print "Key Up"
        return True
        
    def stop(self):
        print "Stop called."
        self.stopvar = True

    def wait_for_keypress(self, timing = None):
        self.hm.KeyDown = self.OnKeyDown
        self.hm.KeyUp = self.OnKeyUp
        self.hm.HookKeyboard()
        
        # Wait for first keypress.
        while not (True in self.keys_pressed.values()):
            pygame.event.pump()
        
        print "Pass"
        self.stopvar = False
        t = threading.Timer(0.1, self.stop)
        t.start()
        
        while not self.stopvar:
            pygame.event.pump()

        self.old_keys_pressed = self.keys_pressed.copy()
        if timing != None:
            pygame.event.pump()
            pygame.time.delay(timing)
            self.old_keys_pressed = self.keys_pressed.copy()
            print "Start while loop..."
            while not (self.old_keys_pressed != self.keys_pressed and True in self.keys_pressed.values()):
                self.old_keys_pressed = self.keys_pressed.copy()
                pygame.event.pump()
                pygame.time.delay(timing)
            print "End while loop..."

        self.hm.UnhookKeyboard()
        for i in self.args:
            self.keys_pressed[ord(i.key)] = False
        print self.old_keys_pressed
        return self.old_keys_pressed
        
class Key():
    def __init__(self, key, sendkeys_key = None):
        self.key = key
        self.sendkeys_key = sendkeys_key