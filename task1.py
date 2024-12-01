def func_gen(break_key):
    p = 0
    while True:
        if p != 1 and (p == 2 or p % 2 != 0) and (p == 3 or p % 3 != 0) and (p == 5 or p % 5 != 0) and (p == 7 or p % 7 != 0):
            yield p**2

            if p == break_key:
                break
        
        p += 1


n = 100
gen = func_gen(n)
for i in range(n):
    print(next(gen))