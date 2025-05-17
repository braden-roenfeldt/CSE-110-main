#13 prepare checkpoint
#Hansen, Kristi 9am
#Braden Roenfeldt

import math
def windChillF(temp, wspeed):
    f = 35.74 + (.6215*temp) - (35.75*(wspeed**.16)) + (.4275 * temp * (wspeed**.16))
    print(f"The wind chill with an outside temp. of {temp} and wind speed of {wspeed}mph is {f:.2f} degrees.")


def windChillC(temp, wspeed):
    temp = (temp * (9/5) + 32)
    f = 35.74 + (.6215*temp) - (35.75*(wspeed**.16)) + (.4275 * temp * (wspeed**.16))
    print(f"The wind chill with an outside temp. of {temp}F and wind speed of {wspeed}mph is {f:.2f} degrees.")

def windChillK(temp, wspeed):
    f = 306.15 - ((.453843 * math.sqrt(wspeed)) + .464255 - (.0453843 * wspeed)) * (306.15*temp)
    print(f"The wind chill with an outside temp. of {temp} and wind speed of {wspeed} is {f:.2f} degrees.")

wspeed = 5
temp = float(input("What is the temprature you are looking at? "))
unit = input("What units are you measuring in? (F/C/K) ")

if unit.lower() == "f":
    while wspeed < 60:
        windChillF(temp, wspeed)
        wspeed += 5
elif unit.lower() == "c":
    while wspeed < 60:
        windChillC(temp, wspeed)
        wspeed += 5
elif unit.lower() == "k":
    while wspeed < 60:
        windChillK(temp, wspeed)
        wspeed += 5