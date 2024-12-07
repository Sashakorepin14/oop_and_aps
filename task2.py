import sys
num = int(input(f'Введите ваше число '))
l = [0, 100]
a = sum(l) // 2

def guess_number(a):
    if a != num:
        ans = input(f'Ваше число больше {a}? \n')
        if  ans == 'нет' or ans == 'Нет' or ans == 'No' or ans == 'no':
            l[1] = a
            return guess_number(sum(l) // 2)
        else:
            l[0] = a
            return guess_number(sum(l) // 2)
    return f'Ваше число {a}'

if num >= 1 and num <= 100:
    print(guess_number(a))
else:
    print('Досвидания')
    sys.exit(1)