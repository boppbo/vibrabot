import matplotlib
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *
from VibrabotData import *
from RealtimeGraphData import *
from RealtimeController import *
from remoteapp.services.colors import *


matplotlib.use('TkAgg')


class Graph:

    CONST_GRID_NAME = "insert grid name here"  # TODO
    CONST_XAXIS_NAME = "X"  # TODO
    CONST_YAXIS_NAME = "Y"  # TODO
    CONST_YAXIS_MAX = 260

    def __init__(self, master, graph_data: RealtimeGraphData, controller: RealtimeController):
        fig = Figure(figsize=(12, 4))
        self.data = graph_data
        self.controller = controller
        self.ax = fig.add_subplot(111)
        self.ax.set_title(Graph.CONST_GRID_NAME, fontsize=16)
        self.ax.set_xlabel(Graph.CONST_XAXIS_NAME, fontsize=14)
        self.ax.set_ylabel(Graph.CONST_YAXIS_NAME, fontsize=14)

        self.canvas = FigureCanvasTkAgg(fig, master=master)
        self.canvas.get_tk_widget().pack()
        self.canvas.draw()

    def plot(self):
        self.ax.clear()
        data_light_left = []
        data_light_right = []
        data_mic = []
        data_ir = []
        data_tmp_obj = []
        data_tmp_amb = []
        for i in range(5):
            data_ir.append([])
        for date in self.data.get():
            data_light_left.append(date.get_left_light_sensor())
            data_light_right.append(date.get_right_light_sensor())
            data_mic.append(date.get_microphone_value())
            for i in range(5):
                data_ir[i].append(date.get_ir_sensor(i))
            data_tmp_obj.append(date.get_object_temperature() * 0.02 - 273.15)
            data_tmp_amb.append(date.get_ambient_temperature() * 0.02 - 273.15)

        self.ax.set_ylim(0, Graph.CONST_YAXIS_MAX)
        self.ax.set_xlim(self.data.get_x_min(), max([self.data.get_x_max(), 100]))

        if self.controller.light_left.get():
            self.ax.plot(np.arange(self.data.get_x_min(), self.data.get_x_max()), data_light_left, color=Colors.CONST_COLOR_LIGHT_LEFT)
        if self.controller.light_right.get():
            self.ax.plot(np.arange(self.data.get_x_min(), self.data.get_x_max()), data_light_right, color=Colors.CONST_COLOR_LIGHT_RIGHT)
        if self.controller.mic.get():
            self.ax.plot(np.arange(self.data.get_x_min(), self.data.get_x_max()), data_mic, color='blue')
        for i in range(5):
            if self.controller.ir[i].get():
                self.ax.plot(np.arange(self.data.get_x_min(), self.data.get_x_max()), data_ir[i], color=Colors.CONST_COLOR_IR[i])
        if self.controller.tmp_obj.get():
            self.ax.plot(np.arange(self.data.get_x_min(), self.data.get_x_max()), data_tmp_obj, color=Colors.CONST_COLOR_TMP_OBJ)
        if self.controller.tmp_amb.get():
            self.ax.plot(np.arange(self.data.get_x_min(), self.data.get_x_max()), data_tmp_amb, color=Colors.CONST_COLOR_TMP_AMB)

        self.canvas.draw()

    def clear(self):
        self.ax.clear()
        self.canvas.draw()
