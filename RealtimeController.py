from tkinter import BooleanVar


class RealtimeController:

    def __init__(self):
        self.mic = BooleanVar(False)
        self.light_left = BooleanVar(False)
        self.light_right = BooleanVar(False)
