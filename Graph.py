import matplotlib
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *
from VibrabotData import *


matplotlib.use('TkAgg')


class Graph:

    CONST_GRID_NAME = "Estimation Grid"
    CONST_XAXIS_NAME = "X"
    CONST_YAXIS_NAME = "Y"

    def __init__(self, master):
        fig = Figure(figsize=(4, 4))
        self.ax = fig.add_subplot(111)
        self.ax.set_title(Graph.CONST_GRID_NAME, fontsize=16)
        self.ax.set_xlabel(Graph.CONST_XAXIS_NAME, fontsize=14)
        self.ax.set_ylabel(Graph.CONST_YAXIS_NAME, fontsize=14)

        self.canvas = FigureCanvasTkAgg(fig, master=master)
        self.canvas.get_tk_widget().pack()
        self.canvas.draw()

    def plot(self, vibrabot_data: VibrabotData):
        self.ax.clear()
        self.ax.set_ylim(0, max(date.get_microphone_value() for date in vibrabot_data))
        array = []
        for date in vibrabot_data:
            array.append(date.get_microphone_value())
        self.ax.scatter(np.arange(len(vibrabot_data)), array, color="red")

        self.canvas.draw()

    def clear(self):
        self.ax.clear()
        self.canvas.draw()


if __name__ == '__main__':
    w = Tk()
    g = Graph(w)
    w.mainloop()
    g.add(VibrabotData())
