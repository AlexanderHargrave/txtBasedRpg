from random import randint


class Base:
    def __init__(self, species, level, hp, max_hp, atk, current_atk, defence, speed):
        self.species = species
        self.level = level
        self.hp = hp
        self.max_hp = max_hp
        self.atk = atk
        self.current_atk = current_atk
        self.defence = defence
        self.speed = speed

    def get_species(self):
        return self.species

    def get_level(self):
        return self.level

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.max_hp

    def get_atk(self):
        return self.atk

    def get_current_atk(self):
        return self.current_atk

    def get_defence(self):
        return self.defence

    def get_speed(self):
        return self.speed

    def change_level(self, lvl_change):
        self.level += lvl_change

    def change_hp(self, hp_change):
        self.hp += hp_change
        if self.hp < 0:
            self.hp = 0

    def change_max_hp(self, max_hp_change):
        self.max_hp += max_hp_change

    def change_atk(self, atk_change):
        self.atk += atk_change

    def change_current_atk(self, current_atk_change):
        self.current_atk += current_atk_change

    def change_defence(self, defence_change):
        self.defence += defence_change

    def change_speed(self, speed_change):
        self.speed += speed_change

    def check_death(self):
        if self.hp == 0:
            return True
        else:
            return False


class Hero(Base):
    def __init__(self, species, level, hp, max_hp, atk, current_atk, defence,
                 speed, name, xp, xp_needed, gold, accuracy):
        Base.__init__(self, species, level, hp, max_hp, atk, current_atk, defence, speed)
        self.name = name
        self.xp = xp
        self.xp_needed = xp_needed
        self.gold = gold
        self.accuracy = accuracy

    def get_xp(self):
        return self.xp

    def get_xp_needed(self):
        return self.xp_needed

    def get_gold(self):
        return self.gold

    def get_accuracy(self):
        return self.accuracy

    def change_xp(self, xp_change):
        self.xp += xp_change
        if self.xp >= self.xp_needed:
            self.xp -= self.xp_needed
            self.level_up()


    def change_xp_needed(self, xp_needed_change):
        self.xp_needed += xp_needed_change

    def change_gold(self, gold_change):
        self.gold += gold_change

    def level_up(self):
        status_points = 5
        self.change_level(1)
        print("You have leveled up!")
        print("You are now level " + str(self.get_level()) + "!")
        print("You have " + str(status_points) + " to use!")
        print("Your current stats are;")
        print("HP: " + str(self.get_hp()) + "\t\tATK: " + str(self.get_atk()))
        print("DEF: " + str(self.get_defence()) + "\t\tSPD: "+ str(self.get_speed()))


User = Hero("Human", 1, 10, 10, 3, 3, 2, 5, "Hero", 0, 50, 0, 95)
User.level_up()