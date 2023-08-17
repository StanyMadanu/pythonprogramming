#Python program to find smallest and largest number in a list
from functools import reduce 

l1 = [2,1,0,3]

miniNum = min(l1) #Easy way to find min value with th help of min() function
maxNum = max(l1) #Easy way to find max value with th help of max() function

print("List values:",l1)
print("\nMinimum value:",miniNum)
print("Maximum value:",maxNum)

#without min() function
minV = reduce(lambda x,y:x if x<y else y, l1)
maxV = reduce(lambda x,y:x if x>y else y, l1)
print("\nMinimum Value using reduce() :",minV)
print("Maximum Value using reduce() :",maxV)

#finding min value without pre-defined functions
inVal = l1[0] #assigning initial value of list

for i in range(len(l1)):
    if l1[i] < inVal:
        inVal = l1[i]
else:
    print("\nSmallest value is:",inVal)


#finding max value without pre-defined functions
for i in range(len(l1)):
    if l1[i] > inVal:
        inVal = l1[i]
else:
    print("Largest value is:",inVal)
