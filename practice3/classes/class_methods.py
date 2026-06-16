class Person:
    def __init__(self, name, age): # __init__
        self.name = name
        self.age = age
p = Person("Ali", 20)
print(p.name, p.age)  # Ali 20

class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
    def __str__(self): # __str__
        return f"{self.color} {self.brand}"

c1 = Car("Toyota", "Red")
print(c1)  # Red Toyota

class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
    def __str__(self):
        return f"{self.color} {self.brand}"
c1 = Car("Toyota", "Red")
c2 = Car("BMW", "Blue")
print(c1)  # Red Toyota
print(c2)  # Blue BMW

del c1     
del c2     
print(c1)  # This will cause an error
print(c2)  # This will cause an error

class Calculator:
    def double(self, x): # self
        return x * 2

c = Calculator()
print(c.double(7))  # 14
