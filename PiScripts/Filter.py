

#!/bin/python

# importeer de GPIO bibliotheek.
import RPi.GPIO as GPIO
# Importeer de time biblotheek voor tijdfuncties.
from time import sleep
def SetupFilter():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(20, GPIO.OUT)

def AanzettenFilter():
    sleep(1)
    GPIO.output(20, GPIO.LOW)


def UitzettenFilter():
    sleep(1)
    GPIO.output(20, GPIO.HIGH)



#
# try:
#     while True:
#         # Zet het relais AAN.
#         # Zet de pinmode op Broadcom SOC.
#         GPIO.setmode(GPIO.BCM)
#         # Zet de GPIO pin als uitgang.
#
#         GPIO.setup(20, GPIO.OUT)
#         GPIO.output(20, GPIO.LOW)
#         # Wacht een seconde.
#         sleep(30)
#
#         # Zet het relais UIT.
#
#         # Wacht een seconde.
#         sleep(1)
#
# except KeyboardInterrupt:
#     # GPIO netjes afsluiten.
#     GPIO.cleanup()