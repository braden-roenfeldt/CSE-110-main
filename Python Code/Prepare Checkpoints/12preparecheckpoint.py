#12 prepare checkpoint
#Hansen, Kristi
#Braden Roenfeldt


people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]
comp_age = 999
youngest = ""
for line in people:
    line = line.strip()
    line_list  = line.split(" ")
    name = line_list[0]
    age = int(line_list[1])
    if comp_age >= age:
        comp_age = age
        youngest = name
print(f"{youngest} {comp_age}")