DualShockHero
=============

DSHero is a program for playing GH-like(FOF, Phase Shift, GH3/4) programs with a joystick, or, like the name says, with a joystick.

==========
How to use
==========

1º. (optional) If you want to use the keyboard, set up it with a virtual joystick emulator(PPJoy, vJoy).

2º. Be sure that you have installed:
 - Python 2.7 (http://www.python.org/)
 - pygame module (http://www.pygame.org)
 - SendKeys module (http://www.rutherfurd.net/python/sendkeys/)

3º. Open the DSHero/__init__.py and edit the variables:
 - joystick: set the value to DSLib.Joystick(number), where number is the order of your joystick -- see on Control Panel > Game Controllers(I don't know how it's called, I don't have the English version of Windows XP).
 - green/red/yellow/blue/orange: set to DSLib.Button(number), where number is the number of the button(again, see at Game Controllers).
 - strum: set to the key which you use to strum(recommended: maintain the ENTER key, and set this on the game)

4º. Open the program!
