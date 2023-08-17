#Program to find large and small numbers among 3 values without using "and" operator

big = lambda a,b,c: a if b<=a>c else b if a<b>=c else c if a<=c>b else "All are same"
small = lambda d,e,f: d if e>=d<f else e if d>e<=f else f if d>=f<e else "All are same"

#main program
x = float(input("Enter 1'st value: "))
y = float(input("Enter 2'nd value: "))
z = float(input("Enter 3'rd Value: "))

#function calls
res1 = big(x,y,z)
res2 = small(x,y,z)

print("big()= {}".format(res1))
print("small()= {}".format(res2))