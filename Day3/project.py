#                               # Treasure Island Adventure Game
# 
# *******************************************************************************************    #                                                                                           #
#                                    ____...------------...____                             #
#                               _.-"` /o/__ ____ __ __  __ \o\_`"-._                        #
#                             .'     / /                    \ \     '.                      #
#                             |=====/o/======================\o\=====|                      #
#                             |____/ /________..____..________\ \____|                      #
#                             /  _/  \_     <_o#\__/#o_>     _/  \_  \                      #
#                             \________________\####/________________/                      #
#                              |===\!/========================\!/===|                       #
#                              |   |=|          .---.         |=|   |                       #
#                              |===|o|=========/     \========|o|===|                       #
#                              |   | |         \() ()/        | |   |                       #
#                              |===|o|======{'-.) A (.-'}=====|o|===|                       #
#                              | __/ \__     '-.\uuu/.-'    __/ \__ |                       #
#                              |         ==== .'.'^'.'.====         |                       #
#                              |  _\o/   __  {.' __  '.} _   _\o/  _|                       #
#                              `""""-""""""""""""""""""""""""""-""""`                       #
#                             _                                                             #
#                            | |                                                            #
#                            | |_ _ __ ___  __ _ ___ _   _ _ __ ___                         #
#                            | __| '__/ _ \/ _` / __| | | | '__/ _ \                        #
#                            | |_| | |  __/ (_| \__ \ |_| | | |  __/                        #
#                             \__|_|  \___|\__,_|___/\__,_|_|  \___|                        #
# *******************************************************************************************
 

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction = input("The road is dark and narrow through the thick jungle, \nsuddenly you reach a crossroad, where do you want to go, left or right? ").lower()

if direction == "left":
    # Continue in game
    swim = input("You turned left and avoied a death hole. \nYou approach a lake at high tide, do you want to swim or wait? ").lower()
    if swim == "wait":    
        print("You waited and a boat arrived to take you across. You move forward in your quest!")
    else:
        print("You tried to swim and were eaten by a crocodile. Game Over.")
    door = input("You see a castle in the distance, You reach the castle by nightfall and sneak inside.\nYou walk down a dark staircase and enter a secret crypt, you are faced with 3 doors, one yellow, one red and one blue, one of the doors contains the treasure...\nDestiny awaits, which door do you choose? red, blue or yellow? ").lower()
    if door == "yellow":
        print("You Win, You found the treasure and escaped through a Trap door!")
    elif door == "blue":
        print("You are ripped apart by savage beasts, Game Over!") 
    elif door == "red":
        print("You are Burned alive by a raging inferno, Game Over!")
    else:
        print("You didn't enter a valid response, Game Over!")
else:
    print("You fell in a hole. Game Over.")
  