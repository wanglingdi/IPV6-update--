# This is a sample Python script.
import requests
import os
import time
import ctypes, sys

time1 = time.time()
time.sleep(5)


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def fix():
    if is_admin():
        command = 'netsh interface ipv6 set privacy state=disable'
        os.system(command)

        command = 'netsh interface set interface name="YTW" admin=DISABLED'#YTW改为你的网络名
        os.system(command)

        command = 'netsh interface set interface name="YTW" admin=ENABLED'#YTW改为你的网络名
        os.system(command)
        # os.system('C:/Users/84988/Desktop/fix.bat')

    else:
        if sys.version_info[0] == 3:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        else:  # in python2.x
            ctypes.windll.shell32.ShellExecuteW(None, u"runas", unicode(sys.executable), unicode(__file__), None, 1)

def find():
    try:
        rp = requests.get('http://bt.neu6.edu.cn/')
        # print(rp.status_code)
        if rp.status_code != 200:
            print("ok")
    except:
        fix()



import time
def loop_func(func, second):
    # 每隔second秒执行func函数
    while True:
        func()
        time.sleep(second)

loop_func(find, 60)
