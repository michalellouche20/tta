def display_message():
    print("I am learning Python in this course.")

display_message()
#Exercise 2

def favorite_book(title):
    print(f"One of my favorite books is {title}.")

favorite_book("Alice in Wonderland")

#Exercise 3

def describe_city(city, country="Unknown"):
    print(f"{city} is in {country}.")

describe_city("Reykjavik", "Iceland")

#Exercise 4: Random

import random

def random_number_comparison(user_number):
    random_number = random.randint(1, 100)

    print(f"Your number: {user_number}")
    print(f"Random number: {random_number}")

    if user_number == random_number:
        print("Congratulations! You guessed the right number.")
    else:
        print("Sorry, better luck next time.")

user_number = int(input("Enter a number between 1 and 100: "))
random_number_comparison(user_number)

#Exercise 5

def make_shirt(size="large", text="I love Python"):
    print(f"The size of the shirt is {size} and the text is '{text}'.")

make_shirt()
make_shirt("medium")
make_shirt("small", "Python is fun!")

make_shirt(text="Hello World", size="medium")

#Exercise 6
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians():
    for magician in magician_names:
        print(magician)

def make_great():
    for i in range(len(magician_names)):
        magician_names[i] = "the Great " + magician_names[i]

show_magicians()
make_great()
show_magicians()
#Exercise 7

import random

def get_random_temp(season):
    if season == 'winter':
        return random.randint(-10, 16)
    elif season == 'spring':
        return random.randint(0, 23)
    elif season == 'summer':
        return random.randint(24, 40)
    elif season == 'autumn' or season == 'fall':
        return random.randint(0, 16)

def main():
    season = input("Enter the season (winter, spring, summer, autumn/fall): ")
    temp = get_random_temp(season)
    print(f"The temperature right now is {temp} degrees Celsius.")

    if temp < 0:
        print("Brrr, that’s freezing! Wear some extra layers today.")
    elif 0 <= temp <= 16:
        print("Quite chilly! Don’t forget your coat.")
    elif 16 < temp <= 23:
        print("It's mild and pleasant.")
    elif 24 <= temp <= 32:
        print("Warm weather! Enjoy your day.")
    elif 32 < temp <= 40:
        print("It's hot! Stay hydrated.")

main()
#Exercise 8

import random

def star_wars_quiz():
    data = [
        {"question": "What is Baby Yoda's real name?", "answer": "Grogu"},
        {"question": "Where did Obi-Wan take Luke after his birth?", "answer": "Tatooine"},
        {"question": "What year did the first Star Wars movie come out?", "answer": "1977"},
        {"question": "Who built C-3PO?", "answer": "Anakin Skywalker"},
        {"question": "Anakin Skywalker grew up to be who?", "answer": "Darth Vader"},
        {"question": "What species is Chewbacca?", "answer": "Wookiee"}
    ]

    correct_answers = 0
    wrong_answers = []

    for question_data in data:
        question = question_data["question"]
        answer = question_data["answer"]
        user_answer = input(f"{question} Answer: ")

        if user_answer.lower() == answer.lower():
            correct_answers += 1
        else:
            wrong_answers.append({"question": question, "user_answer": user_answer, "correct_answer": answer})

    print(f"\nYou got {correct_answers} correct answers and {len(wrong_answers)} wrong answers.")

    if len(wrong_answers) > 3:
        print("You had more than 3 wrong answers. You may want to play again.")

    if wrong_answers:
        print("\nIncorrect answers:")
        for wrong_answer in wrong_answers:
            print(f"Q: {wrong_answer['question']}\nYour Answer: {wrong_answer['user_answer']}\nCorrect Answer: {wrong_answer['correct_answer']}\n")

star_wars_quiz()