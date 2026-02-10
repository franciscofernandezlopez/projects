name = "Francisco"
age = 29

class Dog: 
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner
        
    def bark(self):
        print("Whoof whoof")

class Owner:
    def __init__(self, name, address, contact_number):
        self.name = name
        self.address = address
        self.phone_number = contact_number
    

owner1 = Owner("Danny", "122 Springfield Drive", "888-999")

dog1 = Dog("Bruce", "Scottish Terrier", owner1)
dog1.bark() 
print(dog1.name)
print(dog1.breed)
print(dog1.owner.name)

owner2 = Owner("Sally", "122 Springfield Drive", "888-999")

dog2 = Dog("Freya", "Greyhound", owner2)
dog2.bark() 
print(dog2.name)
print(dog2.breed)
print(dog2.owner.name)

class Person: 
    
    # Defines a class -> "template" to define specific objects
    
    def __init__(self, name, age):
        
        # __init__ python method. Automatically runs when we create a new Python objects.
        
        self.name = name
        self.age = age
        
        # For each instance of the person class, we initialize these values to be attributes of each person object.
    
    def greet(self):
        
        # This is a method that displays a greeting message.
        
        print(f"My name is {self.name} and I am {self.age} years old.")
        
person1 = Person("Alice", 30) # Instantiation (creation) of a person1 object. Each instance of the class has its own data.
person1.greet()

person2 = Person("Bob", 42) # Instantiation (creation) of a person2 object. Each instance of the class has its own data.
person2.greet()