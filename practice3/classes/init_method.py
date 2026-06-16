class Person:
    def __init__(self, name):
        self.name = name  #  to assign value for name
p1 = Person("Ali")
print(p1.name)  # Ali

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
s1 = Student("Dana", 10)
print(s1.name, s1.grade)  # Dana 10

class Square:
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2
sq = Square(5)
print(sq.area())  # 25

class Car:
    def __init__(self, brand, color="Red"): # already assigned value for color
        self.brand = brand
        self.color = color

c1 = Car("Toyota")
print(c1.brand, c1.color)  # Toyota Red
c2 = Car("BMW", "Blue")
print(c2.brand, c2.color)  # BMW Blue
