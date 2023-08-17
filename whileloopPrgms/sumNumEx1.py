# A program to find the sum of 1 to n numbers

n = int(input("Enter any number: "))

if(n<0):
    print("Invalid input")
else:
    sum = 0
    i = 1
    while(i<=n):
        sum = sum + i
        print(i)
        i = i + 1
    else:
        print("Sum of all numbers = {}".format(sum))
