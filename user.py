import time as t
class User :
    def __init__(self):
        self.__username=None 
        self.__password=None
        self.__attemps=0 

    def sign_up(self,username,password) :
        self.__username= username
        self.__password=password 
        return "Account Created Successfully"
 
    def login (self,username,password):
        
        if self.__attemps>=3:
            t.sleep(5)
            self.__attemps=0
            return "Wait 5 Seconde. "
        
        if self._username==username and self._password==password:
            return f"Welcome {self.__username} !"
        
        self.__attemps +=1
        return f"Wrong username or password."
user1 = User()