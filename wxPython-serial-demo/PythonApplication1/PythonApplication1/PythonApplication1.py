import wx
from SerialGUI import SerialGUI

import threading
import time


class SerialApp(wx.App):
    def OnInit(self):
        self.Frame = SerialGUI(None)
        self.Frame.Show()

        return True

    def OnExit():
        print("关闭窗口的时候会调用")

#创建线程类
class CreatThread(threading.Thread):#继承父类 threading.Thread
    def __init__(self,  name,counter,thread_addr):
        threading.Thread.__init__(self)
        self.name = name
        self.counter = counter
        self.thread_addr = thread_addr

    ''' 将需要执行的函数写在run（）里面，创建后会自动运行 '''
    def run(self):
        print("Starting" + self.name)
        APP_thread(self.name,self.counter,self.thread_addr)
        print("Exiting" + self.name)


"""
串口助手界面线程
"""
def SerialApp_GUI_Thread():
    app = SerialApp()
    app.MainLoop()


"""
将所有的线程
全部都放在这个里面

根据不同的线程地址分配
"""

def APP_thread(name,delay,thread_addr):
    if thread_addr == 1:
        SerialApp_GUI_Thread()

    elif thread_addr == 2:
        while True:
            time.sleep(delay)
            print("%s: %s" % (name, time.ctime(time.time())))

    #elif thread_addr == 3:

    #elif thread_addr == 4:

    #elif thread_addr == 5:

    #elif thread_addr == 6:


if __name__ == "__main__":

    # 创建新线程
    GUI_Thread = CreatThread("SerialApp_GUI", 1,1)
    thread2 = CreatThread("Serial", 1,2)
        # 开启线程
    GUI_Thread.start()
    thread2.start()
