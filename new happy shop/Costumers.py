from dataclasses import dataclass

@dataclass
class Costumer:
    Costumer_firstname: str
    Costumer_lastname: str
    Costumer_phonenumber: str
    Costumer_email: str
    Costumer_sex: str
    Costumer_age: int

    def __init__(self , firstname ,lastname ,phonenumber ,email ,sex ,age):
        self.Costumer_firstname = firstname
        self.Costumer_lastname = lastname
        self.Costumer_phonenumber = phonenumber
        self.Costumer_email = email
        self.Costumer_sex = sex
        self.Costumer_age = age
