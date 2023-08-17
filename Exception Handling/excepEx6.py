#Exception Handling - Syntax-4

s1 = input("Enter first value: ")
s2 = input("Enter second value: ")

try:
    a = int(s1) #valueError posibility
    b = int(s2) #valueError posibility
    c = a / b #zero divison error posibility
except: #default except block
    print("Ooops..! Something Went Wrong..!!")
else:
    print("Div =",c)
finally:
    print("Program Execution Completed")