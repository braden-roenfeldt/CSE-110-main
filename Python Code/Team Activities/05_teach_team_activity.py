#05 Teach: Team Activity - Grade Calculator
#Hansen, Kristi
#Braden Roenfeldt 9am


user_percent_grade = float(input("What is your grade percentage for the class? "))
user_letter_grade = "F"
if user_percent_grade >= 90:
    user_letter_grade = "A"
elif user_percent_grade >= 80:
    user_letter_grade = "B"
elif user_percent_grade >=70:
    user_letter_grade = "C"
elif user_percent_grade >= 60:
    user_letter_grade = "D"
else:
    user_letter_grade = "F"

if user_letter_grade <= "C": #C is greater than other letters because it occurs later in the alphabet, if it is earlier than in the alphabet it is less than
    print(f"Your letter grade is {user_letter_grade}")
    print(f"Your percent grade is {user_percent_grade}%")
    print(f"Congrats! You passed the class!")
else:
    print(f"Your letter grade is {user_letter_grade}")
    print(f"Your percent grade is {user_percent_grade}%")
    print(f"I'm sorry. You didn't pass the class.")