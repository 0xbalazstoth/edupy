# Callback függvény
# A callback függvény egy olyan függvény, amelyet egy másik függvénynek adunk át paraméterként.
def calculate(a, b, operation):
    return operation(a, b)


def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


sum_result = calculate(5, 3, add)
multiply_result = calculate(5, 3, multiply)
print(sum_result, multiply_result)
