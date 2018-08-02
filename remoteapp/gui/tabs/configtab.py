import tkinter as tk
import serial
from tkinter import *
from tkinter import ttk
from RealtimeDataProvider import *


class ConfigTab(tk.Frame):

    CONST_NAME = "Config"

    def __init__(self, cls, ser: serial.Serial):
        tk.Frame.__init__(self, cls)

        label_name = Label(self, text="Name: ")
        label_name.grid(row=0, column=0)

        label_name_val = Label(self, text="Insert Device Name Here")  # TODO name
        label_name_val.grid(row=0, column=1)

        label_interval = Label(self, text="Interval: ")
        label_interval.grid(row=1, column=0)

        # registering validation command
        validate_interval = (cls.register(self._validate_interval), '%P', '%S', '%W')

        values = list(range(0, 65000, 10))
        # spinbox_interval = Spinbox(self, values=values, validate='all', validatecommand=validate_interval)
        spinbox_interval = Spinbox(self, values=values, validate='all', validatecommand=validate_interval)
        # TODO from, to
        spinbox_interval.grid(row=1, column=1)

    @staticmethod
    def _validate_interval(user_input, new_value, widget_name):
        print("sfsa")
        return S == '' or S.isdigit()



if __name__ == '__main__':
    w = Tk()
    ConfigTab(None, w).pack()
    w.mainloop()
