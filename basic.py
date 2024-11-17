#defining class
class person():
    name=""
    age=0
    nationality=""
    birthday=""
    favcolor=""
    def __init__(self):   #constructor
        print("oject created")
    def userinp(self):
        self.name=input("What is your name?")
        self.age=input("What is your age?")
        self.nationality=input("What is your nationality?")
        self.birthday=input("What is your birthday?")
        self.favcolor=input("What is your favcolor?")
    
    def show(self):
        print("Your name is",self.name)
        print("Your age is",self.age)
        print("Your nationality is",self.nationality)
        print("Your birthday is",self.birthday)
        print("Your favcolor is",self.favcolor)

#object creation
obj1= person()
obj1.userinp()
obj1.show()
obj2= person()
obj2.show()