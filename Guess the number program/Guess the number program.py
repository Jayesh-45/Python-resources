# no of guesses are 9
# prints no of guesses left
# prints no of guesses you took to finish
# prints game over when you guess all your chances incorrectly or congratulations when you guess your number correctly

num = 15
num_of_guesses = 1
print("You have only 9 chances to guess the correct number between 1-50..")
while(num_of_guesses<=9):
    guess_n = int(input("Guess your first chance..\n"))
    if(guess_n<15):
        print("You have entered a smaller number. Try Entering a bigger number..(",end=" ")
        print(9 - num_of_guesses, "guesses left )")
    elif(guess_n>15):
        print("you have entered a bigger number. Try Entering a smaller number..(",end=" ")
        print(9 - num_of_guesses, "guesses left )")
    else:
        print("You guessed the correct number")
        print("The number of guesses you took to finish are:",num_of_guesses)
        break

    num_of_guesses = num_of_guesses+1
if(num_of_guesses>9):
    print("You lost all your chances. Try again Later..\n")
