class Calculator:
    def __init__(self):
        self.__password = "" #private 
        self.__isSecretUnlocked = False #private

    def is_secret_unlocked(self):
        return self.__isSecretUnlocked
    
    def set_password(self, password):
        self.__password = password

    def get_password(self):
        return self.__password
        
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            print("Cannot divide by zero")
        return a / b
    
    def power(self, a, b):
        return a ** b
    
    def unlock_secret(self,password):
        if password == self.__password:
            print("Access granted! Secret Operation unlocked.")
            self.__isSecretUnlocked = True
            return True
        else:
            return False
