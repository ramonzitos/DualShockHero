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

# Timing window(set at your preference).
time_window = 10
timing_repress = 10
class DSHero():
    def __init__(self, joystick, green, red, yellow, blue, orange, strum):
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

    def handleExitEvent(self):
        pygame.quit()
        sys.exit(0)

    def handleJoyEvent(self):
        global time_window
        global timing_repress
        args = [self.green, self.red, self.yellow, self.blue, self.orange]
        old_dict_buttons = joystick.get_buttons_pressed(*args)
        pygame.time.delay(time_window)
        dict_buttons = joystick.get_buttons_pressed(*args)
        while not (old_dict_buttons == dict_buttons):
            old_dict_buttons = dict_buttons
            pygame.time.delay(timing_repress)
            dict_buttons = joystick.get_buttons_pressed(*args)
        self.strum.press()

    def main(self):
        scr = Screen((400, 300), "IGNORE ME")
        white = pygame.color.Color("white")
        black = pygame.color.Color("black")
        font48 = pygame.font.Font("freesansbold.ttf", 48)
        font9 = pygame.font.Font("freesansbold.ttf", 9)
        font12 = pygame.font.Font("freesansbold.ttf", 12)
        while True:
            scr.fill(black)
            scr.write_text((100, 0), "Go play!", font48, white)
            scr.write_text((25, 72), "If you want to exit, press ALT-F4 or click the X Button", font12, white)
            scr.flip()
            pygame.event.pump()
            pygame.event.clear()
            e = pygame.event.wait()
            if e.type == pygame.QUIT: self.handleExitEvent()
            elif e.type == pygame.JOYBUTTONDOWN and DSLib.Button(e.button + 1, joystick) in [green, red, yellow, blue, orange]:
                self.handleJoyEvent()   


if __name__ == "__main__":
    dshero = DSHero(joystick, green, red, yellow, blue, orange, strum)
    dshero.main()
        