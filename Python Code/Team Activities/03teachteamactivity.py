#03 Teach: Team Activity
#Hansen, Kristi 9am
#Braden Roenfeldt

import math
units = input("What units are you working with? (inches, ft. etc.): ")
s_side = input("What is the side length of your square? ")
s_side = float(s_side)
print(f"The area of your square is {s_side**2} {units}\n")

units = input("What units are you working with? (inches, ft. etc.): ")
r_side1 = input("What is the width of your rectangle? ")
r_side1 = float(r_side1)
r_side2 = input("What is the length of your rectangle? ")
r_side2 = float(r_side2)
print(f"The area of your rectangle is {r_side1*r_side2} {units}.\n")

units = input("What units are you working with? (inches, ft. etc.): ")
rad = input("What is the radius of your circle? ")
rad = float(rad)
print(f"The area of your circle is {(rad**2)*(math.pi)} {units}^2.")
