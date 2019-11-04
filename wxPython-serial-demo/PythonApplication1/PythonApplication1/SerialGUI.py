import wx 
from Serial import SerialDev


class SerialGUI(wx.Frame):
    str_test = "hello world \
    hello world "
    SystemFrontSize = 10 #设置系统字体（所有的界面都是修改这个参数）
    ClickNum = 0  #定义变量
    SerialGUI_set = SerialDev()

    def __init__(self,parent):
        wx.Frame.__init__(self, None, -1, '宇宙无敌版V1.0',
                size=(650, 600))

        panel = wx.Panel(self, -1)

        multiLabel = wx.StaticText(panel, -1, " ",pos=(0,0)) #创建静态文本
        font = wx.Font(self.SystemFrontSize, wx.DEFAULT, wx.NORMAL,
        wx.NORMAL)#设置字体信息
        multiLabel.SetFont(font) #设置字体

        #接收
        ShowInfo_txt = wx.TextCtrl(panel, -1,
               self.str_test,
               size=(400, 400), style=wx.TE_MULTILINE,pos=(200,20)) #创建一个文本控件
    
        font = wx.Font(self.SystemFrontSize, wx.DEFAULT, wx.NORMAL,
        wx.NORMAL)#设置字体信息
        ShowInfo_txt.SetFont(font) #设置字体

        #输入
        InputInfo_txt = wx.TextCtrl(panel, -1,
                self.str_test,
                size=(400, 100), style=wx.TE_MULTILINE,pos=(200,440)) #创建一个文本控件
    
        font = wx.Font(self.SystemFrontSize, wx.DEFAULT, wx.NORMAL,
        wx.NORMAL)#设置字体信息
        InputInfo_txt.SetFont(font) #设置字体

        #打开串口 按钮
        self.OpenSerialbutton = wx.Button(panel,-1, "打开串口", pos=(100, 220),size=(80,30)) #在面板上添加控件
        self.Bind(wx.EVT_BUTTON, self.OpenSerial_Event, self.OpenSerialbutton) #将回调函数与按键事件绑定

        #发送数据 按钮
        self.SendDatabutton = wx.Button(panel,-1, "发送数据", pos=(100, 510),size=(80,30)) 
        self.Bind(wx.EVT_BUTTON, self.SendData_Event, self.SendDatabutton) 

        #清空缓存区 按钮
        self.ClearSendBufferbutton = wx.Button(panel,-1, "清空缓存区", pos=(100, 440),size=(80,30)) 
        self.Bind(wx.EVT_BUTTON, self.ClearSendBuffer_Event, self.ClearSendBufferbutton) 

        #清空接收区 按钮
        self.ClearRevBufferbutton = wx.Button(panel,-1, "清空接收区", pos=(100, 260),size=(80,30)) 
        #self.Bind(wx.EVT_BUTTON, self.ClearSendBuffer_Event,
                                                                                                     #self.ClearSendBufferbutton)
                                                                                                     ##将回调函数与按键事件绑定
        #停止显示 按钮
        self.StopShowbutton = wx.Button(panel,-1, "停止显示", pos=(100, 300),size=(80,30)) 
        self.Bind(wx.EVT_BUTTON, self.StopShow_Event, self.StopShowbutton) 


        COMNum_List = ['COM1', 'COM2', 'COM3', 'COM4', 'COM5', 'COM6',  
        'COM7', 'COM8', 'COM9','COM10']  
        Speed_List = ['4800', '9600', '14400', '19200', '28800', '38400',  
        '57600', '115200']  
        ChockPos_List = ['None', 'Odd', 'Even', 'Mark', 'Space']  
        DataPos_List = ['5', '6', '7', '8']  
        StopPos_List = ['1', '1.5', '2']  

        #串口号 复选框
        self.SerialNum_Txt = wx.StaticText(panel, -1, "串口号", (15, 20))  
        self.SerialNum_Option = wx.Choice(panel, -1, (100, 20), choices=COMNum_List,size=(80,30))  
        self.Bind(wx.EVT_CHOICE,self.SerialNum_choice,self.SerialNum_Option)

        #波特率 复选框
        self.Speed_Txt = wx.StaticText(panel, -1, "波特率", (15, 60))  
        self.Speed_Option = wx.Choice(panel, -1, (100, 60), choices=Speed_List,size=(80,30))  
        self.Bind(wx.EVT_CHOICE,self.Speed_choice,self.Speed_Option)

        #校检位 复选框
        self.ChockPos_Txt = wx.StaticText(panel, -1, "校检位", (15, 100))  
        self.ChockPos_Option = wx.Choice(panel, -1, (100, 100), choices=ChockPos_List,size=(80,30))  
        self.Bind(wx.EVT_CHOICE,self.ChockPos_choice,self.ChockPos_Option)

        #数据位 复选框
        self.DataPos_Txt = wx.StaticText(panel, -1, "数据位", (15, 140))  
        self.DataPos_Option = wx.Choice(panel, -1, (100, 140), choices=DataPos_List,size=(80,30))  
        self.Bind(wx.EVT_CHOICE,self.DataPos_choice,self.DataPos_Option)

        #停止位 复选框
        self.StopPos_Txt = wx.StaticText(panel, -1, "停止位", (15, 180))  
        self.StopPos_Option = wx.Choice(panel, -1, (100, 180), choices=StopPos_List,size=(80,30))  
        self.Bind(wx.EVT_CHOICE,self.StopPos_choice,self.StopPos_Option)



        self.Rev_Clear = wx.CheckBox(panel, -1, "自动清空", (15, 261))  #创建控件
        self.Bind(wx.EVT_CHECKBOX, self.Rev_Clear_Event, self.Rev_Clear)#绑定事件
        self.Rev_Clear.SetValue(True)#设置当前是否被选中

        self.Send_Clear = wx.CheckBox(panel, -1, "自动发送", (15, 450))  #创建控件
        self.Bind(wx.EVT_CHECKBOX, self.Send_Clear_Event, self.Send_Clear)#绑定事件
        self.Send_Clear.SetValue(True)#设置当前是否被选中

        self.CycleSend_Text = wx.StaticText(panel, -1, "发送周期(ms)",(15, 478))  
        self.CycleSend_Info = wx.TextCtrl(panel, -1,
                "1000",
                size=(80, 25), style=wx.TE_MULTILINE,pos=(100,475)) #创建一个文本控件


        self.Show_16_Option = wx.CheckBox(panel, -1, "16进制显示", (15, 286))  #创建控件
        self.Bind(wx.EVT_CHECKBOX, self.Show_16_Option_Event, self.Show_16_Option)#绑定事件
        self.Show_16_Option.SetValue(True)#设置当前是否被选中

        self.Show_16_Option = wx.CheckBox(panel, -1, "转向文件", (15, 310))  #创建控件
        self.Bind(wx.EVT_CHECKBOX, self.Show_16_Option_Event, self.Show_16_Option)#绑定事件
        self.Show_16_Option.SetValue(True)#设置当前是否被选中

        self.Show_16_Send = wx.CheckBox(panel, -1, "16进制发送", (15, 515))  #创建控件
        self.Bind(wx.EVT_CHECKBOX, self.Show_16_Send_Event, self.Show_16_Send)#绑定事件
        self.Show_16_Send.SetValue(True)#设置当前是否被选中

        # 系统事件
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.Bind(wx.EVT_SIZE, self.On_size)

    def Show_16_Send_Event(self,event):#事件回调函数
        print(self.Show_16_Send.GetValue())

    def Show_16_Option_Event(self,event):#事件回调函数
        print(self.Show_16_Option.GetValue())

    def Send_Clear_Event(self,event):#事件回调函数
        print(self.Send_Clear.GetValue())

    def Rev_Clear_Event(self,event):#事件回调函数
        print(self.Rev_Clear.GetValue())


    def OpenSerial_Event(self, event):  #回调函数事件
        self.OpenSerialbutton.SetLabel("打开串口") #设置
        self.ClickNum+=1
        if self.ClickNum % 2 == 1:  #根据按下次数判断
            self.OpenSerialbutton.SetLabel("打开串口")#修改按键的标签
            self.SerialGUI_set.OpenSerialDev() #打开串口设备
            #print(self.OpenSerialbutton.GetLabel())#打印信息（返回按键的标签信息）
        else:
            self.OpenSerialbutton.SetLabel("关闭串口")
            self.ClickNum = 0
            #print(self.OpenSerialbutton.GetLabel())

    def SendData_Event(self,event):
        print("SendData_Event test ueing")

    def ClearSendBuffer_Event(self,event):
        print("ClearSendBuffer_Event test ueing")

    def StopShow_Event(self,event):
        self.StopShowbutton.SetLabel("停止显示") #设置
        self.ClickNum+=1
        if self.ClickNum % 2 == 1:  #根据按下次数判断
            self.StopShowbutton.SetLabel("停止显示")#修改按键的标签
            print(self.StopShowbutton.GetLabel())#打印信息（返回按键的标签信息）
        else:
            self.StopShowbutton.SetLabel("已经停止显示")
            self.ClickNum = 0
            print(self.StopShowbutton.GetLabel())

    def SerialNum_choice(self,event):
        ''' 串口号选择 事件函数'''
        temp=event.GetString()#从UI获取串口号
        self.SerialGUI_set.SerialInfo(temp,1)


    def Speed_choice(self,event):
        ''' 波特率选择 事件函数'''
        temp=event.GetString()#从UI获取波特率
        self.SerialGUI_set.SerialInfo(temp,2) 

    def ChockPos_choice(self,event):
        ''' 校检选择 事件函数'''
        print('校检->' + event.GetString())     

    def DataPos_choice(self,event):
        ''' 数据位选择 事件函数'''
        print('数据位->' + event.GetString())    

    def StopPos_choice(self,event):
        ''' 停止位选择 事件函数'''
        print('停止位->' + event.GetString())    

    def On_size(self, evt):
        '''改变窗口大小事件函数'''
        
        self.Refresh()
        evt.Skip() # 体会作用
    
    def OnClose(self, evt):
        '''关闭窗口事件函数'''
        dlg = wx.MessageDialog(None, u'确定要关闭本窗口？', u'操作提示', wx.YES_NO | wx.ICON_QUESTION)
        if(dlg.ShowModal() == wx.ID_YES):
            self.Destroy()
