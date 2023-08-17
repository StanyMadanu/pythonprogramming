# A program to print pattern example 3

rows = int(input("Enter rows: "))

# * symbol pattern
for i in range(rows):
    for j in range(i+1):
        print("*", end=' ')
    print()

for i in range(rows):
    for j in range(rows-i):
        print("*", end=' ')
    print()
    
#------------------------------------------
print("-"*40)

# Numbers pattern
for i in range(rows):
    for j in range(i+1):
        print(j+1, end=' ')
    print()
for i in range(rows):
    for j in range(rows-i):
        print(j+1, end=' ')
    print()

#------------------------------------------
print("-"*40)

Alph_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# Alphabets pattern
for i in range(rows):
    for j in range(i+1):
        print(Alph_list[j], end=' ')
    print()
for i in range(rows):
    for j in range(rows-i):
        print(Alph_list[j], end=' ')
    print()

