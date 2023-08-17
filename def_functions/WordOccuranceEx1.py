#Program to accept a word and find each letter occurance of a word - by using functions
def findoccur():
   word = input("Enter a line/word: ")
   d = {}

   for ch in word:
       if ch not in d:
           d[ch] = 1
       else:
           d[ch] = d[ch] + 1
   return word, d

#main program
w, d = findoccur()
print("Given word or line: {}".format(w))

for let, occ in d.items():
    print("\t{} ---> {}".format(let,occ))