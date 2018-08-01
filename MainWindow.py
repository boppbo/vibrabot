import tkinter as tk
from tkinter import *
from tkinter import ttk
from RealtimeTab import *
from ConfigTab import *
from LogTab import *
from remoteapp.Services.PortDetector import *

# https://smallguysit.com/index.php/2017/03/15/python-tkinter-create-tabs-notebook-widget/


class MainWindow(tk.Tk):

    CONST_TITLE = "insert window title here"
    CONST_SIZE = "1300x700"

    def __init__(self):
        tk.Tk.__init__(self)

        port = PortDetector.detect_port()
        if port is None:
            messagebox.showerror('Error', 'Can\'t find port for device "' + PortDetector.CONST_DEVICE_NAME + '".')
            exit(0)

        self.title(MainWindow.CONST_TITLE)
        self.geometry(MainWindow.CONST_SIZE)
        self.nb = ttk.Notebook(self)
        self.nb.grid(row=1, column=0, columnspan=50, rowspan=49, sticky="NESW")

        # gives weight to the cells in the grid
        rows = 0
        while rows < 50:
            self.rowconfigure(rows, weight=1)
            self.columnconfigure(rows, weight=1)
            rows += 1

        self.realt_tab = RealtimeTab(self.nb, port)
        self.nb.add(self.realt_tab, text=RealtimeTab.CONST_NAME)

        self.confg_tab = ConfigTab(self.nb)
        self.nb.add(self.confg_tab, text=ConfigTab.CONST_NAME)

        self.log_tab = LogTab(self.nb)
        self.nb.add(self.log_tab, text=LogTab.CONST_NAME)

        while 1:
            try:
                self.update_idletasks()
                self.update()
                self.realt_tab.update()
            except TclError:
                exit(0)


app = MainWindow()
