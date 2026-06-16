# syntax: lambda arguments : expression
x = lambda a : a + 5
print(x(5)) # 10

square = lambda x: x ** 2
print(square(5))  # 25

add = lambda a, b: a + b
print(add(3, 7))  # 10

is_even = lambda n: n % 2 == 0
print(is_even(8))  # True
