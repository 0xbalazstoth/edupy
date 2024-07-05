# Páros és páratlan számok összege, random listából
import random

numbers = random.sample(range(1, 100), 10)
print(numbers)

odd_nums = []
even_nums = []

for number in numbers:
    if number % 2 == 0:
        even_nums.append(number)
    else:
        odd_nums.append(number)
