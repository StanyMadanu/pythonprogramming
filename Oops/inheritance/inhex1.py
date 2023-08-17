#program for demonstrating single inheritance

class parent:
    def dis1(self):
        print("Parent ---> disp1()")


class child(parent): #single inheritance
    def dis2(self):
        print("Child ---> dis2()")
        self.dis1() #calling parent call dis1() from child class dis2()



#main program
o2 = child()  #object creation
o2.dis2()



