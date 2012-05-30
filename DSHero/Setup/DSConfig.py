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
            self.scr = Screen((500, 100), "DSConfig")
        self.parser = ConfigParser.ConfigParser()
    
    def wait_for_joystick(self):
        for i in range(1, pygame.joystick.get_count()): # Joystick init.
            DSLib.Joystick(i)
        while True:
            e = pygame.event.wait()
            print "Event get! %r" % e.type
            if e.type == pygame.JOYBUTTONDOWN:
                print e.joy
                return DSLib.Joystick(e.joy + 1)
                break
            elif e.type == pygame.QUIT: pygame.quit(); sys.exit(0)
    
    def wait_for_button(self, joy):
        print "I'm waiting..."
        while True:
            e = pygame.event.wait()
            if e.type == pygame.JOYBUTTONDOWN and e.joy == joy.get_order() - 1:
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
        green = self.wait_for_button(joy)
        self.write("A good start! Now press a button for red fret.")
        red = self.wait_for_button(joy)
        self.write("Right! Now press a button for yellow fret.")
        yellow = self.wait_for_button(joy)
        self.write("Really good! Now press a button for blue fret.")
        blue = self.wait_for_button(joy)
        self.write("Almost finished! Now press a button for the orange fret.")
        orange = self.wait_for_button(joy)
        # Adding to config file.
        self.parser.add_section("Buttons")
        self.parser.set("Buttons", "joystick", str(joy.get_order()))
        self.parser.set("Buttons", "green", str(green.get_name()))
        self.parser.set("Buttons", "red", str(red.get_name()))
        self.parser.set("Buttons", "yellow", str(yellow.get_name()))
        self.parser.set("Buttons", "blue", str(blue.get_name()))
        self.parser.set("Buttons", "orange", str(orange.get_name()))
        with open("buttons.cfg", "w") as f:
            self.parser.write(f)
        e = pygame.event.wait()
        if e.type == pygame.QUIT: pygame.quit()

if __name__ == "__main__": DSConfig().main()