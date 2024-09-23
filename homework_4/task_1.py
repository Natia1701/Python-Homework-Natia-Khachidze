import random

number_of_players = int(input("please enter number of players- "))

for n in range (number_of_players) :
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    print (str(dice_1), str(dice_2))
    