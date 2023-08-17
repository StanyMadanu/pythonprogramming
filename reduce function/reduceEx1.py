#program to find the sum of values in a given list by using reduce() function
import functools
lst=[10, 20, 30, 40, 50]

def sumop(a,b):
    return a + b

#main program
result = functools.reduce(sumop,lst)
print("Sum of all values: {}".format(result))

