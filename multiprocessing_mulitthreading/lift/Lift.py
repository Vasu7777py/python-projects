
from threading import Thread
from time import sleep

class Lift:
    def __init__(self, Number:int, Present_floor = 0):
        self.Number = Number
        self.Running = False
        self.Interception = False
        self.Request_list = []
        self.Intercept_requst = []
        self.Present_floor = Present_floor
        self.Destination = None
        self.Direction = None

    def time_requried(self, floor, direction):
        pass
    
    def pick_up(self):
        pass

    def start(self):
        pass
