import random
class Attack:
    def attack(self, other):
        if self.health > 0:
            self.attack_power = random.randint(self.min_damage, self.max_damage) * self.count_creatures
            print(f"{self.name} атакует {other.name} и наносит {self.attack_power} урона!")
            other.take_damage(self.attack_power)
        else:
            print(f"{self.name} не может атаковать, так как он повержен.")
    

    def bow_attack(self, other):
        if self.health > 0:
            self.attack_power = random.randint(self.min_damage, self.max_damage) * self.count_creatures
            print(f"{self.name} атакует {other.name} и наносит {self.attack_power} урона!")
            other.take_damage(self.attack_power)
        else:
            print(f"{self.name} не может атаковать, так как он повержены.")
    

    def bite_attack(self, other):
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
        else:
            print(f"{self.name} не может атаковать, так как он повержен.")

        
    def ray_attack(self, other):
        if self.health > 0:
            self.attack_power = random.randint(self.min_damage, self.max_damage) * self.count_creatures * 5
            print(f"{self.name} атакует смертельным лучом {other.name} и наносит {self.attack_power} урона!")
            other.take_damage(self.attack_power)
        else:
            print(f"{self.name} не может атаковать, так как он повержен.")
        

    def mage_attack(self, other):
        if self.health > 0:
            self.attack_power = random.randint(self.min_damage, self.max_damage) * self.count_creatures
            print(f"{self.name} атакует {other.name} и наносит {self.attack_power} урона!")
            other.take_damage(self.attack_power)
        else:
            print(f"{self.name} не может атаковать, так как он повержен.")
        
    
    def meteorite_attack(self, other):
        if self.health > 0:
            self.attack_power = random.randint(self.min_damage, self.max_damage) * self.count_creatures * 5
            print(f"{self.name} атакует метеоритом {other.name} и наносит {self.attack_power} урона!")
            other.take_damage(self.attack_power)
        else:
            print(f"{self.name} не может атаковать, так как он повержен.")
    

    def retaliatory_attack(self, other):
        if self.health > 0:
            self.attack_power = random.randint(self.min_damage, self.max_damage) * self.count_creatures
            print(f"{self.name} атакует в ответ {other.name} и наносит {self.attack_power} урона!")
            other.take_damage(self.attack_power)
        else:
            print(f"{self.name} не может атаковать, так как он повержен.")


class Take_damage:
    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            print(f"{self.name} пал в бою!")
            self.count_creatures = 0
        else:
            print(f"{self.name} получил {damage} урона. Осталось здоровья: {self.health}")
            if self.health % self.max_hp != 0:
                self.count_creatures = self.health // self.max_hp + 1
            else:
                self.count_creatures = self.health // self.max_hp
    

    def ghoast_take_damage(self, damage):
        a = random.randint(1, 4)
        if a == 1:
            self.health -= damage
            if self.health <= 0:
                self.health = 0
                print(f"{self.name} пал в бою!")
                self.count_creatures = 0
            else:
                print(f"{self.name} получили {damage} урона. Осталось здоровья: {self.health}")
        else:
            print(f"{self.name} не получили {damage} урона. Осталось здоровья: {self.health}")


    def paladin_take_damage(self, damage):
        self.health -= damage * 0.7
        if self.health <= 0:
            self.health = 0
            print(f"{self.name} пал в бою!")
            self.count_creatures = 0
        else:
            print(f"{self.name} получил {damage} урона. Осталось здоровья: {self.health}")


def game_info():
    print('Игра похожая на Hero of might and magic есть два класса некроманты и люди в каждом классе есть пять видов юнитов и у каждого свои особенности для игры нужно создать армию: написать количество существ определенного класса.')
    print('От количества существ увеличивается их урон и здоровье.')
    print('Игра: для атаки противника используется функция attack также у некоторых персонажей есть два вида атак или свои способности.')
    pass

class Lich(Attack, Take_damage):
    max_damage = 200
    min_damage = 100
    def __init__(self, count_creatures):
        self.count_creatures = count_creatures
        self.name = 'Лич'
        self.health = 100 * count_creatures
        self.max_hp = 100


    def retaliatory_attack(self, other):
        super().retaliatory_attack(other = other)


    def mage_attack(self, other):
        super().mage_attack(other = other)
        other.retaliatory_attack(lich)

    
    def ray_attack(self, other):
        super().ray_attack(other = other)
        other.retaliatory_attack(lich)
    

    def take_damage(self, damage):
        super().take_damage(damage = damage)
    

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
        print('Лич может атаковать с помощбю функций mage_attack и ray_attack первая атака это обычная магическая атака, а вторая в 5 раз сильнее чем первая')
        print('Лич может кроме атаки призыватьсвоих преспешникав в виде зомби или скелетов в размере от 1 до 5')
        print(f'У лича {self.health} здоровья, {self.max_damage * self.count_creatures} максимальный урон,{self.min_damage * self.count_creatures} минимальный урон')
    pass


