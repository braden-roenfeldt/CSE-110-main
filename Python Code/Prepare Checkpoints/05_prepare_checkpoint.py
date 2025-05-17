#05 Prepare: Checkpoint - Interger comparator
#Hansen, Kristi
#Braden Roenfeldt 9am


num1 = int(input("Give me an integer: "))
num2 = int(input("Give me another integer: "))
if num1 > num2 :
    print(f"Guess what, {num1} is greater than {num2}.")
elif num2 > num1 :
    print(f"Guess what, {num2} is greater than {num1}.")
else:
    print(f"This may suprise you but the numbers you gave me are the same size.\n\n")

animal1 = input("Hey, also what is your favorite animal? ")
animal2 = "owl"
if animal1.lower() != animal2 :
    print(f"Well thats sad, we don't share a favorite animal.")
    print(f"Mine is an {animal2}")
else:
    print(f"No way! A {animal1} is my favorite animal too.")