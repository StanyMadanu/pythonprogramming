#Program to convert word to uppercase by using Anonymous function

convertWord = lambda word: word.upper()

#main program
w = input("Enter a word/line: ")

res= convertWord(w)

print("Given word/line: {}".format(w))
print("Converted word/line: {}".format(res))