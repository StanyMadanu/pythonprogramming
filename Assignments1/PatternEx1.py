# A Program to print left triangle pattern

rows = int(input("Enter rows: "))

# prinitng * symbol 
for i in range(rows):
    for j in range(i+1):
        print("*", end=' ')
    print()

#-----------------------------------------------------
print("-"*40)

#printing numbers
for i in range(rows):
    for j in range(i+1):
        print(j+1, end=' ')
    print()

#-----------------------------------------------------

print("-"*40)
#printing same numbers in row
for i in range(rows):
    for j in range(i+1):
        print(i+1, end=' ')
    print()

#-----------------------------------------------------
print("-"*40)

Alph_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

for i in range(rows):
    for j in range(i+1):
        print(Alph_list[j], end=' ')
    print()

#------------------------------------------------
print("-"*40)
#------------------------------------------------

# Same Alphabet in row
for i in range(rows):
    for j in range(i+1):
        print(Alph_list[i], end=' ')
    print()