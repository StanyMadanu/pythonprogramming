# program to find the total amount of simple interest
#formula: simple_interest = PTR / 100
#PTR: Principle amount, Time, Rate of interest

#Heading
print("Simple Interest Program")
print("=====================================")

#Assigning values by taking input from user
principle=float(input("Enter the Principle Amount:"))
time=int(input("Enter the Time Period in months:"))
roi=float(input("Enter the Rate of Interest:"))

#simple interest formula
si = (principle*time*roi) / 100
totalamount = principle + si
print("===========================================")
print("Principle = {} \nTime Period = {}\nRate of Interest = {}".format(principle,time,roi))
print("--------------------------------------------")
print("Simple Interest = {}\nTotal amount = {}".format(si,totalamount))
print("===========================================")