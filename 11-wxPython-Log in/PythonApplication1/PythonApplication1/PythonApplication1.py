import wx

APP_TITLE = 'Log in'
class TextFrame(wx.Frame):
    str_test = ""
    SystemFrontSize = 12 #设置系统字体（所有的界面都是修改这个参数）
    ClickNum = 0  #定义变量
    """ 起始位置 """
    start_x = 0
    start_y = 0
    def __init__(self, parent): 
        style = wx.CAPTION | wx.DEFAULT_FRAME_STYLE  | wx.CLOSE_BOX | wx.MINIMIZE_BOX | wx.SIMPLE_BORDER
        wx.Frame.__init__(self, parent=None, id=-1, title=APP_TITLE, style=style,size=(300, 180))

        panel = wx.Panel(self, -1)  #创建面板
        """  创建控件 """
        x = self.start_x    
        y = self.start_y    #可移动的相对位置坐标
        self.Account_number_text = wx.StaticText(panel, -1, "账号",pos=(10 + x,14 + y))
        self.Password_text = wx.StaticText(panel, -1, "密码",pos=(10 + x,54 + y))#style=wx.TE_MULTILINE
        self.Account_number = wx.TextCtrl(panel, -1,self.str_test,size=(200, 30), style=wx.TE_NO_VSCROLL,pos=(60 + x,10 + y)) #创建一个文本控件
        self.Password = wx.TextCtrl(panel, -1,self.str_test,size=(200, 30), style=wx.TE_PASSWORD,pos=(60 + x,54 + y)) #创建一个文本控件

        self.button = wx.Button(panel,-1, "登录", pos=(100, 90),size=(80,35)) #在面板上添加控件
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.button) #将回调函数与按键事件绑定

      
        """ 设置 字体信息 """
        font = wx.Font(self.SystemFrontSize, wx.DEFAULT, wx.NORMAL,
        wx.NORMAL)#设置字体信息
        self.Account_number_text.SetFont(font) #设置字体
        self.Password_text.SetFont(font)
        self.Account_number.SetFont(font) #设置字体
        self.Password.SetFont(font)

    def OnClick(self, event):  #回调函数事件
        self.button.SetLabel("登录成功") #设置
        self.ClickNum+=1
        if self.ClickNum % 2 == 1:  #根据按下次数判断
            self.button.SetLabel("登录成功")#修改按键的标签

            print("账 号 ： " + self.Account_number.GetValue())
            print("密 码 ： " + self.Password.GetValue())
            print(self.button.GetLabel())#打印信息（返回按键的标签信息）
        else:
            #self.button.SetLabel("登录")
            self.ClickNum = 0
            print(self.button.GetLabel())

class mainApp(wx.App):
    """
    在OnInit() 里边申请Frame类，这样能保证一定是在app后调用，
    这个函数是app执行完自己的__init__函数后就会执行
    """
    def OnInit(self):
        self.Frame = TextFrame(None)
        self.Frame.Show()
        return True

    """
    在def OnExit(self):这个是窗口关闭后调用的函数，
    把要释放的非wx资源或者要保存的放到这个函数里，
    优雅的退出不留遗憾
    """
    def OnExit(self):
       # self.Frame.ExitFrame()
       print("关闭窗口后调用,可以在这里保存一些相关的配置")
       pass

if __name__ == "__main__":
    app = mainApp()
    app.MainLoop()