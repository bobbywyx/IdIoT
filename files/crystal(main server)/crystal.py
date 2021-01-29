import time
import json
from EventManager import EventManager


def b(a=1):
    for i in range(a):
        print('ok')


if __name__ == '__main__':
    # 启动时 先读取address book并尝试重连

    EventMgr = EventManager()

    EventMgr.register_event_listener('a', b)
    EventMgr.broadcast_event('a', None, False)
