num = int(input())
if num >= 1 and num <= 100:
    def guess_number(num):
        n = 100
        min = 0
        max = n
        if n != num:
            print(f'Ваше число больше {(max - min)//2}')
            if input() == 'да' or input() == 'Да':
                min = n // 2
                max = n
            else:
                min = 0
                max = n // 2
            return 1
        else:
            print(f'ваше число {n}')
            
        return guess_number()
#
guess_number(num)