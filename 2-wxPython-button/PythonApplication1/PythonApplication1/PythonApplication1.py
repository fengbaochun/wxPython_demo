import wx  #导入wx模块

APP_TITLE = u'控件事件、鼠标事件、键盘事件、系统事件'

class ButtonFrame(wx.Frame): 
    '''程序主窗口类，继承自wx.Frame'''

    ClickNum = 0  #定义变量
    def __init__(self, parent): 
        '''构造函数'''
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


class mainApp(wx.App):
    """
    在OnInit() 里边申请Frame类，这样能保证一定是在app后调用，
    这个函数是app执行完自己的__init__函数后就会执行
    """
    def OnInit(self):
        self.Frame = ButtonFrame(None)
        self.Frame.Show()
        return True

    """
    在def OnExit(self):这个是窗口关闭后调用的函数，
    把要释放的非wx资源或者要保存的放到这个函数里，
    优雅的退出不留遗憾
    """
    def OnExit(self):
       # self.Frame.ExitFrame()
       print("关闭窗口后调用")

if __name__ == "__main__":
    app = mainApp()
    app.MainLoop()

