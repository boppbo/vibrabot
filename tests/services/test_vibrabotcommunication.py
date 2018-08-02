from unittest import TestCase
from .serialmock import SerialMock
from remoteapp.services.vibrabotcommunication import Sensor, VibraBotCommunication


class TestVibrabotCommunication(TestCase):
    def setUp(self):
        """ Gets run before every test """
        self.mock = SerialMock()
        self.out = VibraBotCommunication(self.mock)
        self.config = [Sensor(0,"c", 30, "Foo"), Sensor(1,"s", 50, "Bar")]

    def test_read_config(self):
        self.mock.read_messages = "$02;$00,c,000A,Foo;$01,s,0014,Bar;"

        config = self.out.read_config()
        
        self.assertEqual(2, len(config))
        self.assertEquals("$0;", self.mock.written_messages)

        self.assertEqual(0, config[0].id)
        self.assertEqual('c', config[0].data_type)
        self.assertEqual(10, config[0].interval)
        self.assertEqual("Foo", config[0].label)

        self.assertEqual(1, config[1].id)
        self.assertEqual('s', config[1].data_type)
        self.assertEqual(20, config[1].interval)
        self.assertEqual("Bar", config[1].label)

    def test_read_config_noisy(self):
        self.mock.read_messages = "4t43z6$02;$00,c,000A,Foo;42.34$01,s,0014,Bar;"

        config = self.out.read_config()
        
        self.assertEqual(2, len(config))

        self.assertEqual(0, config[0].id)
        self.assertEqual('c', config[0].data_type)
        self.assertEqual(10, config[0].interval)
        self.assertEqual("Foo", config[0].label)

        self.assertEqual(1, config[1].id)
        self.assertEqual('s', config[1].data_type)
        self.assertEqual(20, config[1].interval)
        self.assertEqual("Bar", config[1].label)

    def test_write_config(self):
        self.out.write_config(self.config)
        self.assertEquals(
            "$1,001E,0032;",
            self.mock.written_messages)
    
    def test_read_data(self):
        self.mock.read_messages = "$00,BE;$00,BE;$01,ABCD;$00,BF;$FF;"

        self.out.read_data(self.config)
        
        self.assertEqual(3, len(self.config[0].values))
        self.assertEqual(0xBE, self.config[0].values[0])
        self.assertEqual(0xBE, self.config[0].values[1])
        self.assertEqual(0xBF, self.config[0].values[2])

        self.assertEqual(1, len(self.config[1].values))
        self.assertEqual(0xABCD, self.config[1].values[0])
        

    def test_stop_live_data(self):
        self.out.stop_live_data()
        self.assertEquals("$4;", self.mock.written_messages)
