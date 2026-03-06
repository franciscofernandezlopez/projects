# Inheritance

# Inheritance is a fundamental concept of OOP. It involvs creating new classes (subclasses or derived classes) based on existing classes (super classes or base classes).

# Subclasses inherit properties or behaviors of superclasses and can overwrite features.

# A car is a sehicle, and a bike is a vecicle.

# Inheritance: "IS A ..." relationship

class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        
    def start(self):
        print("Vehicle is starting")
        
    def stop(self):
        print("Vehicle is stopping")
     
        
class Car(Vehicle):
    # Car should inherit the Vehicle methods and attributes
    
    def __init__(self, brand, model, year, number_of_doors, number_of_wheels):
        super().__init__(brand, model, year)
        self.number_of_doors = number_of_doors
        self.number_of_wheels = number_of_wheels
    
    
class Bike(Vehicle):
    # Car should inherit the Vehicle methods and attributes
    
    def __init__(self, brand, model, year, number_of_wheels):
        super().__init__(brand, model, year)
        self.number_of_wheels = number_of_wheels
        
car = Car("Ford", "Fiesta", 2009, 4, 4)

bike = Bike("Focus", "Pantera", 2009, 2)

print(car.__dict__)
print(bike.__dict__)