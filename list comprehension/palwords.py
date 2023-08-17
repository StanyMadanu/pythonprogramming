#Program to accept list of words from KBD and obtain palindrome words and 
#also find the length and find highest palindrome word length

print("Enter a list of words separated by comma")
lst = [w for w in input().split(",")]

palwords = [ p for p in lst if p==p[::-1]]

plenth = dict( [(w,len(w)) for w in palwords])

for p,pl in plenth.items():
    print("\t{}\t{}".format(p,pl))
print("-"*50)

#code for max length of palindrome
ml = max(plenth.values())
maxword = [w for w,l in plenth.items() if ml==l]

if(len(maxword)==1):
    print("Max length word:{} and its length={}".format(maxword[0],ml))
else:
    for word in maxword:
        print("Max length word:{} and its length={}".format(word,ml))



