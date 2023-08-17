#Use bitwise operators inside forloop with list input of integer elements
# & | ~ ^

lst = [100, 200]

print("-"*50)
print("\tList of values = [100, 200]")
print("-"*50)


for i in range(0,1):
    print("\tBitwise Operators")
    print("\n\t{} & {} = {}".format(lst[0], lst[1], lst[0] & lst[1]))
    print("\t{} | {} = {}".format(lst[0], lst[1], lst[0] | lst[1]))
    print("\t{} ^ {} = {}".format(lst[0], lst[1], lst[0] ^ lst[1]))
    print("\t~100 = {}, ~200 = {}".format(~(lst[0]), ~(lst[1])) )

print("="*50)
