
from threading import Thread, Lock
from time import sleep

Threadlock = Lock()

class Lift:

    Requests = []
    Lifts = []

    def __init__(self, Number:int, Present_floor = 0):
        self.Number = Number
        self.Running = False
        self.Interception = False
        self.Request_list = []
        self.Intercept_request = []
        self.Present_floor = Present_floor
        self.Destination = None
        self.Direction = None

    def time_requried(self, floor, direction):
        pass
    
    @classmethod
    def get_request(cls):
        Threadlock.acquire()
        for request in cls.Requests:
            floor, direction = request
            for lift in cls.Lifts:
                Time_Requried = lift.time_requried(floor, direction)
                if (Time_Requried != None):
                    lift.set_request(floor, direction, lift)
        Threadlock.release()

    @classmethod
    def set_request(cls, floor, direction, lift:Lift):
        lift.Request_list.append((floor, direction))

    def pick_up(self):
        pass

    def start(self):
        pass
