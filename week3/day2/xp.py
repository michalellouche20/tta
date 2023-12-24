# Exercise 1

class Pets:
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat:
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Siamese(Cat):
    pass

bengal_cat = Bengal('BengalCat', 3)
chartreux_cat = Chartreux('ChartreuxCat', 4)
siamese_cat = Siamese('SiameseCat', 2)

all_cats = [bengal_cat, chartreux_cat, siamese_cat]

sara_pets = Pets(all_cats)

sara_pets.walk()
# Exercise 2

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f'{self.name} is barking'

    def run_speed(self):
        return self.weight / self.age * 10

    def fight(self, other_dog):
        if self.run_speed() * self.weight > other_dog.run_speed() * other_dog.weight:
            return f'{self.name} won the fight!'
        elif self.run_speed() * self.weight < other_dog.run_speed() * other_dog.weight:
            return f'{other_dog.name} won the fight!'
        else:
            return 'It was a draw!'

dog1 = Dog('Buddy', 3, 25)
dog2 = Dog('Max', 4, 30)
dog3 = Dog('Charlie', 2, 20)

print(dog1.bark())
print(dog1.run_speed())
print(dog1.fight(dog2))

# Exercise 3

class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        bark_output = self.bark()
        self.trained = True
        return bark_output

    def play(self, *dog_names):
        return f'{", ".join(dog_names)} all play together.'

    def do_a_trick(self):
        if self.trained:
            import random
            tricks = [
                f'{self.name} does a barrel roll.',
                f'{self.name} stands on his back legs.',
                f'{self.name} shakes your hand.',
                f'{self.name} plays dead.'
            ]
            return random.choice(tricks)
        else:
            return f'{self.name} is not trained yet.'

pet_dog = PetDog('Buddy', 3, 25)

print(pet_dog.train())
print(pet_dog.play('Max', 'Charlie'))
print(pet_dog.do_a_trick())

# Exercise 4

class Family:
    def __init__(self, last_name, members):
        self.last_name = last_name
        self.members = members

    def born(self, **kwargs):
        self.members.append(kwargs)
        print(f"Congratulations! New family member born.")

    def is_18(self, name):
        for member in self.members:
            if member['name'] == name:
                return member['age'] >= 18
        return False

    def family_presentation(self):
        print(f"{self.last_name}'s family")
        for member in self.members:
            print(f"Name: {member['name']}, Age: {member['age']}, Gender: {member['gender']}, Child: {member['is_child']}")

family_members = [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
]

family_instance = Family("Smith", family_members)
family_instance.born(name='Baby', age=0, gender='Unknown', is_child=True)

family_instance.family_presentation()
print(f"Is Michael over 18? {family_instance.is_18('Michael')}")

# Exercise 5

class TheIncredibles(Family):
    def __init__(self, last_name, members):
        super().__init__(last_name, members)

    def use_power(self, name):
        for member in self.members:
            if member['name'] == name and member['age'] >= 18:
                return f"{member['name']}'s power: {member['power']}"
            elif member['name'] == name and member['age'] < 18:
                raise ValueError(f"{member['name']} is not over 18 years old.")

    def incredible_presentation(self):
        print(f"*Here is our powerful family**")
       