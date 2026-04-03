# Coupling introduction and naive solution

# Referes to the degree of dependency of classes or modules in a system.
# If classes are tighly coupled, modifying the class can crash the program.
# Abstract classses decouples the implementations of dependent classes that allows different implementations and easy substitution between classes
# Improves maintenability

# Order class

from abc import ABC, abstractmethod

# What are abstract classes or methods.

# Abstract class is a blue print for another classes, they can't be intantietied on their own.
# Allows to enforce that certain methods are inherented in certain classes.
# Any subclass that methods are not implemented (pass)



class NotificationService(ABC):
    @abstractmethod
    def send_notification(self, message: str): ## No need to define a particular method, we use an abstract idea of what the method does so the class can be independently modified afterwards
        pass
    
class EmailService(NotificationService): # We pass the abstract class NotificationService
    def send_notification(self, message):
        print(f"Sending email: {message}")
       
class MobileService(NotificationService):
    def send_notification(self, message):
        print(f"Send text message {message}")
        
class Order:
    def __init__(self, notification_service: NotificationService):
        self.notification_service = notification_service
    
    def create(self):
        # Perform order creation logic
        self.notification_service.send_notification("Hi, your order was placed and will be ready in the next 2-5 days.")
        
        # Changes in EmailSender require changes in the Order class.
        
order = Order(EmailService())
order.create()

order2 = Order(MobileService())
order2.create()

# And email sender class

# To reduce coupling, we can make an abstraction of the methods.