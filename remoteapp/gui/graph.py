import matplotlib
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *
from VibrabotData import *
from RealtimeGraphData import *
from RealtimeController import *
from typing import List
from remoteapp.model.sensor import *


matplotlib.use('TkAgg')


class Graph:

    CONST_GRAPH_NAME = "log data"
    CONST_XAXIS_NAME = "time [ms]"
    CONST_YAXIS_NAME = "value"
    CONST_YAXIS_MAX = 260
    CONST_COLORS = ["#cccc00",  # left light
                    "#666600",  # right light
                    "#3366ff",  # mic
                    "#d966ff",  # ir 1
                    "#cc33ff",  # ir 2
                    "#bf00ff",  # ir 3
                    "#9900cc",  # ir 4
                    "#730099",  # ir 5
                    "#5cd65c",  # led 1
                    "#33cc33",  # led 2
                    "#29a329",  # led 3
                    "#1f7a1f",  # led 4
                    "#145214",  # led 5
                    "#e60000",  # temp obj
                    "#800000",  # temp amb
                    ]
    CONST_COLOR_DEFAULT = "#000000"

    def __init__(self, master, config: List[Sensor]):
        self.config = config
        self.frame = Frame(master)
        self.frame.pack()
        self.enabled = []
        self.checkboxes = []

        for i in range(len(config)):
            self.enabled.append(BooleanVar())

            self.checkboxes.append(
                Checkbutton(
                    self.frame,
                    text=config[i].label,
                    borderwidth=2,
                    fg=Graph.CONST_COLORS[i],
                    variable=self.enabled[i],
                    command=lambda: self.plot(None)))
            self.checkboxes[i].grid(row=i, column=0, sticky="W")

            self.enabled[i].set(config[i].interval != 0)

        fig = Figure(figsize=(12, 4))
        self.ax = fig.add_subplot(111)
        self.ax.set_title(Graph.CONST_GRAPH_NAME, fontsize=16)
        self.ax.set_xlabel(Graph.CONST_XAXIS_NAME, fontsize=14)
        self.ax.set_ylabel(Graph.CONST_YAXIS_NAME, fontsize=14)

        self.canvas = FigureCanvasTkAgg(fig, master=self.frame)
        self.canvas.get_tk_widget().grid(row=0, rowspan=len(config), column=1)
        self.canvas.draw()

    def plot(self, config: List[Sensor]):

        if config is not None:
            self.config = config
            #for i in range(len(config)):
            #    self.checkboxes[i].config(state=None if config[i].interval != 0 else DISABLED)
            for i in range(len(config)):                
                self.enabled[i].set(config[i].interval != 0)

        config = self.config
        self.clear()

        for i in range(len(config)):
            if i > len(Graph.CONST_COLORS):
                config[i].color = Graph.CONST_COLOR_DEFAULT
            else:
                config[i].color = Graph.CONST_COLORS[i]

        self.ax.set_ylim(-5, Graph.CONST_YAXIS_MAX)

        max_x = 0

        for conf in config:

            if conf.interval * len(conf.values) > max_x:
                max_x = conf.interval * len(conf.values)

        self.ax.set_xlim(0, max_x, 100)

        for i in range(len(config)):
            values = []
            for val in range(len(self.config[i].values)):
                values.append(self.config[i][val][2])

            if self.enabled[i].get() and len(config[i].values):
                self.ax.plot(
                    np.arange(0, config[i].interval * len(config[i].values), config[i].interval),
                    values,
                    color=config[i].color)

        self.ax.set_title(Graph.CONST_GRAPH_NAME, fontsize=16)
        self.ax.set_xlabel(Graph.CONST_XAXIS_NAME, fontsize=14)
        self.ax.set_ylabel(Graph.CONST_YAXIS_NAME, fontsize=14)

        self.canvas.draw()

    def clear(self):
        self.ax.clear()
        # self.canvas.draw()
