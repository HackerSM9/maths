from colorama import Fore

c = Fore.LIGHTCYAN_EX

def addition():
    x = int(input("\nEnter Number One: "))
    y = int(input("Enter Number Two: "))
    s = x + y
    print(c + f"The Sum of Two is : {s}")

def subtraction():
    x = int(input("\nEnter Number One: "))
    y = int(input("Enter Number Two: "))
    s = x - y
    print(c + f"The Sum of Two is : {s}")

def multiplication():
    x = int(input("\nEnter Number One: "))
    y = int(input("Enter Number Two: "))
    s = x * y
    print(c + f"The Sum of Two is : {s}")

def division():
    x = int(input("\nEnter Number One: "))
    y = int(input("Enter Number Two: "))
    s = x / y
    if y == 0:
        raise ValueError("Cannot divide by zero")
    else:
        print(c + s)
    
def square_root():
    num = int(input('\nEnter a number to find its square root: '))
    print (c + num ** 2)

def cube_root():
    num = int(input('\nEnter a number to find the cube of it: '))
    print ((c + num ** 3))