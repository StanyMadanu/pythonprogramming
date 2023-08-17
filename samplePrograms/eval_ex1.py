# a program to evaluate a power m / a power n

a=int(input("Enter Numerator value:"))
m=int(input("Enter power of Numerator value:"))

#Numerator Value
print("-------------------------------------------------------------")
rslt1=a**m
print("Numerator = {}".format(rslt1))
print("=============================================================")


b=int(input("Enter Denominator value:"))
n=int(input("Enter power of Denominator value:"))

print("-------------------------------------------------------------")
#Denominator Value
rslt2 = b**n
print("Denominator = {}".format(rslt2))
print("=============================================================")

result= (a**m)/ (b**n)

print("Fraction of {} power {} and {} power {} is ={}".format(a,m, b,n, result))
print("=============================================================")
