# A program to find the largest number among 3 numerical values by using Ternary Operator

num1 = int(input("Enter the 1st Number: "))
num2 = int(input("Enter the 2nd Number: "))
num3 = int(input("Enter the 3rd Number: "))

res= num1 if num1>num2 and num1>num3 else "All the numbers are equal" if num1==num2==num3 else "1st and 2nd numbers are largest and are equal" if num1==num2 else "1st and 3rd numbers are largest and are equal" if num1==num3 else num2 if num2>num1 and num2>num3 else "2nd and 3rd are largest numbers and are equal" if num2==num3 else num3 if num3>num1 and num3>num2 else "Not a number"


print("Among {}, {}, {} the largest number is = {}".format(num1, num2, num3, res))

