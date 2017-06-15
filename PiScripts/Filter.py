#!/bin/python

# importeer de GPIO bibliotheek.
import RPi.GPIO as GPIO
# Importeer de time biblotheek voor tijdfuncties.
from time import sleep

# Zet waarschuwingen uit.
GPIO.setwarnings(False)

try:
    while True:
        # Zet het relais AAN.
        # Zet de pinmode op Broadcom SOC.
        GPIO.setmode(GPIO.BCM)
        # Zet de GPIO pin als uitgang.

        GPIO.setup(20, GPIO.OUT)
        GPIO.output(20, GPIO.LOW)
        # Wacht een seconde.
        sleep(30)

        # Zet het relais UIT.
        GPIO.cleanup()
        # Wacht een seconde.
        sleep(1)

except KeyboardInterrupt:
    # GPIO netjes afsluiten.
    GPIO.cleanup()