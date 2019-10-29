import wx  #导入wx模块

class ButtonFrame(wx.Frame): 
    ClickNum = 0  #定义变量
    def __init__(self):  
        wx.Frame.__init__(self, None, -1, 'Button Demo',   
                size=(300, 200))  #初始化窗口信息

        panel = wx.Panel(self, -1)  #创建面板
        self.button = wx.Button(panel,-1, "OFF", pos=(50, 50),size=(50,30)) #在面板上添加控件
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.button) #将回调函数与按键事件绑定

    def OnClick(self, event):  #回调函数事件
        self.button.SetLabel("ON") #设置
        self.ClickNum+=1
        if self.ClickNum % 2 == 1:  #根据按下次数判断
            self.button.SetLabel("ON")#修改按键的标签
            print(self.button.GetLabel())#打印信息（返回按键的标签信息）
        else:
            self.button.SetLabel("OFF")
            self.ClickNum = 0
            print(self.button.GetLabel())

#主函数入口
if __name__ == '__main__':  
    # 下面是使用wxPython的固定用法
    app = wx.PySimpleApp()  
    frame = ButtonFrame()  
    frame.Show()  
    app.MainLoop()
