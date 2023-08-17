#Program to separate even and odd numbers separtely from given list

nums = []

def takeNums():
    num = int(input("How many number u have: "))
    if (num<=0):
        return nums
    else:
        for i in range(1,num+1):
            n = int(input("Enter {} Number: ".format(i)))
            nums.append(n)
        return nums


#main program
takeNums()  
even= list(filter(lambda x: x%2==0,nums))
odd = list(filter(lambda x: x%2!=0, nums))
print("Given numbers = {}".format(nums))

print("List of Even numbers = {}".format(even))
print("List of Odd numbers = {}".format(odd))