#List Sum
#Hansen, Kristi 9am
#Braden Roenfeldt


print("Hello, enter any number and create your number list, use zero to exit.")
user_input = int(input("Enter your number here: "))
number_list = []
list_sum = 0
big_num = 0
avg = 0

while user_input != 0:      #while user has not input 0 it keeps asking for more numbers
    number_list.append(user_input)      #adds input to list
    user_input = int(input("Enter your number here: "))
print(f"Your list of numbers is: {number_list}.")

for num_loc in range(len(number_list)):     #goes through each number in the list and adds it, also check if each number is bigger than the next
    list_sum += number_list[num_loc]
    if number_list[num_loc] >= big_num:     #big number check
        big_num = number_list[num_loc]
avg = list_sum/len(number_list)    #takes the average of the numbers

print(f"Your list was {len(number_list)} numbers long.")
print(f"The sum of all numbers in your list is {list_sum}")
print(f"The biggest number in your list was {big_num}.")
print(f"The average of your numbers was {avg}.")
number_list.sort()
print(f"The sorted list is {number_list}.")