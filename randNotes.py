import random


random_float = random.random()
print(random_float)
# 0.00000 - 0.999999...

# Create a random decimal number between 0 and 5

random_dec = random_float * 5
print(random_dec)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")