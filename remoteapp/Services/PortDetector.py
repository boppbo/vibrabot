import serial
import serial.tools.list_ports
from typing import List

class PortDetector():
    CONST_DEVICE_NAME = 'Arduino LilyPad USB'
        
    def detect_port(self) -> list:
        """
        Searches for the right port of Arduino LilyPad device using arduino_device_name.
        :return: com port if any found, otherwise None
        """
        ports = list(serial.tools.list_ports.comports())

        for p in ports:
            #p[1] Description
            if PortDetector.CONST_DEVICE_NAME in p[1]:
                #p[0] COM??
                return p[0]

        return None
