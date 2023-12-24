
# Exercise 1: Set
my_fav_numbers = {3, 7, 21}
my_fav_numbers.add(42)
my_fav_numbers.add(8)
my_fav_numbers.remove(8)

friend_fav_numbers = {5, 7, 11, 21}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)

# Exercise 2: Tuple


# Exercise 3: List
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0, "Apples")
apples_count = basket.count("Apples")
basket.clear()
print(basket)

# Exercise 4: Floats

float_sequence = [1.5 + i * 0.5 for i in range(8)]
# Another way to generate a sequence of floats: list(range(15, 51, 5))/10

# Exercise 5: For Loop
for i in range(1, 21):
    print(i)

for i in range(1, 21, 2):
    print(i)

# Exercise 6: While Loop
user_name = "Michal"  
while True:
    user_input = input("Enter your name: ")
    if user_input == user_name:
        break

# Exercise 7: Favorite Fruits
favorite_fruits_str = input("Enter your favorite fruit(s) separated by a space: ")
favorite_fruits = favorite_fruits_str.split()

user_input_fruit = input("Enter a fruit: ")
if user_input_fruit in favorite_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy.")

# Exercise 8: Who Ordered A Pizza?
topping_list = []
while True:
    topping = input("Enter a pizza topping (type 'quit' to finish): ")
    if topping.lower() == 'quit':
        break
    print(f"Adding {topping} to your pizza.")
    topping_list.append(topping)

print("Toppings on the pizza:", ', '.join(topping_list))
total_price = 10 + 2.5 * len(topping_list)
print("Total price:", total_price)

# Exercise 9: Cinemax
family_tickets = []
while True:
    age_str = input("Enter the age of a person (type 'done' to finish): ")
    if age_str.lower() == 'done':
        break
    age = int(age_str)
    if age < 3:
        ticket_price = 0
    elif 3 <= age <= 12:
        ticket_price = 10
    else:
        ticket_price = 15
    family_tickets.append(ticket_price)

total_cost = sum(family_tickets)
print("Total cost for the family's tickets:", total_cost)

teenagers = ["Alice", "Bob", "Charlie", "David"]
allowed_teens = []
for teen in teenagers:
    age_str = input(f"Enter the age of {teen}: ")
    age = int(age_str)
    if 16 <= age <= 21:
        allowed_teens.append(teen)

print("Final list of allowed teenagers:", allowed_teens)

# Exercise 10: Sandwich Orders
sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]

while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")

finished_sandwiches = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"I made your {current_sandwich}")
    finished_sandwiches.append(current_sandwich)

print("\nSandwiches that were made:")
for sandwich in finished_sandwiches:
    print(sandwich)