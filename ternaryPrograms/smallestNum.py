# A program to find the smallest number and are equal by using Ternary Operator

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
num3 = int(input("Enter 3rd number: "))

res = num1 if num1<num2 and num1<num3 else "All the numbers are equal" if num1==num2==num3 else "1st and 2nd numbers are smallest and equal" if num1==num2 else "1st and 3rd numbers are smallest and equal" if num1==num3 else num2 if num2<num1 and num2<num3 else "2nd and 3rd numbers are smallest and equal" if num2==num3 else num3 if num3<num1 and num3<num2 else "Not a number"

print("Among {}, {}, {} the smallest number is = {}".format(num1, num2, num3, res))