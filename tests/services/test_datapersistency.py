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
            ["sensorid", "label", "interval", "data_type", "value"],
            [0, 'Foo', 30, 'c', 190],
            [0, 'Foo', 30, 'c', 190],
            [0, 'Foo', 30, 'c', 191],
            [1, 'Bar', 50, 's', 43981]
        ])

    def test_deserialize(self):
        ser = [
            ["sensorid", "label", "interval", "data_type", "value"],
            [0, 'Foo', 30, 'c', 190],
            [0, 'Foo', 30, 'c', 190],
            [0, 'Foo', 30, 'c', 191],
            [1, 'Bar', 50, 's', 43981]
        ]
        
        res = self.out.deserialize(ser)

        self.assertEquals(len(res), len(TestDataPersistency.CONST_DATA))
        
        self.assertEqual(res[0].id, TestDataPersistency.CONST_DATA[0].id)
        self.assertEqual(res[0].label, TestDataPersistency.CONST_DATA[0].label)
        self.assertEqual(res[0].interval, TestDataPersistency.CONST_DATA[0].interval)
        self.assertEqual(res[0].data_type, TestDataPersistency.CONST_DATA[0].data_type)
        self.assertListEqual(res[0].values, TestDataPersistency.CONST_DATA[0].values)

        self.assertEqual(res[1].id, TestDataPersistency.CONST_DATA[1].id)
        self.assertEqual(res[1].label, TestDataPersistency.CONST_DATA[1].label)
        self.assertEqual(res[1].interval, TestDataPersistency.CONST_DATA[1].interval)
        self.assertEqual(res[1].data_type, TestDataPersistency.CONST_DATA[1].data_type)
        self.assertListEqual(res[1].values, TestDataPersistency.CONST_DATA[1].values)
        
