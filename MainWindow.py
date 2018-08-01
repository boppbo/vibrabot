import tkinter as tk
from tkinter import *
from tkinter import ttk
from RealtimeTab import *
from ConfigTab import *

# https://smallguysit.com/index.php/2017/03/15/python-tkinter-create-tabs-notebook-widget/


class MainWindow(tk.Tk):

    CONST_TITLE = "insert window title here"
    CONST_SIZE = "1024x768"

    def __init__(self):
        tk.Tk.__init__(self)
        super().title(MainWindow.CONST_TITLE)
        super().geometry(MainWindow.CONST_SIZE)
        self.nb = ttk.Notebook(self)
        self.nb.grid(row=1, column=0, columnspan=50, rowspan=49, sticky="NESW")

        # gives weight to the cells in the grid
        rows = 0
        while rows < 50:
            self.rowconfigure(rows, weight=1)
            self.columnconfigure(rows, weight=1)
            rows += 1

        self.realt_tab = RealtimeTab(self.nb)
        self.nb.add(self.realt_tab, text=self.realt_tab.get_name())

        self.confg_tab = ConfigTab(self.nb)
        self.nb.add(self.confg_tab, text=self.confg_tab.get_name())

        while 1:
            self.update_idletasks()
            self.update()
            self.realt_tab.update()


    """
    def update(self):
        while 1:
            tk.Tk.update(self, n)
            self.page1.update()

    def update_idletasks(self):
        while 1:
            tk.TK.update_idletasks(self)
            self.page1.update()
            """


app = MainWindow()
app.mainloop()
