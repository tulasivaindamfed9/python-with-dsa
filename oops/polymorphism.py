# POLYMORPHISM:(diff forms) 
# Polymorphism allows different classes to implement the same method differently.
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")
for animal in [Dog(), Animal()]:
    animal.speak()
# Dog barks
# Animal speaks