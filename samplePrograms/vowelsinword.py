#a program to find whether vowels present in a given word

word = input("Enter the word:")

if "a" in word:
    print("{} has a vowel--> {}".format(word,"a"))
elif "e" in word:
    print("{} has a vowel--> {}".format(word,"e"))
elif "i" in word:
    print("{} has a vowel--> {}".format(word,"i"))
elif "o" in word:
    print("{} has a vowel--> {}".format(word, "o"))
elif "u" in word:
    print("{} has a vowel--> {}".format(word, "u"))
else:
    print("{} has no vowels".format(word))
