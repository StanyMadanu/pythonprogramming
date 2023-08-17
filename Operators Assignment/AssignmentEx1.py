#Program to find largest number of two given values - by using Assignment Operators inside conditional statements

print("\tProgram to find largest number")
print("-"*50)
num1 = int(input("\tEnter 1'st Value: "))
num2 = int(input("\tEnter 2'nd Value: "))

print("="*50) #decorate purpose

#conditional statement
# using '>' greater than, '<' less than and '==' double equal operators
if (num1 > num2):
    print("\t{} > {} = {} is the largest number".format(num1, num2, num1))
elif (num1 < num2):
    print("\t{} < {} = {} is the largest number".format(num1, num2, num2))
elif (num1 == num2):
    print("\t{} == {} both are equal numbers".format(num1, num2))

print("="*50) #decorate purpose

