import socket
import threading
import datetime

class Client:
    def __init__(self, rip, rport):  # 服务器ip 和 端口
        self._raddr = rip, rport
        self._sock = socket.socket()
        self._connect()

    def _connect(self):
        self._sock.connect(self._raddr)   # 尝试连接指定的地址
        self.f = self._sock.makefile("rw")
        self.f.write("i am client at {}\n".format(self._sock.getsockname()))
        self.f.flush()
        threading.Thread(target=self.recv, name="recv", daemon=True).start()  # 一个进程接收消息
        self.send()   # 主进程发送消息

    def send(self):
        while True:
            msg = input(">>>").strip()
            self.f.write(msg)
            self.f.flush()
            if msg == "quit":
                self.stop()
                break

    def recv(self):
        while True:
            msg = self.f.readline()
            print("server:{}{:%Y/%m/%d %H:%M:%S}\n\t{}".format(self._sock.getpeername(), datetime.datetime.now(), msg))

    def stop(self):
        self.f.close()
        self._sock.close()

c = Client("192.168.1.103", 1234)