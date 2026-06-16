# class Child(Parent): # syntax
#    pass

class Animal:
    def speak(self):
        return "Sound"
class Dog(Animal): # Dog inherited method speak() from Animal
    pass
d = Dog()
print(d.speak())  # Sound 

class Animal:
    def speak(self):
        return "Sound"

class Cat(Animal):
    def speak(self):
        return "Meow" # Changed inherited method speak() in Cat

c = Cat()
print(c.speak())  # Meow

class Vehicle:
    def start(self):
        return "Vehicle started"

class Car(Vehicle):
    def stop(self): # Added new method in Car
        return "Car stopped"

c = Car()
print(c.start())  # Vehicle started
print(c.stop())   # Car stopped
