# Accessing and modifying object data.

class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
    
    def say_hi_to_user(self, user):
        print(f"Sending message to {user.username}: Hi {user.username} it's {self.username}")
        
user1 = User("dantheman", email = "dan@gmail.com", password = "123")
user2 = User("batman", email = "bat@gmail.com", password = "abc")

user1.say_hi_to_user(user2)

print(user1.email)

user1.email = "danny@gmail.com" # PROBLEM WITH THIS: we can send a not valid email address.

print(user1.email)

# Accessing and modifying object data.
# 1. The traditional way: make the data private and use getters and setters.

class User:
    def __init__(self, username, email, password):
        self.username = username
        self.__email = email # Python convention: an underscore shows a private attribute.
        ## NOTE: a double underscore makes the attribute striclty private
        self.password = password
        
    # def get_email():
    #     return self._email

    def clean_email(self):
        self.__email.lower()
        return
    
user1 = User("dantheman", email = "Dan@gmail.com", password = "123")

print(user1._email) # This DOESn't throw an error. The protected attribute is accesible outside of the class.
print(user1.__email) # This thorws an error

user1._email = 'string' # This is not something we are supposed to do. This is poor ethics, as a private attribute is being exposed.
print(user1.clean_email())