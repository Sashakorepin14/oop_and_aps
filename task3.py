b = [23, 96, 53, 45, 9, 25, 80, 13, 79, 52]
print(list(map(lambda a: a**3 if a % 2 == 0 else a, b)))