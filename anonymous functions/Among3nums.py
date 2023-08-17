big=lambda a,b,c: a if a>=b and a>c else b if b>a and b>=c else c if c>=a and c>b else "All are equal"
small=lambda x,y,z: x if x<=y and x<z else y if y<x and y<=z else z if z<=x and z<y else "All are equal"

#main program
x = float(input("Enter value 1: "))
y = float(input("Enter value 2: "))
z = float(input("Enter value 3: "))
res=big(x,y,z)
res1=small(x,y,z)
print("big() = {}".format(res))
print("small() = {}".format(res1))