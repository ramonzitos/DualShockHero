import SendKeys
import pygame
import threading

'''DSLib is used for manupulating keys(still not fully working) and joysticks(i think that works)'''

# I don't know if i will use this, but...
class Key():
    '''Initializes the key control.
    Please, use this as an example for 'key' argument:
    "space", "left", "a", "s", "tab", "alt"
    'sendkeys_key': ADVANCED, for certain keys, like RETURN, you need to use
    a special key, like {ENTER}. Search for the SendKeys Python module.'''
    def __init__(self, key, sendkeys_key = None):
        pygame.init()
        self.key = key
        self.sendkeys_key = sendkeys_key
    
    '''Press the key.
    WARNING: Untested, even if the program is dependent of that!!!'''
    def press(self):
        if self.sendkeys_key != None:
            SendKeys.SendKeys(self.sendkeys_key, pause=0, turn_off_numlock=False)
        else:
            SendKeys.SendKeys(self.key, pause=0, turn_off_numlock=False)
    
    '''Return the key name.'''
    def get_name(self):
        return self.key
    
    '''Return if the key is pressed.'''
    def is_pressed(self):
        return pygame.key.get_pressed()[self.key]
#       for i in pygame.event.get():
#           if i.type == pygame.KEYDOWN and i.key == self.key:
#               is_pressed = True
#           elif i.type == pygame.KEYUP and i.key == self.key:
#               is_pressed = False
#       return is_pressed
class Button():
    '''Initializes the button control.
    'button' argument: a integer that represent the button number
    'joystick' argument: a Joystick() from this same module, that represent the
    joystick button.'''
    def __init__(self, button, joystick):
        pygame.init()
#        if isinstance(joystick, Joystick):
#            raise TypeError, "Joystick must be a Joystick class!"
        self.joystick = joystick
        self.button = button
    
    '''Get the button number that you pass on initialize'''
    def get_name(self):
        return self.button
    
    '''Return if the button is pressed.'''
    def is_pressed(self):    
        return self.joystick.is_pressed(self)

class Joystick():
    '''Initializes the joystick control
    'order' argument: a Integer that represent the joystick order(1st, 2nd)'''
    def __init__(self, order):
        pygame.init()
        assert isinstance(order, int) == True
        if pygame.joystick.get_count() < order:
            raise Exception, "Hey, you don't have that number of joysticks."
        self.joystick = pygame.joystick.Joystick(order - 1)
        self.joystick.init()
    
    
    '''Return the joystick name.'''
    def get_name(self):
        return self.joystick.get_name()
    
    '''Return if a button is pressed
    'button' argument: the Button() that represent the button that you asked.'''
    def is_pressed(self, button):
        return self.joystick.get_button(button.get_name() - 1)
    
    '''Get the list of buttons that are pressed.
    'args': I really suppose that you will pass as argument buttons.'''    
    def get_buttons_pressed(self, *args):
        dictbtn = {}
        for _ in args:
                dictbtn[_.get_name()] = _.is_pressed()
        return dictbtn