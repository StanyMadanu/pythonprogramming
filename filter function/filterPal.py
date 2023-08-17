#Program to take input list of words and filter them which are palindrome

def readWords():
    lst = list()
    n = int(input("Enter how many words u have: "))
    if n<=0:
        return lst
    else:
        for i in range(1,n+1):
            word=input("Enter {} word: ".format(i))
            lst.append(word)
        return lst
    

#main program
words= readWords()

if(len(words)==0):
    print("List is Empty")
else:
    palwords = list(filter(lambda word: word==word[::-1], words))
    print("Given Words: {}".format(words))
    print("List of Palindrome: {}".format(palwords))
