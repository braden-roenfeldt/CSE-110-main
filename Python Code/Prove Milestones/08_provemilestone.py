#08 Prove assignment
#Hansen, Kristi
#Braden Roenfeldt

import random


play_again = True

while play_again == True: #checks if they said to play again
    guess_number = 1
    wordlist = ["BEANS", "HOUSE", "CLOCK"]
    secretword = random.choice(wordlist)
    user_input = ""
    print("You have 6 guess to find the correct word.")
    user_input = input("Make a 5 letter guess: ")

    while user_input.upper() != secretword: #checks that input doesnt equal secretword
        if len(user_input) != 5:
            print("Your word was not the right length. Try again")
            guess_number -= 1
        for i in range(len(user_input.upper())):    #goes through each letter to see if they match
            if (user_input[i].upper() == secretword[i]):
                print(f"{secretword[i]}",end="")    #prints out each letter if they match
            else:
                print(f"_", end="") #prints out underscore if it isnt the same
        print()
        user_input = input("Try Again:")
        guess_number += 1
        if guess_number == 6:
            user_input = secretword
            print("Sorry, you took to many tries to guess.")



    if guess_number == 1 and user_input.upper() == secretword:
        print(f"Correct! You guess the word in {guess_number} try!")
    else:
        print(f"Correct! You guess the word in {guess_number} tries!")
    user_input = input("Would you like to try again? (yes/no) ")
    if user_input.upper() == "YES": #checks user input to see if they want to play again
        play_again = True   #if yes then they play again
    else:
        play_again = False  #if no then changes it to false so they dont play again
