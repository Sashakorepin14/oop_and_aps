import random

class Day_cycle:
    def __init__(self):
        self.curent_day = 1
    

    def check_curent_day(self):
        print(self.curent_day)


    def day_cycle(self):
        self.curent_day += 1


class Gold_mine(Day_cycle):
    def __init__(self):
        self.level = 0
        self.curent_day = 1
        self.curent_gold_amount = 0
        self.production_in_day = 0

    def create_gold_mine(self):
        self.cost = 300
        if self.gold >= self.cost:
            self.gold -= self.cost
            self.level = 1
            self.production_in_day = 20
            print(f'Вы создали золотоносную шахту ее характеристики: {self.level} уровень, доходность {self.production_in_day} золота')
        else:
            print('Недостаточно золота для покупки')
    

    def level_up_gold_mine(self):
        if self.level == 1:
            self.cost = 200
            if self.gold >= self.cost:
                self.gold -= self.cost
                self.level = 2
                self.production_in_day = 40
                print(f'Вы улучшили золотоносную шахту до второго уровня теперь ее доходность состовляет {self.production_in_day}')
        elif self.level == 2:
            self.cost = 400
            if self.gold >= self.cost:
                self.gold -= self.cost
                self.level = 3
                self.production_in_day = 60
                print(f'Вы улучшили золотоносную шахту до третьего уровня теперь ее доходность состовляет {self.production_in_day}')

    
    def collect_products_with_gold_mine(self):
        if self.curent_gold_amount > 0:
            self.gold += self.curent_gold_amount
            print(f'Вы забрали {self.curent_gold_amount} золота')
        else:  
            print('Шахта с золтом пуста')
    

    def day_cycle(self):
        super().day_cycle()
        self.curent_gold_amount += self.production_in_day * self.curent_day


class Town(Gold_mine):
    def __init__(self):
        pass

    
    def day_cycle(self):
        super().day_cycle()


class Attack:
    def attack(self, other):
        if self.health > 0:
            if self.curent_motion < self.curent_day:
                self.attack_power = random.randint(self.min_damage, self.max_damage) * self.count_creatures
                print(f"{self.name} атакует {other.name} и наносит {self.attack_power} урона!")
                other.take_damage(self.attack_power)
                self.curent_motion += 1
            else:
                print('Юнит устал и больше не может ходить')
        else:
            print(f"{self.name} не может атаковать, так как он повержен.")
    

    def bow_attack(self, other):
        if self.health > 0:
            if self.arrows > 0:
                if self.curent_motion < self.curent_day:
                    self.attack_power = random.randint(self.min_damage, self.max_damage) * self.count_creatures
                    print(f"{self.name} стреляет в {other.name} и наносит {self.attack_power} урона!")
                    other.take_damage(self.attack_power)
                    self.curent_motion += 1
                else:
                    print('Юнит устал и больше не может ходить')
            else:
                print('Стрелы закончились')
        else:
            print(f"{self.name} не может атаковать, так как он повержены.")
    

    def bite_attack(self, other):
        if self.health > 0:
            if self.curent_motion < self.curent_day:
                self.attack_power = random.randint(self.min_damage, self.max_damage) * self.count_creatures
                other.take_damage(self.attack_power)
                print(f"{self.name} кусает {other.name} и наносит {self.attack_power} урона!")
                self.curent_motion += 1
                if self.health < 150 * self.count_creatures:
                    self.health += self.attack_power * 0.15
                    if self.health >= 150 * self.count_creatures:
                        self.health = 150 * self.count_creatures
                else:
                    self.health = 150 * self.count_creatures
            else:
                print('Юнит устал и больше не может ходить')
        else:
            print(f"{self.name} не может атаковать, так как он повержен.")

        
    def ray_attack(self, other):
        if self.health > 0:
            if self.mana > 25:
                if self.curent_motion < self.curent_day:
                    self.attack_power = random.randint(self.min_damage, self.max_damage) * self.count_creatures * 5
                    print(f"{self.name} атакует смертельным лучом {other.name} и наносит {self.attack_power} урона!")
                    other.take_damage(self.attack_power)
                    self.curent_motion += 1
                    self.mana -= 25
                else:
                    print('Юнит устал и больше не может ходить')
            else:
                print('Недостаточно маны')
        else:
            print(f"{self.name} не может атаковать, так как он повержен.")
        

    def mage_attack(self, other):
        if self.health > 0:
            if self.mana > 5:
                if self.curent_motion < self.curent_day:
                    self.attack_power = random.randint(self.min_damage, self.max_damage) * self.count_creatures
                    print(f"{self.name} атакует магией {other.name} и наносит {self.attack_power} урона!")
                    other.take_damage(self.attack_power)
                    self.curent_motion += 1
                    self.mana -= 5
                else:
                    print('Юнит устал и больше не может ходить')
            else:
                print('Недостаточно маны')
        else:
            print(f"{self.name} не может атаковать, так как он повержен.")
        
    
    def meteorite_attack(self, other):
        if self.health > 0:
            if self.mana > 25:
                if self.curent_motion < self.curent_day:
                    self.attack_power = random.randint(self.min_damage, self.max_damage) * self.count_creatures * 5
                    print(f"{self.name} атакует метеоритом {other.name} и наносит {self.attack_power} урона!")
                    other.take_damage(self.attack_power)
                    self.curent_motion += 1
                    self.mana -= 25
                else:
                    print('Юнит устал и больше не может ходить')
            else:
                print('Недостаточно маны')
        else:
            print(f"{self.name} не может атаковать, так как он повержен.")
    

    def retaliatory_attack(self, other):
        if self.health > 0:
            self.attack_power = int((random.randint(self.min_damage, self.max_damage) * self.count_creatures) * 0.75)
            print(f"{self.name} атакует в ответ {other.name} и наносит {self.attack_power} урона!")
            other.take_damage(self.attack_power)
        else:
            print(" ")


    def len1(self):
        print(self.count_creatures)


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
        if a == 1 or a == 2:
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


    def take_damage_with_defence(self, damage):
        self.health -= damage * self.procent_of_defence
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
    

    def create(self, count):
        self.count_creatures += count
        self.health += self.max_hp * self.count_creatures


