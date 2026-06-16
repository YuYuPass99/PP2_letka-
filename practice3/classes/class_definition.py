class Class: #creating class 
  x = 10
p1 = Class() # Create an object named p1, and print the value of x:
print(p1.x) # 10

class Greeter:
    def greet(self):
        return "Hello!"
g = Greeter()
print(g.greet())  # Hello!

class Message:
    def show(self):
        print("This is a simple class")
m = Message()
m.show()  # This is a simple class

class Number:
    value = 10  # атрибут класса
n = Number()
print(n.value)  # 10
