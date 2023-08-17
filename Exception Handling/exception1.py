#Exception Handling Ex1 - Normal Program

print("Program Execution Started")
s1=input("Enter first value: ")
s2=input("Enter second value: ")

#type casting/conversion
a = int(s1) #----------------x ValueError
b = int(s2) #----------------x ValueError

#logic
c = a/b #-----------------x ZeroDivisionError

print("Div =",c)