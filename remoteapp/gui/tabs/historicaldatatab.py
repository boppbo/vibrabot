import time, csv
import tkinter as tk
import serial
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox, Button
from remoteapp.services.datapersistency import CsvLogWriter, CsvSerializer
from remoteapp.services.portdetector import PortDetector
from remoteapp.services.vibrabotcommunication import VibraBotCommunication

class HistoricalDataController:
    def __init__(self, serial: serial.Serial,  view):
        self._view = view
        self._writer = CsvLogWriter(CsvSerializer())

        commService = VibraBotCommunication(serial)
        #config = commService.read_config()

    def save(self):
        path = filedialog.asksaveasfilename(
            initialdir = "~",
            initialfile = time.strftime(CsvLogWriter.CONST_FILENAME),
            defaultextension = CsvLogWriter.CONST_EXTENSION,
            filetypes = ( ("Comma separated value", "*.csv"), ("All Files", "*.*") ) )

        self._writer.export(path, None)
        self._view.info_written(path)


class HistoricalDataTab(tk.Frame):
    CONST_NAME = "Log"
    
    def __init__(self, cls, ser: serial.Serial):
        tk.Frame.__init__(self, cls)

        self._controller = HistoricalDataController(ser, self)
        log_save_button = Button(self, text="save", command=lambda: self._controller.save())
        log_save_button.pack()

        #self._graph = LogGraph(self, None, None)  # TODO
    def info_written(self, filename: str):
        messagebox.showinfo('Info', 'Log saved to "' + filename + '".')