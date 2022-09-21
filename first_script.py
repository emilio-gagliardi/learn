# Number Guessing Game
# number 1-100
# 100 points
# -10 for wrong answers
# at zero points, restart game
# written by: Emilio
import random


# set variables


def guessing_game():
    randomNumber = int(random.randrange(1, 101))
    guessedCorrect = False
    totalPoints = 100
    penalty = 10
    guess = int(input('Choose a number between 1-100: '))

    while guess != randomNumber and totalPoints > 0:
        print("Incorrect, deducting 10")
        if guess > randomNumber:
            print("Hint: you guessed to high")
        else:
            print("Hint: you guessed too low")
        totalPoints -= penalty
        guess = int(input('choose again '))

    if guess == randomNumber:
        guessedCorrect = True

    if guessedCorrect:
        print("You guessed correctly.")
    else:
        print("you guessed incorrectly. The correct answer was: " + str(randomNumber))
    return guessedCorrect


first_hand = guessing_game()
response = input("Would you like to play again? (Y) or (N) ")
if response == "Y" or response == "y":
    guessing_game()
