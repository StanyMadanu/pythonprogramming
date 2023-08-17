# A program to print pattern 1
n = int(input("Enter any number"))

if(n<0):
    print("Invalid input")
else:
    for i in range(1,n):
        print(i)
        if(i==2):
            continue
    else:
        print("program completed")
