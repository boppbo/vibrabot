import time, csv
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, Button
from remoteapp.services.datapersistency import CsvLogWriter, CsvSerializer

class LogController:
    def __init__(self, view):
        self._view = view
        self._writer = CsvLogWriter(CsvSerializer())
    def save(self):
        filename = self._writer.export(None)
        self._view.info_written(filename)


class LogTab(tk.Frame):
    CONST_NAME = "Log"
    
    def __init__(self, cls):
        tk.Frame.__init__(self, cls)

        self._controller = LogController(self)
        log_save_button = Button(self, text="save", command=lambda: self._controller.save())
        log_save_button.pack()

        #self._graph = LogGraph(self, None, None)  # TODO
    def info_written(self, filename: str):
        messagebox.showinfo('Info', 'Log saved to "' + filename + '".')