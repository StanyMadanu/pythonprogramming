# a program to output multiplication table of a given number

print("="*50)
table = int(input("\tEnter a table number: "))
print("="*50)

for i in range(1,11):
    print(table, "X", i, "=", table*i)

print("="*50)
