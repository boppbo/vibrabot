import tkinter as tk

from tkinter import *
from tkinter import ttk

import serial.tools.list_ports

from VibrabotData import *

import serial

irSensorCount = 5

global label


def build_window():
    Label(fenster, text="light", borderwidth="2")

    return


def update_window(vibrabot_data):
    leftLightSensorlabel.config(text=str(vibrabot_data.get_left_light_sensor()))
    rightLightSensorlabel.config(text=str(vibrabot_data.get_right_light_sensor()))

    microphonelabel.config(text=str(vibrabot_data.get_microphone()))

    for irSensor in range(irSensorCount):
        irSensorLabel[irSensor].config(text=str(vibrabot_data.get_ir_sensor(irSensor)))

    for irSensor in range(irSensorCount):

        if vibrabot_data.get_ir_sensor_status(irSensor):
            irLedButton[irSensor].config(text="on")
        else:
            irLedButton[irSensor].config(text="off")

        objectTemperaturelabel.config(text=round((vibrabot_data.get_object_temperature() * 0.02 - 273.15), 2))
        ambientTemperaturelabel.config(text=round((vibrabot_data.get_ambient_temperature() * 0.02 - 273.15), 2))

    return


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


def decode(line, vibrabot_data):
    if ser.in_waiting > 1:
        token = ser.read(1)
        #		print("token")

        #		print(token)
        if token == b'#':
            # if (token == 35):
            #			print("serial")

            value = read_remote_byte()
            vibrabot_data.set_left_light_sensor(value)

            value = read_remote_byte()
            vibrabot_data.set_right_light_sensor(value)

            value = read_remote_byte()
            vibrabot_data.set_microphone(value)

            for sensor in range(5):
                value = read_remote_byte()
                vibrabot_data.set_ir_sensor(sensor, value)

            value = read_remote_byte()

            for sensor in range(5):
                if value & (1 << sensor):
                    vibrabot_data.set_ir_sensor_status(sensor, True)
                else:
                    vibrabot_data.set_ir_sensor_status(sensor, False)

            value = read_remote_word()
            vibrabot_data.set_object_temperature(value)

            value = read_remote_word()
            vibrabot_data.set_ambient_temperature(value)

    fenster.update_idletasks()
    fenster.update()

    return


def text_mod(arg):
    ir_sensor = arg

    arg = arg + 48

    byte1 = arg.to_bytes(1, byteorder='big')

    if vibrabotData.get_ir_sensor_status(ir_sensor):
        ser.write(b'#i')
    else:
        ser.write(b'#I')

    ser.write(byte1)
    ser.write(b';')

    return


def find_port():
    ports = list(serial.tools.list_ports.comports())

    substring = 'Arduino'

    for p in ports:
        if substring in p[1]:
            return p[0]

    return "LOL ERROR"


"""
root = tk.Tk()

hi_there = tk.Button(root)
hi_there["text"] = "Hello World\n(click me)"
hi_there.pack(side="top")

root.mainloop()
"""

ser = serial.Serial(find_port(), 115200)

fenster = Tk()
fenster.title("Vibrabot")
fenster.geometry("800x400")
build_window()

label = Label(fenster, text="Light", borderwidth="2")
label.place(x=60, y=10)  # Anordnung durch Place-Manager

leftLightSensorlabel = Label(fenster, text="Hallo Welt!", borderwidth="2")
leftLightSensorlabel.place(x=10, y=30)  # Anordnung durch Place-Manager

rightLightSensorlabel = Label(fenster, text="Hallo Welt2!", borderwidth="2")
rightLightSensorlabel.place(x=100, y=30)  # Anordnung durch Place-Manager

label = Label(fenster, text="microphone", borderwidth="2")
label.place(x=10, y=60)  # Anordnung durch Place-Manager

microphonelabel = Label(fenster, text="Hallo Welt2!", borderwidth="2")
microphonelabel.place(x=100, y=60)  # Anordnung durch Place-Manager

label = Label(fenster, text="Ir Sensors", borderwidth="2")
label.place(x=60, y=10)  # Anordnung durch Place-Manager

irSensorLabel = [0 for x in range(irSensorCount)]
irLedButton = [0 for x in range(irSensorCount)]

for irLabel in range(irSensorCount):
    irSensorLabel[irLabel] = Label(fenster, text="-", borderwidth="2")
    irSensorLabel[irLabel].place(x=10 + irLabel * 50, y=120)

for irButton in range(irSensorCount):
    irLedButton[irButton] = Button(fenster, text="OK", command=lambda arg=irButton,: text_mod(arg))
    irLedButton[irButton].place(x=10 + irButton * 50, y=150)

Label(fenster, text="Object :", borderwidth="2").place(x=10, y=210)

objectTemperaturelabel = Label(fenster, text="0C", borderwidth="2")
objectTemperaturelabel.place(x=60, y=210)  # Anordnung durch Place-Manager

Label(fenster, text="Ambient :", borderwidth="2").place(x=120, y=210)

ambientTemperaturelabel = Label(fenster, text="0C", borderwidth="2")
ambientTemperaturelabel.place(x=170, y=210)  # Anordnung durch Place-Manager

value = 0

vibrabotData = VibrabotData()

while 1:
    # line = ser.read(10)
    line = "a"
    # print(line)

    value += 1
    # print(hex(value))

    # print(int(str(value),16))

    decode(line, vibrabotData)
    update_window(vibrabotData)
