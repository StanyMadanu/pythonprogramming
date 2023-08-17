# Python Program to remove a specific digit from every element of the list

lst = [534, 4352, 5235, 5102, 1525]

digitToRemove = 5
result = []

for i in lst:
    strVal = str(i).replace(str(digitToRemove), '')
    result.append(int(strVal))
else:
    print('-'*50)
    print("Removing digit 5 in specific element in the given list")
    print('-'*50)
    print("Original List: {}".format(lst))
    print("\nModified List: {}".format(result))
    print('-'*50)
