# Program to accept list of names and sorting them in ascending and decending order

n = int(input("How many friends you have: "))

if(n<=0):
    print("Make some friends...😑")
else:
    names = list()
    for i in range(1, n+1):
        val = input("Enter friend {}".format(i))
        names.append(val)
    else:
        print("-"*50)
        print("Your friends are {}, total {}".format(names, len(names)))
        names.sort()
        print("Ascending order {}".format(names))
        names.sort(reverse=True)
        print("Descending order {}".format(names))
        print("-"*50)
