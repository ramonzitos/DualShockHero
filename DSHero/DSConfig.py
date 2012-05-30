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
import ConfigParser
import sys
from PyGameWinLib import Screen

class DSConfig():
    def __init__(self, lib_mode = False):
        pygame.init()
        pygame.joystick.init()
        pygame.display.init()
        self.lib_mode = lib_mode
        self.black = pygame.color.Color("black")
        self.white = pygame.color.Color("white")
        self.font = pygame.font.Font("freesansbold.ttf", 16)
        if not lib_mode:
            self.scr = Screen((700, 50), "DSConfig")
        self.parser = ConfigParser.ConfigParser()
    
    
    '''Wait for a button press in a joystick, and return the joystick.'''
    def wait_for_joystick(self):
        for i in range(1, pygame.joystick.get_count()): # Joystick init.
            DSLib.Joystick(i)
        while True:
            e = pygame.event.wait()
            if e.type == pygame.JOYBUTTONDOWN:
                print e.joy
                return DSLib.Joystick(e.joy + 1)
            elif e.type == pygame.QUIT: pygame.quit(); sys.exit(0)
    
    '''Wait for a button press and return this button.
    'joy' argument: The Joystick that you want to capture the button.
    'buttons' argument: (optional) The list of Buttons that you want to exclude.'''
    def wait_for_button(self, joy, buttons = []):
        btnnumbers = []
        for i in buttons:
            btnnumbers.append(i.get_name())
        while True:
            e = pygame.event.wait()
            if e.type == pygame.JOYBUTTONDOWN and e.joy == joy.get_order() - 1 and (e.button + 1) not in btnnumbers:
                return DSLib.Button(e.button + 1, joy)
            elif e.type == pygame.QUIT: pygame.quit(); sys.exit(0)

    def write(self, text):
        self.scr.fill(self.black)
        self.scr.write_text((0,0), text, self.font, self.white)
        self.scr.flip()
    
    def main(self):
        self.write("Let's start: press a button on your joystick")
        joy = self.wait_for_joystick()
        self.write("Okay. Now press a button for green fret.")
        buttons = []
        buttons.append(self.wait_for_button(joy, buttons))
        self.write("A good start! Now press a button for red fret.")
        buttons.append(self.wait_for_button(joy, buttons))
        self.write("Right! Now press a button for yellow fret.")
        buttons.append(self.wait_for_button(joy, buttons))
        self.write("Really good! Now press a button for blue fret.")
        buttons.append(self.wait_for_button(joy, buttons))
        self.write("Almost finished! Now press a button for the orange fret.")
        buttons.append(self.wait_for_button(joy, buttons))
        # Adding to config file.
        self.parser.add_section("Buttons")
        self.parser.set("Buttons", "joystick", str(joy.get_order()))
        self.parser.set("Buttons", "green", str(buttons[0].get_name()))
        self.parser.set("Buttons", "red", str(buttons[1].get_name()))
        self.parser.set("Buttons", "yellow", str(buttons[2].get_name()))
        self.parser.set("Buttons", "blue", str(buttons[3].get_name()))
        self.parser.set("Buttons", "orange", str(buttons[4].get_name()))
        with open("buttons.cfg", "w") as f:
            self.parser.write(f)
        while True:
            pygame.time.delay(1000/50)
            self.write("Finished! Now, at game, set ENTER as the pick and buttons on frets.")
            e = pygame.event.wait()
            if e.type == pygame.QUIT: pygame.quit()

if __name__ == "__main__": DSConfig().main()