#simple program to demonstrate method overridden

class student():
    def status(self):
        print("Person is a student when he is in school")

class driver(student): 
    def status(self):
        super().status()
        print("Person is a driver when he is driving")

class customer(driver):
    def status(self):
        super().status()
        print("Person is a customer when he is in shop")

class person(customer):
    def status(self):
        self.name = "Tony"
        print("Person name:",self.name)
        super().status()

#main program
p1 = person() #object creation
p1.status() #function call