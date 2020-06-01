from time import sleep
import getpass

Passcode = 7474
flag = True
wait = 10
while flag == True:
    Passcode2 = int(getpass.getpass(prompt = "Enter the PASSCODE : "))
    if Passcode2 == Passcode:
        print("Welcome BOSS...")
        flag = False
    else:
        for i in range(wait):
            print("Wait for " + str(wait - i) + ".")
            sleep(1)
