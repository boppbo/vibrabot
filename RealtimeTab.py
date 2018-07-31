import tkinter as tk
from tkinter import *
from tkinter import ttk
from RealtimeDataProvider import *


class RealtimeTab(tk.Frame):

    def __init__(self, cls):
        tk.Frame.__init__(self, cls)
        # super(RealtimeTab, self).__init__(cls)
        self._name = "Realtime Analysis"
        self._provider = RealtimeDataProvider("COM15")

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

        self._ir_sensor_label = [0 for x in range(RealtimeDataProvider.ir_sensor_count)]
        self._ir_led_button = [0 for x in range(RealtimeDataProvider.ir_sensor_count)]

        for ir_label in range(RealtimeDataProvider.ir_sensor_count):
            self._ir_sensor_label[ir_label] = Label(self, text="-", borderwidth="2")
            self._ir_sensor_label[ir_label].place(x=10 + ir_label * 50, y=120)

        for ir_button in range(RealtimeDataProvider.ir_sensor_count):
            self._ir_led_button[ir_button] = Button(self, text="OK", command=lambda arg=ir_button: text_mod(arg))
            self._ir_led_button[ir_button].place(x=10 + ir_button * 50, y=150)

        Label(self, text="Object :", borderwidth="2").place(x=10, y=210)

        self._object_temperature_label = Label(self, text="0C", borderwidth="2")
        self._object_temperature_label.place(x=60, y=210)  # Anordnung durch Place-Manager

        Label(self, text="Ambient :", borderwidth="2").place(x=120, y=210)

        self._ambient_temperature_label = Label(self, text="0C", borderwidth="2")
        self._ambient_temperature_label.place(x=170, y=210)  # Anordnung durch Place-Manager

    def get_name(self):
        return self._name

    def update(self):
        tk.Frame.update(self)
        vibrabot_data = self._provider.get_data()
        self._left_light_sensor_label.config(text=str(vibrabot_data.get_left_light_sensor()))
        self._right_light_sensor_label.config(text=str(vibrabot_data.get_right_light_sensor()))

        self._microphone_label.config(text=str(vibrabot_data.get_microphone_value()))

        for ir_sensor in range(RealtimeDataProvider.ir_sensor_count):
            self._ir_sensor_label[ir_sensor].config(text=str(vibrabot_data.get_ir_sensor(ir_sensor)))

        for ir_sensor in range(RealtimeDataProvider.ir_sensor_count):

            if vibrabot_data.get_ir_sensor_status(ir_sensor):
                self._ir_led_button[ir_sensor].config(text="on")
            else:
                self._ir_led_button[ir_sensor].config(text="off")

            self._object_temperature_label.config(text=round((vibrabot_data.get_object_temperature() * 0.02 - 273.15), 2))
            self._ambient_temperature_label.config(text=round((vibrabot_data.get_ambient_temperature() * 0.02 - 273.15), 2))


RealtimeDataProvider("COM15")