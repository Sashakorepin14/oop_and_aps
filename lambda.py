def sum_arg(a, b):
    return a + b

print(sum_arg(12, 25))

sum_arg = lambda a, b: a + b

print(sum_arg(7, 13))


a = [lambda a: a**2 for a in range(10)]

list1 = [0, 1, 2]
list2 = [1, 3, 4]
a = list(map(lambda a, b: a+b, list1, list2))
print(a)

maximum = (lambda a, b: a if a > b else b)
print(maximum(23, 25))



lambda_list = [lambda x: x + 1,
               lambda x: x * 2,
               lambda x: x ** 3]
for i in lambda_list:
    print(i(2))

print(lambda_list[0](4))