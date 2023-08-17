# a program to find whether the given word is palindrome or not - by using simple if statements

word = input("Enter any word: ")

if(word[0]==word[-1]):
    print("{} ---> is a PALINDROME word".format(word))
if(word[0]!=word[-1]):
    print("{} ---> is not a PALINDROME word".format(word))