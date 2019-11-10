import wx    
app_title = 'Hello, wxPython!'
IMG_PATH = '公众号.jpg'
class Frame(wx.Frame):

    def __init__(self,  parent, id=-1,pos=wx.DefaultPosition,title=app_title,size=(800, 800)):

        self.image = wx.Image(IMG_PATH, wx.BITMAP_TYPE_JPEG)
        temp = self.image.ConvertToBitmap()                           
        
        wx.Frame.__init__(self, parent, id, title, pos, size=(500,500))   
        self.bmp = wx.StaticBitmap(parent=self, bitmap=temp)

        #wx.StaticBitmap(parent, id=-1, bitmap=temp, pos=wx.DefaultPosition, size=wx.DefaultSize, style=0, name="test")



class mainApp(wx.App):
    """
    在OnInit() 里边申请Frame类，这样能保证一定是在app后调用，
    这个函数是app执行完自己的__init__函数后就会执行
    """
    def OnInit(self):
        self.Frame = Frame(None)
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