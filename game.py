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
            if self.arrows > 0:
                self.attack_power = random.randint(self.min_damage, self.max_damage) * self.count_creatures
                print(f"{self.name} стреляет в {other.name} и наносит {self.attack_power} урона!")
                other.take_damage(self.attack_power)
            else:
                print('Стрелы закончились')
        else:
            print(f"{self.name} не может атаковать, так как он повержены.")
    

    def bite_attack(self, other):
        if self.health > 0:
            self.attack_power = random.randint(self.min_damage, self.max_damage) * self.count_creatures
            other.take_damage(self.attack_power)
            print(f"{self.name} кусает {other.name} и наносит {self.attack_power} урона!")
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
            if self.mana > 25:
                self.attack_power = random.randint(self.min_damage, self.max_damage) * self.count_creatures * 5
                print(f"{self.name} атакует смертельным лучом {other.name} и наносит {self.attack_power} урона!")
                other.take_damage(self.attack_power)
                self.mana -= 25
            else:
                print('Недостаточно маны')
        else:
            print(f"{self.name} не может атаковать, так как он повержен.")
        

    def mage_attack(self, other):
        if self.health > 0:
            if self.mana > 5:
                self.attack_power = random.randint(self.min_damage, self.max_damage) * self.count_creatures
                print(f"{self.name} атакует магией {other.name} и наносит {self.attack_power} урона!")
                other.take_damage(self.attack_power)
                self.mana -= 5
            else:
                print('Недостаточно маны')
        else:
            print(f"{self.name} не может атаковать, так как он повержен.")
        
    
    def meteorite_attack(self, other):
        if self.health > 0:
            if self.mana > 25:
                self.attack_power = random.randint(self.min_damage, self.max_damage) * self.count_creatures * 5
                print(f"{self.name} атакует метеоритом {other.name} и наносит {self.attack_power} урона!")
                other.take_damage(self.attack_power)
                self.mana -= 25
            else:
                print('Недостаточно маны')
        else:
            print(f"{self.name} не может атаковать, так как он повержен.")
    

    def retaliatory_attack(self, other):
        if self.health > 0:
            self.attack_power = (random.randint(self.min_damage, self.max_damage) * self.count_creatures) * 0.75
            print(f"{self.name} атакует в ответ {other.name} и наносит {self.attack_power} урона!")
            other.take_damage(self.attack_power)
        else:
            print(" ")


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
    

    def take_damage_with_evasion(self, damage):
        a = random.randint(1, 4)
        if a == 1:
            self.health -= damage
            if self.health <= 0:
                self.health = 0
                print(f"{self.name} пал в бою!")
                self.count_creatures = 0
            else:
                print(f"{self.name} получили {damage} урона. Осталось здоровья: {self.health}")
                if self.health % self.max_hp != 0:
                    self.count_creatures = self.health // self.max_hp + 1
                else:
                    self.count_creatures = self.health // self.max_hp
        else:
            print(f"{self.name} не получили {damage} урона. Осталось здоровья: {self.health}")


    def take_damage(self, damage):
        self.health -= damage * 0.7
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
        self.max_hp = 100
        self.health = self.max_hp * self.count_creatures
        self.mana = 100


    def mage_attack(self, other):
        super().mage_attack(other = other)
        
    
    def ray_attack(self, other):
        super().ray_attack(other = other)
        

    def take_damage(self, damage):
        super().take_damage(damage = damage)
    

    def create(self, count):
        self.count_creatures += count
        self.health += self.max_hp * self.count_creatures


    def spawn_minion(self):
        if self.health > 0:
            a = random.randint(1, 2)
            spawn = random.randint(1, 5)
            if a == 1:
                zombie.spawn_new(spawn)
                print(f'появилось {spawn} зомби')
            else:
                skelet.spawn_new(spawn)
                print(f'появилось {spawn} скелетов')
        else:
            print(f"{self.name} не может использовать способность, так как он повержен.")
    

    def info(self):
        print('Лич может атаковать с помощбю функций mage_attack и ray_attack первая атака это обычная магическая атака, а вторая в 5 раз сильнее чем первая')
        print('Лич может кроме атаки призыватьсвоих преспешникав в виде зомби или скелетов в размере от 1 до 5')
        print(f'У лича сейчас {self.health} здоровья, {self.max_damage * self.count_creatures} максимальный урон,{self.min_damage * self.count_creatures} минимальный урон, {self.mana} маны')
    pass


class Skelet(Attack, Take_damage):
    max_damage = 150
    min_damage = 100
    def __init__(self, count_creatures):
        self.count_creatures = count_creatures
        self.name = 'Скелет'
        self.health = 50 * self.count_creatures
        self.max_hp = 50
        self.arrows = 5


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
        print(f'У скелета сейчас {self.health * self.count_creatures} здоровья, {self.max_damage * self.count_creatures} максимальный урон,{self.min_damage * self.count_creatures} минимальный урон, {self.arrows} стрел')
    pass


