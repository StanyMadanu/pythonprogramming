# A program to find the leap year

year = int(input("Enter a year: "))

if (year % 4 == 0 or year % 400 == 0):
    print("{} --> is a Leap Year".format(year))
else:
    print("{} --> is not a Leap Year".format(year))