import wx

class SerialGUI(wx.Frame):
    str_test = "hello world \
    hello world "
    SystemFrontSize=10 #设置系统字体（所有的界面都是修改这个参数）
    def __init__(self):
        wx.Frame.__init__(self, None, -1, '宇宙无敌版V1.0',
                size=(650, 600))

        panel = wx.Panel(self, -1)

        multiLabel = wx.StaticText(panel, -1, " ",pos=(0,0)) #创建静态文本
        font = wx.Font(self.SystemFrontSize, wx.DEFAULT, wx.NORMAL,
        wx.NORMAL)#设置字体信息
        multiLabel.SetFont(font) #设置字体


        ShowInfo_txt = wx.TextCtrl(panel, -1,
               self.str_test,
               size=(400, 400), style=wx.TE_MULTILINE,pos=(200,20)) #创建一个文本控件
     
        font = wx.Font(self.SystemFrontSize, wx.DEFAULT, wx.NORMAL,
        wx.NORMAL)#设置字体信息
        ShowInfo_txt.SetFont(font) #设置字体

        InputInfo_txt = wx.TextCtrl(panel, -1,
                self.str_test,
                size=(400, 100), style=wx.TE_MULTILINE,pos=(200,440)) #创建一个文本控件
     
        font = wx.Font(self.SystemFrontSize, wx.DEFAULT, wx.NORMAL,
        wx.NORMAL)#设置字体信息
        InputInfo_txt.SetFont(font) #设置字体


        COMNum_List = ['COM1', 'COM2', 'COM3', 'COM4', 'COM5', 'COM6',  
        'COM7', 'COM8', 'COM9','COM10']  
        Speed_List = ['4800', '9600', '14400', '19200', '28800', '38400',  
        '57600', '115200']  
        ChockPos_List = ['None', 'Odd', 'Even', 'Mark', 'Space']  
        DataPos_List = ['5', '6', '7', '8']  
        StopPos_List = ['1', '1.5', '2']  
        self.SerialNum_Txt=wx.StaticText(panel, -1, "串口号", (15, 20))  
        self.SerialNum_Option=wx.Choice(panel, -1, (90, 20), choices=COMNum_List,size=(100,30))  

        self.Speed_Txt=wx.StaticText(panel, -1, "波特率", (15, 60))  
        self.Speed_Option=wx.Choice(panel, -1, (90, 60), choices=Speed_List,size=(100,30))  

        self.ChockPos_Txt=wx.StaticText(panel, -1, "校检位", (15, 100))  
        self.ChockPos_Option=wx.Choice(panel, -1, (90, 100), choices=ChockPos_List,size=(100,30))  

        self.DataPos_Txt=wx.StaticText(panel, -1, "数据位", (15, 140))  
        self.DataPos_Option=wx.Choice(panel, -1, (90, 140), choices=DataPos_List,size=(100,30))  

        self.StopPos_Txt=wx.StaticText(panel, -1, "停止位", (15, 180))  
        self.StopPos_Option=wx.Choice(panel, -1, (90, 180), choices=StopPos_List,size=(100,30))  
        #font = wx.Font(self.SystemFrontSize, wx.DEFAULT, wx.NORMAL,
        #wx.NORMAL)#设置字体信息
        #self.StopPos_Txt.SetFont(font) #设置字体


        self.Rev_Clear = wx.CheckBox(panel, -1, "自动清空", (50, 240))  #创建控件
        self.Bind(wx.EVT_CHECKBOX, self.Rev_Clear_Event, self.Rev_Clear)#绑定事件

        self.Send_Clear = wx.CheckBox(panel, -1, "自动发送", (50, 260))  #创建控件
        self.Bind(wx.EVT_CHECKBOX, self.Send_Clear_Event, self.Send_Clear)#绑定事件

        self.Show_16_Option = wx.CheckBox(panel, -1, "16进制显示", (50, 280))  #创建控件
        self.Bind(wx.EVT_CHECKBOX, self.Show_16_Option_Event, self.Show_16_Option)#绑定事件

        self.Show_16_Send = wx.CheckBox(panel, -1, "16进制显示", (50, 300))  #创建控件
        self.Bind(wx.EVT_CHECKBOX, self.Show_16_Send_Event, self.Show_16_Send)#绑定事件

    def Show_16_Send_Event(self,event):#事件回调函数
        print("Show_16_Send_Event 被选中")

    def Show_16_Option_Event(self,event):#事件回调函数
        print("Show_16_Option_Event 被选中")

    def Send_Clear_Event(self,event):#事件回调函数
        print("Send_Clear_Event 被选中")

    def Rev_Clear_Event(self,event):#事件回调函数
        print("Rev_Clear_Event 被选中")



    ##设置字体demo
    # text = wx.StaticText(panel, -1 ,"设置文本font", (20,100))
    # font = wx.Font(18, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
    # text.SetFont(font)

if __name__ == '__main__':
    # 下面是使用wxPython的固定用法
    app = wx.PySimpleApp()
    frame = SerialGUI()
    frame.Show()
    app.MainLoop()

