#program to demonstrate data encapsulation
class Account:
    def __init__(self):
        self.__acno=10 #hidden
        self.cname="Rossum"
        self.__bal=5.7 #hidden
        self.__pin=1234 #hidden
        self.bname="HDFC"