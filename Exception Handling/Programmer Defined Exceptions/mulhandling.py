#program to handle the programmer defined exceptions
from mulhitting import multable
from muldef import NegativeNumError, ZeroError

try:
    print("\tProgram Execution Started")
    n = int(input("Which Mul table you want: "))
    multable(n)
except NegativeNumError:
    print("\tDon't Enter Negative Number..!")
except ZeroError:
    print("\tDon't Enter Zero..!")
except ValueError:
    print("\tDon't enter string, alnums, space and special symbols...!")
finally:
    print("\tProgram Execution Completed")
