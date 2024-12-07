num = int(input())
l = [0, 100]
a = sum(l) // 2
if num >= 1 and num <= 100:
    def func(a):
        if a != num:
            if num < a:
                l[1] = a
                func(sum(l) // 2)
            else:
                l[0] = a
                func(sum(l) // 2)
        return a

    print(func(a))