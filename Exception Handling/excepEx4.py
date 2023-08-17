#Exception Handling - Syntax-2

s1 = input("Enter first value: ")
s2 = input("Enter second value: ")

try:
    a = int(s1) #valueError posibility
    b = int(s2) #valueError posibility
    c = a / b #zero divison error posibility
except (ValueError, ZeroDivisionError):
    print("Don't enter empty spaces, alphanumerics, string and special symbols..!!")
    print("Don't enter zero in denominator..!!")
else:
    print("Div =",c)
finally:
    print("Program Execution Completed")