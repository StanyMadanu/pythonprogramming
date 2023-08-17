# Program to find strings with given substring in list

lst =["apple","banana", "pineapple", "mango", "custardapple"]

updatedlst = []

for i in lst:
    if(i.endswith("apple")):
        updatedlst.append(i)
else:
    print("-"*50)
    print("Original List:{}".format(lst))
    print("\nList of words contains only apples:{}".format(updatedlst))
    print("-"*50)
