import DSLib
import pygame
import sys

# Use this if you want to use a joystick:
joystick = DSLib.Joystick(2)

#shit = DSLib.Button(6, joystick)
red = DSLib.Button(3, joystick)
green = DSLib.Button(2, joystick)
yellow = DSLib.Button(4, joystick)
blue = DSLib.Button(5, joystick)
orange = DSLib.Button(6, joystick)
#green = DSLib.Key(pygame.K_a, "a")
#red = DSLib.Key(pygame.K_s, "s")
#yellow = DSLib.Key(pygame.K_j, "j")
#blue = DSLib.Key(pygame.K_k, "k")
#orange = DSLib.Key(pygame.K_l, "l")
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
    button_pressed = False
    dict_buttons = joystick.get_buttons_pressed(*args)
    for k, v in dict_buttons.iteritems():
        if v == True and old_dict_buttons[k] != v: button_pressed = True
    if old_dict_buttons != dict_buttons:
        old_dict_buttons = dict_buttons
        if button_pressed:
            pygame.time.delay(time_window)
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
        elif e.type == pygame.JOYBUTTONDOWN or e.type == pygame.JOYBUTTONUP:
            old_dict_buttons = handleJoyEvent(old_dict_buttons, joystick, green, red, yellow, blue, orange, strum)
        screen.fill(pygame.color.Color("black"))
        font72 = pygame.font.Font(None, 72)
        font16 = pygame.font.Font(None, 16)
        font20 = pygame.font.Font(None, 20)
        screen.blit(font72.render("Go play!", True, [255, 255, 255]), (100, 0))
        screen.blit(font16.render("If you want to exit, press ALT-F4 or click the X Button", True, [255, 255, 255]), (50, 72))
#        screen.blit()
        pygame.display.flip()

if __name__ == "__main__": main(joystick, green, red, yellow, blue, orange, strum)
        