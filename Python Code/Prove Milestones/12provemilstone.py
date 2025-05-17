#12 Prove Milestone - Year Analysis
#Hansen, Kristi 9am
#Braden Roenfeldt


print("Note: If we have no data on the year you input then the life expectancy will show as 0 and 9999")
user_input = int(input("What year are you interested in? "))
with open("life-expectancy.csv") as life_exp:
    header = next(life_exp)
    bigsize_comp = 0
    smallsize_comp = 9999
    yearbsize = 0
    yearssize = 9999
    blife_country =""
    blife_year = 0
    slife_country =""
    slife_year = 0
    buser_country = ""
    suser_country = ""
    #print(header)
    """
    #check text file for missing years and add in code so the user input cant be set to it
    """
    for line in life_exp:
        line = line.strip()
        line_list = line.split(",")
        Entity = line_list[0]
        Code = line_list[1]
        Year = int(line_list[2])
        Life = float(line_list[3])
        if bigsize_comp <= Life:
            bigsize_comp = Life     #finds the biggest life expectancy
            blife_year = Year
            blife_country = Entity
        if smallsize_comp >= Life:
            smallsize_comp = Life       #finds the smallest life expectancy
            slife_year = Year
            slife_country = Entity
        if user_input == Year:
            if yearbsize <= Life:
                yearbsize = Life     #finds the biggest life expectancy
                buser_country = Entity
            if yearssize >= Life:
                yearssize = Life       #finds the smallest life expectancy
                suser_country = Entity
    if yearssize == 9999 and yearbsize == 0:
        print("Sorry we don't have any data on the year you input.")
    if yearssize != 9999:
        print(f"The greatest life expectancy is in {blife_country} years at {bigsize_comp} in the year {blife_year}")
        print(f"The smallest life expectancy is in {slife_country} years at {smallsize_comp} in the year {slife_year}")

        print(f"In the year {user_input} the highest life expectancy came from {buser_country} with a life expectancy of {yearbsize}")
        print(f"In the year {user_input} the lowest life expectancy came from {suser_country} with a life expectancy of {yearssize}")