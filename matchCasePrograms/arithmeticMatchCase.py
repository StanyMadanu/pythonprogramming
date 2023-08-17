# a program for arithmetic operations as a menu driven application by using match case statements
import sys

print("="*50)
print("\tArithmetic Operations")
print("="*50)

print("\t1. Addition")
print("\t2. Substraction")
print("\t3. Multiplication")
print("\t4. Division")
print("\t5. Modulo Division")
print("\t6. Exponentiation")
print("\t7. Exit")

print("="*50)
ch=int(input("Enter Ur Choice: "))

match(ch):
    case 1:
        print("Enter two values for Addition")
        a,b=float(input("")),float(input())
        print("Sum ({},{}) = {}".format(a,b,a+b))
    case 2:
        print("Enter two Values for Substraction")
        a,b = float(input()),float(input())
        print("Sub ({}, {})= {}".format(a, b, a-b))
    case 3:
        print("Enter two values for Multiplication")
        a,b = float(input()),float(input())
        print("Mul ({},{}) = {}".format(a, b, a*b))
    case 4:
        print("Enter two values for Division")
        a,b = float(input()),float(input())
        print("Normal Div ({}, {}) = {}".format(a, b, a/b))
        print("Floor Div ({}, {}) = {}".format(a, b, a//b))
    case 5:
        print("Enter two values for Modulo Division")
        a,b = float(input()),float(input())
        print("Mod Div ({}, {}) = {}".format(a, b, a%b))
    case 6:
        print("Enter two values of Exponentiation")
        a,b = float(input("Enter base: ")), float(input("Enter power: "))
        print("Exponentiation ({}, {}) = {}".format(a, b, a**b))
    case 7:
        print("Thanks for using this application")
        sys.exit()
    case _:
        print("Invalid Selection..!")




