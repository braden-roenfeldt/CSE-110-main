# W2 Prove: Assignment - madlibs
# Sister Hansen 9am
#Braden Roenfeldt



print("\nWELCOME TO MY MADLIBS")
print("How to Play:")
print("You will be given prompts asking for either a verb, adjective, or noun, etc.")
print("Type in each prompt correctly and enjoy the funny story with messed up words.")
input("Press 'Enter' to continue")
verb1 = input("Past tense verb: ")
verb1_1 = input("Present tense of verb you just entered: ")
verb2 = input("Untensed/Simple Verb: ")
verb3 = input("Untensed/Simple Verb: ")
verb4 = input("Past tense verb: ")
classname1 = input("Name of a class course: ")
adj1 = input("An adjective: ")
noun1 = input("A noun: ")
noun2 = input("A noun: ")
name1 = input("First name: ")


print("Here is your final Madlibs:\n")
print(f"On the way back from {classname1.title()} today I {verb1.lower()}, which caused me to {verb2.lower()}. A classmate named {name1.title()} saw me and proceded to {verb3.lower()}, so out of embarassment I ended up {verb1_1.lower()} again. Once I got out of there and made it back to my {noun1.lower()}, I {verb4.lower()} to calm my nerves. Once I calmed down I opened by {noun2.lower()} and realized my {adj1.lower()} {classname1.title()} homework had {verb4.lower()}.\n")