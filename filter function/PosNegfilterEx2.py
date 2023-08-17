#positive and negative numbers separationg with dynatic input values

n = int(input("How many numbers you want: "))

lst = []

for i in range(1,n+1):
    if n<=0:
        print(lst)
    else:
        gv=int(input(("Enter {} value: ".format(i))))
        lst.append(gv)
print("List of given values: {}".format(lst))


#function
pos = lambda x: x>0
neg = lambda x: x<0

#postive values
print("Positive values: ",list(filter(pos,lst)))
print("Negative values: ",list(filter(neg,lst)))