def game_info():
    print('Игра похожая на Hero of might and magic есть два класса некроманты и люди в каждом классе есть пять видов юнитов и у каждого свои особенности для игры нужно создать армию: написать количество существ определенного класса.')
    print('От количества существ увеличивается их урон и здоровье.')
    print('Игра: для атаки противника используется функция attack также у некоторых персонажей есть два вида атак или свои способности.')
    pass


class Lich(Attack, Take_damage, Day_cycle):
    max_damage = 200
    min_damage = 100
    def __init__(self, count_creatures):
        self.curent_motion = 0
        self.count_creatures = count_creatures
        self.name = 'Лич'
        self.max_hp = 100
        self.health = self.max_hp * self.count_creatures
        self.mana = 100
        self.curent_day = 1


    def mage_attack(self, other):
        super().mage_attack(other = other)
        
    
    def ray_attack(self, other):
        super().ray_attack(other = other)
        

    def take_damage(self, damage):
        super().take_damage(damage = damage)
    

    def create(self, count):
        super().create(count = count)


    def __len__(self):
        super().len1()
        return self.count_creatures


    def spawn_minion(self):
        if self.health > 0:
            if self.curent_motion < self.curent_day:
                a = random.randint(1, 2)
                spawn = random.randint(1, 5)
                self.curent_motion += 1
                if a == 1:
                    zombie.spawn_new(spawn)
                    print(f'появилось {spawn} зомби')
                else:
                    skelet.spawn_new(spawn)
                    print(f'появилось {spawn} скелетов')
            else:
                print('Юнит устал и больше не может использовать способность')
        else:
            print(f"{self.name} не может использовать способность, так как он повержен.")
    

    def info(self):
        print('Лич может атаковать с помощбю функций mage_attack и ray_attack первая атака это обычная магическая атака, а вторая в 5 раз сильнее чем первая')
        print('Лич может кроме атаки призыватьсвоих преспешникав в виде зомби или скелетов в размере от 1 до 5')
        print(f'У лича сейчас {self.health} здоровья, {self.max_damage * self.count_creatures} максимальный урон,{self.min_damage * self.count_creatures} минимальный урон, {self.mana} маны')
    pass


