# Program to find greatest number among 12 numbers using nested if

num1 = 20
num2 = 20
num3 = 20

if num1 > num2:
    if num1 > num3:
        print(num1, "is greater")
    else:
        if num2 > num1:
            if num2 > num3:
                print(num2, "is greater")
            else:
                if num3 > num1:
                    if num3 > num2:
                        print(num3, "is greater")
else:
    if num1 > num3:
        print(num1, "is greater")
    else:
        if num2 > num1:
            if num2 > num3:
                print(num2, "is greater")
            else:
                if num3 > num1:
                    if num3 > num2:
                        print(num3, "is greater")
        else:
            if num2 > num3:
                print(num2, "is greater")
            else:
                if num3 > num1:
                    if num3 > num2:
                        print(num3, "is greater")