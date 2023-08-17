# A program to print 6th pattern

rows = int(input("Enter rows: "))

print("-"*50)
print("\tEx:6 - Symbols pattern")
print("-"*50)

for i in range(rows):
    for j in range(rows-i-1):   #to print spacing
        print(" ",end='')
    for j in range(i+1):    # to print number of stars in a row
        print("*", end=' ')
    print()

#--------------------------------------
print("-"*50)
print("\tEx:6 - Number pattern")
print("-"*50)

for i in range(rows):
    for j in range(rows-i-1):
        print(" ", end='')
    for j in range(i+1):
        print(j+1, end=' ')
    print()

#--------------------------------------
print("-"*50)
print("\tEx:6 - Alphabets pattern")
print("-"*50)

Alph_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

for i in range(rows):
    for j in range(rows-i-1):
        print(" ", end='')
    for j in range(i+1):
        print(Alph_list[j], end=' ')
    print()