class Skelet(Attack, Take_damage, Day_cycle):
    max_damage = 150
    min_damage = 100
    def __init__(self, count_creatures):
        self.curent_motion = 0
        self.count_creatures = count_creatures
        self.name = 'Скелет'
        self.health = 50 * self.count_creatures
        self.max_hp = 50
        self.arrows = 5
        self.curent_day = 1


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
    

    def create(self, count):
        super().create(count = count)


    def __len__(self):
        super().len1()
        return self.count_creatures
    

    def info(self):
        print('Скелет имеет две атаки мечом (sword_atack) и луком (bow_attack) после атаки луком ему не могут нанести ответный удар')
        print(f'У скелета сейчас {self.health * self.count_creatures} здоровья, {self.max_damage * self.count_creatures} максимальный урон,{self.min_damage * self.count_creatures} минимальный урон, {self.arrows} стрел')
    pass


class Zombie(Attack, Take_damage, Day_cycle):
    max_damage = 75
    min_damage = 50
    def __init__(self, count_creatures):
        self.curent_motion = 0
        self.count_creatures = count_creatures
        self.name = 'Зомби'
        self.health = 200 * self.count_creatures
        self.max_hp = 200
        self.curent_day = 1


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
    

    def create(self, count):
        super().create(count = count)


    def __len__(self):
        super().len1()
        return self.count_creatures
    

    def info(self):
        print('Зомби имеет большое количество здоровья но маленький урон, атакует с помощью функции sword_atack')
        print(f'У зомби сейчас {self.health * self.count_creatures} здоровья, {self.max_damage * self.count_creatures} максимальный урон,{self.min_damage * self.count_creatures} минимальный урон')
    pass


class Ghoast(Attack, Take_damage, Day_cycle):
    max_damage = 150
    min_damage = 75
    def __init__(self, count_creatures):
        self.curent_motion = 0
        self.count_creatures = count_creatures
        self.name = 'Призрак'
        self.health = 75 * self.count_creatures
        self.max_hp = 75
        self.curent_day = 1


    def retaliatory_attack(self, other):
        super().retaliatory_attack(other = other)


    def attack(self, other):
        super().attack(other = other)
        other.retaliatory_attack(ghoast)
    

    def take_damage(self, damage):
        super().take_damage_with_evasion(damage = damage)


    def is_alive(self):
        return self.health > 0
    

    def create(self, count):
        super().create(count = count)


    def __len__(self):
        super().len1()
        return self.count_creatures


    def info(self):
        print('Призрак может атаковать с помощью функции atack, а также может уклонится от удара с шансом 75%')
        print(f'У призрака сейчас {self.health * self.count_creatures} здоровья, {self.max_damage * self.count_creatures} максимальный урон,{self.min_damage * self.count_creatures} минимальный урон')
    pass


class Vampire(Attack, Take_damage, Day_cycle):
    max_damage = 150
    min_damage = 100
    def __init__(self, count_creatures):
        self.curent_motion = 0
        self.count_creatures = count_creatures
        self.name = 'Вампир'
        self.health = 150 * self.count_creatures
        self.max_hp = 150
        self.curent_day = 1
    

    def bite_attack(self, other):
        super().attack(other = other)
        other.retaliatory_attack(vampire)
    

    def take_damage(self, damage):
        super().take_damage(damage = damage)

    
    def retaliatory_attack(self, other):
        super().retaliatory_attack(other = other)


    def is_alive(self):
        return self.health > 0
    

    def create(self, count):
        super().create(count = count)

    
    def __len__(self):
        super().len1()
        return self.count_creatures


    def info(self):
        print('Вампир может атковать укусом (bite_attack) после атаки востанавливает 15% здоровья от урона который он нанес')
        print(f'У вампира сейчас {self.health * self.count_creatures} здоровья, {self.max_damage * self.count_creatures} максимальный урон,{self.min_damage * self.count_creatures} минимальный урон')
    pass


class Villager(Attack, Take_damage, Day_cycle):
    max_damage = 150
    min_damage = 100
    def __init__(self, count_creatures):
        self.curent_motion = 0
        self.count_creatures = count_creatures
        self.name = 'Крестьянин'
        self.health = 100 * self.count_creatures
        self.max_hp = 100
        self.curent_day = 1


    def pitchfork_attack(self, other):
        super().attack(other = other)
    

    def take_damage(self, damage):
        super().take_damage(damage = damage)
    

    def retaliatory_attack(self, other):
        super().retaliatory_attack(other = other)


    def create(self, count):
        super().create(count = count)


    def __len__(self):
        super().len1()
        return self.count_creatures
    

    def info(self):
        print('Крестьянин имеет среднее количество здоровья и средний урон атакует с помощью функции pitchfork_attack')
        print(f'У крестьянина сейчас {self.health * self.count_creatures} здоровья, {self.max_damage * self.count_creatures} максимальный урон,{self.min_damage * self.count_creatures} минимальный урон')
    pass


