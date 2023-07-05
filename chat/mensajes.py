class Message():
    def __init__(self, user, msg="", size=190):
        self.user = user
        self.message = msg
        self.buffer_size = size
    
    def set_message(self, message):
        if len(message) > self.buffer_size:
            self.message = message[:190]
        else: self.message = message
    
    




    