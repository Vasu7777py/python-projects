from time import sleep
from os import system
from getpass import getpass

import security

class Labour:
	def __init__(self, Acc_Number:str, Labour_Class:str, FirstName:str, LastName:str, Age:int, Sex:str, Phone_number:list):
		self.Acc_Number = Acc_Number
		self.Labour_Class = Labour_Class

		self.FirstName = FirstName
		self.LastName = LastName
		self.Age = Age
		self.Sex = Sex
		self.Phone_number = Phone_number

		self.Passcode = None

		self.State = {
			"Locked" : True,
			"Active" : False
		}

	def Assign_Labour_Passcode(self):
		system("cls")
		while self.State["Locked"]:
			Passcode = getpass("Enter the Passcode : ", "*")
			re_entred_Passcode = getpass("Enter the Passcode again : ", "*")
			if (Passcode == re_entred_Passcode):
				self.Passcode = Passcode
				self.State["Locked"] = False
				print("Now try to Login.... \n\n")
				sleep(4)
				if security.Security.activite_labour(self):
					return True
				else:
					return False

	def Forgot_Labour_Passcode(self):
		system("cls")
		while self.State["Locked"]:
			New_Passcode = getpass("Enter the New Passcode : ", "*")
			re_entred_Passcode = getpass("Enter the Passcode again : ", "*")
			if (New_Passcode == re_entred_Passcode):
				self.State["Locked"] = False
				print("Now try to Login... \n\n")
				sleep(4)
				if security.Security.activite_labour(self):
					return True
				else:
					return False

	def get_Labour_Data(self):
		system("cls")
		sleep(0.25)
		print(f"Acc_Number : {self.Acc_Number}")
		print(f"Labour_Class : {self.Labour_Class}")
		print(f"Name : {self.FirstName}.{self.LastName}")
		print(f"Phone_number : {self.Phone_number}")
		print(f"Age : {self.Age}")
		print(f"sex : {self.Sex}")

def main():
	labour = Labour("7RTX47", "s", "Vasu", "Subbannavar", 18, "Male", ["7899927254", "9945177254", "9845131421"])
	labour.Assign_Labour_Passcode()
	labour.get_Labour_Data()

if __name__ == "__main__":
	main()