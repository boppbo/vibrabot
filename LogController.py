from LogTab import *
from LogWriter import *


class LogController:

    def __init__(self, tab, writer: LogWriter):
        self._tab = tab
        self._writer = writer

    def save(self):
        self._writer.write_log([["1", "2"], ["3", "4"]])
        self._tab.info_written(self._writer.get_file_name())
