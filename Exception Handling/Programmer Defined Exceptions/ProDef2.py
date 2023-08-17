#ProDef2.py -------- file and module name

from ProDef1 import ZeroError

def Division(a,b):
    if (b==0):
        raise ZeroError
    else:
        c = a / b
        return c