import wx

class TextFrame(wx.Frame):
    str_test = "123456789qwerttyuiopaslkjdhfgnmzbxvcfaghqjqjh123456789qwerttyuiopaslkjd \
    hfgnmzbxvcfaghqjqjh123456789qwerttyuiopaslkjdhfgnmzbxvcfaghqjqjh"
    SystemFrontSize=12 #设置系统字体（所有的界面都是修改这个参数）
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Text Entry Example',
                size=(800, 600))

        panel = wx.Panel(self, -1)

        multiLabel = wx.StaticText(panel, -1, "接收数据",pos=(0,0)) #创建静态文本
        font = wx.Font(self.SystemFrontSize, wx.DEFAULT, wx.NORMAL,
        wx.NORMAL)#设置字体信息
        multiLabel.SetFont(font) #设置字体

        multiText = wx.TextCtrl(panel, -1,
               self.str_test,
               size=(300, 400), style=wx.TE_MULTILINE,pos=(50,50)) #创建一个文本控件
      
        font = wx.Font(self.SystemFrontSize, wx.DEFAULT, wx.NORMAL,
        wx.NORMAL)#设置字体信息
        multiText.SetFont(font) #设置字体

        #multiText.SetInsertionPoint(0) #设置插入点

    ##设置字体demo
    # text = wx.StaticText(panel, -1 ,"设置文本font", (20,100))
    # font = wx.Font(18, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
    # text.SetFont(font)

if __name__ == '__main__':
    # 下面是使用wxPython的固定用法
    app = wx.PySimpleApp()
    frame = TextFrame()
    frame.Show()
    app.MainLoop()