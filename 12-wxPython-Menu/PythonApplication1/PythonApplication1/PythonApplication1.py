

import wx
class Example(wx.Frame):
    def __init__(self,*args,**kw):
        super(Example,self).__init__(*args,**kw)
        self.InitUI()
    def InitUI(self):
        menuBar = wx.MenuBar()
        
        fileMenu = wx.Menu()
        fileMenu.Append(wx.ID_NEW,"&New")
        fileMenu.Append(wx.ID_OPEN, '&Open')
        fileMenu.Append(wx.ID_SAVE, '&Save')
        fileMenu.AppendSeparator()
        
        imp = wx.Menu()
        imp.Append(wx.ID_ANY, 'Import newsfeed list...')
        imp.Append(wx.ID_ANY, 'Import bookmarks...')
        imp.Append(wx.ID_ANY, 'Import mail...')
 
        qmi = wx.MenuItem(fileMenu, wx.ID_EXIT, '&Quit\tCtrl+W')
        fileMenu.AppendItem(qmi)
        menuBar.Append(fileMenu, '&File')
        self.SetMenuBar(menuBar)
        
        self.Bind(wx.EVT_MENU, self.OnQuit, qmi)
        
        self.SetSize((400,250))
        self.SetTitle("SimpleMenu")
        #self.Centre()
        self.Center()
        self.Show()
    def OnQuit(self,e):
        self.Close()
    
def main():
    ex = wx.App()
    Example(None)
    ex.MainLoop()
if __name__ == '__main__':
    main()

