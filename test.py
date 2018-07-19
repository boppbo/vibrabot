

import tkinter as tk
	
	
from tkinter import *
from tkinter import ttk


from VibrabotData import *

import serial


irSensorCount = 5

ser = serial.Serial('com49', 115200)

global label


def buildWindow():

	Label(fenster, text = "light", borderwidth="2")

	return;



def updateWindow(vibrabotData):

	
	leftLightSensorlabel.config(text=str(vibrabotData.getLeftLightSensor()))
	rightLightSensorlabel.config(text=str(vibrabotData.getRightLightSensor()))
	
	microphonelabel.config(text=str(vibrabotData.getMicrophone()))
	
	
	for irLabel in range(irSensorCount):
		irSensorLabel[irLabel].config(text=str(vibrabotData.getIrSensor(irLabel)))
	
	
	return





def readRemoteByte():

	token = int(ser.read(1),16) * 16
	token += int(ser.read(1),16)
	ser.read(1)
	
#	print(token)

	return (token)


def decode(line, vibrabotData):

	
	if ser.in_waiting > 1:
		token = ser.read(1)
#		print("token")

	
	
#		print(token)	
		if (token == b'#'):
		#if (token == 35):
#			print("serial")	

			value = readRemoteByte()
			vibrabotData.setLeftLightSensor(value)
			
			
			
			value = readRemoteByte()
			vibrabotData.setRightLightSensor(value)

			value = readRemoteByte()
			vibrabotData.setMicrophone(value)
			
			for sensor in range(5):
				value = readRemoteByte()
				vibrabotData.setIrSensor(sensor,value)
			
			
		#	label2.config(text=str(value))
		
		
#			token = int(ser.read(1),16) * 16
#			token += int(ser.read(1),16)


		#print(token)
			
#	label.config(text=line)
	fenster.update_idletasks()
	fenster.update()



	return;

def text_mod(arg):

	arg = arg + 48
	
	byte1 = arg.to_bytes(1,byteorder='big')
	
	ser.write(b'#I')
	ser.write(byte1)
	ser.write(b';')
	
	return


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

label = Label(fenster, text = "Light", borderwidth="2")
label.place(x = 60, y = 10) #Anordnung durch Place-Manager


leftLightSensorlabel = Label(fenster, text = "Hallo Welt!", borderwidth="2")
leftLightSensorlabel.place(x = 10, y = 30) #Anordnung durch Place-Manager

rightLightSensorlabel = Label(fenster, text = "Hallo Welt2!", borderwidth="2")
rightLightSensorlabel.place(x = 100, y = 30) #Anordnung durch Place-Manager


label = Label(fenster, text = "microphone", borderwidth="2")
label.place(x = 10, y = 60) #Anordnung durch Place-Manager


microphonelabel = Label(fenster, text = "Hallo Welt2!", borderwidth="2")
microphonelabel.place(x = 100, y = 60) #Anordnung durch Place-Manager


label = Label(fenster, text = "Ir Sensors", borderwidth="2")
label.place(x = 60, y = 10) #Anordnung durch Place-Manager



irSensorLabel = [0 for x in range(irSensorCount)] 
irLedButton = [0 for x in range(irSensorCount)] 

for irLabel in range(irSensorCount):
	irSensorLabel[irLabel] = Label(fenster, text = "-", borderwidth="2")
	irSensorLabel[irLabel].place(x = 10+irLabel*50, y = 120) 
	
	
for irButton in range(irSensorCount):
	irLedButton[irButton] = Button(fenster, text="OK", command=lambda arg=irButton,  : text_mod(arg))
	irLedButton[irButton].place(x = 10+irButton*50, y = 150) 



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
