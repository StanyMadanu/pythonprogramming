#polymorphism with constructors & inheritance

class circle:
    def __init__(self):
        print("Drawing circle")

class rect(circle):
    def __init__(self):
        print("Drawing rectangle")

class square(rect):
    def __init__(self):
        print("Drawing square")
        super().__init__()
        circle.__init__(self)

#main program
s = square() #object creation

