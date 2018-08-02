import time
import csv


class LogWriter:

    CONST_PREFIX = "log"
    CONST_DATEFORMAT = "%y%m%d%H%M%S"
    CONST_EXTENSION = ".csv"

    def __init__(self):
        self._file_name = None

    def write_log(self, data):
        self._file_name = LogWriter.CONST_PREFIX + time.strftime(LogWriter.CONST_DATEFORMAT) + LogWriter.CONST_EXTENSION
        with open(self._file_name, 'w') as csvfile:
            csv.writer(csvfile, delimiter=';', lineterminator='\n').writerows(data)

    def get_file_name(self):
        return self._file_name
