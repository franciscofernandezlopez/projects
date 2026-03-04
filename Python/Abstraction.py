# Abstraction

# Reduces complexity by hiding unnecessary details

# IN this example, the only method that a user wants to use is the send_email, while the 'complex' methods are hidden as protected attributes.

# Difference with Encapsulation: bundles data carefully labelling protected attributes.
# Abstraction: provides a simple implementation hidding how to do it.

class EmailService:
    
    def _connect(self):
        print("Connecting to email server.")
    
    def _authenticate(self):
        print("Authenticating.")
        
    def _disconnect(self):
        print("Disconnect.")
        
    def send_email(self):
        self._connect()
        self._authenticate()
        print("Sending email...")
        self._disconnect()
    
email = EmailService()

email.send_email()