class Skelet(Attack, Take_damage):
    max_damage = 150
    min_damage = 100
    def __init__(self, count_creatures):
        self.count_creatures = count_creatures
        self.name = 'Скелет'
        self.health = 50 * count_creatures

    def sword_attack(self, other):
        super().attack(other = other)
        other.retaliatory_attack(skelet)
    

    def bow_attack(self, other):
        super().bow_attack(other = other)


    def retaliatory_attack(self, other):
        super().retaliatory_attack(other = other)
    

    def take_damage(self, damage):
        super().take_damage(damage = damage)


    def spawn_new(self, count):
        self.count_creatures += count


    def is_alive(self):
        return self.health > 0
    

    def info(self):
        print('Скелет имеет две атаки мечом (sword_atack) и луком (bow_attack) после атаки луком ему не могут нанести ответный удар')
        print(f'У скелета {self.health * self.count_creatures} здоровья, {self.max_damage * self.count_creatures} максимальный урон,{self.min_damage * self.count_creatures} минимальный урон')
    pass


class Zombie(Attack, Take_damage):
    max_damage = 75
    min_damage = 50
    def __init__(self, count_creatures):
        self.count_creatures = count_creatures
        self.name = 'Зомби'
        self.health = 200 * count_creatures


    def retaliatory_attack(self, other):
        super().retaliatory_attack(other = other)


    def sword_attack(self, other):
        super().attack(other = other)
        other.retaliatory_attack(zombie)
    

    def take_damage(self, damage):
        super().take_damage(damage = damage)
        

    def spawn_new(self, count):
        self.count_creatures += count


    def is_alive(self):
        return self.health > 0
    

    def info(self):
        print('Зомби имеет большое количество здоровья но маленький урон, атакует с помощью функции sword_atack')
        print(f'У зомби {self.health * self.count_creatures} здоровья, {self.max_damage * self.count_creatures} максимальный урон,{self.min_damage * self.count_creatures} минимальный урон')
    pass


class Ghoast(Attack, Take_damage):
    max_damage = 150
    min_damage = 75
    def __init__(self, count_creatures):
        self.count_creatures = count_creatures
        self.name = 'Призрак'
        self.health = 75 * count_creatures


    def retaliatory_attack(self, other):
        super().retaliatory_attack(other = other)


    def attack(self, other):
        super().attack(other = other)
        other.retaliatory_attack(ghoast)
    

    def take_damage(self, damage):
        super().ghoast_take_damage(damage = damage)


    def is_alive(self):
        return self.health > 0


    def info(self):
        print('Призрак может атаковать с помощью функции atack, а также может уклонится от удара с шансом 75%')
        print(f'У призрака {self.health * self.count_creatures} здоровья, {self.max_damage * self.count_creatures} максимальный урон,{self.min_damage * self.count_creatures} минимальный урон')
    pass


class Vampire(Attack, Take_damage):
    max_damage = 150
    min_damage = 100
    def __init__(self, count_creatures):
        self.count_creatures = count_creatures
        self.name = 'Вампир'
        self.health = 150 * count_creatures
    

    def bite_attack(self, other):
        super().attack(other = other)
        other.bite_retaliatory_attack(vampire)
    

    def take_damage(self, damage):
        super().take_damage(damage = damage)


    def is_alive(self):
        return self.health > 0
    

    def info(self):
        print('Вампир может атковать укусом (bite_attack) после атаки востанавливает 15% здоровья от урона который он нанес')
        print(f'У вампира {self.health * self.count_creatures} здоровья, {self.max_damage * self.count_creatures} максимальный урон,{self.min_damage * self.count_creatures} минимальный урон')
    pass


