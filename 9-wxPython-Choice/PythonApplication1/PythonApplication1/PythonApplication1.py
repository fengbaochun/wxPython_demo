import wx  
  
class ChoiceFrame(wx.Frame):  
    def __init__(self,parent):  
        wx.Frame.__init__(self, None, -1, 'Choice Example',   
                size=(250, 200))  
        panel = wx.Panel(self, -1)  
        sampleList = ['COM1', 'COM2', 'COM3', 'COM4', 'COM5', 'COM6',  
                      'COM7', 'COM8', 'COM9']  
        self.Info_txt=wx.StaticText(panel, -1, "串口号", (15, 20))  
        self.ChoiceOption=wx.Choice(panel, -1, (85, 18), choices=sampleList)  
        self.Bind(wx.EVT_CHOICE, self.ChoseBox1, self.ChoiceOption)#绑定事件

         # 系统事件
        self.Bind(wx.EVT_CLOSE, self.OnClose)

    def ChoseBox1(self,event):
        ''' 复选框回调函数'''
        print(event.GetString()+"被选中")   

    def OnClose(self, evt):
        '''关闭窗口事件函数'''
        dlg = wx.MessageDialog(None, u'确定要关闭本窗口？', u'操作提示', wx.YES_NO | wx.ICON_QUESTION)
        if(dlg.ShowModal() == wx.ID_YES):
            self.Destroy()


class mainApp(wx.App):
    """
    在OnInit() 里边申请Frame类，这样能保证一定是在app后调用，
    这个函数是app执行完自己的__init__函数后就会执行
    """
    def OnInit(self):
        self.Frame = ChoiceFrame(None)
        self.Frame.Show()
        return True

    """
    在def OnExit(self):这个是窗口关闭后调用的函数，
    把要释放的非wx资源或者要保存的放到这个函数里，
    优雅的退出不留遗憾
    """
    def OnExit(self):
       print("关闭窗口后调用")

#主函数入口
if __name__ == "__main__":
    app = mainApp()
    app.MainLoop()



