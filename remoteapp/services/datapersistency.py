import time
import csv
from typing import List
from remoteapp.model.sensor import Sensor

class CsvSerializer():
    def serialize(self, data: List[Sensor]):
        result = []

        result.append(
            ["id","label","interval","data_type","value"])

        for s in data:
            for val in s.values:
                line = []
                line.append(s.id)
                line.append(s.label)
                line.append(s.interval)
                line.append(s.data_type)
                line.append(val)
                result.append(line)
                
        return result
    
    def deserialize(self, csvData: List[List[str]]) -> List[Sensor]:
        pass

class CsvLogWriter():
    CONST_PREFIX = "log_"
    CONST_DATEFORMAT = "%y%m%d_%H%M%S"
    CONST_EXTENSION = ".csv"
    CONST_FILENAME = CONST_PREFIX + CONST_DATEFORMAT + CONST_EXTENSION

    def __init__(self, serializer: CsvSerializer):
        self._serializer = serializer

    def export(self, path: str, data: List[Sensor]):
        ser_data = self._serializer.serialize(data)

        with open(path, 'w') as csvfile:
            csv.writer(csvfile, delimiter=';', lineterminator='\n') \
               .writerows(ser_data)
