import random 
def game_info():
    print('Игра похожая на Hero of might and magic есть два класса некроманты и люди в каждом классе есть пять видов юнитов и у каждого свои особенности для игры нужно создать армию: написать количество существ определенного класса.')
    print('От количества существ увеличивается их урон и здоровье.')
    print('Игра: для атаки противника используется функция attack также у некоторых персонажей есть два вида атак или свои способности.')
    pass

class Lich:
    max_damage = 200
    min_damage = 100
    def __init__(self, count_creatures):
        self.count_creatures = count_creatures
        self.name = 'Лич'
        self.health = 100 * count_creatures


    def attack(self, other):
        if self.health > 0:
            self.attack_power = random.randint(self.min_damage, self.max_damage) * self.count_creatures
            other.take_damage(self.attack_power)
            print(f"{self.name} атакует {other.name} и наносит {self.attack_power} урона!")
            other.attack(lich)
        else:
            print(f"{self.name} не может атаковать, так как он повержен.")


    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            print(f"{self.name} пал в бою!")
        else:
            print(f"{self.name} получил {damage} урона. Осталось здоровья: {self.health}")


    def is_alive(self):
        return self.health > 0


    def spawn_minion(self):
        a = random.randint(1, 2)
        spawn = random.randint(1, 5)
        if a == 1:
            zombie.spawn_new(spawn)
            print(f'появилось {spawn} зомби')
        else:
            skelet.spawn_new(spawn)
            print(f'появилось {spawn} скелетов')
    

    def info(self):
        print('Лич может кроме атаки призыватьсвоих преспешникав в виде зомби или скелетов в размере от 1 до 5')
        print(f'У лича {self.health} здоровья, {self.max_damage} максимальный урон,{self.min_damage} минимальный урон')
    pass


class Skelet:
    max_damage = 150
    min_damage = 100
    def __init__(self, count_creatures):
        self.count_creatures = count_creatures
        self.name = 'Скелет'
        self.health = 50 * count_creatures


    def attack(self, other):
        if self.health > 0:
            self.attack_power = random.randint(self.min_damage, self.max_damage) * self.count_creatures
            other.take_damage(self.attack_power)
            print(f"{self.name} атакует {other.name} и наносит {self.attack_power} урона!")
            other.attack(skelet)
        else:
            print(f"{self.name} не может атаковать, так как он повержен.")
        
    
    def bow_attack(self, other):
        if self.health > 0:
            self.attack_power = random.randint(self.min_damage, self.max_damage) * self.count_creatures
            other.take_damage(self.attack_power)
            print(f"{self.name} атакует {other.name} и наносит {self.attack_power} урона!")
        else:
            print(f"{self.name} не может атаковать, так как он повержены.")


    def take_damage(self, damage):
            self.health -= damage
            if self.health <= 0:
                self.health = 0
                print(f"{self.name} пал в бою!")
            else:
                print(f"{self.name} получил {damage} урона. Осталось здоровья: {self.health}")


    def spawn_new(self, count):
        self.count_creatures += count


    def is_alive(self):
        return self.health > 0
    

    def info(self):
        print('Скелет имеет две атаки мечом и луком после атаки луком ему не могут нанести ответный удар')
        print(f'У скелета {self.health} здоровья, {self.max_damage} максимальный урон,{self.min_damage} минимальный урон')
    pass


class Zombie:
    max_damage = 75
    min_damage = 50
    def __init__(self, count_creatures):
        self.count_creatures = count_creatures
        self.name = 'Зомби'
        self.health = 200 * count_creatures


    def attack(self, other):
        if self.health > 0:
            self.attack_power = random.randint(self.min_damage, self.max_damage) * self.count_creatures
            other.take_damage(self.attack_power)
            print(f"{self.name} атакует {other.name} и наносит {self.attack_power} урона!")
            other.attack(zombie)
        else:
            print(f"{self.name} не может атаковать, так как он повержен.")


    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            print(f"{self.name} пал в бою!")
        else:
            print(f"{self.name} получил {damage} урона. Осталось здоровья: {self.health}")
        

    def spawn_new(self, count):
        self.count_creatures += count


    def is_alive(self):
        return self.health > 0
    

    def info(self):
        print('Зомби имеет большое количество здоровья но маленький урон')
        print(f'У зомби {self.health} здоровья, {self.max_damage} максимальный урон,{self.min_damage} минимальный урон')
    pass


