from random import randint

class Base:
    def __init__(self,species,level,hp,maxhp,atk,currentatk,defence,speed):
        self.species = species
        self.level = level
        self.hp = hp
        self.maxhp = maxhp
        self.atk = atk
        self.currentatk = currentatk
        self.defence = defence
        self.speed = speed
    def getspecies(self):
        return self.species
    def getlevel(self):
        return self.level
    def gethp(self):
        return self.hp
    def getmaxhp(self):
        return self.maxhp
    def getatk(self):
        return self.atk
    def getcurrentatk(self):
        return self.currentatk
    def getdefence(self):
        return self.defence
    def getspeed(self):
        return self.speed
    def change_level(self,lvlchange):
        self.level += lvlchange