#program to separte the postive and negative values from given list

posNums = lambda x: x>0
negNums = lambda x: x<0


#main program
lst = [10, -20, 30, -40, 50, -60]

print("poslist: ", list(filter(posNums,lst)))
print("Neglist: ",list(filter(negNums,lst)))