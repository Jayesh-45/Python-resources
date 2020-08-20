> ## This is a Snake, Water and Gun Game.

This Game is played by **The User and The Computer**.

- The Computer selects a random choice between Snake, Water or a Gun and User inputs his choice.
- Based on the rules that are inbuilt in the game, The User or The Computer gets a point and the game is carried on.
- There are 10 chances and the one who gets the maximum points Wins Finally.
- The Scores of both the players are displayed after each chance.
- If the user and the computer enter same choice, then it is a tie and no one gets any points.
- This program uses the "random module", that is used by the computer to select randomly between a snake, water or gun.


### The Rules of the game are simple:

1. If the Player inputs Snake and the other one inputs Water,
the Snake wins as it drinks Water. //Bad logic.

2. If the Player inputs Snake and the other one inputs Gun,
the Gun kills the Snake. //Bad logic. 

3. If the Player inputs Water and the other one inputs Gun,
the Water wins as the Gun gets lost in the Water. //Bad logic. 


## The Code::

First we import the "random module" and create a list for the options of snake, water and gun.
	
    list = ['s', 'w', 'g']# This is the list.

Then we initialize some variables for the chances, noofchances taken, and points for computer and you.
- We initialize the value of chances = 10.
- And rest all values are 0.

The Game will start from the while loop, that runs untill the chances become greater than the noofchances.
- Then We input the choice of the user .
	
       _input = input('Snake, Water or Gun:\n')

Then we select the random choice of the computer from the list.

		_random = random.choice(list)

When the choices of both The User and The Computer are same, it's a Tie.
- Noone gets any point in that case.

		    if _input == _random:
   		      print("Its a Tie. 0 points to each..")
            
#### If the inputs are not the same.

----
1]. The First Case: # When user inputs S(Snake).

When the User inputs S(Snake) and Computer selects W(Water), you get one point.

		your_points = your_points + 1

- Then with the help of "fstrings", we print The inputs of both, the user and the Computer.

		print(f"Your input was {_input} and the Computers choice was {_random}. ")

- Also, the scores are shown after the points are allotted.

		print(f"Your points are {your_points} and the Computer's points are {comp_points}. ")
            
When the User inputs S(Snake) and Computer selects G(Gun), The Computer gets one point.

		comp_points = comp_points + 1

Then with the help of "fstrings", the inputs of both, the user and the Computer are again printed.

		print(f"Your input was {_input} and the Computers choice was {_random}. ")

Also, the scores are again showed after the points are allotted.

----
Similarly the Program is written to abide by the rules of the game which includes both the scenarios.

- When the user enters Water(W), and the computer selects one of the remaining two choices of Snake(S) or Gun(G).
- Similarly for the situation where the user enters Gun(G).

After every chance, the program increments the value of noofchance by 1.

And after all the 10 chances are completed, that will take the value of noofchance till 10,
after which the game stopps.

		no_of_chance = no_of_chance+1
		print(f"{chances - no_of_chance} are left out of {chances} \n")

Also, the remaining chances are printed with the help of fstrings.
















