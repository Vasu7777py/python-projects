
from threading import Thread, Lock
from time import sleep

Threadlock = Lock()

class Lift:

    Requests = []
    Lifts = []
    speed = 1
    wait = 6

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
        #return_val = None
        Threadlock.acquire()
        if (floor > self.Present_floor):
            if self.Running:
                if (self.Direction == direction):
                    if (self.Direction == 1):
                        floor_diff = (floor - self.Present_floor)
                    else:
                        floor_diff = ((floor - self.Present_floor) + (2 * (self.Present_floor - self.Destination) ) )
                elif ((direction == 1) and (self.Direction == -1)):
                    floor_diff = ((floor - self.Present_floor) + (2 * (self.Present_floor - self.Destination) ) )
                elif ((direction == -1) and (self.Direction == 1)):
                    if (floor > self.Destination):
                        floor_diff = (floor - self.Present_floor)
                    else:
                        floor_diff = ((2 * (self.Destination - floor) + (floor - self.Present_floor) ) )
            else:
                floor_diff = (floor - self.Present_floor)
        elif (floor < self.Present_floor):
            if self.Running:
                if (self.Direction == direction):
                    if (self.Direction == -1):
                        floor_diff = (self.Present_floor - floor)
                    else:
                        floor_diff = ((self.Present_floor - floor) + (2 * (self.Destination - self.Present_floor) ) )
                elif ((direction == 1) and (self.Direction == -1)):
                    floor_diff = (self.Present_floor - floor)
                elif((direction == -1) and (self.Direction == 1)):
                    floor_diff = ((self.Present_floor - floor) + (2 * (self.Destination - self.Present_floor) ) )
            else:
                floor_diff = (self.Present_floor - floor)
        time_req = ((floor_diff * self.speed) + (len(self.Request_list) * self.wait))
        Threadlock.release()
        return (self,time_req)
    
    @classmethod
    def get_request(cls):
        Threadlock.acquire()
        Requests = cls.Requests
        cls.Requests.clear()
        Threadlock.release()
        for request in Requests:
            floor, direction = request
            for lift in cls.Lifts:
                if request not in lift.Request_list:
                    Time_Requried = lift.time_requried(floor, direction)
                    if (Time_Requried != None):
                        lift.set_request(floor, direction, lift)

    @classmethod
    def set_request(cls, floor, direction, lift:Lift):
        lift.Request_list.append((floor, direction))

    def pick_up(self):
        pass

    def start(self):
        pass


Lift.Lifts.append(Lift(1))
Lift.Lifts.append(Lift(2))
Lift.Lifts.append(Lift(3))
Lift.Lifts.append(Lift(4))