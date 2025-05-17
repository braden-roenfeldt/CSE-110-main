#04 Teach: Team Activity
#Hansen, Kristi
#Braden Roenfeldt


import math
#v(t) = sqrt(mg/c) * (1 - exp((-sqrt(mgc)/m)t)) unedited equation

print("\nInput all your variables to find how fast something will fall. Units are in Kg, meters and seconds\n")
mass = float(input("Your objects mass: "))
time = float(input("Number of seconds you object will fall: "))
cross_area = float(input("Cross sectional area of your object: "))
drag_co = float(input("Closest approximation of your objects drag coefficient (.47-Sphere, .5-Cone, 1.05-Cube, .8-Angled Cube, .82-Long Cylinder, 1.15-Short Cylinder, .04-Streamlined Body, .09-Streamlined Half Body): "))
c = ((1.3*cross_area*drag_co)/2)

vel_time = math.sqrt((mass*9.8)/c) * (1-math.exp(-(math.sqrt(mass*9.8*c)/mass)*time))
print(f"\nYour objects velocity at {time} seconds will be approximatly: {vel_time:.3f} meters per second if your object is falling on Earth through air.")

c = ((1000*cross_area*drag_co)/2)
vel_time = math.sqrt((mass*9.8)/c) * (1-math.exp(-(math.sqrt(mass*9.8*c)/mass)*time))
print(f"\nIf your object is falling on Earth through water the then it will be moveing at ")

c = ((.02*cross_area*drag_co)/2)
vel_time = math.sqrt((mass*3.72)/c) * (1-math.exp(-(math.sqrt(mass*3.72*c)/mass)*time))
print(f"\nIf your object is falling on Mars then it will be moveing at {vel_time:.3f}")