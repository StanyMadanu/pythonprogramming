# A program to print example 4th pattern 

rows = int(input("Enter rows for 4th pattern: "))

for i in range(rows):
    for j in range(rows-i):
        print(j+1, end=' ')
    print()
for i in range(rows):
    for j in range(i+1):
        print(j+1, end=' ')
    print()

#------------------------------------------------------
print("-"*40)

#Alphabets pattern
Alph_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

for i in range(rows):
    for j in range(rows-i):
        print(Alph_list[j], end=' ')
    print()
for i in range(rows):
    for j in range(i+1):
        print(Alph_list[j], end=' ')
    print()