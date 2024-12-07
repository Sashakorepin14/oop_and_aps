import sys
num = int(input())
l = [0, 100]
a = sum(l) // 2

def func(a):
    if a != num:
        print(f'Ваше число больше {a}')
        ans = input()
        if  ans == 'нет' or ans == 'Нет':
            l[1] = a
            return func(sum(l) // 2)
        else:
            l[0] = a
            return func(sum(l) // 2)
    return a

if num >= 1 and num <= 100:
    print(func(a))
else:
    print('Досвидания')
    sys.exit(1)