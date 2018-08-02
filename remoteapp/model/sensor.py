from enum import Enum

class Sensor():
    CONST_DATA_TYPES = {
        "c": 2, #ascii hex char (Byte)
        "s": 4  #ascii hex short (Word)
    }

    def __init__(self, id, data_type, interval, label, values = []):
        self.id = id
        self.label = label
        self.interval = interval
        self.data_type = data_type
        self.values = values

    @property
    def data_type(self) -> str:
        return self._data_type
    
    @data_type.setter
    def data_type(self, value : str) -> None:
        if (value not in Sensor.CONST_DATA_TYPES):
            raise ValueError("Invalid data type for sensor!", value)
        self._data_type = value

    @property
    def interval(self) -> int:
        return self._interval

    @interval.setter
    def interval(self, interval: int) -> None:
        if (interval < 0):
            raise ValueError("Only positive interval allowed!")
        if (interval > (2**16)-1):
            raise ValueError("Interval too big for WORD!")

        self._interval = interval
