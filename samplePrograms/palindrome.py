#a program to find the whether the given value is palindrome or not
#using python ternary operator

word = input("Enter the word:")
result = "is a Palindrome" if word==word[::-1] else "is not a Palindrome"

print("{} ---> {}".format(word, result))