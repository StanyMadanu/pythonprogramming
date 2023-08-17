""" 
import keyword

print(keyword.kwlist)


username = "Stany"
userid = 20
decimal_num = 3.5


print(username, type(username), id(username))
print(userid, type(userid), id(userid))
print(decimal_num, type(decimal_num), id(decimal_num)) """

#True, False, and, or, not keywords
""" 
print(0 and 1 or 0) #---------------0
print("Hello" and 1 or "False") #---1 """

#===============================================

#assert, async, await keywords
#a = 5
#assert a > 10

""" import asyncio
async def sample():
    print("Sample Function Logged in")
    await asyncio.sleep(10)
    print("Sample Function Logged-out!")

asyncio.run(sample()) """

#conditional statements: if, elif, else
""" print("-"*30)
print("\tif else")
print("-"*30)
a = 7
if a>5:
    print("{} is greater than 5".format(a))
elif a>0:
    print("{} is greater than 0".format(a))
elif a>=7:
    print("{} is greater than or equal to 7".format(a))
else:
    print("Invalid number!") """
#---------------------------------------------------------------------------
#looping statements: for, while
""" print("-"*30)
print("\tfor loop")
print("-"*30)
for i in range(0,10):
    if i == 5:
       # break # breaking the loop when the value is equal to 5
        continue   # skipping the value 5
    print(i) """
#----------------------------------------------------------------------------
""" print("-"*30)
print("\tWhile loop")
print("-"*30)

b = 5
while (b):
    print(b)
    b = b - 1 """
    
#-----------------------------------------------------------------------------

""" lambda b: b*20

with open('sample.txt', 'w') as file1:
    file1.write("File Handling") """

#-------------------------------------------------

#Arithematic Operators
print("-"*50)
print("\tAddition")
print("-"*50)
print("\tFundamental Category Data Types")
print(10 + 20) #int
print(20.10 + 40.20) # float
print((2+4j)+(3+2j)) # complex
print(True + False) #bool
print("\n\tSequence Category Data Types")
print("water" + "bottle") # str
#print(range(2)+range(3)) # range----TypeError: unsupported operand type(s) for +: 'range' and 'range'
print("\n\tList Category Data Types")
print([10, 20, 30] + [1, 2, 3]) #list
print((10, 20, 30) + (11, 12, 13)) #tuple
#print({100, 200, 300} + {110, 220, 330}) #set---TypeError: unsupported operand type(s) for +: 'set' and 'set'
#print({10:"Ten", 20:"Twenty"} + {30:"Thirty", 40:"Fourty"}) #dict/dictionary-------TypeError: unsupported operand type(s) for +: 'dict' and 'dict'

#------------------------------------------------------------------------------------------------------------------------------------

print("\n","-"*50)
print("\tSubtraction")
print("-"*50)
print("\tFundamental Category Data Types")
print(10 - 20) #int
print(20.10 - 40.20) # float
print((2+4j) - (3+2j)) # complex
print(True - False) #bool
print("\n\tSequence Category Data Types")
#print("water" - "bottle") # str------TypeError: unsupported operand type(s) for -: 'str' and 'str'
#print(range(2) - range(3)) # range----TypeError: unsupported operand type(s) for -: 'range' and 'range'
print("\n\tList Category Data Types")
#print([10, 20, 30] - [1, 2, 3]) #list----TypeError: unsupported operand type(s) for -: 'list' and 'list'
#print((10, 20, 30) - (11, 12, 13)) #tuple---TypeError: unsupported operand type(s) for -: 'tuple' and 'tuple'
print({100, 200, 300} - {110, 220, 330}) #set---This expression only considers first occurance set data
#print({10:"Ten", 20:"Twenty"} - {30:"Thirty", 40:"Fourty"}) #dict----TypeError: unsupported operand type(s) for -: 'dict' and 'dict'

#-------------------------------------------------------------------------------------------------------------------------------------

print("\n","-"*50)
print("\tMultiplication")
print("-"*50)
print("\tFundamental Category Data Types")
print(10 * 20) #int
print(20.10 * 40.20) # float
print((2+4j) * (3+2j)) # complex
print(True * False) #bool
print("\n\tSequence Category Data Types")
#print("water" * "bottle") # str----TypeError: can't multiply sequence by non-int of type 'str'
#print(range(2) * range(3)) # range----TypeError: unsupported operand type(s) for *: 'range' and 'range'
print("\n\tList Category Data Types")
#print([10, 20, 30] * [1, 2, 3]) #list--TypeError: can't multiply sequence by non-int of type 'list'
#print((10, 20, 30) * (11, 12, 13)) #tuple---TypeError: can't multiply sequence by non-int of type 'tuple'
#print({100, 200, 300} * {110, 220, 330}) #set---TypeError: unsupported operand type(s) for *: 'set' and 'set'
#print({10:"Ten", 20:"Twenty"} * {30:"Thirty", 40:"Fourty"}) #dict/dictionary-------TypeError: unsupported operand type(s) for *: 'dict' and 'dict'

