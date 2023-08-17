# Program to accept a line text and display in reverse order without using slicing

text = input("Enter a line of text/word:  ")

print("By using slicing")
reversetext = text[::-1]
print(reversetext)

print("By using logic")
rtext= ""
for ind in range(len(text)-1, -1, -1):
    rtext = rtext + text[ind]
else:
    print("Given line: {}".format(text))
    print("Reversed line: {}".format(rtext))
