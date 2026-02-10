# Accessing and modifying object data.
# 1. The traditional way: make the data private and use getters and setters.

class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email # Python convention: an underscore shows a private attribute.
        self.password = password
        
    # def get_email():
    #     return self._email

    def clean_email(self):
        self._email.lower()
        return
    
user1 = User("dantheman", email = "dan@gmail.com", password = "123")

print(user1._email) # This DOESn't throw an error. The protected attribute is accesible outside of the class.