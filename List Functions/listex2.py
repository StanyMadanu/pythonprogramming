#Python | Multiply all numbers in the list

print("Enter values with space separated to multiply")
l1 = [int(n) for n in input().split()]
mul = 1

print("\tList Values: ",l1)
print("="*50)
for i in l1:
    mul = mul * i
    print("\t\t",i)
else:
    print("="*50)
    print("\tMul of all numbers =",mul)
    print("="*50)
