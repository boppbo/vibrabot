class VibrabotData:
    leftLightSensor = 0
    rightLightSensor = 0
    microphoneValue = 0
    irSensor = [0, 0, 0, 0, 0]
    irSensorStatus = [False, False, False, False, False]
    objectTemperature = 0.0
    ambientTemperature = 0.0

    def set_left_light_sensor(self, value):

        self.leftLightSensor = value

        return

    def get_left_light_sensor(self):

        return self.leftLightSensor

    def set_right_light_sensor(self, value):

        self.rightLightSensor = value

        return

    def get_right_light_sensor(self):

        return self.rightLightSensor

    def set_ir_sensor(self, index, value):

        if index < len(self.irSensor):
            self.irSensor[index] = value

        return

    def get_ir_sensor(self, index):
        if index < len(self.irSensor):
            return self.irSensor[index]

        return 0

    def set_ir_sensor_status(self, index, status):

        if index < len(self.irSensorStatus):
            self.irSensorStatus[index] = status

        return

    def get_ir_sensor_status(self, index):
        if index < len(self.irSensorStatus):
            return self.irSensorStatus[index]

        return 0

    def set_microphone(self, value):
        self.microphoneValue = value

        return

    def get_microphone(self):
        return self.microphoneValue

    def set_object_temperature(self, temperature):
        self.objectTemperature = temperature

        return

    def get_object_temperature(self):
        return self.objectTemperature

    def set_ambient_temperature(self, temperature):
        self.ambientTemperature = temperature

        return

    def get_ambient_temperature(self):
        return self.ambientTemperature
