#ProDef3.py ----------- main program

from ProDef2 import Division
from ProDef1 import ZeroError

a = int(input("Enter a value: "))
b = int(input("Enter b value: "))

try:
    c = Division(a,b) #function call ---- gives result / exception
except ZeroError:
    print("Don't enter zero in denominator")
else:
    print(c)
finally:
    print("Program Execution is completed")


