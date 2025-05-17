#07 Prove: Assignment Milestone - Wordle
#Hansen, Kristi 9am
#Braden Roenfeldt

secretword = "BEANS"
print("You have 6 guess to find the correct word.")
userword = input("Make a 5 letter guess: ")
guess_number = 1
if ((userword.upper() == secretword) and (guess_number == 1)):
    print(f"You guessed the word in {guess_number} try!")
else:
    while (secretword != userword):
        if (userword.upper() == secretword):
            print(f"You guessed the word in {guess_number} tries!")
            exit()
        elif (guess_number == 7):
            print("Sorry game over, too many tries.")
            exit()
        else:
            guess_number += 1
            userword = input("Make a 5 letter guess: ")
            print(guess_number)
