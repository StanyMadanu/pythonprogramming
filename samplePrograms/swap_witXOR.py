# Swapping two numerical values using Bitwise XOR Operator
#Bitwise XOR operator won't accept string and float values

a = int(input("Enter the 'a' Value: "))
b = int(input("Enter the 'b' Value: "))

print("-"*30)
print("Original Value of a : {}".format(a))
print("Original Value of b : {}".format(b))

#Swapping values with XOR Operator
a = a^b
b = a^b
a = a^b

print("-"*30)
print("Swapped Value of a : {}".format(a))
print("Swapped Value of b : {}".format(b))
print("="*30)
