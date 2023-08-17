from ATMMenu import menu
from ATMExceptions import ZeroError, NegativeNumError,DepositError,WithdrawError,InSuffFundError
from ATMOperations import deposit,withdraw,balanq


while(True):
    menu() #function call
    try:
        ch = int(input("Enter your choice of operation: "))
        if (ch==0):
            raise ZeroError
        elif (ch<0):
            raise NegativeNumError
        else:
            match(ch):
                case 1:
                    try:
                        deposit()
                    except ValueError:
                        print("Don't try to deposit spaces, alphanumerics, strs and special symbols..!...Try again..!!")
                    except DepositError:
                        print("Don't try to deposit Negative and Zero values")
                case 2:
                    try:
                        withdraw()
                    except ValueError:
                        print("Don't try to withdraw spaces, alphanumerics, strs and special symbols..!...Try again..!!")
                    except WithdrawError:
                        print("Don't try to enter withdraw amount as Negative and Zero values")
                    except InSuffFundError:
                        print("Your Mininum amount should contain INR: 500")
                case 3:
                    balanq()
                case 4:
                    print("Thankyou for using our Application..!")
                    break
                case _:
                    print("Your choice of operation is invalid.. please try again")
    except ValueError:
        print("Don't Enter spaces, alphanumerics, strs and special symbols..!...Try again..!!")
    except ZeroError:
        print("Don't enter Zero for choice selection...Try again..!!")
    except NegativeNumError:
        print("Don't enter negative number for choic selection...Try again..!!")
