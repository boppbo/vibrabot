class SerialMock:
    def __init__(self):
        self.read_messages = ""
        self.written_messages = ""
        self.timeout = None 
        self.pos = 0

    def write(self, message: bytes):
        msg = message.decode("ascii")
        self.written_messages = self.written_messages + msg
        print(msg)

    def read(self, count):
        oldpos = self.pos
        self.pos = self.pos + count
        
        if (self.pos > len(self.read_messages)):
            raise AssertionError("Read too many bytes!")

        return (self.read_messages[oldpos:self.pos]).encode('ascii')

    def read_until(self, terminator):
        result = bytearray()
        while True:
            result += self.read(1)
            if (result[-1] == terminator[0]):
                return bytes(result)
        