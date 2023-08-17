#Exception Handling Ex1 - Normal Program
try:
    print("========try block==========")
    print("Program Execution Started")
    s1=input("Enter first value: ")
    s2=input("Enter second value: ")

    #type casting/conversion
    a = int(s1) #----------------x ValueError
    b = int(s2) #----------------x ValueError
    #logic
    c = a/b #-----------------x ZeroDivisionError

except ValueError:
    print("\n=====except block==================")
    print("Don't Enter Strings, Symbols, Spaces and Alphanumeric")
except ZeroDivisionError:
    print("\n=====except block================")
    print("Don't enter zero as denominator")
else:  #option
    print("\n=====else block======")
    print("Value of a =",a)
    print("Value of b =",b)
    print("Div =",c)
finally:
    print("\nIam from finally block")