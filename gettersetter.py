class HelloWorld:
    def __init__(self):
        self.__message = "Hello World"
    
    @property
    def message(self):
        print("getter 실행됨")
        return self.__message
    
    @message.setter
    def message(self, message):
        print("setter 실행됨")
        if len(message) > 10:
            raise ValueError("Message is too long")
        
        self.__message = message

h = HelloWorld()
h.message = "Helloe"
print(h.message)