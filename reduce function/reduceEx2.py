#Program to take values dynamically from KBD and find the sum of all values by reduce()
import functools as f

n = int(input("Enter how many numbers you have: "))
lst = []

def takevals(x):
    if(n<=0):
        print("Invalid input..!")
    else:
        for i in range(1,n+1):
            val = int(input("Enter {} Value: ".format(i)))
            lst.append(val)
        return lst
    
    
#main program
res = takevals(n)
print("Given Values: {}".format(res))
sumv = f.reduce(lambda x,y: x+y,res)
print("Sum = {}".format(sumv))