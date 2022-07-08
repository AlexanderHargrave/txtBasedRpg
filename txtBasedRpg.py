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