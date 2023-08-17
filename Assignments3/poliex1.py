#Program to achieve object call using user defined function in polymorphism

class carfunc1:
    def func(self):
        print("\tStart Mode")

class carfunc2:
    def func(self):
        print("\tDriving Mode")

class carfunc3:
    def func(self):
        print("\tStop Mode")

class car(carfunc1,carfunc2,carfunc3):
    def __init__(self):
        self.cname = "BMW"
        self.ccolor = "Blue"
        print("Car Name:",self.cname)
        print("Car Color:",self.ccolor)
    def func(self):

        carfunc1.func(self) #function call
        carfunc2.func(self) #function call
        carfunc3.func(self) #function call

#main program
c = car() #object creation
c.func() #object call using user defined function