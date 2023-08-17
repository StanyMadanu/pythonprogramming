#String Predefined Functions

text = "python is a oop language"

print("="*70)
print("\ttext =",text)
print("="*70)

#capitalize
cap = text.capitalize()
print("\tCapitalize() =",cap)

#title
titl = text.title()
print("\tTitle() =",titl)

#upper
up = text.upper()
print("\tUpper() =",up)

#lower
low = text.lower()
print("\tLower() =",low)

#count
cnt = text.count("a")
print("\n\tCount of 'a' letter in text =",cnt)

#find
fnd = text.find("a")
print("\tFind Index of 'a' =",fnd) #gives index of first occurance of 'a'

#replace
rep = text.replace("python","Java")
print("\tReplace() from python to Java =",rep)


word = "Python"
print("\n")
print("="*70)
print("\tword =",word)
print("="*70)

#isupper
isup = word.isupper()
print("\t'Python' isupper() =",isup)

#islower
islow = word.islower()
print("\t'Python' islower() =",islow)

#istitle
istitl = word.istitle()
print("\t'Python' istitle() =",istitl)

#isdigit
isdig = word.isdigit()
print("\t'Python' isdigit() =",isdig)

#isalpha
isalp = word.isalpha()
print("\t'Python' isalpha() =",isalp)

#isalnum
isaln = word.isalnum()
print("\t'Python' isalnum() =",isaln)

#isspace
isspc = word.isspace()
print("\t'Python' isspace() =",isspc)
print("="*70)
