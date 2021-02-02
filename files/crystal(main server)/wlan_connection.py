# -*- coding: utf-8 -*-
import socket
import threading


wlanport = 1234
serverip = "192.168.1.103"


class Server:
    def __init__(self, ip=serverip, port=wlanport):  # 设置默认值
        self.addr = ip, port
        self.lock = threading.Lock()
        self.sock = socket.socket()
        self.sock.bind(self.addr)
        self.socks = {"accept": self.sock}  # 将所有创建的socket都放字典，方便释放

    def start(self):  # 启动接口
        self.sock.listen()
        threading.Thread(target=self.accept, name="accept", daemon=True).start()

    def accept(self):  # 该线程等待连接并创建处理线程
        while True:
            s, raddr = self.sock.accept()
            with self.lock:
                self.socks[raddr] = s
            threading.Thread(target=self.recv, args=(s, raddr), name="recv", daemon=True).start()

    def recv(self, s, raddr):  # 每个客户端开启一个线程与其交互
        while True:
            data = s.recv(1024).decode()
            if data.strip() == "" or data.strip() == "quit":  # 客户端结束条件
                with self.lock:
                    self.socks.pop(raddr)
                    s.close()
                    break
            print(data)
            s.send("server:{}\n".format(data).encode())

    def stop(self):
        with self.lock:
            for s in self.socks.values():
                s.close()
s = Server()
s.start()

while True:
    cmd = input("server commond:>>>")
    if cmd == "quit":  # 服务器退出条件
        s.stop()
        break
    print(threading.enumerate())

