#Program to accept 2 numerical values and display largest number among them 
#by using Anonymous Function

biggest = lambda a,b: a if a>b else b if a<b else "Both are equal"
small = lambda c,d: c if c<d else d if c>d else "Both are equal"



#main program
x = float(input("Enter 1'st value: "))
y = float(input("Enter 2'nd value: "))
res=biggest(x,y) #anony..function call
print("Biggest() = {}".format(res))
res2=small(x,y)
print("Small() = {}".format(res2))
