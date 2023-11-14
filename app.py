import sys,os
from modules import sprint as sp
from modules import banner as bn
from modules import maths as mt
from colorama import Fore,Style

os.system("clear")

bn.ban()
print("""
1) ADDITION
2) SUBTRACTION
3) MULTIPLICATION
4) DIVISION
5) SQUARE ROOT
6) CUBE ROOT
7) EXIT
""")

choose = "Choose your Equation: "
sp.sprint(input(choose))

if choose == '1':
    num1 = input('Enter the first number: ')
    num2 = input('Enter the second number: ')
    print(f'{num1} + {num2} = ',mt.addition(int(num1), int(num2)))
          elif choose == '2':
          num1 = input('Enter the first number: ')
          num2 = input('Enter the second number: ')
          print(f'{num1} - {num2} = ',mt.subtraction(int(num1), int(num)))
          elif choose == '3':
          num1 = input('Enter the first number: ')
          num2 = input('Enter the second number: ')
          print(f'{num1} * {num2} = ',mt.multiplication(int(num1), int(num)))
          elif choose == '4':