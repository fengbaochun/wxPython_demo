import wx  #导入模块
  
class CheckBoxFrame(wx.Frame):  
    def __init__(self):  
        wx.Frame.__init__(self, None, -1, 'Checkbox Demo',   
                size=(400, 300))  #初始化窗口信息
        panel = wx.Panel(self, -1) #创建画板，控件容器
        
        self.box = wx.CheckBox(panel, -1, "Checkbox", pos=(50, 50),size=(80,20))  #创建控件
        self.Bind(wx.EVT_CHECKBOX, self.ChoseBox_Event, self.box)#绑定事件
        self.box.SetValue(False)#设置当前是否被选中

    def ChoseBox_Event(self,event):#事件回调函数
        print(self.box.GetValue())#打印True 证明复选框已经被选中 False 则反之
        
#主函数入口
if __name__ == '__main__':
    # 下面是使用wxPython的固定用法
    app = wx.PySimpleApp()
    frame = CheckBoxFrame()
    frame.Show()
    app.MainLoop()
