# A program to print example pattern 5
rows = int(input("Enter rows to print 5th pattern: "))

for i in range(rows):
    for j in range(rows-i, -1, -1):
        print(j+1, end=' ')
    print()

for i in range(rows):
    for j in range(i, -1, -1):
        print(j + 1, end=' ')
    print()
    


    