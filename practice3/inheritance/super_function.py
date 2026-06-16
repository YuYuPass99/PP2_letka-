# super().method(args) syntax

class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)  # calling the __init__ method of the parent class (Person)
        self.grade = grade

s = Student("Dana", 10)
print(s.name, s.grade)  # Dana 10

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self, brand, color):
        super().__init__(brand)  # initializing brand using the parent class's method

c = Car("Toyota", "Red")
print(c.brand, c.color)  # Toyota Red

class Parent:
    def greet(self):
        return "Hello from Parent"

class Child(Parent):
    def greet(self):
        return super().greet() + " and Hello from Child" # calling the greet method of the parent class and adding more

c = Child()
print(c.greet())  # Hello from Parent and Hello from Child
