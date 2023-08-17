# A program to find the sum of digits of given +ve number

num = int(input("Enter a Number: "))

if(num<=0):
    print("Invalid input")
else:
    sum = 0
    while(num>0):
        reminder = num % 10
        sum = sum + reminder
        num = num//10
    else:
        print("Sum of Digits for given number is: {}".format(sum))