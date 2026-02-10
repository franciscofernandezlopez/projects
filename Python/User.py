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

