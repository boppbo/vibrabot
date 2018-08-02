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
            id = line[0]

            if (id == len(result)):
                result.append(
                    Sensor(
                        id = id,
                        label = line[1],
                        interval = line[2],
                        data_type = line[3],
                        values = [ line[4] ]))

            elif id < len(result):
                sensor = result[id]
                if id != sensor.id:
                    raise ValueError("Invalid file")
                sensor.values.append(line[4])
            else:
                raise ValueError("Invalid file")

        return result
