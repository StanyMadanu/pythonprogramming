# a program to find the first and last letters are same or not in the given word by using Ternary Operator
print("\tEnter a word to find the 1st and last letters are same or not")
print("-"*80)

word = input("Your word: ")
result = "First and Last letters are same" if word[0]==word[-1] else "First and Last letters are not same"

print(result)
