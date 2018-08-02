import tkinter as tk
import serial
from tkinter import *
from tkinter import ttk
from RealtimeDataProvider import *
from remoteapp.services.vibrabotcommunication import VibraBotCommunication
from remoteapp.model.sensor import Sensor


class ConfigTab(tk.Frame):

    CONST_NAME = "Config"

    def __init__(self, cls, com: VibraBotCommunication):
        tk.Frame.__init__(self, cls)

        values = list(range(0, 65000, 10))

        # self.config = com.read_config() TODO
        self.config = [
            Sensor(0, "c", 30, "Foo", [190, 190, 191]),
            Sensor(1, "s", 50, "Bar", [43981])
        ]

        row = 0

        header = Label(self, text="Interval, 0 to 65000")
        header.grid(row=row, column=1, padx=4, pady=4, sticky="W")

        row += 1

        for i in self.config:
            label = Label(self, text=i.label)
            label.grid(row=row, column=0, sticky="W",  padx=4, pady=4)
            var = StringVar()
            spinbox = Spinbox(self, textvariable=var, values=values, justify=RIGHT)
            var.set(i.interval)
            spinbox.grid(row=row, column=1, padx=4, pady=4, sticky="WE")
            row += 1

        button_save = Button(self, text="save", command=lambda: self.save())
        button_save.grid(row=row, column=1, sticky="WE", padx=4, pady=4)

        row += 1

    def save(self):
        print("click")


if __name__ == '__main__':
    w = Tk()
    ConfigTab(None, w).pack()
    w.mainloop()
