#import wx  
 
#class ListBoxFrame(wx.Frame):  
#    def __init__(self):  
#        wx.Frame.__init__(self, None, -1, 'List Box Example',   
#                size=(250, 200))  
#        panel = wx.Panel(self, -1)  
 
#        sampleList = ['����', 'ƻ��', '�㽶', '����', '��֦', '����',  
#                      'â��', '����', 'ʯ��', '����', '����', '���۹�',  
#                      '�����', '⨺���', '������']  
 
#        listBox = wx.ListBox(panel, -1, (20, 20), (80, 120), sampleList, wx.LB_SINGLE)                 
#        self.Bind(wx.EVT_LISTBOX,self.on_combobox,listBox) #����¼�����
#        listBox.SetSelection(3)  


#    def on_combobox(self,event):
#            listBox=event.GetEventObject()
#            print("ѡ��{0}".format(listBox.GetSelection()))

                 
#if __name__ == '__main__':  
#    app = wx.PySimpleApp()  
#    frame = ListBoxFrame()  
#    frame.Show()  
#    app.MainLoop()  

##############################################
#import wx  


#class ButtonFrame(wx.Frame): 
#    ClickNum = 0  #�������
#    def __init__(self):  
#        wx.Frame.__init__(self, None, -1, 'Serial Demo',   
#                size=(800, 600))  

#        panel = wx.Panel(self, -1)  

#        self.button = wx.Button(panel, -1, "OFF", pos=(400, 300),size=(100,50))  
#        self.Bind(wx.EVT_BUTTON, self.OnClick, self.button) #���ص������밴����
#        self.button.SetDefault() 

#    def OnClick(self, event):  
#        self.button.SetLabel("ON") 
#        self.ClickNum+=1
#        if self.ClickNum % 2 == 1:  #���ݰ��´����ж�
#            self.button.SetLabel("ON")
#            print(self.ClickNum)
#        else:
#            self.button.SetLabel("OFF")
#            self.ClickNum = 0
#            print(self.ClickNum)


        
#if __name__ == '__main__':  
#    # ������ʹ��wxPython�Ĺ̶��÷�
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
#        self.sc = wx.SpinCtrl(panel, -1, "", (30, 20), (80, -1)) #�����ؼ�
#        self.sc.SetRange(-100,100)     #���÷�Χ
#        self.sc.SetValue(0)      #���õ�ǰֵ

#    def GetSpinner_val():#��ȡ
#        #print(sc.GetValue())
#        return self.sc.GetValue()
    

#if __name__ == '__main__':  
#    # ������ʹ��wxPython�Ĺ̶��÷�
#    app = wx.PySimpleApp()
#    frame = SpinnerFrame()
#    frame.Show()
#    app.MainLoop() 