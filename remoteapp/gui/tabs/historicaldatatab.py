import time, csv
import tkinter as tk
import tkinter.ttk
from typing import List
from tkinter import messagebox
from remoteapp.model.sensor import Sensor
from remoteapp.services.datapersistency import CsvLogWriter, CsvSerializer
from remoteapp.services.vibrabotcommunication import VibraBotCommunication
from remoteapp.gui.graph import Graph

class HistoricalDataController:
    def __init__(self, commService: VibraBotCommunication,  view):
        self._view = view
        self._writer = CsvLogWriter(commService.read_config(), CsvSerializer())

        self._data = commService.read_config()
        commService.read_data(self._data)
        self._view.updateAllData(self._data)


    def save(self):
        path = tk.filedialog.asksaveasfilename(
            initialdir = "~",
            initialfile = time.strftime(CsvLogWriter.CONST_FILENAME),
            defaultextension = CsvLogWriter.CONST_EXTENSION,
            filetypes = ( ("Comma separated value", "*.csv"), ("All Files", "*.*") ) )

        if len(path) > 0:
            self._writer.export(path, self._data)
            self._view.info_written(path)
    def open(self):
        path = tk.filedialog.askopenfilename(
            initialdir = "~",
            filetypes = ( ("Comma separated value", "*.csv"), ("All Files", "*.*") ) )
        
        if len(path) > 0:
            self._data = self._writer.import_(path)
            self._view.updateAllData(self._data)


class HistoricalDataTab(tk.Frame):
    CONST_NAME = "Log"
    
    def __init__(self, cls, commService: VibraBotCommunication):
        tk.Frame.__init__(self, cls)

        log_open_button = tk.Button(self, text="open", command=lambda: self._controller.open())
        log_open_button.grid(row=0, column=0, sticky="WE")

        log_save_button = tk.Button(self, text="save", command=lambda: self._controller.save())
        log_save_button.grid(row=0, column=1, sticky="WE")

        frame = tk.Frame(self)
        self.log_graph = Graph(frame, commService.read_config())
        frame.grid(row=1, column=0, columnspan=2)

        self._controller = HistoricalDataController(commService, self)


    def info_written(self, filename: str):
        messagebox.showinfo('Info', 'Log saved to "' + filename + '".')

    def updateAllData(self, config: List[Sensor]):
        self.log_graph.plot(config)
