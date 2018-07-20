class VibrabotData:

	leftLightSensor = 0
	rightLightSensor = 0
	microphoneValue = 0
	irSensor = [0, 0, 0, 0, 0]
	irSensorStatus = [False, False, False, False, False]
	objectTemperature = 0.0
	ambientTemperature = 0.0
	
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
	
		if (index < len(self.irSensor)):
			self.irSensor[index] = value
		
		return;
		
		
	def getIrSensor(self, index):
		if (index < len(self.irSensor)):
			return(self.irSensor[index]);	
			
		return(0);	
		
		
	def setIrSensorStatus(self, index, status):
	
		if (index < len(self.irSensorStatus)):
			self.irSensorStatus[index] = status
		
		return;
		
		
	def getIrSensorStatus(self, index):
		if (index < len(self.irSensorStatus)):
			return(self.irSensorStatus[index]);	
			
		return(0);			
		
		
		
	def setMicrophone(self, value):
		self.microphoneValue = value
		
		return;
		
		
	def getMicrophone(self):
		return(self.microphoneValue);	
		
		
		
	def setObjectTemperature(self, temperature):
		self.objectTemperature = temperature
		
		return;
		
		
	def getObjectTemperature(self):
		return(self.objectTemperature);		
		
		
	def setAmbientTemperature(self, temperature):
		self.ambientTemperature = temperature
		
		return;
		
		
	def getAmbientTemperature(self):
		return(self.ambientTemperature);		