def solar_sys_generate():
    for i in ['merc', 'ven', 'earth']:
        yield i

planets = solar_sys_generate()

print(next(planets))
print(next(planets))
print(next(planets))