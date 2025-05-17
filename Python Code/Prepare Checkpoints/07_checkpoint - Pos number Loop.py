#07 Prepare: Checkpoint
#Hansen, Kristi 9am
#Braden Roenfeldt


num = -1
while num < 0:
    num = float(input("Please input a positive number: "))
    if num  < 0:
        print("\nThat wasn't a positive number, please try again.")
    else:
        print("Thank you!")