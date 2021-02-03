from wlan_connection import Client
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN)
c = Client("192.168.1.103",1234)


while True:
    if GPIO.input(4):
        print('Input was HIGH')
        c.send("open light")
    else:
        # print('Input was LOW')
	    pass

