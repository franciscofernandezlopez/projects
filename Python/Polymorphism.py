# Polymorphism

# Using superclasses to factor the code can reduce if statements on list of objects
# Using polymorphism, we can now treat all objects similarly since they all having the same attributes and methods for all istances
# Easy extension and maintenance to the system

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
    
    def start(self):
        print("Car is starting")
        
    def stop(self):
        print("Car is stopping")
    
class Bike(Vehicle):
    # Bike should inherit the Vehicle methods and attributes
    
    def __init__(self, brand, model, year, number_of_wheels):
        super().__init__(brand, model, year)
        self.number_of_wheels = number_of_wheels
        
    def start(self):
        print("Bike is starting")
        
    def stop(self):
        print("Bike is stopping")
        
class Plane(Vehicle):
    # Bike should inherit the Vehicle methods and attributes
    
    def __init__(self, brand, model, year, number_of_doors):
        super().__init__(brand, model, year)
        self.number_of_doors = number_of_doors
        
    def start(self):
        print("Plane is starting")
        
    def stop(self):
        print("Plane is stopping")
        
        
# Create instances of objects
car = Car("Ford", "Fiesta", 2009, 4, 4)
bike = Bike("Focus", "Pantera", 2009, 2)

print(car.__dict__)
print(bike.__dict__)

# Create list of objects to inspect
vehicles = [
    Car("Ford", "Fiesta", 2008, 4, 4),
    Bike("Focus", "Pantera", 2009, 2)
]

## Not using polymorphism

for vehicle in vehicles:
    if isinstance(vehicle, Car):
        print(f"Inspect {vehicle.brand} {vehicle.model} ({type (vehicle).__name__})")
    elif isinstance(vehicle, Bike):
        print(f"Inspect {vehicle.brand} {vehicle.model} ({type (vehicle).__name__})")
        vehicle.start()
    else:
        raise Exception("Object is not a valid vehicle")
    

## Using the vehicle polymorphism

for vehicle in vehicles:
    if isinstance(vehicle, Vehicle):
        print(f"Inspect {vehicle.brand} {vehicle.model} ({type (vehicle).__name__})")
        vehicle.start()
        vehicle.stop()
    else:
        raise Exception("Object is not a valid vehicle")
    
    
# Create list of objects to inspect
vehicles: list[Vehicle] = [
    Car("Ford", "Fiesta", 2008, 4, 4),
    Bike("Focus", "Pantera", 2009, 2),
    Plane("Airbus", "Plane", 2009, 8)
]

for vehicle in vehicles:
    print(f"Inspect {vehicle.brand} {vehicle.model} ({type (vehicle).__name__})")
    vehicle.start()
    vehicle.stop()