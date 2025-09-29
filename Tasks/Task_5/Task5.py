# Task 1: Collect popular Nigerian dishes and display them
print("\n--- Task 1: Nigerian dishes ---")
dish_1 = input("Enter a Nigerian dish: ").strip()
dish_2 = input("Enter another Nigerian dish: ").strip()
dish_3 = input("Enter one more Nigerian dish: ").strip()

dishes_list = [dish_1, dish_2, dish_3]
dish_tuple = tuple(dishes_list)
print("You entered these dishes:")
print("\n".join(dish_tuple))

# Task 2: Friends (expecting 5 names separated by spaces or commas)
print("\n--- Task 2: Friends ---")
friends_input = input(
    "Enter your 5 best friends' names (separate by space or comma): ").replace(',', ' ').split()
if len(friends_input) < 5:
    print("You provided fewer than 5 names; continuing with the ones given.")
friends_tuple = tuple(friends_input)
print("Friends in reverse order:", friends_tuple[::-1])

# Task 3: Nigerian states
print("\n--- Task 3: Nigerian states ---")
states = []
for i in range(1, 6):
    s = input(f"Enter Nigerian state #{i}: ").strip()
    states.append(s)
state_list = tuple(states)
print(f"First state: {state_list[0]}\nLast state: {state_list[-1]}")
print("Is 'Lagos' in the list?", any(
    st.lower() == 'lagos' for st in state_list))
print("Number of states entered:", len(state_list))

# Task 4: Basic user info display
print("\n--- Task 4: User info ---")
first_name = input('Please enter your first name: ').strip()
age = input('Please enter your age: ').strip()
fav_color = input('Please enter your favourite color: ').strip()
hometown = input('Please enter your home town: ').strip()
user_list = [first_name, age, fav_color, hometown]
print('\nCollected info:', user_list)
print('-----------------------')
print(f"First name: \t| {first_name}")
print(f"Age: \t\t| {age}")
print(f"Color: \t\t| {fav_color}")
print(f"Home town: \t| {hometown}")

# Task 5: Shopping list
print("\n--- Task 5: Shopping list ---")
item_list = []
for i in range(1, 6):
    item = input(f"Enter shopping list item #{i}: ").strip()
    item_list.append(item)
print("Your shopping list:", item_list)
