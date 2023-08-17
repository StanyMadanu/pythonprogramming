# a program to find a prime number

number = int(input("Enter any number: "))

for i in range(2,number):
    if number % i == 0:
        print("{} --> is not a Prime Number".format(number))
        break
else:
    print("{} --> is a Prime Number".format(number))