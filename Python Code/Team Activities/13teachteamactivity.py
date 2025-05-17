#13 Team Activity
#Hansen, Kristi 9am
#Braden Roenfeldt 


import math

def compute_squareArea(unit, dimension):
    """calls compute_rectangleArea"""
    return(compute_rectangleArea(unit, dimension, dimension))

def compute_rectangleArea(unit, dimension1, dimension2):
    """computes ares of rectangle and returns it"""
    return_val = (dimension1)*(dimension2)
    return(return_val)

def compute_circleArea(unit, radius):
    """Computes the area of circle and returns it"""
    return_val = (radius**2)*(math.pi)
    return(return_val)

units = ""
dim1 = ""
dim2 = ""

user_input = input("Welcome to the area calculator, press enter to continue or quit to exit the program")
while user_input.lower() != "quit":
    user_input = input(f"Type Square for square areas, Rectangle for rectangeles, Circle for circles, and quit to exit the program. ")
    if user_input.lower() == "square":
        units = input("\nWhat units are you working in? (inches, feet, etc.) ")
        dim1 = float(input("What is the side length of your square? "))
        returned = compute_squareArea(units, dim1)
        print(f"The area of your square is {returned:.2f} {units}^2.")
    if user_input.lower() == "rectangle":
        units = input("\nWhat units are you working in? (inches, feet, etc.) ")
        dim1 = float(input("What is one of the side lengths of your rectangle? "))
        dim2 = float(input("What is the other side length of your rectangle? "))        
        returned = compute_rectangleArea(units, dim1, dim2)
        if dim1 == dim2:
            print(f"The area of your square is {returned:.2f} {units}^2.")
        else:
            print(f"The area of your rectangle is {returned:.2f} {units}^2.")
    if user_input.lower() == "circle":
        units = input("\nWhat units are you working in? (inches, feet, etc.) ")
        dim1 = float(input("What is the radius of your circle? "))
        returned = compute_circleArea(units, dim1)
        print(f"The area of your circle is {returned:.2f} {units}^2.")
    
