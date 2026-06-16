
def square(x):
    return x ** 2
print(square(5))  # 25

def operations(a, b):
    return a+b, a-b, a*b
sum_, diff, prod = operations(5, 3)
print(sum_, diff, prod)  # 8 2 15

def is_even(n):
    return n % 2 == 0
print(is_even(4))  # True

def list_square(lst):
    return [x**2 for x in lst]
print(list_square([1,2,3]))  # [1, 4, 9]


