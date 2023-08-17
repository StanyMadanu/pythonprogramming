# A program to print example 7th & 8th patterns 
rows = int(input("Enter rows to print 7th & 8th pattern: "))
print("="*50)
print("\t7th Pattern with Numbers & Alphabets ")
print("="*50)

for i in range(rows):
    for j in range(rows-i):
        print(rows-j, end=' ')
    print()

#-------------------------------------------

print("-"*40)
Alph_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

for i in range(rows):
    for j in range(rows-i):
        print(Alph_list[rows-(j+1)], end=' ')
    print()

#=============================================
print("="*50)
print("\t8th Pattern with Numbers & Alphabets")
print("="*50)

for i in range(rows):
    for j in range(i+1):
        print(rows-j, end=' ')
    print()  

#-------------------------------------------

print("-"*40)

for i in range(rows):
    for j in range(i+1):
        print(Alph_list[rows-(j+1)], end=' ')
    print()