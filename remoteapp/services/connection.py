import serial
import serial.tools.list_ports
from typing import List


class ConnectionFactory:

    CONST_DEVICE_NAME = 'Arduino LilyPad USB'
    CONST_BAUD_RATE = 115200

    def detect_ports(self) -> List[str]:
        """
        Searches for the right port of Arduino LilyPad device using arduino_device_name.
        :return: com port if any found, otherwise None
        """
        ports = list(serial.tools.list_ports.comports())

        for p in ports:
            # p[1] Description
            if ConnectionFactory.CONST_DEVICE_NAME in p[1]:
                # p[0] COM??
                yield p[0]
    
    def detect_port(self) -> str:
        for p in self.detect_ports():
            return p
        return None

    def open_connection(self, port: str) -> serial.Serial:
        return serial.Serial(port, ConnectionFactory.CONST_BAUD_RATE )

    
