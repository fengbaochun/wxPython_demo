#静态文本
import wx  
 
class StaticTextFrame(wx.Frame):  
    def __init__(self):  
        wx.Frame.__init__(self, None, -1, 'Text Example',   
                size=(400, 300))  
        panel = wx.Panel(self, -1)  
 
        # 这是一个基本的静态文本  
        wx.StaticText(panel, -1, "这是一个基本的静态文本  ",   
                (100, 10))  
 
        # 指定了前景色和背景色的静态文本  
        rev = wx.StaticText(panel, -1, " 指定了前景色和背景色的静态文本",   
                (100, 30))  
        rev.SetForegroundColour('white')  
        rev.SetBackgroundColour('black')  
 
        # 指定新字体的静态文本  
        str = "You can also change the font."  
        text = wx.StaticText(panel, -1, str, (20, 100))  
        font = wx.Font(18, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)  
        text.SetFont(font)  
 

 
if __name__ == '__main__':  
    app = wx.PySimpleApp()  
    frame = StaticTextFrame()  
    frame.Show()  
    app.MainLoop()  