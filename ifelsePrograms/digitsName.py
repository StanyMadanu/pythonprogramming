# a program to display name of the any digits

numdict = {0:"Zero", 1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine"}
num = int(input("Enter a digit: "))

if num in numdict.keys():
    print("{} ---> {}".format(num, numdict.get(num)))
else:
    print("I told you enter any digit but you entered number 🤣")
    print("**number is nothing but the combination of 2 or more digits**")

