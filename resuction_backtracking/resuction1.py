def factorial(num:int):
    if (num == 0):
        return 1
    return (num * factorial(num -1) )

def main():
    flag = False
    num = None
    while (not(flag)):
        num = int(input("Enter a number to find a Factorial : "))
        if (num < 0):
            print("Can not find a factorial of a negetive number ")
        else:
            flag = True
    Factorial = factorial(num)
    print(f"Factorial of {num} = {Factorial}")

if __name__ == "__main__":
    main()