class Zombie(Attack, Take_damage):
    max_damage = 75
    min_damage = 50
    def __init__(self, count_creatures):
        self.count_creatures = count_creatures
        self.name = 'Зомби'
        self.health = 200 * self.count_creatures
        self.max_hp = 200


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
        print(f'У зомби сейчас {self.health * self.count_creatures} здоровья, {self.max_damage * self.count_creatures} максимальный урон,{self.min_damage * self.count_creatures} минимальный урон')
    pass


class Ghoast(Attack, Take_damage):
    max_damage = 150
    min_damage = 75
    def __init__(self, count_creatures):
        self.count_creatures = count_creatures
        self.name = 'Призрак'
        self.health = 75 * self.count_creatures
        self.max_hp = 75


    def retaliatory_attack(self, other):
        super().retaliatory_attack(other = other)


    def attack(self, other):
        super().attack(other = other)
        other.retaliatory_attack(ghoast)
    

    def take_damage(self, damage):
        super().take_damage_with_evasion(damage = damage)


    def is_alive(self):
        return self.health > 0


    def info(self):
        print('Призрак может атаковать с помощью функции atack, а также может уклонится от удара с шансом 75%')
        print(f'У призрака сейчас {self.health * self.count_creatures} здоровья, {self.max_damage * self.count_creatures} максимальный урон,{self.min_damage * self.count_creatures} минимальный урон')
    pass


class Vampire(Attack, Take_damage):
    max_damage = 150
    min_damage = 100
    def __init__(self, count_creatures):
        self.count_creatures = count_creatures
        self.name = 'Вампир'
        self.health = 150 * self.count_creatures
        self.max_hp = 150
    

    def bite_attack(self, other):
        super().attack(other = other)
        other.retaliatory_attack(vampire)
    

    def take_damage(self, damage):
        super().take_damage(damage = damage)

    
    def retaliatory_attack(self, other):
        super().retaliatory_attack(other = other)


    def is_alive(self):
        return self.health > 0
    

    def info(self):
        print('Вампир может атковать укусом (bite_attack) после атаки востанавливает 15% здоровья от урона который он нанес')
        print(f'У вампира сейчас {self.health * self.count_creatures} здоровья, {self.max_damage * self.count_creatures} максимальный урон,{self.min_damage * self.count_creatures} минимальный урон')
    pass


class Villager(Attack, Take_damage):
    max_damage = 150
    min_damage = 100
    def __init__(self, count_creatures):
        self.count_creatures = count_creatures
        self.name = 'Крестьянин'
        self.health = 100 * self.count_creatures
        self.max_hp = 100


    def pitchfork_attack(self, other):
        super().attack(other = other)
        other.retaliatory_attack(villager)
    

    def take_damage(self, damage):
        super().take_damage(damage = damage)
    

    def retaliatory_attack(self, other):
        super().retaliatory_attack(other = other)


    def create(self, count):
        self.count_creatures += count
        self.health += self.max_hp * self.count_creatures
    

    def info(self):
        print('Крестьянин имеет среднее количество здоровья и средний урон атакует с помощью функции pitchfork_attack')
        print(f'У крестьянина сейчас {self.health * self.count_creatures} здоровья, {self.max_damage * self.count_creatures} максимальный урон,{self.min_damage * self.count_creatures} минимальный урон')
    pass


class Archer(Attack, Take_damage):
    max_damage = 200
    min_damage = 100
    def __init__(self, count_creatures):
        self.count_creatures = count_creatures
        self.name = 'Лучник'
        self.health = 75 * self.count_creatures
        self.max_hp = 75
        self.arrows = 5


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
        print(f'У лучника сейчас {self.health * self.count_creatures} здоровья, {self.max_damage * self.count_creatures} максимальный урон,{self.min_damage * self.count_creatures} минимальный урон, {self.arrows} стрел')
    pass


class Paladin(Attack, Take_damage):
    max_damage = 200
    min_damage = 100
    def __init__(self, count_creatures):
        self.count_creatures = count_creatures
        self.name = 'Паладин'
        self.health = 300 * self.count_creatures
        self.max_hp = 300


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
        print(f'У паладина сейчас {self.health * self.count_creatures} здоровья, {self.max_damage * self.count_creatures} максимальный урон,{self.min_damage * self.count_creatures} минимальный урон')
    pass


class Grifon(Attack, Take_damage):
    max_damage = 250
    min_damage = 150
    def __init__(self, count_creatures):
        self.count_creatures = count_creatures
        self.name = 'Грифон'
        self.health = 500 * self.count_creatures
        self.max_hp = 500


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
        print(f'У грифона сейчас {self.health * self.count_creatures} здоровья, {self.max_damage * self.count_creatures} максимальный урон,{self.min_damage * self.count_creatures} минимальный урон')
    pass


