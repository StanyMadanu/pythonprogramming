# A program to print square pattern

rows = int(input("Enter rows :"))

for i in range(rows): #rows
    for j in range(rows): #columns
        print("*", end=' ')
    print()

#-----------------------------------------------
print("-"*40)
#-----------------------------------------------

for i in range(rows):
    for j in range(1, rows+1):
        print(j, end=' ')
    print()

#-----------------------------------------------
print("-"*40)
#-----------------------------------------------

for i in range(rows):
    for j in range(rows):
        print(i+1, end=' ')
    print()

#-----------------------------------------------
print("-"*40)
#-----------------------------------------------

Alph_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

for i in range(rows):
    for j in range(rows):
        print(Alph_list[j], end=' ')
    print()

print("-"*40)

for i in range(rows):
    for j in range(rows):
        print(Alph_list[i], end=' ')
    print()