class Ghoast:
    max_damage = 150
    min_damage = 75
    def __init__(self, count_creatures):
        self.count_creatures = count_creatures
        self.name = 'Призрак'
        self.health = 75 * count_creatures


    def attack(self, other):
        if self.health > 0:
            self.attack_power = random.randint(self.min_damage, self.max_damage) * self.count_creatures
            other.take_damage(self.attack_power)
            print(f"{self.name} атакует {other.name} и наносит {self.attack_power} урона!")
        else:
            print(f"{self.name} не может атаковать, так как он повержен.")


    def take_damage(self, damage):
        a = random.randint(1, 4)
        if a == 1:
            self.health -= damage
            if self.health <= 0:
                self.health = 0
                print(f"{self.name} пал в бою!")
            else:
                print(f"{self.name} получили {damage} урона. Осталось здоровья: {self.health}")
        else:
            print(f"{self.name} не получили {damage} урона. Осталось здоровья: {self.health}")


    def is_alive(self):
        return self.health > 0


    def info(self):
        print('Призрак после атаки ему не могут нанести ответный удар, также может уклонится от удара с шансом 75%')
        print(f'У призрака {self.health} здоровья, {self.max_damage} максимальный урон,{self.min_damage} минимальный урон')
    pass


class Vampire:
    max_damage = 150
    min_damage = 100
    def __init__(self, count_creatures):
        self.count_creatures = count_creatures
        self.name = 'Вампир'
        self.health = 150 * count_creatures


    def attack(self, other):
        if self.health > 0:
            self.attack_power = random.randint(self.min_damage, self.max_damage) * self.count_creatures
            other.take_damage(self.attack_power)
            print(f"{self.name} атакует {other.name} и наносит {self.attack_power} урона!")
            if self.health < 150 * self.count_creatures:
                self.health += self.attack_power * 0.15
                if self.health >= 150 * self.count_creatures:
                    self.health = 150 * self.count_creatures
            else:
                self.health = 150 * self.count_creatures
            other.attack(vampire)
        else:
            print(f"{self.name} не может атаковать, так как он повержен.")


    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            print(f"{self.name} пал в бою!")
        else:
            print(f"{self.name} получил {damage} урона. Осталось здоровья: {self.health}")


    def is_alive(self):
        return self.health > 0
    

    def info(self):
        print('Вампир после атаки востанавливает 15% здоровья от урона который он нанес')
        print(f'У вампира {self.health} здоровья, {self.max_damage} максимальный урон,{self.min_damage} минимальный урон')
    pass


class Villager:
    max_damage = 150
    min_damage = 100
    def __init__(self, count_creatures):
        self.count_creatures = count_creatures
        self.name = 'Крестьянин'
        self.health = 100 * count_creatures


    def attack(self, other):
        if self.health > 0:
            self.attack_power = random.randint(self.min_damage, self.max_damage) * self.count_creatures
            other.take_damage(self.attack_power)
            print(f"{self.name} атакует {other.name} и наносит {self.attack_power} урона!")
            other.attack(villager)
        else:
            print(f"{self.name} не может атаковать, так как он повержен.")


    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            print(f"{self.name} пал в бою!")
        else:
            print(f"{self.name} получил {damage} урона. Осталось здоровья: {self.health}")


    def is_alive(self):
        return self.health > 0
    

    def info(self):
        print('Крестьянин имеет среднее количество здоровья и средний урон')
        print(f'У крестьянина {self.health} здоровья, {self.max_damage} максимальный урон,{self.min_damage} минимальный урон')
    pass


class Archer:
    max_damage = 200
    min_damage = 100
    def __init__(self, count_creatures):
        self.count_creatures = count_creatures
        self.name = 'Лучник'
        self.health = 75 * count_creatures


    def attack(self, other):
        if self.health > 0:
            self.attack_power = random.randint(self.min_damage, self.max_damage) * self.count_creatures
            other.take_damage(self.attack_power)
            print(f"{self.name} атакует {other.name} и наносит {self.attack_power} урона!")
        else:
            print(f"{self.name} не может атаковать, так как он повержен.")


    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            print(f"{self.name} пал в бою!")
        else:
            print(f"{self.name} получил {damage} урона. Осталось здоровья: {self.health}")


    def is_alive(self):
        return self.health > 0
    

    def info(self):
        print('Лучник имеет малое количество здоровья но высокий урон, после атки не может получить ответный удар')
        print(f'У лучника {self.health} здоровья, {self.max_damage} максимальный урон,{self.min_damage} минимальный урон')
    pass


