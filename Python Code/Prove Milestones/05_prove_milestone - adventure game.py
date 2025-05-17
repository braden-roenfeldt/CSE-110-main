#05 05 Prove: Milestone - Adventure Game
#Hansen, Kristi
#Braden Roenfeldt 9am


choice = input("\nWelcome to my choose your own adeventure game. You will be asked a series of questions about what you want to do.\nFor each of the things you are asked you will answer with a letter deciding on which thing you want to do. Have fun and don't die. Press enter to continue.")

choice = input("\nYou wake up and look at the time, realizing you are late for work, what do you do?\nA. GET READY FOR WORK AS NORMAL\nB. GET READY FOR WORK AS FAST AS YOU CAN.\n")
if choice.upper() == "A":
    choice = input("Taking your time to get to work you ended up getting there two hours late. Your boss starts to yell at you for being late. What do you do?\nA. YELL BACK AT THE MAN\nB. STAY SILENT WHILE HE BERATES YOU.")
    if choice.upper() == "A":
        print("uhoh.")
        choice == input("Your boss gets extreemly mad at you for talking back and grabs you by the collar. He takes you to the back of the building and throws you on the ground. What do you do?\nA. FIGHT BACK\nB. RUN FOR YOUR LIFE.")
        if choice.upper() == "A":
            print("Fighting back you end up beating him up till he passes out, however you are badly hurt and need to go home. Heading home you pass out in the car and crash. You died.")
        elif choice.upper() == "B":
            print("Running away from the fight your boss tries to follow you but you masterfully frogger across the street and get away from him. Now walking home you come across train tracks that you trip on and get knocked unconscious. You die. ")
        else:
            print("This wasn't  supposed to happen, restart and try again.")
            
    elif choice.upper() == "B":
        choice = input("Staying quiet he eventually walks away and you are now alone. What do you do?\nA. GET BACK TO WORK\nB. LEAVE AND GO HOME")
        if choice.upper() == "A":
            choice = input("Getting back to work you remember how much you hate your job and want to go home. Needing the money however you stay and keep working till your lunch break. What do you do on your lunch break.\nA. TAKE LUNCH AS NORMAL\nB. LEAVE WORK EARLY")
            if choice.upper() == "A":
                print("Getting back to work you feel like quiting but stick through it and finish your day.")
            elif choice.upper() == "B":
                print("As you get home from work you see a text on your phone saying that you are fired. Disapointed you now have to find a new job.")
            else:
                print("That wasn't supposed to happen, restart and try again")
        elif choice.upper() == "B":
            print("As you get home from work you see a text on your phone saying that you are fired. Disapointed you now have to ofind a new job.")
        else:
            print("That wasn't supposed to happen, restart and try again.")

    else:
        print("That wasn't supposed to happen, restart and try again.")


elif choice.upper() == "B":
    choice = input("Getting ready for work as fast as you can you make it there only ten minutes late. Sitting down at your desk you get to work and act like nothing happened. A few hours later you make it to your lunch break only to realize that you forgot your lunch. What do you do?\nA. TOUGH IT OUT AND GO WITH NO LUNCH\nB. ASK TO STEAL FROM A CO-WORKERS LUNCH\n")
    if choice.upper() == "A":
        choice = input("Toughing it out you finish off your work day and decide to leave the building. How do you decide to get home\nA. TAKE YOUR CAR AND DRIVE HOME\nB. DECIDE TO GET SOME EXERSICE AND WALK HOME\n")
        if choice.upper() == "A":
            print("Taking your car and driving home you pass out from the lack of food and crash the car.")
        elif choice.upper() == "B":
            print("You decide to get some exersice and take the senic route home, eventually you pass out from the lack of food and wake up in the middle of the forest. Lost and with no where to go you turn into a hobo living in the woods.")
        else:
            print("OH NO YOU GOT BEANED! THAT WASNT SUPPOSED TO HAPPEN")
    elif choice.upper() == "B":
        choice = input("Going to your next door co-worker you ask for a quick snack and suprisingly they give you two granola bars. What do you do next\nA. TRY FOR MORE FOOD FROM ANOTHER COWORKER\nB. SAY THANKS AND GO BACK TO WORK")
        if choice.upper() == "A":
            print("Going to another co-worker for more food you try another neighbor and they end up asking for your granola bars. You say no and sit back down eating your food.")
        elif choice.upper() == "B":
            print("Sitting back down you eat your granola bars and finish your day.")
        else:
            print("OH NO YOU'VE BEEN BEANED! THAT WASNT SUPPOSED TO HAPPEN")
    else:
        print("OH NO YOU'VE BEEN BEANED! THAT TOTALLY WAS SUPPOSED TO HAPPEN")
        print(choice)


else:
    print("OH NO YOU'VE BEEN BEANED! THAT WASNT SUPPOSED TO HAPPEN")