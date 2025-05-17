# W2 Teach: Programming Activity
# Sister Hansen



print("Please enter the following information:")
f_name = input("First Name: ")
l_name = input("Last Name: ")
email_add = input("Email Address: ")
p_number = input("Phone Number: ")
job_title = input("Job Title:  ")
id_num = input("ID Number: ")
eye_color = input("Eye Color: ")
hair_color = input("Hair Color: ")

print("\n\nThe ID Card is:")
print("-"*20)
print(f"{l_name.upper()}, {f_name.title()}\nID: {id_num}\n{job_title.title()}\n\n{email_add}\n{p_number}\nEye: {eye_color.title()}\nHair: {hair_color.title():10}")
print("-"*20)