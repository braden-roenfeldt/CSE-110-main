#11 Team Teach Activity
#Hansen, Kristi 9am
#Braden Roenfeldt

# any code we need to run after the file is closed

with open("hr_system.txt") as file_var:   # use with to open a file and store data in a variable (file object)
    header = next(file_var)         # if the file has a header line, skip it
    print(header)
    for line in file_var:           # read each line, one by one, into a loop variable (for loop)
        #print(line)
        line = line.strip()
        line_list = line.split(" ")            # split the current line into parts (into a list)
        name = line_list[0]                 # save different parts of the list into variables as needed
        id = line_list[1]
        title = line_list[2]
        salary = int(line_list[3])
        salary = salary/24        # do any calculations needed while still on a single line
        if title.upper() == "ENGINEER":
            salary += 1000
        print(f"Name: {name} (ID: {id}), Title: {title} - ${salary:.2F}")               # output (print) necessary items