# Program to swapcase of text/word by using functions

def wordswap(word):
    res = ""
    for ch in word:
        if ch.isupper():
            res = res + ch.lower()
        elif ch.islower():
            res = res + ch.upper()
        elif ch.isspace():
            res = res + ch
    return res


# main program
word = input("Enter word/sentence: ")
swapword = wordswap(word)

print("Given word = {}".format(word))
print("Swapped case = {}".format(swapword))
