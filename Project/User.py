
from abc import ABCMeta,abstractmethod
class Users(metaclass=ABCMeta):
    def __init__(self,userName,password):
        self.userName=userName
        self.password=password

    @abstractmethod
    def logIn(self,userName,password):
        pass
    
    def signUp(self):
        pass

    def LogOut (self):
        pass

        
        