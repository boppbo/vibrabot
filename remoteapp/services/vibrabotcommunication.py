import serial
from typing import List
from remoteapp.model.sensor import Sensor

class VibraBotCommunication():
    CONST_ENCODING = 'ascii'
    
    def __init__(self, serial: serial.Serial):
        self._serial = serial
    def _discard_noise(self):
        """ Remove alien protocol noise
        
            Our data logging software isn't the only software using
            the serial interface on the vibrabot so we have to discard
            other messages until the start sequence occurs.
        """
        self._serial.read_until(terminator=b"$")
    def _expect_character(self, character: bytes):
        if (self._serial.read(len(character)) != character):
            raise ValueError("I/O Error expected ", character)
    def _expect_semicolon(self):
        self._expect_character(b";")
    def _expect_comma(self):
        self._expect_character(b",")
    def _parseInteger(self, data: bytes) -> int:
        """ Numbers are interchanged as HEX strings """
        #return int(data, 16)
        return int.from_bytes(
            bytes.fromhex(data.decode(VibraBotCommunication.CONST_ENCODING)),
            byteorder = 'big',
            signed = False)
    def _readInteger(self, size = 2):
        return self._parseInteger(self._serial.read(size))


    def read_config(self) -> List[Sensor]:
        # Format $<count><sensor>...<sensor>
        # count: 2 ASCII Hex characters, sensor count
        # sensor: see below
        
        result = []
        
        # $0; = READ_CONFIG
        self._serial.write(b"$0;")

        self._discard_noise()
        count = self._readInteger(2)
        self._expect_semicolon()

        # pylint: disable=W0612
        for i in range(count):
            # Format $<id>,<value_data_type>,<interval>,<label>;
            # id: 2 ASCII Hex characters
            # value_data_type: 1 ASCII character ('c' / 's')
            # interval: 4 ASCII Hex characters
            # label: n ASCII characters terminated by ';'
            self._discard_noise()
            
            id = self._readInteger(2)
            self._expect_comma()
            
            data_type = self._serial.read(1) \
                            .decode(VibraBotCommunication.CONST_ENCODING)
            self._expect_comma()

            interval = self._readInteger(4)
            self._expect_comma()

            #split ';' from result
            label = self._serial.read_until(terminator=b";") \
                        .decode(VibraBotCommunication.CONST_ENCODING)[:-1]
            
            result.append( Sensor(id, data_type, interval, label) )

        return result

    def write_config(self, config: List[Sensor]):
        # Format $1,<interval>,<interval>,...,<interval>;
        # interval: 4 ASCII Hex characters
        intervals = [format(sensor.interval, "04X") for sensor in config]
        
        msg = ",".join( ["$1"] + intervals ) + ";"
        bytes_msg = msg.encode(VibraBotCommunication.CONST_ENCODING)
        
        self._serial.write(bytes_msg)

    def read_data(self, config: List[Sensor], live_data: bool = False):
        # $2; = READ_DATA
        # $3; = READ_LIVE_DATA
        self._serial.write(b"$2;" if live_data else b"$3;")

        # Format <entry>...<entry>$FF;
        # entry: see below
        # $FF;: Finished transmitting
        while True:
            # Format $<id>,<value>;
            # id: 2 ASCII Hex characters
            # value: Variable length of ASCII chars depending on value_type
            self._discard_noise()
            
            id = self._readInteger(2)

            if (id == 0xFF):
                self._expect_semicolon()
                break

            self._expect_comma()
            
            sensor = config[id]

            if (id != sensor.id):
                raise ValueError("Sensor id not ongoing!")

            data_length = Sensor.CONST_DATA_TYPES[sensor.data_type]
            value = self._readInteger(data_length)
            self._expect_semicolon()

            sensor.values.append( value )

    def stop_live_data(self):
        # $4; = READ_LIVE_DATA
        self._serial.write(b"$4;")
