class Vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def start(self):
        print(f"{self.brand} brand {self.model} model vehicle is started")
    def stop(self):
        print(f"{self.brand} brand {self.model} model vehicle is stopped")

class Car(Vehicle):
    def __init__(self,brand,model,color,types,year):
        super().__init__(brand,model)
        self.types=types
        self.color=color
        self.year=year

    def basic_details(self):
        print(
        f" brand :{self.brand}\n"
        f" model :{self.model}\n"
        f" types :{self.types}\n"
        f" color :{self.color}\n"
        f" year :{self.year}"
         )

car=Car("BMW","M5","car","Black","2020")
car.basic_details()
car.start()
car.stop()


#  brand :BMW
#  model :M5
#  types :Black
#  color :car
#  year :2020
# basic_details() is the method of child 

# start(),stop() is the method of parent
# BMW brand M5 model vehicle is started 
# BMW brand M5 model vehicle is stopped

"""Inheritance is a fundamental concept in object-oriented programming (OOP), including Python. 
It allows a class (known as a subclass or derived class) to inherit attributes and methods from another class 
(known as a superclass or base class). The subclass can extend or override the functionality
 of the superclass, enabling code reuse and promoting a hierarchical organization of classes."""
