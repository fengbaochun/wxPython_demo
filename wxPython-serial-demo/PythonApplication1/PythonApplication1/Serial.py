import serial #导入模块
import serial.tools.list_ports


class SerialDev():

    """串口设备 """

    SerialName_list=[]
    CurrentSerial_num=""#当前的串口号
    CurrentSerial_speed=0#当前的波特率
    Timeout=0#超时时间


    #获取串口设备
    def GetSerial_list():
        SerialName_list = list(serial.tools.list_ports.comports())
        if len(SerialName_list) == 0:
            print('无可用串口')
        else:
            for i in range(0,len(SerialName_list)):
                print(SerialName_list[i])
 
    #设置串口的波特率、串口号、等
    def SerialInfo(self):

        print("已设置")

    #打开串口设备
    def OpenSerialDev(self):
        print("已打开")

    def CloseSerialDev(self):
        print("已关闭")


