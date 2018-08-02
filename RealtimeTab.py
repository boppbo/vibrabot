import tkinter as tk
from tkinter import *
from tkinter import ttk
from RealtimeDataProvider import *
from RealtimeGraph import *
from RealtimeGraphData import *
from RealtimeController import *


class RealtimeTab(tk.Frame):

    CONST_NAME = "Realtime Analysis"

    def __init__(self, parent, port):
        tk.Frame.__init__(self, parent)

        self.i = 0
        self.graph_data = RealtimeGraphData()
        self.controller = RealtimeController()

        self._provider = RealtimeDataProvider(port)

        self._label_light = Label(self, text="Light", borderwidth="2")
        self._label_light.place(x=60, y=10)  # Anordnung durch Place-Manager

        self._left_light_sensor_label = Label(self, text="Hallo Welt!", borderwidth="2")
        self._left_light_sensor_label.place(x=10, y=30)  # Anordnung durch Place-Manager

        self._right_light_sensor_label = Label(self, text="Hallo Welt2!", borderwidth="2")
        self._right_light_sensor_label.place(x=100, y=30)  # Anordnung durch Place-Manager

        self._label_mic = Label(self, text="microphone", borderwidth="2")
        self._label_mic.place(x=10, y=60)  # Anordnung durch Place-Manager

        self._microphone_label = Label(self, text="Hallo Welt2!", borderwidth="2")
        self._microphone_label.place(x=100, y=60)  # Anordnung durch Place-Manager

        self._label_ir = Label(self, text="Ir Sensors", borderwidth="2")
        self._label_ir.place(x=60, y=10)  # Anordnung durch Place-Manager

        self._ir_sensor_label = [0 for x in range(RealtimeDataProvider.CONST_SENSOR_IR_COUNT)]
        self._ir_led_button = [0 for x in range(RealtimeDataProvider.CONST_SENSOR_IR_COUNT)]

        for ir_label in range(RealtimeDataProvider.CONST_SENSOR_IR_COUNT):
            self._ir_sensor_label[ir_label] = Label(self, text="-", borderwidth="2")
            self._ir_sensor_label[ir_label].place(x=10 + ir_label * 50, y=120)

        for ir_button in range(RealtimeDataProvider.CONST_SENSOR_IR_COUNT):
            self._ir_led_button[ir_button] = Button(self, text="OK", command=lambda arg=ir_button: text_mod(arg))
            self._ir_led_button[ir_button].place(x=10 + ir_button * 50, y=150)

        Label(self, text="Object :", borderwidth="2").place(x=10, y=210)

        self._object_temperature_label = Label(self, text="0C", borderwidth="2")
        self._object_temperature_label.place(x=60, y=210)  # Anordnung durch Place-Manager

        Label(self, text="Ambient :", borderwidth="2").place(x=120, y=210)

        self._ambient_temperature_label = Label(self, text="0C", borderwidth="2")
        self._ambient_temperature_label.place(x=170, y=210)  # Anordnung durch Place-Manager

        self._check_mic = Checkbutton(self, text="microphone", variable=self.controller.mic)
        self._check_mic.place(x=200, y=100)

        self._check_mic = Checkbutton(self, text="light left", variable=self.controller.light_left)
        self._check_mic.place(x=200, y=10)

        self._check_mic = Checkbutton(self, text="light right", variable=self.controller.light_right)
        self._check_mic.place(x=200, y=40)

        self._box = Frame(self, relief=RAISED, borderwidth=1)
        self._box.place(x=0, y=200)
        self._graph = Graph(self._box, self.graph_data, self.controller)

    def update(self):
        tk.Frame.update(self)
        vibrabot_data = self._provider.get_data()
        if self.i % 100 is 0:
            self.graph_data.add(vibrabot_data)
            # self._data.append(vibrabot_data)
        self._left_light_sensor_label.config(text=str(vibrabot_data.get_left_light_sensor()))
        self._right_light_sensor_label.config(text=str(vibrabot_data.get_right_light_sensor()))

        self._microphone_label.config(text=str(vibrabot_data.get_microphone_value()))

        for ir_sensor in range(RealtimeDataProvider.CONST_SENSOR_IR_COUNT):
            self._ir_sensor_label[ir_sensor].config(text=str(vibrabot_data.get_ir_sensor(ir_sensor)))

        for ir_sensor in range(RealtimeDataProvider.CONST_SENSOR_IR_COUNT):

            if vibrabot_data.get_ir_sensor_status(ir_sensor):
                self._ir_led_button[ir_sensor].config(text="on")
            else:
                self._ir_led_button[ir_sensor].config(text="off")

            self._object_temperature_label.config(text=round((vibrabot_data.get_object_temperature() * 0.02 - 273.15), 2))
            self._ambient_temperature_label.config(text=round((vibrabot_data.get_ambient_temperature() * 0.02 - 273.15), 2))

        if self.i % 100 == 0:
            self._graph.plot()
            # self._graph.plot(self._data)

        self.i += 1
