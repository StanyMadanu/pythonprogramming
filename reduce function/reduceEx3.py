#Program to find max and min values by accept list of values using reduce()
import functools as f

def findmax(x,y):
    if x>y:
        return x
    else:
        return y
    

def findmin(x,y):
    if x<y:
        return x
    else:
        return y



#main program
print("Enter list of values separated by comma")
lst = [int(n) for n in input().split()]

maxv = f.reduce(findmax,lst)
minv = f.reduce(findmin,lst)
print("List of Vals: {}".format(lst))
print("Max value: {}".format(maxv))
print("Min value: {}".format(minv))
