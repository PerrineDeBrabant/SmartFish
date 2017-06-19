from PiScripts.LCD_scherm import InitLCD, Setup, SendString, heater
from PiScripts.temperatuur import Temp_sensor
from DbClass import DbClass
import time
import RPi.GPIO as GPIO

try:
    while True:

        Temp_sensor()
        db = DbClass()
        Setup()
        InitLCD()
        temperatuur = str(Temp_sensor().temp())
        SendString("Het is " + temperatuur + chr(223) + "C")
        Stand= db.getCurrent()
        print(Stand)
        db2=DbClass()
        Gewenst=db2.GewensteTemperatuur('Tropical')
        Gewenst=str(Gewenst)
        Gewenst=Gewenst.replace("(", "").replace(")", "").replace(",", "").replace("[", "").replace("]",                                                                                    "").replace(
                "'", "")
        Gewenst=float(Gewenst)
        print(Gewenst)
        if Stand == [(1,)]:
            if Temp_sensor().temp() >= (Gewenst+0.5):
                GPIO.output(heater, GPIO.HIGH)
                standheater=0
            #     Heater stand aanpassen naar 0

            else:
                print("Heater is aan")
                GPIO.output(heater, GPIO.LOW)
                standheater = 1
        #         Heater stand aanpassen naar 1
        else:
            if Temp_sensor().temp() <= Gewenst :
                print("Heater is aan")
                GPIO.output(heater, GPIO.LOW)
                standheater = 1
            else:
                print("Heater is uit")
                GPIO.output(heater, GPIO.HIGH)
                standheater = 0
        db3=DbClass()
        import datetime
        tijd=datetime.datetime.now()



        db3.VoegMetingToe(temperatuur,tijd,'1',standheater)
        time.sleep(60)


except KeyboardInterrupt():
    GPIO.cleanup()