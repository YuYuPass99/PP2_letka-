names = ["Zangar", "Yama", "Aki"]
scores = [85, 92, 78]

# enumerate(): Index and value
for index, name in enumerate(names):
    print(f"{index}: {name}") # Output: 0: Zangar, 1: Yama, 2: Aki

# zip(): Pair two lists
for name, score in zip(names, scores):
    print(f"{name} scored {score}") # Output: Zangar scored 85, Yama scored 92, Aki scored 78