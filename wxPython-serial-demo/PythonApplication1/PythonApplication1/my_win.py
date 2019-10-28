#import wx  
 
#class ListBoxFrame(wx.Frame):  
#    def __init__(self):  
#        wx.Frame.__init__(self, None, -1, 'List Box Example',   
#                size=(250, 200))  
#        panel = wx.Panel(self, -1)  
 
#        sampleList = ['橘子', '苹果', '香蕉', '柿子', '荔枝', '西瓜',  
#                      '芒果', '柠檬', '石榴', '葡萄', '榴莲', '哈蜜瓜',  
#                      '百香果', '猕猴桃', '火龙果']  
 
#        listBox = wx.ListBox(panel, -1, (20, 20), (80, 120), sampleList, wx.LB_SINGLE)                 
#        self.Bind(wx.EVT_LISTBOX,self.on_combobox,listBox) #添加事件处理
#        listBox.SetSelection(3)  


#    def on_combobox(self,event):
#            listBox=event.GetEventObject()
#            print("选择{0}".format(listBox.GetSelection()))

                 
#if __name__ == '__main__':  
#    app = wx.PySimpleApp()  
#    frame = ListBoxFrame()  
#    frame.Show()  
#    app.MainLoop()  

##############################################
#import wx  


#class ButtonFrame(wx.Frame): 
#    ClickNum = 0  #定义变量
#    def __init__(self):  
#        wx.Frame.__init__(self, None, -1, 'Serial Demo',   
#                size=(800, 600))  

#        panel = wx.Panel(self, -1)  

#        self.button = wx.Button(panel, -1, "OFF", pos=(400, 300),size=(100,50))  
#        self.Bind(wx.EVT_BUTTON, self.OnClick, self.button) #将回调函数与按键绑定
#        self.button.SetDefault() 

#    def OnClick(self, event):  
#        self.button.SetLabel("ON") 
#        self.ClickNum+=1
#        if self.ClickNum % 2 == 1:  #根据按下次数判断
#            self.button.SetLabel("ON")
#            print(self.ClickNum)
#        else:
#            self.button.SetLabel("OFF")
#            self.ClickNum = 0
#            print(self.ClickNum)


        
#if __name__ == '__main__':  
#    # 下面是使用wxPython的固定用法
#    app = wx.PySimpleApp()  
#    frame = ButtonFrame()  
#    frame.Show()  
#    app.MainLoop()


##########################################
#import wx  

#class SpinnerFrame(wx.Frame):  
#    def __init__(self):  
#        wx.Frame.__init__(self, None, -1, 'Spinner Example',   
#                size=(300, 300))  
#        panel = wx.Panel(self, -1)  
#        self.sc = wx.SpinCtrl(panel, -1, "", (30, 20), (80, -1)) #创建控件
#        self.sc.SetRange(-100,100)     #设置范围
#        self.sc.SetValue(0)      #设置当前值

#    def GetSpinner_val():#获取
#        #print(sc.GetValue())
#        return self.sc.GetValue()
    

#if __name__ == '__main__':  
#    # 下面是使用wxPython的固定用法
#    app = wx.PySimpleApp()
#    frame = SpinnerFrame()
#    frame.Show()
#    app.MainLoop() 