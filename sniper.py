"""
Sniper duel


TODO:
Fix end of the game glitches
Fix the inputs changing them from 1-3 to actual weapons with different chances to hit
Add critical hits




"""

import random

while True:

    print("!")

    enemy_HP = 20
    your_HP = 20

    if random.randint(0, 1) == 0:
        current_player = "infiltrator"
    else:
        current_player = "sniper"

    while enemy_HP or your_HP >= 0:
      
        print("The sniper is aiming at you. \nSniper HP:" + str(enemy_HP), "\nYour HP:" + str(your_HP))
        print

        if current_player == "infiltrator":
            
            print("1, 2, or 3")
            
            player_choice = ""
            while player_choice not in ["1", "2", "3"]:
                if your_HP >= 1:
                    player_choice = input("How will you attack?")
                else:
                    print("You are dead...")
                   

            player_choice = int(player_choice)
            enemy_HP = enemy_HP - player_choice
            print("Your attack hits for " + str(player_choice) + " damage!")
            print

            if your_HP == 0:
                
                print()
                print("Another dead soldier")
                break
            current_player = "sniper"

        else:

            computer_choice = random.randint(0, 3)
            your_HP = your_HP - computer_choice
            if computer_choice <=0:
                print("The sniper missed!\n")
            elif computer_choice >=1 and enemy_HP >=1:
                print("The sniper fires at you and hits for " + str(computer_choice) + " Damage!\n")
            print

            if enemy_HP <=1:
                print("Enemy down!")
                print()
                print("Advance immediately!")
                break
            current_player = "infiltrator"

    print
    play_again = input("Do you want to play again? ")
    if play_again.lower().startswith("y"):
        continue
    else:
        print("Goodbye")
        break

