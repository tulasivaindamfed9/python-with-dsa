# oops object oriented programming in python
# CLASS VS OBJECTS----
# Class is a blue print ..eg:a tower blue print
# Object is constructed or created based on blue print ..eg:so many towers are constructed based on the class tower blue print

# CONSTRUCTURE:
# __init__ is the constructor method in Python.
# It initializes object attributes when an object is created.

class Tower:
    def __init__(self,towerName,yearOfConstruction):
        self.name=towerName
        self.year=yearOfConstruction
        
    def towerDetails(self):
        print(f"{self.name} is constructed in year {self.year}")
        
# object creation from class Tower
t1=Tower("eifel",1890)
t1.towerDetails()
print(t1.name)