class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):  # Overriding the speak method of the parent class (Animal)
        return "Woof!"

d = Dog()
print(d.speak())  # Woof!

class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)  # Using parent __init__
        self.grade = grade

s = Student("Dana", 10)
print(s.name, s.grade)  # Dana 10

class Vehicle:
    def start(self):
        return "Vehicle started"

class Car(Vehicle):
    def start(self):
        return super().start() + " and Car engine running" # Overriding start method and calling the parent method using super()

c = Car()
print(c.start())  # Vehicle started and Car engine running
