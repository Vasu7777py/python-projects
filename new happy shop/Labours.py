from dataclasses import dataclass
import getpass
import Security

@dataclass
class Labour:
    Labour_id: str
    Labour_firstname: str
    Labour_lastname: str
    Labour_DOB: str
    Labour_age: int
    Labour_salary: float
    Labour_type: str
    Labour_exprence: int

    def __init__(self ,lid ,firstname ,lastname ,DOB ,age ,salary ,ltype ,exprence ,passcode):
        self.Labour_id = lid
        self.Labour_firstname = firstname
        self.Labour_lastname = lastname
        self.Labour_DOB = DOB
        self.Labour_age = age
        self.Labour_salary = salary
        self.Labour_type = ltype
        self.Labour_exprence = exprence
        self.passcode = Security.User_Passcode(passcode)
    
    def print_labour(self):
        print("id code : " + self.Labour_id)
        print("Name : " + self.Labour_firstname + "." + self.Labour_lastname)
        print("Type : " + self.Labour_type)
        print("Date of birth : " + self.Labour_DOB)
        print("Age : " + self.Labour_age)
        print("Salary : " + str(self.Labour_salary))
        print("Exprence : " + str(self.Labour_exprence + "years"))
    
    def Security_check(self ,passcode):
        flag = False
        count = 0
        Max_trys = 5
        while (flag is not True) and (count < Max_trys):
            if count == 0:
                flag = self.passcode.Password_entry(passcode)
                count += 1
            else:
                print("NUMBER OF TRYS REMAINING IS " + str(Max_trys - count))
                flag = self.passcode.Password_entry(getpass.getpass(prompt = "Enter the Passcode again : "))
                count += 1
