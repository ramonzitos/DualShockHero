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
import time
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
time_window = 20
timing_repress = 20

def init():
    pygame.init()
    pygame.display.init()
    pygame.joystick.init()
    
def create_screen(size, title):
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(title)
    return screen

def handleExitEvent():
    pygame.quit()
    sys.exit(0)

def handleJoyEvent(joystick, *args):
    global time_window
    global timing_repress
    old_dict_buttons = {}
    dict_buttons = joystick.get_buttons_pressed(*args)
    time.sleep(float(time_window)/1000.0)
    print "handleJoyEvent: Starting loop."
    while not (old_dict_buttons == dict_buttons):
        old_dict_buttons = dict_buttons
        time.sleep(float(timing_repress)/1000.0)
        dict_buttons = joystick.get_buttons_pressed(*args)
    print "handleJoyEvent: Ending loop."
    args[-1].press()
    return old_dict_buttons

def main(joystick, green, red, yellow, blue, orange, strum):
    init()
    scr = Screen((400, 300), "IGNORE ME")
    white = pygame.color.Color("white")
    black = pygame.color.Color("black")
    font48 = pygame.font.Font("freesansbold.ttf", 48)
    font9 = pygame.font.Font("freesansbold.ttf", 9)
    font12 = pygame.font.Font("freesansbold.ttf", 12)
    while True:
        pygame.event.pump()
        pygame.event.clear()
        e = pygame.event.wait()
        if e.type == pygame.QUIT: handleExitEvent()
        elif e.type == pygame.JOYBUTTONDOWN:
            print "Starting handleJoyEvent"
            handleJoyEvent(joystick, green, red, yellow, blue, orange, strum)
            print "Ending."
        scr.screen.fill(black)
        scr.write_text((100, 0), "Go play!", font48, white)
        scr.write_text((25, 72), "If you want to exit, press ALT-F4 or click the X Button", font12, white)
        scr.flip()

if __name__ == "__main__": main(joystick, green, red, yellow, blue, orange, strum)
        