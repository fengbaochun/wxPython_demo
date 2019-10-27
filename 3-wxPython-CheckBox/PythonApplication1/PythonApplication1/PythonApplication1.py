#复选框
import wx  
  
class CheckBoxFrame(wx.Frame):  
    def __init__(self):  
        wx.Frame.__init__(self, None, -1, 'Checkbox Example',   
                size=(400, 300))  
        panel = wx.Panel(self, -1) #创建画板，控件容器
        
        self.box1 = wx.CheckBox(panel, -1, "Checkbox", (50, 50))  #创建控件
        self.Bind(wx.EVT_CHECKBOX, self.ChoseBox1, self.box1)#绑定事件

    def ChoseBox1(self,event):#事件回调函数
        print("被选中")



if __name__ == '__main__':
    # 下面是使用wxPython的固定用法
    app = wx.PySimpleApp()
    frame = CheckBoxFrame()
    frame.Show()
    app.MainLoop()
