def addition(x,y):
    return x + y

def subtraction(x,y):
    return x - y

def multiplication(x,y):
    return x * y

def division(x,y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    else:
        return x / y
    
def squareroot():
    num = int(input('Enter a number to find its square root: '))
    print (num ** 2)

def cuberoot():
    num = int(input('Enter a number to find the cube of it: '))
    print ((num ** 3))