# A program to print example of 10th pattern 

rows = int(input("Enter rows for 10th pattern: "))

for i in range(rows):
    for j in range(i+1):
        print(j+1, end=' ')
    print()