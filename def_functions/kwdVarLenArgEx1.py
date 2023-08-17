# varible length arguments

def dispvalues(id,sname,*a, city="Hyd"):
    print("-"*50)
    print("Student ID:{}, Name:{}, City:{}".format(id,sname,city))
    print("-"*50)
    s=0
    
    for val in a:
        print("\t{}".format(val))
        s = s+val
    else:
        print("Sum={}".format(s))


#main program
dispvalues(200,"RS",10)
dispvalues(300,"TS",10,20)
dispvalues(400,"BS",10,20,30,city="Bang")
dispvalues(500,"SS",10, 20, 30, 40) #function-call