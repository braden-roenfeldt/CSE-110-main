#07 Team activity - Number Guessing Game
#Hansen, Kristi 9am
#Braden Roenfeldt

import random

user_guess = 0
guess_num = 0
play_again = input("Welcome to the number guessing game, you will have to guess a random number between 1 and 35. Are you ready to start? (yes/no) ")
while play_again.lower() == "yes":
    rand_num = random.randint(1,35)
    while user_guess != rand_num:
        guess_num += 1
        user_guess = int(input("Guess the random number between 1 and 35. "))
        if user_guess != rand_num:
            print("Sorry, try again.")
            if user_guess < rand_num:
                print("Guess higher.")
            else:
                print("Guess lower.")
        else:
           print("Nice guess.")
           print(f"It took you {guess_num} tries to guess correctly.")
           play_again = "no"
           play_again = input("Would you like to play again? (yes/no) ")

