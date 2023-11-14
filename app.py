import sys,os
from modules import sprint as sp
from modules import banner as bn
from modules import maths as mt
from colorama import Fore

os.system("clear")

bn.ban()
print(Fore.LIGHTMAGENTA_EX + """
1) ADDITION
2) SUBTRACTION
3) MULTIPLICATION
4) DIVISION
5) SQUARE ROOT
6) CUBE ROOT\n"""
+ Fore.LIGHTRED_EX + 
"""0) EXIT
""")

Q = int(input(Fore.LIGHTYELLOW_EX + "Choose your Equation: "))

if Q == 1:
    mt.addition()

elif Q == 2:
    mt.subtraction()

elif Q == 3:
    mt.multiplication()

elif Q == 4:
    mt.division()

elif Q == 5:
    mt.square_root()

elif Q == 6:
    mt.cube_root()

elif Q == 0:
    sp.sprint("\n"+Fore.LIGHTRED_EX+"Exiting...\n")

else:
    sp.sprint("\n"+Fore.LIGHTRED_EX+"Exiting...\n")