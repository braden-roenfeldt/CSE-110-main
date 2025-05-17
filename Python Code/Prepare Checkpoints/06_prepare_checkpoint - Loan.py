#06 Prepare: Checkpoint
#Hansen, Kristi
#Braden Roenfeldt

input("Hello welcome to the Loan Qualifier, you will be asked multiple questions, answer them and see if you qualify for a loan. Press enter to continue. ")
loan_size = int(input("On a scale of 1-10 how large is your loan? "))
qualify = False

if loan_size >= 5: 
    cred_hist = int(input("On a scale of 1-10 how good is your credit history? "))
    income = int(input("On a scale of 1-10 how high is your income? "))
    down_pay = int(input("On a scale of 1-10 how large is your down payment? "))
    if cred_hist and income >= 7:
        qualify = True
        print(f"You qualify for a loan! Please call us and we can discuss your loan further.")
    elif (cred_hist >= 7 or income >= 7) and down_pay >= 5:
        qualify = True
        print(f"You qualify for a loan! Please call us and we can discuss your loan further.")
    else :
        qualify = False
        print(f"Sorry, you do not qualify for a loan, please try again another time.")
elif loan_size < 5:
    if loan_size < 4:
        qualify = False
        print(f"Sorry, you do not qualify for a loan, please try again another time.")
    elif loan_size < 5-----------
else :
        qualify = False
        print(f"Sorry, you do not qualify for a loan, please try again another time.")


down_pay = int(input("On a scale of 1-10 how large is your down payment? "))
