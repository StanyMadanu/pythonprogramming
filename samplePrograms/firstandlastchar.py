#program to find the first and last letters are same or not
#using python ternary operator

word = input("Enter the word:")
res = "1st and last letters are same" if word[0]==word[-1] else "1st and last letters are not same"

print("{} word of : {}".format(word, res))