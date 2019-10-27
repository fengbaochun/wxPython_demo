
import wx
class Frame1(wx.Frame):
   def __init__(self):
        wx.Frame.__init__(self,"hello world", pos = (100,200), size = (200,100))
        #容纳其他组件的容器
        panel = wx.Panel(self)
        text1 = wx.TextCtrl(panel, value = "Hello, World!", size = (200,100))
        self.Show(True)
#if __name__ == '__main__':
#    #创建一个应用程序对象，用于消息循环
#    app = wx.App()
#    #创建一个窗体
#    frame = Frame1(None, "Example")


        
if __name__ == '__main__':  
    # 下面是使用wxPython的固定用法
    app = wx.App()  
    frame = Frame1()  
    frame.Show()  
    app.MainLoop()
