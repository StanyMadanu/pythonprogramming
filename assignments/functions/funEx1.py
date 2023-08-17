#1 - Program with argument and with return statement in functions

def example(a,b): #defining function with arg/parameters and return statement
    sum = a + b
    sub = a - b
    div = a / b
    mul = a * b
    return sum, sub, div, mul

#main program
result = example(10,20) #function call stored in object

print("="*50)
print("Returning values in tuple:",result) #values stored in tuple
print("="*50)

print("\tSum of 10+20 = {}".format(result[0]))
print("\tSub of 10-20 = {}".format(result[1]))
print("\tDiv of 10/20 = {}".format(result[2]))
print("\tMul of 10x20 = {}".format(result[3]))

print("="*50)

