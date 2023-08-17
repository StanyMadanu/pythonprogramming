#Program to find the word is palindrom or not by using Anonymous function

isPalindrom = lambda word: "is Palindrome" if word == word[::-1] else "not a Palindrome"

#main program
w = input("Enter a word to check it is palindrome or not: ")
res = isPalindrom(w)

print("Given word: {}".format(w))
print("Reversed word: {}".format(w[::-1]))
print("{}-->{}".format(w,res))
