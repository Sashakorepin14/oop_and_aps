class Businessman:

    def __init__(self, name, age):
        def_name  = 'cj'
        def_age = 40

        self._money = 1000000
        self._business = ''
    
    def info(self):
        print(self.name, self.age, self._business, self._money)

    @staticmethod
    def def_info()