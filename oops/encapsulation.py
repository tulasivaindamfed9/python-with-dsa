# ENCAPSULATION: wrapping cariables(data) and methods(functions) into a single unit(class) 
# and controlling the access to the data.
# we allow access only through methods "getters" and "seetters"

# This is done to prevent accidental modification of data and to hide the internal 
# implementation details of a class from the outside world. 
# It is denoted with "__" (double underscore) before the variable or method. These are called private variables or methods. We cannot access these private variables or methods from outside the class. We can only access them from inside the class.
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private

    def deposit(self, amount):
        self.__balance += amount
        
    def get_balance(self):
        return self.__balance
        
    def set_balance(self,balance):
        self.__balance=balance


        
# user1 object
user1=BankAccount(500)
user1.deposit(200)
print(user1.get_balance())
print(user1.set_balance(1000))  
print(user1.get_balance())

# user2 object  
user2=BankAccount(1000)
print(user2.get_balance())      
print(user2.set_balance(2000))
print(user2.get_balance())