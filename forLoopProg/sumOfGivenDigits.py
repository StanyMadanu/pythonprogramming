# A program to find the sum of digits on given +ve number by using for loop

num = int(input("Enter a number: "))

if(num<=0):
    print("Invalid input")
else:
    sum = 0
    x = str(num)
    for i in x:
        i = int(i)
        sum = sum + i
    else:
        print("Sum of Digits : {}".format(sum))
