# Static Attributes
# Shared around all instances of a class. Belongs to the class ifself, not to any specific instance of the class.

# When to use them?

# Data that is common to all instances of a class. For example, counts and totals. Useful for data that must be consistent across all instances.

class User:
    user_count = 0
    
    def __init__(self, username, email):
        self.username = username
        self.email = email
        User.user_count += 1
        
    def display_user(self):
        print(f'Username: {self.username}, Email: {self.email}')
        
user1 = User("dantheman", email = "dan@gmail.com")
user2 = User("batman", email = "bat@gmail.com")

print(User.user_count)
print(user1.user_count)
print(user2.user_count)