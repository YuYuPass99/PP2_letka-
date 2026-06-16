class Car:
    wheels = 4  # class variable, shared for everything

c1 = Car()
c2 = Car()

print(c1.wheels)  # 4
print(c2.wheels)  # 4

class Car:
    wheels = 4

Car.wheels = 6  # editing the class variable

c1 = Car()
print(c1.wheels)  # 6

class Light:
    status = "Off"  # class variable

    def turn_on(self):
        Light.status = "On"

l1 = Light()
l2 = Light()

l1.turn_on()
print(l1.status)  # On
print(l2.status)  # On

class Circle:
    pi = 3.14  # class variable

    def __init__(self, radius):
        self.radius = radius  # instance variable

c1 = Circle(5)
c2 = Circle(7)

print(c1.pi, c1.radius)  # 3.14 5
print(c2.pi, c2.radius)  # 3.14 7
