#List Sum week 9/10prove
#Hansen, Kristi 9am
#Braden Roenfeldt


print("Hello, enter a number to complete an action.")
user_input = 0
grocery_ls = []
total_ls = []
list_sum = 0


while user_input != "5":      #while user has not input 0 it keeps asking for more numbers
    user_input = input("1. Add item to cart\n2. Remove item from cart\n3. View cart\n4. Find subtotal\n5. Exit\nEnter your choice here: ")
    if user_input == "1":   #used to check which choice they made 
        while user_input.upper() != "NO":   #used to loop through to add more than one item to list
            user_input = input("Enter your grocery item here: ")    #takes user input to append on next line
            grocery_ls.append(user_input)      #adds input to list
            user_input = float(input(f"What is the price of {user_input}: "))   #takes user input to append on next line
            total_ls.append(user_input)     #adds price to list
            user_input = input("Item added, would you like to another item? ")   #input to check if should loop

    if user_input == "3":
        print(f"\nYour grocery list is:")
        for i in range(len(grocery_ls)):
            print(f"{i+1}. {grocery_ls[i]} - ${total_ls[i]:.2f}")
        print()


    if user_input == "2":
        print(f"\nYour grocery list is:")
        for i in range(len(grocery_ls)):
            print(f"{i+1}. {grocery_ls[i]} - ${total_ls[i]:.2f}")
        user_input = int(input("Which item number would you like to remove? "))
        del(grocery_ls[user_input-1])
        del(total_ls[user_input-1])
        print(f"Item deleted\n")

    if user_input == "4":
        list_sum = 0    #sets  sum to zero to make sure changes from last time are not saved
        for num_loc in range(len(total_ls)):     #goes through each number in the list and adds it, also check if each number is bigger than the next
            list_sum += total_ls[num_loc]
        print(f"\nThe subtotal of your list is ${list_sum:.2f}\n")     #prints the total of the cost    
print("Goodbye")

