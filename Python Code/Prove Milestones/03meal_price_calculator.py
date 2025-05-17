#03 Prove: Milestone - Meal Price Calculator
#Hansen, Kristi
#Braden Roenfeldt 9am

print(f"\nMenu: Burger:$5.00      Kids Burger:$3.50\nMac and Cheese:$7.00     Kids Mac and Cheese:$5\n")
a_meal = float(input("Insert  the price of an adult meal:  $"))
c_meal = float(input("Insert the price of an child meal:  $"))
children = int(input("How many children are there? "))
adults = int(input("How many adults are there? "))
tax = float(input("What is your states tax rate (in percent)? "))
subtotal = ((a_meal*adults)+(c_meal*children))
sales_tax = (tax*.01)*subtotal
total = subtotal+sales_tax

print(f"\nSubtotal: ${subtotal:.2f}")
print(f"Sales Tax: ${sales_tax:.2f}")
print(f"Total: ${total:.2f}\n")

payment_amt =float(input("What is the payment amount? $"))
change = (payment_amt-total)
print(f"Change: ${change:.2f}")
print(f"Tell the customer to 'Enjoy your meal!'")