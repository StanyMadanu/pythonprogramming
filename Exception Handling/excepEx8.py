#Exception Handling - Final Syntax in another way

s1 = input("Enter first value: ")
s2 = input("Enter second value: ")

try:
    a = int(s1) #valueError posibility
    b = int(s2) #valueError posibility
    c = a / b #zero divison error posibility
    d = "python"
    e = d[2]
except (ValueError, ZeroDivisionError, IndexError):
    print("Don't enter empty spaces, alphanumerics, string and special symbols..!!")
    print("Don't enter zero in denominator..!!")
    print("Index value out of range..!")
except:
    print("Oops.. something went wrong..!!")
else:
    print(e)
    print("Div =",c)
finally:
    print("Program Execution Completed")