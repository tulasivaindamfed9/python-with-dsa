# ABSTRACTION:showing only the required data and hiding the data which is not necessary 
# eg: if a user in atm room only want to withdraw the amount. He doesn't need any data like which server used, which database used etc. We only just show him the amount to withdraw or balance left in his account...
# denoted with "@abstractmethod"

from abc import ABC, abstractmethod

# abstract class-- here ATM is an abstract class because it contains abstract methods withdraw, check_balance and deposit. We cannot create an object of abstract class. We need to create a subclass that inherits from the abstract class and implements the abstract methods.    
# means functions or methods are declared but not implemented in the abstract class. We need to implement those methods in the subclass.
class ATM(ABC):
    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def check_balance(self):
        pass

    @abstractmethod
    def deposit(self, amount):
        pass


# subclass MyATM inherits from abstract class ATM and implements the abstract methods withdraw, check_balance and deposit. We can create an object of MyATM class and call the methods withdraw, check_balance and deposit.
class MyATM(ATM):
    def __init__(self,balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds")

    def check_balance(self):
        print(f"Current balance: {self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")    



#user interaction with MyATM class
user1 = MyATM(1000)
user1.check_balance()  # Current balance: 1000
user1.withdraw(200)   # Withdrew 200. New balance: 800
user1.deposit(500)    # Deposited 500. New balance: 1300
