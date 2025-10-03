import random

numbers = [random.randint(1, 10) for _ in range(20)]
unique_numbers = set(numbers)
print(unique_numbers)
