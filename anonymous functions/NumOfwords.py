#Program to find the number of words in a sentence by using anonymous function

wordCount = lambda words: len(words.split())

#main program
w = input("Enter a word/sentence to count of words: ")
res = wordCount(w)

print("Count of words: {}".format(res))

