from time import sleep
from os import system
from getpass import getpass

class Security:
	@staticmethod
	def activite_labour(Labour):
		system("cls")
		count = 0
		Max_try = 5
		while not(Labour.State["Locked"]):
			code = getpass("Enter the Passcode : ", "*")
			count += 1
			if (code == Labour.Passcode):
				return True
			else:
				if (count < Max_try):
					if ((Max_try - count) > 1):
						print(f"you have {Max_try - count} trys left left.....")
						sleep(1)
					else:
						print("you have a single try left left.....")
						sleep(1)
				else:
					sleep(5)
					Labour.State["Locked"] = True
					print(f"{Labour.Acc_Number} This account is locked......")
					print("This account can only be unlocked by Manager....")

		return False