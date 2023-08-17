import functools

#main program
print("Enter values with space separated")
lst = [int(n) for n in input().split()] # list comprehension
maxv = functools.reduce(lambda x,y: x if x>y else y,lst)
minv = functools.reduce(lambda x,y: x if x<y else y,lst)

print("Given Values: {}".format(lst))
print("Max: {}".format(maxv))
print("Min: {}".format(minv)) 