#--------------------------------------------------------------------------------------------------------------------------------------

print("-"*50)
print("\tDivision")
print("-"*50)

print("\tFundamental Category Data Types")
print(10 / 20) #int
print(20.10 / 40.20) # float
print((2+4j) / (3+2j)) # complex
#print(True / False) #bool-----ZeroDivisionError: division by zero
print("\n\tSequence Category Data Types")
#print("water" / "bottle") # str----TypeError: unsupported operand type(s) for /: 'str' and 'str'
#print(range(2) / range(3)) # range----TypeError: unsupported operand type(s) for +: 'range' and 'range'
print("\n\tList Category Data Types")
#print([10, 20, 30] / [1, 2, 3]) #list----TypeError
#print((10, 20, 30) / (11, 12, 13)) #tuple---TypeError
#print({100, 200, 300} / {110, 220, 330}) #set---TypeError: unsupported operand type(s) for +: 'set' and 'set'
#print({10:"Ten", 20:"Twenty"} /   {30:"Thirty", 40:"Fourty"}) #dict/dictionary-------TypeError: unsupported operand type(s) for +: 'dict' and 'dict'

#--------------------------------------------------------------------------------------------------------------------------------------

print("-"*50)
print("\tFloor division")
print("-"*50)

print("\tFundamental Category Data Types")
print(10 // 20) #int
print(20.10 // 40.20) # float
#print((2+4j) // (3+2j)) # complex----------TypeError
#print(True // False) #bool------ZeroDivisionError
print("\n\tSequence Category Data Types")
#print("water" // "bottle") # str----TypeError
#print(range(2) // range(3)) # range----TypeError: unsupported operand type(s) for +: 'range' and 'range'
print("\n\tList Category Data Types")
#print([10, 20, 30] // [1, 2, 3]) #list--------TypeError
#print((10, 20, 30) // (11, 12, 13)) #tuple--------TypeError
#print({100, 200, 300} // {110, 220, 330}) #set---TypeError: unsupported operand type(s) for +: 'set' and 'set'
#print({10:"Ten", 20:"Twenty"} //   {30:"Thirty", 40:"Fourty"}) #dict/dictionary-------TypeError: unsupported operand type(s) for +: 'dict' and 'dict'




#--------------------------------------------------------------------------------------------------------------------------------------

print("-"*50)
print("\tModulous")
print("-"*50)

print("\tFundamental Category Data Types")
print(10 % 20) #int
print(20.10 % 40.20) # float
#print((2+4j) % (3+2j)) # complex-----TypeError
#print(True % False) #bool---------ZeroDivisionError:
print("\n\tSequence Category Data Types")
#print("water" % "bottle") # str-----TypeError
#print(range(2) % range(3)) # range----TypeError: unsupported operand type(s) for +: 'range' and 'range'
print("\n\tList Category Data Types")
#print([10, 20, 30] % [1, 2, 3]) #list------TypeError
#print((10, 20, 30) % (11, 12, 13)) #tuple------TypeError
#print({100, 200, 300} % {110, 220, 330}) #set---TypeError: unsupported operand type(s) for +: 'set' and 'set'
#print({10:"Ten", 20:"Twenty"} %   {30:"Thirty", 40:"Fourty"}) #dict/dictionary-------TypeError: unsupported operand type(s) for +: 'dict' and 'dict'


#--------------------------------------------------------------------------------------------------------------------------------------

print("-"*50)
print("\tPower/Exponent")
print("-"*50)

print("\tFundamental Category Data Types")
print(10 ** 20) #int
print(20.10 ** 40.20) # float
print((2+4j) ** (3+2j)) # complex
print(True ** False) #bool
print("\n\tSequence Category Data Types")
#print("water"** "bottle") # str-------TypeError
#print(range(2) ** range(3)) # range----TypeError: unsupported operand type(s) for +: 'range' and 'range'
print("\n\tList Category Data Types")
#print([10, 20, 30] ** [1, 2, 3]) #list----TypeError
#print((10, 20, 30) ** (11, 12, 13)) #tuple----TypeError
#print({100, 200, 300} ** {110, 220, 330}) #set---TypeError: unsupported operand type(s) for +: 'set' and 'set'
#print({10:"Ten", 20:"Twenty"} **   {30:"Thirty", 40:"Fourty"}) #dict/dictionary-------TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
