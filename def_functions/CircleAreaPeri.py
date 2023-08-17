# Program to calculate Area and perimeter of a circle by using functions

def area(r):
    ac = 3.14 * r ** 2
    print("Area of Circle = {}".format(ac))


def peri():
    r = float(input("Enter Radios to Cal Perimeter: "))
    pc = 2 * 3.14 * r
    print("Perimeter of Circle = {}".format(round(pc, 2)))


# main program
r = float(input("Enter Radios to Calculate Area: "))
area(r)
print('-'*50)
peri()
