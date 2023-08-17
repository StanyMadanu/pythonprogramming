#Write a program to perform single inheritance property with looping 
#and conditional statements inside

class parent():
    def p(self):
        self.n = int(input("Enter a number of row to print pattern: "))

class child(parent):
    def c(self):
        parent.p(self) #function call
        for i in range(self.n):
            for j in range(self.n-i-1):
                print(" ",end="")
            for j in range(i+1):
                print("*",end=" ")
            print()

        print("=========================")
        for i in range(1,self.n+1):
            for j in range(1,self.n+1):
                if(j<=self.n-i):
                    print(" ",end=" ")
                else:
                    print("*",end=" ")
            print()            


#main program
ch = child() #object creation
ch.c() #function call