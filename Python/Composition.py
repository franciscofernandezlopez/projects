# Composition

# Composition involves createing complex objects by combining simpler objects or components.

# A "has" relationship

# Low level components

class Engine:
    def start(self):
        print("Engine starting.")
        
class Wheels:
    def rotate(self):
        print("Rotate wheels.")

class Chassis:
    def support(self):
        print("Chassis is supporting")
        
class Seats:
    def sit(self):
        print("Sitting on seats.")

class Car:
    def __init__(self):
        self._engine = Engine()
        self._wheels = Wheels()
        self._chassis = Chassis()
        self._seats = Seats()
        
    def start(self):
        
        # The car class delegates components to other lower level classes
        
        self._engine.start()
        self._wheels.rotate()
        self._chassis.support()
        self._seats.sit()
        
car = Car()
car.start()

# When to use composition and when to use composition?

# When to use composition:
# When you need more flexibility to use smaller, reusable components;
# Clear "has-a" relationship
# Avoid limitations of inheritance (tiught coupling and fragile class problem)

# When to use inheritance?
#Clear "is-a" relationship
# Promote code reuse by inheriting properties and behaviours

# Key points on Fragile Base Class Problem:
# Ripple Effect
# Limited Extensibility
# Brittle Software
# Mitigation Strategies