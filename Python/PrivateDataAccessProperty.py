# Accessing and modifying object data.
# 1. The traditional way: make the data private and use getters and setters.

from datetime import datetime

class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email # Python convention: an underscore shows a private attribute.
        self.password = password
    
    @property # The property decorator permits turns this method into a getter property, which we can access it using class.method
    def email(self):
        print('Email accessed.')
        return self._email
    
    @email.setter
    def email(self, new_email):
        if "@" in new_email:
            self._email = new_email
    
    # def get_email(self): # convention for getter methods: prefix the name the attribute with "get"
    #     print(f"Email accesed at {datetime.now()}.")
    #     return self._email
    
    def set_email(self, new_email):
        if "@" in new_email:
            self._email = new_email
        
# Protected values should not be updated outside of the class
        
user1 = User("dantheman", email = "Dan@gmail.com", password = "123")
print(user1.email)

# Why use properties?

# It gives us full control with what happens when an attribute is modified or accessed
# It is less verbose than a get or set methods

user1.set_email("123") # Does not change email since it is not "valid"