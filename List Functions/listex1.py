#Python program to Sum of number digits in List

l1 = [1,2,3,4]
sum = 0

print("="*50)
print("\tList Values:",l1)
print("="*50)
for i in l1:
    sum = sum + i
    print("\t\t",i)
else:
    print("="*50)
    print("\tSum of all values =",sum)
    print("="*50)


