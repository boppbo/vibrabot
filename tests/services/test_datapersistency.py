from unittest import TestCase
from remoteapp.model.sensor import Sensor
from remoteapp.services.datapersistency import CsvSerializer

class TestDataPersistency(TestCase):
    CONST_DATA = [
            Sensor(0,"c", 30, "Foo", [190, 190, 191]),
            Sensor(1,"s", 50, "Bar", [43981])
        ]
    
    def setUp(self):
        self.out = CsvSerializer()
        

    def test_serialize(self):
        res = self.out.serialize(TestDataPersistency.CONST_DATA)

        self.assertListEqual(res, [
            ["id", "label", "interval", "data_type", "value"],
            [0, 'Foo', 30, 'c', 190],
            [0, 'Foo', 30, 'c', 190],
            [0, 'Foo', 30, 'c', 191],
            [1, 'Bar', 50, 's', 43981]
        ])

