import serial #导入模块
import serial.tools.list_ports

import threading

STRGLO =" "#读取的数据
class SerialDev():

    """串口设备 """
    #以下类变量所有SerialDev实例共享
    SerialName_list = []
    CurrentSerial_num = ""#当前的串口号
    CurrentSerial_speed = 0#当前的波特率
    Timeout = 0#超时时间

    Dev_num=0#串口设备数量
    

    #获取串口设备
    def GetSerial_list(self):
        self.SerialName_list = list(serial.tools.list_ports.comports())
        self.Dev_num=len(self.SerialName_list)
        print(self.Dev_num)#打印设备个数
        #if self.Dev_num == 0:
        #    print('无可用串口')
        #else:
        #    for i in range(0,self.Dev_num):
        #        print(self.SerialName_list[i])
 
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



    
        #读数代码本体实现
    def ReadData(ser):
        global STRGLO
        # 循环接收数据，此为死循环，可用线程实现
        while True:
            if ser.in_waiting:
                STRGLO = ser.read(ser.in_waiting).decode("gbk")
                print(STRGLO)

    #打开串口设备
    def OpenSerialDev(self):
        self.SerialName_list = list(serial.tools.list_ports.comports())
        self.Dev_num=len(self.SerialName_list)
        ret = False
        print(self.Dev_num)#打印设备个数
        if self.Dev_num > 0:
            try:
                # 打开串口，并得到串口对象
                ser_dev = serial.Serial(self.CurrentSerial_num, self.CurrentSerial_speed, timeout=None)
                #判断是否打开成功
                if(ser_dev.is_open):
                    ret = True
                    print(self.CurrentSerial_num + "已打开")
                    #此处接收数据有问题
                    ##threading.Thread(target=ReadData, args=(ser_dev,)).start()

                    ## 循环接收数据，此为死循环，可用线程实现
                    #while True:
                    #    if ser_dev.in_waiting:
                    #        STRGLO = ser_dev.read(ser_dev.in_waiting).decode("gbk")
                    #        print(STRGLO)
            except Exception as e:
                print("---异常---：", e)
            return ser_dev,ret
        else:
            print("没有可用设备")

    def CloseSerialDev(self):
        print("已关闭")


