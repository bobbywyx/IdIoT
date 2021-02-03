# -*- coding: utf-8 -*-
import serial
import binascii


class Serial_communicate:
    def __init__(self,port,baudrate=9600,bytesize=8,stopbits=1,parity="N"):
        self.engine = serial.Serial()
        self.engine.port = port  # 设置端口号
        self.engine.baudrate = baudrate  # 设置波特率
        self.engine.bytesize = bytesize  # 设置数据位
        self.engine.stopbits = stopbits  # 设置停止位
        self.engine.parity = parity  # 设置校验位

    def port_open(self):
        self.engine.open()  # 打开串口,要找到对的串口号才会成功
        if (self.engine.isOpen()):
            print("打开成功")
            return(True)
        else:
            print("打开失败")
            return(False)

    def port_close(self):
        self.engine.close()
        if (self.engine.is_open()):
            print("关闭失败")
            return (False)
        else:
            print("关闭成功")
            return (True)

    def send(self,send_data):
        if (self.engine.isOpen()):
            self.engine.write(send_data.encode('utf-8'))  # utf-8 编码发送
            # ser.write(binascii.a2b_hex(send_data))  #Hex发送
            print("发送成功", send_data)
            return (True)
        else:
            print("发送失败")
            return (False)

    def read_event(self):
        pass


if __name__ == "__main__":
    test = Serial_communicate("com4")
    test.port_open()
    # port_close()
    while True:
        if(input("输入1发送")=="1"):
            test.send("open\n")
