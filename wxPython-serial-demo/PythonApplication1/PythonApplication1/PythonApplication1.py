import wx
from SerialGUI import SerialGUI_WX
from SerialGUI import SerialDev
import Serial
import threading
import time

class SerialApp(wx.App):
    global Frame
    def OnInit(self):
        self.Frame = SerialGUI_WX(None)
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
    """ """
    thread_Ser = SerialDev()#实例化对象
    if thread_addr == 1:
        SerialApp_GUI_Thread()#GUI线程

    elif thread_addr == 2:
        while True:
            time.sleep(delay)
            thread_Ser.GetSerial_list()#调用获取串口设备函数


    elif thread_addr == 3:#接收数据线程
        pass

    elif thread_addr == 4:#发送数据线程
        time.sleep(1)#延时一秒
        
        #print(thread_Ser.ser_dev())
            #print("已打开")
        

    elif thread_addr == 5:
        pass

    elif thread_addr == 6:
        pass

if __name__ == "__main__":

    # 创建新线程
    GUI_Thread = CreatThread("SerialApp_GUI", 1,1)
    thread2 = CreatThread("Serial", 1,2)
    serial_rev_thread= CreatThread("serial_rev_thread", 1,3)
    serial_send_thread= CreatThread("serial_send_thread", 1,4)
    # 开启线程
    GUI_Thread.start()
    thread2.start()
    #打开串口后在开启线程
    serial_rev_thread.start()
    serial_send_thread.start()
