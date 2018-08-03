import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import font
from RealtimeDataProvider import *
from RealtimeGraph import *
from RealtimeGraphData import *
from RealtimeController import *
from remoteapp.services.colors import *
import serial


class RealtimeTab(tk.Frame):

    CONST_NAME = "Realtime Analysis"

    def __init__(self, parent, ser: serial.Serial):
        tk.Frame.__init__(self, parent)

        self.i = 0
        self.graph_data = RealtimeGraphData()
        self.controller = RealtimeController()

        self._provider = RealtimeDataProvider(ser)

        # self._frame_upper = Frame(self, relief=RAISED, borderwidth=1).pack()

        row = 0

        self._check_light_left = Checkbutton(self, text="Left Light Sensor:", borderwidth=2, fg=Colors.CONST_COLOR_LIGHT_LEFT, variable=self.controller.light_left)
        self._check_light_left.grid(row=row, column=0, sticky="W")

        self._left_light_sensor_value = Label(self, text="-1", borderwidth="2")
        self._left_light_sensor_value.grid(row=row, column=1, sticky="E")

        row += 1

        self._check_light_right = Checkbutton(self, text="Right Light Sensor:", borderwidth=2, fg=Colors.CONST_COLOR_LIGHT_RIGHT, variable=self.controller.light_right)
        self._check_light_right.grid(row=row, column=0, sticky="W")

        self._right_light_sensor_value = Label(self, text="-1", borderwidth="2")
        self._right_light_sensor_value.grid(row=row, column=1, sticky="E")

        row += 1

        self._check_mic = Checkbutton(self, text="Microphone:", fg=Colors.CONST_COLOR_MIC, variable=self.controller.mic)
        self._check_mic.grid(row=row, column=0, sticky="W")

        self._microphone_label = Label(self, text="-1", borderwidth="2")
        self._microphone_label.grid(row=row, column=1, sticky="E")

        row += 1

        # self._label_ir = Label(self, text="Ir Sensors", borderwidth="2")
        # self._label_ir.place(x=60, y=10)  # Anordnung durch Place-Manager

        self._ir_sensor_check = [0 for x in range(RealtimeDataProvider.CONST_SENSOR_IR_COUNT)]
        self._ir_sensor_label = [0 for x in range(RealtimeDataProvider.CONST_SENSOR_IR_COUNT)]

        for ir_label in range(RealtimeDataProvider.CONST_SENSOR_IR_COUNT):

            self._ir_sensor_check[ir_label] = Checkbutton(self, text="IR Sensor " + str(ir_label + 1) + ":", fg=Colors.CONST_COLOR_IR[ir_label], variable=self.controller.ir[ir_label])
            self._ir_sensor_check[ir_label].grid(row=row, column=0, sticky="W")

            self._ir_sensor_label[ir_label] = Label(self, text="-1", borderwidth="2")
            self._ir_sensor_label[ir_label].grid(row=row, column=1, sticky="E")

            row += 1

        self._temp_obj_label = Checkbutton(self, text="Object Temperature:", fg=Colors.CONST_COLOR_TMP_OBJ, variable=self.controller.tmp_obj)
        self._temp_obj_label.grid(row=row, column=0, sticky="W")

        self._temp_obj_val = Label(self, text="-1", borderwidth="2")
        self._temp_obj_val.grid(row=row, column=1, sticky="E")

        row += 1

        self._temp_amb_label = Checkbutton(self, text="Ambient Temperature:", fg=Colors.CONST_COLOR_TMP_AMB, variable=self.controller.tmp_amb)
        self._temp_amb_label.grid(row=row, column=0, sticky="W")

        self._temp_amb_val = Label(self, text="-1", borderwidth="2")
        self._temp_amb_val.grid(row=row, column=1, sticky="E")

        row += 1

        self._box = Frame(self, relief=RAISED, borderwidth=1)
        self._box.grid(row=0, rowspan=row, column=2)
        self._graph = Graph(self._box, self.graph_data, self.controller)

    def update(self):
        tk.Frame.update(self)
        vibrabot_data = self._provider.get_data()
        if self.i % 100 is 0:
            self.graph_data.add(vibrabot_data)
            # self._data.append(vibrabot_data)
        self._left_light_sensor_value.config(text=str(vibrabot_data.get_left_light_sensor()))
        self._right_light_sensor_value.config(text=str(vibrabot_data.get_right_light_sensor()))

        self._microphone_label.config(text=str(vibrabot_data.get_microphone_value()))

        for ir_sensor in range(RealtimeDataProvider.CONST_SENSOR_IR_COUNT):
            self._ir_sensor_label[ir_sensor].config(text=str(vibrabot_data.get_ir_sensor(ir_sensor)))

        self._temp_obj_val.config(text=round((vibrabot_data.get_object_temperature() * 0.02 - 273.15), 2))
        self._temp_amb_val.config(text=round((vibrabot_data.get_ambient_temperature() * 0.02 - 273.15), 2))

        if self.i % 100 is 0:
            self._graph.plot()
            # self._graph.plot(self._data)

        self.i += 1
