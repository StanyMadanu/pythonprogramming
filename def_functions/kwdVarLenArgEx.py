#Keyword variable length arugments

def dispvalue(city="hyd",**val ):
    for k,v in val.items():
        print("\t{}--->{}".format(k,v))
    else:
        print("-"*50)


#main program
dispvalue(id=1000, sname="TS",)
dispvalue(enum=200, ename="SG")