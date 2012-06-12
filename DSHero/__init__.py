#    Copyright (C) 2012  Ramon Dantas
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License along
#    with this program; if not, write to the Free Software Foundation, Inc.,
#    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

import DSLib
import pygame
import sys
import ConfigParser
from PyGameWinLib import Screen

# ConfigParser setted on DSConfig.exe
parser = ConfigParser.ConfigParser()
if len(parser.read(["buttons.cfg"])) == 0:
    raise Exception, "Can't read the config file."

# Use this if you want to use a joystick:
joystick = DSLib.Joystick(parser.getint("Buttons", "joystick"))

# Button definition
green = DSLib.Button(parser.getint("Buttons", "green"), joystick)
red = DSLib.Button(parser.getint("Buttons", "red"), joystick)
yellow = DSLib.Button(parser.getint("Buttons", "yellow"), joystick)
blue = DSLib.Button(parser.getint("Buttons", "blue"), joystick)
orange = DSLib.Button(parser.getint("Buttons", "orange"), joystick)
strum = DSLib.Key(pygame.K_RETURN, "{ENTER}")

class DSHero():
    def __init__(self, joystick, green, red, yellow, blue, orange, strum, parser):
        pygame.init()
        pygame.display.init()
        pygame.joystick.init()
        self.joystick = joystick
        self.green = green
        self.red = red
        self.yellow = yellow
        self.blue = blue
        self.orange = orange
        self.strum = strum
        self.parser = parser
        self.time_window = 5
        self.time_repress = 5
    
    '''Exit the program.'''
    def handleExitEvent(self):
        pygame.quit()
        sys.exit(0)

    def handleJoyEvent(self):
        args = [self.green, self.red, self.yellow, self.blue, self.orange]
        old_dict_buttons = joystick.get_buttons_pressed(*args)
        pygame.time.delay(self.time_window)
        dict_buttons = joystick.get_buttons_pressed(*args)
        reruns = 0
        i = 0
        for k, v in dict_buttons.iteritems():
            if old_dict_buttons[k] != v: reruns += 1
        while not (i == reruns):
            old_dict_buttons = dict_buttons
            pygame.time.delay(self.time_repress)
            dict_buttons = joystick.get_buttons_pressed(*args)
            for k, v in dict_buttons.iteritems():
                if old_dict_buttons[k] != v: reruns += 1
            i += 1
        self.strum.press()

    def main(self):
        
        scr = Screen((400, 300), "IGNORE ME")
        white = pygame.color.Color("white")
        black = pygame.color.Color("black")
        orange = pygame.color.Color("orange")
        font48 = pygame.font.Font("freesansbold.ttf", 48)
        font12 = pygame.font.Font("freesansbold.ttf", 12)
        font16 = pygame.font.Font("freesansbold.ttf", 16)
        
        menu_position = 0
        menu_items = {"Time for first press:": self.time_window, "Time for repress:": self.time_repress}
        while True:
            scr.fill(black)
            scr.write_text((100, 0), "Go play!", font48, white)
            scr.write_text((25, 72), "If you want to exit, press ALT-F4 or click the X Button", font12, white)
            i = 82
            for k, v in self.parser.items("Buttons"):
                i += 13
                if k == "joystick": scr.write_text((10, i), "Joystick: (%d) %s" % (self.joystick.get_order(), self.joystick.get_name()),
                                                   font12, white)
                else: scr.write_text((10, i), "%s button: %s" % (k.capitalize(), v),
                                     font12, white)
            
            i += 20
            for k, v in menu_items.iteritems():
                i += 16
                if menu_items.keys()[menu_position] == k:
                    scr.write_text((10, i), "%s < %d >" % (k, v), font16, orange)
                else:
                    scr.write_text((10, i), "%s < %d >" % (k, v), font16, white)
            scr.flip()
            pygame.event.pump()
            pygame.event.clear()
            while True:
                e = pygame.event.wait()
                if e.type in [pygame.QUIT, pygame.JOYBUTTONDOWN, pygame.KEYDOWN]:
                    break
            
            # Event manegament
            if e.type == pygame.QUIT: self.handleExitEvent()
            elif e.type == pygame.JOYBUTTONDOWN and DSLib.Button(e.button + 1, joystick) in [self.green, self.red, self.yellow,
                                                                                             self.blue, self.orange]:
                self.handleJoyEvent()
            elif e.type == pygame.KEYDOWN and e.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
                if e.key == pygame.K_UP and menu_position > 0: menu_position -= 1
                elif e.key == pygame.K_DOWN and menu_position < 1: menu_position += 1
                elif e.key == pygame.K_LEFT:
                    if menu_items.values()[menu_position] > 0:
                        menu_items[menu_items.keys()[menu_position]] -= 1
                        if menu_position == 0: self.time_window -= 1
                        elif menu_position == 1: self.time_repress -= 1
                elif e.key == pygame.K_RIGHT:
                    menu_items[menu_items.keys()[menu_position]] += 1
                    if menu_position == 0: self.time_window += 1
                    elif menu_position == 1: self.time_repress += 1
if __name__ == "__main__":
    dshero = DSHero(joystick, green, red, yellow, blue, orange, strum, parser)
    dshero.main()
        