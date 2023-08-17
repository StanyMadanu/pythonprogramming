#1. Achieve abstraction with protected data member

class person():
    def bankinfo(self):
        self.name = "Jarvis"
        self.age = 27
        self._bankname = "HDFC" #protected data
        self._pin = 6767 #protected data
        self._amount = 20000 #protected data
    
class info(person):
    def getinfo(self):
        person.bankinfo(self) #function call
        print(self.name)
        print(self._bankname)
        print(self._pin)
        print(self._amount)


#main program
inf = info() #object creation
inf.getinfo() #function call