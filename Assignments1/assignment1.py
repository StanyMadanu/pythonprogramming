# A program to find the largest number among given 9 numbers

print("\tPROGRAM TO FIND THE LARGEST NUMBER")
print("="*60)

num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))
num3 = int(input("Enter the 3rd number: "))
num4 = int(input("Enter the 4th number: "))
num5 = int(input("Enter the 5th number: "))
num6 = int(input("Enter the 6th number: "))
num7 = int(input("Enter the 7th number: "))
num8 = int(input("Enter the 8th number: "))
num9 = int(input("Enter the 9th number: "))

print("The given numbers are:{},{},{},{},{},{},{},{},{}".format(num1, num2, num3, num4, num5, num6, num7, num8, num9))

#using simple if statement
if num1>num2 and num1>num3 and num1>num4 and num1>num5 and num1>num6 and num1>num7 and num1>num8 and num1>num9:
    print("\t{} is greater number among all 9 numbers".format(num1))
elif num2>num1 and num2>num3 and num2>num4 and num2>num5 and num2>num6 and num2>num7 and num2>num8 and num2>num9:
    print("\t{} is greater number among all 9 numbers".format(num2))
elif num3>num1 and num3>num2 and num3>num4 and num3>num5 and num3>num6 and num3>num7 and num3>num8 and num3>num9:
    print("\t{} is greater number among all 9 numbers".format(num3))
elif num4>num1 and num4>num2 and num4>num3 and num4>num5 and num4>num6 and num4>num7 and num4>num8 and num4>num9:
    print("\t{} is greater number among all 9 numbers".format(num4))
elif num5>num1 and num5>num2 and num5>num3 and num5>num4 and num5>num6 and num5>num7 and num5>num8 and num5>num9:
    print("\t{} is greater number among all 9 numbers".format(num5))
elif num6>num1 and num6>num2 and num6>num3 and num6>num4 and num6>num5 and num6>num7 and num6>num8 and num6>num9:
    print("\t{} is greater number among all 9 numbers".format(num6))
elif num7>num1 and num7>num2 and num7>num3 and num7>num4 and num7>num5 and num7>num6 and num7>num8 and num7>num9:
    print("\t{} is greater number among all 9 numbers".format(num7))
elif num8>num1 and num8>num2 and num8>num3 and num8>num4 and num8>num5 and num8>num6 and num8>num7 and num8>num9:
    print("\t{} is greater number among all 9 numbers".format(num8))
elif num9>num1 and num9>num2 and num9>num3 and num9>num4 and num9>num5 and num9>num6 and num9>num7 and num9>num8:
    print("\t{} is greater number among all 9 numbers".format(num9))
else:
    print("Invalid Number..!")
