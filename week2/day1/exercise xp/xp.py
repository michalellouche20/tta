# Exercise 1
print("Hello world\n" * 4)

# Exercise 2
result = (99**3) * 8
print(result)

# Exercise 3
print(5 < 3)
print(3 == 3)
print(3 == "3")
print(3 > 3)
print("Hello" == "hello")

# Exercise 4
computer_brand = "Asus"  
print(f"I have a {computer_brand} computer")

# Exercise 5
name = "Michal" 
age = 25 
shoe_size = 38 

info = f"My name is {name}. I am {age} years old, and my shoe size is {shoe_size}."
print(info)

# Exercise 6
b = 10  

if a > b:
    print("Hello World")

# Exercise 7: Odd Or Even
user_number = int(input("Enter a number: "))
if user_number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# Exercise 8
user_name = input("What is your name? ")
if user_name.lower() == name.lower():
    print("Wow, we have the same name! What a coincidence!")
else:
    print(f"Nice to meet you, {user_name}!")

# Exercise 9
height_inches = float(input(2.54))
min_height_cm = 145  


if height_inches * 2.54 > min_height_cm:
    print("You are tall enough to ride the roller coaster. Enjoy the ride!")
else:
    print("Sorry, you need to grow some more to ride the roller coaster.")