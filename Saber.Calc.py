import wx


class MyFrame(wx.Frame):  # Создан класс с наследованием wx.Frame
    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(300, 300))
        panel = wx.Panel(self)  # Создана панель

        font = wx.SystemSettings.GetFont(wx.SYS_DEFAULT_GUI_FONT)  # Изменен размера шрифта
        font.SetPointSize(10)
        panel.SetFont(font)

        vbox = wx.BoxSizer(wx.VERTICAL)  # Создан вертикальный сайзер
        self.txtCtrl = wx.ComboBox(panel)  # Создано поле ввода
        vbox.Add(self.txtCtrl, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        gbox = wx.GridSizer(5, 4, 5, 5)
        gbox.AddMany([(wx.Button(panel, label='C'), wx.ID_ANY, wx.EXPAND),  # Создание кнопок
                      (wx.StaticText(panel), wx.EXPAND),
                      (wx.Button(panel, label='<-'), wx.ID_ANY, wx.EXPAND),
                      (wx.Button(panel, label='Close'), wx.ID_ANY, wx.EXPAND),
                      (wx.Button(panel, label='7'), wx.ID_ANY, wx.EXPAND),
                      (wx.Button(panel, label='8'), wx.ID_ANY, wx.EXPAND),
                      (wx.Button(panel, label='9'), wx.ID_ANY, wx.EXPAND),
                      (wx.Button(panel, label='/'), wx.ID_ANY, wx.EXPAND),
                      (wx.Button(panel, label='4'), wx.ID_ANY, wx.EXPAND),
                      (wx.Button(panel, label='5'), wx.ID_ANY, wx.EXPAND),
                      (wx.Button(panel, label='6'), wx.ID_ANY, wx.EXPAND),
                      (wx.Button(panel, label='*'), wx.ID_ANY, wx.EXPAND),
                      (wx.Button(panel, label='1'), wx.ID_ANY, wx.EXPAND),
                      (wx.Button(panel, label='2'), wx.ID_ANY, wx.EXPAND),
                      (wx.Button(panel, label='3'), wx.ID_ANY, wx.EXPAND),
                      (wx.Button(panel, label='-'), wx.ID_ANY, wx.EXPAND),
                      (wx.Button(panel, label='0'), wx.ID_ANY, wx.EXPAND),
                      (wx.Button(panel, label='.'), wx.ID_ANY, wx.EXPAND),
                      (wx.Button(panel, label='='), wx.ID_ANY, wx.EXPAND),
                      (wx.Button(panel, label='+'), wx.ID_ANY, wx.EXPAND)])
        vbox.Add(gbox, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        panel.SetSizer(vbox)
        self.Bind(wx.EVT_BUTTON, self.OnClicked)  # Создана связь кнопка c функцией

    # Создана функция для нажатий кнопок
    def OnClicked(self, evt):
        label = evt.GetEventObject().GetLabel()

        if label == '=':
            compute = self.txtCtrl.GetValue()  # Выражение берется из поля ввода
            if not compute.strip():
                return

            result = eval(compute)  # Подсчитывается полученное выражение
            self.txtCtrl.Insert(compute, 0)
            self.txtCtrl.SetValue(str(result))

        elif label == 'C':
            self.txtCtrl.SetValue("")  # Удаляется вся строка все
        elif label == '<-':
            self.txtCtrl.SetValue(self.txtCtrl.GetValue()[:-1])  # Чистим последний символ в string
        elif label == 'Close':
            frame.Destroy()  # Закрывается окно
        else:
            self.txtCtrl.SetValue(self.txtCtrl.GetValue() + label)


# Создание окна
app = wx.App()
frame = MyFrame(None, 'Saber.Calc')
frame.Show()
app.MainLoop()

