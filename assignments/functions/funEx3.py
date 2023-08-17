#3)Use nonlocal variable within nested functions includes looping

def outerfun():
    a = 10 #nonlocal variable
    def innerfun():
        print("="*50)
        print("\tMultiplication Table:",a)
        print("="*50)
        for i in range(1,a+1):
            print("\t{} x {} = {}".format(a,i,a*i))
        else:
            print("="*50)
            
    innerfun() #function call


#main program
outerfun() #function call