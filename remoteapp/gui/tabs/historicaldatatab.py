import time, csv
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox, Button
from remoteapp.model.sensor import Sensor
from remoteapp.services.datapersistency import CsvLogWriter, CsvSerializer
from remoteapp.services.vibrabotcommunication import VibraBotCommunication

class HistoricalDataController:
    def __init__(self, commService: VibraBotCommunication,  view):
        self._view = view
        self._writer = CsvLogWriter(CsvSerializer())

        self._data = commService.read_config()
        commService.read_data(self._data)
        self._view.updateAllData(self._data)

    def save(self):
        path = filedialog.asksaveasfilename(
            initialdir = "~",
            initialfile = time.strftime(CsvLogWriter.CONST_FILENAME),
            defaultextension = CsvLogWriter.CONST_EXTENSION,
            filetypes = ( ("Comma separated value", "*.csv"), ("All Files", "*.*") ) )

        self._writer.export(path, self._data)
        self._view.info_written(path)
    def open(self):
        path = filedialog.askopenfilename(
            initialdir = "~",
            filetypes = ( ("Comma separated value", "*.csv"), ("All Files", "*.*") ) )
        
        self._data = self._writer.import_(path)


class HistoricalDataTab(tk.Frame):
    CONST_NAME = "Log"
    
    def __init__(self, cls, commService: VibraBotCommunication):
        tk.Frame.__init__(self, cls)

        self._controller = HistoricalDataController(commService, self)
        
        log_open_button = Button(self, text="open", command=lambda: self._controller.open())
        log_open_button.pack()

        log_save_button = Button(self, text="save", command=lambda: self._controller.save())
        log_save_button.pack()

    def info_written(self, filename: str):
        messagebox.showinfo('Info', 'Log saved to "' + filename + '".')

    def updateAllData(self, config: List[Sensor] ):
        #self._graph = LogGraph(self, None, None)  # TODO
