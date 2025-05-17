#07 Prepare: Checkpoint
#Hansen, Kristi 9am
#Braden Roenfeldt


candy = "no"
while candy.lower() == "no":
    candy = input("Please can I have a piece of candy? ")
    if candy.lower() == "yes":
        print("Thank you!")
    else:
        candy = "no"