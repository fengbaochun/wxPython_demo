import serial #导入模块
import serial.tools.list_ports
import time
import threading
import _thread

STRGLO = " 123"#读取的数据


 
def Rev_data(dev):
    """ 读取数据 线程实现"""
    global STRGLO
    while True:
        if dev.in_waiting:
            STRGLO = dev.read(dev.in_waiting).decode("gbk")
            print(STRGLO)

def Send_data(dev):
    """ 发送数据 线程实现"""
    #等待发送按钮按下，读取对话框并写入串口
    while True:
        time.sleep(1)
        print(dev)


class SerialDev():

    """串口设备 """
    #以下类变量所有SerialDev实例共享
    SerialName_list = []
    CurrentSerial_num = ""#当前的串口号
    CurrentSerial_speed = 0#当前的波特率
    Timeout = 0#超时时间

    Dev_num = 0#串口设备数量
    #获取串口设备
    def GetSerial_list(self):
        self.SerialName_list = list(serial.tools.list_ports.comports())
        self.Dev_num = len(self.SerialName_list)
        print(self.Dev_num)#打印设备个数

 
    #设置串口的波特率、串口号、等
    def SerialInfo(self,temp_info,flag):
        if flag == 1:
            self.CurrentSerial_num = temp_info
            print("当前串口号-》" + self.CurrentSerial_num)
            print(self.Dev_num)#打印设备个数
        elif flag == 2:
            self.CurrentSerial_speed = temp_info
            print("当前波特率-》" + self.CurrentSerial_speed)
        elif flag == 3:
            self.CurrentSerial_speed = temp_info
            print("当前校检位-》" + self.CurrentSerial_speed)
        elif flag == 4:
            self.CurrentSerial_speed = temp_info
            print("当前数据位-》" + self.CurrentSerial_speed)
        elif flag == 5:
            self.CurrentSerial_speed = temp_info
            print("当前停止位-》" + self.CurrentSerial_speed)



    def OpenSerialDev(self):
        """打开串口设备"""
        self.SerialName_list = list(serial.tools.list_ports.comports())
        self.Dev_num = len(self.SerialName_list)
        ret = False
        print(self.Dev_num)#打印设备个数
        if self.Dev_num > 0:
            try:
                # 打开串口，并得到串口对象
                ser_dev = serial.Serial(self.CurrentSerial_num, self.CurrentSerial_speed, timeout=None)
                #判断是否打开成功
                if(ser_dev.is_open):
                    ret = True
                    print(self.CurrentSerial_num + "已打开" + "新建接收数据线程")
                    #新建接收线程，接收到的数据打印出来
                    _thread.start_new_thread(Rev_data, (ser_dev,))
                    _thread.start_new_thread( Send_data, (ser_dev,) )
                    
            except Exception as e:
                ser_dev.close()#关闭串口
                print("---异常---：", e)
            return ser_dev,ret
        else:
            print("没有可用设备") 

    def CloseSerialDev(self):

        print("已关闭")
        pass


