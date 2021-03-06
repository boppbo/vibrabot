import tkinter as tk
from tkinter import ttk
from remoteapp.gui.tabs.configtab import ConfigTab
from remoteapp.gui.tabs.historicaldatatab import HistoricalDataTab
from remoteapp.services.connection import ConnectionFactory
from remoteapp.services.vibrabotcommunication import VibraBotCommunication

# https://smallguysit.com/index.php/2017/03/15/python-tkinter-create-tabs-notebook-widget/
class MainWindow(tk.Tk):
    CONST_TITLE = "Vibrabot remoteapp"

    def __init__(self):
        tk.Tk.__init__(self)

        connFactory = ConnectionFactory()
        port = connFactory.detect_port()
        if port is None:
            tk.messagebox.showerror('Error', 'Can\'t find port for device "' + ConnectionFactory.CONST_DEVICE_NAME + '".')
            exit(0)
        com = VibraBotCommunication(connFactory.open_connection(port))

        self.title(MainWindow.CONST_TITLE)
        self.nb = ttk.Notebook(self)
        self.nb.grid(row=1, column=0, columnspan=50, rowspan=49, sticky="NESW")

        # gives weight to the cells in the grid
        rows = 0
        while rows < 50:
            self.rowconfigure(rows, weight=1)
            self.columnconfigure(rows, weight=1)
            rows += 1

        self.log_tab = HistoricalDataTab(self.nb, com)
        self.nb.add(self.log_tab, text=HistoricalDataTab.CONST_NAME)

        self.confg_tab = ConfigTab(self.nb, com)
        self.nb.add(self.confg_tab, text=ConfigTab.CONST_NAME)

        self.mainloop()