class Archer(Attack, Take_damage, Day_cycle):
    max_damage = 200
    min_damage = 100
    def __init__(self, count_creatures):
        self.curent_motion = 0
        self.count_creatures = count_creatures
        self.name = 'Лучник'
        self.health = 75 * self.count_creatures
        self.max_hp = 75
        self.arrows = 5
        self.curent_day = 1


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
    

    def create(self, count):
        super().create(count = count)


    def __len__(self):
        super().len1()
        return self.count_creatures


    def info(self):
        print('Лучник имеет малое количество здоровья но высокий урон, после атаки луком (bow_attack) не может получить ответный удар, также может атаковать мечом(sword_atack)')
        print(f'У лучника сейчас {self.health * self.count_creatures} здоровья, {self.max_damage * self.count_creatures} максимальный урон,{self.min_damage * self.count_creatures} минимальный урон, {self.arrows} стрел')
    pass


class Paladin(Attack, Take_damage, Day_cycle):
    max_damage = 200
    min_damage = 100
    def __init__(self, count_creatures):
        self.curent_motion = 0
        self.count_creatures = count_creatures
        self.name = 'Паладин'
        self.health = 300 * self.count_creatures
        self.max_hp = 300
        self.procent_of_defence = 0.7
        self.curent_day = 1


    def sword_attack(self, other):
        super().attack(other = other)
        other.retaliatory_attack(paladin)
    

    def retaliatory_attack(self, other):
        super().retaliatory_attack(other = other)
    

    def take_damage_with_defence(self, damage):
        super().paladin_take_damage(damage = damage)
    

    def is_alive(self):
        return self.health > 0
    

    def create(self, count):
        super().create(count = count)


    def __len__(self):
        super().len1()
        return self.count_creatures


    def info(self):
        print('Паладин имеет большое количество здоровья и высокий урон, паладин имеет защиту и получает на 30% меньше урона, атакует с помощью функции sword_attack')
        print(f'У паладина сейчас {self.health * self.count_creatures} здоровья, {self.max_damage * self.count_creatures} максимальный урон,{self.min_damage * self.count_creatures} минимальный урон')
    pass


class Grifon(Attack, Take_damage, Day_cycle):
    max_damage = 250
    min_damage = 150
    def __init__(self, count_creatures):
        self.curent_motion = 0
        self.count_creatures = count_creatures
        self.name = 'Грифон'
        self.health = 500 * self.count_creatures
        self.max_hp = 500
        self.curent_day = 1


    def attack(self, other):
        super().attack(other = other)
        


    def retaliatory_attack(self, other):
        super().retaliatory_attack(other = other)
    

    def take_damage(self, damage):
        super().take_damage(damage = damage)


    def is_alive(self):
        return self.health > 0
    

    def create(self, count):
        super().create(count = count)


    def __len__(self):
        super().len1()
        return self.count_creatures
    

    def info(self):
        print('Грифон имеет гиганское количество здоровья и высокий урон,может атаковать с помощью функции attack')
        print(f'У грифона сейчас {self.health * self.count_creatures} здоровья, {self.max_damage * self.count_creatures} максимальный урон,{self.min_damage * self.count_creatures} минимальный урон')
    pass


