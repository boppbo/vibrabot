import tkinter as tk

from tkinter import *
from tkinter import ttk

from tkinter import messagebox

import serial.tools.list_ports

from VibrabotData import *

import serial

ir_sensor_count = 5

arduino_device_name = 'Arduino LilyPad USB'

global label


def build_window():
    Label(fenster, text="light", borderwidth="2")


def update_window(vibrabot_data):
    left_light_sensor_label.config(text=str(vibrabot_data.get_left_light_sensor()))
    right_light_sensor_label.config(text=str(vibrabot_data.get_right_light_sensor()))

    microphone_label.config(text=str(vibrabot_data.get_microphone_value()))

    for ir_sensor in range(ir_sensor_count):
        ir_sensor_label[ir_sensor].config(text=str(vibrabot_data.get_ir_sensor(ir_sensor)))

    for ir_sensor in range(ir_sensor_count):

        if vibrabot_data.get_ir_sensor_status(ir_sensor):
            ir_led_button[ir_sensor].config(text="on")
        else:
            ir_led_button[ir_sensor].config(text="off")

        object_temperature_label.config(text=round((vibrabot_data.get_object_temperature() * 0.02 - 273.15), 2))
        ambient_temperature_label.config(text=round((vibrabot_data.get_ambient_temperature() * 0.02 - 273.15), 2))


def read_remote_byte():
    token = int(ser.read(1), 16) * 16
    token += int(ser.read(1), 16)
    ser.read(1)

    return token


def read_remote_word():
    token = int(ser.read(1), 16) * 4096
    token += int(ser.read(1), 16) * 256
    token += int(ser.read(1), 16) * 16
    token += int(ser.read(1), 16)
    ser.read(1)

    return token


def decode(vibrabot_data):
    if ser.in_waiting > 1:
        token = ser.read(1)
        # print("token")

        # print(token)
        if token == b'#':
            # if (token == 35):
            # print("serial")

            val = read_remote_byte()
            vibrabot_data.set_left_light_sensor(val)

            val = read_remote_byte()
            vibrabot_data.set_right_light_sensor(val)

            val = read_remote_byte()
            vibrabot_data.set_microphone(val)

            for sensor in range(5):
                val = read_remote_byte()
                vibrabot_data.set_ir_sensor(sensor, val)

            val = read_remote_byte()

            for sensor in range(5):
                if val & (1 << sensor):
                    vibrabot_data.set_ir_sensor_status(sensor, True)
                else:
                    vibrabot_data.set_ir_sensor_status(sensor, False)

            val = read_remote_word()
            vibrabot_data.set_object_temperature(val)

            val = read_remote_word()
            vibrabot_data.set_ambient_temperature(val)

    fenster.update_idletasks()
    fenster.update()


def text_mod(arg):
    ir_sensor = arg

    arg = arg + 48

    byte1 = arg.to_bytes(1, byteorder='big')

    if data.get_ir_sensor_status(ir_sensor):
        ser.write(b'#i')
    else:
        ser.write(b'#I')

    ser.write(byte1)
    ser.write(b';')


def find_port():
    """
    Searches for the right port of Arduino LilyPad device using @arduino_device_name.
    :return: com port if any found, otherwise None
    """
    ports = list(serial.tools.list_ports.comports())

    for p in ports:
        if arduino_device_name in p[1]:
            return p[0]

    return None


"""
root = tk.Tk()

hi_there = tk.Button(root)
hi_there["text"] = "Hello World\n(click me)"
hi_there.pack(side="top")

root.mainloop()
"""

port = find_port()

if port is None:
    messagebox.showerror('Error', 'Can\'t find "' + arduino_device_name + '".')
    exit(0)

ser = serial.Serial(port, 115200)

fenster = Tk()
fenster.title("Vibrabot")
fenster.geometry("800x400")
build_window()

label = Label(fenster, text="Light", borderwidth="2")
label.place(x=60, y=10)  # Anordnung durch Place-Manager

left_light_sensor_label = Label(fenster, text="Hallo Welt!", borderwidth="2")
left_light_sensor_label.place(x=10, y=30)  # Anordnung durch Place-Manager

right_light_sensor_label = Label(fenster, text="Hallo Welt2!", borderwidth="2")
right_light_sensor_label.place(x=100, y=30)  # Anordnung durch Place-Manager

label = Label(fenster, text="microphone", borderwidth="2")
label.place(x=10, y=60)  # Anordnung durch Place-Manager

microphone_label = Label(fenster, text="Hallo Welt2!", borderwidth="2")
microphone_label.place(x=100, y=60)  # Anordnung durch Place-Manager

label = Label(fenster, text="Ir Sensors", borderwidth="2")
label.place(x=60, y=10)  # Anordnung durch Place-Manager

ir_sensor_label = [0 for x in range(ir_sensor_count)]
ir_led_button = [0 for x in range(ir_sensor_count)]

for ir_label in range(ir_sensor_count):
    ir_sensor_label[ir_label] = Label(fenster, text="-", borderwidth="2")
    ir_sensor_label[ir_label].place(x=10 + ir_label * 50, y=120)

for ir_button in range(ir_sensor_count):
    ir_led_button[ir_button] = Button(fenster, text="OK", command=lambda arg=ir_button: text_mod(arg))
    ir_led_button[ir_button].place(x=10 + ir_button * 50, y=150)

Label(fenster, text="Object :", borderwidth="2").place(x=10, y=210)

object_temperature_label = Label(fenster, text="0C", borderwidth="2")
object_temperature_label.place(x=60, y=210)  # Anordnung durch Place-Manager

Label(fenster, text="Ambient :", borderwidth="2").place(x=120, y=210)

ambient_temperature_label = Label(fenster, text="0C", borderwidth="2")
ambient_temperature_label.place(x=170, y=210)  # Anordnung durch Place-Manager

value = 0

data = VibrabotData()

while 1:
    # line = ser.read(10)
    line = "a"
    # print(line)

    value += 1
    # print(hex(value))

    # print(int(str(value),16))

    decode(data)
    update_window(data)
