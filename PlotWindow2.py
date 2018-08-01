import matplotlib
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *


matplotlib.use('TkAgg')


class PlotWindow2:

    def __init__(self, window):
        self.window = window
        self.box = Entry(window)
        self.button = Button(window, text="check", command=lambda: self.plot(int(self.box.get())))
        self.button_clear = Button(window, text="clear", command=lambda: self.clear())
        self.box.pack()
        self.button.pack()
        self.button_clear.pack()
        self.data = [2, 3, 4]

        fig = Figure(figsize=(6, 6))
        self.a = fig.add_subplot(111)
        self.a.set_title("Estimation Grid", fontsize=16)
        self.a.set_ylabel("Y", fontsize=14)
        self.a.set_xlabel("X", fontsize=14)

        self.canvas = FigureCanvasTkAgg(fig, master=self.window)
        self.canvas.get_tk_widget().pack()
        self.canvas.draw()

    def plot(self, data: int):
        self.data.append(data)
        self.a.clear()
        self.a.set_ylim(0, max(self.data))
        self.a.scatter(np.arange(len(self.data)), self.data, color='red')

        self.canvas.draw()

    def clear(self):
        self.a.clear()
        self.data.clear()
        self.canvas.draw()


if __name__ == '__main__':
    w = Tk()
    start = PlotWindow2(w)
    w.mainloop()
