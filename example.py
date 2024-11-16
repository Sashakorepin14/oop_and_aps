class StarSystem:
    def __init__(self, planets, name):
        self.planets = list(planets)
        self.name = name

    def __len__(self):
        return len(self.planets)

    def __add__(self, other):
        planets_1 = self.planets[:]
        planets_1.append(other)
        return StarSystem(planets_1, self.name)
    
    def __radd__(self, other):
        planets_1 = self.planets[:]
        planets_1.insert(0, other)
        return StarSystem(planets_1, self.name)
    
    def __iadd__(self, other):
        self.planets.append(other)
        return self
    
    def __bool__(self):
        return len(self.planets) > 0
    
    def __str__(self):
        return f'Название системы {self.name} и ее планеты {self.planets}'
    
    def __getitem__(self, key):
        return self.planets[key]
system = StarSystem(['planet1', 'planet2', 'planet3'], 
                    'StarSystem1')
print(len(system))
system = system + 'planet4'
print(system.planets)
system ='planet5' + system 
print(system.planets)
system += 'planet6'
print(system.planets)
print(bool(system))
print(system)
print(system[0])
print(system[0:2])