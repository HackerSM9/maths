def addition():
    x = int(input("Enter Number One: "))
    y = int(input("Enter Number Two: "))
    s = x + y
    print(f"The Sum of Two is : {s}")

def subtraction():
    x = int(input("Enter Number One: "))
    y = int(input("Enter Number Two: "))
    s = x - y
    print(f"The Sum of Two is : {s}")

def multiplication():
    x = int(input("Enter Number One: "))
    y = int(input("Enter Number Two: "))
    s = x * y
    print(f"The Sum of Two is : {s}")

def division():
    x = int(input("Enter Number One: "))
    y = int(input("Enter Number Two: "))
    s = x / y
    if y == 0:
        raise ValueError("Cannot divide by zero")
    else:
        print(s)
    
def square_root():
    num = int(input('Enter a number to find its square root: '))
    print (num ** 2)

def cube_root():
    num = int(input('Enter a number to find the cube of it: '))
    print ((num ** 3))