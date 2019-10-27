import wx  
 
class ListBoxFrame(wx.Frame):  
    def __init__(self):  
        wx.Frame.__init__(self, None, -1, 'List Box Example',   
                size=(250, 200))  
        panel = wx.Panel(self, -1)  
 
        sampleList = ['橘子', '苹果', '香蕉', '柿子', '荔枝', '西瓜',  
                      '芒果', '柠檬', '石榴', '葡萄', '榴莲', '哈蜜瓜',  
                      '百香果', '猕猴桃', '火龙果']  
 
        listBox = wx.ListBox(panel, -1, (20, 20), (80, 120), sampleList, wx.LB_SINGLE)                 
        self.Bind(wx.EVT_LISTBOX,self.on_combobox,listBox) #添加事件处理
        listBox.SetSelection(3)  


    def on_combobox(self,event):
            listBox=event.GetEventObject()
            print("选择{0}".format(listBox.GetSelection()))

                 
if __name__ == '__main__':  
    app = wx.PySimpleApp()  
    frame = ListBoxFrame()  
    frame.Show()  
    app.MainLoop()  




