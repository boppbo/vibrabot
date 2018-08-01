from VibrabotData import *
from collections import deque


class RealtimeGraphData:

    CONST_MAX_SIZE = 100

    def __init__(self):
        self.data = deque()
        self.x_min = 0

    def add(self, date: VibrabotData):
        if len(self.data) > 100:
            self.data.popleft()
            self.x_min += 1
        self.data.append(date)

    def get(self):
        return self.data

    def get_x_min(self):
        return self.x_min

    def get_x_max(self):
        return self.x_min + len(self.data)
