#10 Team Activity - Multiple Lists
#Hansen, Kristi 9am
#Braden  Roenfeldt


acc_name = []
acc_balc = []
user_input = input("What is the name of this account? ")
while user_input.upper() != "QUIT":
    acc_name.append(user_input)
    user_input = float(input("What is the amount of money in the account? "))
    acc_balc.append(user_input)
    user_input = input("What is the name of this account? ")
print("\nAccount information:")
for i in range(len(acc_balc)):
    print(f"{acc_name[i]} - ${acc_balc[i]}")
total = 0
for i in range(len(acc_balc)):
    total += acc_balc[i]
print(f"\nTotal balance between all accounts: ${total}")
print(f"Average balance between all accounts: ${total/len(acc_balc)}")