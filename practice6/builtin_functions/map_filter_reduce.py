from functools import reduce

nums = [1, 2, 3, 4, 5, 6]

# map(): Square each number
squared = list(map(lambda x: x**2, nums)) # Output: [1, 4, 9, 16, 25, 36]

# filter(): Keep only even numbers
evens = list(filter(lambda x: x % 2 == 0, nums)) # Output: [2, 4, 6]

# reduce(): Sum all numbers
total = reduce(lambda x, y: x + y, nums) # Output: 21

print(f"Squared: {squared}, Evens: {evens}, Total: {total}") # Output: Squared: [1, 4, 9, 16, 25, 36], Evens: [2, 4, 6], Total: 21