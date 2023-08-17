#Program to accept list of numeric values and separate even, odd numbers

print("Enter the numeric values sepated by space")
lst = [int(var) for var in input().split()]

print("Given Values: ",lst)
print("="*50)
evenlst = [n for n in lst if n%2==0]
oddlst = [n for n in lst if n%2!=0]

print("Even numbers list: ",evenlst)
print("Odd numbers list: ",oddlst)
print("="*50)
