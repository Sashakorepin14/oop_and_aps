class Ball:

    def __init__(self):
        self.name = 'oval'
        self._radius = 5
        self.__color = 'red'

    def update_name(self, name):
        self.name = name
        print('name update to: ', self.name)

    def _update_radius(self, radius):
        self._radius = radius
        print('radius update to: ', self._radius)
    
    def __update_color(self, color):
        self.__color = color
        print('color update to: ', self.__color)

    def default_color(self):
        print('default color')
        self.__update_color('red')

ball = Ball()

print(ball.name)
print(ball._radius)
print()
ball.update_name('gdhfh')
ball._update_radius(5)
ball._Ball__update_color('blue')
print(dir(ball))