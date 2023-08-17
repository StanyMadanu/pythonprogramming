# a program to find the whether the given number is even or odd by using Ternary Operator
print("-"*60)
print("\tProgram to find whether the given is Even and Odd")
print("-"*60)

num = int(input("Enter the number: "))
res = "an even Number" if num%2==0 else "a odd Number"

print("\t{} is {}".format(num, res))
print("="*60)