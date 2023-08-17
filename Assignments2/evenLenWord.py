# Program to find the even-length words from a given list of words and sort them by length

lst = ["building","pen","bullettrack", "ball", "birds", "TS", "pencil", "blanket", "S", "ninetynine" ]
result = []
print("-"*50)

for i in lst:
    if (len(i)%2 == 0):
        print("\t{} ---> even length = {}".format(i, len(i)))
        result.append(i)  
        result.sort()
else:
    print("-"*50)
    print(result)
    print("-"*50)


#for j in range(0,len(result)):
#   print(max(len(result[j])))

    