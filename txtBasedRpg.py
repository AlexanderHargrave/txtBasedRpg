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

    def set_hp(self, hp_set):
        self.hp = hp_set
        self.max_hp = hp_set

    def set_attack(self, atk_set):
        self.atk = atk_set
        self.current_atk = atk_set

    def set_defence(self, def_set):
        self.defence = def_set

    def set_speed(self, speed_set):
        self.speed = speed_set

    def set_stats(self, hp, atk, defence, speed):
        self.set_hp(hp)
        self.set_attack(atk)
        self.set_defence(defence)
        self.set_speed(speed)

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
                 speed, name, xp, xp_needed, gold, accuracy, status_points):
        Base.__init__(self, species, level, hp, max_hp, atk, current_atk, defence, speed)
        self.name = name
        self.xp = xp
        self.xp_needed = xp_needed
        self.gold = gold
        self.accuracy = accuracy
        self.status_points = status_points

    def get_xp(self):
        return self.xp

    def get_xp_needed(self):
        return self.xp_needed

    def get_gold(self):
        return self.gold

    def get_accuracy(self):
        return self.accuracy

    def get_status_points(self):
        return self.status_points

    def change_xp(self, xp_change):
        self.xp += xp_change
        if self.xp >= self.xp_needed:
            self.xp -= self.xp_needed
            self.level_up()

    def change_xp_needed(self, xp_needed_change):
        self.xp_needed += xp_needed_change

    def change_gold(self, gold_change):
        self.gold += gold_change

    def change_status_points(self, status_points_change):
        self.status_points += status_points_change

    def level_up(self):
        self.change_status_points(5)
        self.change_xp_needed(15)
        self.change_level(1)
        print("You have leveled up!")
        self.status_screen()
        ask = False
        use_status_p = input("Would you like to use your Status Points(y/n): ")
        while not ask:
            if use_status_p == "y":
                self.use_status_points()
                ask = True
            elif use_status_p == "n":
                ask = True
                pass
            else:
                use_status_p = input("Would you like to use your Status Points(y/n): ")



    def status_screen(self):
        print("You are now level " + str(self.get_level()) + "!")
        print("Your current stats are;")
        print("HP: " + str(self.get_hp()) + "\t\tATK: " + str(self.get_atk()))
        print("DEF: " + str(self.get_defence()) + "\t\tSPD: " + str(self.get_speed()))
        print("You currently have " + str(self.get_xp()) +
              "XP\t\tXP Needed: " + str(self.get_xp_needed() - self.get_xp()))
        print("You have " + str(self.get_status_points()) + " to use!")

    def use_status_points(self):
        current_status_points = self.get_status_points()
        hp_status_ask, atk_status_ask, def_status_ask, speed_status_ask = 0, 0, 0, 0
        confirm = False
        while not confirm:
            hp_status_ask = int(input("How many Status Points would you like to put into HP: "))
            while hp_status_ask > current_status_points:
                print("You do not have enough Status Points.")
                hp_status_ask = int(input("How many Status Points would you like to put into HP: "))
            current_status_points -= hp_status_ask
            print("You now have " + str(current_status_points) + " status points left.")
            atk_status_ask = int(input("How many Status Points would you like to put into ATK: "))
            while atk_status_ask > current_status_points:
                print("You do not have enough Status Points.")
                atk_status_ask = int(input("How many Status Points would you like to put into ATK: "))
            current_status_points -= atk_status_ask
            print("You now have " + str(current_status_points) + " status points left.")
            def_status_ask = int(input("How many Status Points would you like to put into DEF: "))
            while def_status_ask > current_status_points:
                print("You do not have enough Status Points.")
                def_status_ask = int(input("How many Status Points would you like to put into DEF: "))
            current_status_points -= def_status_ask
            print("You now have " + str(current_status_points) + " status points left.")
            speed_status_ask = int(input("How many Status Points would you like to put into SPD: "))
            while speed_status_ask > current_status_points:
                print("You do not have enough Status Points.")
                speed_status_ask = int(input("How many Status Points would you like to put into SPD: "))
            current_status_points -= speed_status_ask
            print("You now have " + str(current_status_points) + " status points left.")
            confirm_status_selection = input("You have "
                                             + str(current_status_points)
                                             + " left, would you like to choose again(y/n): ")
            valid_choice = False
            while not valid_choice:
                if confirm_status_selection == "y":
                    confirm = True
                    valid_choice = True
                elif confirm_status_selection == "n":
                    print("You have reset your status choices!")
                    current_status_points = self.get_status_points()
                    print("You now have " + str(current_status_points) + " status points left.")
                    valid_choice = True
                else:
                    print("You have not given either (y/n)!")
                    confirm_status_selection = input("You have "
                                                     + str(current_status_points)
                                                     + " status points left, would you like to choose again(y/n): ")

        self.change_status_points(-current_status_points)
        self.change_max_hp(3 * hp_status_ask)
        self.change_atk(atk_status_ask)
        self.change_defence(def_status_ask)
        self.change_speed(speed_status_ask)
        self.after_change()
        self.status_screen()

    def after_change(self):
        self.set_hp(self.get_max_hp())
        self.set_attack(self.get_atk())

class Monster(Base):
    def __init__(self, species, level, hp, max_hp, atk, current_atk, defence,
                 speed):
        Base.__init__(self, species, level, hp, max_hp, atk, current_atk, defence, speed)

    def stats_calcs(self):
        lvl = self.get_level()
        species = self.get_species()
        hp_random = randint(1, 6)
        atk_random = randint(1, 6)
        if species == "Goblin":
            self.set_stats(round(3 * lvl * (1+(hp_random-3)/10)), round(lvl * (1+(atk_random-3)/10)), 0, round(0.5*lvl))
        elif species == "Slime":
            self.set_stats(round(5 * lvl * (1+(hp_random-3)/10)), round(0.5 * lvl * (1+(atk_random-3)/10)), 1, 0)
        elif species == "Kobold":
            self.set_stats(round(2 * lvl * (1+(hp_random-3)/10)),
                           round(0.75 * lvl * (1+(atk_random-3)/10)), round(0.5 * lvl), round(2 * lvl))
        elif species == "Golem":
            self.set_stats(round(5 * lvl * (1+(hp_random-3)/10)),
                           round(0.25*lvl * (1+(atk_random-3)/10)), round(1.2 * lvl), round(0.2 * lvl))


User = Hero("Human", 1, 10, 10, 3, 3, 2, 5, "Hero", 0, 50, 0, 95, 0)