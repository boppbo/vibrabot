

import tkinter as tk
	
	
from tkinter import *
from tkinter import ttk


from VibrabotData import *

import serial
ser = serial.Serial('com49', 115200)

global label


def buildWindow():

	Label(fenster, text = "light", borderwidth="2")

	return;



def updateWindow(vibrabotData):

	
	leftLightSensorlabel.config(text=str(vibrabotData.getLeftLightSensor()))
	rightLightSensorlabel.config(text=str(vibrabotData.getRightLightSensor()))
	return





def readRemoteByte():

	token = int(ser.read(1),16) * 16
	token += int(ser.read(1),16)
	ser.read(1)
	
	print(token)

	return (token)


def decode(line, vibrabotData):

	
	if ser.in_waiting > 1:
		token = ser.read(1)
		print("token")

	
	
		print(token)	
		if (token == b'#'):
		#if (token == 35):
			print("serial")	

			value = readRemoteByte()
			vibrabotData.setLeftLightSensor(value)
			
			
			
			value = readRemoteByte()
			vibrabotData.setRightLightSensor(value)
		#	label2.config(text=str(value))
		
		
#			token = int(ser.read(1),16) * 16
#			token += int(ser.read(1),16)


		#print(token)
			
#	label.config(text=line)
	fenster.update_idletasks()
	fenster.update()



	return;




"""
root = tk.Tk()

hi_there = tk.Button(root)
hi_there["text"] = "Hello World\n(click me)"
hi_there.pack(side="top")

root.mainloop()
"""




fenster = Tk()
fenster.title("Vibrabot")
fenster.geometry("800x400")
buildWindow()



leftLightSensorlabel = Label(fenster, text = "Hallo Welt!", borderwidth="2")
leftLightSensorlabel.place(x = 10, y = 10) #Anordnung durch Place-Manager

rightLightSensorlabel = Label(fenster, text = "Hallo Welt2!", borderwidth="2")
rightLightSensorlabel.place(x = 10, y = 30) #Anordnung durch Place-Manager

#label = Label(fenster, text = "Hallo Welt!", borderwidth="2")
#label.place(x = 10, y = 10) #Anordnung durch Place-Manager
#fenster.mainloop()	

value = 0

vibrabotData = VibrabotData()


while 1:
	#line = ser.read(10)
	line = "a"
#	print(line)
	

	value+= 1 
#	print(hex(value))
	
#	print(int(str(value),16))
	
	decode(line, vibrabotData)
	updateWindow(vibrabotData)