class Mage(Attack, Take_damage):
    max_damage = 150
    min_damage = 100
    def __init__(self, count_creatures):
        self.count_creatures = count_creatures
        self.name = 'Маг'
        self.health = 100 * count_creatures
        self.max_health = 100 * self.count_creatures
        self.max_hp = 100
        self.mana = 100


    def mage_attack(self, other):
        super().mage_attack(other = other)
    

    def meteorite_attack(self, other):
        super().meteorite_attack(other = other)
    

    def take_damage(self, damage):
        super().take_damage(damage = damage)


    def is_alive(self):
        return self.health > 0


    def heal(self):
        if self.health > 0:
            if self.health < 100 * self.count_creatures:
                self.health += self.max_health * 0.1
                if self.health >= 100 * self.count_creatures:
                        self.health = self.max_health
            else:
                self.health = self.max_health
        else:
            print(f"{self.name} не может использовать способность, так как он повержен.")

    
    def info(self):
        print('Маг имеет среднее количество здоровья и средний урон, маг может востановить 10% от его максимального здоровья, может атаковать с помощью магии (mage_attack) и метеоритом meteorite_attack')
        print(f'У мага сейчас {self.health * self.count_creatures} здоровья, {self.max_damage * self.count_creatures} максимальный урон,{self.min_damage * self.count_creatures} минимальный урон, {self.mana} маны')   
    pass


villager = Villager(0)
archer = Archer(0)
paladin = Paladin(0)
grifon = Grifon(0)
mage = Mage(0)
lich = Lich(0)
skelet = Skelet(0)
zombie = Zombie(0)
ghoast = Ghoast(0)
vampire = Vampire(0)


class Player_people:

    def __init__(self, gold):
        self.golda = gold
    

    def count_of_gold(self):
        print(f'У вас сейчас {self.golda} золота')


    def create_villager(self, count):
        self.cost = 15
        print('Стоимость юнита одного 15 золота')
        if self.cost * count <= self.golda:
            villager.create(count)
            print(f'Вы купили {count} юнитов')
        else:
            print('Недостаточно золота')


    def create_archer(self, count):
        self.cost = 50
        print('Стоимость юнита одного 50 золота')
        if self.cost * count <= self.golda:
            archer.create(count)
            print(f'Вы купили {count} юнитов')
        else:
            print('Недостаточно золота')


    def create_paladin(self, count):
        self.cost = 80
        print('Стоимость юнита одного 80 золота')
        if self.cost * count <= self.golda:
            paladin.create(count)
            print(f'Вы купили {count} юнитов')
        else:
            print('Недостаточно золота')


    def create_grifon(self, count):
        self.cost = 260
        print('Стоимость юнита одного 260 золота')
        if self.cost * count <= self.golda:
            grifon.create(count)
            print(f'Вы купили {count} юнитов')
        else:
            print('Недостаточно золота')


    def create_mage(self, count):
        self.cost = 600
        print('Стоимость юнита одного 600 золота')
        if self.cost * count <= self.golda:
            mage.create(count)
            print(f'Вы купили {count} юнитов')
        else:
            print('Недостаточно золота')
    

    def army_info(self):
        print('Армия людей')
        print(f'{villager.count_creatures} крестьянинов')
        print(f'{archer.count_creatures} лучников')
        print(f'{paladin.count_creatures} паладинов')
        print(f'{grifon.count_creatures} грифонов')
        print(f'{mage.count_creatures} магов')


class Player_necromancers:

    def __init__(self, gold):
        self.golda = gold
        

    def count_of_gold(self):
        print(f'У вас сейчас {self.golda} золота')


    def create_lich(self, count):
        self.cost = 600
        print('Стоимость юнита одного 600 золота')
        if self.cost * count <= self.golda:
            lich.create(count)
            print(f'Вы купили {count} юнитов')
        else:
            print('Недостаточно золота')


    def create_skelet(self, count):
        self.cost = 30
        print('Стоимость юнита одного 30 золота')
        if self.cost * count <= self.golda:
            skelet.create(count)
            print(f'Вы купили {count} юнитов')
        else:
            print('Недостаточно золота')


    def create_zombie(self, count):
        self.cost = 15
        print('Стоимость юнита одного 15 золота')
        if self.cost * count <= self.golda:
            zombie.create(count)
            print(f'Вы купили {count} юнитов')
        else:
            print('Недостаточно золота')
        

    def create_ghoast(self, count):
        self.cost = 100
        print('Стоимость юнита одного 100 золота')
        if self.cost * count <= self.golda:
            ghoast.create(count)
            print(f'Вы купили {count} юнитов')
        else:
            print('Недостаточно золота')
        

    def create_vampire(self, count):
        self.cost = 250
        print('Стоимость юнита одного 250 золота')
        if self.cost * count <= self.golda:
            vampire.create(count)
            print(f'Вы купили {count} юнитов')
        else:
            print('Недостаточно золота')
    

    def army_info(self):
        print('Армия некромантов')
        print(f'{lich.count_creatures} личей')
        print(f'{skelet.count_creatures} скелетов')
        print(f'{zombie.count_creatures} зомби')
        print(f'{ghoast.count_creatures} призраков')
        print(f'{vampire.count_creatures} вампиров')
        


if __name__ == '__main__':
    p1 = Player_people(10000000000)
    p1.create_villager(10)
    p2 = Player_necromancers(10000000000)
    p2.create_lich(5)
    p1.army_info()
    p2.army_info()
    lich.ray_attack(villager)
    # lich.info()
    # lich.spawn_minion()
    # battle_info()