#polymorphism with inheritance - by calling super() & classname approaches

class circle:
    def disp(self):
        print("Drawing circle")

class rect(circle):
    def disp(self):
        print("Drawing Rectangle")
        super().disp()

class square(rect):
    def disp(self):
        print("Drawing square")
        super().disp()
        

#main program
s=square() #object creation
s.disp() #function call
