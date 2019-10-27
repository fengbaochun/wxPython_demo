import wx  

class SpinnerFrame(wx.Frame):  
    def __init__(self):  
        wx.Frame.__init__(self, None, -1, 'Spinner Example',   
                size=(300, 300))  
        panel = wx.Panel(self, -1)  
        self.sc = wx.SpinCtrl(panel, -1, "", (30, 20), (80, -1)) #创建控件
        self.sc.SetRange(-100,100)     #设置范围
        self.sc.SetValue(0)      #设置当前值

    def GetSpinner_val():#获取
        #print(sc.GetValue())
        return self.sc.GetValue()
    

if __name__ == '__main__':  
    # 下面是使用wxPython的固定用法
    app = wx.PySimpleApp()
    frame = SpinnerFrame()
    frame.Show()
    app.MainLoop() 