class Paladin:
    max_damage = 200
    min_damage = 100
    def __init__(self, count_creatures):
        self.count_creatures = count_creatures
        self.name = 'Паладин'
        self.health = 300 * count_creatures


    def attack(self, other):
        if self.health > 0:
            self.attack_power = random.randint(self.min_damage, self.max_damage) * self.count_creatures
            other.take_damage(self.attack_power)
            print(f"{self.name} атакует {other.name} и наносит {self.attack_power} урона!")
            other.attack(paladin)
        else:
            print(f"{self.name} не может атаковать, так как он повержен.")


    def take_damage(self, damage):
        self.health -= damage * 0.7
        if self.health <= 0:
            self.health = 0
            print(f"{self.name} пал в бою!")
        else:
            print(f"{self.name} получил {damage} урона. Осталось здоровья: {self.health}")


    def is_alive(self):
        return self.health > 0
    

    def info(self):
        print('Паладин имеет большое количество здоровья и высокий урон, паладин имеет защиту и получает на 30% меньше урона')
        print(f'У паладина {self.health} здоровья, {self.max_damage} максимальный урон,{self.min_damage} минимальный урон')
    pass


class Grifon:
    max_damage = 250
    min_damage = 150
    def __init__(self, count_creatures):
        self.count_creatures = count_creatures
        self.name = 'Грифон'
        self.health = 500 * count_creatures


    def attack(self, other):
        if self.health > 0:
            self.attack_power = random.randint(self.min_damage, self.max_damage) * self.count_creatures
            other.take_damage(self.attack_power)
            print(f"{self.name} атакует {other.name} и наносит {self.attack_power} урона!")
            other.attack(grifon)
        else:
            print(f"{self.name} не может атаковать, так как он повержен.")


    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            print(f"{self.name} пал в бою!")
        else:
            print(f"{self.name} получил {damage} урона. Осталось здоровья: {self.health}")


    def is_alive(self):
        return self.health > 0
    

    def info(self):
        print('Грифон имеет гиганское количество здоровья и высокий урон')
        print(f'У грифона {self.health} здоровья, {self.max_damage} максимальный урон,{self.min_damage} минимальный урон')
    pass


class Mage:
    max_damage = 150
    min_damage = 100
    def __init__(self, count_creatures):
        self.count_creatures = count_creatures
        self.name = 'Маг'
        self.health = 100 * count_creatures
        self.max_health = 100 * count_creatures


    def attack(self, other):
        if self.health > 0:
            self.attack_power = random.randint(self.min_damage, self.max_damage) * self.count_creatures
            other.take_damage(self.attack_power)
            print(f"{self.name} атакует {other.name} и наносит {self.attack_power} урона!")
            other.attack(mage)
        else:
            print(f"{self.name} не может атаковать, так как он повержен.")


    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            print(f"{self.name} пал в бою!")
        else:
            print(f"{self.name} получил {damage} урона. Осталось здоровья: {self.health}")


    def is_alive(self):
        return self.health > 0


    def heal(self):
        if self.health < 100 * self.count_creatures:
            self.health += self.max_health * 0.1
            if self.health >= 100 * self.count_creatures:
                    self.health = self.max_health
        else:
            self.health = self.max_health

    
    def info(self):
        print('Маг имеет среднее количество здоровья и средний урон, маг может востановить 10% от его максимального здоровья')
        print(f'У мага {self.health} здоровья, {self.max_damage} максимальный урон,{self.min_damage} минимальный урон')   
    pass


def battle_info():
    print('Армия противника')
    print(f'{villager.count_creatures} крестьянинов')
    print(f'{archer.count_creatures} лучников')
    print(f'{paladin.count_creatures} паладинов')
    print(f'{grifon.count_creatures} грифонов')
    print(f'{mage.count_creatures} магов')
    print('Ваша армия')
    print(f'{lich.count_creatures} личей')
    print(f'{skelet.count_creatures} скелетов')
    print(f'{zombie.count_creatures} зомби')
    print(f'{ghoast.count_creatures} призраков')
    print(f'{vampire.count_creatures} вампиров')
    pass   


# создание армии противника
villager = Villager(random.randint(5, 20))
archer = Archer(random.randint(5, 20))
paladin = Paladin(random.randint(5, 20))
grifon = Grifon(random.randint(5, 20))
mage = Mage(random.randint(5, 20))


# создание вашей армии
lich = Lich(1)
skelet = Skelet(10)
zombie = Zombie(15)
ghoast = Ghoast(5)
vampire = Vampire(3)


battle_info()
lich.attack(villager)
lich.spawn_minion()
battle_info()