

def posDecide(x):
    if x>0:
        return True
    else:
        return False
    

def negDecide(x):
    if x<0:
        return True
    else:
        return False
    
    

#main program
n = int(input("Enter how many number u have: "))
lst = []

def takeValues(n):
    if n<=0:
        print("Invalid input..!")
    else:
        for i in range(1,n+1):
            value = int(input("Enter {} value:".format(i)))
            lst.append(value)
        else:
            print(lst)


takeValues(n) #function call
poslist = list(filter(posDecide, lst))
neglist = list(filter(negDecide,lst))

print("Given list:{}".format(lst))
print("Positive list:{}".format(poslist))
print("Negative list:{}".format(neglist))