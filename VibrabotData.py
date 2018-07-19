class VibrabotData:

	leftLightSensor = 0
	rightLightSensor = 0
	microphoneValue = 0
	irSensor = [0,0,0,0,0]
	
	def setLeftLightSensor(self, value):
	
		self.leftLightSensor = value
		
		return;
		
	def getLeftLightSensor(self):
	
		return (self.leftLightSensor);
		
		
		
		
	def setRightLightSensor(self, value):
	
		self.rightLightSensor = value
		
		return;
		
		
	def getRightLightSensor(self):
	
		return(self.rightLightSensor);
		
		
		
	def setIrSensor(self, index, value):
	
		#if (index < len(irSensor)):
			self.irSensor[index] = value
		
			return;
		
		
	def getIrSensor(self, index):
	#	if (index < len(irSensor)):
			return(self.irSensor[index]);	
			
		#	return(0);	
		
		
	def setMicrophone(self, value):
		self.microphoneValue = value
		
		return;
		
		
	def getMicrophone(self):
		return(self.microphoneValue);	