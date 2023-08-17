
def sumop():
    #input
    a = float(input("Enter first value: "))
    b = float(input("Enter second value: "))

    #processing
    c = a + b
    return a, b, c #return kwd can return one or more number of vals

#main program
s, t, n = sumop() #function call with multiline assignment
print("sum ({}, {}) = {}".format(s, t, n))

print("---------------------------------------------")

x = sumop() #function call with single assignment - x is tuple
print(x)
print("sum ({}, {}) = {}".format(x[0], x[1], x[-1]))