class Villager(Attack, Take_damage):
    max_damage = 150
    min_damage = 100
    def __init__(self, count_creatures):
        self.count_creatures = count_creatures
        self.name = 'Крестьянин'
        self.health = 100 * count_creatures
        self.max_hp = 100


    def pitchfork_attack(self, other):
        super().attack(other = other)
        other.retaliatory_attack(villager)
    

    def take_damage(self, damage):
        super().take_damage(damage = damage)


    def is_alive(self):
        return self.health > 0
    

    def info(self):
        print('Крестьянин имеет среднее количество здоровья и средний урон атакует с помощью функции pitchfork_attack')
        print(f'У крестьянина {self.health * self.count_creatures} здоровья, {self.max_damage * self.count_creatures} максимальный урон,{self.min_damage * self.count_creatures} минимальный урон')
    pass


class Archer(Attack, Take_damage):
    max_damage = 200
    min_damage = 100
    def __init__(self, count_creatures):
        self.count_creatures = count_creatures
        self.name = 'Лучник'
        self.health = 75 * count_creatures


    def sword_attack(self, other):
        super().attack(other = other)
        other.retaliatory_attack(archer)
    

    def bow_attack(self, other):
        super().bow_attack(other = other)


    def retaliatory_attack(self, other):
        super().retaliatory_attack(other = other)
    

    def take_damage(self, damage):
        super().take_damage(damage = damage)


    def is_alive(self):
        return self.health > 0
    

    def info(self):
        print('Лучник имеет малое количество здоровья но высокий урон, после атаки луком (bow_attack) не может получить ответный удар, также может атаковать мечом(sword_atack)')
        print(f'У лучника {self.health * self.count_creatures} здоровья, {self.max_damage * self.count_creatures} максимальный урон,{self.min_damage * self.count_creatures} минимальный урон')
    pass


class Paladin(Attack, Take_damage):
    max_damage = 200
    min_damage = 100
    def __init__(self, count_creatures):
        self.count_creatures = count_creatures
        self.name = 'Паладин'
        self.health = 300 * count_creatures


    def sword_attack(self, other):
        super().attack(other = other)
        other.retaliatory_attack(paladin)
    

    def retaliatory_attack(self, other):
        super().retaliatory_attack(other = other)
    

    def take_damage(self, damage):
        super().paladin_take_damage(damage = damage)
    

    def is_alive(self):
        return self.health > 0
    

    def info(self):
        print('Паладин имеет большое количество здоровья и высокий урон, паладин имеет защиту и получает на 30% меньше урона, атакует с помощью функции sword_attack')
        print(f'У паладина {self.health * self.count_creatures} здоровья, {self.max_damage * self.count_creatures} максимальный урон,{self.min_damage * self.count_creatures} минимальный урон')
    pass


class Grifon(Attack, Take_damage):
    max_damage = 250
    min_damage = 150
    def __init__(self, count_creatures):
        self.count_creatures = count_creatures
        self.name = 'Грифон'
        self.health = 500 * count_creatures


    def attack(self, other):
        super().attack(other = other)
        other.retaliatory_attack(grifon)


    def retaliatory_attack(self, other):
        super().retaliatory_attack(other = other)
    

    def take_damage(self, damage):
        super().take_damage(damage = damage)


    def is_alive(self):
        return self.health > 0
    

    def info(self):
        print('Грифон имеет гиганское количество здоровья и высокий урон,может атаковать с помощью функции attack')
        print(f'У грифона {self.health * self.count_creatures} здоровья, {self.max_damage * self.count_creatures} максимальный урон,{self.min_damage * self.count_creatures} минимальный урон')
    pass


class Mage(Attack, Take_damage):
    max_damage = 150
    min_damage = 100
    def __init__(self, count_creatures):
        self.count_creatures = count_creatures
        self.name = 'Маг'
        self.health = 100 * count_creatures
        self.max_health = 100 * count_creatures


    def mage_attack(self, other):
        super().mage_attack(other = other)
        other.retaliatory_attack(mage)
    

    def meteorite_attack(self, other):
        super().meteorite_attack(other = other)
        other.retaliatory_attack(mage)

    def retaliatory_attack(self, other):
        super().retaliatory_attack(other = other)
    

    def take_damage(self, damage):
        super().take_damage(damage = damage)


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
        print('Маг имеет среднее количество здоровья и средний урон, маг может востановить 10% от его максимального здоровья, может атаковать с помощью магии (mage_attack) и метеоритом meteorite_attack')
        print(f'У мага {self.health * self.count_creatures} здоровья, {self.max_damage * self.count_creatures} максимальный урон,{self.min_damage * self.count_creatures} минимальный урон')   
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
lich.ray_attack(villager)
lich.spawn_minion()
battle_info()