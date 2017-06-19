
from DbClass import DbClass
import time
import RPi.GPIO as GPIO

from PiScripts.Filter import AanzettenFilter, UitzettenFilter, SetupFilter


try:
    while True:
        SetupFilter()
        db=DbClass()
        standFilter=db.standFilter('Tropical')
        if standFilter==[(1,)]:
            AanzettenFilter()
        else:
            UitzettenFilter()

        GPIO.setmode(GPIO.BCM)
        RED = 17
        GREEN = 24
        BLUE = 22
        GPIO.setup(RED, GPIO.OUT)
        GPIO.setup(GREEN, GPIO.OUT)
        GPIO.setup(BLUE, GPIO.OUT)
        db2=DbClass()
        hexwaarde=db2.HuidigeKleur('Tropical')
        hexwaarde=str(hexwaarde)
        hexwaarde = hexwaarde.replace("(", "").replace(")", "").replace(",", "").replace("[", "").replace("]",
                                                                                                          "").replace(
            "'", "")
        db3 = DbClass()
        standVerlichting = db3.standVerlichting('Tropical')
        print(standVerlichting)
        if standVerlichting ==[(1,)]:

            h = hexwaarde.lstrip('#')
            rgb = tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))
            print(rgb)
            GPIO.output(RED, rgb[0])
            GPIO.output(GREEN, rgb[1])
            GPIO.output(BLUE, rgb[2])
            time.sleep(1)
        else:
            nulwaarde='#000000'
            h = nulwaarde.lstrip('#')
            rgb = tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))
            print(rgb)
            GPIO.output(RED, rgb[0])
            GPIO.output(GREEN, rgb[1])
            GPIO.output(BLUE, rgb[2])
            time.sleep(1)



except KeyboardInterrupt():
    GPIO.cleanup()