#08 Teach Team Activity
#Hansen, Kristi
#Braden Roenfeldt


word = "Commitment"

for letters in word:
    if letters.upper() == "M":
        letters = "_"
    print(f"{letters}", end="")


for spot, letter in enumerate(word):
    print(f"The letter {letter} is in place {spot}")
