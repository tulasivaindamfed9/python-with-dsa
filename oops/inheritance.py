# INHERITANCE: example-- parents(Animal) assserts or genes will be given to children(Dog)
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

d = Dog()
d.speak()  # Dog barks