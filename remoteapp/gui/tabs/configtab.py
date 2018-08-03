import tkinter as tk
from remoteapp.services.vibrabotcommunication import VibraBotCommunication
from remoteapp.model.sensor import Sensor

class ConfigTab(tk.Frame):

    CONST_NAME = "Config"
    _allowed_interval_values = list(range(0, 65000, 10))

    def __init__(self, cls, commService: VibraBotCommunication):
        tk.Frame.__init__(self, cls)

        self._commService = commService
        self._config = commService.read_config()

        
        row = 0

        header = tk.Label(self, text="Decimal Interval from 0 to 65000 in ms, must be divisible by 10")
        header.grid(row=row, column=1, padx=4, pady=4, sticky="W")
        row += 1

        for sensor in self._config:
            label = tk.Label(self, text=sensor.label)
            label.grid(row=row, column=0, sticky="W",  padx=4, pady=4)
            
            sensor.var = tk.IntVar()
            spinbox = tk.Spinbox(self, textvariable=sensor.var, values=ConfigTab._allowed_interval_values, justify=tk.RIGHT)
            sensor.var.set(sensor.interval)
            
            spinbox.grid(row=row, column=1, padx=4, pady=4, sticky="WE")
            row += 1

        button_save = tk.Button(self, text="save", command=lambda: self.save())
        button_save.grid(row=row, column=1, sticky="WE", padx=4, pady=4)
        row += 1

    def save(self):
        for sensor in self._config:
            sensor.interval = sensor.var.get()
        
        self._commService.write_config(self._config)
        tk.messagebox.showinfo("Werte geschrieben", "Der Vibrabot wurde konfiguriert")