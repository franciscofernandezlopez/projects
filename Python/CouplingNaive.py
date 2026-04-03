# Coupling introduction and naive solution

# Referes to the degree of dependency of classes or modules in a system.
# If classes are tighly coupled, modifying the class can crash the program.

# Order class

class EmailSender:
    def send(self, message):
        print(f"Sending email: {message}")
        
class Order:
    def create(self):
        # Perform order creation logic
        email = EmailSender()
        email.send("Hi, your order was placed.")
        
        # Changes in EmailSender require changes in the Order class.
        
order = Order()
order.create()

# And email sender class

# To reduce coupling, we can make an abstraction of the methods.