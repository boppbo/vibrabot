import time
import csv
from typing import List
from remoteapp.model.sensor import Sensor

class CsvSerializer():
    def serialize(self, data: List[Sensor]):
        result = []

        result.append(
            ["sensorid","label","interval","data_type","value"])

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
    
    def deserialize(self, csvData: List[List]) -> List[Sensor]:
        result = []

        #Remove header line by slicing
        for line in csvData[1:]:
            id = int(line[0])

            inserted = False
            for sensor in result:
                if sensor.id == id:
                    inserted = True
                    sensor.values.append(int(line[4]))
        
            if (not inserted):
                result.append(
                    Sensor(
                        id = id,
                        label = line[1],
                        interval = int(line[2]),
                        data_type = line[3],
                        values = [ int(line[4]) ]))

        return result

class CsvLogWriter():
    CONST_PREFIX = "log_"
    CONST_DATEFORMAT = "%y%m%d_%H%M%S"
    CONST_EXTENSION = ".csv"
    CONST_FILENAME = CONST_PREFIX + CONST_DATEFORMAT + CONST_EXTENSION

    def __init__(self, baseConfig: List[Sensor], serializer: CsvSerializer):
        self._serializer = serializer
        self._config = baseConfig

    def export(self, path: str, data: List[Sensor]):
        ser_data = self._serializer.serialize(data)

        with open(path, 'w') as csvfile:
            csv.writer(csvfile, delimiter=';', lineterminator='\n') \
               .writerows(ser_data)
        
    def import_(self, path: str) -> List[Sensor]:
        with open(path, 'r') as csvfile:
            iter = csv.reader(csvfile, delimiter=';', lineterminator='\n')
            config = self._serializer.deserialize(list(iter))
            for cfg in self._config:
                cfg.values = []
                cfg.interval = 0

                for readcfg in config:
                    if readcfg.id == cfg.id:
                        cfg.interval = readcfg.interval
                        cfg.values = readcfg.values
            return self._config
               