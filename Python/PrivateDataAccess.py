# Accessing and modifying object data.
# 1. The traditional way: make the data private and use getters and setters.

class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email # Python convention: an underscore shows a private attribute.
        self.password = password
    
    def get_email(self): # convention for getter methods: prefix the name the attribute with "get"
        return self._email
    
    def set_email(self, new_email):
        self._email = new_email
        
# Protected values should not be updated outside of the class
        
user1 = User("dantheman", email = "Dan@gmail.com", password = "123")
print(user1.get_email())

user1 = User("dantheman", email = "Dan@gmail.com", password = "123")
print(user1.get_email())