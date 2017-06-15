import RPi.GPIO as GPIO
import time

# -*- coding: uft-8 -*-
from PiScripts.temperatuur import Temp_sensor

RS = 16
E = 12
DB4 = 25
DB5 = 23
DB6 = 18
DB7 = 5
pinData = [25,23,18,5]
heater= 21



# def print_start():
#     print('Program is running...')

def Setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(RS, GPIO.OUT)
    GPIO.setup(E, GPIO.OUT)
    GPIO.setup(DB4, GPIO.OUT)
    GPIO.setup(DB5, GPIO.OUT)
    GPIO.setup(DB6, GPIO.OUT)
    GPIO.setup(DB7, GPIO.OUT)
    GPIO.setup(21, GPIO.OUT)

def SetData(byte):
    MSB = byte >> 4
    LSB = byte & 0x0f
    for i in range(0,4):
        GPIO.output(pinData[i], MSB & 1 << i)
    GPIO.output(E, False)
    time.sleep(0.001)
    GPIO.output(E, True)
    for i in range(0, 4):
        GPIO.output(pinData[i], LSB & 1 << i)

def Instuctie(byte):
    GPIO.output(E, True)
    GPIO.output(RS,False)
    SetData(byte)
    GPIO.output(E, False)
    time.sleep(0.01)

def Teken(char):
    GPIO.output(E, True)
    GPIO.output(RS, True)
    SetData(ord(char))
    GPIO.output(E, False)
    time.sleep(0.01)

def SendString(string):
    deel1 = string[0:16]
    deel2 = string[18:31]

    if (len(string) > 16):
        for letter in enumerate(deel1):
            Teken(letter[1])
            print("Deel 1: " + letter[1])

        for letter in enumerate(deel2):
            Teken(letter[1])
            print("Deel 2: " + letter[1])

    else:
        for letter in enumerate(string):
            Teken(letter[1])


def InitLCD():
    Instuctie(0x3)

    Instuctie(0x2)
    Instuctie(0x28)
    Instuctie(0xc)
    Instuctie(0x1)


GPIO.cleanup()

try:
    while True:
        Setup()
        InitLCD()

        temperatuur = str(Temp_sensor().temp())
        SendString("Het is " + temperatuur + chr(223) + "C")

        time.sleep(10)

        if Temp_sensor().temp() <= 26.0:
            print("Heater is aan")
            GPIO.output(heater, GPIO.LOW)
            time.sleep(30)
        else:
            print("Heater is uit")
            GPIO.output(heater, GPIO.HIGH)


except KeyboardInterrupt:
    GPIO.cleanup()