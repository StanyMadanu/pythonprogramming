
from ATMExceptions import DepositError,WithdrawError,InSuffFundError

bal = 1500.00 #global variable

#Defining deposit function
def deposit():
    global bal
    damount = float(input("Enter Deposit amount: ")) #ValueError
    if (damount<=0):
        raise DepositError
    else:
        bal = bal + damount
        print("Your Account Xxxxxxxxx123 is credited with INR:{}".format(damount))
        print("Available Balance in Account INR:{}".format(bal))

#Defining withdraw function
def withdraw():
    global bal
    wdraw = float(input("Enter Withdraw amount: ")) #ValueError
    if (wdraw<=0):
        raise WithdrawError
    elif ((wdraw+500)>bal):
        raise InSuffFundError
    else:
        bal = bal-wdraw
        print("Your Account Xxxxxxxxx123 Debited with INR:{}".format(wdraw))
        print("Available Balance in Account INR:{}".format(bal))

#Defining balance enquiry function
def balanq():
        print("Available Balance in Account INR:{}".format(bal))
