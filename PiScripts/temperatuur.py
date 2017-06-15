# import time
#
# import RPi.GPIO  as GPIO
# #id van one-wire sensor opzoeken
# sensor_file = '/sys/bus/w1/devices/28-031674f199ff/w1_slave'
# heater = 21
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(heater, GPIO.OUT)
# def read_temp_raw():
#     with open (sensor_file, 'r') as f:
#         lines = f.readlines()
#         return lines
# def read_temp():
#     lines = read_temp_raw()
#     equals_pos = lines[1].find('t=')
#     if equals_pos != -1:
#             return lines[1]
# def temp():
#     temp = read_temp()
#     temperatuur = temp.split ("=")[1]
#     temperatuur = float(temperatuur)/1000
#     return temperatuur
# while True:
#     print("Het is: " + str(temp()) + "°C")
#     time.sleep(1)
#     if temp() >= 28.0:
#             print("Heater is aan")
#             GPIO.output(heater,GPIO.HIGH)
#     else:
#             print("Heater is uit")
#             GPIO.output(heater,GPIO.LOW)

import time
class Temp_sensor():
    #id van one-wire sensor opzoeken
    sensor_file = '/sys/bus/w1/devices/28-0516a143eaff/w1_slave'

    def read_temp_raw(self):
        with open(Temp_sensor().sensor_file, 'r') as f:
            lines = f.readlines()
        return lines
    def read_temp(self):
        lines = Temp_sensor().read_temp_raw()
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
                return lines[1]
    def temp(self):
        temp = Temp_sensor().read_temp()
        temperatuur = temp.split("=")[1]
        temperatuur = float(temperatuur)/1000
        return temperatuur