import tkinter as tk
from tkinter import ttk
from remoteapp.gui.graph import Graph
from remoteapp.services.vibrabotcommunication import VibraBotCommunication


class RealtimeTab(tk.Frame):

    CONST_NAME = "Realtime Analysis"

    def __init__(self, parent, commService: VibraBotCommunication):
        tk.Frame.__init__(self, parent)

        self.com = commService

        self.config = commService.read_config()
        self.com.start_live_data()

        self.graph = Graph(self, self.config)

    def refresh(self):
        self.com.read_live_data_entry(self.config)
        self.graph.plot(self.config)
