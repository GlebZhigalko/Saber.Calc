import wx


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(300, 300))
        panel = wx.Panel(self)

        font = wx.SystemSettings.GetFont(wx.SYS_DEFAULT_GUI_FONT)
        font.SetPointSize(10)
        panel.SetFont(font)

        vbox = wx.BoxSizer(wx.VERTICAL)
        self.txtCtrl = wx.ComboBox(panel)

        vbox.Add(self.txtCtrl, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)
