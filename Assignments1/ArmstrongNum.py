# A Program to find the ARMSTRONG number

number = int(input("Enter any number: "))

#converting given int to string
strnum = str(number)

#length of given number
strnumlen = int(len(strnum))

#converting & separating string values to int and storing in another variables
strnum1 = int(strnum[0])
strnum2 = int(strnum[1])
strnum3 = int(strnum[2])

#Formula
sum = strnum1**strnumlen + strnum2**strnumlen + strnum3**strnumlen

#if statement
if (number == sum):
    print("{} ---> is an Armstrong Number".format(number))
else:
    print("{} ---> is not an Armstrong Number".format(number))