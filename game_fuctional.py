import random as rand

class Entity():
    def __init__(self):
        self.hp = 100
	
class Item():
    def __init__(self, name, is_equipable, worth):
        self.name = name 
        self.is_equipable = is_equipable
        self.worth = worth


class Weapon(Item):
    def __init__(self, name, is_equipable, worth, damage, max_crit):
        super().__init__(name, is_equipable, worth)
        self.damage = damage 
        self.max_crit = max_crit 
        
class Enemy():
    
    def __init__(self, name, attack, hp, chance):
        self.name = name 
        self.attack = attack
        self.hp = hp
        self.drop_chance = chance
        
    def attack_enemy(self, enemy):
        enemy.current_health -= self.attack
        self.hp -= enemy.attack * round(rand.uniform(1.0, enemy.equipment["weapon"].max_crit), 1)
        return self.attack


class Player(Entity):
	
    def __init__(self, player_class=None):
        super().__init__()
        self.current_health = self.hp
        init_weapon = Weapon("Fists", True, 1000, 15, 1.5)
        self.player_class = player_class 
        self.attack = init_weapon.damage 
        self.equipment = {
            "body": None, 
            "head": None, 
            "legs": None, 
            "weapon": init_weapon, 
            "inventory": []
        }	
    
    def pick_up(self, item):
        self.equipment["inventory"].append(item)
    
    def open_inventory(self):
        for i in range(len(self.equipment["inventory"])):
            print(i + 1, self.equipment["inventory"][i])
            
        print("What to do?")
        print("1) Equip an item")
        print("2) Drop an item")
        print("3) Eat")
        print("4) Close the inventory")

        
    def eat(self, item):
        pass 
    
    def equip(self, item): 
        if item.is_equipable:
            if isinstance(item, Weapon):
                self.equipment["weapon"] = item
                self.attack = item.damage
    
    def drop(self, item):
        pass 
    
    def attack_enemy(self, enemy):
        ret_dmg = self.attack * round(rand.uniform(1.0, self.equipment["weapon"].max_crit), 1)
        enemy.hp -= ret_dmg
        self.current_health -= enemy.attack 
        return ret_dmg



game_weapons = {
    "Pistol": Weapon("Pistol", True, 1000, 40, 2.0),
    "Knife": Weapon("Knife", True, 500, 25, 2.5)
    }
        
game_classes = {"1":"Human", "2":"Robot", "3":"Zhizha"}