# -*- coding: utf-8 -*-
import time
import json

from EventManager import EventManager
# import EventManager

def b(a=1):
    for i in range(a):
        print('ok')


class Crystal:
    def __init__(self,hostname,version,id_level,):
        self.hostname = hostname
        self.version = version
        self.id_level = id_level

    def pop_information(self):
        information = 'IdIoT Server Information'
        information+= 'version:\n   IdIoT:'+str(self.version)
        # print('version:\n   IdIoT:',self.version)
        # print('hostname:\n  name:',self.hostname)
        print(information)


if __name__ == '__main__':
    # 启动时 先读取address book并尝试重连

    EventMgr = EventManager()

    EventMgr.register_event_listener('a', b)
    # EventMgr.broadcast_event('a', None, False)

    server = Crystal('IdIoT-starter', '0.0.1-py', 15)

    server.pop_information()
