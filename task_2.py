import math
def factorial(n):
    try:
        if n < 0:
            raise ValueError
        return math.factorial(n)
    except ValueError:
        return 'Нужно неотрицательное целое число'

print(factorial(5))
print(factorial(-5))