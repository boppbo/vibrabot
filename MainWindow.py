import tkinter as tk
from tkinter import *
from tkinter import ttk
from RealtimeTab import *

# https://smallguysit.com/index.php/2017/03/15/python-tkinter-create-tabs-notebook-widget/


class MainWindow(tk.Tk):

    title = "insert window title here"

    def __init__(self):
        tk.Tk.__init__(self)
        super().title(MainWindow.title)
        super().geometry("500x500")
        self.nb = ttk.Notebook(self)
        self.nb.grid(row=1, column=0, columnspan=50, rowspan=49, sticky="NESW")

        # gives weight to the cells in the grid
        rows = 0
        while rows < 50:
            self.rowconfigure(rows, weight=1)
            self.columnconfigure(rows, weight=1)
            rows += 1

        self.page1 = RealtimeTab(self.nb)
        self.nb.add(self.page1, text=self.page1.get_name())

        self.page2 = tk.Frame(self.nb)
        self.nb.add(self.page2, text="Tab2")

        self.after(1, self.page1.update)



        while 1:
            self.update_idletasks()
            self.update()
            self.page1.update() 


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
