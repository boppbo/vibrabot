

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
	
	microphonelabel.config(text=str(vibrabotData.getMicrophone()))
	
	ir0Label.config(text=str(vibrabotData.getIrSensor(0)))
	ir1Label.config(text=str(vibrabotData.getIrSensor(1)))
	ir2Label.config(text=str(vibrabotData.getIrSensor(2)))
	ir3Label.config(text=str(vibrabotData.getIrSensor(3)))
	ir4Label.config(text=str(vibrabotData.getIrSensor(4)))
	
	return





def readRemoteByte():

	token = int(ser.read(1),16) * 16
	token += int(ser.read(1),16)
	ser.read(1)
	
#	print(token)

	return (token)



def callback():
	print ("click!")
	return;

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
	print(arg)
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


ir0Label = Label(fenster, text = "-", borderwidth="2")
ir0Label.place(x = 10, y = 120) #Anordnung durch Place-Manager

ir1Label = Label(fenster, text = "-", borderwidth="2")
ir1Label.place(x = 60, y = 120) #Anordnung durch Place-Manager

ir2Label = Label(fenster, text = "-", borderwidth="2")
ir2Label.place(x = 110, y = 120) #Anordnung durch Place-Manager

ir3Label = Label(fenster, text = "-", borderwidth="2")
ir3Label.place(x = 160, y = 120) #Anordnung durch Place-Manager

ir4Label = Label(fenster, text = "-", borderwidth="2")
ir4Label.place(x = 210, y = 120) #Anordnung durch Place-Manager


#irLed1Button = Button(fenster, text="OK", command=callback)
#b['command'] = text_mod
#irLed1Button['command'] = lambda arg=1,  : text_mod(arg)
#irLed1Button.place(x = 10, y = 150) #Anordnung durch Place-Manager


#irLed2Button = Button(fenster, text="OK", command=callback)

#irLed2Button['command'] = lambda arg=2,  : text_mod(arg)
#irLed2Button.place(x = 60, y = 150) #Anordnung durch Place-Manager


irLedButton = [0 for x in range(5)] 

for irButton in range(5):
	irLedButton[irButton] = Button(fenster, text="OK", command=lambda arg=irButton,  : text_mod(arg))
	irLedButton[irButton].place(x = 10+irButton*50, y = 150) #Anordnung durch Place-Manager

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