class Mage(Attack, Take_damage, Day_cycle):
    max_damage = 150
    min_damage = 100
    def __init__(self, count_creatures):
        self.curent_motion = 0
        self.count_creatures = count_creatures
        self.name = 'Маг'
        self.health = 100 * count_creatures
        self.max_health = 100 * self.count_creatures
        self.max_hp = 100
        self.mana = 100
        self.curent_day = 1


    def mage_attack(self, other):
        super().mage_attack(other = other)
    

    def meteorite_attack(self, other):
        super().meteorite_attack(other = other)
    

    def take_damage(self, damage):
        super().take_damage(damage = damage)


    def is_alive(self):
        return self.health > 0
    

    def create(self, count):
        super().create(count = count)


    def __len__(self):
        super().len1()
        return self.count_creatures


    def heal(self):
        if self.health > 0:
            if self.curent_motion < self.curent_day:
                self.curent_motion += 1
                if self.health < 100 * self.count_creatures:
                    self.health += self.max_health * 0.1
                    if self.health >= 100 * self.count_creatures:
                            self.health = self.max_health
                else:
                    self.health = self.max_health
            else:
                print('Юнит устал и больше не может использовать способность')
        else:
            print(f"{self.name} не может использовать способность, так как он повержен.")

    
    def info(self):
        print('Маг имеет среднее количество здоровья и средний урон, маг может востановить 10% от его максимального здоровья, может атаковать с помощью магии (mage_attack) и метеоритом meteorite_attack')
        print(f'У мага сейчас {self.health * self.count_creatures} здоровья, {self.max_damage * self.count_creatures} максимальный урон,{self.min_damage * self.count_creatures} минимальный урон, {self.mana} маны')   
    pass


class Player_people(Town, Day_cycle):

    def __init__(self, gold):
        self.gold = gold
        self.curent_day = 1
        self.curent_gold_amount = 0
        self.villager = Villager(0)
        self.archer = Archer(0)
        self.paladin = Paladin(0)
        self.grifon = Grifon(0)
        self.mage = Mage(0)
        self.gold_mine = Gold_mine()
    

    def count_of_gold(self):
        print(f'У вас сейчас {self.golda} золота')


    def create_villager(self, count):
        self.cost = 15
        print('Стоимость юнита одного 15 золота')
        if self.cost * count <= self.gold:
            self.villager.create(count)
            self.gold -= self.cost * count
            print(f'Вы купили {count} юнитов')
        else:
            print('Недостаточно золота')

    def villager_attack(self, other):
        self.villager.pitchfork_attack(other)
        other.retaliatory_attack(self.villager)


    def create_archer(self, count):
        self.cost = 50
        print('Стоимость юнита одного 50 золота')
        if self.cost * count <= self.gold:
            self.archer.create(count)
            self.gold -= self.cost * count
            print(f'Вы купили {count} юнитов')
        else:
            print('Недостаточно золота')
    

    def archer_sword_attack(self, other):
        self.archer.sword_attack(other)
        other.retaliatory_attack(self.archer)
    

    def archer_bow_attack(self, other):
        self.archer.bow_attack(other)


    def create_paladin(self, count):
        self.cost = 80
        print('Стоимость юнита одного 80 золота')
        if self.cost * count <= self.gold:
            self.paladin.create(count)
            self.gold -= self.cost * count
            print(f'Вы купили {count} юнитов')
        else:
            print('Недостаточно золота')


    def paladin_attack(self, other):
        self.paladin.sword_attack(other)
        other.retaliatory_attack(self.paladin)


    def create_grifon(self, count):
        self.cost = 260
        print('Стоимость юнита одного 260 золота')
        if self.cost * count <= self.gold:
            self.grifon.create(count)
            self.gold -= self.cost * count
            print(f'Вы купили {count} юнитов')
        else:
            print('Недостаточно золота')


    def grifon_attack(self, other):
        self.grifon.attack(other)
        other.retaliatory_attack(self.grifon)


    def create_mage(self, count):
        self.cost = 600
        print('Стоимость юнита одного 600 золота')
        if self.cost * count <= self.gold:
            self.mage.create(count)
            self.gold -= self.cost * count
            print(f'Вы купили {count} юнитов')
        else:
            print('Недостаточно золота')
    

    def mag_mage_attack(self, other):
        self.mage.mage_attack(other)
        other.retaliatory_attack(self.mage)
    

    def mag_meteorite_attack(self, other):
        self.mage.meteorite_attack(other)
        other.retaliatory_attack(self.mage)


    def army_info(self):
        print('Армия людей')
        print(f'{self.villager.count_creatures} крестьянинов')
        print(f'{self.archer.count_creatures} лучников')
        print(f'{self.paladin.count_creatures} паладинов')
        print(f'{self.grifon.count_creatures} грифонов')
        print(f'{self.mage.count_creatures} магов')
    

    def day_cycle(self):
        self.gold_mine.day_cycle()
        self.curent_gold_amount += self.production_in_day * self.curent_day
        self.villager.day_cycle()
        self.archer.day_cycle()
        self.paladin.day_cycle()
        self.grifon.day_cycle()
        self.mage.day_cycle()
        self.curent_day += 1
    

