
def sumop(a,b):
    c = a + b
    return c

#main program
a = float(input("Enter first value: "))
b = float(input("Enter second value: "))
c = sumop(a,b)

print("Sum ({}, {}) = {}".format(a,b,c))
print("-"*50)
print(type(sumop))