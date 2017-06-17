# #! /usr/bin/env python
# import RPi.GPIO as GPIO
# import sys
# import time
#
# # RGB LED pinnen configureren.
# pinRood = 17
# pinGroen = 27
# pinBlauw = 22
#
# # GPIO setup.
# GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False)
#
# # Zet de GPIO pinnen als uitgang.
# GPIO.setup(pinRood, GPIO.OUT)
# GPIO.setup(pinGroen, GPIO.OUT)
# GPIO.setup(pinBlauw, GPIO.OUT)
#
# # Gebruik PWM op de pinnen.
# ROOD = GPIO.PWM(pinRood, 1000)
# GROEN = GPIO.PWM(pinGroen, 1000)
# BLAUW = GPIO.PWM(pinBlauw, 1000)
# ROOD.start(0)
# GROEN.start(0)
# BLAUW.start(0)
#
# if len(sys.argv) > 3:
#     # converteer de waarde 255 tot max 100 voor PWM.
#     roodwaarde = (int(sys.argv[1]) * 100) / 255
#     groenwaarde = (int(sys.argv[2]) * 100) / 255
#     blauwwaarde = (int(sys.argv[3]) * 100) / 255
#
#     ROOD.ChangeDutyCycle(roodwaarde)
#     GROEN.ChangeDutyCycle(groenwaarde)
#     BLAUW.ChangeDutyCycle(blauwwaarde)
#     time.sleep(3)
#     ROOD.stop()
#     GROEN.stop()
#     BLAUW.stop()
#
# GPIO.cleanup()

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

RED = 17
GREEN = 22
BLUE = 24

GPIO.setup(RED,GPIO.OUT)
GPIO.output(RED,255)
GPIO.setup(GREEN,GPIO.OUT)
GPIO.output(GREEN,255)
GPIO.setup(BLUE,GPIO.OUT)
GPIO.output(BLUE,255)

try:
    while (True):
            h = input('Enter hex: ').lstrip('#')
            rgb=tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))
            print(rgb)
            GPIO.output(RED,rgb[0])
            GPIO.output(GREEN,rgb[1])
            GPIO.output(BLUE,rgb[2])


except KeyboardInterrupt:
    GPIO.cleanup()

# h = input('Enter hex: ').lstrip('#')
# print('RGB =', tuple(int(h[i:i+2], 16) for i in (0, 2 ,4)))
# h = input('Enter hex: ').lstrip('#')
# bla=tuple(int(h[i:i+2], 16) for i in (0,2,4))
# print('RGB =', bla)
# print(bla[1])