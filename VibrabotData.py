class VibrabotData:

    def __init__(self):
        self._left_light_sensor = 0
        self._right_light_sensor = 0
        self._microphone_value = 0
        self._ir_sensor = [0, 0, 0, 0, 0]
        self._ir_sensor_status = [False, False, False, False, False]
        self._object_temperature = 0.0
        self._ambient_temperature = 0.0

    def set_left_light_sensor(self, value):
        self._left_light_sensor = value

    def get_left_light_sensor(self):
        return self._left_light_sensor

    def set_right_light_sensor(self, value):
        self._right_light_sensor = value

    def get_right_light_sensor(self):
        return self._right_light_sensor

    def set_ir_sensor(self, index, value):
        if 0 <= index < len(self._ir_sensor):
            self._ir_sensor[index] = value

    def get_ir_sensor(self, index):
        if 0 <= index < len(self._ir_sensor):
            return self._ir_sensor[index]

    def set_ir_sensor_status(self, index, status):
        if 0 <= index < len(self._ir_sensor_status):
            self._ir_sensor_status[index] = status

    def get_ir_sensor_status(self, index):
        if 0 <= index < len(self._ir_sensor_status):
            return self._ir_sensor_status[index]

    def set_microphone_value(self, value):
        self._microphone_value = value

    def get_microphone_value(self):
        return self._microphone_value

    def set_object_temperature(self, temperature):
        self._object_temperature = temperature

    def get_object_temperature(self):
        return self._object_temperature

    def set_ambient_temperature(self, temperature):
        self._ambient_temperature = temperature

    def get_ambient_temperature(self):
        return self._ambient_temperature
