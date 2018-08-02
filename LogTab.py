import tkinter as tk
from tkinter import *
from tkinter import ttk
from RealtimeDataProvider import *
from LogController import *
from LogWriter import *
from tkinter import messagebox
from LogGraph import *


class LogTab(tk.Frame):

    CONST_NAME = "Log"

    def __init__(self, cls):
        tk.Frame.__init__(self, cls)
        self._writer = LogWriter()
        self._controller = LogController(self, self._writer)

        log_save_button = Button(self, text="save", command=lambda: self._controller.save())
        log_save_button.pack()

        self._graph = LogGraph(self, None, None)  # TODO

    @staticmethod
    def info_written(filename: str):
        messagebox.showinfo('Info', 'Log saved to "' + filename + '".')
