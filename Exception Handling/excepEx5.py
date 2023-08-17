#Exception Handling - Syntax-3

s1 = input("Enter first value: ")
s2 = input("Enter second value: ")

try:
    a = int(s1) #valueError posibility
    b = int(s2) #valueError posibility
    c = a / b #zero divison error posibility
except ValueError as v:
    print(v)
except ZeroDivisionError as z:
    print(z)
else:
    print("Div =",c)
finally:
    print("Program Execution Completed")