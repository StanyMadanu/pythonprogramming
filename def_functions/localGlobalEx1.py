#Local and Global Variables
a = 10 #global var

def fun1():
    global a
    a = a + 20 #local var

def fun2():
    global a
    a = a*10 #local var
    

#main program
print("Value of a={}".format(a))
fun1() #function call
print("Value of a={} after fun1".format(a))
fun2() #function call
print("value of a={} after fun2 call".format(a))