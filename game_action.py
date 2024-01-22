import game_fuctional as gf
import random as rand
import time
def fight(player, enemy):
    turn = rand.choice([player, enemy])
    while player.current_health > 0 and enemy.hp > 0:
        if turn == 0:
            turn = 1 
            print(f"Your Turn! HP = {player.current_health}, Enemy HP = {enemy.hp}")
            print("1 - Attack, 2 - Pass, 3 - Try to run away")
            user_input = str(input())
            if user_input == '1':
                dmg = player.attack_enemy(enemy)
                print(f"You hit the enemy with {player.equipment['weapon'].name} and did {dmg} damage! But the enemy also hit you...")
            elif user_input == "3":
                chance = rand.randint(0, 100 - (player.current_health / 2))
                if chance > 60:
                    print("You ran away from the enemy!")
                    return player.current_health

                else:
                    enemy.attack_enemy(player)
                    print("Enemy extra hits you!")
            time.sleep(2)
                
        else:
            turn = 0
            print(f"Enemy's turn, HP = {player.current_health}, Enemy HP = {enemy.hp}")
            time.sleep(3)
            enemy_choice = rand.choice(["hit", "pass"])
            if enemy_choice == "hit":
                dmg = enemy.attack_enemy(player)
                print(f"Enemy hits you with {dmg} damage, but you also hit him")
            else:
                print("Enemy does not hit you")
            time.sleep(2)
    if enemy.hp <= 0:
        print("Enemy is dead")
        return player.current_health
    else:
        print("You are dead")
        return player.current_health
        


print("Hello! Let's play the game!")
print("Which class would you like to play? ")
print("1 - Human, 2 - Robot, 3 - Zhizha")
print("'-1' - Close")
user_input = str(input())

if user_input == "1" or user_input == "2" or user_input == "3":
        player = gf.Player(gf.game_classes[user_input])
else:
    if user_input == '-1':
        exit(1)
    else:
        print("Please enter a number!")

while True:
    
    
    zombie1 = gf.Enemy("Zombie", 10, 150, 0.7)
    # player.pick_up(gf.game_weapons["Pistol"])
    # player.equip(gf.game_weapons["Knife"])
    print(player.equipment["weapon"].name)

    print(f"The {player.player_class} was walking down the road and met {zombie1.name}, it time to fight...")
    player.current_health = fight(player, zombie1)
    
    if player.current_health <= 0:
        break
    
    print("The fight was hard... Let's check the loot!")
    time.sleep(5)
    

    if zombie1.drop_chance >= rand.uniform(0.0, 1.0):
        item = rand.choice(list(gf.game_weapons.keys()))
        print(f"You found the {item} with damage {gf.game_weapons[item].damage}!")
        print(f"Press 1 to pick the {item} or 0 to skip")
        time.sleep(1)
        
        user_input = str(input())
        if user_input == "1":
            player.equip(gf.game_weapons[item])
        else:
            print("You skipped the item")
    else:
        print("You found nothing...")
    
    time.sleep(5)
