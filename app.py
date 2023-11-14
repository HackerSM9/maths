import sys,os
from modules import sprint as sp
from modules import banner as bn
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