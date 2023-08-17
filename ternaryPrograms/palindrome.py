# a program to find whether the given word is palindrome or not by using Ternary Operator

print("\tTO FIND PALINDROME WORD")
print("-"*40)

word = input("Enter a word: ")
result = "is Palindrome word" if word==word[::-1] else "is not Palindrome word"

print("{} --> {}".format(word, result))