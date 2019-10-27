import wx  
 
class Slider(wx.Frame):  
    def __init__(self):  
        wx.Frame.__init__(self, None, -1, 'Text Entry Example',   
                size=(800, 600))  
        panel = wx.Panel(self, -1)   
        self.widthSlider = wx.Slider(panel, 10, minValue=-200, maxValue=200, pos=(190, 140), size=(330, 30), style=wx.SL_LABELS)
        self.widthSlider.SetValue(0)#设置当前数值
        self.Bind(wx.EVT_SCROLL_THUMBRELEASE, self.sliderSubThumbMoveFunc, self.widthSlider)#绑定回调函数


    def sliderSubThumbMoveFunc(self, event):#回调函数
        obj = event.GetEventObject()
        objID = obj.GetId()
        width = obj.GetValue()
        print("width->%d",width)#打印数值
        pass

# 下面是使用wxPython的固定用法
if __name__ == '__main__':  
    app = wx.PySimpleApp()  
    frame = Slider()  
    frame.Show()  
    app.MainLoop()   