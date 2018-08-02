import matplotlib
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *
from VibrabotData import *
from RealtimeGraphData import *
from RealtimeController import *


matplotlib.use('TkAgg')


class LogGraph:

    CONST_GRID_NAME = "insert grid name here"  # TODO
    CONST_XAXIS_NAME = "X"  # TODO
    CONST_YAXIS_NAME = "Y"  # TODO
    CONST_YAXIS_MAX = 250

    def __init__(self, master, graph_data, controller: RealtimeController):
        fig = Figure(figsize=(12, 4))
        self.data = graph_data
        self.controller = controller
        self.ax = fig.add_subplot(111)
        self.ax.set_title(LogGraph.CONST_GRID_NAME, fontsize=16)
        self.ax.set_xlabel(LogGraph.CONST_XAXIS_NAME, fontsize=14)
        self.ax.set_ylabel(LogGraph.CONST_YAXIS_NAME, fontsize=14)

        self.canvas = FigureCanvasTkAgg(fig, master=master)
        self.canvas.get_tk_widget().pack()
        self.canvas.draw()

    def plot(self):
        self.controller
        None  # TODO
