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

# Use this if you want to use a joystick:
joystick = DSLib.Joystick(2)

green = DSLib.Button(2, joystick)
red = DSLib.Button(3, joystick)
yellow = DSLib.Button(4, joystick)
blue = DSLib.Button(5, joystick)
orange = DSLib.Button(6, joystick)
strum = DSLib.Key(pygame.K_RETURN, "{ENTER}")

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

def handleJoyEvent(old_dict_buttons, joystick, *args):
    global time_window
    global timing_repress
    dict_buttons = joystick.get_buttons_pressed(*args)
    while not (old_dict_buttons == dict_buttons):
        dict_buttons = joystick.get_buttons_pressed(*args)
        old_dict_buttons = dict_buttons
        pygame.time.delay(timing_repress)
    args[-1].press()
    return old_dict_buttons

def main(joystick, green, red, yellow, blue, orange, strum):
    old_dict_buttons = {green.get_name(): False, red.get_name(): False,
                        yellow.get_name(): False, blue.get_name(): False,
                        orange.get_name(): False}
    
    init()
    screen = create_screen((400, 300), "IGNORE ME")
    while True:
        e = pygame.event.wait()
        if e.type == pygame.QUIT: handleExitEvent()
        elif e.type == pygame.JOYBUTTONDOWN:
            old_dict_buttons = handleJoyEvent(old_dict_buttons, joystick, green, red, yellow, blue, orange, strum)
        screen.fill(pygame.color.Color("black"))
        font48 = pygame.font.Font("freesansbold.ttf", 48)
        font9 = pygame.font.Font("freesansbold.ttf", 9)
        font12 = pygame.font.Font("freesansbold.ttf", 12)
        screen.blit(font48.render("Go play!", True, [255, 255, 255]), (100, 0))
        screen.blit(font12.render("If you want to exit, press ALT-F4 or click the X Button", True, [255, 255, 255]), (50, 72))
#        screen.blit()
        pygame.display.flip()

if __name__ == "__main__": main(joystick, green, red, yellow, blue, orange, strum)
        