from dataclasses import dataclass
from time import sleep

@dataclass
class User_Passcode:
    Passcode: str

    def __init__(self ,Passcode):
        self.Passcode = Passcode
    
    def Password_entry(self ,Passcode):
        if self.Passcode == Passcode:
            sleep(2.5)
            print("Access granted")
            return True
        else:
            sleep(1)
            print("Access denied")
            return False
