numbers = [1, 2, 3, 4]
result = list(map(lambda x: x**2, numbers))
print(result)  # [1, 4, 9, 16]

numbers = [5, 10, 15]
result = list(map(lambda x: x * 2, numbers))
print(result)  # [10, 20, 30]

numbers = [1, 2, 3, 4, 5]
result = list(map(lambda x: x % 2 == 0, numbers))
print(result)  # [False, True, False, True, False]

strings = ["1", "2", "3"]
numbers = list(map(lambda x: int(x), strings))
print(numbers)  # [1, 2, 3]
