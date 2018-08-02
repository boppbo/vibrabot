from tkinter import BooleanVar


class RealtimeController:

    def __init__(self):
        self.light_left = BooleanVar(False)
        self.light_right = BooleanVar(False)
        self.mic = BooleanVar(False)
        self.ir = [BooleanVar(False), BooleanVar(False), BooleanVar(False), BooleanVar(False), BooleanVar(False)]
        self.tmp_obj = BooleanVar(False)
        self.tmp_amb = BooleanVar(False)
