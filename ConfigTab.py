import tkinter as tk
from tkinter import *
from tkinter import ttk
from RealtimeDataProvider import *


class ConfigTab(tk.Frame):

    def __init__(self, cls):
        tk.Frame.__init__(self, cls)
        self._name = "Config"

        self._label = Label(self, text="Hier koennte Ihre Werbung stehen", borderwidth="2")
        self._label.place(x=60, y=210)

    def get_name(self):
        return self._name
