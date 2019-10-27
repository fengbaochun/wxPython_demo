import wx  


class ButtonFrame(wx.Frame): 
    ClickNum = 0  #定义变量
    def __init__(self):  
        wx.Frame.__init__(self, None, -1, 'Button Demo',   
                size=(300, 300))  

        panel = wx.Panel(self, -1)  
        self.button = wx.Button(panel, -1, "OFF", pos=(50, 50),size=(50,50))  
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.button) #将回调函数与按键绑定
        self.button.SetDefault() 

    def OnClick(self, event):  
        self.button.SetLabel("ON") 
        self.ClickNum+=1
        if self.ClickNum % 2 == 1:  #根据按下次数判断
            self.button.SetLabel("ON")
            print(self.ClickNum)
        else:
            self.button.SetLabel("OFF")
            self.ClickNum = 0
            print(self.ClickNum)


        
if __name__ == '__main__':  
    # 下面是使用wxPython的固定用法
    app = wx.PySimpleApp()  
    frame = ButtonFrame()  
    frame.Show()  
    app.MainLoop()
