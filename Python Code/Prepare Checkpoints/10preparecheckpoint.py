#10 Prepare Checkpoint Shopping List
#Hansen, Kristi 9am
#Braden  Roenfeldt

shop_list = []
user_input = input("Please enter the items for your shopping list (type 'quit' to stop): ")
print(f"Item: {user_input}")
while user_input.upper() != "QUIT":
    shop_list.append(user_input)
    user_input = input("Enter your next item (type 'quit' to stop): ")
    print(f"Item: {user_input}")
print(f"\nYour shopping list is:")
for i in range(len(shop_list)):
    print(f"{i}: {shop_list[i]}")

user_input = input("Would you like to edit your list? ")
while user_input.upper() == "YES":
    user_input = input("Type change to change or delete to delete an item? ")
    if user_input.upper() == "CHANGE":
        list_num = int(input("Which item would you like to change? "))
        shop_list[list_num] = input("What would you like to change it to? ")
    if user_input.upper() == "DELETE":
        list_num = int(input("Which item would you like to delete? "))
        shop_list.pop(list_num)
    user_input = input("Continue editing? ")
print(f"\nYour new shopping list is:")
for i in range(len(shop_list)):
    print(f"{i}: {shop_list[i]}")