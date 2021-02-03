from wlan_connection import Server
from serial_connection import Serial_communicate
import time


serial_communicate = Serial_communicate('com4')
serial_communicate.port_open()
server = Server('192.168.1.103', 1234)
server.start()


while True:
    if server.getmsg() != 'no message':
        serial_communicate.send("open\n")
        time.sleep(0.2)
