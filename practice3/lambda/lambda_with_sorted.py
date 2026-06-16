numbers = [5, 2, 9, 1]
result = sorted(numbers, key=lambda x: x) # ascending order
print(result)  # [1, 2, 5, 9]

numbers = [5, 2, 9, 1]
result = sorted(numbers, key=lambda x: x, reverse=True) # descending order
print(result)  # [9, 5, 2, 1]

words = ["apple", "cat", "banana", "dog"]
result = sorted(words, key=lambda x: len(x)) # by length in ascneding
print(result)  # ['cat', 'dog', 'apple', 'banana']

words = ["applE", "bananA", "cherrY"]
result = sorted(words, key=lambda x: x[-1]) # by last letter in ascending
print(result) # ['bananA', 'applE', 'cherrY']

