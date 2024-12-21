import numpy as np
def square_root(x):
    try:
        if x < 0:
            raise ValueError
        return np.sqrt(x)
    except ValueError:
        return 'Нельзя извлекать корень из отрицательного числа'


print(square_root(4))
print(square_root(-4))