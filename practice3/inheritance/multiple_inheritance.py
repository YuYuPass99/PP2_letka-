class Flyer:
    def fly(self):
        return "Flying"

class Swimmer:
    def swim(self):
        return "Swimming"

class Duck(Flyer, Swimmer): # Duck inherits from both Flyer and Swimmer 
    pass

d = Duck()
print(d.fly())   # Flying
print(d.swim())  # Swimming

class Flyer:
    def move(self):
        return "Flying"

class Swimmer:
    def move(self):
        return "Swimming"

class Duck(Flyer, Swimmer):
    def move(self):
        return super().move() + " and Quacking"

d = Duck()
print(d.move())  # Flying and Quacking

class Person:
    def __init__(self, name):
        self.name = name

class Worker:
    def __init__(self, job):
        self.job = job

class Employee(Person, Worker):
    def __init__(self, name, job):
        Person.__init__(self, name)
        Worker.__init__(self, job)

e = Employee("Ali", "Engineer")
print(e.name, e.job)  # Ali Engineer

class Writer:
    def write(self):
        return "Writing"

class Singer:
    def sing(self):
        return "Singing"

class Artist(Writer, Singer):
    pass

a = Artist()
print(a.write())  # Writing
print(a.sing())   # Singing
