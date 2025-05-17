#06 Teach: Team Activity - Park Rides
#Hansen, Kristi
#Braden Roenfeldt 9am


rider1_age = int(input("What is the age of the rider? "))
rider1_height = int(input("What is the height of the rider (in inches)? "))
two_riders = input("Is there a second rider? (yes/no) ")
if two_riders.lower() == "yes":
    rider2_age = int(input("What is the age of the second rider? "))
    rider2_height = int(input("What is the height of the second rider (in inches)? "))
    if rider1_height or rider2_age < 36:
        print("Sorry, you are too short to ride this ride.")
    elif (rider1_age or rider2_age >= 18) and (rider1_height or rider2_height >= 36):
        print("Enjoy the ride together.")
elif rider1_height < 36:
    print("Sorry, you are too short to ride this ride.")
elif rider1_age >= 18 and rider1_height >=62:
    print("Enjoy the Ride by yourself.")
elif rider1_age < 18 and rider1_height >=62:
    print("Sorry you are too young to ride alone.")
elif rider1_age >= 18 and rider1_height < 62:
    print("Sorry you are too short to ride alone.")
else:
    print("Sorry, there must have been an error")