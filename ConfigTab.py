import tkinter as tk
from tkinter import *
from tkinter import ttk
from RealtimeDataProvider import *


class ConfigTab(tk.Frame):

    CONST_NAME = "Config"

    def __init__(self, cls):
        tk.Frame.__init__(self, cls)

        self._label = Label(self, text="Hier koennte Ihre Werbung stehen", borderwidth="2")
        self._label.place(x=60, y=210)
