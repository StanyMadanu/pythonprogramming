#program to hit programmer defined exceptions
#mulhitting.py ----------> file and module name

from muldef import NegativeNumError, ZeroError

def multable(n):
    if (n<0):
        raise NegativeNumError
    elif (n==0):
        raise ZeroError
    else:
        print("="*50)
        print("\tMul Table =",n)
        print("="*50)
        for i in range(1,11):
            print("\t{} x {} = {}".format(n,i,n*i))
        print("="*50)
        