with open('example.txt') as f:
    # print(f.readline(), end='')
    # print(f.readline(), end='')
    # print(f.readline())

    print(next(f), end='')
    print(next(f))
    # print(next(f), end='')

with open('example2.txt') as f2:
    for i in f2:
        print(i, end='')
print('')