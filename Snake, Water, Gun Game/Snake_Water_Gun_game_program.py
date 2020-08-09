#This is a Snake, Water and Gun Game.

import random
list = ['s', 'w', 'g']# this is a list for snake, water and gun..

# We have 10 chances.
chances = 10
no_of_chance = 0
comp_points = 0
your_points = 0

print("This is Your Snake, Water and Gun Game..")
print("Chose 's' for Snake, 'w' for Water, 'g' for Gun..")

# This is the Game

while no_of_chance < chances:
    # We input the choice of the user here.
    _input = input('Snake, Water or Gun:\n')
    #Here we select the random choice of the computer from the list.
    _random = random.choice(list)

    if _input == _random:
        print("Its a Tie. 0 points to each..")

    # When user inputs S.
    elif _input == "s" and _random == "w":
        your_points = your_points + 1
        print(f"Your input was {_input} and the Computers choice was {_random}. ")
        print("You win 1 point..")
        print(f"Your points are {your_points} and the Computer's points are {comp_points}. ")

    elif _input == "s" and _random == "g":
        comp_points = comp_points + 1
        print(f"Your input was {_input} and the Computers choice was {_random}. ")
        print("Comp wins 1 point..")
        print(f"Your points are {your_points} and the Computer's points are {comp_points}. ")
        
    # When user inputs W.
    elif _input == "w" and _random == "s":
        comp_points = comp_points + 1
        print(f"Your input was {_input} and the Computers choice was {_random}. ")
        print("Comp wins 1 point..")
        print(f"Your points are {your_points} and the Computer's points are {comp_points}. ")

    elif _input == "w" and _random == "g":
        your_points = your_points + 1
        print(f"Your input was {_input} and the Computers choice was {_random}. ")
        print("You win 1 point..")
        print(f"Your points are {your_points} and the Computer's points are {comp_points}. ")
        
    # When user inputs G.
    elif _input == "g" and _random == "s":
        your_points = your_points + 1
        print(f"Your input was {_input} and the Computers choice was {_random}. ")
        print("You win 1 point..")
        print(f"Your points are {your_points} and the Computer's points are {comp_points}. ")

    elif _input == "g" and _random == "w":
        comp_points = comp_points + 1
        print(f"Your input was {_input} and the Computers choice was {_random}. ")
        print("Comp wins 1 point..")
        print(f"Your points are {your_points} and the Computer's points are {comp_points}. ")

    else:
        print("The input is Wrong.")

    no_of_chance = no_of_chance+1
    print(f"{chances - no_of_chance} are left out of {chances} \n")

    print("The Game is Over Now..")

if comp_points == your_points:
    print("Its a Tie.")

elif comp_points > your_points:
    print("The Computer has Won and you lost.")
else:
    print("You Won and Computer Lost.")

print(f"You have {your_points} points and the Computer has {comp_points} points.")