class Player_necromancers(Town, Day_cycle):

    def __init__(self, gold):
        self.gold = gold
        self.curent_day = 1
        self.curent_gold_amount = 0
        self.lich = Lich(0)
        self.skelet = Skelet(0)
        self.zombie = Zombie(0)
        self.ghoast = Ghoast(0)
        self.vampire = Vampire(0)
        self.gold_mine = Gold_mine()
        

    def count_of_gold(self):
        print(f'У вас сейчас {self.golda} золота')


    def create_lich(self, count):
        self.cost = 600
        print('Стоимость юнита одного 600 золота')      
        if self.cost * count <= self.gold:
            self.lich.create(count)
            self.gold -= self.cost * count
            print(f'Вы купили {count} юнитов')
        else:
            print('Недостаточно золота')
    

    def lich_mage_attack(self, other):
        self.lich.mage_attack(other)
        other.retaliatory_attack(self.lich)

    
    def lich_ray_attack(self, other):
        self.lich.ray_attack(other)
        other.retaliatory_attack(self.lich)


    def create_skelet(self, count):
        self.cost = 30
        print('Стоимость юнита одного 30 золота')
        if self.cost * count <= self.gold:
            self.skelet.create(count)
            self.gold -= self.cost * count
            print(f'Вы купили {count} юнитов')
        else:
            print('Недостаточно золота')


    def skelet_bow_attack(self, other):
        self.skelet.bow_attack(other)


    def skelet_sword_attack(self, other):
        self.skelet.sword_attack(other)
        other.retaliatory_attack(self.skelet)


    def create_zombie(self, count):
        self.cost = 15
        print('Стоимость юнита одного 15 золота')
        if self.cost * count <= self.gold:
            self.zombie.create(count)
            self.gold -= self.cost * count
            print(f'Вы купили {count} юнитов')
        else:
            print('Недостаточно золота')


    def zombie_attack(self, other):
        self.zombie.sword_attack(other)
        other.retaliatory_attack(self.zombie)
        

    def create_ghoast(self, count):
        self.cost = 100
        print('Стоимость юнита одного 100 золота')
        if self.cost * count <= self.gold:
            self.ghoast.create(count)
            self.gold -= self.cost * count
            print(f'Вы купили {count} юнитов')
        else:
            print('Недостаточно золота')
        

    def ghoast_attack(self, other):
        self.ghoast.attack(other)
        other.retaliatory_attack(self.ghoast)


    def create_vampire(self, count):
        self.cost = 250
        print('Стоимость юнита одного 250 золота')
        if self.cost * count <= self.gold:
            self.vampire.create(count)
            self.gold -= self.cost * count
            print(f'Вы купили {count} юнитов')
        else:
            print('Недостаточно золота')
    

    def vampire_attack(self, other):
        self.vampire.attack(self.other)
        other.retaliatory_attack(self.vampire)


    def army_info(self):
        print('Армия некромантов')
        print(f'{self.lich.count_creatures} личей')
        print(f'{self.skelet.count_creatures} скелетов')
        print(f'{self.zombie.count_creatures} зомби')
        print(f'{self.ghoast.count_creatures} призраков')
        print(f'{self.vampire.count_creatures} вампиров')
        
    
    def day_cycle(self):
        self.gold_mine.day_cycle()
        self.curent_gold_amount += self.production_in_day * self.curent_day
        self.lich.day_cycle()
        self.skelet.day_cycle()
        self.zombie.day_cycle()
        self.ghoast.day_cycle()
        self.vampire.day_cycle()
        self.curent_day += 1
    

    def check_count_of_gold(self):
        print(self.gold)


if __name__ == '__main__':
    p1 = Player_people(100000)
    p2 = Player_necromancers(100000)
    p1.create_villager(50)
    p2.create_lich(5)
    p2.create_ghoast(7)
    p2.check_count_of_gold()
    p1.army_info()
    p2.army_info()
    p2.lich_ray_attack(p1.villager)
    p1.villager_attack(p2.ghoast)
    p2.create_gold_mine()
    p2.level_up_gold_mine()
    p2.check_curent_day()
    p2.day_cycle()
    p2.check_curent_day()
    p2.collect_products_with_gold_mine()
    p2.check_count_of_gold()