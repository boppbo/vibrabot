import serial.tools.list_ports
from VibrabotData import *


class RealtimeDataProvider:

    CONST_SENSOR_IR_COUNT = 5

    def __init__(self, serial: serial.Serial):
        self._ser = serial
        self._data = VibrabotData()

    def _read_remote_byte(self):
        token = int(self._ser.read(1), 16) * 16
        token += int(self._ser.read(1), 16)
        self._ser.read(1)

        return token

    def _read_remote_word(self):
        token = int(self._ser.read(1), 16) * 4096
        token += int(self._ser.read(1), 16) * 256
        token += int(self._ser.read(1), 16) * 16
        token += int(self._ser.read(1), 16)
        self._ser.read(1)

        return token

    def _decode(self):
        if self._ser.in_waiting > 1:
            token = self._ser.read(1)
            # print("token")

            # print(token)
            if token == b'#':
                self._data = VibrabotData();
                # if (token == 35):
                # print("serial")

                value = self._read_remote_byte()
                self._data.set_left_light_sensor(value)

                value = self._read_remote_byte()
                self._data.set_right_light_sensor(value)

                value = self._read_remote_byte()
                self._data.set_microphone_value(value)

                for sensor in range(RealtimeDataProvider.CONST_SENSOR_IR_COUNT):
                    value = self._read_remote_byte()
                    self._data.set_ir_sensor(sensor, value)

                value = self._read_remote_byte()

                for sensor in range(RealtimeDataProvider.CONST_SENSOR_IR_COUNT):
                    if value & (1 << sensor):
                        self._data.set_ir_sensor_status(sensor, True)
                    else:
                        self._data.set_ir_sensor_status(sensor, False)

                value = self._read_remote_word()
                self._data.set_object_temperature(value)

                value = self._read_remote_word()
                self._data.set_ambient_temperature(value)

    def _text_mod(self, arg):
        ir_sensor = arg

        arg = arg + 48

        byte1 = arg.to_bytes(1, byteorder='big')

        if data.get_ir_sensor_status(ir_sensor):
            self._ser.write(b'#i')
        else:
            self._ser.write(b'#I')

            self._ser.write(byte1)
            self._ser.write(b';')

    def get_data(self):
        self._decode()
        return self._data
