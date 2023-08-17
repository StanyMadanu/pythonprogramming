#list data type pre-defined functions

l1 = [] #empty list

print("="*80)

#append() function
l1.append(10)
l1.append("Python")
l1.append(20)
l1.append(2+3j)
l1.append(True)
print("Values added to list using append()=",l1)

#insert() function
l1.insert(1,20)
l1.insert(6,"Java")
l1.insert(4,"ReactJS")
print("Values inserted using insert()=",l1)

#remove() function
l1.remove("ReactJS")
print("ReactJS is removed using remove()=",l1)

#pop() function
l1.pop() #removes last value in the list
print("pop() function removes last value in the list=",l1)

#pop(index) function
l1.pop(0)
print("pop(index) removes specified index value = ",l1)

#index() function
indv = l1.index("Python")
print("index()--> returns specificed value index position=",indv)

#count() function
cnt = l1.count(20)
print("count()---> returns number of occurances of given value =",cnt)

#extend() function
l2 =[100,200,300]
l1.extend(l2)
print("l1 extented values of l2 using extend() =",l1)

#reverse() function
l1.reverse()
print("reverse()---->",l1)

#sort()
l3 =[9,-299, 10, 5, 0, 300, -900]
print("\nlist 3 without sort()----->",l3)
l3.sort()
print("list 3 with sort()----->",l3)


print("="*80)