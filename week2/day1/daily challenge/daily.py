user= input("Enter a string of 10 characters:")
if len(user)<10:
    print('string not long enough')
elif len (user)>10:
    print('string too long')
else :
    print ('Perfect string')
print (user[0], user [-1])

print("\nConstruction de la chaîne caractère par caractère:")
for i in range(1, len(user) + 1):
        print(user[:i])

    # Bonus: Shuffle some characters and print the scrambled string
import random
shuffled_chars = list(user)
random.shuffle(shuffled_chars)
scrambled_string = ''.join(shuffled_chars)
print("\nChaîne nouvellement brouillée:", scrambled_string)