#tuple, set, dict data types
s1 = {10,20,30,40,50}
s2 = {"python", "java", "c++", "R", 10, 20, 30}

#add()
s1.add(70)
print(s1)

#remove()
s1.remove(30)
print(s1)

#union
un = s1.union(s2)
print(un)

#intersection
intrsn = s1.intersection(s2)
print(intrsn)

#difference
dif = s1.difference(s2)
print(dif)
dif2 = s2.difference(s1)
print(dif2)

#update
s1.update(s2)
print(s1)

#dict pre-defined functions
di = {10:"Travis", 20:"Rossum", 30:"Musk", 40:"Zukerburg", 50:"Tesla"}

#copy() in dict
d2=di.copy()
print("\nOriginal dict :",di, id(di))
print("Copy dict :",d2, id(d2))

#pop() in dict
d2.pop(30)
print("key-value is removed with pop():",d2)

#popitem() in dict
d2.popitem()
print("popitem() removes last element:",d2)

#clear() in dict
d2.clear()
print("d2 dict removed using clear(): ",d2)

#keys() in dict
di.keys() #----to print this we have to store in object or else print directly
print(di.keys())

#values() in dict
di.values() #----to print this we have to store in object or else print directly
print(di.values())

#items() in dict
print(di.items())

for k,v in di.items():
    print("\t{}---->{}".format(k,v))

#get() in dict
print("\nget() to obtain given value of key=",di.get(50))

#update() in dict
d2.update(di)
print(d2, id(d2)) 
