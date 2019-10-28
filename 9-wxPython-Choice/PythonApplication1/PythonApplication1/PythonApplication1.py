import wx  
  
class ChoiceFrame(wx.Frame):  
    def __init__(self):  
        wx.Frame.__init__(self, None, -1, 'Choice Example',   
                size=(250, 200))  
        panel = wx.Panel(self, -1)  
        sampleList = ['COM1', 'COM2', 'COM3', 'COM4', 'COM5', 'COM6',  
                      'COM7', 'COM8', 'COM9']  
        self.Info_txt=wx.StaticText(panel, -1, "串口号", (15, 20))  
        self.ChoiceOption=wx.Choice(panel, -1, (85, 18), choices=sampleList)  
        
    #    self.Bind(wx.EVT_CHECKBOX, self.ChoseBox1, self.ChoiceOption)#绑定事件

    #def ChoseBox1(self,event):#事件回调函数
    #    print("被选中")
  

if __name__ == '__main__':
    # 下面是使用wxPython的固定用法
    app = wx.PySimpleApp()
    frame = ChoiceFrame()
    frame.Show()
    app.MainLoop()
