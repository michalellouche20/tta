# Exercise 1: Currency class
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        return f'{self.amount} {self.currency}s'

    def __int__(self):
        return self.amount

    def __repr__(self):
        return f'{self.amount} {self.currency}s'

    def __add__(self, other):
        if isinstance(other, int):
            return Currency(self.currency, self.amount + other)
        elif isinstance(other, Currency) and self.currency == other.currency:
            return Currency(self.currency, self.amount + other.amount)
        else:
            raise TypeError(f'Cannot add between Currency type <{self.currency}> and <{other.currency}>')

    def __iadd__(self, other):
        if isinstance(other, int):
            self.amount += other
        elif isinstance(other, Currency) and self.currency == other.currency:
            self.amount += other.amount
        else:
            raise TypeError(f'Cannot add between Currency type <{self.currency}> and <{other.currency}>')
        return self

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(str(c1))  
print(int(c1))
print(repr(c1))  

print(c1 + 5) 
print(c1 + c2) 

print(c1) 
c1 += 5
print(c1)  

c1 += c2
print(c1)  




# Exercise 3
import string
import random

random_string = ''.join(random.choice(string.ascii_letters) for _ in range(5))
print(random_string)

# Exercise 4
from datetime import datetime

current_date = datetime.now()
print(current_date)

# Exercise 5
from datetime import datetime, timedelta

january_1st = datetime(current_date.year + 1, 1, 1)
time_left = january_1st - current_date
print(f'The 1st of January is in {time_left.days} days and {time_left.seconds // 3600}:{(time_left.seconds % 3600) // 60}:{time_left.seconds % 60} hours.')

# Exercise 6
def minutes_lived(birthdate):
    birth_datetime = datetime.strptime(birthdate, '1990-01-01')
    time_lived = current_date - birth_datetime
    return f'You have lived for {time_lived.days * 24 * 60} minutes.'

print(minutes_lived('1990-01-01'))

# Exercise 7
from faker import Faker

fake = Faker()

users = []

def add_user():
    user = {
        'name': fake.name(),
        'address': fake.address(),
        'language_code': fake.language_code()
    }
    users.append(user)

for _ in range(5):
    add_user()

print(users)