#Name List creation
#Hansen, Kristi 9am
#Braden Roenfeldt


name_list = []
user_input = None
user_input = input("Type in a name you know, enter 'end' to exit ")
while user_input.lower() != "end":
    name_list.append(user_input)   
    user_input = input("Type in a name you know, enter 'end' to exit ")
print(name_list)